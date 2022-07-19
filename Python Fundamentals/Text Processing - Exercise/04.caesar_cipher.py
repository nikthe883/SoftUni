user_input = input()

output = ""

for char in user_input:
    output += chr(ord(char) + 3)
print(output)

output = [chr(ord(char) + 3) for char in user_input ]
print("".join(output))