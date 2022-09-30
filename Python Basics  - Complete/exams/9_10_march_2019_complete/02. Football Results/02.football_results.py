

won = 0
lost = 0
draw = 0

for i in range(3):
    result = input()

    if result[0] > result[2]:
        won += 1
    elif result[0] < result[2]:
        lost += 1
    else:
        draw += 1
print(f"Team won {won} games.\n"
f"Team lost {lost} games.\n"
f" Drawn games: {draw}"
)

