# Define the Pipe class
import os
import random

import pygame
from setting import HEIGHT, WIDTH, PIPE_GAP, PIPE_SPEED

ASSETS_FOLDER = os.path.join("flappy-bird")
PIPE_IMAGE = pygame.image.load(os.path.join(ASSETS_FOLDER, "pipe-green.png"))

class Pipe:
    def __init__(self, x):
        self.height = random.randint(50, HEIGHT - PIPE_GAP - 50)
        self.top_image = pygame.transform.flip(PIPE_IMAGE, False, True)
        self.bottom_image = PIPE_IMAGE
        self.top_rect = self.top_image.get_rect(midbottom=(x, self.height))
        self.bottom_rect = self.bottom_image.get_rect(midtop=(x, self.height + PIPE_GAP))

    def update(self):
        self.top_rect.x -= PIPE_SPEED
        self.bottom_rect.x -= PIPE_SPEED

    def draw(self, screen: pygame.Surface):
        screen.blit(self.top_image, self.top_rect)
        screen.blit(self.bottom_image, self.bottom_rect)

    def offscreen(self):
        return self.top_rect.x < -50

    def collide(self, bird):
        return self.top_rect.colliderect(bird.rect) or self.bottom_rect.colliderect(bird.rect)
    
    def reset(self):
        self.height = random.randint(50, HEIGHT - PIPE_GAP - 50)
        self.top_rect = self.top_image.get_rect(midbottom=(WIDTH + 100, self.height))
        self.bottom_rect = self.bottom_image.get_rect(midtop=(WIDTH + 100, self.height + PIPE_GAP))