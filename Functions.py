#A function is a collection of codes which performs a specific tasks
# function helps you to organize your code a lot better
# you can pass any type of data inside a function
# You can only call a fuction so that it can prints on your terminal
def sayhi(name, age):
    print("Hello " + name + ", your are " + age)
sayhi("mike", "40") # calling the fuction. 
sayhi("Steve", "20")

def money():
    print("Euro " + "Pounds " + "Dollar ")
money()

def animal():
    print("Dog", "Goat", "Fish")

def country(UK, US):
    print("Welcome to " + UK + " and we are in good terms with " + US + "!")
country("London", "America")
money()
animal()