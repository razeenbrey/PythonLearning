# 12/24 Time Converter
# Name: Razeen
# Student Number: BRYRAZ002
# Date: 17/03/23

inp = input('Enter the date and time (yyyy-mm-dd hh:mm):\n')
months_lst = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# Deriving values from input string for calc
hr = int(inp [11:13:])
date = inp [8:10:]
month = months_lst[int(inp[5:7:])]
yr = str(inp[2:4:])

# Find date suffix
# For 11 to 19
date_1 = int(inp[8:9:])
if date_1 == 1:
    date_suf = 'th'
# 19 onwards
else:
    date_num = int(date[1::])
    if date_num == 0 or date_num > 3:
        date_suf = 'th'
    if date_num == 1:
        date_suf = 'st'
    if date_num == 2:
        date_suf = 'nd'
    if date_num == 3:
        date_suf = 'rd'    
  
# am or pm and 24-12 conversion
if hr == 0:
    ToD = 'am'
    hr += 12
    
else:
    if hr == 12:
        ToD = 'pm'
        
    if hr >0 and hr<12:
        ToD = 'am'
        
    if hr >=13 and hr<=23:
        ToD = 'pm'
        hr-=12    

print(hr, inp[13:16:], ' ', ToD, ' on the ', int(date), date_suf, ' of ', month, ' \'', yr, sep='')