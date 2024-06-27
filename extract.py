# Extract Data from block
# Name: Razeen
# Student Number: BRYRAZ002
# Date: 03/04/23

def location(block):
    '''Slice and return location'''
    num = block.find('END')
    num2 = block.find('S')
    loc = block[(num2 + 1):(num-1):]
    rev = loc[::-1]
    return rev.title()


def temperature(block):
    '''Slice and return temp'''
    temp = (block[6:block.find('_'):])
    return temp


def x_coordinate(block):
    '''Slice and return x-coord'''
    x_co = block[block.find(':')+1:block.find(','):]
    return x_co


def y_coordinate(block):
    '''Slice and return y-coord'''
    y_co = block[block.find(',')+1:27:]
    return y_co


def pressure(block):
    '''Slice and return pressure'''
    pres = float(block[block.find('_')+1:block.find(':'):])
    return pres


def get_block(data):
    '''Extract data and store as block'''
    raw_data = data [data.find('BEGIN'):data.find('END')+3:]
    return raw_data


def main():
    data = str(input('Enter the raw data:\n'))
    block = get_block(data)
    print('Site information:')
    print('Location:', location(block))
    print('Coordinates:', y_coordinate(block), x_coordinate(block))
    print('Temperature: {:.2f} C'.format(float(temperature(block))))
    print('Pressure: {:.2f} hPa'.format(pressure(block)))

if __name__=='__main__':
    main()