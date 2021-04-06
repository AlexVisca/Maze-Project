from models.maze import Maze
import pygame
import random

class MazeController:
    def __init__(self, tile_width=50, tile_height=50):
        """Initaliaze MazeController

        Args:
            tile_width (int): number of pixels in one tile width
            tile_height (int): number of pixels in one tile height
        """
        maze = Maze()
        self.tile_width = tile_width
        self.tile_height = tile_height
        
        self.cells = maze.cells()
        self.load_from_file()

        self.wall_coordinates = maze.wall_coordinates
        self.empty_cells = maze.empty_cells
        self.items = maze.items
        
        # images
        self.coin_image = maze.coin_image
        self.wall_image = maze.wall_image
        
        # have random items been generated?
        self.generated = maze.generated
        self.end_coordinates = maze.end_coordinates

    def draw(self, window):
        """
        Draw the maze in pygame.
        
        Args:
            window (pygame window): main game window
        """
        # populate pygame maze based on cells
        for y in range(0, len(self.cells)):
            line = self.cells[y]
            for x in range(len(line)):
                cell = line[x]
                if cell == 'X':
                    self.wall_coordinates.append((x,y))
                    window.blit(self.wall_image, (x*self.tile_width, y*self.tile_height))
                elif cell == 'I':
                    window.blit(self.coin_image, (x*self.tile_width, y*self.tile_height))
                elif cell != 'E' and cell != 'P':
                    self.empty_cells.append((x,y))
                else:
                    continue
        
        if not self.generated:
            # add random items to the maze, this cannot be done in the initalization because the 
            # cells are all empty until 'draw' is called
            self.generate_items()
        
        if not self.end_coordinates:
            #set end coordinates
            self.get_end_coordinates()
    
    def generate_items(self, num_items=4):
        """Generate random coordinates for items in the maze

        Args:
            num_items (int, optional): Number of items to generate. Defaults to 4.
        """
        # boolean to mark that items have been generated so they are only generated once
        self.generated = True
        item_coords = list()
        
        for i in range(0, num_items):
            # get a random index from empty cell list
            rand_index = random.randint(0, len(self.empty_cells) -1)
            item_coord = self.empty_cells[rand_index]
            item_coords.append(item_coord)
            self.empty_cells.remove(item_coord) # remove chosen cell so we do not reselect it
        
        # Update our cells with character 'I' to indicate where items are
        for coord in item_coords:
            self.cells[coord[1]][coord[0]] = 'I'
            
        self.items = item_coords
    
    def start_coordinates(self):
        """Return the (x,y) coordinates of the start location

        Assume the start is at the top of the Maze
        Raises:
            Exception: When the start can not be found

        Returns:
            tuple of ints: (x,y) coordinates of the start position
        """
        first_row = self.cells[0]
        for i in range(len(first_row)):
            x = first_row[i]
            if x == 'P':
                return (i,0) # as x and y coordinates
        raise Exception("Start coordinates could not be found")

    def get_end_coordinates(self):
        """
        Find and save the coordinates of the exit
        
        Assume the exit is at the bottom of the maze
        """
        last_row = self.cells[-1]
        for i in range(len(last_row)):
            x = last_row[i]
            if x == 'E':
                self.end_coordinates = (i,len(self.cells) -1)
                return # end found, return nothing 
        raise Exception("End coordinates could not be found")
    
    def is_collision(self, coordinates):
        """Return True if there is a wall at coordinates

        Args:
            coordinates (tuple of int): (x,y) x and y coordinates to check

        Returns:
            boolean: True if wall at coordinates, False if wall not at coordinates
        """
        # check that x coordinate is in the range of 0 to the len of the cells in the x axis, same for y axis
        if (0 <= coordinates[0] < len(self.cells[0])) and (0 <= coordinates[1] < len(self.cells)):
            return coordinates in self.wall_coordinates
        return True # coordinates out of map range

    def is_item(self, coordinates):
        """Return True if there is an item at coordinates

        Args:
            coordinates (tuple of int): (x,y) x and y coordinates to check

        Returns:
            boolean: True if item at coordinates, False if item not at coordinates
        """
        return coordinates in self.items

    def load_from_file(self, filename=None):
        """create a matrix of cells from the maze text file

        Args:
            filename (string, optional): maze filename. Defaults to None.
        """
        if not filename:
            filename = "m_lvl_2.txt"
        
        with open(filename, 'r+') as file:
            data = file.readlines()
            for line in data:
                line = line.strip() # remove blank spaces
                line = line.strip('\n') # remove newline characters
                self.cells.append(list(line))