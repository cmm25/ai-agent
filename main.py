import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse

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
            "role": "user",
            "content": args.user_prompt },
]



client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)

response = client.chat.completions.create(
    model="openrouter/free",
    messages=messages,
)

print(response.choices[0].message.content)
if args.verbose:    
    print("User prompt:",args.user_prompt )
    print("Prompt tokens:", response.usage.prompt_tokens)
    print("Response tokens:", response.usage.completion_tokens)