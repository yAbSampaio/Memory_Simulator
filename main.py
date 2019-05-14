#coding= utf -8
from pro_mem import*

#------------------------VarGloais------------------------------------#
atual_clock = 0
t_apply = 0
t_wait = 0
t_fail = 0
t_medio = 0

#-----------------------------------------------------------#
proce = open("process.txt","r")
List = []
list_proc = []
Memo = mem_virtual()

for i in proce : #padronização do arquivo
    line=i.split("\n")[0]
    cell = line.split(" ")
    List.append(cell)
    
for i in List: #cria lista de classe processo
    Var = process(int(i[0]),int(i[1]),int(i[2]),int(i[3]))
    list_proc.append(Var)
list_proc = sorted(list_proc, key = process.get_arr)

#---------------------------------------------------------------#
n_wait = 0
while (list_proc != None):#Enquato haver processo na lista 
    while (list_proc[n_wait].get_arr() <= atual_clock):#Fazer lista de espera
        Memo.FirstFit(processo)
        #Chamada da função first, best worst
        n_wait += 1        
    
    for i in range(len(list_proc)):
        if atual_clock == list_proc[i].get_end():
            Memo.out_proce(list_proc[i])