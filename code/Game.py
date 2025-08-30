import pygame

from code.Const import MENU_OPTIONS
from code.Level import Level
from code.Menu import Menu
from code.Score import Score


#!/usr/bin/python
# -*- coding: utf-8 -*-
#import Level

class Game:
    def __init__(self):
        self.window = None
        self.Port1 = None
        self.name = None
        self.entity_list = None

        pygame.init()
        self.window = pygame.display.set_mode(size=(576, 324))  # inicializa a janela


    def run(self, ):
        while True:  # laço para manter a janela
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTIONS[0], MENU_OPTIONS[1], MENU_OPTIONS[2]]:
                player_score = [0,0] #[player1, player2]
                level = Level(self.window, 'level1', menu_return, player_score)
                level_return = level.run(player_score)
                if level_return:
                    level = Level(self.window, 'level2', menu_return, player_score)
                    level_return = level.run(player_score)
                    if level_return:
                        score.save(menu_return, player_score)

            elif menu_return == MENU_OPTIONS[3]:
                score.show()

            elif menu_return == MENU_OPTIONS[4]:
                pygame.quit()
                quit()

            else:
                pass


