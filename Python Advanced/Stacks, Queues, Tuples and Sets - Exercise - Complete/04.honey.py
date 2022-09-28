from collections import deque

working_bees = deque(map(int, input().split()))
nectar = list(map(int, input().split()))
symbols = deque(input().split())

total_honey = 0


def honey(bee_arg, nectar_arg):
    symbol_one = symbols.popleft()
    honey_made = abs(eval(str(bee_arg) + symbol_one + str(nectar_arg)))
    return honey_made


while nectar and working_bees:
    bee = working_bees.popleft()
    curr_nectar = nectar.pop()
    if bee > curr_nectar:
        working_bees.appendleft(bee)
        continue
    if curr_nectar == 0:
        continue
    else:
        total_honey += abs(honey(bee, curr_nectar))

print(f"Total honey made: {total_honey}")
if working_bees:
    print(f"Bees left: {', '.join(str(x) for x in working_bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")
