#Distance Traveled
#The distance a vehicle travels can be calculated as follows:
#For example, if a train travels 40 miles per hour for three hours,
#the distance traveled is 120 miles. Write a program that asks the
#user for the speed of a vehicle (in miles per hour) and the number
#of hours it has traveled. It should then use a loop to display the
#distance the vehicle has traveled for each hour of that time period. 
#Here is an example of the desired output:

speed = int(input('Enter mph: '))
time = int(input('Enter hours: '))

if time <= 0 or speed <= 0:
    print('Invalid Hours and mph must be greater than 0')
else:
    for t in range(time):
        distance = speed * (t+1)        

        print(t + 1,':', distance)
                  
                  