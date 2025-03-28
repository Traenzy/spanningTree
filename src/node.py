class Node:
    def __init__(self, name, id, pEdges=None):
        self.name = name
        self.id = id
        self.pEdges = pEdges
        self.nextHop = self # Every node thinks it is the root in the beginning

    def addEdges(self, edges):
        self.pEdges = edges
    
    # Function to get the edge to a directly connected node
    def getEdgeToNeighbour(self, nodeName):
        for edge in self.pEdges:
            if edge.getNeighbour(self).name == nodeName:
                return edge
        return None

    def sendBPDU(self):
        nextHop = self.nextHop
        # Send BPDU to all connected neighbours
        for edge in self.pEdges:
            edge.getNeighbour(self).receiveBPDU(self, nextHop)

    def receiveBPDU(self, node, toRoot):
        # Receive ID of Node and weight decide if it is better than current to root
        edgeToNode = self.getEdgeToNeighbour(node.name)
        # Todo: possibleWeight = toRoot.id + edgeToNode.weight # Weight of the maybe new path to root
    
        if self.nextHop.id > toRoot.id:
            self.nextHop = node
        # Todo: Else if the costs of new path are lower than the current path change path
    
    def __str__(self):
        return f"{self.name}: {self.id}"
