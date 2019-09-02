import pygame, random
from tabulate import tabulate
branco  = (255,255,255)
preto = (0,0,0)
pygame.mixer.init()

pygame.font.init()

largura_tela = 800

altura_tela = 600

tela = pygame.display.set_mode((largura_tela,altura_tela))

terminou = False

def mostra_titulo():
    font = pygame.font.Font(None,24)
    text = font.render("S1",1,preto)
    textpos = text.get_rect(centerx=tela.get_width()/2)
    tela.blit(text,textpos)
    
def mostrar_dados(texto,y):
    font = pygame.font.Font(None,20)
    text = font.render(texto, 1 ,preto)
    textpos = text.get_rect(center =(tela.get_width()/4 ,y))
    tela.blit(text,textpos)

def montar_tabela(texto,y):
    font = pygame.font.Font(None,20)
    text = font.render(texto, 1 ,preto)
    textpos = text.get_rect(center =(tela.get_width()/2 ,y))
    tela.blit(text,textpos)

while not terminou:

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

    print("ACME Inc.           Uso do espaço em disco pelos usuários",)
    print("------------------------------------------------------------------------")
    print("Nr.    Usuário        Espaço utilizado     % do uso")
    print("")
        
    for i in dicionario.keys():
        dicionario[i] = round(dicionario[i],2)
        porcentagem = round((dicionario[i]/soma)*100,2)
        print('{:^1}     {:<10}        {:>9,.2f}      {:>11,.2f}'.format(soma_indices, i, dicionario[i], porcentagem))
        soma_indices = soma_indices + 1

    print(" ")
    print("Total de memoria usada:", round(soma,2), "Mb")
    print("Media de memoria usada:", round(soma_media,2), "Mb")
    

    
    tela.fill(branco)
    mostra_titulo()
    montar_tabela("ACME Inc.           Uso do espaço em disco pelos usuários",50)
    montar_tabela("Nr.    Usuário        Espaço utilizado     % do uso", 100)
    mostrar_dados(dicionario, 30+soma_indices*10)
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
            pos = pygame.mouse.get_pos()
            if aba1.area.collidepoint(pos):
                
    
    pygame.display.update()
    
pygame.display.quit()
     
