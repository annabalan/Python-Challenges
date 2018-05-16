#create a program that will play the “cows and bulls” game with the user. The game works like this:
#Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.
print("\n\n\t\t\t'Welcome to Cows & Bulls'")
print("\nI will generate a number, and you have to guess the numbers one digit at a time.")
print("\nFor every number in the wrong place, you get a cow. For every one in the right place, you get a bull.")
print("\nThe game will end when you get 4 bulls!")



from random import randint
random_number = randint(1000, 9999)  # randint is inclusive at both ends
guess = int(input("Enter a 4 digit number: "))
cows = 0
bulls = 0
tries = 0
def counting_cows():
    while cows != 4:
        for i in range(0, 4):
            if guess[i] == random_number[i]:
                cows += 1
            elif guess[i] in random_number:
                bulls += 1
        return(cows, bulls)
def cow_game():
    while cows < 4:
        guess = int(input("Enter a 4 digit number: "))
        cows, bulls = counting_cows(guess)
        print("cows:", cows)
        print("bulls:", bulls)
        if cows == 4:
            print("Congrats! You guessed " + str(tries) + times.")
