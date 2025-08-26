#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

import pygame.display

from code.Enemy import Enemy
from code.EntityMediator import EntityMediator
from code.Const import MENU_OPTIONS, EVENT_ENEMY, SPAWN_TIME, EVENT_TIMEOUT, TIMEOUT_LEVEL, SPAWN_TIME_2
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from pygame import Surface, Rect
from pygame.font import Font

from code.Player import Player


class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]):
        self.timeout = 0
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list : list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name))
        player = (EntityFactory.get_entity('ship_pixel_player1'))
        player.score = player_score[0]
        self.entity_list.append(player)

        if self.name == 'level1':
            self.timeout = 50000
        else:
            self.timeout = 70000



        if game_mode in [MENU_OPTIONS[1], MENU_OPTIONS[2]]:
            player = (EntityFactory.get_entity('ship_pixel_player2'))
            player.score = player_score[1]
            self.entity_list.append(player)
            pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME_2)
        else:
            pygame.time.set_timer(EVENT_ENEMY,SPAWN_TIME)

        pygame.time.set_timer(EVENT_TIMEOUT,100)#100ms



    def run(self, player_score: list[int] ):
        pygame.mixer_music.load('assets/MUSICS/level1.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()  # limitar fps
        while True:
            clock.tick(75)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()

                    if shoot is not None:
                        self.entity_list.append(shoot)
                if ent.name =='ship_pixel_player1':
                    self.level_text(15, f'Jogador1 - Vida: {ent.health} | Score {ent.score}', (0, 0, 0), (54, 20))

                if ent.name =='ship_pixel_player2':
                    self.level_text(15, f'Jogador2 - Vida: {ent.health}  | Score {ent.score}', (0, 0, 0), (54, 35))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == EVENT_ENEMY and self.name == 'level1':
                    choice = random.choice(('nave_1', 'nave_2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

                elif event.type == EVENT_ENEMY and self.name == 'level2':
                    choice = random.choice(('nave_1', 'nave_2', 'nave_3'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

                if event.type == EVENT_TIMEOUT:
                    self.timeout -= 100
                    if self.timeout == 0:
                        for  ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'ship_pixel_player1':
                                player_score[0] = ent.score
                            if isinstance(ent, Player) and ent.name == 'ship_pixel_player2':
                                player_score[1] = ent.score
                        return True

                found_player = False
                for ent in self.entity_list:
                    if isinstance( ent, Player):
                        found_player = True

                if not  found_player:
                    return False

            #printed text
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000 : .1f}s', (0, 0, 0), (20, 5))
            self.level_text(14, f'fps: {clock.get_fps() : .0f}', (0, 0, 0), (20,285))
            self.level_text(14, f'entidades: {len(self.entity_list)}', (0, 0, 0), (35,300))
            pygame.display.flip()

            #Colisões
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        # Carrega a fonte do sistema (note o 'F' maiúsculo em SysFont)
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)

        # Renderiza o texto com antialiasing (suavização) e converte para alpha
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()

        # Obtém o retângulo (Rect) do texto e centraliza na posição especificada
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)

        # Desenha o texto na janela (note que 'dest' é opcional como argumento nomeado)
        self.window.blit(source=text_surf, dest=text_rect)