def concatenate(*args, **kwargs):
    mah_string = "".join(args)
    for k,v  in kwargs.items():
        if k in mah_string:
            mah_string = mah_string.replace(k, v)
    return mah_string

