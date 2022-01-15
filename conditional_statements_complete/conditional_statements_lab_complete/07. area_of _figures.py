
# area of figures

# imports

from math import pi

# inputs

figure = input()

# decision

if figure == "square":

    side_a = float(input())

    square_area = side_a * side_a

    print(f'{square_area:.03f}')

elif figure == "rectangle":

    side_a = float(input())
    side_b = float(input())

    rectangle_area = side_a * side_b

    print(f'{rectangle_area:.03f}')

elif figure == "circle":

    r = float(input())

    circle_area = pi * r *r

    print(f'{circle_area:.03f}')

elif figure == "triangle":

    a = float(input())
    h = float(input())

    triangle_area = (a * h) / 2

    print(f'{triangle_area:.03f}')