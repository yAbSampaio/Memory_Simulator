#coding= utf -8
atual_clock = 0
t_apply = 0
t_wait = 0
t_fail = 0
t_medio = 0

class Process():

    def __init__(self,arr,beg,run):
        self.t_arrival = arr
        self.t_run = run
        self.size = beg
        self.t_end = 0
    
    def get_arr(self):
        return self.t_arrival


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
Processos = []
t = []
for i in Proce :
    line=i.split("\n")[0]
    cell = line.split(" ")
    Lista.append(cell)

for i in Lista:
    Var = Process(int(i[1]),int(i[2]),int(i[3]))
    Processos.append(Var)
print Processos[2].t_arrival
Processos = sorted(Processos, key = Process.get_arr)  
print Processos[2].t_arrival
