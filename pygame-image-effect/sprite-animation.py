import os
import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Animation Example")
assets_folder = os.path.join("pygame-animation")
# Load the sprite sheet
sprite_sheet = pygame.image.load(os.path.join(assets_folder, "DinoSprites-tard.png")).convert_alpha()

# Sprite frame settings
FRAME_WIDTH = 24
FRAME_HEIGHT = 24
NUM_FRAMES = 24

# Extract frames from the sprite sheet for both idle and movement animations
idle_frame = sprite_sheet.subsurface((0, 0, FRAME_WIDTH, FRAME_HEIGHT))  # Frame 1 (idle)
movement_frames = [sprite_sheet.subsurface((i * FRAME_WIDTH, 0, FRAME_WIDTH, FRAME_HEIGHT)) for i in range(18, 24)]

# Extract each frame from the sprite sheet
frames = []
for i in range(NUM_FRAMES):
    frame = sprite_sheet.subsurface((i * FRAME_WIDTH, 0, FRAME_WIDTH, FRAME_HEIGHT))
    frames.append(frame)

# Animation settings
frame_index = 0
frame_delay = 5  # Delay between frames to control the animation speed
frame_counter = 0
x_pos = WIDTH // 2 - FRAME_WIDTH // 2
y_pos = HEIGHT // 2 - FRAME_HEIGHT // 2
speed = 5
moving_left = False
moving_right = False
facing_left = False
# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving_left = True
                facing_left = True
            elif event.key == pygame.K_RIGHT:
                moving_right = True
                facing_left = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            elif event.key == pygame.K_RIGHT:
                moving_right = False

    # Clear the screen
    screen.fill((255, 255, 255))
    
    # Update the position based on movement flags
    if moving_left:
        x_pos -= speed
    if moving_right:
        x_pos += speed

    # Update the animation frame only when moving
    if moving_left or moving_right:
        frame_counter += 1
        if frame_counter >= frame_delay:
            frame_counter = 0
            frame_index = (frame_index + 1) % len(movement_frames)  # Loop through movement frames
        current_frame = movement_frames[frame_index]
    else:
        # Use the idle frame when not moving
        frame_index = 0
        current_frame = idle_frame

    if facing_left: 
        current_frame = pygame.transform.flip(current_frame, True, False)

    # Draw the current frame on the screen
    screen.blit(current_frame, (x_pos, y_pos))

    # Update the display
    pygame.display.flip()
    pygame.time.Clock().tick(30)

# Quit Pygame
pygame.quit()
sys.exit()
