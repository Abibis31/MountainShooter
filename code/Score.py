from datetime import datetime

import pygame
from pygame import Surface, KEYDOWN, K_RETURN, K_BACKSPACE, K_ESCAPE
from pygame.font import Font
from pygame.rect import Rect

from code.Const import WHITE, SCORE_POS, MENU_OPTIONS
from code.DBProxy import DBProxy


class Score:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('assets/bodys/Level1/score.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def save(self, game_mode: str, player_score: list[int]):

        pygame.mixer_music.load('assets/MUSICS/menu_music.mp3')  # buscando music
        pygame.mixer_music.play(-1)  # o menos um e para fazer um loop´na music
        db_proxy = DBProxy('DBScore')
        name = ''


        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(48, 'YOU WIN!!', (255, 255, 0), SCORE_POS['Title'] )


            if  game_mode == MENU_OPTIONS[0]:
                score = player_score[0]
                text = 'Enter Player1 name (4 characters):'

            if  game_mode == MENU_OPTIONS[1]:
                score = (player_score[0]+ player_score[1]) /2
                text = 'Enter Team name (4 characters):'

            if  game_mode == MENU_OPTIONS[2]:
                if player_score[0] >= player_score[1]:
                    score = player_score[0]
                    text = 'Enter Player1 name (4 characters):'
                else:
                    score = player_score[1]
                    text = 'Enter Player2 name (4 characters):'

            self.score_text(20, text , WHITE, SCORE_POS['Enter Name'] )
            pygame.display.flip()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) == 4:
                        db_proxy.save({'name': name, 'score': score, 'date':get_formatted_date()})
                        self.show()
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) <4:
                            name += event.unicode
            self.score_text(20, name, WHITE, SCORE_POS['Name'])

            pygame.display.flip()
    def show(self):
        pygame.mixer_music.load('assets/MUSICS/menu_music.mp3')  # buscando music
        pygame.mixer_music.play(-1)  # o menos um e para fazer um loop´na music


       # self.score_text(48, 'TOP 10 SCORE', (255, 255, 0), SCORE_POS['Title'])
       # self.score_text(20, 'NAME     SCORE     DATE', (255, 255, 0), SCORE_POS['Label'])
        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(48, 'TOP 10 SCORE', (255, 255, 0), SCORE_POS['Title'])
            self.score_text(20, 'NAME         SCORE         DATE', (255, 255, 0), SCORE_POS['Label'])
            for player_score in list_score:
                id_, name, score, date = player_score
                self.score_text(20, f'           {name}         {score :05d}         {date}',WHITE,
                            SCORE_POS[list_score.index(player_score)])



            #pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return

    pygame.display.flip()
    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        # Carrega a fonte do sistema (note o 'F' maiúsculo em SysFont)
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)

        # Renderiza o texto com antialiasing (suavização) e converte para alpha
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()

        # Obtém o retângulo (Rect) do texto e centraliza na posição especificada
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)

        # Desenha o texto na janela (note que 'dest' é opcional como argumento nomeado)
        self.window.blit(source=text_surf, dest=text_rect)



def get_formatted_date():
    current_datetime = datetime.now()
    concurrent_time = current_datetime.strftime('%H:%M')
    concurrent_date = current_datetime.strftime('%d/%m/%y')
    return  f'{concurrent_time} - {concurrent_date}'










