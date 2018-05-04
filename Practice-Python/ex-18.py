#create a program that will play the “cows and bulls” game with the user. The game works like this:
#Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.
import random
print("\n\n\t\t\t'Welcome to Cows & Bulls'")
print("\nI will generate a number, and you have to guess the numbers one digit at a time.")
print("\nFor every number in the wrong place, you get a cow. For every one in the right place, you get a bull.")
print("\nThe game will end when you get 4 bulls!")

guess = int(input("Enter a 4 digit number: "))

from random import randint
random_number = randint(1000, 9999)  # randint is inclusive at both ends
