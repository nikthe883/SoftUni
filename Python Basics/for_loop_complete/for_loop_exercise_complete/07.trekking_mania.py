
number_of_groups = int(input())

musala = 0
mont_blanc = 0
kilimanjaro = 0
k2 = 0
everest = 0
total_people = 0


for i in range(number_of_groups):

    number_of_people_per_group = int(input())
    total_people += number_of_people_per_group

    if number_of_people_per_group <= 5:
        musala += number_of_people_per_group
    elif 6 <= number_of_people_per_group <= 12:
        mont_blanc += number_of_people_per_group
    elif 13 <= number_of_people_per_group <= 25:
        kilimanjaro += number_of_people_per_group
    elif 26 <= number_of_people_per_group <= 40:
        k2 += number_of_people_per_group
    else:
        everest += number_of_people_per_group

musala_percent = musala / total_people * 100
mont_blanc_percent = mont_blanc / total_people * 100
kilimanjaro_percent = kilimanjaro / total_people * 100
k2_percent = k2 / total_people * 100
everest_percent = everest / total_people * 100

print(f"{musala_percent:.02f}%\n"
      f"{mont_blanc_percent:.02f}%\n"
      f"{kilimanjaro_percent:.02f}%\n"
      f"{k2_percent:.02f}%\n"
      f"{everest_percent:.02f}%")
