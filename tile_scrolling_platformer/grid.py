import math

import pygame.sprite
from constants import display, tile_size
from costume_sprite import CostumeSpriteFactory

class Grid:
    """
    Represents a grid of tiles. The scene contains the entire grid, and a
    viewport looks into a rectangular region of the scene.
    """

    # (x, y) dimensions of tiles to fill display
    viewport = (math.ceil(display[0] / tile_size) + 1,
                math.ceil(display[1] / tile_size + 1))

    # (x, y) dimensions of tiles in larger scene into which viewport is looking
    scene = (18 * viewport[0], 4 * viewport[1])

    def __init__(self):
        # make costume numbers for each grid position
        self.tiles = [[0 for _ in range(Grid.scene[1])]
                      for _ in range(Grid.scene[0])]
        for i in range(Grid.scene[0]):
            for j in range(Grid.scene[1]):
                self.tiles[i][j] = (i + j) % 10  # TODO init to a real scene

        # make sprites for each viewport position
        sprite_factory = CostumeSpriteFactory('assets/Tiles')
        self.sprites = \
            [[sprite_factory.make_sprite() for _ in range(Grid.viewport[0])]
             for _ in range(Grid.viewport[1])]

        # make a group for the tiles
        self.group = pygame.sprite.Group()
        for row in self.sprites:
            self.group.add(row)

    def draw(self, screen, camera):
        """Draws the viewport on a screen.

        This function draws the tiles in the scene, spaced evenly across the
        screen. The scene's position is offset by the camera coordinates
        provided in the camera argument.

        Args:
            screen: the Pygame surface to draw on.
            camera: A tuple containing the (x, y) coordinates of the camera.
            These coordinates are used to offset the scene's position, allowing
            for scrolling or camera movement.
        """
        row = 0
        for sprite_row in self.sprites:
            column = 0
            for sprite in sprite_row:
                tile = self.select_tile((column, row), camera)
                sprite.switch_costume(tile)
                location = self.locate((column, row), camera)
                sprite.go_to(location)
                column += 1
            row += 1

        self.group.draw(screen)

    def select_tile(self, tile_position, camera):
        """Selects a tile from the scene, given the tile and camera positions.

        This function determines the tile at a given screen position,
        considering the camera offset.

        Args:
            tile_position: A tuple (column, row) representing the tile's
            position.
            camera: A tuple (x, y) representing the camera's coordinates in the
            scene.

        Returns:
            The tile object at the specified position.
        """
        x = tile_position[0] * tile_size + camera[0]
        y = tile_position[1] * tile_size + camera[1]
        column = math.floor(x / tile_size)
        row = math.floor(y / tile_size)
        return self.tiles[column][row]

    def locate(self, tile_position, camera):
        """Calculates the viewport coordinates of a tile.

          This function determines the pixel coordinates of a tile relative to
          the current viewport, taking into account the tile and camera
          positions.

          Args:
              tile_position: A tuple (column, row) representing the tile's
              position.
              camera: A tuple (x, y) representing the camera's coordinates in
              the scene.

          Returns:
              A tuple (x, y) containing the pixel coordinates of the tile's
              top-left corner relative to the viewport.
        """
        return (-(camera[0] % tile_size) + (tile_position[0] * tile_size),
                -(camera[1] % tile_size) + (tile_position[1] * tile_size))
