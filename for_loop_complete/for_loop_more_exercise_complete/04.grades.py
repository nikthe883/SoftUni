
number_students = int(input())

top_students = 0
between_four_and_five = 0
between_three_and_four = 0
total_mark = 0
fail = 0


for i in range(number_students):
    mark = float(input())
    total_mark += mark
    if mark >= 5:
        top_students += 1
    elif 4 <= mark <= 4.99:
        between_four_and_five += 1
    elif 3 <= mark <= 3.99:
        between_three_and_four += 1
    else:
        fail += 1

average_mark = total_mark / number_students
average_top = top_students / number_students * 100
average_between_four_and_five = between_four_and_five / number_students * 100
average_between_three_and_four = between_three_and_four / number_students * 100
average_fail = fail / number_students * 100

print(f"Top students: {average_top:.2f}%\n"
      f"Between 4.00 and 4.99: {average_between_four_and_five:.2f}%\n"
      f"Between 3.00 and 3.99: {average_between_three_and_four:.2f}%\n"
      f"Fail: {average_fail:.2f}%\n"
      f"Average: {average_mark:.2f}")

