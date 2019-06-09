import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.ticker as mtick
from matplotlib import style
import pandas as pd

class graficos():
        def __init__(self):
            self.falhas = []
            self.t_espera = []
            self.t_clock = []
            self.holes = []
            self.process = []

        def import_falhas(self,f):
            self.falhas.append(f)

        def import_process(self,p):
            self.process.append(p)

        def import_espera(self,e):
            self.t_espera.append(e)

        def import_clock(self,c):
            self.t_clock.append(c)
        
        def import_buraco(self,v):
            self.holes.append(v)

        def my_graph_falhas(self):
            style.use('Solarize_Light2')
            ys = self.falhas
            xs = self.t_clock
            plt.xlabel('Clock')
            plt.ylabel('Falhas')
            plt.plot(xs,ys)
            plt.show()

        def my_graph_espera(self):
            style.use('Solarize_Light2')
            xs = self.process
            ys = self.t_espera
            plt.xlabel('Processo')
            plt.ylabel('Espera')
            plt.bar(xs,ys)
            plt.show()

        def my_graph_buracos(self):
            style.use('Solarize_Light2')
            ys = self.holes
            xs = self.t_clock
            plt.xlabel('Clock')
            plt.ylabel('Buraco')
            plt.plot(xs,ys)
            plt.show()
    
#criar um menu na main pra escolher os first fit etc
#qnd acabar mostrar botao na memoria pra fechar e trocar o menu pra escolher os graficos
#uma seta pra controlar o clock pra avancar 
#output trocar cor do processo q irar sair apagar o id da memoria e dps colocar um retangulo de msm tamanho embaixo
        #dps att memoria
