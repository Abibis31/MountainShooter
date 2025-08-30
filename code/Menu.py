#from lib2to3.pytree import convert

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import MENU_OPTIONS, WHITE

#!/usr/bin/python
# -*- coding: utf-8 -*-
image_menu = 'assets/bodys/menu.png'

class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load(image_menu).convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):

        menu_option = 0
        pygame.mixer_music.load('assets/MUSICS/menu_music.mp3')  # buscando music
        pygame.mixer_music.play(-1)  # o menos um e para fazer um loop´na music

        while True:
            #desenho do fundo
            self.window.blit(source=self.surf, dest=self.rect)
            #desenho do menu
            self.menu_text(50,"MOUNTAIN",(255, 174, 66), (320, 70))
            self.menu_text(50, "Shotter", (255, 174, 66), (320, 105))


            #tamanho = 200
            for i in range(len(MENU_OPTIONS)):
                if i == menu_option:
                    self.menu_text(23, MENU_OPTIONS[i], (255, 165, 10), (320, 200 + 20 * i))
                else:
                    self.menu_text(23, MENU_OPTIONS[i], (100, 100, 100), (320, 200 + 20 * i))
            pygame.display.flip()


            #EVENTOS DE TECLAS

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() #close window
                    quit() #end

                if event.type ==pygame.KEYDOWN:
                    if  event.key == pygame.K_DOWN: #verificando se a tecla pressionada é a K_DOWN(seta pra baixo)
                        if menu_option < len(MENU_OPTIONS) -1:
                            menu_option += 1
                        else:
                            menu_option = 0

                    if  event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTIONS) -1

                    if event.key == pygame.K_RETURN:
                        return MENU_OPTIONS[menu_option]


    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        # Carrega a fonte do sistema (note o 'F' maiúsculo em SysFont)
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)

        # Renderiza o texto com antialiasing (suavização) e converte para alpha
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()

        # Obtém o retângulo (Rect) do texto e centraliza na posição especificada
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)

        # Desenha o texto na janela (note que 'dest' é opcional como argumento nomeado)
        self.window.blit(source=text_surf, dest=text_rect)
   