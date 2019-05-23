#coding= utf-8
#from graphic import *
from process import *
from memory import *
import time
#------------------------VarGlobais------------------------------------#
atual_clock = 0
t_apply = 0
t_wait = 0 #t_inicio_clock - t_chegada
t_fail = 0 #tentativas falhas
t_medio = 0 #tempo médio
contador_ = 0 #contador

#------------------------Tentativa 2------------------------------------#
falhas = []
t_espera = []
t_clock = []
#importa falhas no ciclo de clock
def import_falhas(f):
    falhas.append(f)
#importa espera no ciclo de clock
def import_espera(e):
    t_espera.append(e)
#importa clock no final
def import_clock(c):
    t_clock.append(c)
#importa falhas por clock
def my_graph_falhas():
    xs = falhas
    ys = t_clock
    #plota x e y
    plt.plot(xs,ys)

#------------------------inicialização---------------------------------#
proce = open("process.txt","r")
List = [] #temporária para padronizar
list_proc = [] #lista de processos padronizados
Memo = mem_virtual() #memória virtual
choice = 0
t_medio = time.time()
for i in proce : #padronização do arquivo
    line=i.split("\n")[0]
    cell = line.split(" ")
    List.append(cell)
    
for i in List: #cria lista de classe processo
    Var = process(int(i[0]),int(i[1]),int(i[2]),int(i[3]))
    list_proc.append(Var) #adiciona processos na lista de processos
list_proc = sorted(list_proc, key = process.get_arr) #ordena ascendente os processos por tempo de chegada
print("* --------------------- Simulador de Memória ---------------------- *")
choice = int(input("|Digite a opção de qual algoritmo deseja testar:\n|(1) First Fit\n|(2) Best Fit\n|(3) Worst Fit\n* --------------------- Simulador de Memória ---------------------- *\n|Opção: "))
#---------------------------------------------------------------#
while (Memo.get_len() != 1 or contador_ < len(list_proc)): #Enquanto houver processos na lista 
    if(contador_ < len(list_proc)):
        while ((contador_ < len(list_proc)) and (list_proc[contador_].get_arr() <= atual_clock)):#Fazer lista de espera
            #Chamada da função first, best worst
            if(choice == 1): #*------First Fit --------*#
                if(Memo.FirstFit(list_proc[contador_],atual_clock)):
                    t_wait += atual_clock - list_proc[contador_].get_arr()
                    contador_ += 1
                else:
                    t_fail += 1
                    # Fazer logica fila de espera
            elif(choice == 2):#*------Best Fit --------*#              
                if(Memo.BestFit(list_proc[contador_],atual_clock)):
                    t_wait += atual_clock-list_proc[contador_].get_arr()
                    contador_ += 1 #Logica de t wait
                    # Fazer logica fila de espera
                else:
                    t_fail += 1
                    contador_ += 1
            elif(choice == 3):#*------Worst Fit --------*#
                if(Memo.WorstFit(list_proc[contador_],atual_clock)):
                    t_wait += atual_clock-list_proc[contador_].get_arr()
                    contador_ += 1 #Logica de t wait
                else:
                    t_fail += 1
                    contador_ += 1
                # Fazer logica fila de espera
        #import_falhas(t_fail)
        #import_espera(t_wait)
        #import_clock(atual_clock)
    for i in range(len(list_proc)): #Remove o processo se acabou de executar
        if atual_clock == list_proc[i].get_end():
            Memo.out_proce(list_proc[i])
            #list_proc[i].pop()
    
    print("-------------")
    print("Clock: "+str(atual_clock))
    Memo.printf()
    #input()
    print("------")
    print("\n")
    atual_clock += 1
    #Memo.graph(atual_clock)
print("Numero de falhas "+ str(t_fail))
a = t_wait/contador_
t_medio = time.time()-t_medio
print("Numero medio de espera "+str(a))
print("tempo de execução "+str(t_medio))
#chama a função
#my_graph_falhas()