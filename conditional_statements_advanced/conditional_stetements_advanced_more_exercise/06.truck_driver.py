
season = input()
km = float(input())



salary = 0
pay_per_km = 0

seasons = {"Spring": 0.75, "Summer": 0.90, "Autumn": 0.75, "Winter": 1.05}

for k,v in seasons.items():
    if k == season:
        pay_per_km = v

if km <= 5000:
    salary = pay_per_km * km * 4
elif 5000 < km <= 10_000:
    salary = (pay_per_km + 0.20) * km * 4
else:
    salary = 1.45 * km * 4

taxes = 0.1
salary = salary - (salary * taxes)

print(f"{salary:.2f}")

