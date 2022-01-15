
# inputs

nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())

# variables

nylon_price = 1.5
paint_price = 14.5
thinner_price = 5
bags = 0.4
nylon_add = 2
paint_add = 0.1
workers_pay_rate = 0.3 # for 1 hour

# calculations

nylon_total_price = (nylon + nylon_add) * nylon_price
paint_total_price = (paint + (paint_add * paint)) * paint_price
thinner_total_price = thinner_price * thinner
total_material_price = nylon_total_price + paint_total_price + thinner_total_price + bags

workers_total_price = (total_material_price * workers_pay_rate) * hours

total_price = total_material_price + workers_total_price

# output

print(total_price)