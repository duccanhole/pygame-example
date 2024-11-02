import time
import pygame
from setting import WIDTH, HEIGHT, FONT_SIZE, BLACK, BROWN, HOOK_LENGTH
from cart import Cart
from item import Item

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gold mining Game")

# Clock for controlling the frame rate
clock = pygame.time.Clock()


score = 0
target = 100


# Function to render the score at the top left of the screen
def show_score(screen: pygame.Surface, score: int, target: int):
    font = pygame.font.Font(None, 24)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    target_text = font.render(f"Target: {target}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    screen.blit(target_text, (10, 25))


# Function to render the countdown timer at the top right of the screen
def show_time(screen: pygame.Surface, start_time):
    # Calculate remaining time
    current_time = time.time()
    elapsed_time = int(current_time - start_time)
    countdown_time = max(0, 60 - elapsed_time)  # Example: 60-second timer

    # Render the timer text
    font = pygame.font.Font(None, FONT_SIZE)
    time_text = font.render(f"Time: {countdown_time}", True, BLACK)
    screen.blit(time_text, (WIDTH - 70, 10))

    return countdown_time


def check_collide_screen(cart: Cart):
    (x, y) = cart.get_hook_pos()
    return x >= WIDTH or x <= 0 or y >= HEIGHT or y <= 0


# Function to display Game Over message
def display_game_over(screen: pygame.Surface, level: int):
    font = pygame.font.Font(None, 35)
    text = font.render(f"Mission not completed! Your level is {level+1}", True, BLACK)
    subtext = font.render("Press Enter to play again", True, BLACK)

    # Get text rect and position it in the center of the screen
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    subtext_rect = subtext.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))

    # Blit the text to the screen
    screen.blit(text, text_rect)
    screen.blit(subtext, subtext_rect)

    # Update the display
    pygame.display.flip()


# Function to display message
def display_misson_completed(screen: pygame.Surface, level: int):
    font = pygame.font.Font(None, 35)
    text = font.render("Mission completed!", True, BLACK)
    subtext = font.render(f"Press Enter to play level {level+1}", True, BLACK)

    # Get text rect and position it in the center of the screen
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    subtext_rect = subtext.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))

    # Blit the text to the screen
    screen.blit(text, text_rect)
    screen.blit(subtext, subtext_rect)

    # Update the display
    pygame.display.flip()


# Main game loop
running = True
is_over = False
is_completed = False
level = 0
start_time = time.time()
cart = Cart()

items: list[Item] = []
for i in range(10):
    item = Item()
    items.append(item)

while running:
    screen.fill(BROWN)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                cart.hook_extending = True
            elif event.key == pygame.K_RETURN:
                if is_over:
                    level = 0
                    score = 0
                    cart.reset_hook()
                    for i in items:
                        i.reset()
                    is_over = False
                    is_completed = False
                    start_time = time.time()
                elif is_completed:
                    cart.reset_hook()
                    for i in items:
                        i.reset()
                    is_over = False
                    is_completed = False
                    start_time = time.time()

    if is_over:
        display_game_over(screen, level)
        continue

    if is_completed:
        display_misson_completed(screen, level)
        continue

    target = int(100 * (1 + 0.5) ** level)
    show_score(screen, score, target)
    remain_time = show_time(screen, start_time)

    cart.draw(screen)
    cart.update_hook(screen)

    for item in items:
        item.draw(screen)
        if item.check_collide_point(cart.get_hook_pos()):
            item.is_hodling = True
            cart.hook_extending = False
            cart.hook_speed = (50 / item.type["weight"]) * 5
        if item.is_hodling:
            if cart.hook_length <= HOOK_LENGTH:
                score = score + item.type["value"]
                cart.reset_hook()
                item.reset()
            else:
                (x, y) = cart.get_hook_pos()
                item.update(x, y)

    if check_collide_screen(cart):
        cart.hook_extending = False

    if remain_time <= 0:
        if score < target:
            is_over = True
        else:
            is_completed = True
            level = level + 1

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
