from tkinter import *
from tkinter import messagebox
import random
import sys

#POPULATE:
list = ["ELEPHANT", "MATHEMATICS", "COMPUTER SCIENCE", "BAZINGA", "ZIGZAG", "YOLO", "SNAKE",
        "CAT", "MEOW", "WORLD", "JOHN SNOW", "GAME OF THRONES", "DRAGON", "FRIENDS",
        "HOUSE", "LONDON", "THEORY", "WEIGHT", "SCIENTIST", "WINTER", "AUTUMN"]
random_word = random.choice(list)

#GAME:
count = 0
word_guessed = False
if(count ==10):
    messagebox.showwarning("You lose", "You guessed wrong 10 times, you LOSE")
    sys.exit()
if(word_guessed):
    messagebox.showwarning("Congratulations", "You guessed the word, you WIN!")
    sys.exit()

#EVENTS:
def set_text(event =None):
    string.set(string.get()+ "A")

#GUI:
root = Tk()

string = StringVar()
frame = Frame(root)
frame2 = Frame(root)
title_lable = Label(frame, text="Guess the word. Press letter or word to select the mode", width=70).pack()
play_lable = Label(frame, textvariable = string, width=70).pack()

buttonA = Button(frame2, text="A", width=10, command=set_text).grid(row=2, column=0, sticky=W)
buttonB = Button(frame2, text="B", width=10, command=set_text).grid(row=2, column=1, sticky=W)
buttonC = Button(frame2, text="C", width=10, command=set_text).grid(row=2, column=2, sticky=W)
buttonD = Button(frame2, text="D", width=10, command=set_text).grid(row=2, column=3, sticky=W)
buttonE = Button(frame2, text="E", width=10, command=set_text).grid(row=2, column=4, sticky=W)
buttonF = Button(frame2, text="F", width=10, command=set_text).grid(row=2, column=5, sticky=W)
buttonG = Button(frame2, text="G", width=10, command=set_text).grid(row=2, column=6, sticky=W)
buttonH = Button(frame2, text="H", width=10, command=set_text).grid(row=3, column=0, sticky=W)
buttonI = Button(frame2, text="I", width=10, command=set_text).grid(row=3, column=1, sticky=W)
buttonJ = Button(frame2, text="J", width=10, command=set_text).grid(row=3, column=2, sticky=W)
buttonK = Button(frame2, text="K", width=10, command=set_text).grid(row=3, column=3, sticky=W)
buttonL = Button(frame2, text="L", width=10, command=set_text).grid(row=3, column=4, sticky=W)
buttonM = Button(frame2, text="M", width=10, command=set_text).grid(row=3, column=5, sticky=W)
buttonN = Button(frame2, text="N", width=10, command=set_text).grid(row=3, column=6, sticky=W)
buttonO = Button(frame2, text="O", width=10, command=set_text).grid(row=4, column=0, sticky=W)
buttonP = Button(frame2, text="P", width=10, command=set_text).grid(row=4, column=1, sticky=W)
buttonQ = Button(frame2, text="Q", width=10, command=set_text).grid(row=4, column=2, sticky=W)
buttonR = Button(frame2, text="R", width=10, command=set_text).grid(row=4, column=3, sticky=W)
buttonS = Button(frame2, text="S", width=10, command=set_text).grid(row=4, column=4, sticky=W)
buttonT = Button(frame2, text="T", width=10, command=set_text).grid(row=4, column=5, sticky=W)
buttonU = Button(frame2, text="U", width=10, command=set_text).grid(row=4, column=6, sticky=W)
buttonV = Button(frame2, text="V", width=10, command=set_text).grid(row=5, column=0, sticky=W)
buttonW = Button(frame2, text="W", width=10, command=set_text).grid(row=5, column=1, sticky=W)
buttonX = Button(frame2, text="X", width=10, command=set_text).grid(row=5, column=2, sticky=W)
buttonY = Button(frame2, text="Y", width=10, command=set_text).grid(row=5, column=3, sticky=W)
buttonZ = Button(frame2, text="Z", width=10, command=set_text).grid(row=5, column=4, sticky=W)
buttonLetter = Button(frame2, text="Letter", width=10, command=set_text).grid(row=5, column=5, sticky=W)
buttonWord = Button(frame2, text="Word", width=10, command=set_text).grid(row=5, column=6, sticky=W)


frame.pack(side = TOP)
frame2.pack()

root.mainloop()


