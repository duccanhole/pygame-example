import os
import pygame
from bird import Bird
from pipe import Pipe
from setting import WIDTH, HEIGHT

# Initialize Pygame
pygame.init()

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

ASSETS_FOLDER = os.path.join("flappy-bird")

BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_FOLDER, "background-day.png")), (WIDTH, HEIGHT))


# Function to display Game Over message
def display_game_over(screen: pygame.Surface):
    font = pygame.font.Font(None, 35)
    text = font.render("Game Over!", True, BLACK)
    subtext = font.render("Press Enter to play again", True, BLACK)

    # Get text rect and position it in the center of the screen
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    subtext_rect = subtext.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))

    # Blit the text to the screen
    screen.blit(text, text_rect)
    screen.blit(subtext, subtext_rect)

    # Update the display
    pygame.display.flip()

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
    pygame.quit()

if __name__ == "__main__":
    game_loop()
