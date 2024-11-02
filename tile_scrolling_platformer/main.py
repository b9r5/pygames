import pygame
from constants import display
from selector import Selector
from grid import Grid

pygame.init()
screen = pygame.display.set_mode(display)
clock = pygame.time.Clock()
running = True

grid = Grid()
selector = Selector()
edit_mode = False
selector_mode = False
camera = pygame.Vector2(0, 0)
dt = 0  # delta time in seconds since last frame

while running:
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False

    if running:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]: camera.y -= 64 * dt
        if keys[pygame.K_s]: camera.y += 64 * dt
        if keys[pygame.K_a]: camera.x -= 64 * dt
        if keys[pygame.K_d]: camera.x += 64 * dt

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e: edit_mode = not edit_mode
                if event.key == pygame.K_t: selector_mode = not selector_mode
        if not edit_mode: selector_mode = False

        # clamp camera
        if camera.x < 0: camera.x = 0
        if camera.y < 0: camera.y = 0
        # TODO clamp camera to be within right and bottom limits

        screen.fill("white")

        grid.draw(screen, camera)
        if selector_mode: selector.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

pygame.quit()