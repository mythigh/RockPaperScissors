from random import *
import time
# my code
class main():

    # selecting a button runs the function and inputs a choice
    def main(self,choice):
        x = True
        while x:
            if choice == 'ROCK':
                p1 = "Rock"
                x = False
            elif choice == 'PAPER':
                p1 = "Paper"
                x = False
            elif choice == 'SCISSORS':
                p1 = "Scissors"
                x = False
            else:
                print("Invalid Input")


        # cpu's choice is randomly selected
        option = ["Rock", "Paper", "Scissors", "Shoot!\n"]
        cpu = option[randint(0, 2)]


        result = " "

        # different outcomes for the game

        if p1 == cpu:
            result = "Draw"
        elif (p1 == "Rock" and cpu == "Paper") or (p1 == "Paper" and cpu == "Scissors") or (p1 == "Scissors" and cpu == "Rock"):
            result = "Computer Wins"
        elif (p1 == "Rock" and cpu == "Scissors") or (p1 == "Paper" and cpu == "Rock") or (p1 == "Scissors" and cpu == "Paper"):
            result = "You Win"

        return result
