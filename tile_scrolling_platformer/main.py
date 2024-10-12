import pygame
from constants import display, tile_size
from costume_sprite import CostumeSprite

pygame.init()
screen = pygame.display.set_mode(display)
clock = pygame.time.Clock()
running = True

tile_group = pygame.sprite.Group()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if running:
        tile_group.empty()

        screen.fill("white")

        clone_count_y = 5
        x = display[0] / 2
        y = display[1] / 2

        for _ in range(clone_count_y):
            tile = CostumeSprite('assets/Tiles')
            tile.go_to((x, y))
            tile.switch_costume(8)
            tile_group.add(tile)
            x += tile_size

        tile_group.draw(screen)
        pygame.display.flip()
        clock.tick(60)

pygame.quit()