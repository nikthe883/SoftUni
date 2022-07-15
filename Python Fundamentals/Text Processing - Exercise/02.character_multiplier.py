user_input = input().split(" ")

result = 0
if len(user_input[0]) == len(user_input[1]):
    for i in range(len(user_input[0])):
        result += ord(user_input[0][i]) * ord(user_input[1][i])
elif len(user_input[0]) > len(user_input[1]):
    diff = len(user_input[1]) - len(user_input[0])
    for i in range(len(user_input[1])):
        result += ord(user_input[0][i]) * ord(user_input[1][i])

    for i in range(len(user_input[0]) + diff, len(user_input[0])):
        result += ord(user_input[0][i])
else:
    diff = len(user_input[0]) - len(user_input[1])
    for i in range(len(user_input[0])):
        result += ord(user_input[0][i]) * ord(user_input[1][i])

    for i in range(len(user_input[1]) + diff, len(user_input[1])):

        result += ord(user_input[1][i])

print(result)
