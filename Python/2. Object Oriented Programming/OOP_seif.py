# Encapsulation: Keeping details (like variables) private inside a class and providing public methods to access or modify them.

# Define the User class
class User:
    # Constructor method to initialize the object
    def __init__(self, username, password):
        self.__username = username  # Private variable for username
        self.__password = password  # Private variable for password

    # Method for signing in
    def sign_in(self):
        print(f'{self.__username} logged in')

    # Method to change the password
    def change_password(self, old_password, new_password):
        # Check if the old password matches the current password
        if old_password == self.__password:
            self.__password = new_password  # Update to the new password
            print('Password changed successfully')
        else:
            print('Password change failed')

# Inheritance: Creating a new class from an existing class to reuse code and add new features.

# Define the Wizard class that inherits from User
class Wizard(User):
    # Constructor method to initialize the object
    def __init__(self, username, password, name, power):
        # Call the constructor of the parent class (User)
        super().__init__(username, password)
        self.name = name  # Public variable for name
        self.power = power  # Public variable for power

    # Method for attacking
    def attack(self):
        print(f'{self.name} attacking with power of {self.power}')

# Define the Archer class that inherits from User
class Archer(User):
    # Constructor method to initialize the object
    def __init__(self, username, password, name, num_arrows):
        # Call the constructor of the parent class (User)
        super().__init__(username, password)
        self.name = name  # Public variable for name
        self.num_arrows = num_arrows  # Public variable for number of arrows

    # Method for attacking
    def attack(self):
        print(f'{self.name} attacking with arrows: arrows left: {self.num_arrows}')

# Polymorphism: Using a single interface to represent different types of objects.

# Define a function for player attack
def player_attack(char):
    char.attack()  # Call the attack method of the character

# Abstraction: Hiding the complex implementation details and showing only the necessary features.

# Define the Game class
class Game:
    # Constructor method to initialize the object
    def __init__(self):
        self.characters = []  # List to hold characters

    # Method to add a character to the game
    def add_character(self, character):
        self.characters.append(character)

    # Method to start the battle
    def start_battle(self):
        # Loop through each character and call their attack method
        for char in self.characters:
            char.attack()

# Instantiating objects

# Create a Wizard object
wizard1 = Wizard('wizard_user', 'wiz_password', 'Merlin', 60)
# Create an Archer object
archer1 = Archer('archer_user', 'arch_password', 'Robin', 30)

# Encapsulation example
wizard1.sign_in()  # Call the sign_in method
wizard1.change_password('wiz_password', 'new_wiz_password')  # Change the password

# Polymorphism example
player_attack(wizard1)  # Call the player_attack function with a Wizard
player_attack(archer1)  # Call the player_attack function with an Archer

# Abstraction example
game = Game()  # Create a Game object
game.add_character(wizard1)  # Add the Wizard to the game
game.add_character(archer1)  # Add the Archer to the game
game.start_battle()  # Start the battle