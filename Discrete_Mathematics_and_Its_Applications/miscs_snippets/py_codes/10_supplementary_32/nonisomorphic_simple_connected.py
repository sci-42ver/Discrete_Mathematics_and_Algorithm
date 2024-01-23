# https://qr.ae/pK60bs Since this exercise main part is not to get all nonisomorphic_simple_connected graphs, so I just use the brute-force method.

import matplotlib.pyplot as plt 
import networkx as nx 
import itertools 
 
n = 3
graphs = [] 
all_nodes = list( range( 1, n+1 ) ) 
all_edges = list( itertools.combinations( all_nodes, r=2 ) ) 
 
for num_edges in range( 0, n*(n-1)//2 + 1): 
    new_graphs = [] 
    for edge_set in itertools.combinations( all_edges, r=num_edges ): 
        g = nx.Graph() 
        g.add_nodes_from( all_nodes ) 
        g.add_edges_from( edge_set ) 
        found = False 
        for existing in new_graphs: 
            if nx.is_isomorphic( g, existing ): 
                found = True 
                break 
        if not found: 
            new_graphs.append( g ) 
    graphs.extend( new_graphs ) 

connected_graphs=[]
for graph in graphs:
    if nx.is_connected(graph)==True:
        connected_graphs.append(graph)
graphs=connected_graphs

columns = min( len( graphs), 7 ) 
rows = (len( graphs ) + columns - 1) // columns 
 
for i, g in enumerate( graphs ): 
    ax = plt.subplot( rows, columns, i+1 ) 
    ax.axis( 'off' ) 
    pos = nx.drawing.layout.circular_layout( g ) 
    nx.drawing.nx_pylab.draw_networkx( g, node_size=30, with_labels=False, 
                                       pos=pos ) 
 
plt.show() 