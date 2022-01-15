
# inputs

days = int(input())
room = input()
review = input()

# variables

total_price_no_review = 0
total_price = 0
overnight = days - 1
one_person_room = 18
apartment = 25
president_apartment = 35

# decisions

if room == "room for one person":

    if days < 10:
        total_price_no_review = overnight * one_person_room
    elif 10 <= days <= 15:
        total_price_no_review = overnight * one_person_room
    else:
        total_price_no_review = overnight * one_person_room

elif room == "apartment":

    if days < 10:
        total_price_no_review = (overnight * apartment) - \
                                (overnight * apartment) * 0.3

    elif 10 <= days <= 15:
        total_price_no_review = (overnight * apartment) - \
                                (overnight * apartment) * 0.35
    else:
        total_price_no_review = (overnight * apartment) - \
                                (overnight * apartment) * 0.50

elif room == "president apartment":

    if days < 10:
        total_price_no_review = (overnight * president_apartment) - \
                                (overnight * president_apartment) * 0.1

    elif 10 <= days <= 15:
        total_price_no_review = (overnight * president_apartment) - \
                                (overnight * president_apartment) * 0.15
    else:
        total_price_no_review = (overnight * president_apartment) - \
                                (overnight * president_apartment) * 0.20


if review == 'positive':
    total_price = total_price_no_review + (total_price_no_review * 0.25)

else:
    total_price = total_price_no_review - (total_price_no_review * 0.10)

# output

print(f"{total_price:.2f}")
