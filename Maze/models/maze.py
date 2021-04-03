
import pygame

class Maze:
    def __init__(self):
        self.cells = list()

        self.wall_coordinates = list()
        self.empty_cells = list()
        self.items = list()
        
        # coin image
        coin_image = pygame.image.load('Coin_Dollar.png')
        self.coin_image = pygame.transform.scale(coin_image, (50, 50))
        
        # have random items been generated?
        self.generated = False
        self.end_coordinates = False
    
    def cells():
        return self.cells