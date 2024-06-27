# vectormath.py
# Name: Razeen
# Student Number: BRYRAZ002
# Date: 20/04/23

import math
import sys

def obt_mag ():
    '''Given x and y components, returns vector magnitude'''
    comps = str(input(('Enter the components of the vector separated by spaces:\n')))
    if len(comps) != 3:
        print('Error: Vectors must have the same length.')
        main()
    comps = comps.split(' ')
    vx = int(comps[0])
    vy = int(comps[1])
    mag = math.sqrt(((vx)**2) + ((vy)**2))
    print('Magnitude of the vector is:', round(mag, 1))
    main()

def v_add ():
    '''given 2 vectors, returns sum'''
    comps0 = str(input('Enter the components of the first vector separated by spaces:\n'))
    comps1 = str(input('Enter the components of the second vector separated by spaces:\n'))
    if len(comps0) != 3 or len(comps1) != 3:
        print('Error: Vectors must have the same length.')
        main()
    else:
        comps0 = comps0.split(' ')
        comps1 = comps1.split(' ')
        vx =  int(comps0[0])
        vy =  int(comps0[1])
        vx1 = int(comps1[0])
        vy1 = int(comps1[1])
        vsumx = vx + vx1
        vsumy = vy + vy1
        print('Sum of the vectors is: (', vsumx, ', ', vsumy, ')', sep='')
        main()

def s_multip ():
    '''multiplies given vector by given scalar'''
    comps = str(input('Enter the components of the vector separated by spaces:\n'))
    m = int(input('Enter the scalar:\n'))
    if len(comps) == 3:
        comps = comps.split(' ')
        vx = int(comps[0])
        vy = int(comps[1])
        print('Scalar multiplication of the vector is: (', (vx*m),  ', ', (vy*m), ')',sep='')
        main()
    if len(comps) == 5:
        comps = comps.split(' ')
        vx = int(comps[0])
        vy = int(comps[1])
        vz = int(comps[2])
        print('Scalar multiplication of the vector is: (', (vx*m),  ', ', (vy*m), ', ', (vz*m), ')',sep='')
        main()      

def d_prod ():
    '''Given 2 vectors, returns the dot product'''
    comps0 = str(input('Enter the components of the first vector separated by spaces:\n'))
    comps1 = str(input('Enter the components of the second vector separated by spaces:\n'))
    if len(comps0) != 3 or len(comps1) != 3:
        print('Error: Vectors must have the same length.')
        main()
    else:
        comps0 = comps0.split(' ')
        comps1 = comps1.split(' ')
        vx =  int(comps0[0])
        vy =  int(comps0[1])
        vx1 = int(comps1[0])
        vy1 = int(comps1[1])
        dprod = ((vx*vx1) + (vy*vy1))
        print('Dot product of the vectors is:', dprod)
    main()

def c_prod ():
    '''Given two 3d vectors, returns the cross product'''
    comps0 = str(input('Enter the components of the first 3-dimensional vector\nseparated by spaces:\n'))
    comps1 = str(input('Enter the components of the second 3-dimensional vector\nseparated by spaces:\n'))
    if len(comps0) != 5 or len(comps1) != 5:
        print('Error: Vectors must have the same length and 3-dimensional.')
        main()
    else:
        comps0 = comps0.split(' ')
        comps1 = comps1.split(' ')
        vx =  int(comps0[0])
        vy =  int(comps0[1])
        vz =  int(comps0[2])
        vx1 = int(comps1[0])
        vy1 = int(comps1[1])
        vz1 = int(comps1[2])
        cprod = [((vy*vz1) - (vz*vy1)), ((vz*vx1) - (vx*vz1)), ((vx*vy1) - (vy*vx1))]
        print('Cross product of the vectors is: (', cprod[0], ', ', cprod[1], ', ', cprod[2], ')', sep='')
    main()

def error ():
    '''Error message for incorrect menu input'''
    print('Invalid choice. Please choose a valid option.')
    main()

def main ():
    '''main menu'''
    print('''Choose an option:
1. Magnitude of a vector
2. Vector addition
3. Scalar multiplication
4. Dot product of two vectors
5. Cross product of two 3-dimensional vectors
6. Exit''')
    option = str(input(''))
    
    if option == '1':
        obt_mag()
    
    if option == '2':
        v_add()
    
    if option == '3':
        s_multip()
    
    if option == '4':
        d_prod()
    
    if option == '5':
        c_prod()
    
    if option == '6':
        print('Exiting...')
        sys.exit()  
    
    else:
        error()

if __name__ == '__main__':
    main()