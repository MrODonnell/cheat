""" Animals has a super class of animal along with several subclasses """
print("hello animals")
class Animal:
    def __init__(self, name=None, weight=0):
        self.name = name
        self.weight = weight

class Dog(Animal):
    def speak(self, voice='Bark'):
        return voice

class Cat(Animal):
    def speak(self, voice='Meow'):
        return voice
