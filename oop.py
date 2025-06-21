class student:
    #Properties/Attributes
    name = "Peter"
    gender = "Male"
    age = 19

    def study(self):
        print("Student is studying")
    def movement(self):
        print("Student is walking")


student1 = student() # Creating an object
student1.study()
student1.movement()


print(student1.age)

student2 = student()
print(student2.name)