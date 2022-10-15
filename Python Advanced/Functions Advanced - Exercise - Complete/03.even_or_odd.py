def even_odd(*args):
    numbers_list = [int(x) for x in args[:-1]]
    if args[-1] == "even":
        return [x for x in numbers_list if x % 2 == 0]
    if args[-1] == "odd":
        return [x for x in numbers_list if x % 2 == 1]

