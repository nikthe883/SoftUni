def even_odd_filter(**kwargs):
    for k, v in kwargs.items():
        if k == "odd":
            kwargs['odd'] = [int(x) for x in kwargs['odd'] if x % 2 == 1]
        else:
            kwargs['even'] = [int(x) for x in kwargs['even'] if x % 2 == 0]
    return kwargs

