my_list = [1,2,3]

# def multiply_by2(item):
#     return item*2

print(list(map(lambda item: item*2,my_list)))

#lambda is used when you are only going to do a function once.
#as shown above, if we didnt need to run multiplyby2 more than once
#we could just lambda it

#Excercise:

#square
my_list = [5,4,3]

print(list(map(lambda item: item * item, my_list)))

#list sorting

a = [(0,2), (4,3), (9,9), (10,-1)]
a.sort(key = lambda x: x[1])
print(a)
