el = input().split(" ")
bakery = {}

for i in range(0, len(el), 2):
    k = el[i]
    v = el[i + 1]
    bakery[k] = int(v)

print(bakery)
