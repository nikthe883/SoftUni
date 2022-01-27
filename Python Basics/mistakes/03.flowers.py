hriz = int(input())
rozi = int(input())
laleta = int(input())
season = input()
praz = input()

if season == "Spring" or season == "Summer":  # was put like if season == "Spring" or "Summer"
    price = hriz * 2 + rozi * 4.1 + laleta * 2.5
    if praz == "Y":
        price *= 1.15
    if (season == "Spring") and (laleta > 7):
        price *= 0.95
    if hriz + rozi + laleta > 20:
        price *= 0.8
    price += 2

else:
    price = hriz * 3.75 + rozi * 4.5 + laleta * 4.15
    if praz == "Y":
        price *= 1.15
    if (season == "Winter") and (rozi >= 10):
        price *= 0.9
    if hriz + rozi + laleta > 20:
        price *= 0.8
    price += 2

print(f'{price:.2f}')
