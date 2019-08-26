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
    
def mostra_dados_pid(texto, y):
    font = pygame.font.Font(None, 24)
    text = font.render(texto, 1 , preto)
    textpos = text_rect.middle(justify=LEFT,y))
    tela.blit(text, textpos)
    



while not terminou:
    
    tela.fill(branco)
    mostra_titulo()
   # mostra_dados_pid()
    
    dicionario = {'alexandre': 456123789, 'anderson': 1245698456,
              'antonio': 123456456, 'carlos': 91257581,
              'cesar':987458, 'rosemary': 789456125 }

    valores_Bytes = dicionario.values()

    soma = sum(dicionario.values())
    soma = soma/1024/1024
    soma_media = soma/len(dicionario)
    soma_indices = 1

    for i in dicionario.keys():
        valor = dicionario[i]
        converter_mb = valor /1024/1024
        dicionario[i] = round(converter_mb,2)

    #text = font.render("ACME Inc.           Uso do espaço em disco pelos usuários")
    
    print("------------------------------------------------------------------------")
    print("Nr.    Usuário        Espaço utilizado     % do uso")
    print("")
        
    for i in dicionario.keys():
        
        dicionario[i] = round(dicionario[i],2)
        porcentagem = round((dicionario[i]/soma)*100,2)
        mostra_dados_pid(f'{soma_indices:^1}  {i:<10}        {dicionario[i]:>9,.2f}      {porcentagem:>11,.2f}', 60+soma_indices*30)
        soma_indices = soma_indices + 1

    print(" ")
    print("Total de memoria usada:", round(soma,2), "Mb")
    print("Media de memoria usada:", round(soma_media,2), "Mb")
    
    # Checar os eventos do mouse aqui:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            terminou = True

    # Atualiza a tela
    pygame.display.update()
    
# Finaliza a janela do jogo
pygame.display.quit()
