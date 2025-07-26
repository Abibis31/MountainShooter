import pygame
from code.menu import Menu
#!/usr/bin/python
# -*- coding: utf-8 -*-

class Game:
    def __init__(self):
        self.window = None
        self.Port1 = None
        self.name = None
        self.enity_list = None

        pygame.init()
        self.window = pygame.display.set_mode(size=(576, 324))  # inicializa a janela

    def Operation1(self, ):
        pass

    def run(self, ):


        while True:  # laço para manter a janela
            menu = Menu(self.window)
            menu.run()
            pass


