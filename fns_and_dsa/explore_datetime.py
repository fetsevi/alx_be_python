# Define current date and time function

from datetime import datetime, timedelta

current_date=datetime.now()
#format_date=current_date.strftime("%Y-%m-%d %H:%M:%S")

def display_current_datetime():

    print("Current date and time: ", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
     
     display_current_datetime()     # Display current date
     number_of_days=int(input("Enter the number of days to add to the current date: "))
     future_date=current_date + timedelta(days=number_of_days)  # future date operation
     print("Future date: ", future_date.strftime("%Y-%m-%d %H:%M:%S"))   # Display future date

calculate_future_date()
