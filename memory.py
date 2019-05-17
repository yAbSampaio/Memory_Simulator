#coding=utf-8
from cell import*
from process import*

class mem_virtual():
    def __init__(self):
        self.memory = []
        self.idb = 0
        self.memory.append(cell_memory(1024, self.idb))

    def inp_proce(self, proce, clock, id_h):  #input
        self.memory[id_h].modify(self.memory[id_h].get_size() - proce.get_size())
        if self.memory[id_h].get_size() == 0:
            self.memory[id_h].pop()
        self.memory.insert(id_h, proce)
        proce.modify(clock)

    def out_proce(self, proce):
        pos = self.get_pos(proce)
        sz = proce.get_size()
        if self.checking(pos-1):#Logica da posição na memória
            self.memory[pos-1].set_size(sz)
            if self.checking(pos+1):
                self.memory[pos-1].set_size(self.memory[pos+1].get_size())
                self.memory.pop(pos+1)
                self.memory.pop(pos)
            else:
                self.memory.pop(pos)
        elif self.checking(pos+1):
            self.memory[pos+1].set_size(sz)
            self.memory.pop(pos)
        else:
            self.idb += 1
            self.memory.pop(pos)
            self.memory.insert(pos,cell_memory(sz,self.idb))
        
    def checking(self,position):
        if(position != -1 and position != len(self.memory)):
            if (isinstance(self.memory[position],cell_memory)):
                return True
            return False
        return False

    def dsc_hole(self):
        hole = []
        for i in self.memory:
            if isinstance(i,cell_memory):
                hole.append(i)
        return hole

    def get_pos(self,proce):#juntar tds os gets
        cont = 0
        for i in self.memory:
            if (isinstance(i,process)):
                if (i.get_name() == proce.get_name()):
                    return cont
            cont += 1
        cont += 1

    def get_len(self):
        return len(self.memory)

    def get_id(self,hol):
        for i in range(len(self.memory)):
            if isinstance(self.memory[i],cell_memory):
                if (self.memory[i].get_ids() == hol.get_ids()):
                    return i

    def BestFit(self,processo, clock):
        hole = self.dsc_hole()
        list_best = sorted(hole, key = cell_memory.get_size)
        for cell in list_best:
            if (cell.get_size() >= processo.get_size()):
                id = self.get_id(cell)
                self.inp_proce(processo,clock,id)
                return True
        return False
    
    def WorstFit(self,processo, clock):
        hole = self.dsc_hole()
        list_worst = sorted(hole, key = cell_memory.get_size,reverse=True)
        for cell in list_worst:
            if (cell.get_size() >= processo.get_size()):
                id = self.get_id(cell)
                self.inp_proce(processo,clock,id)
                return True
        return False
    
    def FirstFit(self,processo, clock):
        for cell in self.memory:
            if isinstance(cell,cell_memory):
                if cell.get_size() >= processo.get_size():
                    id = self.get_id(cell)
                    self.inp_proce(processo, clock, id)
                    return True
        return False

    def printf(self):
        for i in self.memory:
            i.printf()
