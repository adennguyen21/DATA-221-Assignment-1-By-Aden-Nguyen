# Question 8: Pandas DataFrame with Computed Column
#======================================================

import pandas as pd

data = { # Given in the question starter code.
    "A": [1, 2, 2, 1],
    "B": [3.1, 4.2, 1.5, 6.3],
    "C": [800, 150, 400, 210]
}

my_dataframe = pd.DataFrame(data) # Creates the DataFrame and stores it in my_dataframe.

my_dataframe["D"] = my_dataframe["A"] + my_dataframe["B"] * my_dataframe["C"]
# Making a new column that is derived from the other columns (A+B*C).

print(my_dataframe) # Prints the final DataFrame.