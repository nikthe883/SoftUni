from collections import deque

ramen = [int(x) for x in input().split(', ')]
customers = deque(int(x) for x in input().split(', '))

while ramen and customers:
    ramen_bowl = ramen.pop()
    customer = customers.popleft()

    if ramen_bowl == customer:
        continue
    elif ramen_bowl > customer:
        ramen_bowl -= customer
        ramen.append(ramen_bowl)
    elif ramen_bowl < customer:
        customer -= ramen_bowl
        customers.appendleft(customer)

if not customers:
    print("Great job! You served all the customers.")
    if ramen:
        print(f"Bowls of ramen left: {', '.join(str(x) for x in ramen)}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    if customers:
        print(f"Customers left: {', '.join(str(x) for x in customers)}")
