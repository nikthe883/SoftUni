
number_opened_tabs = int(input())
monthly_salary = int(input())

fine = 0

for i in range(number_opened_tabs):
    open_tabs = input()
    if open_tabs == "Facebook":
        fine += 150
    elif open_tabs == "Instagram":
        fine += 100
    elif open_tabs == "Reddit":
        fine += 50

if fine >= monthly_salary:
    print("You have lost your salary.")

else:
    salary_left = monthly_salary - fine
    print(salary_left)
