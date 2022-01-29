
# imports

import pandas as pd

# loading the data

table_raw = pd.read_excel('shop.xlsx')

# cleaning the data

table = table_raw.set_index('city')

# inputs

product = input()
city = input()
quantity = float(input())

# getting the cell

get_price = table.loc[city][product]
total_price = get_price * quantity

# output

print(total_price)

