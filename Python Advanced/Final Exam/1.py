from collections import deque

caffeine = [int(x) for x in input().split(', ')]
energy_drinks = deque(int(x) for x in input().split(', '))

stamat = 0

while caffeine and energy_drinks:

    caf = caffeine.pop()
    energy_drink = energy_drinks.popleft()

    total = caf * energy_drink


    if (stamat + total) <= 300:
        stamat += total
    else:
        energy_drinks.append(energy_drink)
        reduction = stamat - 30
        if reduction >= 0:
            stamat -= 30

if energy_drinks:
    print(f"Drinks left: {', '.join(str(x) for x in energy_drinks)}")

else:
    print(f"At least Stamat wasn't exceeding the maximum caffeine.")


print(f"Stamat is going to sleep with {stamat} mg caffeine.")