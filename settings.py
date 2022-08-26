import pygame
pygame.init()

# Setting the Title of the Application
pygame.display.set_caption("Enter Title Here:")

# Screen Window Size (16:9)
screen_length = 1024
screen_height = 576

title_screen = (screen_length, screen_height)

# Clock, Time, Framerate
clock = pygame.time.Clock()
FPS = 60

# Surface Variables
start_background = pygame.image.load("assets/backgrounds/title_screen.jpg")
play_background_test = pygame.image.load("assets/backgrounds/title_screen.jpg")

# Text Settings
test_font = pygame.font.Font(None, 50)
text_surface = test_font.render('Game Text Test', False, 'Black')