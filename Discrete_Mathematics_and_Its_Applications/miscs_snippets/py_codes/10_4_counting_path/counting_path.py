import numpy as np
# 24
adjacency_mat=np.block([
  [np.zeros((3,3)),np.ones((3,3))],
  [np.ones((3,3)),np.zeros((3,3))]
])
num=5
print("exercise 24\nwe need to check the top-right and bottom-left submatrix")
def check_path(adjacency_mat,num,check_entry:tuple=()):
  prec_mat=adjacency_mat
  for i in range(2,num+1):
    prec_mat=np.matmul(prec_mat,adjacency_mat)
    if check_entry==():
      print(f"len: {i}\n{prec_mat}")
    else:
      print(f"len: {i}\n{prec_mat[check_entry[0]-1,check_entry[1]-1]}")
check_path(adjacency_mat,num)
# 26
# https://codereview.stackexchange.com/a/107098
print("\nexercise 26")
num=7
val_list=[1,0,1,1,0,
          1,0,1,1,
          1,0,1,
          1,0,
          1]
def simple_graph_sym_matrix(dim,val_list:list):
  m = np.zeros([dim,dim], dtype=np.double)
  xs,ys = np.triu_indices(dim,k=1)
  if len(val_list)!=(dim**2-dim)/2:
    print("err")
  m[xs,ys] = val_list
  m[ys,xs] = val_list
  m[ np.diag_indices(dim) ] = 0
  return m
adjacency_mat=simple_graph_sym_matrix(6,val_list)
check_path(adjacency_mat,num,(3,4))