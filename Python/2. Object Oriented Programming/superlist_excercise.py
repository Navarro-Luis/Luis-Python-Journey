class SuperList(list): #add list to be able to call upon it and add
    def __len__(self):
        return 1000
    

super_list1 = SuperList()

print(len(super_list1))
super_list1.append(5)
print(super_list1[0])

print(issubclass(SuperList, list)) #is super cass a subclass of class