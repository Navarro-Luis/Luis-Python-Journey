some_list = ['a','b','c','b','d','m','n','n']

duplicates = []
for letter in some_list:
    if some_list.count(letter)>1:
        if letter not in duplicates:
            duplicates.append(letter)

print(duplicates)
