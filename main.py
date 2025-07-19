import pygame

print('Setup Start')
pygame.init()
window = pygame.display.set_mode(size = (600, 480))#inicializa a janela
print('Setup End')

print('Loop Start')
while True: #laço para manter a janela
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #Close Window
            quit() #End Pygame
