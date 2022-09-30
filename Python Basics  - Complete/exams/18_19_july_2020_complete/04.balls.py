from math import floor

n = int(input())

counter = 0
total_points = 0
red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
other_colors = 0
divides_from_black_balls = 0

while counter < n:
    counter +=1
    ball_color = input()
    if ball_color == "red":
        total_points += 5
        red_balls += 1
    elif ball_color == "orange":
        total_points += 10
        orange_balls += 1
    elif ball_color == "yellow":
        total_points += 15
        yellow_balls += 1
    elif ball_color == "white":
        total_points += 20
        white_balls += 1
    elif ball_color == "black":
        total_points *= 0.5
        divides_from_black_balls += 1
    else:
        other_colors += 1

print(f"Total points: {floor(total_points)}\n"
      f"Red balls: {red_balls}\n"
      f"Orange balls: {orange_balls}\n"
      f"Yellow balls: {yellow_balls}\n"
      f"White balls: {white_balls}\n"
      f"Other colors picked: {other_colors}\n"
      f"Divides from black balls: {divides_from_black_balls}")

