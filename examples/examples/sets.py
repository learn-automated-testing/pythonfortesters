# Create a tuple with specified elements
my_tuple = (10, 20, 30, 40, 50)

# Convert the tuple to a set
my_set = set(my_tuple)
print("Set created from tuple:", my_set)

# Add an element to the set
my_set.add(60)
print("Set after adding an element:", my_set)

# Check if an element is in the set
if 20 in my_set:
    print("20 is in the set.")
else:
    print("20 is not in the set.")