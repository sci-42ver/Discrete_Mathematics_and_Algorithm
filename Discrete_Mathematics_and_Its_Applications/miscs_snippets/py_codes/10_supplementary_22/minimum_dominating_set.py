"""
Since I don't have time to study all algorithms,
So I here just use the brute-force, although it has one factor `n` with the current possible best algorithm.
https://en.wikipedia.org/wiki/Dominating_set#Exact_algorithms
"""
orig_neighbor_list=[]
idx_to_character=lambda idx:chr(ord('a')+idx)
# notice here not append list but we should append str.
orig_neighbor_list.append('be')
for i in range(1,2+1):
  orig_neighbor_list.append(idx_to_character(i-1)+idx_to_character(i+1)+idx_to_character(i+4))
orig_neighbor_list.append('ch')
orig_neighbor_list.append('afi')
for i in range(1+4,2+4+1):
  orig_neighbor_list.append(idx_to_character(i-4)+idx_to_character(i-1)+idx_to_character(i+1)+idx_to_character(i+4))
orig_neighbor_list.append('dgl')
orig_neighbor_list.append('ej')
for i in range(1+4*2,2+4*2+1):
  orig_neighbor_list.append(idx_to_character(i-1)+idx_to_character(i+1)+idx_to_character(i+4))
orig_neighbor_list.append('hk')

neighbor_list=[]
for Str in orig_neighbor_list:
  neighbor_list.append([character for character in Str])

end_character='l'
vertex_list=[chr(ord('a')+idx) for idx in range(ord(end_character)-ord('a')+1)]

import itertools
def find_minimum_dominating_set(vertex_list,neighbor_list,whether_str):
  find=False
  target_vertices=[]
  for L in range(len(vertex_list) + 1):
      if find:
          break
      for subset in itertools.combinations(vertex_list, L):
          if find:
            break
          other_vertices=[vertex for vertex in vertex_list if vertex not in subset]
          adjacent_vertices=[]
          for vertex in subset:
            #  here not use append because it will use one list as elements instead of elements of the list.
            if whether_str:
              adjacent_vertices+=[vertex_2 for vertex_2 in neighbor_list[ord(vertex)-ord('a')] if vertex_2 not in adjacent_vertices]
            else:
              adjacent_vertices+=[vertex_2 for vertex_2 in neighbor_list[vertex] if vertex_2 not in adjacent_vertices]
          not_adjacent_vertices=[vertex for vertex in other_vertices if vertex not in adjacent_vertices]
          if len(not_adjacent_vertices)==0:
            find=True
            target_vertices=subset
  return target_vertices
print(find_minimum_dominating_set(vertex_list,neighbor_list,True))

# 27
import numpy as np
def chess_neighbor_list(dim):
  neighbor_list=[]
  for i in range(dim**2):
    a = np.zeros((dim,dim))
    target_idx=(i//dim,i%dim)
    a[target_idx[0],:]=1
    a[:,target_idx[1]]=1
    # https://stackoverflow.com/a/49452560/21294350
    major_start=[0,target_idx[0]-target_idx[1]] if (target_idx[0]>target_idx[1]) else [target_idx[1]-target_idx[0],0]
    while major_start[0]<dim and major_start[1]<dim:
      a[major_start[0],major_start[1]]=1
      major_start[0]+=1
      major_start[1]+=1
    # https://stackoverflow.com/a/46135971/21294350
    minor_start=[0,target_idx[0]+target_idx[1]] if (target_idx[0]+target_idx[1]<dim) else [target_idx[1]+target_idx[0]-(dim-1),dim-1]
    while minor_start[0]<dim and minor_start[0]>=0 and minor_start[1]>=0 and minor_start[1]<dim:
      a[minor_start[0],minor_start[1]]=1
      minor_start[0]+=1
      minor_start[1]-=1
    a[target_idx]=0
    adjacent_idx=np.where(a==1)
    neighbor_list.append(list(adjacent_idx[0]*dim+adjacent_idx[1]))
  return neighbor_list
for dim in range(3,5+1):
  neighbor_list=chess_neighbor_list(dim)
  idx_list=find_minimum_dominating_set(list(range(dim**2)),neighbor_list,False)
  print([(idx//dim,idx%dim) for idx in idx_list])