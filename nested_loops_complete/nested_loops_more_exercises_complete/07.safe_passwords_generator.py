
num_a = int(input())
num_b = int(input())
max_count = int(input())

a_symbol = 35
b_symbol = 64
counter = 0

for a in range(1, num_a + 1):
    for b in range(1, num_b + 1):
        counter += 1
        if a_symbol > 55:
            a_symbol = 35
        if b_symbol > 96:
            b_symbol = 64

        if counter > max_count:
            break
        else:
            print(f"{chr(a_symbol)}{chr(b_symbol)}{a}{b}{chr(b_symbol)}{chr(a_symbol)}", end="|")

        a_symbol += 1
        b_symbol += 1
