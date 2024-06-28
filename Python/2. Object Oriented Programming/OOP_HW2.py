# Problem 1: Zoo Management System
# Task:
# Create a simple zoo management system that demonstrates the use of inheritance, polymorphism, and encapsulation. 
# Your system should include at least three animal types and a Zoo class that manages them. 
# Each animal should have at least one unique method besides common methods that apply to all of them.

# Steps:
# Define a base class Animal with common attributes like name and age, and methods like eat() and sleep().
# Create three derived classes from Animal (e.g., Lion, Elephant, Monkey) each with at least one unique method (e.g., roar() for Lion).
# Implement polymorphism for a method speak() that each animal class will override to make a unique sound.
# Encapsulate some attributes where appropriate.
# The Zoo class should be able to add animals, remove animals, and display information about all animals.```

class Animal():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def eat():
        print('I love eating')

    def sleep():
        print('I love sleeping')

class Lion(Animal):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def roar():
        print('Roar')
    def speak(self):
        print(f'My name is {self.name} and I am {self.age} years old')

class Elephant(Animal):
    def yell():
        print('yell')
    def speak():
        print('bow')

class Monkey(Animal):
    def ooh():
        print('oooh oohh ah ah')
    def speak():
        print('WOW')


lion1= Lion("luis",25)

print(lion1.speak())