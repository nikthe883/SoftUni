from collections import deque



food_quantity = int(input())

 
queue = deque(int(i) for i in input().split())

print(max(queue))

while True:
    if int(queue[0]) <= food_quantity:
        order = queue.popleft()
        food_quantity -= int(order)
    else:
        break
    if not queue:
        break

    

if queue:
    print(f"Orders left: {' '.join(map(str, queue))}")
else:
    print("Orders complete")
