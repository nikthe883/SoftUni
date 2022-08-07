import re

pattern = r"@#{1,}([A-Z]{1,}[A-Za-z0-9]{4,}[A-Z]{1,})@#{1,}"

n = int(input())

for _ in range(n):
    barcode = input()
    matches = re.match(pattern, barcode)
    if matches:
        product_group = ""
        for i in barcode:
            if i.isdigit():
                product_group += i

        if product_group:
            print(f"Product group: {product_group}")
        else:
            print("Product group: 00")
        product_group = ""

    else:
        print("Invalid barcode")

