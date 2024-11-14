import pygame
import sys

# Khởi tạo Pygame
pygame.init()

# Thiết lập kích thước cửa sổ
screen = pygame.display.set_mode((500, 500))

# Tạo Clock để quản lý thời gian
clock = pygame.time.Clock()

# Lấy thời điểm ban đầu
start_time = pygame.time.get_ticks()

# Vòng lặp game
while True:
    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Cập nhật màn hình và nội dung
    screen.fill((0, 0, 0))  # Đổ màu nền đen

    # Lấy thời gian hiện tại và tính thời gian trôi qua
    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - start_time

    # Cứ mỗi 1000 mili giây (1 giây), thực hiện hành động
    if elapsed_time > 1000:
        print("1 giây đã trôi qua")
        start_time = current_time  # Cập nhật lại thời gian bắt đầu

    # Cập nhật màn hình
    pygame.display.flip()

    # Giới hạn tốc độ khung hình ở mức 30 FPS
    clock.tick(30)
