import pygame
from tile import *
from settings import tile_size, screen_length
from player import *

class Level:
    def __init__(self, level_data, surface):

        # level setup
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for row_index, row in enumerate(layout):
            for col_index, column in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                
                if column == 'X':
                    tile = Tile((x,y), tile_size)
                    self.tiles.add(tile)
                if column == 'P':
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)
                    

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        
        # If player moves to far right or left they stop moving and instead          the world moves, making it seem like they are still travelling far
        if player_x < screen_length / 4 and direction_x < 0:
            self.world_shift = 5
            player.speed = 0
        elif player_x > screen_length*0.75 and direction_x > 0:
            self.world_shift = -5
            player.speed = 0
        else: 
            self.world_shift = 0
            player.speed = 5
            
    def run(self):

        # level tiling
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)

        # player mechanics
        self.player.update()
        self.player.draw(self.display_surface)
        self.scroll_x()
        