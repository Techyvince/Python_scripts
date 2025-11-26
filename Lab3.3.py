#  The month of February normally has 28 days. But if it is a leap year, 
#  February has 29 days. Write a program that asks the user to enter a year.
#  The program should then display the number of days in February that year.
#  Use the following criteria to identify leap years:
#  Determine whether the year is divisible by 100. If it is, 
#  then it is a leap year if and only if it is also divisible by 400. 
#  For example, 2000 is a leap year, but 2100 is not.
#  If the year is not divisible by 100, then it is a leap year if and
#  only if it is divisible by 4. For example, 2008 is a leap year, but 2009 is not.
# Here is a sample run of the program:
# Enter a year: 2008  [Enter]
# In 2008 February has 29 days.
# if it is a leap year feb has 29 days 
# if it is not a leap year feb has 28 days
# The following determines whether a year is evenly divisible by
# 100 and 400, or not 100 and 4.
# (year % 100) == 0 and 


year = int(input('Enter a year: '))
if (year % 400) == 0:
    print('February', year, 'has 29 days and is a leap year.')
elif (year % 100) != 0 and (year % 4) == 0:
    print('February', year, 'has 29 days and is a leap year.')
else:
    print('February', year, 'has 28 days and is not a leap year.')

# Asks user to press Enter to exit.
print()
(input('Press ENTER to exit.'))
