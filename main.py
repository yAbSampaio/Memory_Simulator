#coding= utf-8
#from graphic import*
from process import*
from memory import*
import time
#------------------------VarGlobais------------------------------------#
atual_clock = 0
t_apply = 0
t_wait = 0 #t_inicio_clock - t_chegada
t_fail = 0 #tentativas falhas
t_medio = 0 #tempo médio
cont = 0 #contador
n_try = 0
#------------------------inicialização---------------------------------#

proce = open("process.txt","r")
List = [] #temporária para padronizar
list_proc = [] #lista de processos padronizados
list_espera = []
Memo = mem_virtual() #memória virtual
choice = 0

print("* --------------------- Simulador de Memória ---------------------- *")
choice = int(input("|Digite a opção de qual algoritmo deseja testar:\n|(1) First Fit\n|(2) Best Fit\n|(3) Worst Fit\n* --------------------- Simulador de Memória ---------------------- *\n|Opção: "))

t_medio = time.time()

for i in proce : #padronização do arquivo
    line = i.split("\n")[0]
    cell = line.split(" ")
    List.append(cell)
    
for i in List: #cria lista de classe processo
    Var = process(int(i[0]),int(i[1]),int(i[2]),int(i[3]))
    list_proc.append(Var)
list_proc = sorted(list_proc, key = process.get_arr)

#---------------------------------------------------------------#
while (Memo.get_len() != 1 or cont < len(list_proc)):#Enquato haver processo na lista 
    control = True
    while (cont < len(list_proc) and (list_proc[cont].get_arr() <= atual_clock) and control):#Fazer lista de espera
        #Chamada da função first, best worst
        if(choice == 1):#*------First Fit --------*#
            if(Memo.FirstFit(list_proc[cont],atual_clock)):
                n_try += atual_clock-list_proc[cont].get_arr()
                cont += 1
            else:
                control = False

        elif(choice == 2):#*------Best Fit --------*#
            if(Memo.BestFit(list_proc[cont],atual_clock)):
                n_try += atual_clock-list_proc[cont].get_arr()
                cont += 1
            else:
                control = False
        
        elif(choice == 3):#*------Worst Fit --------*#
            if(Memo.WorstFit(list_proc[cont],atual_clock)):
                n_try += atual_clock-list_proc[cont].get_arr()
                cont += 1
            else:
                control = False
                
    for i in range(len(list_proc)):#Remove o processo se acabou de executar
        if atual_clock == list_proc[i].get_end():
            Memo.out_proce(list_proc[i])
    
    print("-------------")
    print("Clock: "+str(atual_clock))
    Memo.printf()
    #input("")
    print("-------------")
    print("\n")
    atual_clock += 1
    #Memo.graph(atual_clock)
print("Numero de falhas "+ str(n_try))
t_wait = n_try/cont
t_medio = time.time()-t_medio
print("Numero medio de espera "+str(t_wait))
print("Tempo de execução "+str(t_medio))