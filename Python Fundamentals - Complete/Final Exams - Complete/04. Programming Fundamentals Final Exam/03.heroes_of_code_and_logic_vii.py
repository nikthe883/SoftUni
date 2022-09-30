n = int(input())
heroes = {}

for _ in range(n):
    user_input = input().split(" ")
    heroes[user_input[0]] = {"HP": int(user_input[1]), "MP": int(user_input[2])}

commands = input().split(" - ")

while commands[0] != "End":

    if commands[0] == "CastSpell":
        if heroes[commands[1]]["MP"] >= int(commands[2]):
            heroes[commands[1]]["MP"] -= int(commands[2])
            print(f"{commands[1]} has successfully cast {commands[3]} and now has {heroes[commands[1]]['MP']} MP!")
        else:
            print(f"{commands[1]} does not have enough MP to cast {commands[3]}!")
    elif commands[0] == "TakeDamage":

        heroes[commands[1]]["HP"] -= int(commands[2])

        if heroes[commands[1]]["HP"] > 0:
            print(f"{commands[1]} was hit for {commands[2]} HP by {commands[3]} and now has {heroes[commands[1]]['HP']} HP left!")
        else:
            print(f"{commands[1]} has been killed by {commands[3]}!")
            del heroes[commands[1]]

    elif commands[0] == "Recharge":

        needed_to_full = 200 - heroes[commands[1]]["MP"]
        heroes[commands[1]]["MP"] += int(commands[2])

        if heroes[commands[1]]["MP"] > 200:
            heroes[commands[1]]["MP"] = 200
            print(f"{commands[1]} recharged for {needed_to_full} MP!")
        else:
            print(f"{commands[1]} recharged for {commands[2]} MP!")

    elif commands[0] == "Heal":
        needed_to_full = 100 - heroes[commands[1]]["HP"]
        heroes[commands[1]]["HP"] += int(commands[2])

        if heroes[commands[1]]["HP"] > 100:
            heroes[commands[1]]["HP"] = 100
            print(f"{commands[1]} healed for {needed_to_full} HP!")
        else:
            print(f"{commands[1]} healed for {commands[2]} HP!")

    commands = input().split(" - ")

for k in heroes:
    print(k)
    print(f"  HP: {heroes[k]['HP']}")
    print(f"  MP: {heroes[k]['MP']}")
