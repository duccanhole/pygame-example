import math
import pygame
from setting import CART_LENGTH, CART_WIDTH, HOOK_LENGTH, ANGLE_SPEED, WIDTH, BLACK


class Cart:
    def __init__(self):
        self.width = CART_WIDTH
        self.length = CART_LENGTH
        self.hook_length = HOOK_LENGTH
        self.hook_angle = 90
        self.angle_speed = ANGLE_SPEED
        self.rotate_direction = 1
        self.x = WIDTH // 2 
        self.y = 15
        self.hook_extending = False
        self.hook_x = self.x
        self.hook_y = self.y
        self.hook_speed = 10

    def draw(self, screen: pygame.Surface):
        # pygame.draw.rect(screen, BLACK, (self.x, self.y, CART_WIDTH, CART_LENGTH))
        pygame.draw.circle(screen, BLACK, (self.x, self.y), 10)
        # Make a divider
        pygame.draw.line(screen, BLACK, (0, 45), (WIDTH, 45), 1)

    def draw_hook(self, screen: pygame.Surface):
        # Calculate hook position based on the current angle
        radians = math.radians(self.hook_angle)
        self.hook_x = self.x + self.hook_length * math.cos(radians)
        self.hook_y = self.y + self.hook_length * math.sin(radians)
        # Draw the hook line
        pygame.draw.line(
            screen,
            BLACK,
            (self.x, self.y),
            (self.hook_x, self.hook_y),
            3,
        )
    
    def update_hook(self, screen: pygame.Surface):
        if self.hook_extending:
            self.hook_length += self.hook_speed
            self.draw_hook(screen)
        else: 
            if self.hook_length > HOOK_LENGTH:
                self.hook_length -= self.hook_speed
            self.draw_hook(screen)
            if self.hook_length == HOOK_LENGTH:
                # Rotate the hook from 10 degrees to 170 degrees and back
                self.hook_angle += ANGLE_SPEED * self.rotate_direction
                if self.hook_angle >= 170 or self.hook_angle <= 10:
                    self.rotate_direction *= -1  # Reverse direction when limits are reached
    
    def get_hook_pos(self):
        return (self.hook_x, self.hook_y)
    
    def reset_hook(self):
        self.hook_x = self.x
        self.hook_y = self.y
        self.hook_extending = False
        self.hook_length = HOOK_LENGTH
        self.hook_angle = 90
        self.angle_speed = ANGLE_SPEED
        self.rotate_direction = 1
        self.hook_speed = 10