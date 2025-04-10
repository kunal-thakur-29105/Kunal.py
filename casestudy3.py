# -*- coding: utf-8 -*-
"""casestudy3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Lxvce8Va4uvRQkhI-dVKwI5-CGRL52Pn
"""

def display_welcome_message():
    """Display a welcome message to the user."""
    print("Welcome to the Temperature Monitoring System!")
    print("This system will monitor the temperature and provide alerts if it goes outside the safe range.\n")

def get_temperature_input():
    """Get temperature input from the user and handle invalid input."""
    while True:
        try:
            current_temp = float(input("Please enter the current temperature (in Celsius): "))
            return current_temp
        except ValueError:
            print("Invalid input! Please enter a valid number for the temperature.")

def check_temperature_range(current_temp, lower_limit, upper_limit):
    """Check if the current temperature is within the safe range and provide alerts."""
    if current_temp < lower_limit:
        return "Alert: Temperature is too low! It is below the lower safe limit of {}°C.".format(lower_limit)
    elif current_temp > upper_limit:
        return "Alert: Temperature is too high! It is above the upper safe limit of {}°C.".format(upper_limit)
    else:
        return "Temperature is within the safe range. It is safe at {}°C.".format(current_temp)

def display_goodbye_message():
    """Display a goodbye message."""
    print("\nThank you for using the Temperature Monitoring System.")
    print("Stay safe and keep monitoring your environment!")

def monitor_temperature():
    """Main function to monitor the temperature and provide alerts."""
    # Define the safe temperature range (upper and lower limits)
    lower_limit = 10  # Minimum safe temperature (example: 10°C)
    upper_limit = 30  # Maximum safe temperature (example: 30°C)

    # Display a welcome message
    display_welcome_message()

    # Get the current temperature input from the user
    current_temp = get_temperature_input()

    # Check the current temperature against the defined limits and display the appropriate message
    alert_message = check_temperature_range(current_temp, lower_limit, upper_limit)
    print(alert_message)

    # Display a goodbye message
    display_goodbye_message()

# Calling the function to start monitoring the temperature
monitor_temperature()

