
begin_num1 = int(input())
begin_num2 = int(input())
end_num1 = int(input())
end_num2 = int(input())

for num1 in range(begin_num1, begin_num1 + end_num1 + 1):
    for num2 in range(begin_num2, begin_num2 + end_num2 + 1):
        if num1 % 2 !=0 and num1 % 3 != 0 and num1 % 5 != 0 and num1 % 7 != 0:
            if num2 % 2 != 0 and num2 % 3 != 0 and num2 % 5 != 0 and num2 % 7 != 0:
                print(f"{num1}{num2}")
