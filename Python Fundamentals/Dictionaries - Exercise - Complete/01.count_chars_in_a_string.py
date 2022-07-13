
user_input = input()
counts = {}

for i in user_input:
    if i != " ":
        if i not in counts:
            counts[i] = 0
        counts[i] += 1


[print(f"{k} -> {v}") for k,v in counts.items()]