from math import floor

biscuits_for_worker = int(input())
count_workers = int(input())
competing_factory_biscuits = int(input())

total_biscuits = 0

for production in range(1, 31):
    total_biscuits_per_day = biscuits_for_worker * count_workers

    if production % 3 == 0:
        total_biscuits_per_day = floor(total_biscuits_per_day * 0.75)

    total_biscuits += total_biscuits_per_day

print(f"You have produced {total_biscuits} biscuits for the past month.")

if total_biscuits > competing_factory_biscuits:
    diff = total_biscuits - competing_factory_biscuits
    percent_change = diff/competing_factory_biscuits * 100
    print(f"You produce {percent_change:.2f} percent more biscuits.")
else:
    diff = competing_factory_biscuits - total_biscuits
    percent_change = diff / competing_factory_biscuits * 100
    print(f"You produce {percent_change:.2f} percent less biscuits.")
