
num1 = int(input())
num2 = int(input())
num3 = int(input())


for a in range(1,num1+1):
    for b in range(1,num2+1):
        for c in range(1,num3+1):
            if a % 2 == 0 and b in [2,3,5,7] and c % 2 == 0 :
                print(a,b,c)