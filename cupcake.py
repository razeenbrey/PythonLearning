# Decision Tree of a dropped cupcake
# Name: Razeen
# Student Number: BRYRAZ002
# Date: 06/03/23

print('Welcome to the 30 Second Rule Expert')
print('------------------------------------')
print('Answer the following questions by selecting from among the options.')

Dec_0 = 'Decision: Eat it.'
Dec_1 = 'Decision: Don\'t eat it.'
Dec_3 = 'Decision: Your call.'

seen = input('Did anyone see you? (yes/no)\n')
if seen == 'yes':
    BLP = input('Was it a boss/lover/parent? (yes/no)\n')
    if BLP == 'no':
        print(Dec_0)
    if BLP == 'yes':

        exp = input('Was it expensive? (yes/no)\n')
        if exp == 'yes':
            floor = input('Can you cut off the part that touched the floor? (yes/no)\n')
            if floor == 'no':
                print(Dec_3)
            if floor == 'yes':
                print(Dec_0)

        if exp == 'no':
            choc = input('Is it chocolate? (yes/no)\n')
            if choc == 'yes':
                print(Dec_0)
            if choc == 'no':
                print(Dec_1)

if seen == 'no':

    sticky = input('Was it sticky? (yes/no)\n')
    if sticky == 'yes':
        raw = input('Is it a raw steak? (yes/no)\n')
        if raw == 'yes':
            
            puma = input('Are you a puma? (yes/no)\n')
            if puma == 'yes':
                print(Dec_0)
            if puma == 'no':
                print(Dec_1)
                
        if raw == 'no':
            c_lick = input('Did the cat lick it? (yes/no)\n')
            if c_lick == 'no':
                print(Dec_0)
            if c_lick == 'yes':
                c_health = input('Is your cat healthy? (yes/no)\n')
                if c_health == 'yes':
                    print(Dec_0)
                if c_health == 'no':
                    print(Dec_3)
    if sticky == 'no':
        E_dino = input('Is it an Emausaurus? (yes/no)\n')
        if E_dino == 'yes':
            M_dino = input('Are you a Megalosaurus? (yes/no)\n')
            if M_dino == 'yes':
                print(Dec_0)
            if M_dino == 'no':
                print(Dec_1)
        if E_dino == 'no':
            c_lick2 = input('Did the cat lick it? (yes/no)\n')
            if c_lick2 == 'no':
                print(Dec_0)
            if c_lick2 == 'yes':
                c_health2 = input('Is your cat healthy? (yes/no)\n')
                if c_health2 == 'yes':
                    print(Dec_0)
                if c_health2 == 'no':
                    print(Dec_3)