
name_actor = input()
academy_points = float(input())
judges_number = int(input())

max_points = 1250.5
actor_points = academy_points


for i in range(judges_number):

    judge_name = input()
    judge_points = float(input())

    actor_points += (len(judge_name) * judge_points) / 2
    if actor_points >= max_points:
        print(f"Congratulations, {name_actor} got a nominee for leading role with {actor_points:.1f}!")
        break

if actor_points < max_points:
    points_needed = max_points - actor_points
    print(f"Sorry, {name_actor} you need {points_needed:.1f} more!")

