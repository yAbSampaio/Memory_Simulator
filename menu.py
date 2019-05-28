from graphics import*

class Menu():
    
    def __init__(self):
        self.__menu = GraphWin("Menu", 400,300, autoflush=False )
        self.__menu.setBackground('white')

        espacamento = 30
        self.Title = Text(Point(200,50), 'Simulador de\nAlocação de\nProcessos')
        self.Title.setFace("times roman")
        self.Title.setSize(18)
        self.Title.setTextColor("dark blue")
        self.Title.setStyle("bold")
        self.Title.draw(self.__menu)

        self.Algoritmos = Text(Point(100,120), 'Gráficos')
        self.Algoritmos.setFace("times roman")
        self.Algoritmos.setSize(15)
        self.Algoritmos.setTextColor("red")
        self.Algoritmos.setStyle("bold")
        self.Algoritmos.draw(self.__menu)
        #self.Title.draw(self.__simulator)

        self.Algoritmos2 = Text(Point(100,160), '>    Falhas' )
        self.Algoritmos2.setFace("times roman")
        self.Algoritmos2.setSize(15)
        self.Algoritmos2.setTextColor("black")
        self.Algoritmos2.setStyle("bold")
        self.Algoritmos2.draw(self.__menu)

        self.Algoritmos3 = Text(Point(100,190), '>    Espera')
        self.Algoritmos3.setFace("times roman")
        self.Algoritmos3.setSize(15)
        self.Algoritmos3.setTextColor("black")
        self.Algoritmos3.setStyle("bold")
        self.Algoritmos3.draw(self.__menu)

        self.Algoritmos4 = Text(Point(100,220), '> Alocação')
        self.Algoritmos4.setFace("times roman")
        self.Algoritmos4.setSize(15)
        self.Algoritmos4.setTextColor("black")
        self.Algoritmos4.setStyle("bold")
        self.Algoritmos4.draw(self.__menu)

        self.Algoritmos4 = Text(Point(100,260), 'Voltar')
        self.Algoritmos4.setFace("times roman")
        self.Algoritmos4.setSize(15)
        self.Algoritmos4.setTextColor("dark blue")
        self.Algoritmos4.setStyle("bold")
        self.Algoritmos4.draw(self.__menu)


        self.Algoritmos = Text(Point(280,120), 'Nro de falhas:')
        self.Algoritmos.setFace("times roman")
        self.Algoritmos.setSize(15)
        self.Algoritmos.setTextColor("dark blue")
        self.Algoritmos.setStyle("bold")
        self.Algoritmos.draw(self.__menu)
        #self.Title.draw(self.__simulator)
        
        self.Algoritmos = Text(Point(280,150), 'xxxxxxxx')
        self.Algoritmos.setFace("times roman")
        self.Algoritmos.setSize(15)
        self.Algoritmos.setTextColor("dark blue")
        self.Algoritmos.setStyle("bold")
        self.Algoritmos.draw(self.__menu)
        #self.Title.draw(self.__simulator)

        self.Algoritmos = Text(Point(280,180), 'Média de espera:')
        self.Algoritmos.setFace("times roman")
        self.Algoritmos.setSize(15)
        self.Algoritmos.setTextColor("dark blue")
        self.Algoritmos.setStyle("bold")
        self.Algoritmos.draw(self.__menu)
        #self.Title.draw(self.__simulator)
        
        self.Algoritmos = Text(Point(280,210), 'xxxxxxxx')
        self.Algoritmos.setFace("times roman")
        self.Algoritmos.setSize(15)
        self.Algoritmos.setTextColor("dark blue")
        self.Algoritmos.setStyle("bold")
        self.Algoritmos.draw(self.__menu)
        #self.Title.draw(self.__simulator)

        cliquePonto = self.__menu.getMouse()
    
    def menu_inicio():
        self.__menu = GraphWin("Menu", 200,250, autoflush=False )
        self.__menu.setBackground('white')

        espacamento = 30
        self.Title = Text(Point(100,50), 'Simulador de\nAlocação de\nProcessos')
        self.Title.setFace("times roman")
        self.Title.setSize(18)
        self.Title.setTextColor("dark blue")
        self.Title.setStyle("bold")
        self.Title.draw(self.__menu)

        self.Algoritmos = Text(Point(100,120), 'Algoritmos')
        self.Algoritmos.setFace("times roman")
        self.Algoritmos.setSize(15)
        self.Algoritmos.setTextColor("red")
        self.Algoritmos.setStyle("bold")
        self.Algoritmos.draw(self.__menu)
        #self.Title.draw(self.__simulator)

        self.Algoritmos2 = Text(Point(100,150), 'First Fit')
        self.Algoritmos2.setFace("times roman")
        self.Algoritmos2.setSize(15)
        self.Algoritmos2.setTextColor("black")
        self.Algoritmos2.setStyle("bold")
        self.Algoritmos2.draw(self.__menu)

        self.Algoritmos3 = Text(Point(100,180), 'Best Fit')
        self.Algoritmos3.setFace("times roman")
        self.Algoritmos3.setSize(15)
        self.Algoritmos3.setTextColor("black")
        self.Algoritmos3.setStyle("bold")
        self.Algoritmos3.draw(self.__menu)

        self.Algoritmos4 = Text(Point(100,210), 'Worst Fit')
        self.Algoritmos4.setFace("times roman")
        self.Algoritmos4.setSize(15)
        self.Algoritmos4.setTextColor("black")
        self.Algoritmos4.setStyle("bold")
        self.Algoritmos4.draw(self.__menu)

        cliquePonto = self.__menu.getMouse()



