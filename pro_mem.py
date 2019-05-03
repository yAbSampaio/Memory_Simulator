class process():
    def __init__(self,name,arr,beg,run):
        self.__name = name
        self.__t_arrival = arr
        self.__size = beg
        self.__t_run = run
        self.__t_end = 0
    
    def get_arr(self):
        return self.__t_arrival

    def modify(self,clock):
        self.__t_end = self.__t_run + clock


class memory():
    def __init__(self,size,st,ids):
        self.__size = size
        self.__status = st
        self.__id_m = ids

    def get_info(self):
        return [self.__size, self.__id_m]

#-------------------------------------------#