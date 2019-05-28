from process import*
from graphics import*

'''
proce = open("process.txt","r")
List = []
list_proc = []


for i in proce : #padronização do arquivo
    line=i.split("\n")[0]
    cell = line.split(" ")
    List.append(cell)
    
for i in List: #cria lista de classe processo
    Var = process(int(i[0]),int(i[1]),int(i[2]),int(i[3]))
    list_proc.append(Var)
list_proc = sorted(list_proc, key = process.get_arr)

for i in list_proc:
    i.printf()
    x= input("")'''
simulator = GraphWin("Memória",1024,500)
simulator.setBackground('white')
Imge = Image(Point(500,150), "set.png")
Imge.draw(simulator)
while (True):
    p3 = simulator.getMouse()
    p3.draw(simulator)
    print(p3)