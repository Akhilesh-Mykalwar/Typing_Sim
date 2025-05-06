# Import Module
from cProfile import label

from pygame import mixer
from tkinter import *
from tkinter import messagebox
import random
import textwrap



def Button_Pressed():
    stopwatch.destroy()
    mixer.music.play()
    timer()

word_list = ["Invest", "Ship", "Catfish", "Jackpot", "Significance", "Carsick", "Kitchenette", "Sometimes",
              "Celebrate", "Law", "Sublime", "Exasperation", "Exhilarating", "Philanthropy", "Psychology", "Pizza",
              "India", "Schizophrenia", "Whatever", "Tired", "Coding", "Capslocklol", "Parkinsons", "Onomatopoeia"]
i = 0
correct = 0
wrong = 0
timeleft = 60
mixer.init()
mixer.music.load("C:\\Users\\Akhil\\OneDrive\\Desktop\\Desktop\\Coding Only\\music.mp3")






def timer():

    
    global timeleft,i,finalscore,correct,wrong
    if timeleft > 0:
        timeleft -= 1
        timelabel.config(text=timeleft)
        timelabel.after(1000, timer)
    else:
        wordentry.config(state=DISABLED)
        finalscore = correct - wrong
        instruction.config(text=f"correct={correct}\nwrong={wrong}\nfinalscore={finalscore}")

        ##if 13>finalscore<=12:

           # emojilabel1.place(x=50, y=650)
            #emojilabel1.place(x=600, y=650)

        if 13>finalscore>=0:
            emojilabel.config(image=noob)
            emojilabel1.config(image=noob)
            emojilabel2.config(image=noob1)
        if 22>finalscore>=13:

            emojilabel.config(image=inter)
            emojilabel1.config(image=inter)
            emojilabel2.config(image=inter1)
        if 30>finalscore>=22:
            emojilabel.config(image=pro)
            emojilabel1.config(image=pro)
            emojilabel2.config(image=god)
        res = messagebox.askyesno("CONFIRM", "DO YOU WANT TO PLAY AGAIN")
        if res:
            i=0
            finalscore=0
            correct=0
            wrong=0
            timeleft=60
            countlabel.config(text="0")
            timelabel.config(text="60")
            wordentry.config(state=NORMAL)
            instruction.config(text="ALRIGHT LETS SEE\nYOU TRY AGAIN")
            emojilabel.config(image="")
            emojilabel1.config(image="")
            emojilabel2.config(image="")
            stopwatch = Button(root, bg = 'white',text = 'start',bd = 40,command = Button_Pressed,font = ('bold',55))
            stopwatch.place (x=300,y=400)
        
        
        else:
            root.quit()


def playgame(game):

   
    global i, correct, wrong
    i += 1
    if wordentry.get() == word_list[0]:
        correct += 1
    if wordentry.get()!=word_list[0]:
        wrong+=1
    countlabel.config(text=i)
    random.shuffle(word_list)
    Wordlistlabel.config(text=word_list[0])
    wordentry.delete(0, END)

   
       




# create root window
root = Tk()

# root window title and dimension
root.title("Typing Game#1")
# Set geometry (widthxheight)
root.geometry('800x800')
root.resizable(0, 0)
root.iconbitmap("icon.ico")
root.config(bg="indian red")
logo = PhotoImage(file="stopwatch.png")
logoLabel = Label(root, image=logo, bg="indian red")
logoLabel.place(x=270, y=100)
Movinglabel = Label(root, text="Typing Simulator 2024", bg="indian red", font=("Georgia", 30, "bold italic"))
Movinglabel.place(x=150, y=10)
random.shuffle(word_list)
Wordlistlabel = Label(root, text=word_list[0], fg="yellow", bg="indian red", font=("Georgia", 30, "bold italic"))
Wordlistlabel.place(x=400, y=450, anchor=CENTER)
wordlabel = Label(root, text="WORDS", bg="indian red", fg="dark green", font=("Castellar", 30, "bold"))
wordlabel.place(x=30, y=200)
countlabel = Label(root, text=0, bg="indian red", font=("Castellar", 30, "bold"))
countlabel.place(x=90, y=290)
timelabel = Label(root, text=timeleft, bg="indian red", font=("Castellar", 30, "bold"))
timelabel.place(x=650, y=290)
timelabel1 = Label(root, text="TIME", fg="dark green", bg="indian red", font=("Castellar", 30, "bold"))
timelabel1.place(x=620, y=200)
wordentry = Entry(root, font=("arial", 30, "bold"), bd=9, justify=CENTER)
wordentry.place(x=170, y=570)
wordentry.focus_set()
instruction = Label(root, text="START TYPING NIGGA", bg="indian red", font=("Times New Roman", 25, "bold italic"))
instruction.place(x=225, y=670)
inter=PhotoImage(file="intermediate.png")
inter=PhotoImage(file="intermediate.png")
inter1=PhotoImage(file="intermediate1.png")
noob = PhotoImage(file="noob1.png")
noob = PhotoImage(file="noob1.png")
noob1=PhotoImage(file="noob2.png")
noob1=PhotoImage(file="noob2.png")
pro = PhotoImage(file="badge.png")
pro = PhotoImage(file="badge.png")
god=PhotoImage(file="god.png")
emojilabel1=Label(root,bg="indian red")
emojilabel1.place(x=50,y=650)
emojilabel=Label(root,bg="indian red")
emojilabel.place(x=600,y=650)
emojilabel2=Label(root,bg="indian red")
emojilabel2.place(x=150,y=250)
root.bind("<Return>", playgame)

stopwatch = Button(root,width=20,height=1, bg = 'white',text = '\nstart\n',bd = 10,command = Button_Pressed,font = ('bold',25))
stopwatch.place (x=200,y=420)
        


    
instruction.config(text="")

# all widgets will be here
# Execute Tkinter
root.mainloop()