from collections import deque

food_q = int(input())
orders = deque(int(i) for i in input().split())

print(max(orders))

while True:
    if int(orders[0]) <= food_q:
        order = orders.popleft()
        food_q -= int(order)
    else:
        break
    if not orders:
        break


if orders:
    print(f"Orders left: {' '.join(map(str, orders))}")
else:
    print("Orders complete")
