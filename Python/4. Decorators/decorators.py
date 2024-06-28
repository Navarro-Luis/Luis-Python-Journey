#higher Order Function (HOC)

def greet(func):# a function that acceps a function within parameter
    func()


def greet2(): # or a function that returns another function
    def func():
        return 5
    return func