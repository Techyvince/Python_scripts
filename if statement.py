# If statement are used to execute certain code when certain conditions are true or false
# if statement responds to the input that they are given 
# if statement helps our code make decisions 

male = True #  true or false is a boolean variable
tall = False

if male and tall:  # and means both conditions is true 
    print("You are a tall male")
elif male and not (tall): 
    print("You are a short male")
elif not(male) and tall: 
    print("You are not a male but are tall")
else:
    print("You are either not male or not tall or both")

if male or tall: # or means one or both values is true
    print("You either a male or tall")
else:
    print("You are not a not a male or tall")


food =  False
car = False
if food:
    print("yaaay")
else:  
    print("naaa")  
if car:
    print("This is a brand new car")
else:
    print("This is not a brand new car")            