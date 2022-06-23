days = int(input())
plunder_per_day = int(input())
expected_plunder = float(input())

total_plunder = 0

for i in range(1, days + 1):

    total_plunder += plunder_per_day
    if i % 3 == 0:
        total_plunder += plunder_per_day * 0.5
    if i % 5 == 0:
        total_plunder -= total_plunder * 0.3


if total_plunder >= expected_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    percent = total_plunder/expected_plunder*100
    print(f"Collected only {percent:.2f}% of the plunder.")
