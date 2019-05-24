#coding= utf-8
#from graphic import*
from process import*
from memory import*
from graphic import *
import time

#------------------------VarGlobais------------------------------------#
atual_clock = 0
t_apply = 0
t_wait = 0 #t_inicio_clock - t_chegada
t_fail = 0 #tentativas falhas
t_medio = 0 #tempo médio
contador_proc = 0 #contador
n_try = 0
grafs = graficos()
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
while (Memo.get_len() != 1 or contador_proc < len(list_proc)):#Enquato haver processo na lista 
    control = contador_proc
    while (contador_proc < len(list_proc) and (list_proc[control].get_arr() <= atual_clock) ):#Fazer lista de espera
        #Chamada da função first, best worst
        if(choice == 1):#*------First Fit --------*#
            if(Memo.FirstFit(list_proc[contador_proc],atual_clock)):
                t_wait += atual_clock-list_proc[contador_proc].get_arr()
                contador_proc += 1
                control += 1
            else:
                n_try += 1
                control += 1

        elif(choice == 2):#*------Best Fit --------*#
            if(Memo.BestFit(list_proc[contador_proc],atual_clock)):
                t_wait += atual_clock-list_proc[contador_proc].get_arr()
                contador_proc += 1
                control += 1
            else:
                n_try += 1
                control += 1
        elif(choice == 3):#*------Worst Fit --------*#
            if(Memo.WorstFit(list_proc[contador_proc],atual_clock)):
                t_wait += atual_clock-list_proc[contador_proc].get_arr()
                contador_proc += 1
                control += 1
            else:
                n_try += 1
                control += 1
    grafs.import_falhas(n_try)
    #grafs.import_espera()
    grafs.import_clock(atual_clock)
                
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
    
grafs.my_graph()

print("Numero de falhas "+ str(n_try))
t_wait = t_wait/contador_proc
t_medio = time.time()-t_medio
print("Numero medio de espera "+str(t_wait))
print("Tempo de execução "+str(t_medio))