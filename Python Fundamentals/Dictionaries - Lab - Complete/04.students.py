user_input = input()
courses = {}

while ':' in user_input:
    students = user_input.split(':')

    if students[2] not in courses.keys():
        courses[students[2]] = {}
    courses[students[2]][students[1]] = students[0]

    user_input = input()

user_input = user_input.replace('_', ' ')

for i in courses[user_input]:
    print(f'{courses[user_input][i]} - {i}')
