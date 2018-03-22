#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

def aging():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    aging = 100 - age
    year = 2018 + aging
    print("Hello " + name + "!" + " You are " + str(age) + "." + "You will be 100 years old in the year," + str(year) + ".")
aging()
