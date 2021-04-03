import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, start_coordinates, tile_width, tile_height):
        super().__init__()
        image = pygame.image.load('blue-stick-man-hi.png')
        self.image = pygame.transform.scale(image, (50, 50))
        self.rect = self.image.get_rect()
        
        self.tile_width = tile_width
        self.tile_height = tile_height

        # Player starts where 'P' is on the map
        x_pixels, y_pixels = start_coordinates
        self.rect.x = x_pixels*tile_width
        self.rect.y = y_pixels*tile_height

        self._backpack = 0