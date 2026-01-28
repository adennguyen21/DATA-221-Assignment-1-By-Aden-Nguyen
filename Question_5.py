# Question 5: Circle Area Comparison with Validation
#====================================================================================

import math

def calculate_circle_area_coverage_percentage(radius_of_circle1, radius_of_circle2):
# Calculates the circle areas, and coverage percentage of how much the smaller circle covers the larger circle.
    area_of_circle1 = math.pi * radius_of_circle1 ** 2 # These calculate area.
    area_of_circle2 = math.pi * radius_of_circle2 ** 2

    if area_of_circle1 >= area_of_circle2: # Checks which circle is bigger.
        percentage_of_area_covered = area_of_circle2 / area_of_circle1 * 100 # Calculates the percentage of area covered, by dividing the smaller circle by the larger circle, then times 100.
    elif area_of_circle1 < area_of_circle2:
        percentage_of_area_covered = area_of_circle1 / area_of_circle2 * 100
    else: # For if both circles are the same size.
        percentage_of_area_covered = area_of_circle1 / area_of_circle2 * 100

    return percentage_of_area_covered


def get_radii_of_circles(what_number_circle): # Gets the input of radii from the user.
    while True: # Repeats the input prompt if user puts an invalid radius.
        try:
            radius_of_circle = int(input(f"Enter the radius of the {what_number_circle} circle: "))
            if radius_of_circle <= 0: # Checks for negative radii, and if radii equal to 0.
                print("Radius cannot be negative or 0, Please provide a positive integer for radius.")
                continue

        except ValueError: # Catches errors so program doesn't crash (Like if the user inputs a string instead of a integer.)
            print("Cannot have strings for radius. Please provide a positive integer for radius.")
            continue

        else: # When all inputs are valid, it returns the radius.
            return radius_of_circle


radius_of_circle1_input = get_radii_of_circles("first")
radius_of_circle2_input = get_radii_of_circles("second")

print(f"Percentage of larger circle's area covered by the smaller circle: {calculate_circle_area_coverage_percentage(radius_of_circle1_input, radius_of_circle2_input)}%")
# Prints out the percentage of area covered by the smaller circle to the larger circle.
