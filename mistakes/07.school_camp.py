season = input()
group_sex = input()
students_number = int(input())
nights = int(input())

discount = 0
price = 0
sport = ""
# For dicount
if students_number >= 50:
    discount = 0.50
elif students_number >= 20:
    discount = 0.85
elif students_number >= 10:
    discount = 0.95
elif students_number < 10:
    discount = 1

# For price
if season == "Winter":
    if group_sex == "girls":
        price = 9.60
    elif group_sex == "boys":
        price = 9.60
    elif group_sex == "mixed":
        price = 10
if season == "Spring":
    if group_sex == "girls":
        price = 7.20
    elif group_sex == "boys":
        price = 7.20
    elif group_sex == "mixed":
        price = 9.50
if season == "Summer":
    if group_sex == "girls":
        price = 15
    elif group_sex == "boys":
        price = 15
    elif group_sex == "mixed":
        price = 20
# For Sports
if season == "Winter":
    if group_sex == "girls":
        sport = "Gymnastics"
    elif group_sex == "boys":
        sport = "Judo"
    elif group_sex == "mixed":
        sport = "Ski"
if season == "Spring":
    if group_sex == "girls":
        sport = "Athletics"
    elif group_sex == "boys":
        sport = "Tenins"  # incorrectly spelled the word tennis
    elif group_sex == "mixed":
        sport = "Cycling"
if season == "Summer":
    if group_sex == "girls":
        sport = "Volleyball"
    elif group_sex == "boys":
        sport = "Football"
    elif group_sex == "mixed":
        sport = "Swimming"
total = (students_number * price * nights) * discount
print(f'{sport} {total:.2f} lv.')

