from random import randint
game=["stone", "paper", "scissor"]
computer=game[randint(0,2)]
player=False
while player==False:
    player=input("stone, paper, scissor")
    if player==computer:
        print("computer's choice", computer)
        print("Draw")
    elif player=="stone":
        if computer=="paper":
            print("computer's choice", computer)
            print("you lose")
    elif player=="stone":
        if computer=="scissor":
            print("computer's choice", computer)
            print("you win")
    elif player=="paper":
        if computer=="scissor":
            print("computer's choice", computer)
            print("you lose")
    elif player=="paper":
        if computer=="stone":
            print("computer's choice", computer)
            print("you win")
    elif player=="scissor":
        if computer=="paper":
            print("computer's choice", computer)
            print("you win")
    elif player=="scissor":
        if computer=="stone":
            print("computer's choice", computer)
            print("you lose")
    else:
        print("that's not a valid play. Please check your spelling.")
    player=False
    computer=game[randint(0,2)]