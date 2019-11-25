import pygame
from mostrar_conteudo import *
branco  = (255,255,255)
preto = (0,0,0)
verde = (0,255,0)
azul = (0,0,156)
red = (255,0,0)
darkBlue = (2 , 24 , 89)
cores = [azul,red,darkBlue,preto]
conta_clocks = 0
conta_segundos = 0

def mostra_clock():
    font = pygame.font.Font(None,20)
    text = font.render("Clock:" + str(conta_clocks),1,preto)
    textpos = text.get_rect(center =(600,200))
    tela.blit(text, textpos)

def mostra_segundos():
    font = pygame.font.Font(None,20)
    text = font.render("Segundos:" + str(conta_segundos),1,preto)
    textpos = text.get_rect(center =(600,120))
    tela.blit(text, textpos)