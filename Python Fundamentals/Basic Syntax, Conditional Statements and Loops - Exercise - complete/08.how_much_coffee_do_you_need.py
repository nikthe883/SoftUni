
keyword_list = ["coding", "dog", "cat", "movie"]
coffee_number = 0

user_input = input()

while user_input != "END":
    if user_input in keyword_list:
        coffee_number += 1
    elif user_input in [x.upper() for x in keyword_list]:
        coffee_number += 2

    user_input = input()

if coffee_number > 5:
    print("You need extra sleep")
else:
    print(coffee_number)
