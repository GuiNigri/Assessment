import pygame,sys,os, time,psutil, netifaces
from datetime import datetime , timedelta
from pytz import timezone 
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
altura_tela = 900

tela = pygame.display.set_mode((largura_tela,altura_tela))
lista = os.listdir("./")

dic = {}
dic2 = {}
formato = "%d/%m/%Y %H:%M:%S"


for i in lista:
    if os.path.isfile(i):
        dic[i] = []
        timestamp_criacao = os.stat(i).st_atime
        timestamp_modificacao = os.stat(i).st_mtime
        data_criacao = time.strftime(formato, time.localtime(timestamp_criacao))
        data_mod = time.strftime(formato, time.localtime(timestamp_modificacao))
        dic[i].append(os.stat(i).st_size)
        dic[i].append(data_criacao)
        dic[i].append(data_mod)
print(dic)

titulo = '{:11}'.format("Tamanho") # 10 caracteres + 1 de espaço
# Concatenar com 25 caracteres + 2 de espaços
titulo = titulo + '{:27}'.format("Data de Modificação")
# Concatenar com 25 caracteres + 2 de espaços
titulo = titulo + '{:27}'.format("Data de Criação")
titulo = titulo + "Nome"
#print(titulo)

terminou = False

class Linha():
    def __init__(self,x,y):
        self.pontos = (x,y)      
        self.cor = preto
    def desenha(self,tela):
        pygame.draw.polygon(tela,self.cor,self.pontos,1)

class Aba():
    def __init__(self,aba_type,cor):
        self.largura = 200
        self.altura = 60
        self.x = 200 * aba_type
        self.y = 0
        self.area = pygame.Rect(self.x,self.y,self.largura,self.altura)
        self.cor = cores[aba_type]
    def desenha(self,tela):
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
    textpos.left = x
    tela.blit(text,textpos)

def mostra_titulo_aba(texto,x):
    font = pygame.font.Font(None,20)
    text = font.render(texto,1,branco)
    textpos = text.get_rect(center =(x,30))
    tela.blit(text, textpos)
    
def cria_abas():
    lista_de_abas = []
    for a in range(0,4):
        aba = Aba(a,cores)
        aba.desenha(tela)
        lista_de_abas.append(aba)
        mostra_titulo_aba(f"ABA {a}", (largura_tela/4 *a)+100)
    return lista_de_abas

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
    

def conteudo_aba1():
    soma_vms = 0
    soma_rss = 0
    soma_percent = 0
    soma_indices = 0
    try:
        for processos in psutil.process_iter():
            if processos.status() == 'running':
                soma_vms += round(processos.memory_info().vms/1024/1024,2)
                soma_rss += round(processos.memory_info().rss/1024/1024,2)
        #print(soma_vms)
        lista_processos_ordenados = []
        for elemento in sorted(psutil.process_iter(), key=lambda x : x.memory_info().rss, reverse = True):
            lista_processos_ordenados.append(elemento)
        for p in lista_processos_ordenados:
            if p.status() == 'running':
                pid = p.pid
                nome = p.name()
                rss = p.memory_info().rss/1024/1024
                vms = p.memory_info().vms/1024/1024
                status = p.status()
                montar_tabela(f'{pid}',10,220+soma_indices*20)
                montar_tabela(f'{nome}',70,220+soma_indices*20)
                montar_tabela(f'{round(vms,2)} MB',250,220+soma_indices*20)
                montar_tabela(f'{round(rss,2)} MB',350,220+soma_indices*20)
                montar_tabela(f'{round(vms/round(soma_vms,2),4)} %',450,220+soma_indices*20)
                montar_tabela(f'{round(rss/round(soma_rss,2),4)} %',550,220+soma_indices*20)
                soma_indices = soma_indices + 1
    except psutil.NoSuchProcess:
        pass
        
    montar_tabela(f'Total de uso do sistema: {soma_percent/100}  %',10,150)
    montar_tabela(f'Total de uso do vms: {round(soma_vms,2)}  MB',10,130)
    montar_tabela(f'Total de uso do rss: {round(soma_rss,2)}  MB',10,110)
    

 
    montar_tabela("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",0,175)
    montar_tabela("pid",10,190)
    montar_tabela("rms",70,190)
    montar_tabela("vms",250,190)
    montar_tabela("rss",350,190)
    montar_tabela("% do vms",450,190)
    montar_tabela("% do rss",550,190)
    """for item in lista_de_dicionario:
        montar_tabela(f'{item["pid"]}',10,155+soma_indices*20)
        montar_tabela(f'{item["nome"]}',50,155+soma_indices*20)
        montar_tabela(f'{round(item["vms"]/1024/1024,2)} MB',200,155+soma_indices*20)
        montar_tabela(f'{round(item["rss"]/1024/1024,2)} MB',300,155+soma_indices*20)
        montar_tabela(f'{round(item["vms"]/round(soma_vms/1024/1024,2)/100,2)} %',400,155+soma_indices*20)
        montar_tabela(f'{round(item["rss"]/round(soma_rss/1024/1024,2)/100,2)} %',500,155+soma_indices*20)
        soma_indices = soma_indices + 1
    montar_tabela(f'Total de uso do sistema: {round(soma_percent/100,2)}  %',200,(200)+50)
    montar_tabela(f'Total de uso do vms: {round(soma_vms/1024/1024,2)}  MB',200,(200)+30)
    montar_tabela(f'Total de uso do rss: {round(soma_rss/1024/1024,2)}  MB',200,(200)+10)"""
    
def conteudo_aba0():
    posx = 10
    soma_indices = 0  
    montar_tabela("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",0,130)
    montar_tabela("Tamanho",10,190)
    montar_tabela("Criação",posx+90,190)
    montar_tabela("Modificação",posx+290,190)
    montar_tabela("Nome do arquivo",posx+470,190)
    
    lista = os.listdir()
    
    soma_tamanho = 0
    for i in dic:
        soma_tamanho = soma_tamanho + dic[i][0]
    for i in lista: # Varia na lista dos arquivos e diretórios
        if os.path.isfile(i): # checa se é um arquivo
            kb = (dic[i][0]/1024)
            tamanho = '{:10}'.format(str('{:.2f}'.format(kb)+' KB'))
            montar_tabela(f'{tamanho}', posx, 220+soma_indices*20) # Tamanho
            montar_tabela(f'{dic[i][1]}', posx+90, 220+soma_indices*20) # Tempo de criação
            montar_tabela(f'{dic[i][2]}', posx+290, 220+soma_indices*20) # Tempo de modificação
            montar_tabela(f'{i}',posx+470,220+soma_indices*20)
            soma_indices = soma_indices + 1
    montar_tabela(f'Tamanho total dos arquivos: {round((soma_tamanho/1024),2)} KB',posx,(220+soma_indices*20))
    montar_tabela(f'Média de tamanho  dos arquivos: {round((soma_tamanho/len(tamanho)/1024),2)} KB',posx,(240+soma_indices*20))
    

def conteudo_aba2():
    soma_indices = 0
    interfaces = psutil.net_if_addrs()
    #print(interfaces)
    #print(interfaces)
   #nomes = []
    """for nome_da_rede in interfaces:
        nomes.append(str(nome_da_rede))
    print(nomes)"""
    identifica_ip_router = netifaces.gateways()
    #print(identifica_ip_router)
    for i, j in identifica_ip_router.items():
        try:
            gat = j[2][0]
        except:
            pass
    montar_tabela("Nome da Rede", 5,200)
    montar_tabela("Endereço Ip da Rede", 200,200)
    montar_tabela("Mascara de Rede", 350,200)
    montar_tabela("Gateway: ", 5,160)
    montar_tabela(gat, 85,160)
    for nome_rede, info_rede in interfaces.items():
        montar_tabela(f'{nome_rede}',5,220+soma_indices*20)
        #Endereço_IP
        montar_tabela(f'{info_rede[1][1]}',200,220+soma_indices*20)
        #mascara
        montar_tabela(f'{info_rede[1][2]}',350,220+soma_indices*20)
        #for j in interfaces[i]:
            #montar_tabela("\t"+str(j),5,300+soma_indices*20)
        soma_indices = soma_indices + 1
            
def conteudo_aba3():
    import matplotlib
    import matplotlib.pyplot as plt
    matplotlib.use("Agg")
    import matplotlib.backends.backend_agg as agg
    data = {'System Idle Process': 53248, 'System': 212992, 'Registry': 109453312, 'svchost.exe': 8384512, 'fontdrvhost.exe': 10928128, 'smss.exe': 499712, 'chrome.exe': 1974272, 'csrss.exe': 2220032, 'conhost.exe': 5558272, 'wininit.exe': 1368064, 'winlogon.exe': 2277376, 'services.exe': 5570560, 'lsass.exe': 6852608, 'unsecapp.exe': 1343488, 'dwm.exe': 55586816, 'audiodg.exe': 10899456, 'igfxCUIService.exe': 2052096, 'sihost.exe': 6144000, 'taskhostw.exe': 6189056, 'atiesrxx.exe': 1363968, 'atieclxx.exe': 1806336, 'WmiPrvSE.exe': 9449472, 'Memory Compression': 32768,}
            #'vmware-authd.exe': 5914624, 'AGMService.exe': 2404352, 'vmnat.exe': 2740224, 'RtkAudioService64.exe': 1789952, 'SearchFilterHost.exe': 1437696, 'AGSService.exe': 3035136, 'AERTSr64.exe': 663552, 'MicrosoftEdgeCP.exe': 5287936, 'RuntimeBroker.exe': 5890048, 'spoolsv.exe': 5771264, 'armsvc.exe': 1396736, 'explorer.exe': 49389568, 'vmnetdhcp.exe': 7983104, 'MsMpEng.exe': 160911360, 'SecurityHealthService.exe': 4235264, 'mysqld.exe': 370147328, 'RAVBg64.exe': 5873664, 'ctfmon.exe': 4661248, 'w.exe': 5083136, 'SkypeApp.exe': 19021824, 'cmd.exe': 3817472, 'SearchUI.exe': 66932736, 'FileCoAuth.exe': 2002944, 'ShellExperienceHost.exe': 30146560, 'igfxEM.exe': 3600384, 'igfxHK.exe': 2379776, 'MicrosoftEdge.exe': 26021888, 'python.exe': 12304384, 'thonny.exe': 50040832, 'SgrmBroker.exe': 2351104, 'ApplicationFrameHost.exe': 10018816, 'browser_broker.exe': 2023424, 'MSASCuiL.exe': 1994752, 'dllhost.exe': 1581056, 'PresentationFontCache.exe': 26099712, 'GoogleCrashHandler.exe': 1699840, 'GoogleCrashHandler64.exe': 1781760, 'SearchProtocolHost.exe': 2465792, 'RtkNGUI64.exe': 4902912, 'SearchIndexer.exe': 43053056, 'MOM.exe': 28057600, 'vmware-tray.exe': 4071424, 'CCC.exe': 77570048, 'NisSrv.exe': 4374528}
    names = list(data.keys())
    values = list(data.values())

    fig, axs = plt.subplots()
    axs.bar(names, values)
    fig.suptitle('Categorical Plotting')

    canvas = agg.FigureCanvasAgg(fig)
    canvas.draw()
    size = canvas.get_width_height()
    renderer = canvas.get_renderer()
    raw_data = renderer.tostring_rgb()

    surf = pygame.image.fromstring(raw_data, size, "RGB")
    tela.blit(surf, (0,0))


clock = pygame.time.Clock()

conta_clocks = 0
conta_segundos = 0

tela.fill(branco)
aba0,aba1,aba2,aba3 =  cria_abas()
aba_setada = "aba_setada_3"
conteudo_aba3()

while True:   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
            pos = pygame.mouse.get_pos()
            if aba0.area.collidepoint(pos):
                tela.fill(branco)
                aba0, aba1, aba2, aba3 = cria_abas()
                aba_setada = "aba_setada_0"
                    
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
       
    conta_clocks +=1
    
    if conta_clocks == 50:
        if conta_segundos>=0:
            conta_segundos+=1
        conta_clocks = 0
        tela.fill(branco)
        aba0, aba1, aba2, aba3 = cria_abas()  
        if aba_setada == "aba_setada_0":
            mostra_segundos()
            conteudo_aba0()  
        if aba_setada == "aba_setada_1":
            mostra_segundos()
            conteudo_aba1()
        if aba_setada == "aba_setada_2":
            mostra_segundos()
            conteudo_aba2()
        if aba_setada == "aba_setada_3":
            mostra_segundos()
            conteudo_aba3()
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()
    clock.tick(50)
    
pygame.display.quit()
