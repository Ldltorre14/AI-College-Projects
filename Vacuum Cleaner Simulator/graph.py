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
        self.startNode = Node(450,50,'A')
        self.node1 = Node(250,100,'B')
        self.node2 = Node(700,100,'C')
        self.node3 = Node(450,150,'D')
        self.node4 = Node(250,200,'E')
        self.node5 = Node(700,200,'F')
        self.node6 = Node(450,250,'G')
        self.node7 = Node(250,300,'H')
        self.node8 = Node(700,300,'I')
        self.node9 = Node(450,350,'J')
        self.node10 = Node(450,400,'K')
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


House = Graph()
G = nx.Graph(House.edges)
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G,pos)
nx.draw_networkx_edges(G,pos)
nx.draw_networkx_labels(G,pos)

plt.show()


