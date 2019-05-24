import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.ticker as mtick
from matplotlib import style
import pandas as pd
from memory import*

class graficos():
        def __init__(self):
            self.falhas = []
            self.t_espera = []
            self.t_clock = []

        def import_falhas(self,f):
            self.falhas.append(f)

        def import_espera(self,e):
            self.t_espera.append(e)

        def import_clock(self,c):
            self.t_clock.append(c)

        def my_graph(self):
            style.use('fivethirtyeight')
            ys = self.falhas
            xs = self.t_clock

            print (xs)
            print (ys)
            plt.xlabel('Clock')
            plt.ylabel('Falhas')
            plt.plot(xs,ys)
            plt.show()

''' #Grafico de processos
    def mem_status(self,clock):
        mem = [] 
        clock_list = []
        for i in self.memory:
            if isinstance(i,cell_memory):
                for j in range(i.get_size()):
                    mem.append('F')
                    clock_list.append(clock)
            elif isinstance(i,process):
                for j in range(i.get_size()):
                    mem.append('O')
                    clock_list.append(clock)
        return clock_list,mem

    #style.use('fivethirtyeight')
   

    def graph(self,clock):
        xs,ys = self.mem_reciever(clock)

        df = pd.DataFrame({
            'time':pd.Series(xs),
            'process': pd.Series(ys),
        })
        df[['time','process']]

        df.groupby(['time','process']).size().groupby(level=0).apply(
            lambda x: 100 * x / x.sum()
        ).unstack().plot(kind='bar',stacked=True,legend='reverse')

        plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter())
        plt.title('Process memory')
        # plt.legend(loc='lower right')
        plt.gcf().set_size_inches(7,4)
        plt.show()
'''