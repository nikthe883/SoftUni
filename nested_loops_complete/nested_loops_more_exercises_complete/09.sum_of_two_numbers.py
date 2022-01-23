
start = int(input())
end = int(input())
magic = int(input())

combination = 0
is_comb = False

for num1 in range(start, end + 1):
    for num2 in range(start, end + 1):
        combination += 1
        if num1 + num2 == magic:
            is_comb = True
            print(f"Combination N:{combination} ({num1} + {num2} = {magic})")


    if is_comb:
        break

if not is_comb:
    print(f"{combination} combinations - neither equals {magic}")
