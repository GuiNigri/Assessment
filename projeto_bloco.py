import pygame, random
branco  = (255,255,255)
preto = (0,0,0)
verde = (0,255,0)
azul = (0,0,156)
red = (255,0,0)
darkBlue = (2 , 24 , 89)
cores = [azul,red,darkBlue,preto]


pygame.mixer.init()

pygame.font.init()

largura_tela = 800
altura_tela = 600

tela = pygame.display.set_mode((largura_tela,altura_tela))

terminou = False

class Aba():
    def __init__(self,aba_type,cor):
        self.largura = 200
        self.altura = 60
        self.x = 200 * aba_type
        self.y = 0
        self.area = pygame.Rect(self.x,self.y,self.largura,self.altura)
        self.cor = cores[aba_type]
    def desenha(self, tela):
        pygame.draw.rect(tela,self.cor,self.area)

def mostra_titulo(texto,x,y):
    font = pygame.font.Font(None,24)
    text = font.render(texto,1,preto)
    textpos = text.get_rect(center=(x,y) )
    tela.blit(text,textpos)
    
def mostrar_dados(texto,x,y):
    font = pygame.font.Font(None,20)
    text = font.render(texto, 1 ,preto)
    textpos = text.get_rect(center =(x,y))
    tela.blit(text,textpos)

def montar_tabela(texto,x,y):
    font = pygame.font.Font(None,20)
    text = font.render(texto, 1 ,preto)
    textpos = text.get_rect(center =(x,y))
    tela.blit(text,textpos)

def mostra_titulo_aba(texto,x):
    font = pygame.font.Font(None,20)
    text = font.render(texto,1,branco)
    textpos = text.get_rect(center =(x,30))
    tela.blit(text, textpos)
def cria_abas():
    lista_de_abas = []
    for i in range(0,4):
        aba = Aba(i,cores)
        aba.desenha(tela)
        lista_de_abas.append(aba)
        mostra_titulo_aba(f"ABA {i}", (largura_tela/4 *i)+100)
    return lista_de_abas

clock = pygame.time.Clock()

conta_clocks = 0

tela.fill(branco)
aba0,aba1,aba2,aba3 =  cria_abas()

while not terminou:

    dicionario = {'alexandre': 456123789, 'anderson': 1245698456,
              'antonio': 123456456, 'carlos': 91257581,
              'cesar':987458, 'rosemary': 789456125 }
    
    conta_clocks = conta_clocks + 1
    
    lista_de_dicionario = [{'rss': 113979392, 'vms': 114520064, 'pid': 88, 'nome': 'Registry', 'percento': 379.85},
                           {'rss': 35794944, 'vms': 20525056, 'pid': 948, 'nome': 'chrome.exe', 'percento': 50.7},
                           {'rss': 34332672, 'vms': 17887232, 'pid': 984, 'nome': 'svchost.exe', 'percento': 44.54},
                           {'rss': 255979520, 'vms': 22016000, 'pid': 1012, 'nome': 'fontdrvhost.exe', 'percento': 977.67},
                           {'rss': 35188736, 'vms': 25378816, 'pid': 1708, 'nome': 'svchost.exe', 'percento': 48.14},
                           {'rss': 25681920, 'vms': 7020544, 'pid': 2300, 'nome': 'ApplicationFrameHost.exe', 'percento': 8.12},
                           {'rss': 64212992, 'vms': 30863360, 'pid': 2372, 'nome': 'MicrosoftEdge.exe', 'percento': 170.34},
                           {'rss': 26263552, 'vms': 6246400, 'pid': 2448, 'nome': 'MicrosoftEdgeCP.exe', 'percento': 10.57},
                           {'rss': 114982912, 'vms': 154681344, 'pid': 2628, 'nome': 'MsMpEng.exe', 'percento': 384.08},
                           {'rss': 25030656, 'vms': 9220096, 'pid': 4024, 'nome': 'svchost.exe', 'percento': 5.38},
                           {'rss': 37093376, 'vms': 20942848, 'pid': 4116, 'nome': 'SkypeApp.exe', 'percento': 56.16},
                           {'rss': 56758272, 'vms': 42430464, 'pid': 4760, 'nome': 'svchost.exe', 'percento': 138.95},
                           {'rss': 45293568, 'vms': 24764416, 'pid': 5328, 'nome': 'vmware-hostd.exe', 'percento': 90.69},
                           {'rss': 124157952, 'vms': 55316480, 'pid': 5400, 'nome': 'explorer.exe', 'percento': 422.7},
                           {'rss': 24948736, 'vms': 5890048, 'pid': 5432, 'nome': 'sihost.exe', 'percento': 5.03},
                           {'rss': 34627584, 'vms': 8003584, 'pid': 6560, 'nome': 'svchost.exe', 'percento': 45.78},
                           {'rss': 79331328, 'vms': 33001472, 'pid': 6644, 'nome': 'ShellExperienceHost.exe', 'percento': 233.98},
                           {'rss': 118439936, 'vms': 61276160, 'pid': 7024, 'nome': 'SearchUI.exe', 'percento': 398.63},
                           {'rss': 80060416, 'vms': 55767040, 'pid': 7052, 'nome': 'chrome.exe', 'percento': 237.05},
                           {'rss': 170975232, 'vms': 144072704, 'pid': 7468, 'nome': 'chrome.exe', 'percento': 619.8},
                           {'rss': 78249984, 'vms': 47955968, 'pid': 7520, 'nome': 'thonny.exe', 'percento': 229.43},
                           {'rss': 36786176, 'vms': 21307392, 'pid': 7628, 'nome': 'chrome.exe', 'percento': 54.87},
                           {'rss': 102436864, 'vms': 77463552, 'pid': 7776, 'nome': 'chrome.exe', 'percento': 331.26},
                           {'rss': 70623232, 'vms': 133386240, 'pid': 7868, 'nome': 'chrome.exe', 'percento': 197.32},
                           {'rss': 125968384, 'vms': 63152128, 'pid': 7900, 'nome': 'chrome.exe', 'percento': 430.32},
                           {'rss': 47972352, 'vms': 31125504, 'pid': 8384, 'nome': 'Microsoft.Photos.exe', 'percento': 101.96},
                           {'rss': 48463872, 'vms': 38649856, 'pid': 9120, 'nome': 'dwm.exe', 'percento': 104.03},
                           {'rss': 192319488, 'vms': 167886848, 'pid': 9220, 'nome': 'chrome.exe', 'percento': 709.66},
                           {'rss': 67276800, 'vms': 41480192, 'pid': 9784, 'nome': 'chrome.exe', 'percento': 183.23},
                           {'rss': 60825600, 'vms': 35332096, 'pid': 9972, 'nome': 'chrome.exe', 'percento': 156.07}]
    
    
    
    valores_Bytes = dicionario.values()

    soma = sum(dicionario.values())
    soma = soma/1024/1024
    soma_media = soma/len(dicionario)
    soma_indices = 1

    for i in dicionario.keys():
        valor = dicionario[i]
        converter_mb = valor /1024/1024
        dicionario[i] = round(converter_mb,2)

    #print("ACME Inc.           Uso do espaço em disco pelos usuários",)
    #print("------------------------------------------------------------------------")
    #print("Nr.    Usuário        Espaço utilizado     % do uso")
    #print("")
        
    for i in dicionario.keys():
        dicionario[i] = round(dicionario[i],2)
        porcentagem = round((dicionario[i]/soma)*100,2)
        #print('{:^1}     {:<10}        {:>9,.2f}      {:>11,.2f}'.format(soma_indices, i, dicionario[i], porcentagem))
        #soma_indices = soma_indices + 1

    #print(" ")
    #print("Total de memoria usada:", round(soma,2), "Mb")
    #print("Media de memoria usada:", round(soma_media,2), "Mb")
    

    
    for event in pygame.event.get():
        aba_setada = "null"
        if event.type == pygame.QUIT:
            terminou = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
            pos = pygame.mouse.get_pos()
            if aba0.area.collidepoint(pos):
                tela.fill(branco)
                aba0, aba1, aba2, aba3 = cria_abas()
                mostra_titulo("ACME Inc.           Uso do espaço em disco pelos usuários",400,150)
                montar_tabela("------------------------------------------------------------------------",400,175)
                montar_tabela("pid",210,200)
                montar_tabela("rms",300,200)
                montar_tabela("vms",470,200)
                montar_tabela("% do uso",550,200)
                """montar_tabela("1",200,150+soma_indices*10),montar_tabela("alexandre",300,150+soma_indices*10),montar_tabela("456123789",450,150+soma_indices*10)
                montar_tabela("2",200,170+soma_indices*10),montar_tabela("anderson",300,170+soma_indices*10),montar_tabela("1245698456",450,170+soma_indices*10)
                montar_tabela("3",200,190+soma_indices*10),montar_tabela("antonio",300,190+soma_indices*10),montar_tabela("123456456",450,190+soma_indices*10)
                montar_tabela("4",200,210+soma_indices*10),montar_tabela("carlos",300,210+soma_indices*10),montar_tabela("91257581",450,210+soma_indices*10)
                montar_tabela("5",200,230+soma_indices*10),montar_tabela("cesar",300,230+soma_indices*10),montar_tabela("987458",450,230+soma_indices*10)
                montar_tabela("5",200,250+soma_indices*10),montar_tabela("rosemary",300,250+soma_indices*10),montar_tabela("789456125",450,250+soma_indices*10)"""
                
                for item in lista_de_dicionario:
                    montar_tabela(f'{item["pid"]:^20}       {item["nome"]:<20}          {item["vms"]+1:>13}         {item["rss"]:>13}',400,200+soma_indices*25)
                    soma_indices = soma_indices + 1
                aba_setada = aba_setada_0
                    
            if aba1.area.collidepoint(pos):
                tela.fill(branco)
                aba0, aba1, aba2, aba3 = cria_abas()
                aba_setada = "aba_setada_1"

            if aba2.area.collidepoint(pos):
                tela.fill(branco)
                aba0, aba1, aba2, aba3 = cria_abas()
                aba_setada = "aba_setada_2"
            if aba3.area.collidepoint(pos):
                tela.fill(branco)
                aba0, aba1, aba2, aba3 = cria_abas()
                aba_setada = "aba_setada_3"
                
    if aba_setada == "aba_setada_1":
        tela.fill(branco)
        for i in range(conta_clocks):
            tela.fill(branco)
            mostra_titulo(str(conta_clocks),400,200)
            aba0, aba1, aba2, aba3 = cria_abas()
    if aba_setada == "aba_setada_2":
        tela.fill(branco)
        for i in range(conta_clocks):
            tela.fill(branco)
            mostra_titulo(str(conta_clocks),400,200)
            aba0, aba1, aba2, aba3 = cria_abas()
    if aba_setada == "aba_setada_3":
        tela.fill(branco)
        for i in range(conta_clocks):
            tela.fill(branco)
            mostra_titulo(str(conta_clocks),400,200)
            aba0, aba1, aba2, aba3 = cria_abas()
                
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True

    pygame.display.update()
    clock.tick(20)
    
pygame.display.quit()
     





