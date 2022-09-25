n = int(input())

longest = []

a = set()
b = set()

for _ in range(n):
    first, second = input().split("-")
    first_start, first_end = [int(x) for x in first.split(",")]
    second_start, second_end = [int(x) for x in second.split(",")]
    for i in range(first_start, first_end + 1):
        a.add(i)
    for i in range(second_start, second_end + 1):
        b.add(i)

    curr = a.intersection(b)
    b = set()
    a = set()
    if len(curr) > len(longest):
        longest = list(curr)

print(f"Longest intersection is {longest} with length {len(longest)}")
