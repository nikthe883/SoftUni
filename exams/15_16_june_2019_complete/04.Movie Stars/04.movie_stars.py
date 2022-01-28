
actor_budget = float(input())

total_actor_salary = 0

actor_name = input()


while actor_name != "ACTION":

    if actor_budget < 0:
        break

    if len(actor_name) > 15:
        actor_budget -= actor_budget * 0.20
    else:
        salary = float(input())
        actor_budget -= salary

    actor_name = input()

if actor_budget > 0:
    print(f"We are left with {actor_budget:.2f} leva.")
else:
    print(f"We need {abs(actor_budget):.2f} leva for our actors.")
