
num_poor_grades = int(input())

total_poor_grade = 0
enough = False
num_assignments = 0
average_score = 0
last_problem = ""

while num_poor_grades != total_poor_grade:
    assignment_name = input()

    if assignment_name == "Enough":
        enough = True
        break

    score = int(input())
    last_problem = assignment_name
    average_score += score
    num_assignments += 1

    if score <= 4:
        total_poor_grade += 1

if enough:
    average_score = average_score / num_assignments
    print(f"Average score: {average_score:.2f}\n"
          f"Number of problems: {num_assignments}\n"
          f"Last problem: {last_problem}")

else:
    print(f"You need a break, {num_poor_grades} poor grades.")

