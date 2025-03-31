import random
import json
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from node import Node
from edge import Edge

# Function to read nodes and edges from JSON file
def read_input(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)  # Parse JSON into a Python dictionary
    return data[0]['nodes'], data[0]['edges']

# ---- Functions to initialize the spanning tree algorithm ----

# Function to create nodes from node data
def create_nodes(node_data):
    nodes = {}
    for node in node_data:
        nodes[node['name']] = Node(node['name'], node['weight'])
    return nodes

# Function to create edges from edge data
def create_edges(edge_data, nodes):
    edges = []
    for edge_name, weight in edge_data.items():
        node_names = edge_name.split('_')
        edges.append(Edge(nodes[node_names[0]], nodes[node_names[1]], weight))
    return edges

# Function to add edges to nodes
def add_edges_to_nodes(nodes, edges):
    for node_name, node in nodes.items():
        node.addEdges(edgeOfNode(node_name, edges, nodes))

# Function to get all edges that are connected to a node
def edgeOfNode(name, edges, nodes):
    nodeEdges = []
    for edge in edges:
        if edge.nodeInEdge(name):
            nodeEdges.append(edge)
    return nodeEdges

# --- Spanning tree algorithm ---

# Executes the spanning tree algorithm
def executeAlgorithm(nodeList):
    random.shuffle(nodeList)
    
    changed = []
    iteration = 0
    while changed.count(True) > 0 or iteration < nodeList.__len__() ** 2:
        changed = []
        for node in nodeList:
            changed.append(node.sendBPDU())
        iteration += 1
    
    return nodeList

# --- Output ---

# Prints the result of the spanning tree algorithm
def result(nodeList):
    for node in nodeList:
        if node.nextHop.name is node.name:
            print(f"{node.name}: ROOT")
        else:
            print(f"{node.name}: -> {node.nextHop.name}")

if __name__ == '__main__':
    file_path = os.path.join(os.path.dirname(__file__), 'input.json')

    node_data, edge_data = read_input(file_path)
    
    # Create nodes and edges
    nodes = create_nodes(node_data)
    edges = create_edges(edge_data, nodes)
    
    # Add edges to nodes
    add_edges_to_nodes(nodes, edges)
    
    # Start Spanning tree algorithm
    nodeList = executeAlgorithm(list(nodes.values()))
    
    # Print the results
    result(nodeList)