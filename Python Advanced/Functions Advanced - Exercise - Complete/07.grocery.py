def grocery_store(**kwargs):
    new_dict = {k: v for k, v in sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))}
    result = ""
    for k, v in new_dict.items():
        result += f"{k}: {v}\n"
    return result
