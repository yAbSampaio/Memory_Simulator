from graphics import*

class Interface():
    
    def __init__(self):
        self.__simulator = GraphWin("Memória",1224,600)
        self.__simulator.setBackground('white')
        self.Title = Text(Point(600, 50), 'Simulador de Memória')
        self.Title.setFace("times roman")
        self.Title.setSize(28)
        self.Title.setStyle("bold")
        self.Title.draw(self.__simulator)
        self.Len = Text(Point(100, 25), 'Status da Memória:')
        self.Len.setFace("times roman")
        self.Len.setSize(12)
        self.Len.setStyle("bold")
        self.Len.draw(self.__simulator)
        self.clock = Text(Point(400, 150), 'Clock: '+str(0))
        self.clock.setFace("times roman")
        self.clock.setSize(20)
        self.clock.setStyle("bold")
        self.clock.draw(self.__simulator)
        self.List_Hole = []
        self.List_id = []
        self.List_info = []

    def atualizar(self,number,mem,clock):
        self.clock.undraw()
        self.clock = Text(Point(400, 150), 'Clock: '+str(clock))
        self.clock.setFace("times roman")
        self.clock.setSize(20)
        self.clock.setStyle("bold")
        self.clock.draw(self.__simulator)
        
        pt_t = 50
        pt_t2 = 50
        pt_t3 = 50
        pt_init = 100
        step = (1024/number)
        pt_1 = pt_init

        for i in range(len(self.List_Hole)):
            self.List_Hole[i].undraw()
            self.List_id[i].undraw()
            for j in range(len(self.List_info[i])):
                self.List_info[i][j].undraw()
        while len(self.List_Hole) != 0:
            self.List_Hole.pop(0)
            self.List_id.pop(0)
            self.List_info.pop(0)

        for i in range(number):
            pt_2 = pt_1+step
            self.List_Hole.append(Rectangle(Point(pt_1, 350), Point(pt_2,450)))
            self.List_id.append(Text(Point((pt_2+pt_1)/2, 400), str(mem.get_ids(i))))
            pt_1 = pt_2
            List = []
            if mem.get_obj(i) == 1:
                self.List_Hole[i].setFill(color_rgb(255,154,154))
                self.List_Hole[i].draw(self.__simulator)
                self.List_id[i].setFace("times roman")
                self.List_id[i].setSize(23)
                self.List_id[i].setStyle("bold")
                self.List_id[i].draw(self.__simulator)
                if(i>=5):
                    if(i>=8):
                        List.append(Text(Point(220, pt_t3), 'Processo'))
                        List.append(Text(Point(220, pt_t3+25), 'Id: '+str(mem.get_ids(i))))
                        List.append(Text(Point(220, pt_t3+50), 'Tam: '+str(mem.get_size(i))))
                        List.append(Text(Point(220, pt_t3+75), 'Saida: '+str(mem.get_end(i))))
                        pt_t3 += 100
                    else:
                        List.append(Text(Point(130, pt_t2), 'Processo'))
                        List.append(Text(Point(130, pt_t2+25), 'Id: '+str(mem.get_ids(i))))
                        List.append(Text(Point(130, pt_t2+50), 'Tam: '+str(mem.get_size(i))))
                        List.append(Text(Point(130, pt_t2+75), 'Saida: '+str(mem.get_end(i))))
                        pt_t2 += 100
                else:
                    List.append(Text(Point(40, pt_t), 'Processo'))
                    List.append(Text(Point(40, pt_t+25), 'Id: '+str(mem.get_ids(i))))
                    List.append(Text(Point(40, pt_t+50), 'Tam: '+str(mem.get_size(i))))
                    List.append(Text(Point(40, pt_t+75), 'Saida: '+str(mem.get_end(i))))
                for i in range(4):
                    List[i].setFace("times roman")
                    List[i].setSize(10)
                    List[i].draw(self.__simulator)
                pt_t += 100
            else:
            
                self.List_Hole[i].setFill(color_rgb(192,192,192))
                self.List_Hole[i].draw(self.__simulator)
                self.List_id[i].setFace("times roman")
                self.List_id[i].setSize(23)
                self.List_id[i].setStyle("bold")
                self.List_id[i].draw(self.__simulator)
                if(i>=5):        
                    if(i>=8):
                        List.append(Text(Point(220, pt_t3), 'Buraco'))
                        List.append(Text(Point(220, pt_t3+25), 'Id: '+str(mem.get_ids(i))))
                        List.append(Text(Point(220, pt_t3+50), 'Tam: '+str(mem.get_size(i))))
                        pt_t3
                    else:
                        List.append(Text(Point(130, pt_t2), 'Buraco'))
                        List.append(Text(Point(130, pt_t2+25), 'Id: '+str(mem.get_ids(i))))
                        List.append(Text(Point(130, pt_t2+50), 'Tam: '+str(mem.get_size(i))))
                        pt_t2 += 100
                else:
                    List.append(Text(Point(40, pt_t), 'Buraco'))
                    List.append(Text(Point(40, pt_t+25), 'Id: '+str(mem.get_ids(i))))
                    List.append(Text(Point(40, pt_t+50), 'Tam: '+str(mem.get_size(i))))
                for i in range(3):
                    List[i].setFace("times roman")
                    List[i].setSize(10)
                    List[i].draw(self.__simulator)
                pt_t += 75            
            self.List_info.append(List)


    def close(self):
        self.__simulator.close()

    def input_p(self,proce, pos):
        Rec = Rectangle(Point(400, 200), Point(550,300))
        Rec.setFill(color_rgb(255,154,154))
        Rec.draw(self.__simulator)
        Linha = Line(Rec.getCenter(),self.List_Hole[pos].getCenter())
        Id = Text(Point(475, 225), 'Id: '+str(proce.get_ids()))
        Tam = Text(Point(475, 250), 'Tam: '+str(proce.get_size()))
        Linha.draw(self.__simulator)
        Id.draw(self.__simulator)
        Tam.draw(self.__simulator)
        #colocar um time sleep, ou um botao na graphics pra ver a interação
        Rec.undraw()
        Linha.undraw()
        Id.undraw()
        Tam.undraw()
    
    def outp(self,id,mem):
        self.List_Hole[id].undraw()
        self.List_Hole[id].setFill('white')
        self.List_Hole[id].draw(self.__simulator)
        Rec = Rectangle(Point(400, 475), Point(550,575))
        Rec.setFill(color_rgb(192,192,192))
        Rec.draw(self.__simulator)
        Id = Text(Point(475, 500), 'Id: '+str(mem.get_ids(id)))
        Tam = Text(Point(475, 525), 'Tam: '+str(mem.get_size(id)))
        Id.draw(self.__simulator)
        Tam.draw(self.__simulator)
        #colocar um time sleep, ou um botao na graphics pra ver a interação
        Rec.undraw()
        Id.undraw()
        Tam.undraw()
