# from curses.panel import bottom_panel
import pygame

from helpers import import_folder

class Tile(pygame.sprite.Sprite):
    def __init__(self, size, x, y):
        super().__init__()
        self.image = pygame.Surface((size,size))
        self.rect = self.image.get_rect(topleft = (x,y))

    def update(self, x_shift):
        self.rect.x += x_shift

class StaticTile(Tile):
    def __init__(self,size,x,y,surface):
        super().__init__(size,x,y)
        self.image = surface
    
    # def update(self):
        # if palyer collides with self = win

class AnimatedTile(Tile):
    def __init__(self,size,x,y,path):
        super().__init__(size,x,y)
        self.frames = import_folder(path)
        self.frame_index = 0
        self.image = pygame.transform.flip(self.frames[int(self.frame_index)],False,True)

    def animate(self):
        self.frame_index += 0.15
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

    def update(self, x_shift):
        self.animate()
        self.rect.x += x_shift

class Enemy(AnimatedTile):
    def __init__(self,size,x,y,path):
        super().__init__(size,x,y,path)
        self.rect.y += size - self.image.get_size()[1]
        self.speed = 4

    def move(self):
        self.rect.x += self.speed
    
    def reverse_image(self):
        if self.speed < 0:
            self.image = pygame.transform.flip(self.image,True,False)

    def reverse(self):
        self.speed *= -1

    def update(self,shift):
        self.rect.x += shift 
        self.animate()
        self.move()
        self.reverse_image()


class Fences(StaticTile):
    def __init__(self,size,x,y):
        super().__init__(size,x,y,pygame.image.load('assets/backgrounds/oak_woods_v1.0/decorations/fence_1.png'))
        y_offset = y + size/1.5
        self.rect = self.image.get_rect(topleft = (x,y_offset))

# class Flag(StaticTile):
    def __init__(self,size,x,y):
        super().__init__(size,x,y,pygame.image.load('assets/start_end/flag.png').convert_alpha)
