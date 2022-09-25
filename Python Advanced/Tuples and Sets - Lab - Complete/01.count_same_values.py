user_input = tuple(input().split())
numbers = []
for i in user_input:
    if i not in numbers:
        print(f"{float(i):.1f} - {user_input.count(i)} times")
        numbers.append(i)
