import random

# Seven random numbers between 0 and 9
lottery_number = [random.randint(0, 9) for _ in range(7)]

# Print the lottery number
print("The winning lottery number is:", ''.join(map(str, lottery_number)))