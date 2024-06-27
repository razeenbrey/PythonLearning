# Column printer
# Name: Razeen
# Student Number: BRYRAZ002
# Date: 07/03/23

num = int(input('Enter a number:\n'))

for i in range (num, num+41, 7):
    # For double digits
    if i >= 10:
        print(i)
    # For 0 and i<=9
    elif i >= 0 and i<10:
        print(' ', i, sep='')
    # For negative numbers
    else:
        print(i)