#The Fast Freight Shipping Company charges the following rates
#2 pounds or less 	$1.50
#Over 2 pounds but not more than 6 pounds 	$3.00
#Over 6 pounds but not more than 10 pounds 	$4.00
#Over 10 pounds $4.75
#Write a program that asks the user to enter the weight of a package then displays the shipping charges.
buyer = input ("Enter weight of package: ")
if int(buyer) <= 2:
    print("Your balance is $1:50")
else:
    if int(buyer) <=6:
      print("Your balance is $3.00 ")
    else:
        if int(buyer) <=10:
           print("Your balance is $4.00")
        else:
            if int(buyer) >10:
               print("Your balance is $4.75")
