# Pairs.py
# Name: Razeen
# Student Number: BRYRAZ002
# Date: 20/04/23


count = 0
def consec (s, w):
    global count
    if len(s) == 0:
        print('Number of pairs:', count)
    
    else:
        '''if char1 = char 2'''
        if s[0] == s[1]:
            count += 1
            return consec (s[2::], w)
        '''if char1 != char2'''
        if s[0] != s[1]:
            return consec(s[2::],w )
        #------------------
        
        '''if char1 = char 2'''
        if w[1] == w[2]:
            count += 1
            return consec (s,w[3::])
        '''if char1 != char2'''
        if w[1] != w[2]:
            return consec(s,w[3::])                
        #------------------
inp = input(('Enter a message:\n'))
s = inp
w = inp
consec(s, w)