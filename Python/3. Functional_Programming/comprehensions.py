# my_list = []

# for char in 'hello':
#     my_list.append(char)

# print(my_list)

# can replace the above with:

#lists:
my_list = [char for char in 'hello']
my_list2 = [num for num in range(0,100)]#print 100 numbers
my_list3 = [num**2 for num in range(0,100)]#square those numbers
my_list4 = [num**2 for num in range(0,100) if  num % 2 ==0] #only look at the evens of those numbers

print(my_list3)

# the way this reads is: hey create a variable "char" then for each
#char variable in iterable, add it to the list.

#dictionary
simple_dict = {'a': 1,
               'b': 2
               }
my_dict = {key: value*2 for key, value in simple_dict.items()}
my_dict = {key: value*2 for key, value in simple_dict.items() if value%2==0}

my_dict = {num: num*2 for num in [1,2,3]}
print(my_dict)