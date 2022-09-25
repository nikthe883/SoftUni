n = int(input())
guests = set([])

for _ in range(n):
    guests.add(input())

command = input()

while command != "END":
    guests.remove(command)
    command = input()
print(len(guests))
for i in list(sorted(guests)):
    print(i)
