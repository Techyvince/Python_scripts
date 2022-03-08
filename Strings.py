#backslash \n helps you insert a new line
#backslash and a quotation mark \" tells python to print out the quotation mark
#You can create a string variable
#You can use concatenation in a string. concatenation is a process of taking a string and appending a string unto it.
#We can also use function. A fuction is a block of code that when you run will perform a specific operation for you.
#We can use method and fuction to modify our strings.
#We can also use method and function to get information about our strings

print("Below are the list of african food")
print("Egusi\nOgbonno\nAmala")
print("I am learning something new\"in python")
Towson = "University"
PC = "Mackbook"
School = "HCC CCBC"
print(Towson)
print("Towson is an expensive " + Towson)
print(Towson.lower()) # What this does is it prints out what is in the variables Towson in lower case
print(Towson.upper())
print(Towson.isupper())
print(PC.lower().isupper()) # What this does is it changes the PC to lower case and then prints out if it is True or False
print(len(PC))
print(len(Towson))
print(PC[0]) # What this does is it prints the first character on the string PC starting from 0
print(Towson[5])
print(Towson.index("ver")) #It prints out the number where the ver starts from in the variable 
print(School.replace("HCC", "UMBC")) # This line replaces the variable in school HCC with UMBC