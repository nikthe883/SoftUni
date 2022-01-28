
number_breads = int(input())
number_eggs = int(input())
cookies_kg = int(input())

total_price_breads = number_breads * 3.20
total_price_eggs = number_eggs * 4.35
total_price_cookies = cookies_kg * 5.40
total_price_paint = 12 * number_eggs * 0.15

total_price = total_price_paint + total_price_cookies +\
                total_price_breads + total_price_eggs

print(f"{total_price:.2f}")
