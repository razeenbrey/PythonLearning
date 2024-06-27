# Perfect number detector
# Name: Razeen
# Student Number: BRYRAZ002
# Date: 06/03/23

num = int(input('Enter a number:\n'))
# Save original input
int_orig = num
int_sum = 0

print('The proper divisors of', num, 'are:')
# Find and print proper divisors
for i in range (1,num):
    if num%i == 0:
        int_sum += i
        print(i, ' ', sep='', end='')
print()
print()
# Determine if input is a perfect number
if int_sum == int_orig:
    print(int_orig, 'is a perfect number.')
else: print(int_orig, 'is not a perfect number.')