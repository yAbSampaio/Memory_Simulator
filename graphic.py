import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.ticker as mtick
from matplotlib import style
import pandas as pd
from graphics import*

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
    
class Interface():
    
    def __init__(self):
        self.__simulator = GraphWin("Memória",1024,500)
        self.__simulator.setBackground('white')
        self.Title = Text(Point(500, 50), 'Simulador de Memória')
        self.Title.setFace("times roman")
        self.Title.setSize(28)
        self.Title.setStyle("bold")
        self.Title.draw(self.__simulator)
        self.List = []

    def atualizar(self,number,mem):
        for i in range(len(self.List)):
            self.List[i].undraw()
        while len(self.List) != 0:
            self.List.pop(0) 
        number += 1
        pt_central = (1000/(number))
        pt1 = pt_central-((mem.get_size(0)/2)*0.75)
        for i in range(number-1):
            pt2 = pt_central+((mem.get_size(i)/2)*0.75)
            self.List.append(Rectangle(Point(pt1, 350), Point(pt2,450)))
            pt_central += (1024/(number))*0.75
            pt1 = pt2
            if mem.get_obj(i) == 1:
                self.List[i].setFill('blue')
                self.List[i].draw(self.__simulator)
            else:
                self.List[i].setFill('yellow')
                self.List[i].draw(self.__simulator)

    def close(self):
        self.__simulator.close()