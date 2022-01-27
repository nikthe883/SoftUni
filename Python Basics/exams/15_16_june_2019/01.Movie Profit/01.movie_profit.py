
movie_name = input()
number_days = int(input())
number_tickets = int(input())
ticket_price = float(input())
theater_cut = int(input())

profit_for_day = number_tickets * ticket_price
profit = profit_for_day * number_days
profit = profit - (theater_cut * profit) / 100

print(f"The profit from the movie {movie_name} is {profit:.2f} lv.")
