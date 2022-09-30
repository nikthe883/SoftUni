theater_capacity = int(input())

number_people = input()
total_people = 0
money = 0



while number_people != "Movie time!":

    total_people += int(number_people)

    if theater_capacity < total_people:
        print("The cinema is full.")
        break

    money += int(number_people) * 5
    if int(number_people) % 3 == 0:
        money -= 5

    number_people = input()

if number_people == "Movie time!":
    print(f"There are {theater_capacity - total_people} seats left in the cinema.")

print(f'Cinema income - {money} lv.')
