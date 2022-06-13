user_input = input().split(" ")
user_input = [int(x) for x in user_input]

minimal = lambda a: min(a)
maximum = lambda a: max(a)
suming = lambda a: sum(a)


print(f"The minimum number is {minimal(user_input)}\n"
      f"The maximum number is {maximum(user_input)}\n"
      f"The sum number is: {suming(user_input)}\n")
