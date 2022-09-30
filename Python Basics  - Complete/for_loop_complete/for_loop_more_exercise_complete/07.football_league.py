
stadium_capacity = int(input())
total_number_fens = int(input())

sector_a = 0
sector_b = 0
sector_v = 0
sector_g = 0


for _ in range(total_number_fens):
    sector = input()

    if sector == "A":
        sector_a += 1

    elif sector == "B":
        sector_b += 1

    elif sector == "V":
        sector_v += 1

    else:
        sector_g += 1

percent_sector_a = sector_a / total_number_fens * 100
percent_sector_b = sector_b / total_number_fens * 100
percent_sector_v = sector_v / total_number_fens * 100
percent_sector_g = sector_g / total_number_fens * 100
stadium_fullness = total_number_fens / stadium_capacity * 100

print(f"{percent_sector_a:.2f}%\n"
      f"{percent_sector_b:.2f}%\n"
      f"{percent_sector_v:.2f}%\n"
      f"{percent_sector_g:.2f}%\n"
      f"{stadium_fullness:.2f}%\n")
