
rent = float(input())

cake = rent * 0.20
drinks = cake - (cake * 0.45)
animator = rent / 3

total_price = rent + cake + drinks + animator

print(f"{total_price:.2f}")
