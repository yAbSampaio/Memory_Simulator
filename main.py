#coding= utf -8
from process import*
from cell import*
from memory import*

#------------------------VarGlobais------------------------------------#
atual_clock = 0
t_apply = 0
t_wait = 0 #t_inicio - t_chegada
t_fail = 0 #tentativas falhas
t_medio = 0 

#------------------------inicialização---------------------------------#

proce = open("process.txt","r")
List = []
list_proc = []
Memo = mem_virtual()
choice = 0
for i in proce : #padronização do arquivo
    line=i.split("\n")[0]
    cell = line.split(" ")
    List.append(cell)
    
for i in List: #cria lista de classe processo
    Var = process(int(i[0]),int(i[1]),int(i[2]),int(i[3]))
    list_proc.append(Var)
list_proc = sorted(list_proc, key = process.get_arr)
choice = int(input("Digite\n1 - First Fit\n2 - Best Fit\n3 - Worst Fit\n"))

#---------------------------------------------------------------#
#Arruma logica de parada
n_wait = 0
while (Memo.get_len() != 1 or n_wait < len(list_proc)):#Enquato haver processo na lista 
    if(n_wait < len(list_proc)):
        while ((n_wait < len(list_proc)) and (list_proc[n_wait].get_arr() <= atual_clock)):#Fazer lista de espera
            #Chamada da função first, best worst
            if(choice == 1):
                Memo.FirstFit(list_proc[n_wait],atual_clock)
                n_wait += 1
            elif(choice == 2):
                Memo.BestFit(list_proc[n_wait],atual_clock)
                n_wait += 1
            else:
                #Memo.FirstFit(list_proc[n_wait],atual_clock)
                n_wait += 1
                
    for i in range(len(list_proc)):
        if atual_clock == list_proc[i].get_end():
            Memo.out_proce(list_proc[i])
            #list_proc[i].pop()
    
    print("-------------")
    print("clock: "+str(atual_clock))
    Memo.printf()
    print("------")
    print("\n")
    atual_clock += 1