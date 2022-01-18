
steps = 0
goal = 10000

while steps <= goal:

    counting_steps = input()
    if counting_steps == "Going home":
        steps += int(input())
        break
    counting_steps_int = int(counting_steps)
    steps += counting_steps_int


steps_needed_or_left = abs(steps - goal)
if steps >= goal:
    print(f"Goal reached! Good job!\n"
          f"{steps_needed_or_left} steps over the goal!")
else:
    print(f"{steps_needed_or_left} more steps to reach goal.")
