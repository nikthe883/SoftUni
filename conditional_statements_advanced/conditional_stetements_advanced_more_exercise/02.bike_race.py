# inputs

number_junior_cyclists = int(input())
number_senior_cyclists = int(input())
trace_kind = input()

# variables

# juniors

junior_trail_tax = 5.50
junior_cross_country_tax = 8
junior_downhill_tax = 12.25
junior_road_tax = 20

# seniors

senior_trail_tax = 7
senior_cross_country_tax = 9.50
senior_downhill_tax = 13.75
senior_road_tax = 21.50

# discounts

discount = 0.25

# variables

total_number_cyclists = number_junior_cyclists + number_senior_cyclists
donation_money = 0

# decisions

if trace_kind == "trail":
    money_before_expenses = number_junior_cyclists * junior_trail_tax + \
                            number_senior_cyclists * senior_trail_tax
    total_expenses = money_before_expenses * 0.05
    donation_money = money_before_expenses - total_expenses

elif trace_kind == "cross-country":
    money_before_expenses = number_junior_cyclists * junior_cross_country_tax + \
                            number_senior_cyclists * senior_cross_country_tax

    if total_number_cyclists >= 50:
        money_before_expenses = money_before_expenses - (money_before_expenses * discount)
        total_expenses = money_before_expenses * 0.05
        donation_money = money_before_expenses - total_expenses

    else:
        total_expenses = money_before_expenses * 0.05
        donation_money = money_before_expenses - total_expenses

elif trace_kind == "downhill":
    money_before_expenses = number_junior_cyclists * junior_downhill_tax + \
                            number_senior_cyclists * senior_downhill_tax
    total_expenses = money_before_expenses * 0.05
    donation_money = money_before_expenses - total_expenses

elif trace_kind == "road":
    money_before_expenses = number_junior_cyclists * junior_road_tax + \
                            number_senior_cyclists * senior_road_tax
    total_expenses = money_before_expenses * 0.05
    donation_money = money_before_expenses - total_expenses

print(f'{donation_money:.2f}')



