
n = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0


for i in range(n):
    num = int(input())

    if num < 200:
        p1 += 1
    elif 200 <= num <= 399:
        p2 += 1
    elif 400 <= num <= 599:
        p3 += 1
    elif 600 <= num <= 799:
        p4 += 1
    else:
        p5 += 1

for i in p1,p2,p3,p4,p5:
    print(f"{i /n * 100 :.02f}%")

