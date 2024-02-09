# https://qr.ae/pK60bs Since this exercise main part is not to get all nonisomorphic_simple_connected graphs, so I just use the brute-force method.

import matplotlib.pyplot as plt 
import networkx as nx 
import itertools
 
n = 3
"""
1. https://www.baeldung.com/cs/cycles-undirected-graph may be wrong.
    I follow this https://www.geeksforgeeks.org/detect-cycle-undirected-graph/
    1.1 Here parent_vertex is not same as the term in the tree.
    TODO DFS validity proof
2. Here p634 transitive closure method will be wrong because the symmetric matrix will always make the diagonal having 1.
"""
# A recursive function that uses
# visited[] and parent to detect
# cycle in subgraph reachable from vertex v.
def isCyclicUtil(v, visited, parent,adjacency_list):

    # Mark the current node as visited
    visited[v] = True

    # Recur for all the vertices
    # adjacent to this vertex
    for i in adjacency_list[v]:

        # If the node is not
        # visited then recurse on it
        if visited[i] == False:
            if(isCyclicUtil(i, visited, v,adjacency_list)):
                return True
        # If an adjacent vertex is
        # visited and not parent
        # of current vertex,
        # then there is a cycle
        elif parent != i:
            return True

    return False

# Returns true if the graph
# contains a cycle, else false.

def isCyclic(graph:nx.classes.graph.Graph,vertex_num):

    adjacency_list=[]
    adj_mat=nx.adjacency_matrix(graph).todense()
    for i in range(adj_mat.shape[0]):
        adjacency_list.append([idx for idx,elem in enumerate(adj_mat[i,:]) if elem == 1])

    # Mark all the vertices
    # as not visited
    visited = [False]*(vertex_num)

    # Call the recursive helper
    # function to detect cycle in different
    # DFS trees
    for i in range(vertex_num):

        # Don't recur for u if it
        # is already visited
        if visited[i] == False:
            if(isCyclicUtil
                (i, visited, -1,adjacency_list)) == True:
                return True

    return False


# def check_cycle_one_vertex(vertex,visited_map,parent_vertex):

"""
Here I modify based on the online version above. 
"""
# def Check_cycle(adj_mat:np.ndarray):
#     find_cycle=False
#     num=0
#     A_power=copy.deepcopy(adj_mat)
    # visited_map={}
    # for i in range(adj_mat.shape()[0]):
    #     visited_map[i]=False
    
    # if type(adj_mat)==np.ndarray:
    #     while num!=n and find_cycle==False:
    #         A_power*=adj_mat
    #         num+=1
    #         if 1 in A_power.diagonal():
    #             find_cycle=True
    # elif type(adj_mat)==scipy.sparse._csr.csr_array:
    #     while num!=n and find_cycle==False:
    #         A_power=A_power @ adj_mat
    #         num+=1
    #         if 1 in A_power.diagonal():
    #             find_cycle=True
    # return find_cycle

def graph_n(n,check_cycle=False):
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

    if check_cycle:
        Use_theorem_edge_number=True
        tree_graphs=[]
        for graph in graphs:
            if not Use_theorem_edge_number:
                if not isCyclic(graph,len(graph.nodes)):
                    tree_graphs.append(graph)
            else:
                if len(graph.edges())==len(graph.nodes())-1:
                    tree_graphs.append(graph)
        graphs=tree_graphs


    columns = min( len( graphs), 7 ) 
    rows = (len( graphs ) + columns - 1) // columns 
    
    for i, g in enumerate( graphs ): 
        ax = plt.subplot( rows, columns, i+1 ) 
        ax.axis( 'off' ) 
        pos = nx.drawing.layout.circular_layout( g ) 
        nx.drawing.nx_pylab.draw_networkx( g, node_size=30, with_labels=False, 
                                        pos=pos ) 
    
    plt.show()
ONLY_TREE=True
if not ONLY_TREE:
    graph_n(5)
    # basis step https://math.stackexchange.com/q/4849754/1059606
    graph_n(3)
# # 11.1-12
# graph_n(4,True)
# # 11.1-13
# graph_n(5,True)
# # 11.1-11 (38 is labelled instead of unlabelled)
# graph_n(3,True)
# 11-supplementary 2
graph_n(6,True)