# def multiply_by2(li):
#     new_list = []
#     for item in li:
#         new_list.append(item*2)
#     return new_list

# print(multiply_by2([1,2,3]))

#map simplifies the above code:

def multiply_by2(item):
    return item*2

print(list(map(multiply_by2,[1,2,3])))

#practice
my_list = [5,8,10]

def squared(item):
    return item*item

print(list(map(squared,my_list)))