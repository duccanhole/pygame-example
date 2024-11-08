import pygame
import sys

# Khởi tạo Pygame
pygame.init()

# Kích thước màn hình
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Đặt FPS
FPS = 60
clock = pygame.time.Clock()

# Kích thước và vị trí của thanh đỡ và bóng
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 20

# Vị trí và tốc độ của thanh đỡ trái
paddle_left_x, paddle_left_y = 50, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2
paddle_left_speed = 5

# Vị trí và tốc độ của thanh đỡ phải
paddle_right_x, paddle_right_y = SCREEN_WIDTH - 50 - PADDLE_WIDTH, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2
paddle_right_speed = 5

# Vị trí và tốc độ của bóng
ball_x, ball_y = SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2
ball_speed_x, ball_speed_y = 5, 5

# Điểm số
score_left = 0
score_right = 0
font = pygame.font.Font(None, 36)

# Vòng lặp chính
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

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

    # Cập nhật vị trí bóng
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Va chạm với cạnh trên và dưới
    if ball_y <= 0 or ball_y >= SCREEN_HEIGHT - BALL_SIZE:
        ball_speed_y = -ball_speed_y

    # Va chạm với thanh đỡ
    if (ball_x <= paddle_left_x + PADDLE_WIDTH and paddle_left_y < ball_y < paddle_left_y + PADDLE_HEIGHT) or \
       (ball_x + BALL_SIZE >= paddle_right_x and paddle_right_y < ball_y < paddle_right_y + PADDLE_HEIGHT):
        ball_speed_x = -ball_speed_x

    # Bóng đi ra khỏi màn hình
    if ball_x < 0:
        score_right += 1
        ball_x, ball_y = SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2
        ball_speed_x = -ball_speed_x
    elif ball_x > SCREEN_WIDTH:
        score_left += 1
        ball_x, ball_y = SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2
        ball_speed_x = -ball_speed_x

    # Vẽ các đối tượng
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (paddle_left_x, paddle_left_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (paddle_right_x, paddle_right_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, BALL_SIZE, BALL_SIZE))
    pygame.draw.aaline(screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT))

    # Hiển thị điểm số
    score_text = font.render(f"{score_left} - {score_right}", True, WHITE)
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 20))

    # Cập nhật màn hình
    pygame.display.flip()
    clock.tick(FPS)
