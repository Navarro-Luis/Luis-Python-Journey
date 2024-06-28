# Create a Python program that behaves as a basic calculator but includes deliberate faults for specific operations 
# (e.g., attempting to divide by zero). The task is to handle these errors gracefully using try-except blocks, 
# providing clear feedback to the user about what went wrong.

def multiply(num1,num2):
    try:
        return int(num1*num2)
    
    except(ValueError,NameError):
        print('Please input two integers')

def divide(num1, num2):
    try:
        return num1 / num2
    except(ZeroDivisionError):
        print('Use non-zero number')
    except(NameError,TypeError,ValueError): #WHY DOESNT THIS WORK
        print('Please input two integers')
    
print(divide(5,a))