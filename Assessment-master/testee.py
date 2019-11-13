import pygame
pygame.init()

LARGURA = 600
ALTURA = 800
tela = pygame.display.set_mode((ALTURA, LARGURA))
terminou = False


while not terminou:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
    
    
    pygame.display.update()
    
pygame.display.quit()

pygame.quit()