
# inputs

day_of_week = int(input())

# dictionary

week_days = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}

# decision
found = False

for k, v in week_days.items():
    if k == day_of_week:
        print(v)
        found = True

if not found:
    print("Error")


