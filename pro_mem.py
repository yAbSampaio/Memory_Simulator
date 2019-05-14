
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

    def get_name(self):
        return self.__name

    def modify_end(self, clock):
        self.__t_end = self.__t_run + clock


class cell_memory():
    def __init__(self, size, ids):
        self.__size = size
        self.__id_m = ids

    def modify_m(self, size):
        self.__size = size

    def get_size(self):
        return self.__size
    def set_size(self,sz):
        self.__size += sz
    def get_ids(self):
        return self.__id_m


class mem_virtual():
    def __init__(self):
        self.memory = []
        self.idb = 0
        self.memory.append(cell_memory(1024, self.idb)) #deveria receber o id do processo?

    def inp_proce(self, proce, clock, id_h):  #input
        self.memory[id_h].modify_m(self.memory[id_h].size() - proce.get_size())
        if self.memory[id_h].size() == 0:
            self.memory[id_h].pop()
        self.memory.insert(id_h, proce)#Arrumar logica do id hole
        proce.modify_end(clock)

    def out_proce(self, proce):
        pos = self.get_pos(proce)
        sz = proce.get_size()
        if self.checking(pos-1):#Logica da posição na memória
            self.memory[pos-1].set_size(sz)
            if self.checking(pos+1):
                self.memory[pos-1].set_size(self.memory[pos+1].get_size())
                self.memory.pop(pos+1)
                self.memory.pop(pos)
        elif self.checking(pos+1):
            self.memory[pos-1].set_size(sz)
            self.memory.pop(pos)
        else:
            self.idb += 1
            self.memory.pop(pos)
            self.memory.insert(pos,cell_memory(sz,self.idb))
        
    def checking(self,position):
        if (self.memory[position] == cell_memory):
            return True
    def dsc_hole(self):
        hole = []
        for i in self.memory:
            if (i == cell_memory):
                hole.append(i)
        return hole
    def get_pos(self,proce):
        cont = 0
        for i in self.memory:
            if (i == process):
                if (i.get_ids() == proce.get_ids()):
                    return cont
        cont += 1
    def get_id(self,hol):
        for i in range(len(self.memory)):
            if (self.memory[i] == cell_memory):
                if (self.memory[i].get_ids() == hol.get_ids()):
                    return i

    def FirstFit(processo, clock):
        for cell in self.memory:
            if cell == cell_memory:
                if cell.get_size() >= processo.get_size():
                    id = self.get_id(cell)
                    self.inp_proce(processo, clock, id)
                    return self

    def Best_fit(self,processo,clock):
        hole = self.dsc_hole()
        list_best = sorted(hole, key = cell_memory.get_size)
        for i in list_best:
            if (i.get_size() >= processo.get_size()):
                id = self.get_id(i)
                self.inp_proce(processo,clock,id)
                return self
