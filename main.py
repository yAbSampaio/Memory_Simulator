#coding= utf-8
#from graphic import*
from process import*
from memory import*
from graphic import *
import time

#------------------------VarGlobais------------------------------------#
atual_clock = 0
media = 0
t_wait = 0 #t_inicio_clock - t_chegada
t_fail = 0 #tentativas falhas
t_medio = 0 #tempo médio
contador_proc = 0 #contador
n_try = 0
wait = 0
grafs = graficos()
interf = Interface()
#------------------------inicialização---------------------------------#

proce = open("process.txt","r")
List = [] #temporária para padronizar
list_proc = [] #lista de processos padronizados
list_espera = []
Memo = mem_virtual() #memória virtual
interf.atualizar(Memo.get_len(),Memo)
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
                wait = atual_clock-list_proc[contador_proc].get_arr()
                grafs.import_espera(wait)
                grafs.import_process(list_proc[contador_proc].get_name())
                contador_proc += 1
                control += 1
            else:
                n_try += 1
                control += 1

        elif(choice == 2):#*------Best Fit --------*#
            if(Memo.BestFit(list_proc[contador_proc],atual_clock)):
                t_wait += atual_clock-list_proc[contador_proc].get_arr()
                wait = atual_clock-list_proc[contador_proc].get_arr()
                grafs.import_espera(wait)
                grafs.import_process(list_proc[contador_proc].get_name())
                contador_proc += 1
                control += 1
            else:
                n_try += 1
                control += 1
        elif(choice == 3):#*------Worst Fit --------*#
            if(Memo.WorstFit(list_proc[contador_proc],atual_clock)):
                t_wait += atual_clock-list_proc[contador_proc].get_arr()
                wait = atual_clock-list_proc[contador_proc].get_arr()
                grafs.import_espera(wait)
                grafs.import_process(list_proc[contador_proc].get_name())
                contador_proc += 1
                control += 1
            else:
                n_try += 1
                control += 1
        

    grafs.import_falhas(n_try)
    grafs.import_clock(atual_clock)
    grafs.import_buraco(len(Memo.dsc_hole()))
                
    for i in range(len(list_proc)):#Remove o processo se acabou de executar
        if atual_clock == list_proc[i].get_end():
            Memo.out_proce(list_proc[i])
    
    print("-------------")
    print("Clock: "+str(atual_clock))
    Memo.printf()
    interf.atualizar(Memo.get_len(),Memo)
    input("")
    print("-------------")
    print("\n")
    atual_clock += 1


    
print("* --------------------- Simulador de Memória ---------------------- *")
choice2 = int(input("|Digite a opção de gráfico deseja analisar:\n|(1) Falhas\n|(2) Espera\n|(3) Fragmentação\n|(4) Encerrar \n* --------------------- Simulador de Memória ---------------------- *\n|Opção: "))
interf.close()
while(choice2 != 4):
    if(choice2 == 1):
        grafs.my_graph_falhas()
        print("Número de falhas "+ str(n_try))
    if(choice2 == 2):
        t_wait = n_try/contador_proc
        print("Número médio de espera "+str(t_wait))
        grafs.my_graph_espera()
    if(choice2 == 3):
        grafs.my_graph_buracos()
        #t_medio = time.time()-t_medio
    choice2 = int(input("|Digite a opção de gráfico deseja analisar:\n|(1) Falhas\n|(2) Espera\n|(3) Alocação\n|(4) Encerrar \n* --------------------- Simulador de Memória ---------------------- *\n|Opção: "))