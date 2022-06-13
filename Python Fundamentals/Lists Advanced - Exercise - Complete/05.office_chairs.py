rooms = int(input())

total_chairs = 0
total_people = 0
for i in range(1, rooms + 1):
    user_input = input().split(" ")
    chairs = len(user_input[0])
    people = int(user_input[1])
    total_people += people
    total_chairs += chairs
    if chairs < people:
        print(f"{int(people)-int(chairs)} more chairs needed in room {i}")


if total_people <= total_chairs:
    print(f"Game On, {total_chairs-total_people} free chairs left")
