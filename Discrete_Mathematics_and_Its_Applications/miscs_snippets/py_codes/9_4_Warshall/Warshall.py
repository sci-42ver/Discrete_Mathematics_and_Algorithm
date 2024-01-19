#########################################################################
# 9.4-EXAMPLE 8
#########################################################################
"""
I wrote this code before reading the Lemma 2
In Lemma 2
1. w_{ij}^{[k-1]} is here `Mat` only changing necessary with the rest unchanged.
2. w_{ik}^{[k-1]} \wegde w_{kj}^{[k-1]} corresponds to `Mat[:,init_subscript]` and `Mat[init_subscript,:]`
"""
import re
import numpy as np
check_list=["""0 0 0 1 
1 0 1 0 
1 0 0 1 
0 0 1 0"""]
def nested_list_to_mat(nested_list:list[list]):
    return np.array([np.array(xi) for xi in nested_list])
def str_lists_to_mat(Str_list,row_size):
    Data_lists=[re.split(' [\\n]*|\\n',Str) for Str in Str_list]
    Data_lists=[[int(elem) for elem in data_list] for data_list in Data_lists]
    Mat_list=[[data_list[i:i+row_size] for i in range(0, len(data_list), row_size)] for data_list in Data_lists]
    Mat_list=[nested_list_to_mat(Mat) for Mat in Mat_list]
    return Mat_list
row_size=4
Mat_list=str_lists_to_mat(check_list,row_size)
"""
1. here Mat is changed. So it should be W_{init_subscript} 
2. let k=init_subscript
3. Here O(n[i]*2n[logical_or+"="])=O(n^2) (Here [...] is the comment)
"""
def Warshall_mat(Mat:np.ndarray,init_subscript:int,path_list:dict[tuple[int,int],list[int]]={}):
    first_pair=Mat[:,init_subscript]
    Check_path=path_list!={}
    if Check_path:
        second_pair=Mat[init_subscript,:]
        # https://stackoverflow.com/a/4915964/21294350 List comprehensions became the preferred style
        valid_second_pair=[col_index for col_index,i in enumerate(second_pair) if i==1]
        for row_index,i in enumerate(first_pair):
            if i==1:
                for col_index in valid_second_pair:
                    if Mat[row_index,col_index]==0:
                        Mat[row_index,col_index]=1
                        path_list[(row_index,col_index)]=path_list[(row_index,init_subscript)]+path_list[(init_subscript,col_index)][1:]
    else:
        for row_index,i in enumerate(first_pair):
            if i==1:
                """
                Here we can also "or", i.e. Mat[k,:] or Mat[row_index,:]
                https://stackoverflow.com/a/69917627/21294350
                1. reduce along axis-1, so len is 6 https://np.org/doc/stable/reference/generated/np.ufunc.reduce.html
                axis(https://stackoverflow.com/a/17079437/21294350)
                2. or https://np.org/doc/stable/reference/generated/np.logical_or.html#np.logical_or
                """
                Mat[row_index,:]=np.logical_or(Mat[row_index,:],Mat[init_subscript,:])
    return Mat
Mat=Mat_list[0]
Check_Data_str_list=["""0 0 0 1 
1 0 1 1 

1 0 0 1 

0 0 1 0""","""0 0 0 1 
1 0 1 1 

1 0 0 1 

0 0 1 0""","""0 0 0 1 
1 0 1 1 

1 0 0 1 
1 0 1 1""","""1 0 1 1 
1 0 1 1 

1 0 1 1 

1 0 1 1"""]
Check_Mat_list=str_lists_to_mat(Check_Data_str_list,row_size)
"""
here O(n[i]*n^2)=O(n^3) (more specifically 2n^3)
Book has 3*n^3 (here assignment is thought as bit operation 
although it is probably done by block based on the assembly code)
"""
def final_Warshall_mat(Mat,row_size)->np.ndarray:
    for i in range(row_size):
        Warshall_mat(Mat,i)
    return Mat
for i in range(row_size):
    if np.array_equal(Warshall_mat(Mat,i),Check_Mat_list[i])==False:
        print("calc err")
##########################################################################################
# 9.4 exercise 16 
##########################################################################################
"""
here assume matrix is of the following form:
  a b c d e
a
b
c
d
e
"""
Mat = np.array([[1,1,0,1,0], 
                [0,0,1,0,1],
                [0,1,1,0,1],
                [0,0,0,0,1],
                [1,0,0,1,1]])
row_size=5

path_list={}
# https://stackoverflow.com/a/49360371/21294350
"""
Here I skip loops
and don't get all possible paths
https://stackoverflow.com/a/9535898/21294350
"""
for ix, iy in np.ndindex(Mat.shape):
    if Mat[ix,iy]==1:
        path_list[(ix,iy)]=[ix,iy]

#########################################################################
# 9.4 exercise 18
#########################################################################
check_node_pair_str="""a, b b) b, a c) b, b
d) a, e e) b, d f ) c, d
g) d, d h) e, a i) e, c
"""
check_node_pair_list=re.split('\w[ ]*\)',check_node_pair_str)
check_node_pair_list=[tuple(re.findall('\w',Str)) for Str in check_node_pair_list]
# https://stackoverflow.com/a/16060908/21294350
import string
alphabet=list(string.ascii_lowercase)
node_index_map={}
for i in range(5):
    node_index_map[alphabet[i]]=i
check_node_pair_list=[tuple(map(lambda letter:node_index_map[letter],Str_pair)) for Str_pair in check_node_pair_list]

"""
this can get the book ans except for b),g) where it contains single-node cases and h) loop cases
"""
for i in range(row_size):
    if np.array_equal(Warshall_mat(Mat,i,path_list),np.ones((row_size, row_size))):
        print(f"strongly connected for W_{i+1}")
        for pair in check_node_pair_list:
            index_1=pair[0]
            index_2=pair[1]
            path_str=','.join([alphabet[idx] for idx in path_list[pair]])
            print(f"{alphabet[index_1]}-{alphabet[index_2]} by {path_str}")
##########################################################################################
# algorithm 1 similar to 9.3-exercise-8 code
# 9.4-exercise-26 a)
##########################################################################################
print("\n9.4-exercise-26")
"""
here mat_1,2 don't change
"""
def Boolean_product(mat_1:np.ndarray,mat_2:np.ndarray):
    # https://www.math.drexel.edu/~dmitryk/Teaching/MATH221-SPRING'12/Quiz6_solutions.pdf
    ret_mat=np.empty([mat_1.shape[0], mat_2.shape[1]])
    for ridx,row in enumerate(mat_1):
        for cidx,col in enumerate(mat_2.T):
            # https://stackoverflow.com/a/36824894/21294350
            ret_mat[ridx,cidx]=np.logical_and(row,col).any()*1
    return ret_mat
row_size=5
Mat=np.zeros([row_size,row_size])
target_pairs="(a, c), (b, d), (c, a), (d, b), (e, d)"
orig_pair_list=re.split('\),',target_pairs)
orig_pair_list=[tuple(re.findall('\w',Str)) for Str in orig_pair_list]
orig_pair_list=[tuple(map(lambda letter:node_index_map[letter],Str_pair)) for Str_pair in orig_pair_list]
for pair in orig_pair_list:
    Mat[pair[0],pair[1]]=1
def Transitive_Closure(Mat:np.ndarray):
    ret_mat=Mat
    result_mat=Mat
    for i in range(1,row_size):
        ret_mat=Boolean_product(ret_mat,Mat)
        result_mat=np.logical_or(result_mat,ret_mat)
    return result_mat
check_list=["""1 0 1 0 0
0 1 0 1 0
1 0 1 0 0
0 1 0 1 0
0 1 0 1 0"""]
check_list=str_lists_to_mat(check_list,5)
print(np.array_equal(Transitive_Closure(Mat)*np.ones([row_size,row_size]),check_list[0]))
##########################################################################################
# 9.4-exercise-26 b~d) (Here to be also used in 28, I use a~d))
##########################################################################################
Mat_list=["""0 0 1 0 0
0 0 0 1 0
1 0 0 0 0
0 1 0 0 0
0 0 0 1 0""","""0 0 0 0 0
0 0 1 0 1
0 0 0 0 1
1 0 0 0 0
0 1 1 0 0""","""0 1 1 0 1
1 0 1 0 0
1 1 0 0 0
1 0 0 0 0
0 0 0 1 0""","""0 0 0 0 1
1 0 0 1 0
0 0 0 1 0
1 0 1 0 0
1 1 1 0 1"""]
Mat_list=str_lists_to_mat(Mat_list,5)
check_B_list=["""1 0 1 0 0
0 1 0 1 0
1 0 1 0 0
0 1 0 1 0
0 1 0 1 0""","""0 0 0 0 0
0 1 1 0 1
0 1 1 0 1
1 0 0 0 0
0 1 1 0 1""","""1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1""","""1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1"""]
check_B_list=str_lists_to_mat(check_B_list,5)
for idx,mat in enumerate(Mat_list):
    print(np.array_equal(Transitive_Closure(mat)*np.ones([row_size,row_size]),check_B_list[idx]))
##########################################################################################
# 9.4-exercise-28
##########################################################################################
print("\n9.4-exercise-28")
for idx,mat in enumerate(Mat_list):
    print(np.array_equal(final_Warshall_mat(mat,row_size),check_B_list[idx]))