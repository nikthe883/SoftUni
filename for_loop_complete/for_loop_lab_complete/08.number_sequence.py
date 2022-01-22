

n = int(input())

numbers_list = []

for i in range(n):
    number = int(input())
    numbers_list.append(number)

print(f"Max number: {max(numbers_list)}\n"
      f"Min number: {min(numbers_list)}")
