user_input = input().split(" ")
user_input = [int(x) for x in user_input]

average = sum(user_input) / len(user_input)


numbers = []
for i in user_input:
    if i > average:
        numbers.append(i)


numbers.sort(reverse=True)
if len(numbers) < 1:
    print("No")
else:
    print(" ".join(str(x) for x in numbers[:5]))
