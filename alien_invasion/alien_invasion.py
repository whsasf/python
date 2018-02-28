#!/usr/bin/env python3

import sys
import pygame
from settings import Settings
from ship import Ship

def run_game():
    #initial game and creare a scren object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    
    #create a ship
    ship = Ship(screen)
    
    #start main loop of the game
    while True:
        #monitor keybord and mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        #let the screen visible
        pygame.display.flip()
run_game()