
def forecast(*args):
    mah_dict = {"Sunny": [], "Cloudy": [], "Rainy": []}

    for i in args:
        mah_dict[i[1]].append(i[0])

    mah_dict_two = {x: sorted(mah_dict[x]) for x in mah_dict.keys()}
    result = ''
    for k, v in mah_dict_two.items():
        for value in v:
            result += f"{value} - {k}\n"
    return result
