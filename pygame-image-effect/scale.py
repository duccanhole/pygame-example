import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Scale Animation Example")

# Colors
BACKGROUND_COLOR = (30, 30, 30)
SQUARE_COLOR = (0, 150, 250)

# Square settings
original_square_size = 100  # The original size of the square
max_scale = 1.5  # Maximum scale factor
min_scale = 0.5  # Minimum scale factor
scale_speed = 0.01  # Scale speed per frame
current_scale = 1  # Starting scale factor
scaling_up = True  # Flag to control the scaling direction

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Update scale factor
    if scaling_up:
        current_scale += scale_speed
        if current_scale >= max_scale:
            scaling_up = False
    else:
        current_scale -= scale_speed
        if current_scale <= min_scale:
            scaling_up = True

    # Calculate new size based on the scale factor
    new_size = int(original_square_size * current_scale)
    square_surface = pygame.Surface((new_size, new_size), pygame.SRCALPHA)
    pygame.draw.rect(square_surface, SQUARE_COLOR, (0, 0, new_size, new_size))

    # Center the square on the screen
    rect = square_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(square_surface, rect.topleft)

    # Update the display
    pygame.display.flip()
    pygame.time.Clock().tick(60)  # Limit the frame rate to 60 FPS

# Quit Pygame
pygame.quit()
sys.exit()
