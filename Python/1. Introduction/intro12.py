#when we create a function, we can give it a description!!!(hover over)

# def test(a):
#     '''
#     Info: This function tests and prints parameter a
#     '''
#     print(a)

# test('!!!!')

#*args and **Kwargs
# *args allows you to input a bunch of arguments, without the * can only do 1
def super_function(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total+=items
    return sum(args) + total

print(super_function(1,2,3,4,5, num1 = 4, num2 = 3))