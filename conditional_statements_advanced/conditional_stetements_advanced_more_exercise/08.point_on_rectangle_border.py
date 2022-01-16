

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x = float(input())
y = float(input())

if x == x1 or x == x2:
    if y1 <= y <= y2:
        print("Border")
    else:
        print("Inside / Outside")
elif y == y1 or y == y2:
    if x1 <= x <= x2:
        print("Border")
    else:
        print("Inside / Outside")
else:
    print("Inside / Outside")
