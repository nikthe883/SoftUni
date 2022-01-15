
# inputs

hour = int(input())
day = input()

# decisions

if day == "Monday" and 10 <= hour <= 18:
    print("open")

elif day == "Tuesday" and 10 <= hour <= 18:
    print("open")

elif day == "Wednesday" and 10 <= hour <= 18:
    print("open")

elif day == "Thursday" and 10 <= hour <= 18:
    print("open")

elif day == "Friday" and 10 <= hour <= 18:
    print("open")

elif day == "Saturday" and 10 <= hour <= 18:
    print("open")

else:
    print("closed")

