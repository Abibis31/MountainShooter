#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractclassmethod, abstractmethod
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./assets/bodys/Level1/'+ name + '.png')
        self.rect = self.surf.get_rect(left= position[0], top=position[1])
        self.speed = 0


    @abstractmethod
    def move(self, ):
        pass
