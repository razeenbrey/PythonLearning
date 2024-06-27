# Personalised spam message generator
# Razeen Brey (BRYRAZ002)
# 28/02/23

f_name = input('Enter first name:\n')
l_name = input('Enter last name:\n')
usd = eval(input('Enter sum of money in USD:\n'))
cntry = input('Enter country name:\n')

usd_30 = usd * 30/100
usd_rnd = round(usd_30, 2)

print()
print('Dearest', f_name)
print('It is with a heavy heart that I inform you of the death of my father,')
print('General Fayk', l_name, end='')
print(', your long lost relative from Mapsfostol.')
print('My father left the sum of', usd, end = '')
print('USD for us, your distant cousins.')
print('Unfortunately, we cannot access the money as it is in a bank in', cntry, end='')
print('.')
print('I desperately need your assistance to access this money.')
print('I will even pay you generously, 30% of the amount -', usd_rnd, end='')
print('USD,')
print('for your help.  Please get in touch with me at this email address asap.')
print('Yours sincerely')
print('Frank', l_name)