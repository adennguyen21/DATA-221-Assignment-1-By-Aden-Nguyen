# Question 1: Controlled Multiplication Loop
#===========================================================

product_threshold = 100
product = 1
current_multiplier = 1

while product < product_threshold: # True until the product exceeds the threshold, which then stops the loop.
    current_multiplier += 1 # Adds 1 to the multiplier each loop.
    product *= current_multiplier # Multiplying the multiplier until product exceeds threshold.

print(f"The final product is {product}.") # Prints out final product.
print(f"The integer that caused the product to exceed the threshold is {current_multiplier}.") # Prints out the integer that caused the product to exceed the threshold.
