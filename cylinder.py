# Cylinder volume calculator
# Name: Razeen
# Student Number: BRYRAZ002
# Date: 03/04/23

import math 

def circle_area(diameter):
    '''Calculating area of cylinder base'''
    A = 0.25 * math.pi * diameter**2
    return float(A)

def cylinder_volume(A, height):
    '''Calculating volume of cylinder using
    height and value from circle_area (A)'''
    V = A * height
    return float(V)

def main():
    '''main function collecting input and
    displaying output'''
    diameter = int(input('Enter diameter: \n'))
    height = int(input('Enter height: \n'))
    Area = circle_area(diameter)
    Volume = cylinder_volume(Area, height)
    print ('The volume of the cylinder is', "%.2f" %round(Volume, 2))

if __name__=='__main__':
    main()