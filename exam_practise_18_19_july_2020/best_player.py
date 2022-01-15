


names = []
goals = []


while True:
    highest_score_name = ""
    highest_score_goal = ""

    name = input()
    names.append(name)

    if name == "END":
        print("END")
        break
    else:
        goal = int(input())
        goals.append(goal)

        for a in names:
            for b in goals:
                if b < goal:
                    highest_score_name  = highest_score_name + a
                    highest_score_goal = highest_score_goal + b


        if goal >= 3:
            print(f"{highest_score_name} is the best player!\n"
                  f"He has scored {highest_score_goal} goals and made a hat-trick !!!")
        else:
            print(f"{highest_score_name} is the best player!\n"
                  f"He has scored {highest_score_goal} goals.")





