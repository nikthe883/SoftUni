# inputs

budget = float(input())
category = input()
number_people = int(input())

# variables

vip = 499.99
normal = 249.99

# transport cost in percentage

one_to_four_people = 0.75
five_to_nine_people = 0.60
ten_to_twenty_four_people = 0.50
twenty_five_to_forty_nine_people = 0.40
above_fifty_people = 0.25


# alternative
def output(remaining_budget, vip_b):

    if vip_b:

        ticket_cost = number_people * vip
        if ticket_cost <= remaining_budget:
            money_left = remaining_budget - ticket_cost
            return f"Yes! You have {money_left:.2f} leva left."

        else:
            money_needed = ticket_cost - remaining_budget
            return f"Not enough money! You need {money_needed:.2f} leva."
    else:
        ticket_cost = number_people * normal
        if ticket_cost <= remaining_budget:
            money_left = remaining_budget - ticket_cost
            return f"Yes! You have {money_left:.2f} leva left."
        else:
            money_needed = ticket_cost - remaining_budget
            return f"Not enough money! You need {money_needed:.2f} leva."


def decisions(categoryf, number_peoplef, budgetf):
    vip_b = False
    if category == "VIP":
        vip_b = True

    if number_people in range(1, 5):
        transport_cost = budget * one_to_four_people
        remaining_budget = budget - transport_cost
        return output(remaining_budget, vip_b)
    elif number_people in range(5, 10):
        transport_cost = budget * five_to_nine_people
        remaining_budget = budget - transport_cost
        return output(remaining_budget, vip_b)
    elif number_people in range(10, 25):
        transport_cost = budget * ten_to_twenty_four_people
        remaining_budget = budget - transport_cost
        return output(remaining_budget, vip_b)
    elif number_people in range(25, 50):
        transport_cost = budget * twenty_five_to_forty_nine_people
        remaining_budget = budget - transport_cost
        return output(remaining_budget, vip_b)
    else:
        transport_cost = budget * above_fifty_people
        remaining_budget = budget - transport_cost
        return output(remaining_budget, vip_b)


smt = decisions(category, number_people, budget)
print(smt)

# and copy and paste

# # decisions
#
# if number_people <= 4:
#     transport_cost = budget * one_to_four_people
#     remaining_budget = budget - transport_cost
#     if category == "VIP":
#         ticket_cost = number_people * vip
#         if ticket_cost <= remaining_budget:
#             money_left = remaining_budget - ticket_cost
#             print(f"Yes! You have {money_left} leva left.")
#         else:
#             money_needed = ticket_cost - remaining_budget
#             print(f"Not enough money! You need {money_needed} leva.")
#     else:
#         ticket_cost = number_people * vip
#         if ticket_cost <= remaining_budget:
#             money_left = remaining_budget - ticket_cost
#             print(f"Yes! You have {money_left} leva left.")
#         else:
#             money_needed = ticket_cost - remaining_budget
#             print(f"Not enough money! You need {money_needed} leva.")
