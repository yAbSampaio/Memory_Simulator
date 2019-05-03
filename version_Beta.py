#coding= utf -8
atual_clock = 0
t_apply = 0
t_wait = 0
t_fail = 0
t_medio = 0

class Process():

    def __init__(self,arr,run,beg):
        self.t_arrival = arr
        self.t_run = run
        self.t_begin = beg
        self.t_end = 0
  

class Memory():

    def __init__(self):
        size = 0
        status = False
        id_m = 0

    def input(self,sz,st,ids):
        self.size = sz
        self.status = st
        self.id_m = ids
#-------------------------------------------#
Proce = open("process.txt","r")
Lista = []
for y in Proce :
    x=y.split("\n")[0]
    w = 0
    coluna = []
    print x
    while (w < 4):
    	k = x.split(" ")[w]
    	coluna.append(int(k))
    	w += 1
    Lista.append(coluna)
print (Lista)
