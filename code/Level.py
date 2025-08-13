#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.display

from code.Entity import Entity
from code.EntityFactory import EntityFactory
from pygame import Surface, Rect
from pygame.font import Font

class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = 20000
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list : list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('level1'))

    def run(self, ):
        pygame.mixer_music.load('assets/MUSICS/level1.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()  # limitar fps
        while True:
            clock.tick(75)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000 : .1f}s', (255, 128, 120), (20, 5))
            self.level_text(14, f'fps: {clock.get_fps() : .0f}', (255, 128, 120), (20,285))
            self.level_text(14, f'entidades: {len(self.entity_list)}', (255, 128, 120), (35,300))
            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        # Carrega a fonte do sistema (note o 'F' maiúsculo em SysFont)
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)

        # Renderiza o texto com antialiasing (suavização) e converte para alpha
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()

        # Obtém o retângulo (Rect) do texto e centraliza na posição especificada
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)

        # Desenha o texto na janela (note que 'dest' é opcional como argumento nomeado)
        self.window.blit(source=text_surf, dest=text_rect)