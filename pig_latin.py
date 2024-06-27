# Pig Latin Converter
# Name: Razeen
# Student Number: BRYRAZ002
# Date: 17/03/23

sen = str(input('Enter a sentence:\n'))
ans = ''
sen_lst = sen.split(' ')

vowels = ['a', 'e', 'i', 'o', 'u']

for i in sen_lst:
    if i [0:1:] in vowels:
        v_lat = i + 'way'
        ans += v_lat
        ans += ' '
    else:
        for e in i:
            if e in vowels:
                pass
                x = i.find(e)
                c_lat = i[x::] + 'a' + i[0:x:] + 'ay'
                ans += c_lat
                ans += ' '
                break

print(ans.lower())