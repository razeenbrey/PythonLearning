# anagramsearch.py
# Name: Razeen
# Student Number: BRYRAZ002
# Date: 03/05/23

print('***** Anagram Finder *****')

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
    
    # Convert words to dictionary of letters
    for w in words_lst:
        d={}
        for l in w:
            
            if l in d:
                d.update({l:d[l]+1})
            if l not in d:
                d.update({l:1})            
        lst_new.append(d)
        
    # Take input and convert into dictionary of letters          
    search = input('Enter a word: ')
    search = search.lower()
    k = {}
    for s in search:
        if s in k:
            k.update({s:k[s]+1})
        if s not in k:
            k.update({s:1})
            
    # Loop through array of dictionaries to find anagrams of <search>
    ana_lst = []
    for v in lst_new:
        if v == k:
            ana_lst.append(words_lst[lst_new.index(v)])
    
    if len(ana_lst) == 0:
        print('Sorry, anagrams of \'', search,'\' could not be found.', sep = '')
    else:
        print(ana_lst)
    

except IOError:
    print('Sorry, could not find file \'EnglishWords.txt\'.')

finally:  
        
    import sys
    sys.exit()    