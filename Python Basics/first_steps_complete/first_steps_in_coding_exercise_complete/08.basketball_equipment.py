
# inputs

annual_basketball_practise_tax = int(input())

# calculations

basketball_shoes_price = annual_basketball_practise_tax - ( annual_basketball_practise_tax * 0.4)
basketball_tracksuit_price = basketball_shoes_price - (basketball_shoes_price * 0.2)
basketball_price = basketball_tracksuit_price * 0.25
basketball_accessories_price = basketball_price * 0.20

total_price = annual_basketball_practise_tax + basketball_shoes_price + \
    basketball_accessories_price + basketball_tracksuit_price + \
    basketball_price

# output

print(total_price)