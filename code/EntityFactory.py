import random


from code.Enemy import Enemy
from code.Player import Player

from code.Const import WIN_HEIGHT
from code.background import Background


#!/usr/bin/python
# -*- coding: utf-8 -*-

class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'level1':
                list_level=[]
                for i in range(5):
                    list_level.append(Background(f'level1{i}', (0, 0)))
                    list_level.append(Background(f'level1{i}', (575, 0)))

                return list_level
            case'level2':
                list_level = []
                for i in range(4):
                    list_level.append(Background(f'level2{i}', (0, 0)))
                    list_level.append(Background(f'level2{i}', (575, 0)))

                return list_level
            case 'ship_pixel_player1':
                print('nave ativa')
                return Player('ship_pixel_player1', (100, 110))
            case 'ship_pixel_player2':
                return Player('ship_pixel_player2', (100, 90))
            case 'nave_1':
                return Enemy('nave_1', (600, random.randint(30,WIN_HEIGHT-30)))
            case 'nave_2':
                return Enemy('nave_2', (600, random.randint(30, WIN_HEIGHT-30)))
            case 'nave_3':
                return Enemy('nave_3', (600, random.randint(30, WIN_HEIGHT - 30)))