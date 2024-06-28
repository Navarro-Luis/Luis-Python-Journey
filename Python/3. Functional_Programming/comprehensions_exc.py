#take some_list and find the duplicate values and return them to me
# in a LIST

some_list = ['a','b','c','d','b','m','n','n']

duplicates = list({value for value in some_list if some_list.count(value)>1})

print(duplicates)