rainfall = []

# Get rainfall data from user input
for i in range(1, 13):
    while True:
        try:
            month_rainfall = float(input(f"Enter rainfall for month {i}: "))
            if month_rainfall >= 0:
                rainfall.append(month_rainfall)
                break
            else:
                print("Rainfall amount must be non-negative.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Calculate total rainfall for the year
total_rainfall = sum(rainfall)

# Calculate average monthly rainfall
avg_rainfall = total_rainfall / 12

# Find the month with highest and lowest rainfall
max_rainfall_month = rainfall.index(max(rainfall)) + 1
min_rainfall_month = rainfall.index(min(rainfall)) + 1

# Display the results
print(f"Total rainfall for the year: {total_rainfall} inches")
print(f"Average monthly rainfall: {avg_rainfall} inches")
print(f"Highest rainfall in month {max_rainfall_month}: {max(rainfall)} inches")
print(f"Lowest rainfall in month {min_rainfall_month}: {min(rainfall)} inches")