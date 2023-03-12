import networkx as nx
import matplotlib.pylab as plt
from time import *

class Node:
    def __init__(self,posX,posY,id):
        self.id = id
        self.status = False
        self.posX = posX
        self.posY = posY


class Graph:
    def __init__(self):
        self.startNode = Node(350,35,'A')
        self.node1 = Node(150,135,'B')
        self.node2 = Node(550,135,'C')
        self.node3 = Node(350,200,'D')
        self.node4 = Node(150,300,'E')
        self.node5 = Node(550,300,'F')
        self.node6 = Node(350,375,'G')
        self.node7 = Node(150,475,'H')
        self.node8 = Node(550,475,'I')
        self.node9 = Node(350,550,'J')
        self.node10 = Node(350,670,'K')
        self.edges = {self.startNode:{self.node1:100,self.node2:100,self.node3:150},
                      self.node1:{self.startNode:100,self.node2:200,self.node4:200,self.node6:250},
                      self.node2:{self.startNode:100,self.node1:200,self.node5:200,self.node6:250},
                      self.node3:{self.startNode:100,self.node6:100},
                      self.node4:{self.node1:100,self.node5:200,self.node6:100,self.node7:100},
                      self.node5:{self.node2:100,self.node4:200,self.node6:100,self.node8:100},
                      self.node6:{self.node1:250,self.node2:250,self.node3:100,self.node4:100,self.node5:100,self.node7:100,self.node8:100,self.node9:100},
                      self.node7:{self.node4:100,self.node6:100,self.node8:200,self.node9:100,self.node10:100},
                      self.node8:{self.node5:100,self.node6:100,self.node7:200,self.node9:100,self.node10:100},
                      self.node9:{self.node7:100,self.node8:100,self.node6:100,self.node10:100},
                      self.node10:{self.node9:100}
                      }

house = Graph()
toVisit = [house.startNode]
visited = 0
              
                
def traverse(house):
    toVisit = [house.startNode]
    visited = []
    distance = 0
    i = 0
    #We traverse through the toVisit nodes (inittialy only startNode)
    while toVisit:
        n = toVisit.pop(0)
        print("Visiting node...",n.id)
        if not n.status:
            #Label for indicating the cleaning process
            print("cleaning...")
            sleep(0.5)
            n.status = True
            #Label for indication the node was cleaned
            print("Clean!")
            #Change the node color to green (Clean)
            sleep(0.5)
            visited.append(n)
            for o in house.edges[n]:
                toVisit.append(o)
                distance += house.edges[n][o]
    
    for x in visited:
        print(x.id)
    print(distance)
    
#traverse(house)          
                 
    
    


#House = Graph()
#G = nx.Graph(House.edges)
#pos = nx.spring_layout(G)
#nx.draw_networkx_nodes(G,pos)
#nx.draw_networkx_edges(G,pos)
#nx.draw_networkx_labels(G,pos)

#plt.show()




        
