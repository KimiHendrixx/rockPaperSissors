import random

def rpsGame():
    
    # choice of the user
    user = input("Hello, play rock, paper, sissors with me! Type in 'rock', 'paper'or 'sissors'>>>   ")

    # choice of computer
    computer = random.choice(["rock", "paper", "sissors"])

    # tie situation
    while computer == user:
        print("\nTie! Please try again")
        user = input("\nType in 'rock', 'paper' or 'sissors'>>>   ")
        computer = random.choice(["rock", "paper", "sissors"])

    # conditions in which the user wins
    user_wins = False
    user_wins = (user=="rock") and (computer=="sissors") or (user=="sissors") and (computer=="paper") or (user=="paper") and (computer=="rock")

    # output of the solution
    if user_wins == True:
        print(f"\nYou put out {user} and I put out {computer}, so you win!\n")
    else: 
        print(f"\nYou put out {user} and I put out {computer}, so I win!\n")

rpsGame()