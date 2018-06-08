from tkinter import *
from tkinter import messagebox
import random
import sys

count =0
#EVENTS:
def make_button():
    def set_textA(event: NONE):
            for b in buttons:
                if b.get_content() == "A":
                    b['text'] = "A"
                if b.get_content()!="A":
                    global count
                    count +=1
            print(count)
    def set_textB(event: NONE):
            for b in buttons:
                if b.get_content() == "B":
                    b['text'] = "B"
                else:
                    global count
                    count+=1
    def set_textC(event: NONE):
            for b in buttons:
                if b.get_content() == "C":
                    b['text'] = "C"
                else:
                    global count
                    count+=1
    def set_textD(event: NONE):
            for b in buttons:
                if b.get_content() == "D":
                    b['text'] = "D"
                else:
                    global count
                    count+=1
    def set_textE(event: NONE):
            for b in buttons:
                if b.get_content() == "E":
                    b['text'] = "E"
                else:
                    global count
                    count+=1
    def set_textF(event: NONE):
            for b in buttons:
                if b.get_content() == "F":
                    b['text'] = "F"
                else:
                    global count
                    count+=1
    def set_textG(event: NONE):
            for b in buttons:
                if b.get_content() == "G":
                    b['text'] = "G"
                else:
                    global count
                    count+=1
    def set_textH(event: NONE):
            for b in buttons:
                if b.get_content() == "H":
                    b['text'] = "H"
                else:
                    global count
                    count+=1
    def set_textI(event: NONE):
            for b in buttons:
                if b.get_content() == "I":
                    b['text'] = "I"
                else:
                    global count
                    count+=1
    def set_textJ(event: NONE):
            for b in buttons:
                if b.get_content() == "J":
                    b['text'] = "J"
                else:
                    global count
                    count+=1
    def set_textK(event: NONE):
            for b in buttons:
                if b.get_content() == "K":
                    b['text'] = "K"
                else:
                    global count
                    count+=1
    def set_textL(event: NONE):
            for b in buttons:
                if b.get_content() == "L":
                    b['text'] = "L"
                else:
                    global count
                    count+=1
    def set_textM(event: NONE):
            for b in buttons:
                if b.get_content() == "M":
                    b['text'] = "M"
                else:
                    global count
                    count+=1
    def set_textN(event: NONE):
            for b in buttons:
                if b.get_content() == "N":
                    b['text'] = "N"
                else:
                    global count
                    count+=1
    def set_textO(event: NONE):
            for b in buttons:
                if b.get_content() == "O":
                    b['text'] = "O"
                else:
                    global count
                    count+=1
    def set_textP(event: NONE):
            for b in buttons:
                if b.get_content() == "P":
                    b['text'] = "P"
                else:
                    global count
                    count+=1
    def set_textQ(event: NONE):
            for b in buttons:
                if b.get_content() == "Q":
                    b['text'] = "Q"
                else:
                    global count
                    count+=1
    def set_textR(event: NONE):
            for b in buttons:
                if b.get_content() == "R":
                    b['text'] = "R"
                else:
                    global count
                    count+=1
    def set_textS(event: NONE):
            for b in buttons:
                if b.get_content() == "S":
                    b['text'] = "S"
                else:
                    global count
                    count+=1
    def set_textT(event: NONE):
            for b in buttons:
                if b.get_content() == "T":
                    b['text'] = "T"
                else:
                    global count
                    count+=1
    def set_textU(event: NONE):
            for b in buttons:
                if b.get_content() == "U":
                    b['text'] = "U"
                else:
                    global count
                    count+=1
    def set_textV(event: NONE):
            for b in buttons:
                if b.get_content() == "V":
                    b['text'] = "V"
                else:
                    global count
                    count+=1
    def set_textW(event: NONE):
            for b in buttons:
                if b.get_content() == "W":
                    b['text'] = "W"
                else:
                    global count
                    count+=1
    def set_textX(event: NONE):
            for b in buttons:
                if b.get_content() == "X":
                    b['text'] = "X"
                else:
                    global count
                    count+=1
    def set_textY(event: NONE):
            for b in buttons:
                if b.get_content() == "Y":
                    b['text'] = "Y"
                else:
                    global count
                    count+=1
    def set_textZ(event: NONE):
            for b in buttons:
                if b.get_content() == "Z":
                    b['text'] = "Z"
                else:
                    global count
                    count+=1
    buttonA = Button(frame2, text="A", width=10)
    buttonA.bind("<Button-1>", set_textA)
    buttonA.grid(row=3, column=0, sticky=W)
    buttonB = Button(frame2, text="B", width=10)
    buttonB.bind("<Button-1>", set_textB)
    buttonB.grid(row=3, column=1, sticky=W)
    buttonC = Button(frame2, text="C", width=10)
    buttonC.bind("<Button-1>", set_textC)
    buttonC.grid(row=3, column=2, sticky=W)
    buttonD = Button(frame2, text="D", width=10)
    buttonD.bind("<Button-1>", set_textD)
    buttonD.grid(row=3, column=3, sticky=W)
    buttonE = Button(frame2, text="E", width=10)
    buttonE.bind("<Button-1>", set_textE)
    buttonE.grid(row=3, column=4, sticky=W)
    buttonF = Button(frame2, text="F", width=10)
    buttonF.bind("<Button-1>", set_textF)
    buttonF.grid(row=3, column=5, sticky=W)
    buttonG = Button(frame2, text="G", width=10)
    buttonG.bind("<Button-1>", set_textG)
    buttonG.grid(row=3, column=6, sticky=W)
    buttonH = Button(frame2, text="H", width=10)
    buttonH.bind("<Button-1>", set_textH)
    buttonH.grid(row=4, column=0, sticky=W)
    buttonI = Button(frame2, text="I", width=10)
    buttonI.bind("<Button-1>", set_textI)
    buttonI.grid(row=4, column=1, sticky=W)
    buttonJ = Button(frame2, text="J", width=10)
    buttonJ.bind("<Button-1>", set_textJ)
    buttonJ.grid(row=4, column=2, sticky=W)
    buttonK = Button(frame2, text="K", width=10)
    buttonK.bind("<Button-1>", set_textK)
    buttonK.grid(row=4, column=3, sticky=W)
    buttonL = Button(frame2, text="L", width=10)
    buttonL.bind("<Button-1>", set_textL)
    buttonL.grid(row=4, column=4, sticky=W)
    buttonM = Button(frame2, text="M", width=10)
    buttonM.bind("<Button-1>", set_textM)
    buttonM.grid(row=4, column=5, sticky=W)
    buttonN = Button(frame2, text="N", width=10)
    buttonN.bind("<Button-1>", set_textN)
    buttonN.grid(row=4, column=6, sticky=W)
    buttonO = Button(frame2, text="O", width=10)
    buttonO.bind("<Button-1>", set_textO)
    buttonO.grid(row=5, column=0, sticky=W)
    buttonP = Button(frame2, text="P", width=10)
    buttonP.bind("<Button-1>", set_textP)
    buttonP.grid(row=5, column=1, sticky=W)
    buttonQ = Button(frame2, text="Q", width=10)
    buttonQ.bind("<Button-1>", set_textQ)
    buttonQ.grid(row=5, column=2, sticky=W)
    buttonR = Button(frame2, text="R", width=10)
    buttonR.bind("<Button-1>", set_textR)
    buttonR.grid(row=5, column=3, sticky=W)
    buttonS = Button(frame2, text="S", width=10)
    buttonS.bind("<Button-1>", set_textS)
    buttonS.grid(row=5, column=4, sticky=W)
    buttonT = Button(frame2, text="T", width=10)
    buttonT.bind("<Button-1>", set_textT)
    buttonT.grid(row=5, column=5, sticky=W)
    buttonU = Button(frame2, text="U", width=10)
    buttonU.bind("<Button-1>", set_textU)
    buttonU.grid(row=5, column=6, sticky=W)
    buttonV = Button(frame2, text="V", width=10)
    buttonV.bind("<Button-1>", set_textV)
    buttonV.grid(row=6, column=0, sticky=W)
    buttonW = Button(frame2, text="W", width=10)
    buttonW.bind("<Button-1>", set_textW)
    buttonW.grid(row=6, column=1, sticky=W)
    buttonX = Button(frame2, text="X", width=10)
    buttonX.bind("<Button-1>", set_textX)
    buttonX.grid(row=6, column=2, sticky=W)
    buttonY = Button(frame2, text="Y", width=10)
    buttonY.bind("<Button-1>", set_textY)
    buttonY.grid(row=6, column=3, sticky=W)
    buttonZ = Button(frame2, text="Z", width=10)
    buttonZ.bind("<Button-1>", set_textZ)
    buttonZ.grid(row=6, column=4, sticky=W)

#POPULATE:
list = ["ELEPHANT", "MATHEMATICS", "COMPUTER", "BAZINGA", "ZIGZAG", "YOLO", "SNAKE",
        "CAT", "MEOW", "WORLD", "JOHN", "SNOW", "THRONE", "DRAGON", "FRIENDS",
        "HOUSE", "LONDON", "THEORY", "WEIGHT", "SCIENTIST", "WINTER", "AUTUMN"]
random_word = random.choice(list)


#GUI:
root = Tk()

frame = Frame(root)
frame2 = Frame(root)
title_label = Label(root, text="Guess the word. Press letter or word to select the mode", width=70).pack()

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
    button = ButtonExtended(random_word[i],frame, text ="", width = 5)
    button.grid(row =0, column = i)
    buttons.append(button)

make_button()

buttonLetter = Button(frame2, text="Letter", width=10)\
    .grid(row=6, column=5, sticky=W)
buttonWord = Button(frame2, text="Word", width=10)\
    .grid(row=6, column=6, sticky=W)



frame.pack(side = TOP)
frame2.pack()

root.mainloop()

#GAME:
word_guessed = False
while(not word_guessed and count <=5):
    if(count >5):
     messagebox.showwarning("You lose", "You guessed wrong more than 5 times, you LOSE")
     sys.exit()
    if(word_guessed):
     messagebox.showwarning("Congratulations", "You guessed the word, you WIN!")
     sys.exit()
