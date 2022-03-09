# a list is a structure we can use inside of python to store list of information.
# We can take different data values, put them into a list, keep track of them and organize them a lot easier 
# we use open and close sqaure bracket[]
# we can store multiple values into the same variable or object
friends = ["Victor", "Jude", "emeka", "emeka", "emeka", "emeka"]
lucky_num = [2,5,8,9,4,7]
class1 = ["ss1","ss2","ss3"]
friends.sort #sorts the friends list in alphabetical other
print(friends)
#print(friends[2]) #prints the third value on the friends variable.
friends.append("favor") #adds favor into the friends list 
friends.insert(1, "Ben") #adds ben into the friends list after victor
print(friends.count("emeka")) # counts how many emeka that is in the friends variable
friends.remove("emeka") # removes emeka on the friends list
lucky_num.pop() #prints all the values in the variable except for the last number
print(friends)
print(friends.index("Jude"))
friends.clear() # gives us an empty list
print(friends)  
friends.extend(lucky_num) #the extend function adds friends and lucky_num together
print(friends)
lucky_num.sort()
print(lucky_num)
#print(class1[1:])
#print(lucky_num[2:3])
