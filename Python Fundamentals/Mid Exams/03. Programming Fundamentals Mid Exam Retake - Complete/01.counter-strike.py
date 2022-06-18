energy = int(input())
action = input()
won_battles = 0

while action != "End of battle":

    if energy >= int(action):

        energy -= int(action)
        won_battles += 1

    else:
        print(f"Not enough energy! Game ends with {won_battles} won battles and {energy} energy")
        break

    if won_battles % 3 == 0:
        energy += won_battles

    action = input()

else:
    print(f"Won battles: {won_battles}. Energy left: {energy}")
