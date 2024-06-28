#Decorator

def my_decorator(func):
    def wrap_func():
        print('xxxxx')
        func()
        print('xxxxx')
    return wrap_func

@my_decorator
def hello():
    print('heloo')

hello()

@my_decorator
def bye():
    print('see ya later')

