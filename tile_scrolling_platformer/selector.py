import math
import pygame
from pygame.sprite import Group

from constants import display, tile_size
from costume_sprite import CostumeSpriteFactory

class Selector:
    """
    A transparent tile selection surface that is overlaid on top of the grid.
    """

    def __init__(self):
        # transparent surface to fill the whole display
        self.alpha_surface = pygame.Surface(display)
        self.alpha_surface.set_alpha(120)
        self.alpha_surface.fill('black')

        # dimension of tile selector. this ends up being 11 x 7, which is large
        # enough to fit all 67 tiles in assets/Tiles
        dimension = (math.floor(display[0] / tile_size) - 4,
                     math.floor(display[1] / tile_size) - 4)

        # black surface behind sprite list
        self.black_surface =\
            pygame.Surface((dimension[0] * tile_size, dimension[1] * tile_size))
        self.black_surface.fill('white')

        sprite_factory = CostumeSpriteFactory('assets/Tiles')
        self.costumes = []
        i = j = 0  # column and row of sprite
        for costume in range(sprite_factory.count()):
            # calculate (x, y) position of tile
            x = (2 + i) * tile_size
            y = (2 + j) * tile_size

            # make the sprite
            sprite = sprite_factory.make_sprite(costume=costume, position=(x, y))
            self.costumes.append(sprite)

            # update column and row
            i += 1
            if i >= dimension[0]:
                i = 0
                j += 1

        self.group = Group()
        self.group.add(self.costumes)

    def draw(self, screen):
        screen.blit(self.alpha_surface, (0, 0))
        screen.blit(self.black_surface, (2 * tile_size, 2 * tile_size))
        self.group.draw(screen)