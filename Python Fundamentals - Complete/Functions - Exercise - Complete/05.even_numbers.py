user_input = input().split(" ")
user_input = [int(x) for x in user_input]
check = lambda a: int(a) % 2 == 0

result = list(filter(check, user_input))
print(result)
