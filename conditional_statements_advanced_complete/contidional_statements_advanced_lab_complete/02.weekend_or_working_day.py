
# inputs

day = input()

week_days = ["Monday",  "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]  # list

found = False # bool


# checks if the word is in list break at end not to print couple of times

for i in week_days:
    if day in week_days[:5]:  # list slicing
        print("Working day")
        found = True
        break
    elif day in week_days[5:]:
        found = True
        print("Weekend")
        break

if not found:
    print("Error")
