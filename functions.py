#1.Built-functions/Standard Library Functions

x = max(45,56,34,38,56,32,12)
print("The maximum number is",x)

y = min(45,56,34,38,56,32,12)
print("The minimum number is",y)

z = pow(2, 3)
print("The power of 2 is",z)
print("The power of 3 is",x*y)

#User-defined functions
def greeting():
    print("Hello world!")
greeting() #Calling a function

def school():
    print("My Coding School is eMobilis")
school()

#Parameter and arguments
def add(num1,num2):
    print(num1+num2)
add(10,5)
add(20,5)

def students(fullname,course,gender):
    print(fullname,course,gender)
students("Peter Gacheru","MIT","Male")
students("John James","MIT","Male")
students("Micky ","MIT","Female")
students("Abdalla","MIT","Male")
students("Carol","MIT","Female")
students("Moses","MIT","Male")

#A python program that displays details of five employee at
#Fintech using parameter and argument
#(Fullname,email,age,position,salary,marriage status)

def employees(fullname,email,age,position,salary,marriagestatus):
    print(fullname,email,age,position,salary,marriagestatus)
employees("Peter Gacheru","petergacheru44@gmail.com","35 years","CEO","ksh.500,000.00","Married")
employees("Marry Ann","maryann23@gmail.com","30 years","Manager","ksh.200,000.00","Married")
employees("Daniel Brian","danielbrian10@gmail.com","33 years","HR","ksh.150,000.00","Single")
employees("Aliice WAirimu","wairimualice@gmail.com","27years","Secretary","ksh.90,000.00","Married")
employees("Donel James","donjames@gmail.com","25years","Bursar","ksh.50,000.00","Single")







