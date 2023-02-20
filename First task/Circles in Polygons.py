
# https://www.codewars.com//kata/5a026a9cffe75fbace00007f

import math


def circle_diameter(sides, side_length):
    diameter = 2 * side_length / (2 * math.tan(math.pi / sides))
    print(math.tan(180 / sides))

    return diameter
