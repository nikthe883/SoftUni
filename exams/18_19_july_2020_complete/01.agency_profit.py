
company_name = input()
number_adults_tickets = int(input())
number_children_tickets = int(input())
price_for_adult_ticket = float(input())
price_service = float(input())

price_children_ticket = price_for_adult_ticket * 0.30

total_price_adult_tickets = number_adults_tickets * (price_for_adult_ticket + price_service)
total_price_children_tickets = number_children_tickets * (price_children_ticket + price_service)

total_price = total_price_adult_tickets + total_price_children_tickets
profit = total_price * 0.20

print(f"The profit of your agency from {company_name} tickets is {profit:.2f} lv.")