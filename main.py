import os
import json
import argparse
import sys

from dotenv import load_dotenv
from openai import OpenAI

from functions.call_function import call_function
from prompts import system_prompt
from functions.function_schemas import available_functions

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

#create the parser 
parser = argparse.ArgumentParser(description="My ai agent")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

#llm messages description list
messages=[
            {
                    "role":"system",
                    "content":system_prompt },
        {
            "role": "user",
            "content": args.user_prompt },
]



client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)
for _ in range(20):
    try:
        response = client.chat.completions.create(
            model="openrouter/free",
            messages=messages,
            temperature=0,
            tools=available_functions
        )


        message = response.choices[0].message
        messages.append(message)

        if message.tool_calls:
            for tool_call in message.tool_calls:
                result_message = call_function(tool_call, args.verbose)
                function_args = json.loads(tool_call.function.arguments or "{}")
                if not result_message["content"]:
                    raise Exception("should always have content")
                if args.verbose:
                    print(f"-> {result_message['content']}")

                messages.append(result_message)
        print(message.content)
    except Exception as e :
        print("Error: agent did not finish within 20 iterations", file=sys.stderr)
        print(f"Error: {e}")
if args.verbose:    
    print("User prompt:",args.user_prompt )
    print("Prompt tokens:", response.usage.prompt_tokens)
    print("Response tokens:", response.usage.completion_tokens)