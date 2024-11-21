# Explain
### Init
- Khởi tạo danh sách xe chướng ngại vật
```python
# Load xe chướng ngại mục
image_name = ["pickup_truck.png", "semi_trailer.png", "taxi.png", "van.png"]
Vehicle_images = []
for name in image_name:
    image = pygame.image.load(os.path.join(ASSETS_FOLDER, name))
    Vehicle_images.append(image)
```
### Game loop
- Lắng nghe sự kiện từ bàn phím để di chuyển xe của người chơi sang trái hoặc sang phải.
- Vẽ đường đua xe của người chơi.
- Kiểm tra số lượng xe chướng ngại vật hiện tại, nếu số lượng ít hơn 2, thì vẽ thêm xe.
```python
# vẽ phương tiện giao thông/ chướng ngại vật
if len(Vehicle_group) < 2:
    add_verhicle = True
    for verhicle in Vehicle_group:
        if verhicle.rect.top < verhicle.rect.height * 1.5:
            add_verhicle = False
    if add_verhicle:
        lane = random.choice(lanes)
        image = random.choice(Vehicle_images)
        verhicle = Vehicle(image, lane, height / -2)
        Vehicle_group.add(verhicle)
```
- Cho xe chướng ngại vật chạy, nếu xe biến mất khỏi màn hình thì xóa xe đó đi và tăng điểm của người chơi.
- Tăng dần tốc độ khi điểm của người chơi tăng lên.
```python
# Cho xe công cộng chạy
for vehicle in Vehicle_group:
    vehicle.rect.y += speed

    # Remove verhicle
    if vehicle.rect.top >= height:
        vehicle.kill()
        score += 1
        # Tăng tốc độ khó - xe chướng ngại vật chạy
        if score > 0 and score % 5 == 0:
            speed += 1
```
- Kiểm tra xem xe của người chơi có va chạm với xe chướng ngại vật hay không.
```python
# Kiểm tra va chạm
for verhicle in Vehicle_group:
    if pygame.sprite.collide_rect(player, verhicle):
        gameover = True
        crash_rect.center = [player.rect.center[0], player.rect.top]
```
- Kiểm tra xem trò chơi đã kết thúc hay chưa, nếu kết thúc thì dừng trò chơi và hiển thị màn hình khởi động lại.
```python
while gameover:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == QUIT:
            gameover = False
            running = False

        if event.type == KEYDOWN:
            if event.key == K_y:
                # reset game
                gameover = False
                score = 0
                speed = 2
                Vehicle_group.empty()
                player.rect.center = [player_x, player_y]
            elif event.key == K_n:
                # exit game
                gameover = False
                running = False
```