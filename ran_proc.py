import random

x = 55
cont = 1
with open('proces.txt', 'w+') as Process:
    while (cont <= x):
        name = cont
        t_arrival = random.randint(1,200)
        t_run = random.randint(20,50)
        size = random.randint(50,200)
        Process.write(str(name)+" ")
        Process.write(str(t_arrival)+" ")
        Process.write(str(t_run)+" ")
        Process.write(str(size)+"\n")
        cont += 1