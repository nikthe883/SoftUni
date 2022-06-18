employee_one = int(input())
employee_two = int(input())
employee_three = int(input())
students = int(input())
total_hours = 0

for hours in range(1, students + 1):
    if students <= 0:
        break
    total_hours += 1
    if total_hours % 4 == 0:
        pass
    else:
        students -= employee_one + employee_two + employee_three

print(f"Time needed: {total_hours}h.")
