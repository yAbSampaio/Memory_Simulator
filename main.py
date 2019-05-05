#coding= utf -8
from version_Beta import*

#------------------------------------------------------------#
atual_clock = 0
t_apply = 0
t_wait = 0
t_fail = 0
t_medio = 0
#verifica se são essas as variaveis msm
#-----------------------------------------------------------#
proce = open("process.txt","r")
List = []
list_proc = []
memory_Virtual = []
memory_Virtual.append(memory(1024))

for i in proce :
    line=i.split("\n")[0]
    cell = line.split(" ")
    List.append(cell)
    
for i in List:
    Var = process(int(i[0]),int(i[1]),int(i[2]),int(i[3]))
    list_proc.append(Var)
list_proc = sorted(list_proc, key = process.get_arr)

#---------------------------------------------------------------#