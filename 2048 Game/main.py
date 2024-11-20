import pygame
import sys
import random

# Khởi tạo Pygame
pygame.init()

# Kích thước màn hình và thiết lập cơ bản
SIZE = 400  # Kích thước màn hình vuông
GRID_SIZE = 4  # Kích thước lưới 4x4
TILE_SIZE = SIZE // GRID_SIZE  # Kích thước mỗi ô vuông
PADDING = 10  # Khoảng cách giữa các ô

# Màu sắc
BACKGROUND_COLOR = (187, 173, 160)
EMPTY_TILE_COLOR = (205, 193, 180)
TILE_COLORS = {
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
}

# Khởi tạo màn hình
screen = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption("2048")

# Font cho ô số
font = pygame.font.Font(None, 36)

# Khởi tạo lưới game 4x4
grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]

# Hàm thêm số ngẫu nhiên (2 hoặc 4) vào ô trống
def add_random_tile():
    empty_tiles = [(r, c) for r in range(GRID_SIZE) for c in range(GRID_SIZE) if grid[r][c] == 0]
    if empty_tiles:
        r, c = random.choice(empty_tiles)
        grid[r][c] = 4 if random.random() < 0.1 else 2

# Hàm vẽ các ô và số
def draw_grid():
    screen.fill(BACKGROUND_COLOR)
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            value = grid[r][c]
            color = TILE_COLORS.get(value, EMPTY_TILE_COLOR)
            rect = pygame.Rect(c * TILE_SIZE + PADDING, r * TILE_SIZE + PADDING, TILE_SIZE - PADDING * 2, TILE_SIZE - PADDING * 2)
            pygame.draw.rect(screen, color, rect)
            if value != 0:
                text = font.render(str(value), True, (119, 110, 101))
                text_rect = text.get_rect(center=(c * TILE_SIZE + TILE_SIZE // 2, r * TILE_SIZE + TILE_SIZE // 2))
                screen.blit(text, text_rect)

# Hàm di chuyển và gộp các ô trong lưới
def move_left():
    moved = False
    for r in range(GRID_SIZE):
        new_row = [i for i in grid[r] if i != 0]
        for i in range(len(new_row) - 1):
            if new_row[i] == new_row[i + 1]:
                new_row[i] *= 2
                new_row[i + 1] = 0
        new_row = [i for i in new_row if i != 0]
        new_row += [0] * (GRID_SIZE - len(new_row))
        if new_row != grid[r]:
            moved = True
        grid[r] = new_row
    return moved

def rotate_grid():
    global grid
    grid = [list(row) for row in zip(*grid[::-1])]

def move(direction):
    moved = False
    for _ in range(direction):
        rotate_grid()
    if move_left():
        moved = True
    for _ in range(-direction % 4):
        rotate_grid()
    return moved

# Thêm hai ô ngẫu nhiên lúc bắt đầu
add_random_tile()
add_random_tile()

# Vòng lặp chính của trò chơi
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if move(0):
                    add_random_tile()
            elif event.key == pygame.K_DOWN:
                if move(1):
                    add_random_tile()
            elif event.key == pygame.K_RIGHT:
                if move(2):
                    add_random_tile()
            elif event.key == pygame.K_UP:
                if move(3):
                    add_random_tile()

    # Vẽ màn hình
    draw_grid()
    pygame.display.flip()

    # Kiểm tra xem trò chơi có kết thúc không
    if not any(0 in row for row in grid) and not any(
        grid[r][c] == grid[r + dr][c + dc]
        for r in range(GRID_SIZE)
        for c in range(GRID_SIZE)
        for dr, dc in [(1, 0), (0, 1)]
        if 0 <= r + dr < GRID_SIZE and 0 <= c + dc < GRID_SIZE
    ):
        print("Game Over!")
        pygame.quit()
        sys.exit()
