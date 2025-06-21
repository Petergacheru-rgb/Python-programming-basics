

class Dog:
    def __init__(self, name, breed, color):
        self.name = name
        self.breed = breed
        self.color = color

    def sound(self):
        print(self.name, "is barking")

    def __str__(self):
        return f"{self.name} is a {self.color} {self.breed}"

Dog1 = Dog("Roo", "German Shepherd", "Black")
print(Dog1) # Will print nicely because of __str__()
Dog2 = Dog("Alex", "Brown", "White")
print(Dog2)
Dog3 = Dog("Max", "Bull dog", "White")
print(Dog3)