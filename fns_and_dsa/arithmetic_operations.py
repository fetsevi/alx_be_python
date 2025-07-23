# Define arithmetic function

num1=0
num2=0
operation=''
def perform_operation(num1, num2, operation):
    
    # operations


    if operation=='add': return num1+num2              # Addition operation
    elif operation=='subtract': return num1-num2       # Sbstraction operation
    elif operation=='multiply': return num1*num2       # Multiplication operation
    
    # Division function

    def divide(num1: float, num2: float) -> float:
      if num2 == 0:
        raise ValueError("Cannot divide by zero.")
    return num1/num2
