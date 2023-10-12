import random


while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    # print(computer)
    player = None
    while player not in choices:
        player=input("rock,paper, or scissor? : ").lower()
        if player==computer:
            print("computer: ",computer)
            print("player: ",player)
            print("Tie!")
        elif player=="rock":
            if computer=="paper":
                print("computer: ", computer)
                print("player: ", player)
                print("you lose")
            else:
                print("computer: ", computer)
                print("player: ", player)
                print("you win")
        elif player=="scissors":
            if computer=="paper":
                print("computer: ", computer)
                print("player: ", player)
                print("you win")
            else:
                print("computer: ", computer)
                print("player: ", player)
                print("you win")
        elif player=="paper":
            if computer=="scissors":
                print("computer: ", computer)
                print("player: ", player)
                print("you lose")
            else:
                print("computer: ", computer)
                print("player: ", player)
                print("you win")
        play_again=input("play again? : (yes/No): ").lower()
        if play_again !="yes":
            break
print("bye bye")