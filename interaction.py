from graphics import*

class Interface():
    
    def __init__(self,number,mem,clock):
        self.step = 0
        self.Jump = 0

        self.__simulator = GraphWin("Memória",1224,600)
        self.__simulator.setBackground('white')

        self.Title = Text(Point(600, 50), 'Simulador de Memória')
        self.Title.setFace("times roman")
        self.Title.setSize(28)
        self.Title.setStyle("bold")
        self.Title.draw(self.__simulator)
        
        self.Lege = Text(Point(100, 25), 'Status da Memória:')
        self.Lege.setFace("times roman")
        self.Lege.setSize(12)
        self.Lege.setStyle("bold")
        self.Lege.draw(self.__simulator)

        self.Legen = Text(Point(1124, 25), 'Status da Memória:')
        self.Legen.setFace("times roman")
        self.Legen.setSize(12)
        self.Legen.setStyle("bold")
        self.Legen.draw(self.__simulator)
        
        self.clock = Text(Point(600, 100), 'Clock: '+str(0))
        self.clock.setFace("times roman")
        self.clock.setSize(20)
        self.clock.setStyle("bold")
        self.clock.draw(self.__simulator)

        self.Leg = Text(Point(800, 100), 'Legenda:')
        self.Leg.setFace("times roman")
        self.Leg.setSize(20)
        self.Leg.setStyle("bold")
        self.Leg.draw(self.__simulator)
        self.LegP = Text(Point(800, 130), 'Processo = ')
        self.LegP.setFace("times roman")
        self.LegP.setSize(15)
        self.LegP.setStyle("bold")
        self.LegP.draw(self.__simulator)
        self.LegH = Text(Point(800, 160), 'Espaço Vazio =')
        self.LegH.setFace("times roman")
        self.LegH.setSize(15)
        self.LegH.setStyle("bold")
        self.LegH.draw(self.__simulator)
        self.recP = Rectangle(Point(875, 120), Point(900,135))
        self.recP.setFill(color_rgb(255,154,154))
        self.recP.draw(self.__simulator)
        self.recH = Rectangle(Point(900, 150), Point(925,165))
        self.recH.setFill(color_rgb(192,192,192))
        self.recH.draw(self.__simulator)

        self.step = Image(Point(500,520), "step.png")
        self.jump = Image(Point(700,520), "jump.png")
        self.jump.draw(self.__simulator)
        self.step.draw(self.__simulator)

        self.List_Hole = []
        self.List_id = []
        self.List_info = []

        self.atualizar(number,mem,clock)

    def atualizar(self,number,mem,clock):
        self.clock.undraw()
        self.clock = Text(Point(600, 100), 'Clock: '+str(clock))
        self.clock.setFace("times roman")
        self.clock.setSize(20)
        self.clock.setStyle("bold")
        self.clock.draw(self.__simulator)
        
        pt_t = 50
        pt_t2 = 50
        pt_init = 100
        pt_1 = pt_init
        self.step = (1024/number)

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
            List = []
            pt_2 = pt_1+self.step

            self.List_Hole.append(Rectangle(Point(pt_1, 350), Point(pt_2,450)))
            self.List_id.append(Text(Point((pt_2+pt_1)/2, 400), 'Id: '+str(mem.get_ids(i))))
            self.List_id[i].setSize(20)
            self.List_id[i].setStyle("bold")
            pt_1 = pt_2

            if mem.get_obj(i) == 1:
                self.List_Hole[i].setFill(color_rgb(255,154,154))
                self.List_Hole[i].draw(self.__simulator)
                self.List_id[i].draw(self.__simulator)
                if(i>=5):
                    List.append(Text(Point(1180, pt_t2), 'Processo'))
                    List.append(Text(Point(1180, pt_t2+25), 'Id: '+str(mem.get_ids(i))))
                    List.append(Text(Point(1180, pt_t2+50), 'Tam: '+str(mem.get_size(i))))
                    List.append(Text(Point(1180, pt_t2+75), 'Saida: '+str(mem.get_end(i))))
                    pt_t2 += 100
                
                else:
                    List.append(Text(Point(40, pt_t), 'Processo'))
                    List.append(Text(Point(40, pt_t+25), 'Id: '+str(mem.get_ids(i))))
                    List.append(Text(Point(40, pt_t+50), 'Tam: '+str(mem.get_size(i))))
                    List.append(Text(Point(40, pt_t+75), 'Saida: '+str(mem.get_end(i))))
                    pt_t += 100

                for i in range(4):
                    List[i].setFace("times roman")
                    List[i].setSize(10)
                    List[i].draw(self.__simulator)
            
            else:
                self.List_Hole[i].setFill(color_rgb(192,192,192))
                self.List_Hole[i].draw(self.__simulator)
                self.List_id[i].draw(self.__simulator)
                if(i>=5):        
                    List.append(Text(Point(1180, pt_t2), 'Buraco'))
                    List.append(Text(Point(1180, pt_t2+25), 'Id: '+str(mem.get_ids(i))))
                    List.append(Text(Point(1180, pt_t2+50), 'Tam: '+str(mem.get_size(i))))
                    pt_t2 += 75
                
                else:
                    List.append(Text(Point(40, pt_t), 'Buraco'))
                    List.append(Text(Point(40, pt_t+25), 'Id: '+str(mem.get_ids(i))))
                    List.append(Text(Point(40, pt_t+50), 'Tam: '+str(mem.get_size(i))))
                    pt_t += 75
                for i in range(3):
                    List[i].setFace("times roman")
                    List[i].setSize(10)
                    List[i].draw(self.__simulator)            

            self.List_info.append(List)


    def close(self):
        self.__simulator.close()

    def input_p(self,proce, pos):
        ent = Text(Point(600, 200), 'Entrada de processo')
        ent.setFace("times roman")
        ent.setSize(20)
        ent.setStyle("bold")
        ent.draw(self.__simulator)
        Rec = Rectangle(Point(100, 225), Point(100+self.step,325))
        Rec.setFill(color_rgb(255,154,154))
        Rec.draw(self.__simulator)
        Id = Text(Point((200+self.step)/2, 255), 'Id: '+str(proce.get_ids()))
        Tam = Text(Point((200+self.step)/2, 285), 'Tam: '+str(proce.get_size()))
        Id.setSize(20)
        Tam.setSize(20)
        Id.setStyle("bold")
        Tam.setStyle("bold")
        Id.draw(self.__simulator)
        Tam.draw(self.__simulator)
                
        if(self.Jump == 0):
            if(pos == 0):
                time.sleep(1)
            time.sleep(0.25)
            
            while (abs((Rec.getCenter()).getX()-(self.List_Hole[pos].getCenter()).getX()) > 1.2):
                time.sleep(0.0009)
                Rec.move(1,0)
                Tam.move(1,0)
                Id.move(1,0)

        Rec.undraw()
        Id.undraw()
        Tam.undraw()
        ent.undraw()

    def outp(self,id,mem):
        end = Text(Point(600, 200), 'Saida de processo')
        end.setFace("times roman")
        end.setSize(20)
        end.setStyle("bold")
        end.draw(self.__simulator)
        self.List_Hole[id].undraw()
        self.List_Hole[id].setFill(color_rgb(192,192,192))
        self.List_Hole[id].draw(self.__simulator)
        
        p1 = (((self.List_Hole[id].getCenter()).getX())-(self.step/2))
        Rec = Rectangle(Point(p1, 225), Point(p1+self.step,325))
        Rec.setFill(color_rgb(255,154,154))
        Rec.draw(self.__simulator)
        Id = Text(Point((p1*2+self.step)/2, 265), 'Id: '+str(mem.get_ids(id)))
        Tam = Text(Point((p1*2+self.step)/2, 285), 'Tam: '+str(mem.get_size(id)))
        Id.setSize(20)
        Tam.setSize(20)
        Id.setStyle("bold")
        Tam.setStyle("bold")
        Id.draw(self.__simulator)
        Tam.draw(self.__simulator)
        
        
        if (self.Jump == 0):
            time.sleep(0.8)
            Rec.undraw()
            Id.undraw()
            Tam.undraw()
            time.sleep(0.8)
            end.undraw()
        else:
            Rec.undraw()
            Id.undraw()
            Tam.undraw()
            end.undraw()

    def Jumper(self):
        while (True):
            Point = self.__simulator.getMouse()
            Px = Point.getX()
            Py = Point.getY()
            if (Px > 469 and Py > 484 and Px < 538 and Py < 557):
                return 0
            elif (Px > 655 and Py > 484 and Px < 747 and Py < 557):
                self.Jump = 1
                return 1
