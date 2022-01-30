
# inputs

pens = int(input())
markers = int(input())
detergents = int(input())

# gets the input for discount in percentages
# alternatively : discount_percentage = discount / 100  - to get 0. something
discount = int(input()) / 100

# variables

pens_pack_price = 5.8
markers_pack_price = 7.2
detergents_liter_price = 1.2



# calculations

total_pens_price = pens * pens_pack_price
total_markers_price = markers * markers_pack_price
total_detergents_price = detergents * detergents_liter_price

price_without_discount = total_pens_price + total_markers_price + total_detergents_price
price_with_discount = price_without_discount - (price_without_discount * discount)

# output

print(f'{price_with_discount}')