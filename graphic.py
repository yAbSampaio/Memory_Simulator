import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.ticker as mtick
from matplotlib import style
#import main
import pandas as pd
from memory import *

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
    plt.show()