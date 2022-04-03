# Dictionaries allows us to store information in python
#all the keys have to be unique 
# the key is jan
# You can also use numbers as a key to save a value 
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr":  "April",
    10:     "December",
    11:     "July",
}

print(monthConversions.get("Jan"))
print(monthConversions["Mar"])
print(monthConversions.get("luv", "Not a valid key"))
print(monthConversions[10])