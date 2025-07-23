# Define arithmetic function

num1=0
num2=0
operation=''
def perform_operation(num1, num2, operation):
    if operation=='add': return num1+num2
    elif operation=='subtract': return num1-num2
    elif operation=='multiply': return num1*num2
    elif num2==0 and operation=='divide': return print("Error cannot be divided by 0")
    elif num2!=0 and operation=='divide': return num1/num2
    
    else: return print("Unknown operator")
