import random
while True:
    choices=["rock","paper","scissors"]
    computer= random.choice(choices)
    player= None
    while player not in choices:
        player=input('rock,paper or scisors?:').lower()
    if player == computer:
        print("computer:>",computer)
        print("PLayer:>",player)
        print("its a tie")
    elif player == "rock":
        if computer == "paper":
            print("computer:>",computer)
            print("PLayer:>",player)
            print("You Lose! " )
        if computer == "Scissors":
            print("computer:>",computer)
            print("PLayer:>",player)
            print("You Win! " )   
    elif player == "paper":
        if computer == "rock":
            print("computer:>",computer)
            print("PLayer:>",player)
            print("You Win! " )
        if computer == "Scissors":
            print("computer:>",computer)
            print("PLayer:>",player)
            print("You Lose! " ) 
    elif player == "Scissors":
        if computer == "paper":
            print("computer:>",computer)
            print("PLayer:>",player)
            print("You Win! " )
        if computer == "rock":
            print("computer:>",computer)
            print("PLayer:>",player)
            print("You Lose! " )  
    
    play = input("Do you want to play agin?-->(yes/no)-->").lower()
    if play != 'yes':
        break
print('See you agin!')