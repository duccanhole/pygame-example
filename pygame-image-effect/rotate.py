import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rotate and Reverse Animation Example")

# Colors
BACKGROUND_COLOR = (50, 150, 200)
SQUARE_COLOR = (255, 100, 100)

# Square settings
square_size = 100
square_surface = pygame.Surface((square_size, square_size), pygame.SRCALPHA)
pygame.draw.rect(square_surface, SQUARE_COLOR, (0, 0, square_size, square_size))

# Rotation settings
angle = 0  # Starting angle
rotation_speed = 2  # Degrees to rotate per frame
direction = 1  # 1 for clockwise, -1 for counterclockwise

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Update the angle for rotation
    angle += rotation_speed * direction

    # Check if the square has completed a full 360-degree rotation
    if angle >= 360 or angle <= -360:
        angle = 0  # Reset angle to zero
        direction *= -1  # Reverse the direction

    # Rotate the square
    rotated_square = pygame.transform.rotate(square_surface, angle)
    rotated_rect = rotated_square.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    # Draw the rotated square at the center of the screen
    screen.blit(rotated_square, rotated_rect.topleft)

    # Update the display
    pygame.display.flip()
    pygame.time.Clock().tick(60)  # Limit the frame rate to 60 FPS

# Quit Pygame
pygame.quit()
sys.exit()
