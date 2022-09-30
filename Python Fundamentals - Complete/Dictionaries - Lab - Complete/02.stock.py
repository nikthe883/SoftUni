el = input().split(" ")
bakery = {}

for i in range(0, len(el), 2):
    k = el[i]
    v = el[i + 1]
    bakery[k] = int(v)

product = input().split()

for i in product:
    if i in bakery:
        print(f"We have {bakery[i]} of {i} left")
    else:
        print(f"Sorry, we don't have {i}")
