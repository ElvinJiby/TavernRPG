import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Tavern RPG')
clock = pygame.time.Clock()
game_running = True

ground_pos = screen.get_height() - 92
player_pos = pygame.Vector2(screen.get_width() / 2, ground_pos) # Default player position
dt = 0 # Delta time
walk_speed = 300
run_speed = 500
acceleration = 50
is_running = False

# Game Loop
while game_running:
    # Close window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    # Render game
    screen.fill("purple")
    pygame.draw.line(screen, "black", (0,screen.get_height() - 50), (screen.get_width(), screen.get_height() - 50), 5)
    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        if player_pos.y == ground_pos:
            player_pos.y -= 300 * dt
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        if player_pos.y >= ground_pos:
            player_pos.y = ground_pos
        else:
            player_pos.y += 300 * dt
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player_pos.x += 300 * dt

    if player_pos.y > ground_pos:
        player_pos.y -= 30 * dt

    pygame.display.flip()
    dt = clock.tick(60) / 1000 # Limits FPS to 60 & gets delta time

pygame.quit()