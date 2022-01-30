
voucher = int(input())

tickets_count = 0
others_count = 0

while True:

    purchase = input()
    if purchase == "End":
        break
    if len(purchase) > 8:
        voucher -= ord(purchase[0]) + ord(purchase[1])
        if voucher < 0:
            break
        tickets_count += 1
    else:
        voucher -= ord(purchase[0])
        if voucher < 0:
            break
        others_count += 1

print(f"{tickets_count}\n"
      f"{others_count}")
