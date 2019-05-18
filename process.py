class process():
    def __init__(self, name, arr,run, tam):
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

    def modify(self, clock):
        self.__t_end = self.__t_run + clock
    
    def printf(self):
        print("->Processo")
        print("-Tamanho: "+str(self.__size))
        print("-Tem end: "+str(self.__t_end))
