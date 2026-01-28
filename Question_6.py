# Question 6: Distribution Analysis
#=========================================================================

def calculate_less_than_or_equal_to_percentage(number_list):
    number_percentage_dictionary = {} #

    for value in number_list: # Traverses through each element in the list.
        less_than_or_equal_to_count = 0

        for comparing_value in number_list: # Traverses through each element again to compare to the value from the outer for-loop.
            if comparing_value <= value: # Counts all the elements that are less than or equal to the value from the outer for-loop.
                less_than_or_equal_to_count += 1

        less_than_or_equal_to_percentage = less_than_or_equal_to_count / len(number_list) * 100
        # Divides the numbers of elements that are less than or equal to the value from the outer for-loop, by the
        # total number of elements in the list, then times 100 to get the percentage.
        number_percentage_dictionary[value] = round(less_than_or_equal_to_percentage, 1) # rounded to make it more neat, instead of having huge, ugly decimals.
        # Stores the outer for-loop value as the key, and the percentage as the value for number_dictionary.
    return dict(sorted(number_percentage_dictionary.items())) # Sorts out the dictionary by smallest key to the largest key.

numbers = [3, 1, 2, 3, 4, 2] # Given in the question example.

print(calculate_less_than_or_equal_to_percentage(numbers))
# Prints out the final dictionary. (Was not asked for, but I wanted to print it anyway.)