from customtkinter import *
from customtkinter import CTkBaseClass
from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
import random
from PIL import Image, ImageTk
import time
from graph import Graph


class application(CTk):
    def __init__(self):
        super().__init__()
        self.playground = Graph()
        self.title("Vacuum Cleaner Simulator")
        self.geometry("900x700")
        self.config(bg="#87CDF6")
        self.resizable(False,False)
        self.label()
        self.canvas()
        self.mainloop()
    
    
    def label(self):
        self.titleLabel = CTkLabel(self,
                                   width=50,
                                   height=30,
                                   text="Vacuum Cleaner\nSimulator",
                                   bg_color="green",
                                   fg_color="#87CDF6",
                                   font=("Helvetica",20),
                                   corner_radius=20)
        self.titleLabel.place(x=35,y=20)
        
    
    #def button(self):
        #Button setting
    
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
                                                          fill="Green")
        
        self.node1 = self.visualizer.create_aa_circle(x_pos=self.playground.node1.posX,
                                                          y_pos=self.playground.node1.posY,
                                                          radius=30,
                                                          tags=self.playground.node1.id,
                                                          fill="Green")
        self.node2 = self.visualizer.create_aa_circle(x_pos=self.playground.node2.posX,
                                                          y_pos=self.playground.node2.posY,
                                                          radius=30,
                                                          tags=self.playground.node2.id,
                                                          fill="Green")
        self.node3 = self.visualizer.create_aa_circle(x_pos=self.playground.node3.posX,
                                                          y_pos=self.playground.node3.posY,
                                                          radius=30,
                                                          tags=self.playground.node3.id,
                                                          fill="Green")
        self.node4 = self.visualizer.create_aa_circle(x_pos=self.playground.node4.posX,
                                                          y_pos=self.playground.node4.posY,
                                                          radius=30,
                                                          tags=self.playground.node4.id,
                                                          fill="Green")
        self.node5 = self.visualizer.create_aa_circle(x_pos=self.playground.node5.posX,
                                                          y_pos=self.playground.node5.posY,
                                                          radius=30,
                                                          tags=self.playground.node5.id,
                                                          fill="Green")
        self.node6 = self.visualizer.create_aa_circle(x_pos=self.playground.node6.posX,
                                                          y_pos=self.playground.node6.posY,
                                                          radius=30,
                                                          tags=self.playground.node6.id,
                                                          fill="Green")
        self.node7 = self.visualizer.create_aa_circle(x_pos=self.playground.node7.posX,
                                                          y_pos=self.playground.node7.posY,
                                                          radius=30,
                                                          tags=self.playground.node7.id,
                                                          fill="Green")
        self.node8 = self.visualizer.create_aa_circle(x_pos=self.playground.node8.posX,
                                                          y_pos=self.playground.node8.posY,
                                                          radius=30,
                                                          tags=self.playground.node8.id,
                                                          fill="Green")
        self.node9 = self.visualizer.create_aa_circle(x_pos=self.playground.node9.posX,
                                                          y_pos=self.playground.node9.posY,
                                                          radius=30,
                                                          tags=self.playground.node9.id,
                                                          fill="Green")
        self.node10 = self.visualizer.create_aa_circle(x_pos=self.playground.node10.posX,
                                                          y_pos=self.playground.node10.posY,
                                                          radius=30,
                                                          tags=self.playground.node10.id,
                                                          fill="Green")
        
