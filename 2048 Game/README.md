# Explain
### Function
- `add_random_tile`: Hàm chọn ô trống và gán giá trị ngẫu nhiên giữa 2 hoặc 4.
- `draw_grid`: Hàm vẽ giá trị của lưới (grid) lên màn hình.
- `move`:
    - Xoay lưới sao cho hướng di chuyển luôn về bên trái.
    - Thực hiện gộp các ô về bên trái thông qua hàm `move_left`
    - Xoay lưới lại về vị trí ban đầu.
    - Kiểm tra xem lưới có thay đổi giá trị không. Nếu có, trả về  True, ngược lại trả về False.
### Game loop
- Lắng nghe sự kiện và di chuyển lưới. Nếu lưới thay đổi giá trị, thêm ngẫu nhiên giá trị vào ô trống.
- Vẽ lưới lên màn hình.
- Hàm kiểm tra game over bao gồm 2 điều kiện sau:
    - Không còn ô trống (giá trị 0) trong lưới.
    -  Không có ô nào có thể gộp với ô lân cận.
```python
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
```
- Nếu game over, dừng vòng lặp và thoát trò chơi.