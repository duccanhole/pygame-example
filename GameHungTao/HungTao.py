from tkinter import *
from time import sleep
from PIL import ImageTk,Image
from random import randint
from playsound import playsound
img = [0,0,0]
y=-20
x=randint(20,690)
game=Tk()
game.title("Catch Apple")
canvas=Canvas(master=game,width=700,height=525,background="white")
canvas.pack()
img[0]=ImageTk.PhotoImage(Image.open("backgr.png"))
img[1]=ImageTk.PhotoImage(Image.open("bowl.png"))
img[2]=ImageTk.PhotoImage(Image.open("apple.png"))
backgr=canvas.create_image(0,0,anchor=NW,image=img[0])
bowl=canvas.create_image(0,420,anchor=NW,image=img[1])
apple=canvas.create_image(x,y,anchor=NW,image=img[2])
canvas.update()
score=0
text_score=canvas.create_text(620,30,text="SCORE:"+str(score),fill="red",font=("Time",20))
def AppleFall():
    global apple,score
    canvas.move(apple,0,10)
    if canvas.coords(apple)[1]>550:
        canvas.delete(apple)
        y=-20
        x=randint(10,690)
        apple=canvas.create_image(x,y,anchor=NW,image=img[2])
    if (canvas.coords(apple)[0]>=canvas.coords(bowl)[0] and canvas.coords(apple)[0]+50<=canvas.coords(bowl)[0]+120) and (canvas.coords(apple)[1]+50>=canvas.coords(bowl)[1]and canvas.coords(apple)[1]+50<=canvas.coords(bowl)[1]+37.5):
        playsound("vacham.wav")
        canvas.delete(apple)
        y=-20
        x=randint(10,690)
        apple=canvas.create_image(x,y,anchor=NW,image=img[2])
        score=score+1
        canvas.itemconfig(text_score,text="SCORE:"+str(score))
    canvas.update()
def right():
    global bowl
    if canvas.coords(bowl)[0]<650:
        canvas.move(bowl,20,0)
    canvas.update()
    
def left():
    global bowl
    if canvas.coords(bowl)[0]>-10:
        canvas.move(bowl,-20,0)
    canvas.update()

def keyPress(event):
    if event.keysym=="Right":
        right()
    if event.keysym=="Left":
        left()
    
canvas.bind_all("<KeyPress>",keyPress)
gameOver=False
while not gameOver:
    AppleFall()
    sleep(0.05)

game.mainloop()

