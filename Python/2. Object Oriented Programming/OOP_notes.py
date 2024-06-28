#OOP
class PlayerCharacter:
    membership = True #class Object Attribute
    def __init__(self,name = 'anonymous',age=0):
            self.name = name #attribute
            self.age = age
    
    def shout(self):
        print(f'my name is {self.name}')
    
    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)

player3 = PlayerCharacter.adding_things(2,3)

print(player3.age)