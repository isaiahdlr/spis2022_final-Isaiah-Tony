from csv import reader
from re import X
import pygame
from settings import tile_size
from os import walk

def import_folder(path):
    animation_list = []

    for _,__,image_files in walk(path):
        for image in image_files:
            fuller_path = path + "/" + str(image)
            image_surface = pygame.image.load(fuller_path).convert_alpha()
            # image_surface = pygame.transform.scale(image_surface, (96,96))
            animation_list.append(image_surface)
                            
    return animation_list  


def import_csv_layout(path):
    terrain_map = []
    with open(path) as map:
        level = reader(map, delimiter = ',')
        for row in level:
            terrain_map.append(list(row))
        return terrain_map

def import_cut_graphics(path):
    surface = pygame.image.load(path).convert_alpha()
    tile_num_x = int(surface.get_size()[0] / tile_size)
    tile_num_y = int(surface.get_size()[1] / tile_size)

    cut_tiles = []

    for row in range(tile_num_y):
        for col in range(tile_num_x):
            x = col * tile_size
            y = row * tile_size
            new_surface = pygame.Surface((tile_size,tile_size))
            new_surface.blit(surface,(0,0),pygame.Rect(x,y,tile_size,tile_size))
            cut_tiles.append(new_surface)

    return cut_tiles