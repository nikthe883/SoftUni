
name = input()

football_name = ""
goals = 0

while name != "END":

    number_of_goals = int(input())
    if number_of_goals > goals:
        goals = number_of_goals
        football_name = name

    if number_of_goals >= 10:
        break

    name = input()



if goals >= 3:
    print(f"{football_name} is the best player!\n"
          f"He has scored {goals} goals and made a hat-trick !!!")
else:
    print(f"{football_name} is the best player!\n"
          f"He has scored {goals} goals.")
