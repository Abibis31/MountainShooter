import pygame
from pygame.examples.grid import WINDOW_HEIGHT

WHITE = (255, 255, 255)

MENU_OPTIONS = ('NEW GAME 1P',
                'NEW GAME 2P - COOPERATIVE',
                'NEW GAME 2P - COMPETITIVE',
                'SCORE',
                'EXIT'

)
EVENT_ENEMY = pygame.USEREVENT + 1

ENTITY_SPEED = {
    'level10': 0,
    'level11': 0.01,
    'level12': 1,
    'level13': 2,
    'level14': 3,

    'nave_1': 2,
    'nave_2': 1.5,

    'nave_1_shot': 3,
    'nave_2_shot': 4,

    'ship_pixel_player1_shot': 3,
    'ship_pixel_player2_shot': 3,
}
ENTITY_HEALTH = {
    'level10':999,
    'level11':999,
    'level12':999,
    'level13':999,
    'level14':999,

    'ship_pixel_player1':300,
    'ship_pixel_player2':300,

    'nave_1': 55,
    'nave_2':65,

    'ship_pixel_player1_shot':1,
    'nave_1_shot':1,
    'nave_2_shot':2,
}
ENITY_SHOT_DELAY ={
    'ship_pixel_player1':13,
    'ship_pixel_player2':13,
    'nave_1':16,
    'nave_2':16,
}

PLAYER_KEY_UP = {'ship_pixel_player1':pygame.K_UP,
                'ship_pixel_player2': pygame.K_w}

PLAYER_KEY_DOWN={'ship_pixel_player1':pygame.K_DOWN,
                'ship_pixel_player2':pygame.K_s}

PLAYER_KEY_LEFT={'ship_pixel_player1':pygame.K_LEFT,
                'ship_pixel_player2':pygame.K_a}

PLAYER_KEY_RIGHT={'ship_pixel_player1':pygame.K_RIGHT,
                 'ship_pixel_player2':pygame.K_d}

PLAYER_KEY_SHOOT={'ship_pixel_player1':pygame.K_RCTRL,
                 'ship_pixel_player2':pygame.K_LCTRL}

SPAWN_TIME= 3000

WIN_HEIGHT = 324
WIN_WIDTH = 576

