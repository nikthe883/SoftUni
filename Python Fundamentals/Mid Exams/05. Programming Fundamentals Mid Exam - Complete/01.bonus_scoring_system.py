from math import ceil

number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus_points = int(input())

max_bonus_points = 0
student = 0

for i in range(number_of_students):
    student_attendances = int(input())
    total_bonus = student_attendances / number_of_lectures * (5 + additional_bonus_points)

    if total_bonus > max_bonus_points:
        max_bonus_points = total_bonus
        student = student_attendances

print(f"Max Bonus: {ceil(max_bonus_points)}.\n"
      f"The student has attended {student} lectures.")