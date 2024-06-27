# gridio.py
# Name: Razeen
# Student Number: BRYRAZ002
# Date: 18/04/23

def genray ():
    '''Genterates array'''
    array = []
    print('Enter an array:')
    for i in range(9):
        array.append(input(''))
    
    return array

def findco (ray):
    '''Finds and returns coordinate values'''
    coords = ''
    ray = ray
    coords = str(input('Enter coordinates:\n'))
    while coords!= '-1 -1':
        co = coords.split(' ')
        val = ray[(int(co[0]))][(int(co[1]))]
        print('Value =', val)
        coords = str(input('Enter coordinates:\n'))
    else:
        print('DONE')
    

def main ():
    '''Main program'''
    array = genray()
    findco(array)

if __name__ == '__main__':
    main()