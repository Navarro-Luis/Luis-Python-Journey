from time import time

def time_calculator(func):#this function times how long another function takes to run
    def helper(*args,**kwargs):
        t1 = time()
        result = func(*args,**kwargs)
        t2 = time()
        print(f'it took {t2-t1} s')
        return result
    return helper


@time_calculator
def print_range():
    print('1')
    for i in range(1000000):
        i*5

@time_calculator
def print_range2():
    print('2')
    for i in list(range(10000000)):
        i*5


print_range()
print_range2()