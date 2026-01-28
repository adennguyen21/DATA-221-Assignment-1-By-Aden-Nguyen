# Question 2: Nested Dictionary from Strings
#======================================================================

def create_string_nested_dictionary(string_list):
    string_dictionary = {}

    for string in string_list: # Goes through each string in the given string list.
        if len(string) % 2 == 0: # Check the parity of the string.
            string_parity = "Even"
        else:
            string_parity = "Odd"

        string_dictionary[string] = {"Length": len(string), "Parity": string_parity} # Stores the string as a key, and its information as its value which is in another dictionary.

    return string_dictionary


my_string_list = ["data", "science", "Meowwwwwwww"] # Same strings from the question example used, plus "Meowwwwwwww".

print(create_string_nested_dictionary(my_string_list)) # Prints the final dictionary.
