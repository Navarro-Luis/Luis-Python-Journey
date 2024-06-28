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
    for i in range(10):
        print(i*5)

#execute performance function with its callback funnction        
print_range()

