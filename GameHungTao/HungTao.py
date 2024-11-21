import os
from tkinter import *
from time import sleep
from PIL import ImageTk, Image
from random import randint
from playsound import playsound

ASSETS_FOLDER = os.path.join("GameHungTao")
img = [0, 0, 0]
y = -20
x = randint(20, 690)
game = Tk()
game.title("Catch Apple")
canvas = Canvas(master=game, width=700, height=525, background="white")
canvas.pack()
img[0] = ImageTk.PhotoImage(Image.open(os.path.join(ASSETS_FOLDER, "backgr.png")))
img[1] = ImageTk.PhotoImage(Image.open(os.path.join(ASSETS_FOLDER, "bowl.png")))
img[2] = ImageTk.PhotoImage(Image.open(os.path.join(ASSETS_FOLDER, "apple.png")))
backgr = canvas.create_image(0, 0, anchor=NW, image=img[0])
bowl = canvas.create_image(0, 420, anchor=NW, image=img[1])
apple = canvas.create_image(x, y, anchor=NW, image=img[2])
canvas.update()
score = 0
applet_fail = 0
text_score = canvas.create_text(
    550, 30, text=f"SCORE:{score}, FAIL:{applet_fail}", fill="red", font=("Time", 20)
)


def AppleFall():
    global apple, score, applet_fail
    canvas.move(apple, 0, 10)
    should_reset_apple = False
    if canvas.coords(apple)[1] > 550:
        should_reset_apple = True
        applet_fail = applet_fail + 1
    if (
        canvas.coords(apple)[0] >= canvas.coords(bowl)[0]
        and canvas.coords(apple)[0] + 50 <= canvas.coords(bowl)[0] + 120
    ) and (
        canvas.coords(apple)[1] + 50 >= canvas.coords(bowl)[1]
        and canvas.coords(apple)[1] + 50 <= canvas.coords(bowl)[1] + 37.5
    ):
        playsound(os.path.join(ASSETS_FOLDER, "vacham.wav"))
        should_reset_apple = True
        score = score + 1
    if should_reset_apple:
        canvas.delete(apple)
        y = -20
        x = randint(10, 690)
        apple = canvas.create_image(x, y, anchor=NW, image=img[2])


def right():
    global bowl
    if canvas.coords(bowl)[0] < 650:
        canvas.move(bowl, 20, 0)
    canvas.update()


def left():
    global bowl
    if canvas.coords(bowl)[0] > -10:
        canvas.move(bowl, -20, 0)
    canvas.update()


def keyPress(event):
    if event.keysym == "Right":
        right()
    if event.keysym == "Left":
        left()


canvas.bind_all("<KeyPress>", keyPress)

while True:
    if applet_fail > 5:
        gameOver = True
        canvas.itemconfig(text_score, text="GAME OVER !")
        canvas.update()
        continue
    AppleFall()
    canvas.itemconfig(text_score, text=f"SCORE: {score}, FAIL: {applet_fail}")
    canvas.update()
    sleep(0.05)

# game.mainloop()
