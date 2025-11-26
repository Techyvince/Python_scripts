import tkinter as tk

# Function to calculate the gas mileage
def calculate_mpg():
    try:
        # Get the values from the entry widgets
        gallons = float(gallons_entry.get())
        miles = float(miles_entry.get())
        
        # Calculate the miles-per-gallon
        mpg = miles / gallons
        
        # Display the result in the label
        result_label.config(text="Miles per gallon: {:.2f}".format(mpg))
    except ValueError:
        # Display an error message if the user enters invalid input
        result_label.config(text="Please enter valid numbers.")

# Create the main window
window = tk.Tk()
window.title("Gas Mileage Calculator")

# Create the entry widgets for the number of gallons and miles
gallons_label = tk.Label(window, text="Number of gallons of gas:")
gallons_label.pack()
gallons_entry = tk.Entry(window)
gallons_entry.pack()

miles_label = tk.Label(window, text="Number of miles on a full tank:")
miles_label.pack()
miles_entry = tk.Entry(window)
miles_entry.pack()

# Create the Calculate MPG button
calculate_button = tk.Button(window, text="Calculate MPG", command=calculate_mpg)
calculate_button.pack()

# Create the label to display the result
result_label = tk.Label(window, text="")
result_label.pack()

# Run the main loop
window.mainloop()
