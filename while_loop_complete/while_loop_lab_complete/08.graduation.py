student_name = input()

graduate_date = 1
average_grade = 0
strikes = 0


while graduate_date <= 12 and strikes != 2:

    grade = float(input())

    if grade >= 4:
        graduate_date += 1
        average_grade += grade
    else:
        strikes += 1

if strikes < 2:
    average_grade = average_grade / 12
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
else:
    print(f"{student_name} has been excluded at {graduate_date} grade")
