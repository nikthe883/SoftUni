country = input().split(", ")
capital = input().split(", ")

my_dict = {k: v for k, v in zip(country, capital)}

for k, v in my_dict.items():
    print(f"{k} -> {v}")
