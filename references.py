# Reference Formatter
# Name: Razeen
# Student Number: BRYRAZ002
# Date: 17/03/23

ref = str(input('Enter the reference:\n'))

# index values
brack = ref.find('(')
brack_2 = ref.find(')')

# detecting 2nd comma
search = ','
oc = 2

comm = ref.find(search)
while comm >= 0 and oc > 1:
  comm = ref.find(search, comm+len(search))
  oc -= 1

# slicing according to index
name = ref [0:brack_2+2:]
title = ref [brack_2+2:comm+1:]
rest = ref [comm+1::]
print('Reformatted reference:')
print(name.title(), title.capitalize(), rest, sep='')