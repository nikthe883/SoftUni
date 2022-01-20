

detergent = int(input()) * 750
loops = 0
washed_pots = 0
washed_dishes = 0



while detergent >= 0:

    number_dishes = input()
    if number_dishes == "End":
        break

    number_dishes_int = int(number_dishes)
    loops += 1
    if loops % 3 == 0:
        detergent -= number_dishes_int * 15
        washed_pots += number_dishes_int
    else:
        detergent -= number_dishes_int * 5
        washed_dishes += number_dishes_int



if detergent < 0:
    print(f"Not enough detergent, {abs(detergent)} ml. more necessary!")
else:
    print(f"Detergent was enough!\n"
          f"{washed_dishes} dishes and {washed_pots} pots were washed.\n"
          f"Leftover detergent {abs(detergent)} ml.")
