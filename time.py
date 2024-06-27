# Time validator
# Razeen Brey (BRYRAZ002)
# 29/02/23

h = int(input('Enter the hours: '))
m = int(input('Enter the minutes: '))
s = int(input('Enter the seconds: '))
ver = 0

if h>=0 and h<= 23:
        ver += 1
if m>=0 and m<=59:
        ver += 1
if s>=0 and s<=59:
        ver += 1
if ver == 3:
        print('Your time is valid.')

else:
        print("Your time is invalid.")