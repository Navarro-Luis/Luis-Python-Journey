# Description of Task:
# Develop a Python decorator called timer that can be used to measure and print the execution time of any function it decorates. 
# This will help in analyzing the performance of different functions.

from time import time

def timer (function):
    def helper(*args,**kwargs):
        time1 = time()
        fn = function(*args,**kwargs)
        time2 = time()
        print(f'it took {time2 - time1} seconds')
        return fn
    return helper



@timer
def multiplier(num1,num2):
    result = num1 * num2
    return result

print(multiplier(56,5))