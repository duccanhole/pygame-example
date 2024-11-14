import pygame
import sys

# Khởi tạo Pygame
pygame.init()

# Thiết lập kích thước cửa sổ
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

# Tạo một lớp nhân vật chính kế thừa từ pygame.sprite.Sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))  # Tạo bề mặt hình vuông cho nhân vật
        self.image.fill((0, 128, 255))  # Đổ màu xanh cho nhân vật
        self.rect = self.image.get_rect(center=(250, 250))  # Vị trí ban đầu
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: self.rect.x -= 5
        if keys[pygame.K_RIGHT]: self.rect.x += 5
        if keys[pygame.K_UP]: self.rect.y -= 5
        if keys[pygame.K_DOWN]: self.rect.y += 5

# Tạo một lớp kẻ thù kế thừa từ pygame.sprite.Sprite
class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((30, 30))  # Tạo bề mặt hình vuông nhỏ hơn cho kẻ thù
        self.image.fill((255, 0, 0))  # Đổ màu đỏ cho kẻ thù
        self.rect = self.image.get_rect(center=pos)

# Tạo nhân vật chính và nhóm sprite cho kẻ thù
player = Player()
enemies = pygame.sprite.Group()

# Thêm một số kẻ thù vào nhóm
for i in range(5):
    enemy = Enemy((100 * i + 50, 100))
    enemies.add(enemy)

# Tạo nhóm tổng hợp chứa tất cả các sprite
all_sprites = pygame.sprite.Group(player, *enemies)

# Vòng lặp game
while True:
    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Cập nhật sprite
    all_sprites.update()
    
    # Kiểm tra va chạm giữa player và các kẻ thù
    if pygame.sprite.spritecollide(player, enemies, dokill=True):
        print("Va chạm! Kẻ thù bị tiêu diệt")

    # Vẽ màn hình
    screen.fill((255, 255, 255))  # Đổ màu nền trắng
    all_sprites.draw(screen)  # Vẽ tất cả sprite lên màn hình

    pygame.display.flip()
    clock.tick(30)  # Giới hạn tốc độ khung hình
