import random
import tkinter

window = tkinter.Tk()
window.title("Game")
window.resizable(0,0)
window.geometry("800x600")
window.configure(bg="cyan")

item = ["Rock", "Paper", "Scissor"]

def selected_rock():
    rock.configure(bg="magenta")
    paper.configure(bg="white")
    Scissor.configure(bg="white")
    global player
    player="Rock"
def selected_paper():
    paper.configure(bg="magenta")
    rock.configure(bg="white")
    Scissor.configure(bg="white")
    global player
    player="Paper"
def selected_scissor():
    Scissor.configure(bg="magenta")
    rock.configure(bg="white")
    paper.configure(bg="white")
    global player
    player="Scissor"

def play2():
    l2.destroy()
    l3.destroy()
    play_again.destroy()
    exit.destroy()
    play()

def end():
    window.destroy()

def game():
    computer = item[random.randint(0,2)]
    global result
    global l2
    global l3
    global play_again
    global exit
    result=""
    if player==computer:
        result="Tie"
    elif player=="Rock" and computer=="Paper":
        result="You Lose"
    elif player=="Paper" and computer=="Scissor":
        result="You Lose"
    elif player=="Scissor" and computer=="Rock":
        result="You Lose"
    else:
        result="You Won"
    l1.configure(text=result)
    statement = "Computer chose: "+computer
    l2 = tkinter.Label(window, text=statement, font = ("Arial Bold",25))
    l2.place(x=200,y=250)
    sta="You chose: "+player
    l3 = tkinter.Label(window, text=sta, font = ("Arial Bold",25))
    l3.place(x=200,y=200)
    rock.destroy()
    Scissor.destroy()
    paper.destroy()
    submit.destroy()
    play_again = tkinter.Button(window, text="Play Again", height=2, width=20, bg="ivory3", command=play2)
    play_again.place(x=300,y=400)
    exit= tkinter.Button(window, text="Exit", height=2, width=20, bg="red", command=end)
    exit.place(x=300, y=500)


def play():
    l1.configure(text="Choose your option")
    bt.destroy()
    global rock
    global paper
    global Scissor
    global submit
    rock = tkinter.Button(window, text="Rock", height=2, width=20, command=selected_rock)
    rock.place(x=100, y=200)
    paper = tkinter.Button(window, text="Paper", height=2, width=20, command= selected_paper)
    paper.place(x=300, y=200)
    Scissor = tkinter.Button(window, text="Scissor", height=2, width=20, command=selected_scissor)
    Scissor.place(x=500, y=200)
    submit = tkinter.Button(window, text="Submit", height=2, width=20, bg="yellow", command=game)
    submit.place(x=300, y=400)


l1 = tkinter.Label(window, text = "Rock Paper Scissor", font = ("Arial Bold",50))
l1.place(x=70,y=0)
bt = tkinter.Button(window, text="Play", height=2, width=50, bg="yellow", command=play)
bt.place(x=200,y=300)

window.mainloop()