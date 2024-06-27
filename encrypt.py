# Encrypt.py
# Name: Razeen
# Student Number: BRYRAZ002
# Date: 20/04/23
    
z = ''
def encrypt (s):
    global z
    if len(s) == 0:
        print('Encrypted message:')
        print(z)
        
    if len(s) != 0:
        '''is lower'''
        if (ord(s[0])) >= 97 and ord(s[0]) <=122:
            
            '''is not z'''
            if (ord(s[0])) >= 97 and ord(s[0]) <=121:
                z += chr(((ord(s[0])+1)))
                encrypt ((s[1::]))
            
            '''is z'''
            if (ord(s[0])) == 122:
                z += chr(97)
                encrypt (s[1::])
                
        else:
            '''other'''
            z += s[0]
            encrypt (s[1::])

encrypt((input('Enter a message:\n')))