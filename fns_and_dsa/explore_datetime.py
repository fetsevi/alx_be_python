# Define current date and time function

from datetime import datetime, timedelta

current_date=datetime.now()



def display_current_datetime():

    format_date=current_date.strftime("%y-%m-%d %H:%M:%S")
    print("Current date and time: ", format_date)


def calculate_future_date():
     
     display_current_datetime()     # Display current date
     number_of_days=int(input("Enter the number of days to add to the current date: "))
     future_date=current_date + timedelta(days=number_of_days)  # future date operation
     print("Future date: ", future_date.strftime("%y-%m-%d %H:%M:%S"))   # Display future date

calculate_future_date()
