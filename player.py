import pygame
from os import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, surface):
        super().__init__()

        self.import_animation_spritesheets()
        self.animation_speed = 0.15 # how fast animations will run
        self.frame_index = 0
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)

        # Player Movement
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 5
        self.gravity = 0.75
        self.jump_height = -20

#    player status
        self.status = 'idle'
        self.facing_right = True
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False
   
    def import_folder(self, path):
        animation_list = []

        for _,__,image_files in walk(path):
            for image in image_files:
                fuller_path = path + "/" + str(image)
                image_surface = pygame.image.load(fuller_path).convert_alpha()
                image_surface = pygame.transform.scale(image_surface, (96,96))
                animation_list.append(image_surface)
                               
        return animation_list     

    def import_animation_spritesheets(self):
        character_path = 'assets/ranger_hero/single_animations'
        self.animations = {"idle":[], "jump":[], "running":[], "slashing":[], "shooting":[]}
        
        for animation in self.animations.keys():
            full_path = character_path + "/" + animation
            self.animations[animation] = self.import_folder(full_path)
    
    def animate(self):
        animation = self.animations[self.status]
        # will be more dynamic later

        # to loop through animation 
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        
        image = animation[int(self.frame_index)]
        if self.facing_right:
            self.image = image        
        else:
            flipped_image = pygame.transform.flip(image,True,False)
            self.image = flipped_image
        # set the rect
        if self.on_ground and self.on_right:
            self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
        elif self.on_ground and self.on_left:
            self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
        elif self.on_ground:
            self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
        elif self.on_ceiling and self.on_right:
            self.rect = self.image.get_rect(topright = self.rect.topright)
        elif self.on_ceiling and self.on_left:
            self.rect = self.image.get_rect(topleft = self.rect.topleft)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop = self.rect.midtop)
        

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_height

    def get_status(self):
        if self.direction.y < 0:
            self.status = 'jump'
        elif self.direction.y > 1:
            self.status = 'jump' # currently do not have an animation for falling
        else:
            if self.direction.x != 0:
                self.status = 'running'
            else:
                self.status = 'idle'
    
    def get_input(self):

        for event in pygame.event.get():  
            keys = pygame.key.get_pressed()

            if keys[pygame.K_d]:
                self.direction.x = 1
                self.facing_right = True
            elif keys[pygame.K_a]:
                self.direction.x = -1
                self.facing_right = False
            else: 
                self.direction.x = 0
            
            if keys[pygame.K_w] and self.on_ground:
                self.jump()
            # if event.type == pygame.KEYDOWN: 
            #     if event.key == pygame.K_w:
            #         self.jump()
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                    
    def update(self): 
        self.get_input()
        self.get_status()
        self.animate()
