#Given the below class:
class Cat:
    crew = []
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

tom = Cat('tom', 12)
bob = Cat('bob', 3)
marley = Cat('marley', 5)

def oldest_cat(*args):
    return max(args)

print(f'Oldest Cat is {oldest_cat(tom.age,bob.age,marley.age)} years old.')

# 1 Instantiate the Cat object with 3 cats



# 2 Create a function that finds the oldest cat



# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2