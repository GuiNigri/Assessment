import psutil, pygame
from mostrar_conteudo import *
def pega_processos(tipo):
        if tipo == "somas":
            soma_vms = 0
            soma_rss = 0
            for proc in psutil.process_iter():
                if proc.status() == 'running':
                    soma_vms += round(proc.memory_info().vms/1024/1024,2)
                    soma_rss += round(proc.memory_info().rss/1024/1024,2)
            return soma_vms, soma_rss
                
        if tipo == "grafico":
            lista_pid = []
            lista_vms = []
            for proc in psutil.process_iter():
                lista_pid.append(proc.pid)
                lista_vms.append(proc.memory_info().vms)
            return lista_pid, lista_vms
            
def desenha_grafico_vms():
    import matplotlib
    import matplotlib.pyplot as plt
    matplotlib.use("Agg")
    import matplotlib.backends.backend_agg as agg
    lista_p, lista_v = pega_processos("grafico")
    names = lista_p
    values = lista_v

    fig, axs = plt.subplots()
    axs.plot(names, values)
    fig.suptitle('Categorical Plotting')

    canvas = agg.FigureCanvasAgg(fig)
    canvas.draw()
    size = canvas.get_width_height()
    renderer = canvas.get_renderer()
    raw_data = renderer.tostring_rgb()

    surf = pygame.image.fromstring(raw_data, size, "RGB")
    tela.blit(surf, (100,150))
    
def captura_processos(tipo):
        if tipo == "somas":
            soma_vms = 0
            soma_rss = 0
            for proc in psutil.process_iter():
                if proc.status() == 'running':
                    soma_vms += round(proc.memory_info().vms/1024/1024,2)
                    soma_rss += round(proc.memory_info().rss/1024/1024,2)
            return soma_vms, soma_rss
                
        if tipo == "grafico":
            lista_pid = []
            lista_rss = []
            for proc in psutil.process_iter():
                lista_pid.append(proc.pid)
                lista_rss.append(proc.memory_info().rss)
            return lista_pid, lista_rss
            
def desenha_grafico_rss():
    import matplotlib
    import matplotlib.pyplot as plt
    matplotlib.use("Agg")
    import matplotlib.backends.backend_agg as agg
    lista_p, lista_v = captura_processos("grafico")
    names = lista_p
    values = lista_v

    fig, axs = plt.subplots()
    axs.plot(names, values)
    fig.suptitle('Categorical Plotting')

    canvas = agg.FigureCanvasAgg(fig)
    canvas.draw()
    size = canvas.get_width_height()
    renderer = canvas.get_renderer()
    raw_data = renderer.tostring_rgb()

    surf = pygame.image.fromstring(raw_data, size, "RGB")
    tela.blit(surf, (100,150))