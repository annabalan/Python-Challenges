#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

def aging():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    number = int(input("Enter a number: "))
    year = str((2018 - age)+100)
    print(("\nHello " + name + "!" + " You are " + str(age) + "." + " You will be 100 years old in the year," + str(year) + ".") * (number))
aging()
