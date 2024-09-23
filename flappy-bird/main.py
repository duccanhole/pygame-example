import os
import sys
import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 400, 500
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Game constants
GRAVITY = 0.5
FLAP_STRENGTH = -7
PIPE_SPEED = 3
PIPE_GAP = 150
BIRD_START_X, BIRD_START_Y = 100, 300

ASSETS_FOLDER = os.path.join("flappy-bird")

# Load assets
BIRD_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join(ASSETS_FOLDER, "bluebird-midflap.png")))
PIPE_IMAGE = pygame.image.load(os.path.join(ASSETS_FOLDER, "pipe-green.png"))
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_FOLDER, "background-day.png")), (WIDTH, HEIGHT))

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

# Function to display Game Over message
def display_game_over(screen):
    font = pygame.font.Font(None, 35)
    text = font.render("Game Over", True, BLACK)
    subtext = font.render("Press Enter to play again", True, BLACK)

    # Get text rect and position it in the center of the screen
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    subtext_rect = subtext.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))

    # Blit the text to the screen
    screen.blit(text, text_rect)
    screen.blit(subtext, subtext_rect)

    # Update the display
    pygame.display.flip()

# Define the Pipe class
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

# Game loop
def game_loop():
    clock = pygame.time.Clock()
    bird = Bird()
    pipes = [Pipe(WIDTH + 100)]
    score = 0
    running = True
    isOver = False

    while running:
        clock.tick(30)
        SCREEN.fill(WHITE)
        SCREEN.blit(BACKGROUND, (0, 0))
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.flap()
                elif event.key == pygame.K_RETURN and isOver:
                    isOver = False
                    score = 0
                    bird.reset()
                    pipe.reset()

        if isOver: 
            display_game_over(SCREEN)
            continue
        # Update bird
        bird.update()

        # Update pipes
        for pipe in pipes:
            pipe.update()
            if pipe.offscreen():
                pipes.remove(pipe)
                pipes.append(Pipe(WIDTH + 100))
                score += 1
            if pipe.collide(bird):
                # running = False
                isOver = True
                
        # Draw everything
        bird.draw(SCREEN)
        for pipe in pipes:
            pipe.draw(SCREEN)

        # Check for collision with ground or ceiling
        if bird.rect.top <= 0 or bird.rect.bottom >= HEIGHT:
            # running = False
            isOver = True

        # Display the score
        font = pygame.font.Font(None, 36)
        text = font.render(f"Score: {score}", True, BLACK)
        SCREEN.blit(text, (10, 10))

        # Update the display
        pygame.display.flip()
    display_game_over(SCREEN)
    pygame.quit()

if __name__ == "__main__":
    game_loop()
