import calendar

year=int(input('\n\tEnter the number to check leap : '))

if calendar.isleap(year):
    print(year," is a leap year.")
else:
    print(year," is NOT a leap year.")