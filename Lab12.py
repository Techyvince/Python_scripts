import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("My Info")

# Create the label for the name
name_label = tk.Label(window, text="Name: Vincent Ifezue")
name_label.pack()

# Create the label for the address
address_label = tk.Label(window, text="Address: 66 Python street")
address_label.pack()

# Function to display the info when the button is clicked
def show_info():
    name_label.config(text="Name: Vincent")
    address_label.config(text="Address: 66 Python street")

# Create the button to show the info
show_info_button = tk.Button(window, text="Show Info", command=show_info)
show_info_button.pack()

# Run the main loop
window.mainloop()
