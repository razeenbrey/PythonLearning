# anagramsets.py
# Name: Razeen
# Student Number: BRYRAZ002
# Date: 03/05/23

print('***** Anagram Set Search *****')
inp = int(input('Enter word length:\n'))
print('Searching...')

file = input('Enter file name:\n')

try:
    # Open, read, close file
    file = open('EnglishWords.txt', 'r')
    words = file.read()
    file.close()
    
    # Convert file input to list
    x = words.find('START')
    words = words[(x+6)::]
    words_lst = words.split('\n')
    lst_new = []
    
    for w in words_lst:
        if len(w) == inp:
            lst_new.append(w)
            
    dlist = []
    for w in lst_new:
        d={}
        for l in w:
            
            if l in d:
                d.update({l:d[l]+1})
            if l not in d:
                d.update({l:1})            
        dlist.append(d)
    
    ana_lst = []
    for x in dlist:
        for y in dlist:
            if y == x:
                ana_lst.append(words_lst[dlist.index(y)])
    print(ana_lst)
    
    # Create file and write
    f = open(file, "x")
    f.write(ana_lst)
    f.close()    
    
            
    
finally:
    import sys
    sys.exit()    