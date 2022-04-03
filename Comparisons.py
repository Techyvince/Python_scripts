#Another way to use if statements with comparisons
# comparison operators <= == != >= and much more
def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
         return num2 
    else:
        return num3

print(max_num(300,40,500))  #Calling the function

def animal(goat,pig,cat):
    if goat == pig:
        return goat
    elif goat != pig:
        return pig
    if cat == goat:
        return cat
    elif cat != goat:
        return goat
print(animal(3,2,3))  