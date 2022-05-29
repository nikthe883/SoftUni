n = int(input())

user_inputs = []
for _ in range(n):
    user_input = int(input())
    user_inputs.append(user_input)

command = input()
if command == "even":
    print([x for x in user_inputs if x % 2 == 0])
elif command == "odd":
    print([x for x in user_inputs if x % 2 != 0])
elif command == "negative":
    print([x for x in user_inputs if x < 0])
else:
    print([x for x in user_inputs if x >= 0])
