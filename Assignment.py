# A python program that checks whether a number is even or odd
number= int(input("Enter the number:"))

if number % 2 ==0 :
    print(f"{number} is even")
else:
    print(f"{number} is odd")

print()
#A python program program that checks whether a letter is a vowel or consonant

letter = input("Enter the letter:") .lower()

if letter in "aeiou":
    print(f"{letter} is a vowel")
else:
    print(f"{letter} is  a consonant")

print()
#A python program that returns the perimeter of a rectangle
lenght = float(input("Enter the length:"))
width = float(input("Enter the width:"))

perimeter = 2*(lenght+width)
print(perimeter ,"is the perimeter of the rectangle")