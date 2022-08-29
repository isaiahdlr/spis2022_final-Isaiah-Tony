import pygame
from sys import exit
from settings import *
from button import *
from spritesheet import *

pygame.init()

def title_screen():
    pygame.display.set_caption("Title of Game")

    while True:
        clock.tick(FPS)
        screen.blit(start_background, (0, 0))

        menu_mouse_pos = pygame.mouse.get_pos()

        menu_text = main_font.render("Title of Game", True, "White")
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

# def play_test():
    running = True
    while running:
        clock.tick(FPS)
        screen.blit(play_background_test, (0, 0))

        start_mouse_pos = pygame.mouse.get_pos()

        start_text = main_font.render("Welcome to the Game!", True, "White")
        start_rect = start_text.get_rect(center=(screen_length // 2, 100))

        start_back = Button(image=pygame.image.load('assets/button.png'),
                            pos=(screen_length // 2, 275),
                            text_input="Back to Menu",
                            font=main_font,
                            base_color="White",
                            hovering_color="Red")

        start_back.checkForHovering(start_mouse_pos)
        start_back.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_back.checkForInput(start_mouse_pos):
                    title_screen()
                    running = False
                    
        screen.blit(start_text, start_rect)
        pygame.display.update()

def load_level1():
    running = True
    while running:
        clock.tick(FPS)
        screen.blit(play_background_level1, (0, 0))

        start_mouse_pos = pygame.mouse.get_pos()

        start_text = main_font.render("Level 1", True, "White")
        start_rect = start_text.get_rect(center=(screen_length // 2, 100))

        start_level = Button(image=pygame.image.load('assets/button.png'),
                            pos=(screen_length // 2, 275),
                            text_input="Start Level",
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
    level1 = True
    while level1:
        clock.tick(FPS)

        screen.blit(play_background_level1, (0, 0))
        screen.blit(player_idle0, player_rect)
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()

title_screen()
