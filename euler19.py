# You are given the following information, but you may prefer to do some research for yourself.
#
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?


startyear = 1901
endyear = 2000
daysinmonth = [31,28,31,30,31,30,31,31,30,31,30,31]




def isLeapYear(year):
    isLeapYear = False
    if year % 4 == 0 and (not year % 100 == 0 or year % 400 == 0):
        isLeapYear = True
    return isLeapYear
day = (1 + 365 + int(isLeapYear(1900))) % 7  # given that 1 jan 1900 is on monday=1

print(isLeapYear(1900))
sundayCounter = 0
for year in range(startyear,endyear+1):

    for month in range(12):
        if day == 0:
            sundayCounter += 1
            print(month, year)
        day = day + daysinmonth[month]
        if month == 1 :
            day += 1
        day = day % 7


    pass
    # print(year, isLeapYear)

print(sundayCounter)