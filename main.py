
from math import pi


figure_name = input()

if figure_name == 'square':
    side_a = float(input())
    area = side_a * side_a
    print(f'{area:.3f}')

elif figure_name == 'rectangle':
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b
    print(f'{area:.3f}')

elif figure_name == 'circle':

    r = float(input())
    area = pi * r * r
    print(f'{area:.3f}')

elif figure_name == 'triangle':
    side_a = float(input())
    h = float(input())
    area = side_a*h / 2
    print(f'{area:.3f}')



#
# # square
# rectangle
# circle
# triangle



