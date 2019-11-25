import pygame,sys,os, time,psutil, netifaces, socket
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
altura_tela = 1024

tela = pygame.display.set_mode((largura_tela,altura_tela))
lista = os.listdir("./")

dic = {}
dic2 = {}
formato = "%d/%m/%Y %H:%M:%S"


for arquivos in lista:
    if os.path.isfile(arquivos):
        dic[arquivos] = []
        timestamp_criacao = os.stat(arquivos).st_atime
        timestamp_modificacao = os.stat(arquivos).st_mtime
        data_criacao = time.strftime(formato, time.localtime(timestamp_criacao))
        data_mod = time.strftime(formato, time.localtime(timestamp_modificacao))
        dic[arquivos].append(os.stat(arquivos).st_size)
        dic[arquivos].append(data_criacao)
        dic[arquivos].append(data_mod)

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
    
def pega_processos(tipo):
        if tipo == "somas":
            soma_vms = 0
            soma_rss = 0
            for proc in psutil.process_iter():
                if proc.status() == 'running':
                    soma_vms += round(proc.memory_info().vms/1024/1024,2)
                    soma_rss += round(proc.memory_info().rss/1024/1024,2)
            return soma_vms, soma_rss
                
        if tipo == "grafico_vms":
            lista_pid = []
            lista_vms = []
            for proc in psutil.process_iter():
                lista_pid.append(proc.pid)
                lista_vms.append(proc.memory_info().vms)
            return lista_pid, lista_vms
        
        if tipo == "grafico_rss":
            lista_pid = []
            lista_rss = []
            for proc in psutil.process_iter():
                lista_pid.append(proc.pid)
                lista_rss.append(proc.memory_info().rss)
            return lista_pid, lista_rss
        
def desenha_grafico(tipo):
    import matplotlib
    import matplotlib.pyplot as plt
    matplotlib.use("Agg")
    import matplotlib.backends.backend_agg as agg
    lista_p, lista_v = pega_processos(tipo)
    names = lista_p
    values = lista_v
    
    fig, axs = plt.subplots()
    axs.plot(names, values)
    
    if(tipo=="grafico_vms"):
        fig.suptitle('Uso de memoria VMS')
        canvas = agg.FigureCanvasAgg(fig)
        canvas.draw()
        size = canvas.get_width_height()
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_rgb()
        surf = pygame.image.fromstring(raw_data, size, "RGB")
        tela.blit(surf, (100,70))
    else:
        fig.suptitle('Uso de memoria RSS')
        canvas = agg.FigureCanvasAgg(fig)
        canvas.draw()
        size = canvas.get_width_height()
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_rgb()
        surf = pygame.image.fromstring(raw_data, size, "RGB")
        tela.blit(surf, (100,550))
    
def obtem_nome_familia(familia):
    if familia == socket.AF_INET:
         return("IPv4")
    elif familia == socket.AF_INET6:
        return("IPv6")
    else:
        return("-")
def obtem_tipo_socket(tipo):
    if tipo == socket.SOCK_STREAM:
        return("TCP")
    elif tipo == socket.SOCK_DGRAM:
        return("UDP")
    elif tipo == socket.SOCK_RAW:
        return("IP")
    else:
        return("-")    
    

def conteudo_aba1():
    soma_percent = 0
    soma_indices = 0

    try:
        soma_v, soma_r = pega_processos("somas")
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
                montar_tabela(f'{round(vms/round(soma_v,2),4)} %',450,220+soma_indices*20)
                montar_tabela(f'{round(rss/round(soma_r,2),4)} %',550,220+soma_indices*20)
                soma_indices = soma_indices + 1
    except psutil.NoSuchProcess:
        pass
        
    montar_tabela(f'Total de uso do sistema: {soma_percent/100}  %',10,150)
    montar_tabela(f'Total de uso do vms: {round(soma_v,2)}  MB',10,130)
    montar_tabela(f'Total de uso do rss: {round(soma_r,2)}  MB',10,110)
    

 
    montar_tabela("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",0,175)
    montar_tabela("pid",10,190)
    montar_tabela("rms",70,190)
    montar_tabela("vms",250,190)
    montar_tabela("rss",350,190)
    montar_tabela("% do vms",450,190)
    montar_tabela("% do rss",550,190)
    
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
    teste = 0
    soma_indices = 0
    espacamento = 0
    interfaces = psutil.net_if_addrs()
    identifica_ip_router = netifaces.gateways()
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
        soma_indices = soma_indices + 1
    dados_de_rede = psutil.net_io_counters()
    pids = psutil.pids()
    montar_tabela(f'PID          End.         Tipo        Status                Endereço Local          Porta L.         Endereço Remoto        Porta R.',5,400)
    for p in pids:
        try:
            processo = psutil.Process(p)
            conn = processo.connections()
            if conn:
                montar_tabela(f'{p}',5,415+espacamento*15)
                montar_tabela(f'{obtem_nome_familia(conn[0][1])}',68,415+espacamento*15)
                montar_tabela(f'{obtem_tipo_socket(conn[0][2])}',135,415+espacamento*15)
                montar_tabela(f'{conn[0][5]}',190,415+espacamento*15)
                montar_tabela(f'{conn[0][3][0]}',295,415+espacamento*15)
                montar_tabela(f'{conn[0][3][1]}',435,415+espacamento*15)
                if len(conn[0][4]) != 0 : 
                    montar_tabela(f'{conn[0][4][0]}',520,415+teste*15)
                    montar_tabela(f'{conn[0][4][1]}',675,415+teste*15)
                    teste +=1

                espacamento += 1 
        except psutil.NoSuchProcess:
            pass
            
def conteudo_aba3():
    desenha_grafico("grafico_vms")
    desenha_grafico("grafico_rss")


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
