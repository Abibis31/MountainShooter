#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key
import pygame
from pygame import joystick

from code.Const import PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, PLAYER_KEY_SHOOT, \
    ENITY_SHOT_DELAY
from code.Entity import Entity
from code.PlayerShot import PlayerShot


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENITY_SHOT_DELAY[self.name]


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
        pass

    def shoot(self, ):
        self.shot_delay-=1
        if self.shot_delay ==0:
            self.shot_delay =ENITY_SHOT_DELAY[self.name]
            pressed_key = pygame.key.get_pressed()
            if pressed_key[PLAYER_KEY_SHOOT[self.name]]:
                return PlayerShot(name = f'{self.name}_shot', position=(self.rect.centerx, self.rect.centery))
