# Explain
# Game loop
- Vẽ nền.
```python
background1_rect = screen.blit(background, (background_x, background_y))
background2_rect = screen.blit(background, (background_x + 600, background_y))
```
- Vẽ khủng long.
```python
dinosaur_rect = screen.blit(dinosaur, (dinosaur_x, dinosaur_y))
```
- Vẽ điểm.
```python
score_txt = font.render("Score:" + str(score), True, RED)
```
- Vẽ cây.
```python
tree_rect = screen.blit(tree, (tree_x, tree_y))
```
- Lắng nghe sự kiện từ bàn phím để di chuyển khủng long.
```python
for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game_over:
                    background_x = 0
                    background_y = 0
                    dinosaur_x = 0
                    dinosaur_y = 230
                    tree_x = 550
                    tree_y = 230
                    x_velocity = 5
                    y_velocity = 7
                    score = 0
                    game_over = False
                elif dinosaur_y == 230:
                    pygame.mixer.Sound.play(sound1)
                    jump = True
if 230 >= dinosaur_y >= 80:
    if jump == True:
            dinosaur_y -= y_velocity
    else:
        jump = False
if dinosaur_y < 230:
    if jump == False:
        dinosaur_y += y_velocity
```
- Di chuyển cây và nền dần về bên trái, nếu cây biến mất khỏi màn hình, reset vị trí của cây và cộng điểm cho người chơi.
```python
if background_x + 600 <= 0:
        background_x = 0
    tree_x -= x_velocity
if tree_x <= -20:
        tree_x = 550
        score += 1
```
- Kiểm tra xem khủng long có va chạm với cây hay không, nếu có thì hiển thị "Game Over" và dừng trò chơi.
```python
if dinosaur_rect.colliderect(tree_rect):
    game_over = True
    pygame.mixer.Sound.play(sound2)
if game_over:
    gameover_txt = font1.render("GAME OVER", True, RED)
    gameover_txt2 = font1.render("PRESS SPACE TWICE TO PLAY AGAIN", True, RED)
    screen.blit(gameover_txt, (0, 130))
    screen.blit(gameover_txt2, (0, 160))
    x_velocity = 0
    y_velocity = 0
    pygame.display.flip()
    continue
```