import re

pattern = r">>([A-z]+)<<(\d+(\.\d+)?)!(\d+)"
text = input()
furniture = []
total_price = 0
while text != "Purchase":
    matches = re.findall(pattern, text)
    for i in matches:
        furniture.append(i[0])
        total_price += float(i[1]) * int(i[3])

    text = input()

print("Bought furniture:")
for i in furniture:
    print(i)
print(f"Total money spend: {total_price:.2f}")
