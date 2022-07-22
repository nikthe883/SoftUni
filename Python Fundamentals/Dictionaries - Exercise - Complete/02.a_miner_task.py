user_input = input()
dct = {}

while user_input != "stop":
    event = user_input
    quantity = int(input())

    if event not in dct:
        dct[event] = 0
    dct[event] += quantity

    user_input = input()

for key, value in dct.items():
    print(f"{key} -> {value}")
