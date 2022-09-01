import pygame
from sys import exit
from settings import *
from button import *
from tile import *
from game_data import level_1
from level import Level
from player import Player

pygame.init()

level = Level(level_1, screen)

def title_screen():
    pygame.display.set_caption("Very Epic Game")
    while True:
        clock.tick(FPS)
        screen.blit(start_background, (0, 0))
       
        menu_mouse_pos = pygame.mouse.get_pos()

        menu_text = main_font.render("The Most Epic Game", True, "Black")
        menu_rect = menu_text.get_rect(center=(screen_length // 2, 100))

        play_button = Button(image=pygame.image.load('assets/button.png'),
                             pos=(screen_length // 2, 275),
                             text_input="Play",
                             font=main_font,
                             base_color="Black",
                             hovering_color="White")
        quit_button = Button(image=pygame.image.load('assets/button.png'),
                             pos=(screen_length // 2, 400),
                             text_input="Quit",
                             font=main_font,
                             base_color="Black",
                             hovering_color="White")

        screen.blit(menu_text, menu_rect)

        for button in [play_button, quit_button]:
            button.checkForHovering(menu_mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(menu_mouse_pos):
                    load_level1()
                if quit_button.checkForInput(menu_mouse_pos):
                    print("Goodbye!")
                    pygame.quit()
                    exit()

        pygame.display.update()

# def lose_level1():
    lose_level1 = True
    while lose_level1:
        clock.tick(FPS)
        screen.fill('black')

        start_mouse_pos = pygame.mouse.get_pos()

        lose_text = main_font.render("You Lose!", True, "White")
        lose_rect = lose_text.get_rect(center=(screen_length // 2, 100))  

        play_again = Button(image=pygame.image.load('assets/button.png'),
                            pos=(screen_length // 2, 275),
                            text_input="Retry",
                            font=main_font,
                            base_color="White",
                            hovering_color="Red")

        play_again.checkForHovering(start_mouse_pos)
        play_again.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_again.checkForInput(start_mouse_pos):
                    play_level1()
                    lose_level1 = False
                    
        screen.blit(lose_text, lose_rect)
        pygame.display.update()

def load_level1():
    first_level = False
    running = True
    while running:
        clock.tick(FPS)
        screen.fill('black')

        start_mouse_pos = pygame.mouse.get_pos()

        start_text = main_font.render("Level 1", True, "White")
        start_rect = start_text.get_rect(center=(screen_length // 2, 100))

        start_level = Button(image=pygame.image.load('assets/button.png'),
                            pos=(screen_length // 2, 275),
                            text_input="Start",
                            font=main_font,
                            base_color="White",
                            hovering_color="Red")

        start_level.checkForHovering(start_mouse_pos)
        start_level.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_level.checkForInput(start_mouse_pos):
                    play_level1()
                    running = False
                    
        screen.blit(start_text, start_rect)
        pygame.display.update()

def play_level1():
    global first_level 
    first_level = True
    while first_level:
        clock.tick(FPS)

        screen.fill("Grey")

        level.run()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            

        pygame.display.update()
    
    # lose_level1()

title_screen()
