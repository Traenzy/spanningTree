from edge import Edge
# --- Static functions to initialize nodes and edges ---

# Function to create nodes from node data
def create_nodes(node_data):
    nodes = {}
    for node in node_data:
        nodes[node['name']] = Node(node['name'], node['id'])
    return nodes

# Function to add edges to nodes
# Goes through all nodes and adds the edges that are connected to the node
def add_edges_to_nodes(nodes, edges):
    for node in nodes:
        node.addEdges(edgeOfNode(node.name, edges))

# Function to get all edges that are connected to a node
# Goes though all edges and checks if the node is in the edge
def edgeOfNode(nodeName, edges):
    nodeEdges = []
    for edge in edges:
        if edge.nodeInEdge(nodeName):
            nodeEdges.append(edge)
    return nodeEdges

class Node:
    def __init__(self, name, id, pEdges=None):
        self.name = name
        self.id = id
        self.pEdges = pEdges
        self.nextHop = self # Every node thinks it is the root in the beginning
        self.root = {
            "node": self,
            "weight": 0
        } # Every node thinks it is the root in the beginning

    def addEdges(self, edges):
        self.pEdges = edges
    
    # Function to get the edge to a directly connected node
    def getEdgeToNeighbour(self, nodeName):
        for edge in self.pEdges:
            if edge.getNeighbour(self).name == nodeName:
                return edge
        return None

    def sendBPDU(self):
        # Send BPDU to all connected neighbours
        changed = False
        for edge in self.pEdges:
            changed = edge.getNeighbour(self).receiveBPDU(self, self.root)
        return changed

    def receiveBPDU(self, node, toRoot):
        changed = False # Flag to check if the root has changed
        # Receive ID of Node and weight decide if it is better than current to root
        edgeToNode = self.getEdgeToNeighbour(node.name)
        possibleWeight = toRoot["weight"] + edgeToNode.weight # Weight of the maybe new path to root
    
        # Root ID is higher than ID of BPDU
        if self.root['node'].id > toRoot['node'].id:
            self.nextHop = node # Change nextHop to the node that sent the BPDU
            self.root['node'] = toRoot['node']  # Change root to the root of the BPDU
            self.root['weight'] = possibleWeight
            changed = True
        # Same Root ID but BPDU has lower weight
        elif self.root['node'].id == toRoot['node'].id and self.root['weight'] > possibleWeight:
            self.nextHop = node
            self.root['weight'] = possibleWeight
            changed = True
        return changed
    
    def __str__(self):
        return f"{self.name}: {self.id}"
