import networkx as nx
import matplotlib.pylab as plt

class Node:
    def __init__(self,posX,posY,id):
        self.id = id
        self.isClean = False
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
        self.edges = {self.startNode.id:{self.node1.id:100,self.node2.id:100,self.node3.id:150},
                      self.node1.id:{self.startNode.id:100,self.node2.id:200,self.node4.id:200,self.node6.id:250},
                      self.node2.id:{self.startNode.id:100,self.node1.id:200,self.node5.id:200,self.node6.id:250},
                      self.node3.id:{self.startNode.id:100,self.node6.id:100},
                      self.node4.id:{self.node1.id:100,self.node5.id:200,self.node6.id:100,self.node7.id:100},
                      self.node5.id:{self.node2.id:100,self.node4.id:200,self.node6.id:100,self.node8.id:100},
                      self.node6.id:{self.node1.id:250,self.node2.id:250,self.node3.id:100,self.node4.id:100,self.node5.id:100,self.node7.id:100,self.node8.id:100,self.node9.id:100},
                      self.node7.id:{self.node4.id:100,self.node6.id:100,self.node8.id:200,self.node9.id:100},
                      self.node8.id:{self.node5.id:100,self.node6.id:100,self.node7.id:200,self.node9.id:100},
                      self.node9.id:{self.node7.id:100,self.node8.id:100,self.node6.id:100},
                      self.node10.id:{self.node9.id:100}
                      }


#House = Graph()
#G = nx.Graph(House.edges)
#pos = nx.spring_layout(G)
#nx.draw_networkx_nodes(G,pos)
#nx.draw_networkx_edges(G,pos)
#nx.draw_networkx_labels(G,pos)

#plt.show()




        

