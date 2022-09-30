n = int(input())

my_dict = {}

for i in range(n):
    name = input()
    grade = float(input())

    if name not in my_dict:
        my_dict[name] = [grade]
    else:
        my_dict[name].append(grade)

for k, v in my_dict.items():
    av = sum(v) / len(v)
    if av >= 4.50:
        print(f"{k} -> {av:.2f}")
