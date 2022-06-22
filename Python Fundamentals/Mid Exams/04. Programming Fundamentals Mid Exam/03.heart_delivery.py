houses = [int(x) for x in input().split("@")]
command = input().split(" ")

jump = 0
had_v = []

while command[0] != "Love!":

    jump += int(command[1])

    if jump > len(houses) - 1:
        jump = 0
        if houses[0] in had_v:
            print(f"Place {0} already had Valentine's day.")
        else:
            houses[0] -= 2

            if houses[0] == 0:
                houses[0] = 0
                print(f"Place {0} has Valentine's day.")
                had_v.append(houses[0])

    else:
        if houses[jump] in had_v:
            print(f"Place {jump} already had Valentine's day.")
        else:
            houses[jump] -= 2
            if houses[jump] == 0:
                houses[jump] = 0
                print(f"Place {jump} has Valentine's day.")
                had_v.append(houses[jump])

    command = input().split(" ")

print(f"Cupid's last position was {jump}.")

valentines_counter = 0

for i in houses:
    if i == 0:
        valentines_counter += 1

if valentines_counter == len(houses):
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(houses) - valentines_counter} places.")
