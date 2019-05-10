
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

    def get_ids(self):
        return self.__id_m


class mem_virtual():
    def __init__(self):
        self.memory = []
        self.memory.append(cell_memory(1024, 0)) #deveria receber o id do processo?

    def inp_proce(self, proce, clock, id_h):  #input
        self.memory[id_h].modify_m(self.memory[id_h].size() - proce.get_size())
        if self.memory[id_h].size() == 0:
            self.memory[id_h].pop()
        self.memory.insert(id_h, proce)
        proce.modify_end(clock)

    def out_proce(self, proce):
        sz = proce.get_size()
        if checking(pos-1):#Logica da posição na memória
            self.memory[pos-1].size() += sz
            if checking(pos+1):
                self.memory[pos-1].size() += self.memory[pos+1].size()
                self.memory.pop(pos+1)
                self.memory.pop(pos)
        elif checking(pos+1):
                self.memory[pos-1].size() += sz
                self.memory.pop(pos)
        else:
            self.memory.pop(pos)
            self.memory.insert(pos,cell_memory(sz,pos))
        
    def checking(self,position):
        if (self.memory[position] == cell_memory):
            return True
    def dsc_hole(self):
        hole = []
        for i in self.memory
            if (i == cell_memory):
                hole.append(i)
        return hole

    def FirstFit(processo, clock):
        for cell in self.memory:
            if cell == cell_memory:
                if cell.get_size() >= processo.get_size():
                    self.inp_proce(processo, clock, processo.get_name())
                    return self



