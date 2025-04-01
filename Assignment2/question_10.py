'''
Function to collect average daily temperatures from the user for each day of the week.
'''

# Function to get daily temperatures from user input
def get_daily_temps():
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    temp_dict = {}

    for day in days_of_week:
        while True:  # Keep prompting until a valid number is entered
            try:
                temp = float(input(f"Enter the average temperature for {day}: "))
                temp_dict[day] = temp
                break  # Exit loop on valid input
            except ValueError:
                print("Invalid input! Please enter a numerical value.")

    return temp_dict  # Return the dictionary containing temperatures

# Example usage
weekly_temperatures = get_daily_temps()
print("Recorded Temperatures:", weekly_temperatures)
