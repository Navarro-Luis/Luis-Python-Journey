class User(): 
     def sign_in(self):
          print('Logged in')

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def attack(self):
     print(f'attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    def attack(self):
     print(f'attacking with arrows: arrows left: {self.num_arrows}')

#instantiating
wizard1 = Wizard('Merlin', 60)
archer1 = Archer('Robin', 30)

# def player_attack(char):
#     char.attack()

# player_attack(wizard1)

for char in [wizard1,archer1]:
    char.attack()