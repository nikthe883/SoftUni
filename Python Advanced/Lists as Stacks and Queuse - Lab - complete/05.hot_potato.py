from collections import deque

children = deque(input().split())
tosses = int(input())
counter = 1

while len(children) > 1:
    child = children.popleft()
    if counter == tosses:
        print(f"Removed {child}")
        counter = 1
    else:
        counter += 1
        children.append(child)

winner = children.popleft()
print(f"Last is {winner}")
