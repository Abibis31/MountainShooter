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
EVENT_TIMEOUT = pygame.USEREVENT + 2

ENTITY_SPEED = {
    'level10': 0,
    'level11': 0.01,
    'level12': 1,
    'level13': 2,
    'level14': 3,

    'level20': 0.5,
    'level21': 1,
    'level22': 1.5,
    'level23': 2,


    'nave_1': 2,
    'nave_2': 1.5,
    'nave_3':1.5,

    'nave_1_shot': 3,
    'nave_2_shot': 2,
    'nave_3_shot':2.5,

    'ship_pixel_player1_shot': 3,
    'ship_pixel_player2_shot': 3,
}
ENTITY_HEALTH = {
    'level10':999,
    'level11':999,
    'level12':999,
    'level13':999,
    'level14':999,

    'level20': 999,
    'level21': 999,
    'level22': 999,
    'level23': 999,

    'ship_pixel_player1':130,
    'ship_pixel_player2':100,

    'nave_1': 50,
    'nave_2':65,
    'nave_3':50,

    'ship_pixel_player1_shot':1,
    'ship_pixel_player2_shot':5,
    'nave_1_shot':1,
    'nave_2_shot':2,
    'nave_3_shot':2
}
ENITY_SHOT_DELAY ={
    'ship_pixel_player1':10,
    'ship_pixel_player2':13,
    'nave_1':50,
    'nave_2':45,
    'nave_3':38
}
ENTITY_DAMAGE ={
    'level10':0,
    'level11':0,
    'level12':0,
    'level13':0,
    'level14':0,

    'level20': 0,
    'level21': 0,
    'level22': 0,
    'level23': 0,

    'ship_pixel_player1':1,
    'ship_pixel_player2':1,

    'nave_1': 1,
    'nave_2':10,
    'nave_3':55,

    'ship_pixel_player1_shot':5,
    'ship_pixel_player2_shot':5,

    'nave_1_shot':15,
    'nave_2_shot':25,
    'nave_3_shot':45
}

ENTITY_SCORE = {
    'level10': 0,
    'level11': 0,
    'level12': 0,
    'level13': 0,
    'level14': 0,
    'level20': 0,
    'level21': 0,
    'level22': 0,
    'level23': 0,

    'ship_pixel_player1': 0,
    'ship_pixel_player2': 0,

    'nave_1': 10,
    'nave_2': 25,
    'nave_3':50,

    'ship_pixel_player1_shot': 0,
    'ship_pixel_player2_shot': 0,
    'nave_1_shot': 0,
    'nave_2_shot': 0,
    'nave_3_shot':0

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

SPAWN_TIME= 500


SPAWN_TIME_2 = 1500 #100ms
TIMEOUT_LEVEL = 50000


WIN_HEIGHT = 324
WIN_WIDTH = 576

SCORE_POS = {
    'Title':(WIN_WIDTH / 2, 50),
    'Enter Name':(WIN_WIDTH / 2, 80),
    'Label':(WIN_WIDTH / 2, 90),
    'Name':(WIN_WIDTH / 2, 110),
    0:(WIN_WIDTH / 2, 110),
    1:(WIN_WIDTH / 2, 130),
    2:(WIN_WIDTH / 2, 150),
    3:(WIN_WIDTH / 2, 170),
    4:(WIN_WIDTH / 2, 190),
    5:(WIN_WIDTH / 2, 210),
    6:(WIN_WIDTH / 2, 230),
    7:(WIN_WIDTH / 2, 250),
    8:(WIN_WIDTH / 2, 270),
    9:(WIN_WIDTH / 2, 290),
}

