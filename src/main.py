from node import Node
from edge import Edge

# Returns all edges that are connected to the node
def edgeOfNode(name, edges, nodes):
    nodeEdges = []
    for edge in edges:
        if name in edge["name"]:
            nameNames = edge["name"].split("_")
            nodeEdges.append(Edge(nodes[nameNames[0]], nodes[nameNames[1]], edge["weight"]))
    return nodeEdges

if __name__ == '__main__':
    edges = [
        {"name": "A_B", "weight": 10},
        {"name": "A_C", "weight": 10},
        {"name": "B_D", "weight": 15},
        {"name": "B_E", "weight": 10},
        {"name": "C_D", "weight": 3},
        {"name": "C_E", "weight": 10},
        {"name": "D_E", "weight": 2},
        {"name": "D_F", "weight": 10},
        {"name": "E_F", "weight": 2}
    ]
    nodes = {
        "A": Node("A", 5),
        "B": Node("B", 1),
        "C": Node("C", 3),
        "D": Node("D", 7),
        "E": Node("E", 6),
        "F": Node("F", 4),
    }
    
    # Add neighbour edges to nodes
    for node_name, node in nodes.items():
        node.addEdges(edgeOfNode(node_name, edges, nodes))
    
    # Start Spanning tree algorithm
    for i in range(49):
        for node in nodes.values():
            node.sendBPDU()
    
    # Print the results
    for node_name, node in nodes.items():
        print(f"Result: {node_name}: {node.nextHop}")

    # Send BPDUs from all Nodes to directly connected Nodes
