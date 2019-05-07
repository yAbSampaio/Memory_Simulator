class process():
    def __init__(self, name, arr, tam, run):
        self.__name = name
        self.__t_arrival = arr
        self.__size = tam
        self.__t_run = run
        self.__t_end = None

    def get_arr(self):
        return self.__t_arrival

    def get_end(self):
        return self.__t_end

    def get_size(self):
        return self.__size

    def modify(self, clock):
        self.__t_end = self.__t_run + clock


class cell_memory():
    def __init__(self, size, ids):
        self.__size = size
        self.__id_m = ids

    def modify(self, size):
        self.__size = size

    def get_size(self):
        return self.__size

    def get_ids(self):
        return self.__id_m


class mem_virtual():
    def __init__(self):
        self.__memory = []
        self.__memory.append(cell_memory(1024, 0))

    def inp_proce(self, proce, clock,id_h):
        self.__memory[id_h].modify(self.__memory[id_h() - proce.get_size())
        if self.__memory[id_h].size() == 0:
            self.__memory[id_h].pop()
        self.__memory.insert(id_h, proce)
        proce.modify(clock) 

    def out_proce(self, proce):
        sz = proce.get_size()
        if checking(pos-1):#Logica da posição
            self.__memory[pos-1].size += sz
            if checking(pos+1):
                self.__memory[pos-1].size += self.__memory[pos+1].size 
                self.__memory.pop(pos+1)
                self.__memory.pop(pos)
        elif checking(pos+1):
                self.__memory[pos-1].size += sz
                self.__memory.pop(pos)
        else:
            self.__memory.pop(pos)
            self.__memory.insert(pos,cell_memory(sz,pos))
        
    def checking(self,position):
        if (self.__memory[position] == cell_memory):
            return True
    def dsc_hole(self):
        hole = []
        for i in self.__memory
            if (i == cell_memory):
                hole.append(i)
        return hole

