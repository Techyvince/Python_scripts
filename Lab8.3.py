# Initialize an empty list to store the numbers
numbers = []

# Get 20 numbers from user input
for i in range(1, 21):
    while True:
        try:
            number = float(input(f"Enter number {i}: "))
            numbers.append(number)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Calculate the lowest number
lowest_number = min(numbers)

# Calculate the highest number
highest_number = max(numbers)

# Calculate the total of the numbers
total = sum(numbers)

# Calculate the average of the numbers
average = total / len(numbers)

# Display the results
print(f"Lowest number: {lowest_number}")
print(f"Highest number: {highest_number}")
print(f"Total: {total}")
print(f"Average: {average}")
