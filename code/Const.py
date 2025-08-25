import pygame
from pygame.examples.grid import WINDOW_HEIGHT

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0,128,0)
CYAN = (0,128,128)
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
    'nave_2_shot': 2,

    'ship_pixel_player1_shot': 3,
    'ship_pixel_player2_shot': 3,
}
ENTITY_HEALTH = {
    'level10':999,
    'level11':999,
    'level12':999,
    'level13':999,
    'level14':999,

    'ship_pixel_player1':150,
    'ship_pixel_player2':130,

    'nave_1': 50,
    'nave_2':65,

    'ship_pixel_player1_shot':1,
    'ship_pixel_player2_shot':5,
    'nave_1_shot':1,
    'nave_2_shot':2,
}
ENITY_SHOT_DELAY ={
    'ship_pixel_player1':13,
    'ship_pixel_player2':13,
    'nave_1':50,
    'nave_2':45,
}
ENTITY_DAMAGE ={
    'level10':0,
    'level11':0,
    'level12':0,
    'level13':0,
    'level14':0,

    'ship_pixel_player1':1,
    'ship_pixel_player2':1,

    'nave_1': 1,
    'nave_2':10,

    'ship_pixel_player1_shot':5,
    'ship_pixel_player2_shot':5,
    'nave_1_shot':2,
    'nave_2_shot':2,
}

ENTITY_SCORE = {
    'level10': 0,
    'level11': 0,
    'level12': 0,
    'level13': 0,
    'level14': 0,

    'ship_pixel_player1': 0,
    'ship_pixel_player2': 0,

    'nave_1': 10,
    'nave_2': 25,

    'ship_pixel_player1_shot': 0,
    'ship_pixel_player2_shot': 0,
    'nave_1_shot': 0,
    'nave_2_shot': 0,

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

