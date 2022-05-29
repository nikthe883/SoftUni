
start = int(input())
end = int(input())

output = ""
for i in range(start, end + 1):
    output += chr(i) + " "

print(output)