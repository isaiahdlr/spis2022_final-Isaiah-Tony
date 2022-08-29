import pygame
from spritesheet import *
pygame.init()

# Screen Window Size (16:9)
screen_length = 1024
screen_height = 576

window_size = (screen_length, screen_height)
screen = pygame.display.set_mode(window_size)
pygame.display.update()

# Clock, Time, Framerate
clock = pygame.time.Clock()
FPS = 60

# Surface Variables
start_background = pygame.image.load("assets/backgrounds/title_screen.jpg")
start_background = pygame.transform.scale(start_background, window_size)
play_background_level1 = pygame.image.load("assets/backgrounds/level1_pt1.png")
play_background_level1 = pygame.transform.scale(play_background_level1, window_size)

# Colors
black = (0,0,0)

# Player Setup - Idling
player_idle_image = pygame.image.load("assets/ranger_hero/spritesheets/single_animations/ranger_idle.png").convert_alpha()
player_idle_spritesheet = SpriteSheet(player_idle_image)
# Each image is 48 x 48 pixels
player_idle0 = SpriteSheet.get_image(player_idle_spritesheet, 0, 48, 48, 2, black)
player_idle1 = SpriteSheet.get_image(player_idle_spritesheet, 1, 48, 48, 2, black)
player_rect = player_idle0.get_rect(topleft = (100, 200))

# Text Settings
main_font = pygame.font.SysFont('cambria', 50)
test_text_surface = main_font.render('Game Text Test', False, 'Black')