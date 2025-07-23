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
        self.window = pygame.display.set_mode(size=(600, 480))  # inicializa a janela

    def Operation1(self, ):
        pass

    def run(self, ):
        print('Setup Start')

        print('Setup End')

        print('Loop Start')
        while True:  # laço para manter a janela
            menu = Menu(self.window)
            menu.run()
            pass
            # Check for all events
            # for event in pygame.event.get():
             #   if event.type == pygame.QUIT:
              #      pygame.quit()  # Close Window
               #     quit()  # End Pygame


