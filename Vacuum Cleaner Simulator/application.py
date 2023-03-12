from customtkinter import *
from customtkinter import CTkBaseClass
from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
import random
from PIL import Image, ImageTk
import time
from graph import Graph
from AI import vacuumCleaner
from time import *


class application(CTk):
    def __init__(self):
        super().__init__()
        self.playground = Graph()
        self.vCleaner = vacuumCleaner()
        self.title("Vacuum Cleaner Simulator")
        self.geometry("900x700")
        self.config(bg="#87CDF6")
        self.resizable(False,False)
        self.label()
        self.button()
        self.canvas()
        self.mainloop()
        
    
    def traverse(self):
        self.vCleaner.toVisit.append(self.playground.startNode)
        self.playgroundStatusInfo_Label.configure(text="DIRTY")
        while self.vCleaner.toVisit:
            n = self.vCleaner.toVisit.pop(0)
            print("Visiting node...",n.id)
            if not n.status:
                self.vaccuumStatusInfo_Label.configure(text="Cleaning...")
                print("cleaning...",n.id)
                sleep(1)
                n.status = True
                print(n.id,"Clean!")
                sleep(0.1)
                self.vCleaner.visited.append(n)
                self.visitedNodesInfo_Label.configure(text=len(self.vCleaner.visited))
                for o in self.playground.edges[n]:
                    self.vCleaner.toVisit.append(o)
                    self.vCleaner.traveled_Distance += self.playground.edges[n][o]
                    self.traveledDistanceCounter_Label.configure(text=str(self.vCleaner.traveled_Distance))
            self.update()
                  
        for x in self.vCleaner.visited:
            print(x.id)
        print(self.vCleaner.traveled_Distance)
        self.vaccuumStatusInfo_Label.configure(text="OFF") 
        self.playgroundStatusInfo_Label.configure(text="CLEAN")   
            
    
    
    def label(self):
        self.titleLabel = CTkLabel(self,
                                   width=50,
                                   height=30,
                                   text="Vacuum Cleaner\nSimulator",
                                   bg_color="#87CDF6",
                                   fg_color="green",
                                   corner_radius=10,
                                   font=("Helvetica",20))
        self.titleLabel.place(x=35,y=20)
        self.traveledDistance_Label = CTkLabel(self,
                                               width=50,
                                               height=20,
                                               text="Traveled\nDistance",
                                               bg_color="#87CDF6",
                                               fg_color="light blue",
                                               corner_radius=10,
                                               font=("Helvetica",14)
                                               )
        self.traveledDistance_Label.place(x=15,y=95)
        self.traveledDistanceCounter_Label = CTkLabel(self,
                                                      width=70,
                                                      height=20,
                                                      text=self.vCleaner.traveled_Distance,
                                                      )
        self.traveledDistanceCounter_Label.place(x=110,y=100)
        self.visitedNodesLabel = CTkLabel(self,
                                    width=50,
                                    height=20,
                                    text="Visited\nPlaces",
                                    bg_color="#87CDF6",
                                    fg_color="light blue",
                                    corner_radius=10,
                                    font=("Helvetica",14)
                                     )
        self.visitedNodesLabel.place(x=15,y=130)
        self.visitedNodesInfo_Label = CTkLabel(self,
                                                width=70,
                                                height=20,
                                                text=len(self.vCleaner.visited)
                                                      )
        self.visitedNodesInfo_Label.place(x=110,y=135)
        self.vaccuumStatusLabel = CTkLabel(self,
                                        width=50,
                                        height=20,
                                        text="Vaccuum\nStatus",
                                        bg_color="#87CDF6",
                                        fg_color="light blue",
                                        corner_radius=10,
                                        font=("Helvetica",14))
        self.vaccuumStatusLabel.place(x=15,y=165)
        self.vaccuumStatusInfo_Label = CTkLabel(self,
                                                width=70,
                                                height=20,
                                                text="OFF")
        self.vaccuumStatusInfo_Label.place(x=110,y=170)
        self.playgroundStatusLabel = CTkLabel(self,
                                        width=50,
                                        height=20,
                                        text="Playground\nStatus",
                                        bg_color="#87CDF6",
                                        fg_color="light blue",
                                        corner_radius=10,
                                        font=("Helvetica",14))
        self.playgroundStatusLabel.place(x=15,y=200)
        self.playgroundStatusInfo_Label = CTkLabel(self,
                                                width=70,
                                                height=20,
                                                text="DIRTY")
        self.playgroundStatusInfo_Label.place(x=110,y=205)
        
    
    def button(self):
        #Button setting
        self.startButton = CTkButton(self,
                                     width=140,
                                     height=20,
                                     corner_radius=20,
                                     bg_color="#87CDF6",
                                     fg_color="green",
                                     text="START",
                                     command=self.traverse)
        self.startButton.place(x=30,y=600)
    
    def canvas(self):
        self.visualizer = CTkCanvas(self, width=700, height=700)
        self.visualizer.place(x=225, y=0)
        self.edge1 = self.visualizer.create_line(self.playground.startNode.posX,
                                                 self.playground.startNode.posY,
                                                 self.playground.node1.posX,
                                                 self.playground.node1.posY,
                                                 width=5,
                                                 activefill="Black"
                                                 )
        self.edge2 = self.visualizer.create_line(self.playground.startNode.posX,
                                                 self.playground.startNode.posY,
                                                 self.playground.node2.posX,
                                                 self.playground.node2.posY,
                                                 width=5,
                                                 activefill="Black")
        self.edge3 = self.visualizer.create_line(self.playground.node1.posX,
                                                 self.playground.node1.posY,
                                                 self.playground.node2.posX,
                                                 self.playground.node2.posY,
                                                 width=5,
                                                 activefill="Black")
        self.edge4 = self.visualizer.create_line(self.playground.startNode.posX,
                                                 self.playground.startNode.posY,
                                                 self.playground.node3.posX,
                                                 self.playground.node3.posY,
                                                 width=5,
                                                 activefill="Black")
        self.edge5 = self.visualizer.create_line(self.playground.node1.posX,
                                                 self.playground.node1.posY,
                                                 self.playground.node6.posX,
                                                 self.playground.node6.posY,
                                                 width=5,
                                                 activefill="Black")
        self.edge6 = self.visualizer.create_line(self.playground.node2.posX,
                                                 self.playground.node2.posY,
                                                 self.playground.node6.posX,
                                                 self.playground.node6.posY,
                                                 width=5,
                                                 activefill="Black")
        self.edge7 = self.visualizer.create_line(self.playground.node3.posX,
                                                 self.playground.node3.posY,
                                                 self.playground.node6.posX,
                                                 self.playground.node6.posY,
                                                 width=5,
                                                 activefill="Black")
        self.edge8 = self.visualizer.create_line(self.playground.node1.posX,
                                                 self.playground.node1.posY,
                                                 self.playground.node4.posX,
                                                 self.playground.node4.posY,
                                                 width=5,
                                                 activefill="Black")
        self.edge9 = self.visualizer.create_line(self.playground.node2.posX,
                                                 self.playground.node2.posY,
                                                 self.playground.node5.posX,
                                                 self.playground.node5.posY,
                                                 width=5,
                                                 activefill="Black")
        self.edge10 = self.visualizer.create_line(self.playground.node4.posX,
                                                 self.playground.node4.posY,
                                                 self.playground.node5.posX,
                                                 self.playground.node5.posY,
                                                 width=5,
                                                 activefill="Black")
        self.edge11 = self.visualizer.create_line(self.playground.node4.posX,
                                                 self.playground.node4.posY,
                                                 self.playground.node6.posX,
                                                 self.playground.node6.posY,
                                                 width=5,
                                                 activefill="Black")
        self.edge12 = self.visualizer.create_line(self.playground.node5.posX,
                                                 self.playground.node5.posY,
                                                 self.playground.node6.posX,
                                                 self.playground.node6.posY,
                                                 width=5,
                                                 activefill="Black")
        self.edge13 = self.visualizer.create_line(self.playground.node6.posX,
                                                 self.playground.node6.posY,
                                                 self.playground.node9.posX,
                                                 self.playground.node9.posY,
                                                 width=5,
                                                 activefill="Black")
        self.edge14 = self.visualizer.create_line(self.playground.node6.posX,
                                                 self.playground.node6.posY,
                                                 self.playground.node7.posX,
                                                 self.playground.node7.posY,
                                                 width=5,
                                                 activefill="Black")
        self.edge15 = self.visualizer.create_line(self.playground.node6.posX,
                                                 self.playground.node6.posY,
                                                 self.playground.node8.posX,
                                                 self.playground.node8.posY,
                                                 width=5,
                                                 activefill="Black")
        self.edge16 = self.visualizer.create_line(self.playground.node4.posX,
                                                 self.playground.node4.posY,
                                                 self.playground.node7.posX,
                                                 self.playground.node7.posY,
                                                 width=5,
                                                 activefill="Black")
        self.edge17 = self.visualizer.create_line(self.playground.node5.posX,
                                                 self.playground.node5.posY,
                                                 self.playground.node8.posX,
                                                 self.playground.node8.posY,
                                                 width=5,
                                                 activefill="Black")
        self.edge18 = self.visualizer.create_line(self.playground.node7.posX,
                                                 self.playground.node7.posY,
                                                 self.playground.node9.posX,
                                                 self.playground.node9.posY,
                                                 width=5,
                                                 activefill="Black")
        self.edge19 = self.visualizer.create_line(self.playground.node8.posX,
                                                 self.playground.node8.posY,
                                                 self.playground.node9.posX,
                                                 self.playground.node9.posY,
                                                 width=5,
                                                 activefill="Black")
        self.edge20 = self.visualizer.create_line(self.playground.node7.posX,
                                                 self.playground.node7.posY,
                                                 self.playground.node10.posX,
                                                 self.playground.node10.posY,
                                                 width=5,
                                                 activefill="Black")
        self.edge21 = self.visualizer.create_line(self.playground.node8.posX,
                                                 self.playground.node8.posY,
                                                 self.playground.node10.posX,
                                                 self.playground.node10.posY,
                                                 width=5,
                                                 activefill="Black")
        self.edge22 = self.visualizer.create_line(self.playground.node9.posX,
                                                 self.playground.node9.posY,
                                                 self.playground.node10.posX,
                                                 self.playground.node10.posY,
                                                 width=5,
                                                 activefill="Black")
        self.startNode = self.visualizer.create_aa_circle(x_pos=self.playground.startNode.posX,
                                                          y_pos=self.playground.startNode.posY,
                                                          radius=30,
                                                          tags=self.playground.startNode.id,
                                                          fill="Red")
        
        self.node1 = self.visualizer.create_aa_circle(x_pos=self.playground.node1.posX,
                                                          y_pos=self.playground.node1.posY,
                                                          radius=30,
                                                          tags=self.playground.node1.id,
                                                          fill="Red")
        self.node2 = self.visualizer.create_aa_circle(x_pos=self.playground.node2.posX,
                                                          y_pos=self.playground.node2.posY,
                                                          radius=30,
                                                          tags=self.playground.node2.id,
                                                          fill="Red")
        self.node3 = self.visualizer.create_aa_circle(x_pos=self.playground.node3.posX,
                                                          y_pos=self.playground.node3.posY,
                                                          radius=30,
                                                          tags=self.playground.node3.id,
                                                          fill="Red")
        self.node4 = self.visualizer.create_aa_circle(x_pos=self.playground.node4.posX,
                                                          y_pos=self.playground.node4.posY,
                                                          radius=30,
                                                          tags=self.playground.node4.id,
                                                          fill="Red")
        self.node5 = self.visualizer.create_aa_circle(x_pos=self.playground.node5.posX,
                                                          y_pos=self.playground.node5.posY,
                                                          radius=30,
                                                          tags=self.playground.node5.id,
                                                          fill="Red")
        self.node6 = self.visualizer.create_aa_circle(x_pos=self.playground.node6.posX,
                                                          y_pos=self.playground.node6.posY,
                                                          radius=30,
                                                          tags=self.playground.node6.id,
                                                          fill="Red")
        self.node7 = self.visualizer.create_aa_circle(x_pos=self.playground.node7.posX,
                                                          y_pos=self.playground.node7.posY,
                                                          radius=30,
                                                          tags=self.playground.node7.id,
                                                          fill="Red")
        self.node8 = self.visualizer.create_aa_circle(x_pos=self.playground.node8.posX,
                                                          y_pos=self.playground.node8.posY,
                                                          radius=30,
                                                          tags=self.playground.node8.id,
                                                          fill="Red")
        self.node9 = self.visualizer.create_aa_circle(x_pos=self.playground.node9.posX,
                                                          y_pos=self.playground.node9.posY,
                                                          radius=30,
                                                          tags=self.playground.node9.id,
                                                          fill="Red")
        self.node10 = self.visualizer.create_aa_circle(x_pos=self.playground.node10.posX,
                                                          y_pos=self.playground.node10.posY,
                                                          radius=30,
                                                          tags=self.playground.node10.id,
                                                          fill="Red")
        
        
