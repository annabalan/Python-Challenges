#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)
# Extras:    Keep the game going until the user types “exit” #Keep track of how many guesses the user has taken, and when the game ends, print this out.
import random
# set the initial values
the_number = random.randint(1, 9)
guess = int(input("Take a guess: "))
tries = 1

#guessing loop
while guess != the_number:
    if guess > the_number:
        print("Lower...")
    elif guess < the_number:
        print("Higher...")
    guess = int(input('Take a guess:'))
    tries += 1
print("You guessed it! The number was", the_number)
print("And it only took you", tries, "tries!\n")
input("\n\nPress the enter key to exit.")
