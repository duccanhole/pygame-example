import os
import pygame
from setting import BIRD_START_X, BIRD_START_Y, FLAP_STRENGTH, GRAVITY

ASSETS_FOLDER = os.path.join("flappy-bird")
BIRD_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join(ASSETS_FOLDER, "bluebird-midflap.png")))


# Define the Bird class
class Bird:
    def __init__(self):
        self.image = BIRD_IMAGE
        self.rect = self.image.get_rect(center=(BIRD_START_X, BIRD_START_Y))
        self.velocity = 0

    def flap(self):
        self.velocity = FLAP_STRENGTH

    def update(self):
        self.velocity += GRAVITY
        self.rect.y += int(self.velocity)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def reset(self):
        self.rect = self.image.get_rect(center=(BIRD_START_X, BIRD_START_Y))
        self.velocity = 0