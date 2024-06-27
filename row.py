# Row printer
# Name: Razeen
# Student Number: BRYRAZ002
# Date: 06/03/23

num = int(input('Enter the start number:\n'))

for i in range (num, num+7):
    # For negative numbers
    if i < 0:
        print (i, ' ', sep='', end='')
    # For single digits 
    elif i < 10 and i !=0:
        print (' ', i, ' ', sep='', end='')
    # For zero
    elif i == 0:
        print (' ', i, ' ', sep='', end='')
    # For Double digits
    else:
        print (i, ' ', sep='', end='')