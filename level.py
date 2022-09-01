import pygame
from tile import *
from settings import tile_size, screen_length
from player import Player
from helpers import import_csv_layout, import_cut_graphics
import os

class Level:
    def __init__(self, level_data, surface):

        # level setup
        # terrain
        terrain_layout = import_csv_layout(level_data['terrain'])
        self.terrain_sprites = self.create_tile_group(terrain_layout, 'terrain')

        # coins
        coin_layout = import_csv_layout(level_data["coins"])
        self.coin_sprites = self.create_tile_group(coin_layout, 'coins')

        # decorations
        decoration_layout = import_csv_layout(level_data['decorations'])
        self.decoration_sprites = self.create_tile_group(decoration_layout, 'decorations')

        # constraints
        constraint_layout = import_csv_layout(level_data['constraints'])
        self.constraint_sprites = self.create_tile_group(constraint_layout,'constraints')

        # enemies
        enemy_layout = import_csv_layout(level_data['enemies'])
        self.enemy_sprites = self.create_tile_group(enemy_layout, 'enemies')

        self.display_surface = surface
        self.world_shift = 0
        self.current_x = 0

        # player setup
        player_layout = import_csv_layout(level_data['player'])
        self.player = pygame.sprite.GroupSingle()
        self.flag = pygame.sprite.GroupSingle()
        self.player_setup(player_layout)
        
        # enemy movement constraints
    def enemy_collision_reverse(self):
        for enemy in self.enemy_sprites.sprites():
            if pygame.sprite.spritecollide(enemy,self.constraint_sprites,False):
                enemy.reverse()

    def create_tile_group(self, layout, type):
        sprite_group = pygame.sprite.Group()
        
        
        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                if 316 > int(val) > -1:
                    x = col_index * tile_size
                    y = row_index * tile_size
                    
                    if type == 'terrain' and int(val) < 316:
                        terrain_tile_list = import_cut_graphics("assets/backgrounds/oak_woods_v1.0/oak_woods_tileset_x2.png")
                        tile_surface = terrain_tile_list[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)

                    if type == 'coins':
                        sprite = AnimatedTile(tile_size,x,y,"assets/coin")
                  
                    if type == 'enemies':
                        sprite = Enemy(tile_size,x,y,"assets/enemies/mushroom/idle")

                    if type == 'decorations':
                        # decoration_tile_list = import_cut_graphics('') will not work because the tileset is made up of a group of images
                        sprite = Fences(tile_size,x,y)
                        
                    if type == 'constraints':
                        print("constraint loaded")
                        sprite = Tile(tile_size,x,y)    
                    
                    sprite_group.add(sprite)
                    
                elif int(val) > 315:
                    print(val)
                    pass
                        
        return sprite_group
               
    def player_setup(self,layout):
        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                y = col_index * tile_size
                x = row_index * tile_size
                if val == '7':
                    sprite = Player((x,y), self.display_surface)
                    self.player.add(sprite)
                if val == '8': 
                    flag_surface = pygame.image.load('assets/start_end/flag.png').convert_alpha
                    sprite = StaticTile(tile_size,x,y,flag_surface)
                    self.flag.add(sprite)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        
        # If player moves to far right or left they stop moving and instead the world moves, making it seem like they are still travelling far
        if player_x < screen_length / 4 and direction_x < 0:
            self.world_shift = 5
            player.speed = 0
        elif player_x > screen_length*0.75 and direction_x > 0:
            self.world_shift = -5
            player.speed = 0
        else: 
            self.world_shift = 0
            player.speed = 5

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.terrain_sprites.sprites(): # will add other collidable sprites later
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                   player.rect.left = sprite.rect.right
                   player.on_left = True
                   self.current_x = player.rect.left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True
                    self.current_x = player.rect.right

        if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
            player.on_left = False
        if player.on_right and (player.rect.right < self.current_x or player.direction.x <= 0):
            player.on_right = False
    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()
        
        for sprite in self.terrain_sprites.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                   player.rect.bottom = sprite.rect.top
                   player.direction.y = 0
                   player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True
        if player.on_ground and player.direction.y < 0 or player.direction.y > 1: 
            player.on_ground = False  
        if player.on_ceiling and player.direction.y > 0:
            player.on_ceiling = False 
    def run(self):

        # level tiling
        self.terrain_sprites.update(self.world_shift)
        self.terrain_sprites.draw(self.display_surface)

        # coins
        self.coin_sprites.update(self.world_shift)
        self.coin_sprites.draw(self.display_surface)

        # decorations
        # self.decoration_sprites.update(self.world_shift)
        # self.decoration_sprites.draw(self.display_surface)

        # enemies
        self.enemy_sprites.update(self.world_shift)
        self.constraint_sprites.update(self.world_shift)
        self.enemy_collision_reverse()
        self.enemy_sprites.draw(self.display_surface)

        # player mechanics WIP
        self.scroll_x()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()

        # self.flag.update(self.world_shift)
        # self.flag.draw(self.display_surface)
        
        self.player.update()
        self.player.draw(self.display_surface)

