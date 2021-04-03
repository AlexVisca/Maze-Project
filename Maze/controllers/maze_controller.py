from models.maze import Maze
import pygame
import random

class MazeController:
    def __init__(self):
        maze = Maze()
        
        self.cells = maze.cells
        self.load_from_file()

        self.wall_coordinates = maze.wall_coordinates
        self.empty_cells = maze.empty_cells
        self.items = maze.items
        
        # coin image
        self.coin_image = maze.coin_image
        
        # have random items been generated?
        self.generated = maze.generated
        self.end_coordinates = maze.end_coordinates

    def draw(self, window, image, tile_width, tile_height):
        for y in range(0, len(self.cells)):
            line = self.cells[y]
            for x in range(len(line)):
                spot = line[x]
                if spot == 'X':
                    self.wall_coordinates.append((x,y))
                    window.blit(image, (x*tile_width, y*tile_height))
                elif spot == 'I':
                    window.blit(self.coin_image, (x*tile_width, y*tile_height))
                elif spot != 'E' and spot != 'P':
                    self.empty_cells.append((x,y))
                else:
                    continue
        
        if not self.generated:
            # add items to the maze
            self.generate_items(window, tile_width, tile_height)
        
        if not self.end_coordinates:
            self.get_end_coordinates()
    
    def generate_items(self, window, tile_width, tile_height):
        self.generated = True
        image = pygame.image.load('Coin_Dollar.png')
        image = pygame.transform.scale(image, (tile_width, tile_height))
        
        item_coords = list()
        for i in range(0, 4):
            # get a random index from empty cell list
            rand_index = random.randint(0, len(self.empty_cells) -1)
            item_coord = self.empty_cells[rand_index]
            item_coords.append(item_coord)
            self.empty_cells.remove(item_coord) # remove chosen cell so we do not reselect it
        
        for coord in item_coords:
            self.cells[coord[1]][coord[0]] = 'I'
            
        self.items = item_coords
    
    def start_coordinates(self):
        # Assume start is in the first line:
        first_row = self.cells[0]
        for i in range(len(first_row)):
            x = first_row[i]
            if x == 'P':
                return (i,0) # as x and y coordinates
        print("default start coordinates")
        return 0

    def get_end_coordinates(self):
        # Assume start is in the first line:
        last_row = self.cells[-1]
        for i in range(len(last_row)):
            x = last_row[i]
            if x == 'E':
                self.end_coordinates = (i,len(self.cells) -1)
                return 
        print("default end coordinates")
        return
    
    def is_collision(self, coordinates):
        # coordinated in format (x,y)
        # return True if x and y is not the location of a wall
        return coordinates in self.wall_coordinates

    def is_item(self, coordinates):
        # coordinated in format (x,y)
        # Return true if item
        return coordinates in self.items

    def load_from_file(self, filename=None):
        if not filename:
            filename = "m_lvl_1.txt"
        
        with open(filename, 'r+') as file:
            data = file.readlines()
            for line in data:
                line = line.strip('\n') #NOTE: remove newline characters
                self.cells.append(list(line))