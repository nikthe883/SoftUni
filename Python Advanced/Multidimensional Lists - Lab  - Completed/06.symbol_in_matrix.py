rows = int(input())
matrix = [input() for x in range(rows)]
symbol = input()

flag = False
pos = ()

for i in range(rows):
    for j in range(rows):
        if matrix[j][i] == symbol:
            flag = True
            pos = (j, i)
            break
if flag:
    print(pos)
else:
    print(f"{symbol} does not occur in the matrix")
