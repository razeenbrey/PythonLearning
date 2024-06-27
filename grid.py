# Grid printer
# Name: Razeen
# Student Number: BRYRAZ002
# Date: 16/03/23

i_num = int(input('Enter a number between -6 and 2:\n'))
r_len = 7
grd = ''

if i_num <= -6 or i_num >= 2:
    ver = 1
    print('Invalid input! The value of \'n\' should be between -6 and 2.')
    quit()    
    
else:
    for i in range (i_num, i_num + r_len):
        # Negative or double digit
        if i<0 or i>= 10:
            grd += str(i)
            grd += ' '
        # Single digit (incl 0)
        elif i < 10 and i > -1:
            grd += ' '
            grd += str(i)
            grd += ' '
    grd += '\n'
        
    for j in range (i_num +7, i_num + 7 + r_len):
        # Negative or double digit
        if j<0 or j>= 10:
            grd += str(j)
            grd += ' '
        # Single digit (incl 0)
        elif j < 10 and j > -1:
            grd += ' '
            grd += str(j)
            grd += ' '
    grd += '\n'

    for k in range (i_num+14, i_num+14+ r_len):
            if k>= 10:
                grd += str(k)
                grd += ' '
            elif k < 10 and k > -1:
                grd += ' '
                grd += str(k)
                grd += ' '            
    grd += '\n'        
    
    for l in range (i_num+21, i_num+21+ r_len):
        if l>= 10:
            grd += str(l)
            grd += ' '
    grd += '\n'
    
    for m in range (i_num+28, i_num+28+ r_len):
        if m>= 10:
            grd += str(m)
            grd += ' '  
    grd += '\n'
    
    for n in range (i_num+35, i_num+35+ r_len):
        if n>= 10:
            grd += str(n)
            grd += ' '   
    grd += '\n'    

print(grd)