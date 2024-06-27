# Triangle area calculator
# Razeen Brey (BRYRAZ002)
# 27/02/23

import math
a = float(input("Enter the length of the first side: "))
b = float(input("Enter the length of the second side: "))
c = float(input("Enter the length of the third side: "))

s = (a + b + c) / 2

if s <= a or s <= b or s <= c or s == 0:
    print("Error: The input does not describe a triangle.")

else:
    calc = s * (s - a) * (s - b) * (s - c)
    area = math.sqrt(calc)
    area_rnd = round(area, 2)
    print('The area of the triangle with sides of length', a, 'and', b, 'and', c, 'is', area_rnd, end='')
    print('.')