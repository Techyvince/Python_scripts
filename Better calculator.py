# More advance calculator
num1 = float(input("Enter first number: ")) #converts whatever the user inputs into a float 
op =input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
   print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator")