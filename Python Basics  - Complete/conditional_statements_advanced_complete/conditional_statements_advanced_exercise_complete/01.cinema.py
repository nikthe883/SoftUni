
# inputs

screen_type = input()
rows = int(input())
columns = int(input())

# variables

income = 0
premiere_ticket_price = 12
normal_ticket_price = 7.5
discount_ticket_price = 5

# calculations

cinema_capacity = rows * columns

# decisions

if screen_type == "Premiere":
    income = cinema_capacity * premiere_ticket_price
elif screen_type == "Normal":
    income = cinema_capacity * normal_ticket_price
elif screen_type == "Discount":
    income = cinema_capacity * discount_ticket_price

# output

print(f"{income:.2f} leva")

