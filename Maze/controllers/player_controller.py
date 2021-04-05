from models.player import Player

"""
Creates an instance of the player and has the player actions
"""
class PlayerController():
    def __init__(self, maze_, tile_width, tile_height):
        """Initalize an instance of the PlayerController

        Args:
            maze_ (Maze): an instance of the maze so the player can interact with it ex: pickup
            tile_width (int): width of a tile for scaling purposes
            tile_height (int): height of a tile for scaling purposes
        """
        start_coords = maze_.start_coordinates()
        self.player = Player(start_coords, tile_width, tile_height)
        self._maze = maze_
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.end = False # Turns to True if game is won

    def pickup(self, coordinates):
        self.player._backpack += 1
        # remove the coin image and remove item from maze
        self._maze.cells[int(coordinates[1])][int(coordinates[0])] = ' '
        self._maze.items.remove(coordinates)      
    
    
    def get_player(self):
        return self.player
    
    def move(self, direction):
        """Move the player in a direction

        Args:
            direction (string): 'LEFT', 'RIGHT', 'UP', or 'DOWN'
        """
        if direction == 'UP':
            # The (x,y) coordinates that the player wants to move to. We have the players pixel location but not the
            # tile location so we have to scale down from pixels to coordinates. 
            # scaling format is (x_pixel_location/tile_width, y_pixel_location/tile_height ) for current location.
            # Then we adjust for the direction they want to move
            want_to_move = (self.player.rect.x/self.tile_width, (self.player.rect.y - self.tile_height)/self.tile_height)
            # Check if the position they want to move to collides with a wall
            if not self._maze.is_collision(want_to_move):
                # check if item, if it is, pickup
                if self._maze.is_item(want_to_move):
                    self.pickup(want_to_move)
                # move player pixel coordinates to new position
                self.player.rect.y -= self.tile_height
                
        elif direction == 'DOWN':
            want_to_move = (self.player.rect.x/self.tile_width, (self.player.rect.y + self.tile_height)/self.tile_height)
            if not self._maze.is_collision(want_to_move):
                if self._maze.is_item(want_to_move):
                    self.pickup(want_to_move)
                # exit condition, if the player is moving down into the coordinates of the exit
                if (want_to_move == self._maze.end_coordinates):
                    self.end = True
                self.player.rect.y += self.tile_height
                
        elif direction == 'LEFT':
            want_to_move = ((self.player.rect.x - self.tile_width)/self.tile_width, self.player.rect.y/self.tile_height)
            if not self._maze.is_collision(want_to_move):
                if self._maze.is_item(want_to_move):
                    self.pickup(want_to_move)
                self.player.rect.x -= self.tile_width
                
        elif direction == 'RIGHT':
            want_to_move = ((self.player.rect.x + self.tile_width)/self.tile_width, self.player.rect.y/self.tile_height)
            if not self._maze.is_collision(want_to_move):
                if self._maze.is_item(want_to_move):
                    self.pickup(want_to_move)
                self.player.rect.x += self.tile_width
    