import os
import pygame
from pygame.locals import *
import random

pygame.init()

ASSETS_FOLDER = os.path.join("GameDuaXe", "images")

# Màu nền
gray = (100, 100, 100)
green = (76, 208, 56)
yellow = (255, 232, 0)
red = (200, 0, 0)
white = (255, 255, 255)

# Tạo của sổ game
width = 500
height = 500
screen_size = (width, height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Game dua xe")

# Khởi tạo biến
gameover = False
speed = 2
score = 0

# đường xe chạy
road_width = 300
street_width = 10
street_height = 50

# lane đường
lane_left = 150
land_center = 250
lane_right = 350
lanes = [lane_left, land_center, lane_right]
lane_move_y = 0


# Road và edge
road = (100, 0, road_width, height)
left_edge = (95, 0, street_width, height)
right_edge = (395, 0, street_width, height)

# Vị trí ban đầu của xe người chơi
player_x = 250
player_y = 400


# Đối tương xe chướng ngại vậy
class Vehicle(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        # Scale image
        image_scale = 45 / image.get_rect().width
        new_width = image.get_rect().width * image_scale
        new_height = image.get_rect().height * image_scale
        self.image = pygame.transform.scale(image, (new_width, new_height))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]


# Đối tượng xe player
class PlayerVehicle(Vehicle):
    def __init__(self, x, y):
        image = pygame.image.load(os.path.join(ASSETS_FOLDER, "car.png"))
        super().__init__(image, x, y)


# sprite group
player_group = pygame.sprite.Group()
Vehicle_group = pygame.sprite.Group()

# Tạo xe người chơi
player = PlayerVehicle(player_x, player_y)
player_group.add(player)

# Load xe chướng ngại mục
image_name = ["pickup_truck.png", "semi_trailer.png", "taxi.png", "van.png"]
Vehicle_images = []
for name in image_name:
    image = pygame.image.load(os.path.join(ASSETS_FOLDER, name))
    Vehicle_images.append(image)

# load hình va chạm
crash = pygame.image.load(os.path.join(ASSETS_FOLDER, "crash.png"))
crash_rect = crash.get_rect()

# cài đặt fps
clock = pygame.time.Clock()
fps = 120

# Vòng lặp xủa lý game
running = True
while running:
    # Chỉnh frame hình trên giây
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        # Điều khiển xe
        if event.type == KEYDOWN:
            if event.key == K_LEFT and player.rect.center[0] > lane_left:
                player.rect.x -= 100
            if event.key == K_RIGHT and player.rect.center[0] < lane_right:
                player.rect.x += 100

    # Kiểm tra va chạm khi xe đứng im
    # if pygame.sprite.spritecollide(player, Vehicle_group, True):
    #     gameover = True
    #     crash_rect.center = [player.rect.center[0], player.rect.top]

    # Vẽ địa hình cỏ
    screen.fill(green)

    # Vẽ road- đường chạy
    pygame.draw.rect(screen, gray, road)
    # Vẽ edge- biên/hành lang đường
    pygame.draw.rect(screen, yellow, left_edge)
    pygame.draw.rect(screen, yellow, right_edge)
    # Vẽ lane đường
    lane_move_y += speed * 2
    if lane_move_y >= street_height * 2:
        lane_move_y = 0
    for y in range(street_height * -2, height, street_height * 2):
        pygame.draw.rect(
            screen,
            white,
            (lane_left + 45, y + lane_move_y, street_width, street_height),
        )
        pygame.draw.rect(
            screen,
            white,
            (land_center + 45, y + lane_move_y, street_width, street_height),
        )

    # Vẽ xe layer
    player_group.draw(screen)

    # vẽ phương tiện giao thông/ chướng ngại vật
    if len(Vehicle_group) < 2:
        add_verhicle = True
        for verhicle in Vehicle_group:
            if verhicle.rect.top < verhicle.rect.height * 1.5:
                add_verhicle = False
        if add_verhicle:
            lane = random.choice(lanes)
            image = random.choice(Vehicle_images)
            verhicle = Vehicle(image, lane, height / -2)
            Vehicle_group.add(verhicle)

    # Cho xe công cộng chạy
    for vehicle in Vehicle_group:
        vehicle.rect.y += speed

        # Remove verhicle
        if vehicle.rect.top >= height:
            vehicle.kill()
            score += 1
            # Tăng tốc độ khó - xe chướng ngại vật chạy
            if score > 0 and score % 5 == 0:
                speed += 1

    # Vẽ nhóm xe lưu thông
    Vehicle_group.draw(screen)
    
    # Kiểm tra va chạm
    for verhicle in Vehicle_group:
        if pygame.sprite.collide_rect(player, verhicle):
            gameover = True
            crash_rect.center = [player.rect.center[0], player.rect.top]

    # Hiển thị điểm
    font = pygame.font.Font(pygame.font.get_default_font(), 16)
    text = font.render(f"Score: {score}", True, white)
    text_rect = text.get_rect()
    text_rect.center = (50, 40)
    screen.blit(text, text_rect)
    if gameover:
        screen.blit(crash, crash_rect)
        pygame.draw.rect(screen, red, (0, 50, width, 100))
        font = pygame.font.Font(pygame.font.get_default_font(), 16)
        text = font.render(f"Game Over! Play again?(Y/N)", True, white)
        text_rect = text.get_rect()
        text_rect.center = (width / 2, 100)
        screen.blit(text, text_rect)

    pygame.display.update()

    while gameover:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == QUIT:
                gameover = False
                running = False

            if event.type == KEYDOWN:
                if event.key == K_y:
                    # reset game
                    gameover = False
                    score = 0
                    speed = 2
                    Vehicle_group.empty()
                    player.rect.center = [player_x, player_y]
                elif event.key == K_n:
                    # exit game
                    gameover = False
                    running = False


pygame.quit()
