# Explain
### Function
- Logic kiem tra game win:
    - Kiem tra hang ngang, doc, cheo co the tao duoc 1 duong thang thi user win
```python
def check_win(player):
    # Vertical win check
    for col in range(COLS):
        if board[0][col] == board[1][col] == board[2][col] == player:
            draw_vertical_winning_line(col, player)
            return True

    # Horizontal win check
    for row in range(ROWS):
        if board[row][0] == board[row][1] == board[row][2] == player:
            draw_horizontal_winning_line(row, player)
            return True

    # Ascending diagonal win check
    if board[2][0] == board[1][1] == board[0][2] == player:
        draw_asc_diagonal(player)
        return True

    # Descending diagonal win check
    if board[0][0] == board[1][1] == board[2][2] == player:
        draw_desc_diagonal(player)
        return True

    return False
```
### Game loop:
- Lang nghe su kien tu chuot
- Neu o ma chuot click chua duoc to thi to o do 
- Kiem tra co nguoi choi nao win khong