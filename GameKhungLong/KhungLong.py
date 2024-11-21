import os
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption("Dinosaur")
WHITE = (255, 255, 255)
background_x = 0
background_y = 0
dinosaur_x = 0
dinosaur_y = 230
tree_x = 550
tree_y = 230
x_velocity = 5
y_velocity = 7
score = 0
RED = (255, 0, 0)
jump = False
game_over = False
font = pygame.font.SysFont("san", 20)
font1 = pygame.font.SysFont("san", 40)
ASSETS_FOLDER = os.path.join("GameKhungLong")
background = pygame.image.load(os.path.join(ASSETS_FOLDER, "background.jpg"))
dinosaur = pygame.image.load(os.path.join(ASSETS_FOLDER, "dinosaur.png"))
tree = pygame.image.load(os.path.join(ASSETS_FOLDER, "tree.png"))
sound1 = pygame.mixer.Sound(os.path.join(ASSETS_FOLDER, "tick.wav"))
sound2 = pygame.mixer.Sound(os.path.join(ASSETS_FOLDER, "te.wav"))
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)
    screen.fill(WHITE)
    background1_rect = screen.blit(background, (background_x, background_y))
    background2_rect = screen.blit(background, (background_x + 600, background_y))
    dinosaur_rect = screen.blit(dinosaur, (dinosaur_x, dinosaur_y))
    score_txt = font.render("Score:" + str(score), True, RED)
    screen.blit(score_txt, (5, 5))
    tree_rect = screen.blit(tree, (tree_x, tree_y))
    background_x -= x_velocity
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
    if game_over:
        gameover_txt = font1.render("GAME OVER", True, RED)
        gameover_txt2 = font1.render("PRESS SPACE TWICE TO PLAY AGAIN", True, RED)
        screen.blit(gameover_txt, (0, 130))
        screen.blit(gameover_txt2, (0, 160))
        x_velocity = 0
        y_velocity = 0
        pygame.display.flip()
        continue
    if 230 >= dinosaur_y >= 80:
        if jump == True:
            dinosaur_y -= y_velocity
    else:
        jump = False
    if dinosaur_y < 230:
        if jump == False:
            dinosaur_y += y_velocity
    if background_x + 600 <= 0:
        background_x = 0
    tree_x -= x_velocity
    if tree_x <= -20:
        tree_x = 550
        score += 1
    if dinosaur_rect.colliderect(tree_rect):
        game_over = True
        pygame.mixer.Sound.play(sound2)
        # gameover_txt = font1.render("GAME OVER", True, RED)
        # screen.blit(gameover_txt, (200, 150))
        # x_velocity = 0
        # y_velocity = 0

    pygame.display.flip()
pygame.quit()
