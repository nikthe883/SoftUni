
btc_number = int(input())
ioan_number = float(input())
commission = float(input())

total_btc_lv = btc_number * 1168
total_ioan_lv = ioan_number * 0.15 * 1.76
total_eur = (total_ioan_lv + total_btc_lv) / 1.95
total_eur = total_eur - ( total_eur * commission / 100)

print(f"{total_eur:.2f}")
