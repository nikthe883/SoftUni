inheritance = float(input())
year_to_live = int(input())

age = 18

for i in range(1800, year_to_live +1):
    if i % 2 == 0:
        inheritance -= 12_000
    else:
        inheritance -= 12_000 + 50*age
    age += 1

if inheritance >= 0:
    print(f'Yes! He will live a carefree life and will have {inheritance:.2f} dollars left.')
else:
    print(f"He will need {abs(inheritance):.2f} dollars to survive.")
