
n = int(input())

num_list = []

for i in range(n):
    num = int(input())
    num_list.append(num)

max_number = max(num_list)
res_numbers = sum(num_list) - max_number
diff = abs(res_numbers - max_number)

if max_number == res_numbers:
    print(f"Yes\n"
          f"Sum = {max_number}")
else:
    print(f"No\n"
          f"Diff = {diff}")



