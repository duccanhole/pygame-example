# Explain
### Init
- Khởi tạo thanh đỡ.
```python
# Vị trí và tốc độ của thanh đỡ trái
paddle_left_x, paddle_left_y = 50, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2
paddle_left_speed = 5

# Vị trí và tốc độ của thanh đỡ phải
paddle_right_x, paddle_right_y = SCREEN_WIDTH - 50 - PADDLE_WIDTH, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2
paddle_right_speed = 5
```
- Khởi tạo quả bóng.
```python
# Vị trí và tốc độ của bóng
ball_x, ball_y = SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2
ball_speed_x, ball_speed_y = 5, 5
```
### Game loop
- Lắng nghe sự kiện từ bàn phím để điều khiển thanh đỡ.
```python
# Lấy input
keys = pygame.key.get_pressed()
if keys[pygame.K_w] and paddle_left_y > 0:
    paddle_left_y -= paddle_left_speed
if keys[pygame.K_s] and paddle_left_y < SCREEN_HEIGHT - PADDLE_HEIGHT:
    paddle_left_y += paddle_left_speed
if keys[pygame.K_UP] and paddle_right_y > 0:
    paddle_right_y -= paddle_right_speed
if keys[pygame.K_DOWN] and paddle_right_y < SCREEN_HEIGHT - PADDLE_HEIGHT:
    paddle_right_y += paddle_right_speed
```
- Di chuyển quả bóng.
```python
# Cập nhật vị trí bóng
ball_x += ball_speed_x
ball_y += ball_speed_y
```
- Logic khi bóng va chạm với cạnh trên và thanh đỡ
    - Va chạm với cạnh trên: Đổi hướng di chuyển theo trục dọc (y) của bóng.
    - Va chạm với thanh đỡ: Đổi hướng di chuyển theo trục (x) của bóng.
```python
# Va chạm với cạnh trên và dưới
if ball_y <= 0 or ball_y >= SCREEN_HEIGHT - BALL_SIZE:
    ball_speed_y = -ball_speed_y

# Va chạm với thanh đỡ
if (ball_x <= paddle_left_x + PADDLE_WIDTH and paddle_left_y < ball_y < paddle_left_y + PADDLE_HEIGHT) or \
    (ball_x + BALL_SIZE >= paddle_right_x and paddle_right_y < ball_y < paddle_right_y + PADDLE_HEIGHT):
    ball_speed_x = -ball_speed_x
```
- Logic tính điểm khi bóng đi ra khỏi màn hình
```python
# Bóng đi ra khỏi màn hình
if ball_x < 0:
    score_right += 1
    ball_x, ball_y = SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2
    ball_speed_x = -ball_speed_x
elif ball_x > SCREEN_WIDTH:
    score_left += 1
    ball_x, ball_y = SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2
    ball_speed_x = -ball_speed_x
```