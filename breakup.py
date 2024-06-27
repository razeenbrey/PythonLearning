# 12/24 Time Converter
# Name: Razeen
# Student Number: BRYRAZ002
# Date: 17/03/23

sen = str(input('Enter a sentence:\n'))
# Container String
ans = ''
# Space counter
n = int(sen.count(' '))

while n != 0:
    x = sen.find(' ')
    ans += str(sen[0:x:])
    ans += ', '
    sen = sen[x+1::]
    n-=1
# Add back remainder of string
ans += sen

print('The word list: ', ans.lower(), '.', sep='')