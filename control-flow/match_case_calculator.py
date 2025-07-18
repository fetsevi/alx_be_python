
# Define variables with input

number1=int(input("Enter the first number: "))
number2=int(input("Enter the second number: "))
operation=input("Choose the operation (+, -, *, /): ")


# Operations base on the operators
match operation:
    case "+": print(f"The result is {number1+number2}")
    case "-": print(f"The result is {number1-number2}")
    case "*": print(f"The result is {number1*number2}")
    case "/":
        if number2!=0: print(f"The result is {number1/number2}")
        else: print("Cannot divide by zero")
        
    case _: print("Invalid operator")