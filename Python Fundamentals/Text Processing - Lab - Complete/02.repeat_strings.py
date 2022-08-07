text = input().split(" ")
result = ""

for i in text:
    length = len(i)
    result += i * length
print(result)
