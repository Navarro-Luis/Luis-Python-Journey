my_list = [1,2,3]
your_list = [10,20,30]

def multiply_by2(item):
    return item*2


def only_odd(item):
    return item % 2 != 0 #modulo(%) by 2 divides the number by 2 and gives you the remainder. % 2 != 0 searches for odds.


print(list(zip(my_list,your_list)))#zip is zipping together a list and putting them un tuples
