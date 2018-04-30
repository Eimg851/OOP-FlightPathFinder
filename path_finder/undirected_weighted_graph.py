'''
Created on 27 Apr 2018

@author: Eimg
'''
import collections
import math

class undirectedWeightedGraph:
    """
    Undirected Weighted Graph: allows edges to be created between nodes in the graph
    """
    def __init__(self, setOfAirports):
        """
        Constructs the graph
        """
        self.vertices = setOfAirports
        #makes the default value for all vertices an empty list
        self.edge = collections.defaultdict(list)
        self.weights = {}
        
    def add_vertex(self, value):
        """
        Adds vertices to the graph
        """
        self.vertices.add(value)
        
    def add_edge(self, from_vertex, to_vertex, distance):
        """"
        Adds edges between nodes in the graph
        """
        if from_vertex == to_vertex: pass #no cycles allowed
        self.edge[from_vertex].append(to_vertex)
        self.edge[to_vertex].append(from_vertex) # undirected graph
        self.weights[(from_vertex, to_vertex)] = distance
        self.weights[(to_vertex, from_vertex)] = distance #undirected graph
    
    def __str__(self):
        """
        Returns the graph in human readable form
        """
        string ="Vertices: "+str(self.vertices)+ "\n"
        string += "Edges: "+str(self.edge) + "\n"
        string += "Weights: "+ str(self.weights)
        return string