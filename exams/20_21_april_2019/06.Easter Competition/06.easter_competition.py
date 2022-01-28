
number_breads = int(input())

best = ""
best_points = 0


for i in range(number_breads):

    name = input()
    score = input()
    points_person = 0

    while score != "Stop":
        points_person += int(score)
        score = input()

    print(f"{name} has {points_person} points.")

    if best_points < points_person:
        best_points = points_person
        best = name
        print(f"{best} is the new number 1!")


print(f"{best} won competition with {best_points} points!")
