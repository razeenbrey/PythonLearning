# Calendar generator
# Name: Razeen
# Student Number: BRYRAZ002
# Date: 17/03/23

m = str(input('Enter the name of a month (e.g. January, ..., December):\n'))
sd = int(input('Enter the start day (1 for Monday, ..., 7 for Sunday):\n'))

# Calendar String
grd = ''
# Month Grouping by number of days
months_30_lst = ['April', 'June', 'September', 'November']
months_31_lst = ['January', 'March', 'May', 'July', 'August', 'October', 'December']

# Month-end Detector
if m in months_30_lst:
    x = 30
    
if m in months_31_lst:
    x = 31
    
if m == 'February':
    x = 28

if sd < 1 or sd > 7:
    print('Invalid calendar: you have either entered an incorrect month name or start day.')
    quit()

if m in months_30_lst or m in months_31_lst or m== 'February' and sd>=1 and sd<=7:
    print(m)
    print('Mo Tu We Th Fr Sa Su')
    if m == 'February':
        print()
    # Blank Days
    if sd == 1:
        grd += ''
    
    if sd == 2:
        grd += '   '
    
    if sd == 3:
        grd += '      '
    
    if sd == 4:
        grd += '         '
    
    if sd == 5:
        grd += '            '
    
    if sd == 6:
        grd += '               '
    
    if sd == 7:
        grd += '                  '    
    
    if sd > 5:
        # Week 1
        for i in range(1, 9-sd):
            grd += ' '
            grd += str(i)
            grd += ' ' 
        grd += '\n'
        # Week 2        
        for i in range(9-sd, 16-sd):
            if i < 10 and i > -1:
                grd += ' '
                grd += str(i)
                grd += ' ' 
            else:
                grd += str(i)
                grd += ' '  
        grd += '\n'
        # Week 3         
        for i in range(16-sd,23-sd):
            if i < 10 and i > -1:
                grd += ' '
                grd += str(i)
                grd += ' ' 
            else:
                grd += str(i)
                grd += ' '              
        grd += '\n'
        # Week 4         
        for i in range(23-sd,30-sd):
            grd += str(i)
            grd += ' '        
        grd += '\n'
        # Week 5        
        for i in range(30-sd,x-1):
            grd += str(i)
            grd += ' '
        grd += '\n'
        # Week 6        
        for i in range(x-1,x+1):
            grd += str(i)
            grd += ' '
    
        print(grd)                       
        
# Week Generators sd != 6 or 7
    if sd <6:
        # Week 1
        for i in range(1, 9-sd):
            grd += ' '
            grd += str(i)
            grd += ' ' 
        grd += '\n'
        # Week 2        
        for i in range(9-sd, 16-sd):
            if i < 10 and i > -1:
                grd += ' '
                grd += str(i)
                grd += ' ' 
            else:
                grd += str(i)
                grd += ' '  
        grd += '\n'
        # Week 3         
        for i in range(16-sd,23-sd):
            if i < 10 and i > -1:
                grd += ' '
                grd += str(i)
                grd += ' ' 
            else:
                grd += str(i)
                grd += ' '              
        grd += '\n'
        # Week 4         
        for i in range(23-sd,30-sd):
            grd += str(i)
            grd += ' '        
        grd += '\n'
        # Week 5        
        for i in range(30-sd,x+1):
            grd += str(i)
            grd += ' '             
    
        print(grd)                
        
else:
    print('Invalid calendar: you have either entered an incorrect month name or start day.')