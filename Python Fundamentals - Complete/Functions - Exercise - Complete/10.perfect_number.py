def perfect_number(n):
    total_sum = 0
    for x in range(1, n):
        if n % x == 0:
            total_sum += x
    return total_sum == n


user_input = int(input())

check_number = perfect_number(user_input)
if check_number:
    print('We have a perfect number!')
else:
    print("It's not so perfect.")
