class Edge:
    def __init__(self, node1, node2, weight):
        self.node1 = node1
        self.node2 = node2
        self.weight = weight
    
    # Function to get the the other node of the edge
    def getNeighbour(self, node):
        if node.name == self.node1.name:
            return self.node2
        else:
            return self.node1
        
    def nodeInEdge(self, nodeName):
        if nodeName in self.node1.name or nodeName in self.node2.name:
            return True
        return False
        
    def __str__(self):
        return f"{self.node1.name} - {self.node2.name}: {self.weight}"
    
