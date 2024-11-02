import os
import pygame
from constants import tile_size

class CostumeSprite(pygame.sprite.Sprite):
    """Sprite with a changeable costume. Corresponds to a clone in Scratch."""

    def __init__(self, costumes, costume=0, position=(0,0)):
        super().__init__()
        self.position = position
        self.costumes = costumes
        self.switch_costume(costume)

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
        self.rect = self.image.get_rect(topleft = self.position)


class CostumeSpriteFactory:
    """Utility class that produces CostumeSprite. Loading images from files is
    expensive, so it's better to pay that cost once up front. Corresponds to a
    sprite in Scratch."""

    def __init__(self, sprite_dir):
        costumes_dir = f'{sprite_dir}/costumes'

        self.costumes = []

        for file in sorted(os.listdir(costumes_dir)):
            image = pygame.image.load(f'{costumes_dir}/{file}')
            image = pygame.transform.scale(image, (tile_size, tile_size))
            image = image.convert_alpha()
            self.costumes.append(image)

    def make_sprite(self, costume=0, position=(0,0)):
        """Make a CostumeSprite with an optional costume number and position."""
        return CostumeSprite(self.costumes, costume, position)

    def count(self):
        """Return the number of costumes."""
        return len(self.costumes)
