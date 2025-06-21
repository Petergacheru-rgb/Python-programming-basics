#Parent class/Super class/Base  class
class Animal:
    def speak(self):
        print("Animal is speaking")

    def eat(self):
        print("Animal is eating")

#Child class/Sub class /Derived class
class Dog(Animal):
    def bark(self):
        print("Dog is barking")

    def  fetch(self):
        print("Dog is fetching a ball")

a = Animal()
a.speak()

d = Dog()
d.bark()
d.fetch()
