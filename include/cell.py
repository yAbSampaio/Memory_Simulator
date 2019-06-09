class cell_memory():
    def __init__(self, size, ids):
        self.__size = size
        self.__id_m = ids

    def modify(self, size):
        self.__size = size

    def get_size(self):
        return self.__size
    def set_size(self,sz):
        self.__size += sz
    def get_ids(self):
        return self.__id_m

    def printf(self):
        print("Hole")
        print("Tamanho: "+str(self.__size))
        print("id: "+str(self.__id_m))
        print("--------------------------")
