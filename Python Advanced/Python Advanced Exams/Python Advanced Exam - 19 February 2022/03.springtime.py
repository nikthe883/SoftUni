def start_spring(**kwargs):
    my_dict = {}

    for k, v in kwargs.items():
        if v not in my_dict:
            my_dict[v] = []
        my_dict[v].append(k)

    sorted_tuple = sorted(my_dict.items(), key=lambda k: (-len(k[1]), k[0]))
    result = ""

    for i in sorted_tuple:
        result += i[0] + ':\n'
        for x in sorted(i[1]):
            result += f"-{x}\n"

    return result

