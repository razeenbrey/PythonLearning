# Calendar Skeleton Generator
# Name: Razeen
# Student Number: BRYRAZ002
# Date: 03/04/23

import math


def day_of_week(day, month, year):
    '''Given day of month, month no. and year;
    return day of week month falls on; 1=Monday...'''
    
    d = day
    m = month
    y = year
    
    if m == 1 or m == 2:
        m += 12
        y -= 1
    h = (d + math.floor( (13*(m+1)) /5) + y + math.floor((y/4)) - math.floor((y/100)) + math.floor((y/400))) % 7
    dayweek = ((h + 5) % 7) + 1
    return dayweek


def is_leap(year):
    '''If leap year, return true'''
    
    if year % 400 == 0:
        notleap = True
    
    if year % 4 == 0 and not year % 100 == 0:
        notleap = True
    
    else:
        if year == 2000:
            pass
        else:
            notleap = False
    return notleap

def month_num(month_name):
    '''return month number 1 = January'''
    month_name = month_name.lower()
    months = ['', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    month_num = (months.index(month_name))
    return month_num

def num_days_in(month_num, year):
    '''return number of days in month'''
    D31 = [1,3,5,7,8,10,12]
    D30 = [4,6,9,11]
    if month_num in D31:
        num_days = 31
    if month_num in D30:
        num_days = 30
    if month_num == 2:
        leap = is_leap(year)
        if leap == False:
            num_days = 28
        if  leap == True:
            num_days = 29
    return num_days

def num_weeks(month_num, year):
    '''return number of weeks month spans'''
    
    y = num_days_in(month_num, year)
    x = day_of_week(1, month_num, year)
    reval = [0, 7, 6, 5, 4, 3, 2, 1]
    weeks = 0
    x = reval.index(x)
    y = (y - x)
    weeks += 1
        
    while y > 7:
        y = y- 7
        weeks += 1
    weeks += 1
    return weeks


def week(week_num, start_day, days_in_month):
    ''' '''
    days = ['', ' 1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
    reval = [0, 7, 6, 5, 4, 3, 2, 1]
    x = reval[start_day]
    weekstr = ''
    if week_num == 1:
        space = '  '
        weekstr += (space*(start_day-1))
        for i in range ((7 - start_day)+1):
            i = i + start_day
            weekstr += days[i]
        return weekstr


def main():
    ''''''
    moninp = input('Enter a month:\n')
    yrinp = input('Enter a year:\n')
    days = num_days_in(month_num(moninp), yrinp)
    outweek = week()

if __name__=='__main__':
    main()