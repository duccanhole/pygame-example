 if event.key == pygame.K_LEFT:
                if move(0):
                    add_random_tile()
            elif event.key == pygame.K_UP:
                if move(1):
                    add_random_tile()
            elif event.key == pygame.K_RIGHT:
                if move(2):
                    add_random_tile()
            elif event.key == pygame.K_DOWN:
                if move(3):
                    add_random_tile()