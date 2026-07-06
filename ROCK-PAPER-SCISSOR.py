import random
choice = ["rock", "paper" , "scissor"]

def get_choices():
    player_choice = input( "enter your choice (rock, paper , scissor) : ")
    computer_choice = random.choice(choice)
    choices = {"player" : player_choice , "computer" : computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose {player}, computer choice  {computer}")
    if player == computer:
      return "It's a tie!"
    elif player == "rock":
        if computer == "scissor":
            return "You  WIN"
        else:
            return "COMPUTER WIN"
        
    elif player == "scissor":
        if computer == "paper":
            return "You  WIN"
        else:
            return "Computer WIN"
        
    elif player == "paper":
        if computer == "rock":
            return "You  WIN"
        else:
            return "COMPUTER WIN"
        
choices = get_choices ()
result = check_win(choices["player"], choices["computer"])
print(result)


