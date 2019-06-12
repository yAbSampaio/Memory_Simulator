#coding= utf-8
#from graphic import*
from include.process import*
from include.memory import*
from src.menu import *
from src.graphic import*
from src.interaction import*
import time


def num_try(memoria,processo):
    list_hole = memoria.dsc_hole()
    tam = 0
    for i in list_hole:
        tam += i.get_size()
    if (tam >= processo.get_size()):
        return 1
    else:
        return 0

back = 0

if __name__ == "__main__":
    while(back == 0):
        back = 1
#------------------------VarGlobais------------------------------------#
        atual_clock = 0 #virtual clock
        t_wait = 0 #t_inicio_clock - t_chegada
        t_fail = 0 #tentativas falhas
        t_medio = 0 #tempo médio
        contador_proc = 0 #contador
        n_try = 0 #numero de falha clock a clock
        wait = 0 #numero de espera clock a clock
        Jump = 0
        List = [] #temporária para padronizar
        list_proc = [] #lista de processos padronizados

    #------------------------inicialização---------------------------------#
        proce = open("include/process.txt","r")
        grafs = graficos()
        menu = Menu_Inicio()
        Memo = mem_virtual() #memória virtual
        choice = menu.choice()
        if choice == 1:
            name = "First Fit"
        elif choice == 2:
            name = "Best Fit"
        elif choice == 3:
            name = "Worst Fit"
        
        screen = Interface(Memo.get_len(),Memo,atual_clock,name)
        #t_medio = time.time()

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
            control = 0
            while (control < len(list_proc) and (list_proc[control].get_arr() <= atual_clock) ):#Fazer lista de espera
                #Chamada da função first, best worst
                if(choice == 1):#*------First Fit --------*#
                    if(Memo.FirstFit(list_proc[control],atual_clock,screen)):
                        screen.atualizar(Memo.get_len(),Memo,atual_clock)
                        t_wait += atual_clock-list_proc[control].get_arr()
                        wait = atual_clock-list_proc[control].get_arr()
                        grafs.import_espera(wait)
                        grafs.import_process(list_proc[control].get_ids())
                        contador_proc += 1
                        control += 1
                    else:
                        if(list_proc[control].get_end() == -1):
                            n_try += num_try(Memo,list_proc[control])
                        control += 1

                elif(choice == 2):#*------Best Fit --------*#
                    if(Memo.BestFit(list_proc[control],atual_clock,screen)):
                        screen.atualizar(Memo.get_len(),Memo,atual_clock)
                        t_wait += atual_clock-list_proc[control].get_arr()
                        wait = atual_clock-list_proc[control].get_arr()
                        grafs.import_espera(wait)
                        grafs.import_process(list_proc[control].get_ids())
                        contador_proc += 1
                        control += 1
                    else:
                        if(list_proc[control].get_end() == -1):
                            n_try += num_try(Memo,list_proc[control])
                        control += 1
                elif(choice == 3):#*------Worst Fit --------*#
                    if(Memo.WorstFit(list_proc[control],atual_clock,screen)):
                        screen.atualizar(Memo.get_len(),Memo,atual_clock)
                        t_wait += atual_clock-list_proc[control].get_arr()
                        wait = atual_clock-list_proc[control].get_arr()
                        grafs.import_espera(wait)
                        grafs.import_process(list_proc[control].get_ids())
                        contador_proc += 1
                        control += 1
                    else:
                        if(list_proc[control].get_end() == -1):
                            n_try += num_try(Memo,list_proc[control])
                        control += 1
                            
            for i in range(len(list_proc)):#Remove o processo se acabou de executar
                if atual_clock == list_proc[i].get_end():
                    screen.outp(Memo.get_pos(list_proc[i]),Memo)
                    Memo.out_proce(list_proc[i])
                    screen.atualizar(Memo.get_len(),Memo,atual_clock)

            grafs.import_falhas(n_try)
            grafs.import_clock(atual_clock)
            grafs.import_buraco(len(Memo.dsc_hole()))
            
            if(Jump == 0):
                Jump = screen.Jumper()
            #time.sleep(0.5)
            atual_clock += 1
            screen.atualizar(Memo.get_len(),Memo,atual_clock)
            
        t_wait = t_wait/contador_proc
        screen.close()
        menu = Menu_Final(n_try,t_wait,name)
        choice = menu.choice()
        while(choice != 5):
            if(choice == 1):
                grafs.my_graph_falhas()
            elif(choice == 2):
                grafs.my_graph_espera()
            elif(choice == 3):
                grafs.my_graph_buracos()
            elif(choice == 4):
                back = 0
                break
            menu = Menu_Final(n_try,t_wait,name)
            choice = menu.choice()