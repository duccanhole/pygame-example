import pygame
import sys

# Khởi tạo Pygame
pygame.init()

# Thiết lập màn hình
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Keyboard Example")

# Màu sắc và thông số hình vuông
WHITE = (255, 255, 255)
RED = (255, 0, 0)
square_size = 50
x, y = screen_width // 2, screen_height // 2  # Vị trí ban đầu của hình vuông
velocity = 5  # Tốc độ di chuyển

# Thiết lập lặp lại phím (tốc độ phản hồi khi giữ phím)
pygame.key.set_repeat(50, 50)

# Vòng lặp chính của trò chơi
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Tăng tốc nếu nhấn giữ Shift
            if event.mod & pygame.KMOD_SHIFT:
                speed = velocity * 2
            else:
                speed = velocity

            # Kiểm tra phím mũi tên để di chuyển hình vuông
            if event.key == pygame.K_LEFT:
                x -= speed
            elif event.key == pygame.K_RIGHT:
                x += speed
            elif event.key == pygame.K_UP:
                y -= speed
            elif event.key == pygame.K_DOWN:
                y += speed

    # Đặt màu nền và vẽ hình vuông
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (x, y, square_size, square_size))

    # Cập nhật màn hình
    pygame.display.flip()

# Thoát khỏi Pygame
pygame.quit()
sys.exit()
