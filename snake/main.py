import random
import pygame
from setting import WIDTH, HEIGHT, SNAKE_BLOCK, SNAKE_SPEED, COLOR_GREEN, COLOR_BLACK, COLOR_RED, COLOR_WHITE
pygame.init()

# set the window size
window = pygame.display.set_mode((WIDTH, HEIGHT))

# set title 
pygame.display.set_caption("Snake game")

# set clock speed for fps
clock = pygame.time.Clock()

# function to draw body of snake
def draw_snake(snake_block: int, snake_list: list): 
    for block in snake_list: 
        pygame.draw.rect(window, COLOR_GREEN, [block[0], block[1], snake_block, snake_block])
# funtion to draw food
def draw_food(food_x: int, food_y: int):
    pygame.draw.rect(window, COLOR_RED, [food_x, food_y, SNAKE_BLOCK, SNAKE_BLOCK])
    
# Function to display Game Over message
def display_game_over(score: int = 0):
    font = pygame.font.Font(None, 35)
    text = font.render(f"Game Over! Your score: {score}", True, COLOR_RED)
    subtext = font.render("Press Enter to play again", True, COLOR_WHITE)

    # Get text rect and position it in the center of the screen
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    subtext_rect = subtext.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))

    # Blit the text to the screen
    window.blit(text, text_rect)
    window.blit(subtext, subtext_rect)

    # Update the display
    pygame.display.flip()
    
def game_loop():
    running = True
    # start position of snake
    x = WIDTH // 2
    y = HEIGHT // 2
    # Set the initial movement direction
    x_change = 0
    y_change = 0
    # Variables to keep track of current and previous direction
    last_direction = None  # Will store the last direction to prevent reversal
    # Set the initial position of food
    food_x = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / SNAKE_BLOCK) * SNAKE_BLOCK
    food_y = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / SNAKE_BLOCK) * SNAKE_BLOCK
    snake_list = []
    snake_length = 10
        
    is_over = False
    while running:         
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # Check for arrow key presses to control the snake's movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and last_direction != "right":
                x_change = -SNAKE_BLOCK
                y_change = 0
                last_direction = "left"
            elif event.key == pygame.K_RIGHT and last_direction != "left":
                x_change = SNAKE_BLOCK
                y_change = 0
                last_direction = "right"
            elif event.key == pygame.K_UP and last_direction != "down":
                y_change = -SNAKE_BLOCK
                x_change = 0
                last_direction = "up"
            elif event.key == pygame.K_DOWN and last_direction != "up":
                y_change = SNAKE_BLOCK
                x_change = 0
                last_direction = "down"
            elif event.key == pygame.K_RETURN and is_over:
                # Reset game
                is_over = False
                x = WIDTH // 2
                y = HEIGHT // 2
                x_change = 0
                y_change = 0
                snake_length = 1
                snake_list = []
        
        if is_over: 
            display_game_over(snake_length)
            continue
                
        x+=x_change
        y+=y_change
        
        if x > WIDTH:
            x = 0
        if x < 0:
            x = WIDTH
        if y > HEIGHT:
            y = 0
        if y < 0:
            y = HEIGHT
        
        window.fill(COLOR_BLACK)
        
        snake_head = [x, y]
        snake_list.append(snake_head) 
        
        if len(snake_list) > snake_length: 
            del snake_list[0]
    
        if x == food_x and y == food_y: 
            food_x = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / SNAKE_BLOCK) * SNAKE_BLOCK
            food_y = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / SNAKE_BLOCK) * SNAKE_BLOCK
            snake_length += 1
        
        # Check if the snake has collided with itself
        for segment in snake_list[:-1]:
            if segment == snake_head:
                is_over = True
        
        draw_food(food_x, food_y)
        
        draw_snake(SNAKE_BLOCK, snake_list)
        
        clock.tick(SNAKE_SPEED)
        pygame.display.update()
    pygame.quit()
    
game_loop()