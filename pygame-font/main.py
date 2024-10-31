import pygame
import sys

# Khởi tạo Pygame
pygame.init()

# Thiết lập màn hình
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Font Example in Pygame")

# Khởi tạo font
pygame.font.init()

# Sử dụng font hệ thống
sys_font = pygame.font.SysFont('arial', 40, bold=True)

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Tạo các surface văn bản
text_surface_sys = sys_font.render("Hello, world !", True, BLACK)

# Tính toán vị trí để căn giữa `text_surface_sys` trên màn hình
text_rect_sys = text_surface_sys.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))

# Vòng lặp chính
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Vẽ màn hình
    screen.fill(WHITE)
    screen.blit(text_surface_sys, text_rect_sys.topleft)  # Hiển thị văn bản hệ thống ở giữa màn hình
    pygame.display.flip()

# Kết thúc Pygame
pygame.font.quit()
pygame.quit()
sys.exit()
