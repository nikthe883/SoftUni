
number_loads = int(input())

van = 0
truck = 0
train = 0
total_price = 0

for i in range(number_loads):
    load = int(input())
    if load <= 3:
        van += load
        total_price += 200 * load
    elif load >= 12:
        train += load
        total_price += 120 * load
    else:
        truck += load
        total_price += 175 * load

total_tons = van + truck + train
average_price_per_ton = total_price / total_tons

print(f"{average_price_per_ton:.2f}\n"
      f"{van/total_tons*100:.2f}%\n"
      f"{truck/total_tons*100:.2f}%\n"
      f"{train/total_tons*100:.2f}%")
