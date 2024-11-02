import os
import random
import pygame
from setting import WIDTH, HEIGHT

ASSETS_FOLDER = os.path.join("gold-mining")

types = [
    {
        "type": "wooden_crate",
        "value": 10,
        "weight": 50,
        "size": 75,
        "path": os.path.join(ASSETS_FOLDER, "wooden_crate.png"),
    },
    {
        "type": "coin",
        "value": 20,
        "weight": 25,
        "size": 45,
        "path": os.path.join(ASSETS_FOLDER, "coin.png"),
    },
    {
        "type": "crystal_2",
        "value": 30,
        "weight": 10,
        "size": 25,
        "path": os.path.join(ASSETS_FOLDER, "crystal_2.png"),
    },
    {
        "type": "crystal_3",
        "value": 45,
        "weight": 15,
        "size": 25,
        "path": os.path.join(ASSETS_FOLDER, "crystal_3.png"),
    },
    {
        "type": "diamond",
        "value": 60,
        "weight": 10,
        "size": 45,
        "path": os.path.join(ASSETS_FOLDER, "diamond.png"),
    },
    {
        "type": "fish_bone",
        "value": 1,
        "weight": 15,
        "size": 35,
        "path": os.path.join(ASSETS_FOLDER, "fish_bone.png"),
    },
    {
        "type": "gold",
        "value": 50,
        "weight": 15,
        "size": 25,
        "path": os.path.join(ASSETS_FOLDER, "gold.png"),
    },
]
rate = [4, 3, 2, 2, 1, 5, 2]


class Item:
    def __init__(self):
        # Generate random x and y coordinates within the specified range
        self.x = random.randint(
            10, WIDTH - 10
        )  # Ensure the square fits within the range
        self.y = random.randint(
            60, HEIGHT - 10
        )  # Ensure the square fits within the range
        self.is_hodling = False
        self.type = random.choices(types, weights=rate, k=1)[0]
        self.image = pygame.image.load(self.type["path"])

    def reset(self):
        self.x = random.randint(
            10, WIDTH - 10
        )  # Ensure the square fits within the range
        self.y = random.randint(
            60, HEIGHT - 10
        )  # Ensure the square fits within the range
        self.is_hodling = False
        self.type = random.choices(types, weights=rate, k=1)[0]
        self.image = pygame.image.load(self.type["path"])

    def update(self, x: int, y: int):
        self.x = x
        self.y = y

    def draw(self, screen: pygame.Surface):
        # Resize the image to custom size
        resized_image = pygame.transform.scale(
            self.image, (self.type["size"], self.type["size"])
        )
        screen.blit(resized_image, (self.x, self.y))

    def check_collide_point(self, point: tuple):
        shape_rect = pygame.Rect(self.x, self.y, self.type["size"], self.type["size"])
        return shape_rect.collidepoint(point)
