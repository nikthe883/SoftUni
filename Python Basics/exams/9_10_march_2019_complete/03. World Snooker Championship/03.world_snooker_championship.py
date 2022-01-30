
stage = input()
ticket_class = input()
ticket_number = int(input())
picture = input()

price = 0
free_pics = False

if stage == "Quarter final":
    if ticket_class == "Standard":
        price += 55.50 * ticket_number
    elif ticket_class == "Premium":
        price += 105.20 * ticket_number
    else:
        price += 118.90 * ticket_number

elif stage == "Semi final":
    if ticket_class == "Standard":
        price += 75.88 * ticket_number
    elif ticket_class == "Premium":
        price += 125.22 * ticket_number
    else:
        price += 300.40 * ticket_number

else:
    if ticket_class == "Standard":
        price += 110.10 * ticket_number
    elif ticket_class == "Premium":
        price += 160.66 * ticket_number
    else:
        price += 400 * ticket_number


if price > 4000:
    price *= 0.75
    free_pics = True

elif price > 2500:
    price *= 0.90

if not free_pics and picture == "Y":
    price += 40 * ticket_number

print(f"{price:.2f}")
