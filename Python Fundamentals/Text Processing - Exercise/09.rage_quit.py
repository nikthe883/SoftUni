message = input().upper()

unique_symbols = ""
cur_symbol = ""
reps = ""

for i in range(len(message)):
    if not message[i].isdigit():
        cur_symbol += message[i]
    else:
        for check in range(i, len(message)):
            if not message[check].isdigit():
                break
            reps += message[check]
        reps = int(reps)
        unique_symbols += reps * cur_symbol
        cur_symbol = ""
        reps = ""
print(f"Unique symbols used: {len(set(unique_symbols))}")
print(unique_symbols)

