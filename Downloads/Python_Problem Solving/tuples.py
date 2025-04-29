# Creating a tuple
my_tuple = ("Green", "Black", "Masala", "Ginger")

# Printing the tuple
print("Tuples:", my_tuple)

print("All element:", my_tuple[0:3])

print(len(my_tuple))

more_tea = ("Earl", "Oolong", "Herbal")

all_tea = my_tuple + more_tea
print("All tea:", all_tea)

if "Green" in all_tea:
    print("I have Green tea")
