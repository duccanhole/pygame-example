import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fade In and Fade Out Example")

# Colors
BACKGROUND_COLOR = (50, 150, 200)
FADE_COLOR = (0, 0, 0)  # Black for fade effect

# Fade settings
fade_alpha = 255  # Starting transparency for fade-out effect
fade_speed = 5  # Controls how fast the fade occurs
fading_in = True  # Start with fade-in effect

# Create a surface for the fade effect
fade_surface = pygame.Surface((WIDTH, HEIGHT))
fade_surface.fill(FADE_COLOR)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen with background color
    screen.fill(BACKGROUND_COLOR)

    # Apply the fade effect
    if fading_in:
        fade_alpha -= fade_speed  # Decrease alpha for fade-in
        if fade_alpha <= 0:
            fade_alpha = 0  # End of fade-in
            fading_in = False  # Switch to fade-out after fade-in completes
    else:
        fade_alpha += fade_speed  # Increase alpha for fade-out
        if fade_alpha >= 255:
            fade_alpha = 255  # End of fade-out
            fading_in = True  # Restart fade-in after fade-out completes

    # Apply the fade effect to the overlay surface and draw it
    fade_surface.set_alpha(fade_alpha)
    screen.blit(fade_surface, (0, 0))

    # Update the display
    pygame.display.flip()
    pygame.time.Clock().tick(30)

# Quit Pygame
pygame.quit()
sys.exit()
