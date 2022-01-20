
total_money_need_to_be_gathered = int(input())


total_money_cc = 0
total_money_cs = 0
total_loops = 0
loops_cc = 0
loops_cs = 0


while total_money_need_to_be_gathered > 0:

    product = input()

    if product == "End":
        print("Failed to collect required money for charity.")
        break

    product = int(product)
    total_loops += 1

    if total_loops % 2 == 0 and product >= 10:
        loops_cc += 1
        total_money_cc += product
        total_money_need_to_be_gathered -= product
        print("Product sold!")

    elif total_loops % 2 == 1 and product <= 100:
        loops_cs += 1
        total_money_cs += product
        total_money_need_to_be_gathered -= product
        print("Product sold!")

    else:
        print("Error in transaction!")


if total_money_need_to_be_gathered <= 0:
    print(f"Average CS: {total_money_cs/loops_cs:.2f}\n"
          f"Average CC: {total_money_cc/loops_cc:.2f}")
