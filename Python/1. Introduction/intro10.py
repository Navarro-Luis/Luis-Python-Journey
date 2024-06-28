#creating our own functions

# def say_hello():
#     print('hellooo')

# say_hello()

#creating parameters:
def say_hello(name, emoji):
    print(f'hellooo {name}{emoji}')

#arguments
say_hello('Luis',':)')
say_hello('bobbu',':O')

#functions with return
def sum(num1, num2):
    return num1+num2

print(sum(10,2))

#a function should do one thing really well,
#and should return something
#return ends the function, it exits the function.