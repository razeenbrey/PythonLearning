# Bulletin Board System
# Name: Razeen
# Student Number: BRYRAZ002
# Date: 15/03/23

# Cursor to navigate
cursor = ''

File_1 = 'The meaning of life is blah blah blah ...'
File_2 = 'Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy'

# Verification that var 'msg' exists
msg_ver = False

while True:
    # Menu Display
    print('Welcome to UCT BBS')
    print('MENU')
    print('(E)nter a message')
    print('(V)iew message')
    print('(L)ist files')
    print('(D)isplay file')
    print('e(X)it')
    
    cursor = str(input('Enter your selection:\n'))
    
    # Enter Message
    if cursor == 'E' or cursor == 'e':
        msg = str(input('Enter the message:\n'))
        msg_ver = True
   
    # View Message
    elif cursor == 'V'or cursor == 'v':
        if msg_ver == True:
            print('The message is:', msg)
        if msg_ver == False:
            print('The message is: no message yet')
   
    # List Files
    elif cursor == 'L'or cursor == 'l':
        print('List of files: 42.txt, 1015.txt')
   
    # Display Files
    elif cursor == 'D'or cursor == 'd':
        F_name = str(input('Enter the filename:\n'))
        if F_name == '42.txt':
            print(File_1)
        if F_name == '1015.txt':
            print(File_2)
        if F_name != '42.txt' or F_name != '1015.txt':
            print('File not found')
   
    # Exit
    elif cursor == 'X'or cursor == 'x':
        print('Goodbye!')
        break
                    