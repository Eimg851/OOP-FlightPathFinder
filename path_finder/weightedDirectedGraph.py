'''
Created on 25 Apr 2018

@author: Eimg
'''
import collections
import math

class directedWeightedGraph:
    """
    Weighted Directed Graph: allows directed edges that carry weights to be created between nodes in the graph
    """
    def __init__(self, setOfAirports):
        """
        Constructs the graph
        """
        self.vertices = setOfAirports
        #makes the default value for all vertices an empty list
        self.edge = collections.defaultdict(list)
        self.weight = {}
        
    def add_vertex(self, value):
        """
        Adds vertices to the graph
        """
        self.vertices.add(value)
        
    def add_edge(self, from_vertex, to_vertex, distance):
        """
        Adds edges that carry a certain weight between nodes in the graph
        """
        if from_vertex == to_vertex: pass #no cycles allowed
        self.edge[from_vertex].append(to_vertex)
        self.weight[(from_vertex, to_vertex)] = distance

    def __str__(self):
        """
        Returns the graph in human readable form
        """
        string ="Vertices: "+str(self.vertices)+ "\n"
        string += "Edges: "+str(self.edge) + "\n"
        string += "Weights: "+ str(self.weight)+ "\n"
        string += "Total number of nodes on this graph: "+str(len(self.vertices))
        return string
        
    def dijkstra(self, start):
        # initializations
        S = set()
        # delta represents the length shortest distance paths from start -> v, for v in delta.
        delta = dict.fromkeys(list(self.vertices), math.inf)
        previous = dict.fromkeys(list(self.vertices), None)
    
        # then we set the path length of the start vertex to 0
        delta[start] = 0
    
        # while there exists a vertex v not in S
        while S != self.vertices:
            # let v be the closest vertex that has not been visited...it will begin at 'start'
            v = (set(delta.keys()).difference(S)), key=delta.get)
    
            # for each neighbor of v not in S
            for neighbor in set(self.edge[v]) - S:
                new_path = delta[v] + self.weight[v,neighbor]
    
                # is the new path from neighbor through
                if new_path < delta[neighbor]:
                    # since it's optimal, update the shortest path for neighbor
                    delta[neighbor] = new_path
    
                    # set the previous vertex of neighbor to v
                    previous[neighbor] = v
            S.add(v)
    
        return (delta, previous)
     
     
     
    def shortest_path(self, start, end):
        '''Uses dijkstra function in order to output the shortest path from start to end
        '''
        delta, previous = self.dijkstra(start)
    
        path = []
        vertex = end
    
        while vertex is not None:
            path.append(vertex)
            vertex = previous[vertex]
    
        path.reverse()
        return path
    
    