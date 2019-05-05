class process():
    def __init__(self,name,arr,beg,run):
        self.__name = name
        self.__t_arrival = arr
        self.__size = beg
        self.__t_run = run
        self.__t_end = None
    
    def get_arr(self):
        return self.__t_arrival
    
    def get_end(self):
        return self.__t_end
    
    def get_size(self):
        return self.__size

    def modify(self,clock):
        self.__t_end = self.__t_run + clock

class cell_memory():
    def __init__(self,size,ids):
        self.__size = size
        self.__id_m = ids
    def modify(self,size):
        self.__size = size
    def get_size(self):
        return self.__size
    def get_ids(self):
        return self.__id_m

class mem_virtual():
    def __init__(self):
        self.__memory = []
        self.__memory.append(cell_memory(1024,0))
    
    def new_hole(self):

    def inp_proce(self,proce,hole,clock):
        self.__memory.insert(hole.get_ids(),proce)#fazer um for no cod pra achar a posicao dodo buraco
        hole.modify(hole.get_size-proce.get_size)#ver com michel se tem q returna ou funciona como ponteiro 
        proce.modify(clock)#ver com michel se tem q returna ou funciona como ponteiro

    def out_proce(self):

    def checking(self)
    def dsc_hole(self):

    def dsc_pro(self):
        

#-------------------------------------------#