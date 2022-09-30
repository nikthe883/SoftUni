from collections import deque

queue = deque()

customer = input()

while True:
    if customer == "Paid":
        for _ in range(len(queue)):
            print(queue.popleft())
    elif customer == "End":
        print(f"{len(queue)} people remaining.")
        break
    else:
        queue.append(customer)
    customer = input()
