from graphics import*

class Menu():
    
    def __init__(self):
        self.__menu = GraphWin("Menu", , )
        self.__menu.setBackground(' ')
        self.Title = Text(Point(, ), 'Menu')
        self.Title.setFace("times roman")
        self.Title.setSize(28)
        self.Title.setStyle("bold")
        self.Title.draw(self.__simulator)