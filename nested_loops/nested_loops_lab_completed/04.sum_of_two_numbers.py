
begin = int(input())
end = int(input())
magic_number = int(input())
combination = 0
success = False

for x in range(begin, end + 1):
    for y in range(begin, end + 1):
        combination += 1
        if x + y == magic_number:
            print(f"Combination N:{combination} ({x} + {y} = {magic_number})")
            success = True
        break


if not success:
    print(f"{combination} combinations - neither equals {magic_number}")
