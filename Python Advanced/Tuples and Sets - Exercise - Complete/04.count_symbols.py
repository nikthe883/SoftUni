user_input = tuple(sorted(input()))

unique = {}
for i in user_input:
    if i not in unique:
        unique[i] = user_input.count(i)

for k, v in unique.items():
    print(f"{k}: {v} time/s")
