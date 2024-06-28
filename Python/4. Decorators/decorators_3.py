#Decorator

def my_decorator(func):
    def wrap_func(*args,**kwargs):
        print('xxxxx')
        func(*args,**kwargs)
        print('xxxxx')
    return wrap_func

@my_decorator
def hello(greeting,emoji=':('):
    print(greeting,emoji)

hello('hi')

@my_decorator
def bye():
    print('see ya later')

