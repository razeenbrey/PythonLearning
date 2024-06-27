# tracer.py
# Name: Razeen
# Student Number: BRYRAZ002
# Date: 03/05/23

print("***** Program Trace Utility *****")
file_name = input("Enter the name of the program file: ")
try:
    file = open(file_name, "r")
    words = file.readlines()
    file.close()
    
    
    if "\"\"\"DEBUG\"\"\"" in words[0]:
        words.pop(0)
        key = "r"
        for w in words:
            if "\"\"\"DEBUG\"\"\"" in w:
                words[words.index(w)] = w[15::]
        
    else:
        key = 'w'
        for w in words:
            if "def" in w:
                s = words[words.index(w)+1]
                snew = s[4::]
                words[words.index(w)+1] = "   \"\"\"DEBUG\"\"\";" + snew
                
    if key == "r":
        print("Program contains trace statements")
        print("Removing...Done")
    if key == "w":
        words.insert(0, "\"\"\"DEBUG\"\"\"\n")
        print("Inserting...Done")
        
    file = open(file_name, "w")
    file.writelines(words)
    file.close()
    

finally:
    pass