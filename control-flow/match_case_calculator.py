
# Define variables with input

number1=int(input("Enter the first number: "))
number2=int(input("Enter the second number: "))
operator=input("Choose the operation (+, -, *, /): ")
result = 0

# Operations base on the operators
match operator:
    case "+": print(f"The result is {number1+number2}")
    case "-": print(f"The result is {number1-number2}")
    case "*": print(f"The result is {number1*number2}")
    case "/":
        if number2!=0: print(f"The result is {number1/number2}")
        else: print("Cannot divide by zero")
        
    case _: print("Invalid operator")