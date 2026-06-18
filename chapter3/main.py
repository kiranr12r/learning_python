import random

def get_choices():
    player_choice = input("Enter a choice:- ")
    options   = ["rock","paper","scissors"]
    computer_choice = random.choice(options)
    choices = {"player":player_choice , "computer":computer_choice}
    return choices

def check_win(player,computer):
    print(f"you chose {player} computer chose {computer}")
    if player  == computer:   
        return "It's a Tie"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! you win!"
    else:
        return "paper covers rock! you lose."

check_win("rock","rock")
