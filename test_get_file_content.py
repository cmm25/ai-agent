from functions.get_file_content import get_file_content

returned_string = get_file_content("calculator", "lorem.txt")

print(f"lorem.txt length: {len(returned_string)}")
print(f"lorem.txt truncated: {'truncated' in returned_string}")
print(get_file_content("calculator", "lorem.txt"))

print (get_file_content("calculator", "main.py"))
print (get_file_content("calculator", "pkg/calculator.py"))
print (get_file_content("calculator", "/bin/cat")) 
print (get_file_content("calculator", "pkg/does_not_exist.py"))
