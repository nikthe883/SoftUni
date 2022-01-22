
number_months = int(input())

electricity_price = 0
water_price = 0
internet_price = 0


for _ in range(number_months):

    electricity_price += float(input())
    water_price += 20
    internet_price += 15


others = (electricity_price + water_price + internet_price) * 1.20
total_price = electricity_price + water_price + \
                internet_price + others
average_per_month = total_price / number_months

print(f"Electricity: {electricity_price:.2f} lv\n"
      f"Water: {water_price:.2f} lv\n"
      f"Internet: {internet_price:.2f} lv\n"
      f"Other: {others:.2f} lv\n"
      f"Average: {average_per_month:.2f} lv")
