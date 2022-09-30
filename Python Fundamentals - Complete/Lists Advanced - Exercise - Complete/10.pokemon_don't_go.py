pokemon_distance = [int(x) for x in input().split(" ")]


def check_distance(number):
    for i in range(len(pokemon_distance)):
        if number >= pokemon_distance[i]:
            pokemon_distance[i] += number
        else:
            pokemon_distance[i] -= number


elements = 0
while len(pokemon_distance) >= 1:

    user_input = int(input())
    number = 0
    if user_input < 0:

        number = pokemon_distance[0]
        pokemon_distance[0] = pokemon_distance[-1]
        check_distance(number)

    elif user_input > len(pokemon_distance) - 1:

        number = pokemon_distance[-1]
        pokemon_distance[-1] = pokemon_distance[0]
        check_distance(number)
    else:
        number = pokemon_distance.pop(user_input)

        check_distance(number)

    elements += number

print(elements)
