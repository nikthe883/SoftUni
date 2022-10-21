def words_sorting(*args):
    my_dict = {}
    for i in args:
        if i not in my_dict:
            my_dict[i] = 0
        my_dict[i] = sum([ord(v) for v in i])

    result = ''

    if sum(my_dict.values()) % 2 == 0:
        mah_list = sorted(my_dict.keys(), key=lambda x: x[0])
        for i in mah_list:
            result += f"{i} - {my_dict[i]}\n"
    else:
        mah_list = sorted(my_dict.values(), key=lambda x: -x)
        for i in mah_list:
            result += f"{list(my_dict.keys())[list(my_dict.values()).index(i)]} - {i}\n"

    return result


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))

print(
    words_sorting(
        'cacophony',
        'accolade'
  ))
