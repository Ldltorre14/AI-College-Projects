from graph import Node
from graph import Graph


class vacuumCleaner(Node):
    def __init__(self):
        self.score = 0
        self.traveled_Distance = 0
        self.previousConfig = []
        self.toVisit = []
        self.visited = []
        
