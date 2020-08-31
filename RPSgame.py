from mainRPS import main
from tkinter import *
from PIL import ImageTk, Image
# main window
screen = Tk()
screen.title("Rock Paper Scissors")
screen.geometry("630x510")
screen.configure(bg= "purple")

# help/ instructions window to explain game
def help_win():
    global lb2
    global bt2
    top = Toplevel()
    top.title("Instructions")
    lb2 = Label(top,text="Rock paper scissors is a game played between two people, in which each player\n"
                         "simultaneously forms one of three shapes \"rock\", \"paper\", and \"scissors\".\n\n"
                         " The outcome of the game is determined by 3 simple rules:\n"
                         "- Rock wins against scissors.\n"
                         "- Scissors win against paper.\n"
                         "- Paper wins against rock.\n\nHave Fun!!", anchor = W).pack(side = TOP,pady = 5,padx = 5, fill="both")
    bt2 = Button(top,text="Close Window", command = top.destroy).pack(side= BOTTOM, pady=5)

# help tab
mainmenu = Menu(screen)
screen.config(menu = mainmenu)
submen= Menu(mainmenu)
mainmenu.add_command(label = "Help", command = help_win)

# window title
title = Label(screen,text="Rock Paper Scissors", font =("impact",35,"bold"), bg = "purple", fg= "white").grid(row = 0,column = 2, sticky=W+E)

# options for countdown
option = ["Rock", "Paper", "Scissors", "Shoot!"]

# rock choice function
def rock(t=0):
    global i
    i = 1
    # countdown before game starts
    if(i==1):
        choice.config(text=option[t], fg="white", font=("impact", 20))
        if (t<3):
            screen.after(600,rock,t+1)
        else:
            i = 0
    # grabbing outcome from main and adding results to window
            game = main()
            if game.main("ROCK")[-1] == "n":
                choice.config(text= "Player choice: ROCK \nComputer choice: SCISSORS\nYou Win", fg="green", font=("impact", 20))
            elif game.main("ROCK")[-1] == "w":
                choice.config(text= "Player choice: ROCK \nComputer choice: ROCK\nDRAW", fg="grey", font=("impact", 20))
            else:
                choice.config(text= "Player choice: ROCK \nComputer choice: PAPER\nComputer Wins", fg="red", font=("impact", 20))




# paper choice function
def paper(t=0):
    global i
    i = 1
    if (i == 1):
        # changing the text on window for countdown
        choice.config(text=option[t], fg="white", font=("impact", 20))
        if (t < 3):
            screen.after(600, paper, t + 1)
        else:
            i = 0
            game = main()
            if game.main("PAPER")[-1] == "n":
                choice.config(text="Player choice: PAPER \nComputer choice: ROCK\nYou Win", fg="green",
                              font=("impact", 20))
            elif game.main("ROCK")[-1] == "w":
                choice.config(text="Player choice: PAPER \nComputer choice: PAPER\nDRAW", fg="grey", font=("impact", 20))
            else:
                choice.config(text="Player choice: PAPER \nComputer choice: SCISSORS\nComputer Wins", fg="red",
                              font=("impact", 20))

# scissors choice function
def scissors(t=0):
    global i
    i = 1
    if(i==1):
        choice.config(text=option[t],fg="white",font=("impact",20))
        if (t<3):
            screen.after(600,scissors,t+1)
        else:
            i = 0
            game = main()
            if game.main("SCISSORS")[-1] == "n":
                choice.config(text= "Player choice: SCISSORS \nComputer choice: PAPER\nYou Win", fg="green", font=("impact", 20))
            elif game.main("ROCK")[-1] == "w":
                choice.config(text= "Player choice: SCISSORS \nComputer choice: SCISSORS\nDRAW", fg="grey", font=("impact", 20))
            else:
                choice.config(text= "Player choice: SCISSORS \nComputer choice: ROCK\nComputer Wins", fg="red", font=("impact", 20))

# space to separate elements

space1 = Label(screen, text=" ",font =("impact",10), bg = "purple", fg= "white",padx=10,pady=10).grid(row = 1, column = 1)

# header for button options
weapon_choices = Label(screen,text="Choose Your Weapon! ", font =("impact",20), bg = "purple", fg= "gold",padx=10,pady=10)
weapon_choices.grid(row = 2,column = 2)

space1 = Label(screen, text=" ",font =("impact",10), bg = "purple", fg= "white",padx=10,pady=10).grid(row = 3, column = 1)

# adding images and resizing them
my_img = Image.open("img/rock.png")
my_img2 = Image.open("img/paper.png")
my_img3 = Image.open("img/scissors.png")
resized = my_img.resize((100,100), Image.ANTIALIAS)
resized2 = my_img2.resize((100,100), Image.ANTIALIAS)
resized3 = my_img3.resize((100,100), Image.ANTIALIAS)


rock_pic = ImageTk.PhotoImage(resized)
pap_pic = ImageTk.PhotoImage(resized2)
scis_pic = ImageTk.PhotoImage(resized3)

# choice buttons, with functions added to command
rock_but = Button(screen, image=rock_pic, bg = "purple", width = 100, command = rock)
pap_but = Button(screen, image=pap_pic, bg = "purple", width = 100, command = paper)
sci_but = Button(screen, image=scis_pic, bg = "purple", width = 100, command = scissors)
rock_but.grid(row = 8,column = 1)
pap_but.grid(row = 8,column = 2)
sci_but.grid(row = 8,column = 3)


space1 = Label(screen, text=" ",font =("impact",20), bg = "purple", fg= "white",padx=10,pady=10).grid(row = 9, column = 1)


# displays the outcome of the game
choice = Label(screen, text="", font=("impact", 20), bg="purple", fg="white", padx=10, pady=10)
choice.grid(row=11, column=2,sticky=W + E)

# inserting image and resizing it


# initiate game
screen.mainloop()





