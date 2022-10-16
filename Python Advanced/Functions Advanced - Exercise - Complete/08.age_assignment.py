def age_assignment(*args, **kwargs):
    result = ""
    mah_list = []
    for letter in args:
        for k, v in kwargs.items():
            if k == letter[0]:
                mah_list.append((letter, v))
    new_list = sorted(mah_list)
    for i in new_list:
        result += f"{i[0]} is {i[1]} years old.\n"
    return result

