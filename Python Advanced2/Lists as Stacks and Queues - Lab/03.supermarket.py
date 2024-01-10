from collections import deque

queue = deque()

customer = input()

while True:
    if customer == "Paid":
        print(queue.popleft())
    elif customer == "End":
        print(f"{len(queue)} people remaining.")
        break
    else:
        queue.append(customer)
    customer = input()