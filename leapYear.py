# Leap Year calculator
# Razeen Brey (BRYRAZ002)
# 28/02/23

year = int(input('Enter a year: \n'))

if year % 400 == 0:
    print(year, "is a leap year.")

if year % 4 == 0 and not year % 100 == 0:
    print(year, 'is a leap year.')

else:
    if year == 2000:
        pass
    else:
        print(year, 'is not a leap year.')