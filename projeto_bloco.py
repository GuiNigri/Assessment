import pygame
import random

#inicializaçao da fonte
pygame.font.init()
terminou = False

#definindo tela
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))

#definindo cores
amarelo = (255,255,0)
cyan = (0,255,255)
verde = (0,255,0)
preto = (0, 0, 0)
branco = (255, 255, 255)
azul = (0,0,156)
vermelho = (127,255,0)

cores = [amarelo,cyan,verde,vermelho,branco,azul]

    
def mostra_titulo():
    font = pygame.font.Font(None, 24)
    text = font.render("S1", 1 , preto)
    textpos = text.get_rect(centerx=tela.get_width()/2)
    tela.blit(text, textpos)



while not terminou:
    
    tela.fill(branco)
    mostra_titulo()
    
    # Checar os eventos do mouse aqui:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            terminou = True

    # Atualiza a tela
    pygame.display.update()
    
# Finaliza a janela do jogo
pygame.display.quit()
