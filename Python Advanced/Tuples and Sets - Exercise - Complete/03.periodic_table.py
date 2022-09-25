n = int(input())

chemical_elements = set()

for _ in range(n):
    [chemical_elements.add(x) for x in input().split()]

print(*chemical_elements, sep="\n")
