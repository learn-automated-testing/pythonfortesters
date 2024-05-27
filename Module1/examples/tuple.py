 # Define a tuple
my_tuple = (1, 2, 3)

# Attempt to modify the second element of the tuple
try:
    my_tuple[1] = 4
except TypeError as e:
    print("Error:", e)