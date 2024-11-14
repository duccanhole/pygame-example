import pygame
import sys

# Khởi tạo Pygame
pygame.init()

# Thiết lập kích thước cửa sổ
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

# Lớp nhân vật chính
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 128, 255))
        self.rect = self.image.get_rect(center=(250, 400))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: self.rect.x -= 5
        if keys[pygame.K_RIGHT]: self.rect.x += 5
        if keys[pygame.K_UP]: self.rect.y -= 5
        if keys[pygame.K_DOWN]: self.rect.y += 5

# Lớp kẻ thù
class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=pos)

# Tạo các nhóm sprite
player = Player()
enemies = pygame.sprite.Group()

# Tạo một số kẻ thù và thêm vào nhóm
for i in range(5):
    enemy = Enemy((100 * i + 50, 100))
    enemies.add(enemy)

all_sprites = pygame.sprite.Group(player, *enemies)

# Vòng lặp game
while True:
    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Cập nhật tất cả các sprite
    all_sprites.update()
    
    # Kiểm tra va chạm giữa player và enemies
    hits = pygame.sprite.spritecollide(player, enemies, dokill=True)
    if hits:
        print("Va chạm! Kẻ thù bị tiêu diệt.")
    
    # Vẽ màn hình
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    pygame.display.flip()
    
    clock.tick(30)
