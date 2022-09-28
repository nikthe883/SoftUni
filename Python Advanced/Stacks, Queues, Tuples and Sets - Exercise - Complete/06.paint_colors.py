color_string = input().split()

colors_found = []

main_colors = ["red", "yellow", "blue"]
secondary_colors = {"orange": ['red', 'yellow'],
                    "purple": ['red', 'blue'],
                    "green": ['yellow', 'blue']}


while color_string:

    if color_string[0] in main_colors and len(color_string) == 1:
        colors_found.append(color_string[0])
        break
    if len(color_string) == 1:
        color_string[0] = color_string[0][1:-1]
        if color_string[0] in main_colors:
            colors_found.append(color_string[0])
            break
        else:
            break

    string_one = color_string.pop(0)
    string_two = color_string.pop(-1)

    if string_one + string_two in main_colors or string_one + string_two in secondary_colors:
        colors_found.append(string_one + string_two)

    elif string_two + string_one in main_colors or string_two + string_one in secondary_colors:
        colors_found.append(string_two + string_one)

    else:
        string_one = string_one[:-1]
        string_two = string_two[:-1]
        if len(color_string) % 2 == 0:
            if string_one:
                color_string.insert(len(color_string) // 2, string_one)
            if string_two:
                color_string.insert(len(color_string) // 2, string_two)
        else:
            if string_one:
                color_string.insert((len(color_string) // 2) + 1, string_one)
            if string_two:
                color_string.insert((len(color_string) // 2) + 1, string_two)

final = []
for i in colors_found:
    if i in main_colors:
        final.append(i)
    else:
        if all(item in colors_found for item in secondary_colors[i]):
            final.append(i)
print(final)
