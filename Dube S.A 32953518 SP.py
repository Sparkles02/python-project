"Dube SA Semester Project for CMPG 313"
import random
import time
import datetime
from datetime import timedelta
from tkinter import*

root  = Tk()
root.geometry("1350x750+0+0")
root.title ("Puzzle Game")
root.configure(background ='Black')

Tops = Frame(root, bg ='Black', pady =2, width =1000, height=1000, relief =RIDGE)
Tops.grid(row=0, column=0)

lblTitle =Label(Tops,font=('arial',80,'bold'), text="Puzzle Game", bd=10,bg='Black',
fg='White',justify=CENTER)
lblTitle.grid(row=0,column=0)

MainFrame = Frame(root, bg='Black', bd=10,width =1000, height=600, relief=RIDGE)
MainFrame .grid(row=1,column=0, padx=30)

LeftFrame = Frame(MainFrame, bd=10,width =700, height=600, pady=2,bg ='Black')
LeftFrame .pack(side=LEFT)

RightFrame = Frame(MainFrame ,bd=10, width =540, height=500, padx=1,pady=2, bg="White" )
RightFrame.pack(side=RIGHT)

RightFrame1 = Frame(RightFrame ,bd=10, width =540, height=200, padx=10,pady=2, bg="White" )
RightFrame1.grid(row=0,column=0)

RightFrame2a = Frame(RightFrame ,bd=10, width =540, height=140, padx=10,pady=2, bg="White" )
RightFrame2a.grid(row=1,column=0)

RightFrame2b = Frame(RightFrame ,bd=10, width =540, height=140, padx=10,pady=2, bg="White" )
RightFrame2b.grid(row=2,column=0)

RightFrame3 = Frame(RightFrame ,bd=10, width =540, height=140, padx=10,pady=2, bg="White" )
RightFrame3.grid(row=3,column=0)

startTime = IntVar()
startTime.set(time.time())
timeElasped = StringVar()
numberOfMoves = 0
displayMoves = StringVar()
displayMoves .set("Number of Moves " +  "\n" + "0")

gameStateString  = StringVar()

def upDateCounter():
    global numberOfMoves, displayMoves

    displayMoves .set("Number of Moves " +  "\n" + str(numberOfMoves))

def gameStateUpdate(gameState):
    global gameStateString
    gameStateString.set(gameState)
    
def timeElapsedUpdate(time):
    global timeElasped
    timeElasped.set(time)


class Button_:
    def __init__(self, text_, x, y):
        self.enterValue = text_
        self.textTaken = StringVar()
        self.textTaken.set(text_)
        self.x = x                          
        self.y = y 
        self.btnNumber = Button(LeftFrame, textvariable=self.textTaken, font=('Arial',80),bd = 3,
                command=lambda i=self.x, j=self.y : emptySpotChecker(i, j))
        self.btnNumber.place(x=self.x*150, y=self.y*150, width=170, height=170)        

def shuffle():
    global btnNumbers, numberOfMoves
    nums = []
    for x in range(9):
        x += 1
        if x == 9:
            nums.append("")
        else:
            nums.append(str(x))

    for y in range(len(btnNumbers)):
        for x in range(len(btnNumbers[y])):
            num = random.choice(nums)
            btnNumbers[y][x].textTaken.set(num)
            nums.remove(num)
    numberOfMoves = 0
    upDateCounter()
    gameStateUpdate("")
    startTime.set(time.time())
    timeElapsedUpdate("")
    

lblCount = Label(RightFrame1, textvariable=displayMoves, font=("Arial", 40)).place(x=0, y=10,  width=480, height=160)
btnNumbershuffle = Button(RightFrame2a, text="Reset", font=("Arial", 40),bd=5, command=shuffle).place(x=0, y=10,
                                                                                            width=480, height=100)
lblGameWon = Label(RightFrame2b, textvariable=gameStateString, font=("Arial", 40)).place(x=0, y=10,  width=480, height=100)

lblTimer = Label(RightFrame3, textvariable=timeElasped , font =("Arial", 40)).place(x=0, y=10, width=480,height=90)

btnNumbers = []

name = 0

for y in range(3):
    btnNumbers_ = []
    for x in range(3):
        name += 1
        if name == 9:
            name = ""
        btnNumbers_.append(Button_(str(name), x, y))
    btnNumbers.append(btnNumbers_)

shuffle()

def emptySpotChecker(y,x):
    global btnNumbers, numberOfMoves

    if not btnNumbers[x][y].textTaken.get() == "":
        for i in range(-1,2):
            newX = x + i

            if not(newX < 0 or len(btnNumbers)-1 < newX or i == 0):
                if btnNumbers[newX][y].textTaken.get() == "":
                    text = btnNumbers[x][y].textTaken.get()
                    btnNumbers[x][y].textTaken.set(btnNumbers[newX][y].textTaken.get())
                    btnNumbers[newX][y].textTaken.set(text)
                    winCheck()
                    break

        for j in range(-1,2):
            newY = y + j

            if not(newY < 0 or len(btnNumbers[0])-1 < newY or j == 0):
                if btnNumbers[x][newY].textTaken.get() == "":
                    text = btnNumbers[x][y].textTaken.get()
                    btnNumbers[x][y].textTaken.set(btnNumbers[x][newY].textTaken.get())
                    btnNumbers[x][newY].textTaken.set(text)
                    winCheck()
                    break

        numberOfMoves += 1
        upDateCounter()


def winCheck():
    lost = False
    for y in range(len(btnNumbers)):
        for x in range(len(btnNumbers[y])):
            if btnNumbers[y][x].enterValue != btnNumbers[y][x].textTaken.get():
                lost = True
                break
    if not lost:
        gameStateUpdate("You win!")
        endTime = IntVar()
        endTime.set(time.time())
        timeLapsed = endTime.get() - startTime.get()
        td = str(timedelta(seconds = timeLapsed))
        timeElapsedUpdate(td)
        
root.mainloop()