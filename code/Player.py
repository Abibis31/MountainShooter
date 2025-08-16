#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key
import pygame
from pygame import joystick

from code.Const import PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT
from code.Entity import Entity



class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)


    def move(self, ):

        press_key = pygame.key.get_pressed()
        if press_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= 2
        if press_key[PLAYER_KEY_DOWN[self.name]] and self.rect.top < 310:
            self.rect.centery += 2
        if press_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.right -= 2
        if press_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.left < 525:
            self.rect.right += 3

        else:
            pass