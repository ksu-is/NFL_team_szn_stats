import random

#gamestats
games = 0
wins = 0 
losses = 0
ties = 0

letsPlay = "y"

while(letsPlay == "y"):
    computer = random.randint(1,3)
    print("computer choise: " + str(computer))
    
    games = games + 1
    
    player = input("rock (1), paper (2), scissors (3) ? or type quit to quit!")
    
    if player == computer:
        print("Tie!")
        ties = ties + 1
    elif player == "rock":
        if computer == "paper":
            print("You lose!", computer, "covers", player)
            losses = losses + 1
        else:
            print("You win!", player, "smashes", computer)
            wins = wins + 1
    elif player == "paper":
        if computer == "scissors":
            print("You lose!", computer, "cut", player)
            losses = losses + 1
        else:
            print("You win!", player, "covers", computer)
            wins = wins + 1 
    elif player == "scissors":
        if computer == "rock":
            print("You lose...", computer, "smashes", player)
            losses = losses + 1
        else:
            print("You win!", player, "cut", computer)
            wins = wins + 1 
    elif player == "quit":
        print("Thank you for playing! Please come back!")
    else:
        print("That's not a valid play. Check your spelling!")
       
    letsPlay = input("Do you want to play again? Enter yes or no: ")
    
print(str(wins)+ " games won." +str(losses)+" games lost." +str(ties)+" games tied." +str(games)+" total games." )    
