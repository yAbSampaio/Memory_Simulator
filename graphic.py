import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.ticker as mtick
from matplotlib import style
import pandas as pd
from memory import*
#from dsutil import plotting

'''
style.use('fivethirtyeight')
def graph(mem,clock):
    xs,ys = mem.mem_reciever(clock)

    df = pd.DataFrame({
        'time':xs,
        'process':ys,
    })

    df.groupby(['time','process']).size().groupby(level=0).apply(
        lambda x: 100 * x / x.sum()
    ).unstack().plot(kind='bar',stacked=True,legend='reverse')

    plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter())
    plt.title('Amount of records by Gender and State, normalized')
    # plt.legend(loc='lower right')
    plt.gcf().set_size_inches(7,4)
    plt.show()'''

def mem_reciever(self,clock):
    mem = []
    falhas = []
    t_espera = []
    t_clock = []

def import_falhas(f):
    falhas.append(f)

def import_espera(e):
    t_espera.append(e)

def import_clock(c):
    t_clock.append(c)

def my_graph():
    xs = falhas
    ys = t_clock

    plt.plot(xs,ys)

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
