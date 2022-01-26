
movie_title = input()
movie_menu = input()
ticket_count = int(input())

ticket_price = 0

if movie_title == "John Wick":
    if movie_menu == "Drink":
        ticket_price = 12
    elif movie_menu == "Popcorn":
        ticket_price = 15
    elif movie_menu == "Menu":
        ticket_price = 19

elif movie_title == "Star Wars":
    if movie_menu == "Drink":
        ticket_price = 18
    elif movie_menu == "Popcorn":
        ticket_price = 25
    elif movie_menu == "Menu":
        ticket_price = 30

else:
    if movie_menu == "Drink":
        ticket_price = 9
    elif movie_menu == "Popcorn":
        ticket_price = 11
    elif movie_menu == "Menu":
        ticket_price = 14

total_price = ticket_price * ticket_count

if movie_title == "Star Wars" and ticket_count >= 4:
    total_price *= 0.70

if movie_title == "Jumanji" and ticket_count == 2:
    total_price *= 0.85

print(f"Your bill is {total_price:.2f} leva.")
