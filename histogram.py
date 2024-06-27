# histogram.py
# Name: Razeen
# Student Number: BRYRAZ002
# Date: 21/04/23

fail  = 0
third = 0
l2nd  = 0
u2nd  = 0
first = 0

marks = str(input('Enter a space-separated list of marks:\n'))
marks_lst = marks.split(' ')

for m in range(len(marks_lst)):
    if int(marks_lst[m]) <50 and int(marks_lst[m])>=0:
        fail += 1
    if int(marks_lst[m]) >= 50 and int(marks_lst[m]) <60:
        third += 1
    if int(marks_lst[m]) >= 60 and int(marks_lst[m]) <70:
        l2nd += 1
    if int(marks_lst[m]) >= 70 and int(marks_lst[m]) <75:
        u2nd += 1
    if int(marks_lst[m]) >= 75 and int(marks_lst[m]) <101:
        first += 1

print('1 |',(first*'X'), sep ='')
print('2+|',(u2nd*'X'), sep ='')
print('2-|',(l2nd*'X'), sep ='')
print('3 |',(third*'X'), sep ='')
print('F |',(fail*'X'), sep ='')