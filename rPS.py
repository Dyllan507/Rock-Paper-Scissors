#Dyllan Spooner
#Creating rock paper scissors against a computer using simple logic
#Rock beats scissors, paper beats rock, scissors beats paper

import random
#going to compare user input by assigning each move with a number and then comparing that to the randomly generated number
#for all intents and purposes rock =1, paper=2, scissors=3 
def rPS():
    #keeping track of stats throughout the games, relatively simple add
    ties = 0
    losses = 0
    wins = 0
    going = True
    while going:
        compMove = random.randint(1,3) #ensures that the computer has a different move every time
        try:
            rps = input("Choose [r]ock, [p]aper, [s]cissors, or [q]uit: ")
            rps = rps.lower()
            #understanding that testing each user input with an if and having the same code under each if is inefficient especially if I wanted to build off of it
            if rps == "r": #if the user chooses r for rock
                
                rps = 1
                if rps == compMove:
                    print("The computer also chose rock. You Tied!")
                    ties = ties + 1
                elif rps+1 == compMove:
                    print("The computer chose paper. You Lose!")
                    losses = losses + 1
                elif rps+2 == compMove: 
                    print("The computer chose scissors. You Win!")
                    wins = wins + 1
                    

            elif rps == "p": #if the user choses p for paper
                rps = 2
                if rps == compMove:
                    print("The computer also chose paper. You Tied!")
                    ties = ties + 1
                elif rps-1 == compMove:
                    print("The computer chose rock. You Win!")
                    wins = wins + 1
                elif rps+1 == compMove:
                    print("The computer chose scissors. You Lose!")
                    losses = losses + 1
            
            elif rps == "s": #if the user chooses s for scissors
                rps = 3
                if rps == compMove:
                    print("The computer also chose scissors. You Tied!")
                    ties = ties + 1
                elif rps-1 == compMove:
                    print("The computer chose paper. You Win!")
                    wins = wins + 1
                elif rps-2 == compMove:
                    print("The computer chose rock. You Lose!")
                    losses = losses+1
            elif rps == "q":
                print("Here are your stats: ")
                print("You won " + str(wins) + " times!")
                print("You lost "+ str(losses) + " times!")
                print("You tied "+ str(ties)+" times!")
                going = False
            else:
                continue
        except: #if the user enters an incorrect data type
            print("Please enter a correct option as indicated by the prompt")
            continue
        



def main():
    rPS()



main()