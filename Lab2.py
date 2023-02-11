#Miles-per-Gallon
MPG1 = int(input("Milesdriven: " ))
MPG2 = int(input("Gallonsofgasused: "))
amount = (MPG1)/(MPG2)
print ("Total number of miles driven: " + str(amount))

##############################(#####################################################################

####################################################################################################
#  Tip, Tax, and Total 
#  Write a program that calculates the total amount of a meal purchased at a restaurant.
#  The program should ask the user to enter the charge for the food, then calculate the amounts of a 
## 18 percent tip and 7 percent sales tax. Display each of these amounts and the total.
###################################################################################################

tip = int(18) 
salesTax = int(7)
user = input ("Enter food amonut: " )
percentage_total = int(user)/100 * tip + int(user)
percentage1_total = int(user)/100 * salesTax + int(user)
print ("18 percent tip plus total: " + str(percentage_total))
print ("7 percent tip plus total: " + str(percentage1_total))
Total = percentage_total + percentage1_total
print ("Total amount including tax: " + str(Total))

##########################################################################################################
# Write a program that converts Celsius temperatures to Fahrenheit temperatures. The formula is as follows:
# F = (9/2)c+32
##########################################################################################################

tempInCelsius = int(input("Enter temperature: "))
Fahrenheit = (9 / 5) *(tempInCelsius) + 32
print ("Temperature converted to Fahrenheit is: " + str(Fahrenheit))

