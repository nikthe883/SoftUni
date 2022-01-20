
cake_width = int(input())
cake_length = int(input())

cake_pieces = cake_length * cake_width

while cake_pieces > 0:
    pieces = input()
    if pieces == "STOP":
        break
    pieces_int = int(pieces)
    cake_pieces -= pieces_int

if cake_pieces >= 0:
    print(f"{cake_pieces} pieces are left.")
else:
    print(f"No more cake left! You need {abs(cake_pieces)} pieces more.")

