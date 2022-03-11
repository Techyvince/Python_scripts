# If statement are used to execute certain code when certain conditions are true or false
# if statement responds to the input that they are given 

is_male = True # This a boolean variable
is_tall = False

if is_male and is_tall:  # both conditions have to be true 
    print("You are a tall male")
else:
    print("You are either not male or tall or both")

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither male nor tall")