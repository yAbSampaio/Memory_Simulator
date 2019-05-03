#coding= utf -8
atual_clock = 0
t_apply = 0
t_wait = 0
t_fail = 0
t_medio = 0
#verifica se são essas as variaveis msm

class process():

    def __init__(self,name,arr,beg,run):
        self.__name = name
        self.__t_arrival = arr
        self.__size = beg
        self.__t_run = run
        self.__t_end = 0
    
    def get_arr(self):
        return self.t_arrival

    def modify(self,clock):
        self.__t_end = self.__t_run + clock
class memory():

    def __init__(self):
        self.__size = 1024
        self.__status = False
        self.__id_m = 0

    def get_size(self):
        return self.__size        
    
    def input(self,sz,st,ids):
        self.__status = True
        self.__id_m = ids
        #fazer logica de trocar de tamanho processo memoria
    
    def output(self):
        #fazer logica de trocar de tamanho processo memoria
        self.__status = False
        self.__id_m = -1
    
    def __modify(self):
        #fazer logica de trocar de tamanho processo memoria




#-------------------------------------------#
Proce = open("process.txt","r")
List = []
list_proc = []
t = []
for i in Proce :
    line=i.split("\n")[0]
    cell = line.split(" ")
    List.append(cell)

for i in List:
    Var = process(int(i[0]),int(i[1]),int(i[2]),int(i[3]))
    list_proc.append(Var)
list_proc = sorted(list_proc, key = process.get_arr)
#fazer modulação de codigo