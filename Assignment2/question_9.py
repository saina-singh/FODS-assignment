'''
Function to add a daily temperature to a dictionary only if the day is not already recorded.
'''

# Function to add temperature for a specific day
def add_daily_temp(temp_dict, day, temp):
    if day not in temp_dict:  # Only add if the day is not already recorded
        temp_dict[day] = temp
    return temp_dict  # Return the updated (or unchanged) dictionary

# Example usage
weekly_temps = {}  # Start with an empty dictionary
weekly_temps = add_daily_temp(weekly_temps, "Monday", 75)
weekly_temps = add_daily_temp(weekly_temps, "Tuesday", 80)
weekly_temps = add_daily_temp(weekly_temps, "Monday", 78)  # Won't update since Monday is already recorded

print(weekly_temps)  
# Output: {'Monday': 75, 'Tuesday': 80}
