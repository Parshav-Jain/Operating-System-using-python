from tkinter import *
import random
root = Tk()
root.title('Color Game')
root.geometry('375x200')
root.resizable(0,0)

colors = ['Red','Blue','Orange','Pink','Black','Green','Yellow','White','Purple','Brown']
score = 0
timeleft = 60
def startGame(event):
    if timeleft == 60:
        countdown()
    nextColor()

def nextColor():
    global score 
    global timeleft
    if timeleft > 0 :
        e.focus_set()
        if e.get().lower() == colors[1].lower():
            score+=1
        e.delete(0,END)
        random.shuffle(colors)
        label.config(fg = str(colors[1]) , text = str(colors[0]))
        score_label.config(text = 'Score :'+str(score))
    
def countdown():
    global timeleft
    if timeleft > 0 :
        timeleft -= 1
        time_label.config(text = 'Time Left : ' + str(timeleft))
        time_label.after(1000,countdown)


instructions = Label(root,text = 'Type the color of the words , and not the word text !' , font = ('Helevetica',12))
score_label = Label(root,text = 'Press Enter To Start' , font = ('Arial',12))
time_label = Label(root,text = 'Time Left : ' + str(timeleft),font = ('Arial',12))
label = Label(root,font = ('Helvetica' , 60))
instructions.pack()
score_label.pack()
time_label.pack()
label.pack()

e = Entry(root)
root.bind('<Return>',startGame)
e.pack()
e.focus_set()




root.mainloop()
