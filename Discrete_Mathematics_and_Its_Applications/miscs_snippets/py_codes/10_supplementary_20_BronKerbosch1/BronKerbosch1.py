# https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm
"""
> exponentially many maximal cliques 
from https://math.stackexchange.com/a/3618978/1059606
"""
orig_neighbor_list=['befc',
               'aec',
               'abeghdi',
               'ceg',
               'abcdfghi',
               'aeg',
               'efcdih',
               'cegi',
               'cegh']
neighbor_list=[]
for Str in orig_neighbor_list:
  neighbor_list.append([character for character in Str])
R=[]
# notice here end_character should not be wrong.
end_character='i'
P=[chr(ord('a')+idx) for idx in range(ord(end_character)-ord('a')+1)]
X=[]
"""
It just restrain P to neighbors.
X is only to store already used vertices.
And it iterates over all vertices by `for each vertex v in P do`
"""
import copy
def BronKerbosch1(R,P,X):
  if len(P)+len(X)==0:
    print("one maximal clique",'-'.join(R))
    # R=[]
    return
  # Here not use for vertex in P because P is changed in the for loop which will cause the chaos
  while len(P)!=0:
    vertex=P[0] # based on `P.remove(vertex)` this will must access the next vertex in P.
    R_arg=copy.deepcopy(R) # here duplicate to generate the independent cliques which will make R won't be changed by recursive calls
    R_arg.append(vertex)
    # notice here not use duplicate name for different variables.
    P_cap=[vertex_2 for vertex_2 in P if vertex_2 in neighbor_list[ord(vertex)-ord('a')]]
    X_cap=[vertex_2 for vertex_2 in X if vertex_2 in neighbor_list[ord(vertex)-ord('a')]]
    # Not change P,R,X in the call
    BronKerbosch1(R_arg,P_cap,X_cap)
    # P := P \ {v} is not implied by for loop because P_cap will use the whole P
    P.remove(vertex)
    X.append(vertex)
  # return R
BronKerbosch1(R,P,X)