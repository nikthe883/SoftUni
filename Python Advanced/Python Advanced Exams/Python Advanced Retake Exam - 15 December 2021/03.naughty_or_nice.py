from collections import Counter

# not working for working
def naughty_or_nice_list(the_list, *args, **kwargs):
    mah_dict = {"Nice": [], "Naughty": [], "Not found": []}
    new_list = []
    mah_list = []
    for i in range(len(the_list)):
        new_list.append((str(the_list[i][0]), the_list[i][1]))

    count = Counter(p[0] for p in new_list)
    names = Counter(p[1] for p in new_list)

    for arg in args:
        arg = arg.split("-")
        for i in range(len(the_list)):
            if int(arg[0]) == the_list[i][0]:
                if count[str(the_list[i][0])] == 1:
                    if the_list[i] not in mah_list:
                        mah_dict[arg[1]].append(f"{the_list[i][1]}")
                        mah_list.append(the_list[i])

    for k, v in kwargs.items():
        for i in range(len(the_list)):
            if k == the_list[i][1]:
                if names[the_list[i][1]] == 1:
                    if the_list[i] not in mah_list:
                        mah_dict[v].append(f"{the_list[i][1]}")
                        mah_list.append(the_list[i])


    the_new_list = (list(set(the_list) - set(mah_list)))
    for i in the_new_list:
        mah_dict['Not found'].append(i[1])

    result = ""
    for k, v in mah_dict.items():
        if v:
            result += k
            result += f": {', '.join(v)}\n"

    return result


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))

print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
))

print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
