import os
import pygame
from constants import tile_size

class CostumeSprite(pygame.sprite.Sprite):
    def __init__(self, sprite_dir, position=(0,0)):
        super().__init__()

        costumes_dir = f'{sprite_dir}/costumes'

        self.position = position

        self.costumes = []

        for file in sorted(os.listdir(costumes_dir)):
            image = pygame.image.load(f'{costumes_dir}/{file}')
            image = pygame.transform.scale(image, (tile_size, tile_size))
            image = image.convert_alpha()
            self.costumes.append(image)

        self.switch_costume(0)

    def switch_costume(self, index):
        """Switch to a specific costume by index."""
        self.current_costume = index
        self.image = self.costumes[self.current_costume]
        self.go_to(self.position)

    def next_costume(self):
        """Switch to the next costume in the list."""
        index = (self.current_costume + 1) % len(self.costumes)
        self.switch_costume(index)

    def go_to(self, position):
        """Sends the sprite to a position."""
        self.position = position
        self.rect = self.image.get_rect(center = self.position)
