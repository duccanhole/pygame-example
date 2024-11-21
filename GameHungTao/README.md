# Explain
### Function
- `AppleFall`
    - Cho trái táo rơi xuống.
    ```python
    canvas.move(apple, 0, 10)
    ```
    - Nếu trái táo rơi xuống đất, đặt biến `reset = True`, tăng biến đếm trái số lần hứng táo thất bại.
    ```python
    if canvas.coords(apple)[1] > 550:
        should_reset_apple = True
        applet_fail = applet_fail + 1
    ```
    - Nếu trái táo rơi vào giỏ, tăng số điểm người chơi, đặt biến `reset = True`.
    ```python
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
    ```
    - Kiểm tra giá trị của biến `reset`, nếu giá trị là `True`, xóa trái táo hiện tại và tạo mới một trái táo khác.
    ```python
    if should_reset_apple:
        canvas.delete(apple)
        y = -20
        x = randint(10, 690)
        apple = canvas.create_image(x, y, anchor=NW, image=img[2])
    ```
    - Lắng nghe sự kiện bàn phím để di chuyển giỏ đựng.
    ```python
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
    ```
### Game loop
- Kiểm tra số lần hứng táo thất bại, nếu vượt quá 5 lần, hiển thị game over và dừng trò chơi.
```python
if applet_fail > 5:
    gameOver = True
    canvas.itemconfig(text_score, text="GAME OVER !")
    canvas.update()
    continue
```
- Chạy hàm `AppleFall`.
- Hiển thị điểm và số lần hứng táo thất bại lên màn hình.
```python
canvas.itemconfig(text_score, text=f"SCORE: {score}, FAIL: {applet_fail}")
canvas.update()
```