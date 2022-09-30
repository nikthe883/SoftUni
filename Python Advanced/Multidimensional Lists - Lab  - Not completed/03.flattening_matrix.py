
"""
https://stackoverflow.com/questions/29244286/how-to-flatten-a-2d-list-to-1d-without-using-numpy

matrix = [[1,2][1,2]]

[i for m in matrix for i in m]

new = []
for i in matrix:
    for j in i:
       new.append(j)

"""
rows = int(input())
matrix = [i for m in [[int(x) for x in input().split(", ")]for x in range(rows)] for i in m]
print(matrix)


