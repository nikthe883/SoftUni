
count_number = int(input())

num1 = []


for i in range(count_number * 2):

    number = int(input())
    num1.append(number)

left_side = num1[:count_number]
right_side = num1[count_number:]

if sum(left_side) == sum(right_side):
    print(f"Yes, sum = {sum(left_side)}")

else:
    diff = abs(sum(left_side) - sum(right_side))
    print(f"No, diff = {diff}")
