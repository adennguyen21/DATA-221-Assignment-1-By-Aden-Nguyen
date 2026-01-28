# Question 3: Safe Function Application
#=========================================================================

def calculate_exponent(base, exponent): # Calculates a base to the power of an exponent.
    final_number = base ** exponent
    return final_number

pairs = [[5, 2], [3, -1], [4, 3], [2, 0], [9, -6], [9, 2], [2, 4]] # Given in the question example, plus some new ones.
final_list = [] # Used to store all the numbers that have been exponentiated.

for pair in pairs: # Checks for negative exponents.
    if pair[1] < 0:
        continue

    final_list.append(calculate_exponent(pair[0], pair[1])) # Appends valid exponentiated numbers in final_list.

print(final_list) # Prints the final list.