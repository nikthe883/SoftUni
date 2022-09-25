n = int(input())
my_dict = {}

for _ in range(n):
    student_grade = input().split()
    if student_grade[0] not in my_dict:
        my_dict[student_grade[0]] = []
    my_dict[student_grade[0]].append(float(student_grade[1]))

for student, grade in my_dict.items():
    string = ' '.join('{:0.2f}'.format(i) for i in grade)
    print(f"{student} -> {string} (avg: {sum(grade) / len(grade):.2f})")
