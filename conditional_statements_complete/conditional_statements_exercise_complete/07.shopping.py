# app


budget = float(input())
video_cards = int(input())
processors = int(input())
ram = int(input())

video_cards_price = 250
processors_price = 250 * 0.35 * video_cards
ram_price = 250 * 0.1 * video_cards
discount = 0.15


total_price_video_cards = video_cards * video_cards_price
total_price_processors = processors * processors_price
total_price_ram = ram * ram_price
total_price_basket = total_price_ram + total_price_processors + total_price_video_cards



# check discount

if video_cards > processors:
    total_price_basket = total_price_basket - (total_price_basket * discount)


# check if budge is enough

if budget >= total_price_basket:
    left_over_budget = budget - total_price_basket
    print(f"You have {left_over_budget:.2f} leva left!")

elif total_price_basket > budget:
    short_over_budget = total_price_basket - budget
    print(f"Not enough money! You need {short_over_budget:.2f} leva more!")

