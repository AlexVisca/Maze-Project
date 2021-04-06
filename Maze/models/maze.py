
import pygame

class Maze:
    """ Maze class

    Stores object attributes
    """
    def __init__(self):
        self._cells = list()

        self.wall_coordinates = list()
        self.empty_cells = list()
        self.items = list()
        
        # coin image
        coin_image = pygame.image.load('./images/Coin_Dollar.png')
        wall_image = pygame.image.load('./images/wall_icon1.png')
        self.coin_image = pygame.transform.scale(coin_image, (50, 50))
        self.wall_image = pygame.transform.scale(wall_image, (50, 50))
        
        # have random items been generated?
        self.generated = False
        self.end_coordinates = False
    
    def cells(self):
        return self._cells