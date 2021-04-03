from models.player import Player
    
class PlayerController():
    def __init__(self, maze_, tile_width, tile_height):
        start_coords = maze_.start_coordinates()
        self.player = Player(start_coords, tile_width, tile_height)
        self._maze = maze_
        self.tile_width = tile_width
        self.tile_height = tile_height

    def pickup(self, coordinates):
        self.player._backpack += 1
        # remove the coin image and cell
        self._maze.cells[int(coordinates[1])][int(coordinates[0])] = ' '
        self._maze.items.remove(coordinates)      
    
    
    def get_player(self):
        return self.player
    
    def move(self, direction):
        if direction == 'UP':
            # scale down from pixels to coordinates
            want_to_move = (self.player.rect.x/self.tile_width, (self.player.rect.y - self.tile_height)/self.tile_height)
            if not self._maze.is_collision(want_to_move):
                # check if item, if it is, pickup
                if self._maze.is_item(want_to_move):
                    self.pickup(want_to_move)
                
                self.player.rect.y -= self.tile_height
                
        elif direction == 'DOWN':
            want_to_move = (self.player.rect.x/self.tile_width, (self.player.rect.y + self.tile_height)/self.tile_height)
            if not self._maze.is_collision(want_to_move):
                if self._maze.is_item(want_to_move):
                    self.pickup(want_to_move)
                # exit condition
                if (want_to_move == self._maze.end_coordinates) and self.player._backpack == 4:
                    exit()
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
