food = float(input()) * 1000
hay = float(input()) * 1000
cover = float(input()) * 1000
guinea_pig_weight = float(input()) * 1000
no_shop = True

for day in range(1, 30 +1):
    food -= 300
    if day % 2 == 0:
        hay -= food * 0.05
    if day % 3 == 0:
        cover -= guinea_pig_weight * 0.33333

    if food <= 0 or hay <= 0 or cover <= 0:
        print("Merry must go to the pet store!")
        no_shop = False
        break

if no_shop:
    print(f"Everything is fine! Puppy is happy! Food: {food / 1000:.2f}, Hay: {hay / 1000 :.2f}, Cover: {cover / 1000 :.2f}.")
