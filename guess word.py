from tkinter import *
from tkinter import messagebox
import random
import sys

class Counter(object):
        countNotGuessed = 0
        countGuessed = 0
        is_changed = False

#EVENTS:
def make_button():
    def check_lose_win():
        if (Counter.countNotGuessed > 5):
            messagebox.showwarning("You lose", "You guessed wrong more than 5 times, you LOSE, haha, dumbass")
            sys.exit()
        if(Counter.countGuessed > len(random_word)-1):
            messagebox.showwarning("Congratulations", "You guessed the word, you WIN!")
            sys.exit()

    def increase_count(button):
        if(Counter.is_changed):
            Counter.countGuessed += random_word.count(button['text'])
        else:
            Counter.countNotGuessed += 1
            count_string.set(str(Counter.countNotGuessed) + "/5")
        Counter.is_changed = False

    def set_text(button):
            for b in buttons:
                if b.get_content() == button['text']:
                 b['text'] = b.get_content()
                 Counter.is_changed = True
            increase_count(button)
            check_lose_win()

    buttonA = Button(frame2, text="A", width=10, command = lambda: set_text(buttonA))
    buttonA.grid(row=3, column=0, sticky=W)
    buttonB = Button(frame2, text="B", width=10, command = lambda: set_text(buttonB))
    buttonB.grid(row=3, column=1, sticky=W)
    buttonC = Button(frame2, text="C", width=10, command = lambda: set_text(buttonC))
    buttonC.grid(row=3, column=2, sticky=W)
    buttonD = Button(frame2, text="D", width=10, command = lambda: set_text(buttonD))
    buttonD.grid(row=3, column=3, sticky=W)
    buttonE = Button(frame2, text="E", width=10, command = lambda: set_text(buttonE))
    buttonE.grid(row=3, column=4, sticky=W)
    buttonF = Button(frame2, text="F", width=10, command = lambda: set_text(buttonF))
    buttonF.grid(row=3, column=5, sticky=W)
    buttonG = Button(frame2, text="G", width=10, command = lambda: set_text(buttonG))
    buttonG.grid(row=3, column=6, sticky=W)
    buttonH = Button(frame2, text="H", width=10, command = lambda: set_text(buttonH))
    buttonH.grid(row=4, column=0, sticky=W)
    buttonI = Button(frame2, text="I", width=10, command = lambda: set_text(buttonI))
    buttonI.grid(row=4, column=1, sticky=W)
    buttonJ = Button(frame2, text="J", width=10, command = lambda: set_text(buttonJ))
    buttonJ.grid(row=4, column=2, sticky=W)
    buttonK = Button(frame2, text="K", width=10, command = lambda: set_text(buttonK))
    buttonK.grid(row=4, column=3, sticky=W)
    buttonL = Button(frame2, text="L", width=10, command = lambda: set_text(buttonL))
    buttonL.grid(row=4, column=4, sticky=W)
    buttonM = Button(frame2, text="M", width=10, command = lambda: set_text(buttonM))
    buttonM.grid(row=4, column=5, sticky=W)
    buttonN = Button(frame2, text="N", width=10, command = lambda: set_text(buttonN))
    buttonN.grid(row=4, column=6, sticky=W)
    buttonO = Button(frame2, text="O", width=10, command = lambda: set_text(buttonO))
    buttonO.grid(row=5, column=0, sticky=W)
    buttonP = Button(frame2, text="P", width=10, command = lambda: set_text(buttonP))
    buttonP.grid(row=5, column=1, sticky=W)
    buttonQ = Button(frame2, text="Q", width=10, command = lambda: set_text(buttonQ))
    buttonQ.grid(row=5, column=2, sticky=W)
    buttonR = Button(frame2, text="R", width=10, command = lambda: set_text(buttonR))
    buttonR.grid(row=5, column=3, sticky=W)
    buttonS = Button(frame2, text="S", width=10, command = lambda: set_text(buttonS))
    buttonS.grid(row=5, column=4, sticky=W)
    buttonT = Button(frame2, text="T", width=10, command = lambda: set_text(buttonT))
    buttonT.grid(row=5, column=5, sticky=W)
    buttonU = Button(frame2, text="U", width=10, command = lambda: set_text(buttonU))
    buttonU.grid(row=5, column=6, sticky=W)
    buttonV = Button(frame2, text="V", width=10, command = lambda: set_text(buttonV))
    buttonV.grid(row=6, column=0, sticky=W)
    buttonW = Button(frame2, text="W", width=10, command = lambda: set_text(buttonW))
    buttonW.grid(row=6, column=1, sticky=W)
    buttonX = Button(frame2, text="X", width=10, command = lambda: set_text(buttonX))
    buttonX.grid(row=6, column=2, sticky=W)
    buttonY = Button(frame2, text="Y", width=10, command = lambda: set_text(buttonY))
    buttonY.grid(row=6, column=3, sticky=W)
    buttonZ = Button(frame2, text="Z", width=10, command = lambda: set_text(buttonZ))
    buttonZ.grid(row=6, column=4, sticky=W)
    label_wrong= Label(frame2, text= "Wrong: ").grid(row=6,column =5, sticky =W)
    count_string = StringVar()
    count_string.set(str(Counter.countNotGuessed) + "/5")
    label_count= Label(frame2, textvariable =count_string).grid(row =6, column = 6, sticky=W)

#POPULATE:
list = ["ELEPHANT", "MATHEMATICS", "COMPUTER", "BAZINGA", "ZIGZAG", "YOLO", "SNAKE",
        "CAT", "MEOW", "WORLD", "JOHN", "SNOW", "THRONE", "DRAGON", "FRIENDS",
        "HOUSE", "LONDON", "THEORY", "WEIGHT", "SCIENTIST", "WINTER", "AUTUMN", "PIANO", "PALACE",
        "INCOMPREHENSIBILITY", "INTELLIGENCE", "WOLVES", "MOTHER", "FATHER", "PSYCHOLOGY",
        "PHILOSOPHY", "UNCOPYRIGHTABLE", "SPONGEBOB", "ANOMALISTIC", "ACCOUNTING", "MAGNANIMOUS",
        "PENULTIMATE", "PERFIDIOUSNESS", "DUMBASS", "WINEBIBBER", "DRUG", "PAPRIKA"]
random_word = random.choice(list)


#GUI:
root = Tk()

frame = Frame(root)
frame2 = Frame(root)
title_label = Label(root, text="Guess the word").pack()

class ButtonExtended(Button):
    def __init__(self, content = "", *args, **kwargs):
        self.content = content
        Button.__init__(self, *args, **kwargs)
    def set_content(self, value):
      self.content = value
    def get_content(self):
      return self.content

buttons = []
for i in range(len(random_word)):
    button = ButtonExtended(random_word[i],frame, text = "", width = 5)
    button.grid(row =0, column = i)
    buttons.append(button)

make_button()


frame.pack(side = TOP)
frame2.pack()


root.mainloop()

