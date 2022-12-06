from random import randint
#create a list of play options
t = ["rock", "paper", "scissors"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = False

while player == False:
#set player to True
    player = input("rock, paper, scissors? or type quit to quit!")
    if player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "paper":
        if computer == "scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "scissors":
        if computer == "rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    elif player == "quit":
        print("Thank you for playing! Please come back!")
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]
