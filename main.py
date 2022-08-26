import pygame
from sys import exit
from settings import *

pygame.init()

screen = pygame.display.set_mode(title_screen)


def title_screen():
    while True:
        clock.tick(FPS)
        screen.blit(start_background, (0, 0))
        screen.blit(text_surface, (100, 100))
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    play()

def play():
    running = True
    while running:
        screen.blit(play_background_test, (0,0))
        pygame.display.update()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

title_screen()