#Tuition Increase
#At one college, the tuition for a full-time student is $8,000 per semester.
# It has been announced that the tuition will increase by 3 percent each year 
# for the next 5 years. Write a program with a loop that displays the projected 
# semester tuition amount for the next 5 years
tuition_increase = 0.03
tuition = 8000
tuition_total = 0
years = 5

print('tuition_total\tyears')
print('--------')
for years in range (0, years ):
    tuition_total = tuition * (1+tuition_increase)** years
    print('{0:<10} {1}'.format(int(tuition_total), years+1))