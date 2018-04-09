#Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

#Remember the rules:
# Rock beats scissors
# Scissors beats paper
# Paper beats rock
print("\n\t\t\t'Welcome to Rock-Paper-Scissors.")
print("\nWhen promted below, enter your move below. You can choose Rock, Paper or Scissors. Remember Rock beats Scissors. Scissors beats paper and Paper beats Rock.")

player_1 = input("Player one, enter your move: ")
player_2 = input("Player two, your move: ")

def game(player_1, player_2):
    if player_1 == player_2:
        return("It's a tie!")
    elif player_1 == 'rock':
        if player_2 == 'scissors':
            return("Rock wins!")
        else:
            return("Paper wins!")
    elif player_1 == 'scissors':
        if player_2 == 'paper':
            return("Scissors win!")
        else:
            return("Rock wins!")
    elif player_1 == 'paper':
        if player_2 == 'rock':
            return("Paper wins!")
        else:
            return("Scissors win!")
    else:
        return("Invalid choice. Please choose rock, paper or scissors.")
        sys.exit()

print(game(player_1, player_2))
