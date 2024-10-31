import os
import pygame
import numpy as np
from PIL import Image, ImageFilter

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Blur Effect Example')

# Load the image with Pillow, apply blur, and convert to Pygame surface
def load_and_blur_image(image_path, blur_radius):
    """Load an image, apply a blur effect, and return it as a Pygame surface."""
    # Open the image using Pillow
    pil_image = Image.open(image_path)
    # Convert image to RGB (if not already in RGB mode)
    if pil_image.mode != 'RGB':
        pil_image = pil_image.convert('RGB')
        
    # Apply Gaussian blur
    blurred_image = pil_image.filter(ImageFilter.GaussianBlur(blur_radius))
    
    # Convert the Pillow image to a format that Pygame can use
    return pygame.image.fromstring(blurred_image.tobytes(), blurred_image.size, 'RGB')

# Load and blur the image
# Load an image (ensure you have an image file in the same directory)
assets_folder = os.path.join("pygame-animation")
image_path = os.path.join(assets_folder, 'image-blur-test.jpg')
blur_radius = 15  # Adjust the blur radius as needed
blurred_image_surface = load_and_blur_image(image_path, blur_radius)

# Main loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))
    
    # Draw the blurred image
    screen.blit(blurred_image_surface, (0, 0))  # Position the blurred image

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()