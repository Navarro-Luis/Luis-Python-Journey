my_list = [1,2,3]
def multiply_by2(item):
    return item*2


def only_odd(item):
    return item % 2 != 0 #modulo(%) by 2 divides the number by 2 and gives you the remainder. % 2 != 0 searches for odds.

print(list(filter(only_odd,my_list)))

#filter is running through my_list and running our only_odd function
#which is giving boolean(true false) answers naturally. filter
#is then applying filtering for trues, list then puts them in a list

#practice
my_list = [16,8,25]
divisor = 4
def divisible(item):
    return item %divisor == 0

print(list(filter(divisible,my_list)))

    