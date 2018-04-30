'''
Created on 29 Apr 2018

@author: Eimg
'''
from main import *
#from Tkinter import *

#root = Tk()
#theLabel = Label(root, text='Fuel Purchasing Optimiser')
#theLabel.pack()
#root.mainloop()

import warnings
from scipy.misc.common import central_diff_weights
warnings.filterwarnings('ignore')
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
 
def PlotGraph(route, graph):
    G = nx.DiGraph(day="Stackoverflow")
    weights = {}
    start = route[0]
    end = route[-1]
    route[0] = ('Start '+route[0])
    route[-1] = ('End '+route[-1])
    for index in range(1, len(route)-1):
        G.add_node(route[index])
 
    for index in graph.weight:
        if index[0] == start:
            weights.update({(route[0], index[1]):graph.weight[index]})
            G.add_weighted_edges_from([(route[0], index[1], graph.weight[index])])
        elif index[1] == end:
            weights.update({(index[0], route[-1]):graph.weight[index]})
            G.add_weighted_edges_from([(index[0], route[-1], graph.weight[index])])
        else:
            weights.update({(index[0], index[1]):graph.weight[index]})
            G.add_weighted_edges_from([(index[0], index[1], graph.weight[index])])
             
     
    plt.figure(figsize=(25,25))
    options = {
        'edge_color': '#FFDEA2',
        'width': 1,
        'with_labels': True,
        'font_weight': 'regular',
    }
    edge_labels=weights
    nx.draw_networkx_edge_labels(G,pos=nx.spring_layout(G, k=0.25, iterations=50),arrows=True,edge_labels=edge_labels)
    nx.draw(G, **options)
    ax = plt.gca()
    ax.collections[0].set_edgecolor("#555555") 
    plt.show()
