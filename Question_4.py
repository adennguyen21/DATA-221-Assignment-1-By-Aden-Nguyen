# Question 4: Sorted Search with Conditions
#========================================================================

from random import random

values_list = [random() for i in range(20)]
x = random()
greater_or_equal_to_x_indices = [] # To store all the indices where a value is greater than or equal to x.
sorted_values_list = sorted(values_list) # Sorts values_list from smallest to greatest.
first_matching_index = "None" # Reassigned when there's a value that equals to x.

for value in sorted_values_list:
    if value >= x:
        greater_or_equal_to_x_indices.append(sorted_values_list.index(value)) # Stores the index of a value greater than or equal to x.
        if value == x:
            first_matching_index = sorted_values_list.index(value) # Stores the index of the first value that matches with x.

print(f"Sorted list: {sorted_values_list}") # Prints the sorted list of random values.
print(f"Value of x: {x}") # Prints the value of x.
print(f"First matching index: {first_matching_index}") # Prints the index of the first matching value to x, if any.
print(f"First greater than or equal to x index: {greater_or_equal_to_x_indices[0]}") # Prints the index of the first greater than or equal to value.
# (Last print statement was not asked for in question, but I decided to add it in since I wasn't too sure what the question was actually asking for.)