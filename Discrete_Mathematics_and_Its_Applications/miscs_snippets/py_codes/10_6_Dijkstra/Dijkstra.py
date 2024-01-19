"""
Since this algorithm is used often and implemented already,
so I just use one online ready-made version.
"""
# Dijkstra's Algorithm in Python


import sys
import copy

# Providing the graph
vertices = [[0, 0, 1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 1, 0],
            [1, 1, 0, 1, 1, 0, 0],
            [1, 0, 1, 0, 0, 0, 1],
            [0, 0, 1, 0, 0, 1, 0],
            [0, 1, 0, 0, 1, 0, 1],
            [0, 0, 0, 1, 0, 1, 0]]

edges = [[0, 0, 1, 2, 0, 0, 0],
         [0, 0, 2, 0, 0, 3, 0],
         [1, 2, 0, 1, 3, 0, 0],
         [2, 0, 1, 0, 0, 0, 1],
         [0, 0, 3, 0, 0, 2, 0],
         [0, 3, 0, 0, 2, 0, 1],
         [0, 0, 0, 1, 0, 1, 0]]

#########################################################################
# 10.6-2
#########################################################################
edge_list={('a','b'):2,
           ('d','b'):5,
           ('d','f'):2,
           ('e','f'):4,
           ('e','c'):5,
           ('a','c'):3,
           ('b','e'):2,
           ('d','e'):1}
idx_to_str=lambda idx:chr(idx+ord('a'))
def edge_list_to_dist_mat_and_adjacency_mat(edge_list):
    # https://stackoverflow.com/a/73153615/21294350 https://stackoverflow.com/a/17016257/21294350
    vertex_pairs=[vertex for edge_dist in edge_list for vertex in edge_dist]
    vertex_cnt=len(list(dict.fromkeys(vertex_pairs)))
    # 1. This will access the global variable if using the same name similar to `global_var1` based on the language properties. 
    # https://stackoverflow.com/a/293097/21294350
    # 2. not use [[0]*vertex_cnt]*vertex_cnt which will duplicate sublist with the same id.
    Vertices=[[0]*vertex_cnt for i in range(vertex_cnt)]
    Edges=copy.deepcopy(Vertices)
    for key, value in edge_list.items():
        vertex_idx=tuple(ord(vertex)-ord('a') for vertex in key)
        for idx in [vertex_idx,vertex_idx[::-1]]:
          Vertices[idx[0]][idx[1]]=1
          Edges[idx[0]][idx[1]]=value
    return Vertices,Edges
vertices,edges=edge_list_to_dist_mat_and_adjacency_mat(edge_list)

# Find which vertex is to be visited next
def to_be_visited(visited_and_distance,num_of_vertices):
    v = -10
    for index in range(num_of_vertices):
        """
        In the original code, here `v < 0` is to ensure `visited_and_distance[v][1]` work by using the short circuit.
        """
        if visited_and_distance[index][0] == 0 \
            and (v < 0 or visited_and_distance[index][1] <=
                 visited_and_distance[v][1]):
            v = index
    return v

def find_shortest_path(vertices,edges,start_vertex):
  num_of_vertices = len(vertices[0])

  # initial infinite 
  visited_and_distance = [[0, sys.maxsize] for i in range(num_of_vertices)]

  start_vertex=start_vertex
  visited_and_distance[start_vertex][1]=0
  path_list={}
  for i in range(num_of_vertices):
      path_list[idx_to_str(i)]=idx_to_str(start_vertex)

  for vertex in range(num_of_vertices):

      # Find next vertex to be visited
      to_visit = to_be_visited(visited_and_distance,num_of_vertices)
      for neighbor_index in range(num_of_vertices):

          # Updating new distances
          if vertices[to_visit][neighbor_index] == 1 and \
                  visited_and_distance[neighbor_index][0] == 0:
              new_distance = visited_and_distance[to_visit][1] \
                  + edges[to_visit][neighbor_index]
              if visited_and_distance[neighbor_index][1] > new_distance:
                  visited_and_distance[neighbor_index][1] = new_distance
                  """
                  1. Since the modification is not one for loop which won't influence the complexity much,
                  I just modify the path list when the path is possible although it may be not the minimal 
                  which will be chosen and must be the global shortest path at the next iteration.
                  2. This is same as exercise 16 P(v)=u where u=path_list[idx_to_str(to_visit)]
                  """
                  path_list[idx_to_str(neighbor_index)]=path_list[idx_to_str(to_visit)]+f'-{idx_to_str(neighbor_index)}'
          
          visited_and_distance[to_visit][0] = 1

  i = 0

  # Printing the distance
  for distance in visited_and_distance:
      print("Distance of ", idx_to_str(i),
            f" from source vertex: {idx_to_str(start_vertex)}", distance[1],
            f"with path {path_list[idx_to_str(i)]}")
      i = i + 1
  print()

find_shortest_path(vertices,edges,0)

"""
Added
"""
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
def Draw(vertices,edges):
  num_of_vertices=len(vertices[0])
  Dist = np.array(edges)
  G = nx.from_numpy_array(Dist)
  G = nx.relabel_nodes(G, {i:idx_to_str(i) for i in range(num_of_vertices)})
  Edge_labels={}
  # https://networkx.org/documentation/stable/reference/generated/networkx.convert_matrix.from_numpy_array.html
  for edge in G.edges(data=True):
      Edge_labels[(edge[0],edge[1])]=edge[2]['weight']
  pos=nx.spring_layout(G,seed=1,k=1,iterations=20)
  # https://stackoverflow.com/a/47135311/21294350
  nx.draw(G, pos,
          labels={node: node for node in G.nodes()},
          node_color='white', alpha=0.5,
          font_color='red',font_weight='bold',font_size=20)
  nx.draw_networkx_edge_labels(
      G, pos,
      edge_labels=Edge_labels,
      font_color='green',font_size=20
  )
  plt.draw()  # pyplot draw()
  plt.show()
Draw(vertices,edges)

#########################################################################
# 10.6-4
#########################################################################
edges=[[0, 2, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 3, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 5, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 3, 3, 2, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 8, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 6, 3, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 2, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 6, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 4, 2, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 6, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 3, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
edges=np.array(edges)+np.array(edges).T
vertices=np.where(edges > 0, 1, 0)
edges=list(edges)
vertices=list(vertices)
find_shortest_path(vertices,edges,0)
Draw(vertices,edges)

#########################################################################
# 10.6-6
#########################################################################
edges=[[0, 4, 3, 0, 0, 0, 0, 0],
       [0, 0, 2, 5, 0, 0, 0, 0],
       [0, 0, 0, 3, 6, 0, 0, 0],
       [0, 0, 0, 0, 1, 5, 0, 0],
       [0, 0, 0, 0, 0, 0, 5, 0],
       [0, 0, 0, 0, 0, 0, 2, 7],
       [0, 0, 0, 0, 0, 0, 0, 4],
       [0, 0, 0, 0, 0, 0, 0, 0]]
start_vertex_list=[0,1,2]
def check_with_edge_AND_start_vertex(edges,start_vertex_list):
    edges=np.array(edges)+np.array(edges).T
    vertices=np.where(edges > 0, 1, 0)
    edges=list(edges)
    vertices=list(vertices)
    for start_vertex in start_vertex_list:
        find_shortest_path(vertices,edges,start_vertex)
    Draw(vertices,edges)
check_with_edge_AND_start_vertex(edges,start_vertex_list)