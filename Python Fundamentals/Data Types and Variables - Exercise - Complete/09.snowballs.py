n = int(input())

snowball_weight_best = 0
snowball_time_best = 0
snowball_quality_best = 0
snowball_value_best = 0

for _ in range(n):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_value = (snowball_weight / snowball_time) ** snowball_quality

    if snowball_value > snowball_value_best:
        snowball_weight_best = snowball_weight
        snowball_time_best = snowball_time
        snowball_quality_best = snowball_quality
        snowball_value_best = snowball_value

print(f"{snowball_weight_best} : {snowball_time_best} = {snowball_value_best:.0f} ({snowball_quality_best})")
