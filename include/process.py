class process():
    def __init__(self, name, arr, run, tam):
        self.__name = name
        self.__t_arrival = int(arr)
        self.__size = int(tam)
        self.__t_run = int(run)
        self.__t_end = -1

    def get_arr(self):
        return self.__t_arrival

    def get_end(self):
        return self.__t_end

    def get_size(self):
        return self.__size

    def get_ids(self):
        return self.__name

    def modify(self, clock):
        self.__t_end = self.__t_run + clock
    
    def printf(self):
        print("Processo: "+str(self.__name))
        print("Tamanho: "+str(self.__size))
        print("Tempo: "+str(self.__t_arrival))
        print("Tem end: "+str(self.__t_end))
        print("--------------------------")