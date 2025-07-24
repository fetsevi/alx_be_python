# Temperature conversion tool

FAHRENHEIT_TO_CELSIUS_FACTOR=5/9
CELSIUS_TO_FAHRENHEIT_FACTOR=9/5

def convert_to_celsius(fahrenheit):     # Convert to celsius function
    return (fahrenheit-32)*FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):     # Convert to fahrenheit function
    return (celsius*CELSIUS_TO_FAHRENHEIT_FACTOR)+32

# Main function 

def main():

    temperature=float(input("Enter the temperature to convert: "))
    if type(temperature)==str:

        raise ValueError("Invalid temperature. Please enter a numeric value.") # To control numeric value
        return print("Invalid temperature")

    unit=input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

    # Operation according to celsius (C) or fahrenheit (F)
    if unit=='F':
        print(f"{temperature}°F is {convert_to_celsius(temperature):.2f}°C")
    elif unit=='C':
        print(f"{temperature}°C is {convert_to_fahrenheit(temperature):.2f}°F")
    else:
        print("Invalid unit. please enter 'C' or 'F' ")

if __name__ == "__main__":
    main()