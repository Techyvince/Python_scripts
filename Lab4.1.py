#Write a program with a loop that asks the user to enter a
#series of positive numbers. The user should enter a negative number
#to signal the end of the series. After all the positive numbers have been
#entered, the program should display their sum.

num = []
while True:
    a = int(input('numbers:'))
    if a > 0:
        num.append(a)
    if a < 0:
        print(sum(num))
        