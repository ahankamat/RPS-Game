import random
def get_choices():
    player_choice=input("Enter your choice(Rock, Paper,Scissor):\n")
    options=["Rock","Paper","Scissor"]
    computer_choice=random.choice(options)
    choices={"player choice":player_choice, "computer choice": computer_choice}
    return choices

def get_win(player,computer):
    # generate f strings , we can also use + for concatenation of strings
    print(f"You chose {player} & computer chose {computer}")
    if player==computer:
        print("It is a tie!")
    elif player=="Rock":
        if computer=="Paper":
            print("You lose :(")
        else:
            print("You win :)")
    
    elif player=="Paper":
        if computer == "Scissor":
            print("You lose :(")
        else:
            print("You win :)")
    
    elif player == "Rock":
        if computer == "Scissor":
            print("You win :)")
        else:
            print("You lose :(")

choices=get_choices()
result=get_win(choices["player choice"],choices["computer choice"])
