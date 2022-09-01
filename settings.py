import pygame
pygame.init()

# Map Settings
# level1_map = [
# '                                                            ',
# '       XXX                             XXXXXX  XXX           ',
# '      XX  X                XXXXXXXXX               XXXX    ',
# '      XX  X         XXX                    XXXXXX           ',
# ' XX   XX X     XXX             XXXX                    XXX',
# 'XXX    XXX     XXXXXX    XXXXXXXX     XXXXXX     XXXXX      ',
# 'XXX    X X                                  XX        XX   ',
# ' XX  P              XXXXXXXXXX            XXXXX           ',
# ' XXXXXXXXX     XXXXXXXXXXXXXXXXX     XXXXXXXXXXXXXXXXXXX    ',
# ' XX    XXX       XXXXXXXXX                 XXXX             ']

tile_size = 64
vertical_tile_count = 11

# Screen Window Size (16:9)
screen_length = 1200
screen_height = vertical_tile_count * tile_size

# tile_count = 11
# screen_height = 64 * tile count

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

# Text Settings
main_font = pygame.font.SysFont('cambria', 50)
test_text_surface = main_font.render('Game Text Test', False, 'Black')
