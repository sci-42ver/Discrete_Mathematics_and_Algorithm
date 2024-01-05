# https://stackoverflow.com/a/45159105/21294350 from https://stackoverflow.com/a/64448213/21294350
first,second=[[1,0,0,1,0,0],[0,1,1,1,0,0]], [[0,1],[1,1],[1,0],[1,0],[1,1],[0,1]]
from itertools import starmap
from operator import mul
# https://stackoverflow.com/a/1790532/21294350
import operator
from functools import *
import re
def my_or(a_list):
  # here set init with 0 to not influence further "or" operation
  return reduce(operator.or_, a_list, 0)
my_or([1,0,1])
# diff from map is how they manipulate with args https://www.educative.io/answers/what-is-the-itertoolsstarmap-method-in-python 
def Boolean_product(mat_1,mat_2):
  return [[my_or(starmap(mul, zip(row, col))) for col in zip(*mat_2)] for row in mat_1]
# https://stackoverflow.com/a/534866/21294350
def one_dim_minus_list(row_1,row_2):
  return [a_i - b_i for a_i, b_i in zip(row_1, row_2)]
# mat_1<=mat_2?
def check_less_equal(mat_1,mat_2):
  minus_mat=[one_dim_minus_list(row_1, row_2) for row_1, row_2 in zip(mat_1,mat_2)]
  # or use `any` https://stackoverflow.com/a/40514152/21294350
  for row_index,row in enumerate(minus_mat):
    for col_index,elem in enumerate(row):
      if elem==1:
        print(f"not transitive for ({row_index+1},{col_index+1})")
Mat_list=[[[1,1,0,1],[1,0,1,0],[0,1,1,1],[1,0,1,1]],
  [[1,1,1,0],[0,1,0,0],[0,0,1,1],[1,0,0,1]],
  [[0,1,0,1],[1,0,1,0],[0,1,0,1],[1,0,1,0]]]
def check_transitive(Mat_list):
    for Index,Mat in enumerate(Mat_list):
        print(f"check {Index}")
        check_less_equal(Boolean_product(Mat,Mat),Mat)
check_transitive(Mat_list)
# directly use the book data
Data_str_list=["""1 1 0 1 
1 0 1 0 
0 1 1 1 
1 0 1 1""","""1 1 1 0 
0 1 0 0 
0 0 1 1 
1 0 0 1""","""0 1 0 1 
1 0 1 0 
0 1 0 1 
1 0 1 0"""]
def str_lists_to_mat(Str_list,row_size):
  Data_lists=[re.split(' [\\n]*',Str) for Str in Str_list]
  Data_lists=[[int(elem) for elem in data_list] for data_list in Data_lists]
  Mat_list=[[data_list[i:i+row_size] for i in range(0, len(data_list), row_size)] for data_list in Data_lists]
  return Mat_list
row_size=4
Mat_list=str_lists_to_mat(Data_str_list,row_size)
# use numpy
import numpy as np
def nested_list_to_mat(nested_list:list[list]):
  return np.array([np.array(xi) for xi in nested_list])
for Index,Mat in enumerate(Mat_list):
  print(f"check {Index}")
  minus_mat=nested_list_to_mat(Boolean_product(Mat,Mat))-nested_list_to_mat(Mat)
  if any(1 in sl for sl in minus_mat):
    print("not transitive")
# 14
# R_1,R_2
Data_str_list=["""0 1 0 
1 1 1 
1 0 0""","""0 1 0 
0 1 1 
1 1 1"""]
Data_lists=str_lists_to_mat(Data_str_list,3)
# 14.c)
print(nested_list_to_mat(Boolean_product(Data_lists[0],Data_lists[1])))
# 14.d)
print(nested_list_to_mat(Boolean_product(Data_lists[0],Data_lists[0])))
##########################################################################################
# 9.5-exercise-24
##########################################################################################
Data_str_list=["""1 0 1 0 
0 1 0 1 

1 0 1 0 
0 1 0 1""","""
1 1 1 0 
1 1 1 0 

1 1 1 0 
0 0 0 1"""]
row_size=4
Data_lists=str_lists_to_mat(Data_str_list,row_size)
check_transitive(Data_lists)
# check by submatrix
Data_lists=[nested_list_to_mat(Mat) for Mat in Data_lists]
submat=lambda Mat,idxes:Mat[np.ix_(idxes,idxes)]
def check_sub_mat(Mat,whether_continue_check:bool,row_idx_arr_in_orig_mat):
  row=Mat[0,:]
  # since we start from 1st row and remove submatrix then, the rest mat always has mat[0,0]=1, i.e. it must has index 0
  # https://stackoverflow.com/a/69329288/21294350
  target_row_idxes=np.delete(np.argwhere(row==1),0)
  for row_idx in target_row_idxes:
    if not np.array_equal(Mat[row_idx,:],row):
      whether_continue_check=False
      print("not one equivalence relation")
  find_sub_mat_idx=np.insert(target_row_idxes,0,0)
  print(f"find submat in the Orig_Mat {row_idx_arr_in_orig_mat[find_sub_mat_idx]}:\
        \n{submat(Mat,find_sub_mat_idx)}")
  if whether_continue_check:
    # https://stackoverflow.com/a/36460734/21294350 this is not used.
    row_idx_arr_in_orig_mat=np.delete(row_idx_arr_in_orig_mat,find_sub_mat_idx)
    # https://stackoverflow.com/a/19161690/21294350
    # by this https://stackoverflow.com/a/11585878/21294350 the LHS is local variable instead of the arg
    # Mat=Mat[np.ix_(row_idx_arr,row_idx_arr)]
    return submat(Mat,row_idx_arr_in_orig_mat),row_idx_arr_in_orig_mat
  else:
    return None
# Here Mat can't be changed https://stackoverflow.com/a/9414582/21294350
# maybe due to next() method will overload it https://wiki.python.org/moin/Iterator.
import copy
for Mat in Data_lists:
  row_size=4
  whether_equivalence_relation=True
  # https://numpy.org/doc/stable/reference/generated/numpy.copy.html
  target_Mat=copy.deepcopy(Mat)
  row_idx_arr=np.array(range(np.shape(Mat)[0]))
  while np.size(target_Mat)!=0 and whether_equivalence_relation:
    # notice how to return tuple https://stackoverflow.com/a/354929/21294350
    target_Mat,row_idx_arr=check_sub_mat(target_Mat,whether_equivalence_relation,row_idx_arr)