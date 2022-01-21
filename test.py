

chrysanthemums_amount = int(input())
roses_amount = int(input())
tulips_amount = int(input())
season = input()
holiday = input()

chrysanthemums_price = 0
roses_price = 0
tulips_price = 0
price = 0



if season == "Spring" or season == "Summer":
    chrysanthemums_price = chrysanthemums_amount * 2
    roses_price = roses_amount * 4.1
    tulips_price = tulips_amount * 2.5
elif season == "Autumn" or season == "Winter":
    chrysanthemums_price = chrysanthemums_amount * 3.75
    roses_price = roses_amount * 4.5
    tulips_price = tulips_amount * 4.15

price = chrysanthemums_price + roses_price + tulips_price

if holiday == "Y":
    price *= 1.15

if tulips_amount > 7 and season == "Spring":
    price *= 0.95

elif roses_amount >= 10 and season == "Winter":
    price *= 0.90

if chrysanthemums_amount + roses_amount + tulips_amount > 20:
    price *= 0.80


print(f"{price + 2:.2f}")
