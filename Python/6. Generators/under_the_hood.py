def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            # print(iterator)
            print(next(iterator))
        except StopIteration:
            break

special_for([1,2,3]) #when this executes. Notice how each iteration is in same location. Thats the point of generators, efficient, less memory space

