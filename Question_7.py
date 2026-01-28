# Question 7: Time Conversion Function
#==============================================================

def get_seconds_since_midnight(): # Gets the seconds since midnight from the user, while catching any errors,
    while True:
        try:
            seconds_since_midnight_input = int(input("Input the number of seconds since midnight: "))
            if seconds_since_midnight_input < 0: # Catches negative numbers.
                print("Cannot input a negative number. Please provide the number of seconds since midnight.")
                continue

            if seconds_since_midnight_input >= 86400: # For if user inputs seconds that amount to more than one day.
                print("Seconds inputted spans more than one day, must be between 0 and 86399 seconds. Please provide the number of seconds since midnight within a day.")
                continue

        except ValueError: # Catches any inputted strings.
            print("Cannot input a string. Please provide the number of seconds since midnight.")
            continue

        else:
            return seconds_since_midnight_input


def convert_seconds_since_midnight(seconds_since_midnight_input):
    if seconds_since_midnight_input < 43200: # To check if the number of seconds is before or past noon. In this case, this is for before noon.

        if seconds_since_midnight_input < 3600: # To check if a 12 for hours is needed, instead of just having a 0 for hours in the final result.
            hours_since_midnight = 12
            minutes_since_midnight = (seconds_since_midnight_input % 3600) // 60
            remaining_seconds_since_midnight = seconds_since_midnight_input % 60

        elif seconds_since_midnight_input >= 3600:
            hours_since_midnight = seconds_since_midnight_input // 3600
            minutes_since_midnight = (seconds_since_midnight_input % 3600) // 60
            remaining_seconds_since_midnight = seconds_since_midnight_input % 60

        am_or_pm_indicator = "AM"


    elif seconds_since_midnight_input >= 43200: # This is for past noon.
        seconds_since_midnight_input_past_noon = seconds_since_midnight_input - 43200 # Subtracts half the day to make calculations similar to if it was before noon (No need for new logic).

        if seconds_since_midnight_input_past_noon < 3600: # Also checks if a 12 for hours is needed.
            hours_since_midnight = 12
            minutes_since_midnight = (seconds_since_midnight_input_past_noon % 3600) // 60
            remaining_seconds_since_midnight = seconds_since_midnight_input_past_noon % 60

        elif seconds_since_midnight_input_past_noon >= 3600:
            hours_since_midnight = seconds_since_midnight_input_past_noon // 3600
            minutes_since_midnight = (seconds_since_midnight_input_past_noon % 3600) // 60
            remaining_seconds_since_midnight = seconds_since_midnight_input_past_noon % 60

        am_or_pm_indicator = "PM"

    return hours_since_midnight, minutes_since_midnight, remaining_seconds_since_midnight, am_or_pm_indicator



hours_since_midnight, minutes_since_midnight, seconds_since_midnight, am_or_pm_indicator = convert_seconds_since_midnight(get_seconds_since_midnight())
# Assigning each value into their own variables.
print(f"{hours_since_midnight} {minutes_since_midnight} {seconds_since_midnight} {am_or_pm_indicator}")
# Printing the final result using a formatted string.