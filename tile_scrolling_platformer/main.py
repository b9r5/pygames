import pygame
from constants import display, tile_size
from grid import Grid

pygame.init()
screen = pygame.display.set_mode(display)
clock = pygame.time.Clock()
running = True

grid = Grid()
camera = pygame.Vector2(0, 0)
dt = 0  # delta time in seconds since last frame

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if running:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            camera.y -= 64 * dt
        if keys[pygame.K_s]:
            camera.y += 64 * dt
        if keys[pygame.K_a]:
            camera.x -= 64 * dt
        if keys[pygame.K_d]:
            camera.x += 64 * dt

        if camera.x < 0:
            camera.x = 0
        if camera.y < 0:
            camera.y = 0
        # TODO clamp camera to be within right and bottom limits

        screen.fill("white")

        grid.draw(screen, camera)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

pygame.quit()