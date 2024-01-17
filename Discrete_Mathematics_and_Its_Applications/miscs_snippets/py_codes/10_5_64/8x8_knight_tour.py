# %%
import matplotlib.pyplot as plt
from matplotlib import colormaps as cm
import networkx as nx
directed_graph=False
G = nx.Graph()
if directed_graph:
  G=nx.DiGraph()
dim_1=8
dim_2=dim_1
num=dim_1*dim_2
def index(i,j,dim_1):
  idx=1+j*dim_1+i
  return idx
def index_to_vertex(idx):
  return (idx,((idx-1)%dim_1,(idx-1)//dim_1))
def vertex_inst(i,j,dim_1):
  return (index(i,j,dim_1),(i,j))
for i in range(dim_1):
  for j in range(dim_2):
    G.add_nodes_from([(index(i,j,dim_1),(i,j))])
def Add_edge(graph,vertex_pair_list,undirected):
  for vertex_pair in vertex_pair_list:
    graph.add_edge(vertex_pair[0],vertex_pair[1])
    if undirected:
      graph.add_edge(vertex_pair[1],vertex_pair[0])
# https://stackoverflow.com/a/11869360/21294350
f1=lambda x,y: (x,y)
f2=lambda x,y: (x,-y)
offset_pair_list=[f(i,j) for i,j in [(1,2),(2,1)] for f in [f1,f2]]
edge_undirected=True
for i in range(dim_1):
  for j in range(dim_2):
    start_vertex=vertex_inst(i,j,dim_1)
    end_vertex={}
    for offset_pair in offset_pair_list:
      (x_off,y_off)=offset_pair
      # Here I don't combine related if although it will be more efficient to have less duplicate similar codes. 
      end_x=i+x_off
      end_y=j+y_off
      if end_x<dim_1 and end_x>=0:
        if end_y<dim_2 and end_y>=0:
          end_vertex=vertex_inst(end_x,end_y,dim_1)
          Add_edge(G,[(start_vertex,end_vertex)],edge_undirected)

# https://stackoverflow.com/a/62161953/21294350
pos = {node:node[1] for node in G.nodes()}
nx.draw(G, pos)
plt.show()

# %%
"""
https://stackoverflow.com/a/58289410/21294350
Here I only temporarily check the colormap, so "import" is not reordered to the beginning.
"""
import numpy as np
fig, (ax1, ax2, ax3) = plt.subplots(3)
x=np.linspace(0,1,64)
sc = ax1.scatter(x,np.ones_like(x), c=x, cmap=cm.get_cmap("jet"))
fig.colorbar(sc, ax=ax1, orientation="horizontal")
plt.show()
plt.figure()

# %%
directed_graph=True
# https://stackoverflow.com/a/31120652/21294350
def candidate_list(adj_mat,vertex_idx,graph):
  orig_list = (adj_mat[:,[vertex_idx]]==1).nonzero()[0]
  return [neighbor_vertex for neighbor_vertex in orig_list 
          if graph.nodes[index_to_vertex(neighbor_vertex+1)]["accessed"]==False]
def degree(vertex_mat_idx,adj_mat,graph):
  return len(candidate_list(adj_mat,vertex_mat_idx,graph))
# not use it due to "Changing the sparsity structure of a csr_matrix is expensive. lil_matrix is more efficient."
def remove_vertex_from_adj_mat(adj_mat,target_vertex_idx):
  adj_mat[:,target_vertex_idx]=0
  adj_mat[target_vertex_idx,:]=0

import copy
hamilton_circuit=nx.Graph()
if directed_graph:
  hamilton_circuit=nx.DiGraph()
hamilton_circuit.nodes=copy.deepcopy(G.nodes)

# start_vertex=vertex(0,0,dim_1)
# next_vertex=vertex(1,2,dim_1)
start_vertex=vertex_inst(0,dim_1-1,dim_1)
next_vertex=vertex_inst(2,dim_1-2,dim_1)
previous_vertex=()

hamilton_circuit_undirected=False
Add_edge(hamilton_circuit,[(start_vertex,next_vertex)],hamilton_circuit_undirected)
adj_mat=nx.adjacency_matrix(G)
for vertex in G.nodes:
  # https://networkx.org/documentation/stable/reference/classes/generated/networkx.Graph.nodes.html
  hamilton_circuit.nodes[vertex]["accessed"] = False
for vertex in [start_vertex,next_vertex]:
  hamilton_circuit.nodes[vertex]["accessed"] = True

def add_vertex(next_vertex,x,y,hamilton_circuit):
  previous_vertex=next_vertex
  # See this https://nedbatchelder.com/text/names.html from https://stackoverflow.com/questions/575196/why-can-a-function-modify-some-arguments-as-perceived-by-the-caller-but-not-oth#comment88016253_575196
  # Here one new tuple is created and assigned to the local similar to `a_list = a_list + [val, val]`, so next_vertex won't influence the global next_vertex
  # But `hamilton_circuit.add_edge` will change `hamilton_circuit` in place, so it will work (similar to `a_list.append(4)`).
  next_vertex=vertex_inst(x,y,dim_1)
  Add_edge(hamilton_circuit,[(previous_vertex,next_vertex)],hamilton_circuit_undirected)
  hamilton_circuit.nodes[next_vertex]["accessed"] = True
  return next_vertex,hamilton_circuit
more_stricted=True
if more_stricted:
  # notice whether same id for the function parameter and passed-in variable is not always the same case
  # https://stackoverflow.com/questions/59877044/why-do-variables-have-same-id-when-they-are-passed-by-value-in-python#comment105883903_59877044
  next_vertex,hamilton_circuit=add_vertex(next_vertex,2*2,dim_1-1,hamilton_circuit)

next_vertex_idx=next_vertex[0]-1

edge_color_bool=True
edge_color_end_vertex=vertex_inst(0,dim_2-2,dim_1)
edge_color_map={}

# https://stackoverflow.com/a/20133763/21294350
# check map value https://stackoverflow.com/a/58289410/21294350
val_map={start_vertex:0.57}
while next_vertex!=start_vertex:
  candidate_vertex_list=candidate_list(adj_mat,next_vertex_idx,hamilton_circuit)
  if len(candidate_vertex_list)!=0:
    # > move to a square connected to the fewest number of unused squares
    min_degree=degree(candidate_vertex_list[0],adj_mat,hamilton_circuit)
    target_vertex_idx=candidate_vertex_list[0]
    for vertex_idx in candidate_vertex_list[1:]:
      if degree(vertex_idx,adj_mat,hamilton_circuit)<min_degree:
        min_degree=degree(vertex_idx,adj_mat,hamilton_circuit)
        target_vertex_idx=vertex_idx
    previous_vertex=copy.deepcopy(next_vertex)
    next_vertex=index_to_vertex(target_vertex_idx+1)
    hamilton_circuit.nodes[next_vertex]["accessed"] = True
    Add_edge(hamilton_circuit,[(previous_vertex,next_vertex)],hamilton_circuit_undirected)
    if edge_color_bool and next_vertex==edge_color_end_vertex:
      for edge in hamilton_circuit.edges:
        edge_color_map[edge]=0.9
    next_vertex_idx=next_vertex[0]-1
  else:
    val_map[next_vertex]=0.57
    break
access_vertex_num=sum([hamilton_circuit.nodes[vertex]["accessed"] == True for vertex in hamilton_circuit.nodes])

for node in hamilton_circuit.nodes():
  if node not in hamilton_circuit:
    val_map[node]=0.72

col_values = [val_map.get(node, 0.25) for node in hamilton_circuit.nodes()]
edge_col_values = [edge_color_map.get(edge, 0) for edge in hamilton_circuit.edges]

"""
https://stackoverflow.com/a/58289410/21294350
Here I only temporarily check the colormap, so "import" is not reordered to the beginning.
"""
# import numpy as np
# fig, (ax1, ax2, ax3) = plt.subplots(3)
# x=np.linspace(0,1,64)
# sc = ax1.scatter(x,np.ones_like(x), c=x, cmap=cm.get_cmap("jet"))
# fig.colorbar(sc, ax=ax1, orientation="horizontal")
# plt.show()
# plt.figure()

if access_vertex_num!=len(hamilton_circuit.nodes):
  # By this https://qr.ae/pKqM5Y the program may fail sometimes, and 
  # https://stackoverflow.com/a/8414849/21294350 which indicates that the improved version still doesn't ensure the solution always.
  print(f"err {access_vertex_num}")
# https://stackoverflow.com/a/62161953/21294350
pos = {node:node[1] for node in hamilton_circuit.nodes()}
print(col_values)
# 1. https://stackoverflow.com/a/32440460/21294350 here must use [vmin,vmax] to set the range to avoid auto setting by nx
# > networkx's interface to maptlotlib will do it for you
# 2. We can also use the directed graph to show the path, but since the original graph is undirected, so I don't do this.
nx.draw_networkx(hamilton_circuit, pos,
                 cmap=cm.get_cmap('jet'),
                 node_color = col_values,
                 with_labels=False,
                 vmin=0,vmax=1,
                 nodelist=G.nodes,
                #  edge parameter
                 edge_color=edge_col_values,
                 edge_cmap=cm.get_cmap('jet'),
                 width=2.0,
                 edge_vmin=0.0,edge_vmax=1.0,
                 arrows=directed_graph)
plt.show()

# %%
