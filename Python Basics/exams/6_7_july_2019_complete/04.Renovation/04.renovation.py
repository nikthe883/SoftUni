
wall_h = int(input())
wall_l = int(input())
no_paint = int(input())

total_to_paint = wall_l * wall_h * 4
total_to_paint *= 1 - no_paint / 100


while True:
    paint = input()

    if paint == "Tired!":
        print(f"{total_to_paint:.0f} quadratic m left.")
        break

    total_to_paint -= int(paint)

    if total_to_paint < 0:
        left = abs(total_to_paint)
        print(f"All walls are painted and you have {left:.0f} l paint left!")
        break

    elif total_to_paint == 0:
        print("All walls are painted! Great job, Pesho!")
        break
