def words_sorting(*args):
    my_dict = {}

    for word in args:
        letter_value = 0
        for letter in word:
            letter_value += ord(letter)
        if word not in my_dict:
            my_dict[word] = letter_value

    sum_values = 0
    for v in my_dict.values():
        sum_values += v

    result = []
    if sum_values % 2 != 0:
        sorted_dict = sorted(my_dict.items(), key=lambda x: -x[1])
        for i in sorted_dict:
            result.append(f"{i[0]} - {i[1]}")

    if sum_values % 2 == 0:
        sorted_dict = sorted(my_dict.items(), key=lambda x: x[1])
        for i in sorted_dict:
            result.append(f"{i[0]} - {i[1]}")

    return "\n".join(result)
