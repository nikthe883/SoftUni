number_painted_eggs = int(input())

red = 0
orange = 0
blue = 0
green = 0

for i in range(number_painted_eggs):
    color = input()
    if color == "red":
        red += 1
    elif color == "orange":
        orange += 1
    elif color == "blue":
        blue += 1
    elif color == "green":
        green += 1

print(f"Red eggs: {red}\n"
      f"Orange eggs: {orange}\n"
      f"Blue eggs: {blue}\n"
      f"Green eggs: {green}")

max_painted_eggs = max(red, orange, blue, green)

egg = [red, orange, blue, green]
dye = ["red", "orange", "blue", "green"]

for i, v in enumerate(egg):
    if v == max_painted_eggs:
        print(f"Max eggs: {v} -> {dye[i]}")
        break
