import pygame
import sys

# Khởi tạo Pygame
pygame.init()

# Thiết lập màn hình
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mouse Example in Pygame")

# Màu sắc và thông số hình tròn
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
circle_radius = 30
circle_pos = [screen_width // 2, screen_height // 2]  # Vị trí ban đầu của hình tròn
dragging = False  # Biến kiểm tra trạng thái kéo thả

# Vòng lặp chính
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Nếu nhấn chuột trái và chuột nằm trong phạm vi hình tròn, kích hoạt kéo
            if event.button == 1:  # Chuột trái
                mouse_x, mouse_y = event.pos
                distance = ((mouse_x - circle_pos[0]) ** 2 + (mouse_y - circle_pos[1]) ** 2) ** 0.5
                if distance < circle_radius:
                    dragging = True
                    
        elif event.type == pygame.MOUSEBUTTONUP:
            # Ngừng kéo khi nhả chuột trái
            if event.button == 1:
                dragging = False

        elif event.type == pygame.MOUSEMOTION:
            # Cập nhật vị trí hình tròn khi đang kéo
            if dragging:
                circle_pos = list(event.pos)

    # Vẽ màn hình
    screen.fill(WHITE)
    pygame.draw.circle(screen, BLUE, circle_pos, circle_radius)
    pygame.display.flip()

# Thoát khỏi Pygame
pygame.quit()
sys.exit()
