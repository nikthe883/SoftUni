rows, cols = [int(x) for x in input().split()]
# start chr(97)
matrix = []
start = 97

for i in range(rows):
    cur_list = []
    for j in range(cols):
        string = chr(start + i) + chr(start + i + j) + chr(start + i)
        cur_list.append(string)
    matrix.append(cur_list)

print('\n'.join(' '.join(map(str, i)) for i in matrix))
