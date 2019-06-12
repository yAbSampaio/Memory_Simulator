from include.graphics import*

class Menu_Final():
    
    def __init__(self,falhas,espera,name):
        self.__menu = GraphWin("Menu", 400,300, autoflush=True )
        self.__menu.setBackground('white')

        self.Title = Text(Point(200,40), 'Simulador de\nAlocação de\nProcessos')
        self.Title.setFace("times roman")
        self.Title.setSize(18)
        self.Title.setTextColor("dark blue")
        self.Title.setStyle("bold")
        self.Title.draw(self.__menu)

        self.Name = Text(Point(200,90), name)
        self.Name.setFace("times roman")
        self.Name.setSize(18)
        self.Name.setTextColor("dark blue")
        self.Name.setStyle("bold")
        self.Name.draw(self.__menu)

        self.Algoritmos = Text(Point(100,120), 'Gráficos')
        self.Algoritmos.setFace("times roman")
        self.Algoritmos.setSize(15)
        self.Algoritmos.setTextColor("dark blue")
        self.Algoritmos.setStyle("bold")
        self.Algoritmos.draw(self.__menu)

        self.Algoritmos2 = Text(Point(100,160), '> Falhas' )
        self.Algoritmos2.setFace("times roman")
        self.Algoritmos2.setSize(15)
        self.Algoritmos2.setTextColor("black")
        self.Algoritmos2.setStyle("bold")
        self.Algoritmos2.draw(self.__menu)

        self.Algoritmos3 = Text(Point(100,190), '> Espera')
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

        self.Algoritmos4 = Text(Point(200,260), 'Fechar')
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
        
        self.Algoritmos = Text(Point(280,150), str(falhas))
        self.Algoritmos.setFace("times roman")
        self.Algoritmos.setSize(15)
        self.Algoritmos.setTextColor("dark blue")
        self.Algoritmos.setStyle("bold")
        self.Algoritmos.draw(self.__menu)

        self.Algoritmos = Text(Point(280,180), 'Média de espera:')
        self.Algoritmos.setFace("times roman")
        self.Algoritmos.setSize(15)
        self.Algoritmos.setTextColor("dark blue")
        self.Algoritmos.setStyle("bold")
        self.Algoritmos.draw(self.__menu)
        
        self.Algoritmos = Text(Point(280,210), str(espera))
        self.Algoritmos.setFace("times roman")
        self.Algoritmos.setSize(15)
        self.Algoritmos.setTextColor("dark blue")
        self.Algoritmos.setStyle("bold")
        self.Algoritmos.draw(self.__menu)

    def choice(self):
        while(True):
            click = self.__menu.getMouse()
            self.__menu.update()
            if(click.getX()>40 and click.getX()<160 and click.getY()>150 and click.getY()<170):
                self.__menu.close()
                return 1
            elif(click.getX()>40 and click.getX()<160 and click.getY()>180 and click.getY()<200):
                self.__menu.close()
                return 2
            elif(click.getX()>40 and click.getX()<160 and click.getY()>210 and click.getY()<230):
                self.__menu.close()
                return 3
            elif(click.getX()>40 and click.getX()<160 and click.getY()>250 and click.getY()<270):
                self.__menu.close()
                return 4
            elif(click.getX()>167 and click.getX()<230 and click.getY()>250 and click.getY()<270):
                self.__menu.close()
                return 5

class Menu_Inicio():

    def __init__(self):
        self.__menu = GraphWin("Menu", 200,250, autoflush=False )
        self.__menu.setBackground('white')

        self.Title = Text(Point(100,50), 'Simulador de\nAlocação de\nProcessos')
        self.Title.setFace("times roman")
        self.Title.setSize(18)
        self.Title.setTextColor("dark blue")
        self.Title.setStyle("bold")
        self.Title.draw(self.__menu)

        self.Algoritmos = Text(Point(100,120), 'Algoritmos')
        self.Algoritmos.setFace("times roman")
        self.Algoritmos.setSize(15)
        self.Algoritmos.setTextColor("dark blue")
        self.Algoritmos.setStyle("bold")
        self.Algoritmos.draw(self.__menu)

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

    def choice(self):
        while(True):
            click = self.__menu.getMouse()
            self.__menu.update()
            if(click.getX()>40 and click.getX()<160 and click.getY()>140 and click.getY()<160):
                self.__menu.close()
                return 1
            elif(click.getX()>40 and click.getX()<160 and click.getY()>170 and click.getY()<190):
                self.__menu.close()
                return 2
            elif(click.getX()>40 and click.getX()<160 and click.getY()>200 and click.getY()<220):
                self.__menu.close()
                return 3
    
        


