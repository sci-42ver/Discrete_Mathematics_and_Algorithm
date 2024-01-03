"""
I wrote this code before reading the Lemma 2
In Lemma 2
1. w_{ij}^{[k-1]} is here `Mat` only changing necessary with the rest unchanged.
2. w_{ik}^{[k-1]} \wegde w_{kj}^{[k-1]} corresponds to `Mat[:,init_subscript]` and `Mat[init_subscript,:]`
"""
import re
import numpy as np
Data_str_list=["""0 0 0 1 
1 0 1 0 
1 0 0 1 
0 0 1 0"""]
def nested_list_to_mat(nested_list:list[list]):
    return np.array([np.array(xi) for xi in nested_list])
def str_lists_to_mat(Str_list,row_size):
    Data_lists=[re.split(' [\\n]*',Str) for Str in Str_list]
    Data_lists=[[int(elem) for elem in data_list] for data_list in Data_lists]
    Mat_list=[[data_list[i:i+row_size] for i in range(0, len(data_list), row_size)] for data_list in Data_lists]
    Mat_list=[nested_list_to_mat(Mat) for Mat in Mat_list]
    return Mat_list
row_size=4
Mat_list=str_lists_to_mat(Data_str_list,row_size)
"""
1. here Mat is changed. So it should be W_{init_subscript} 
2. let k=init_subscript
3. Here O(n[i]*2n[logical_or+"="])=O(n^2) (Here [...] is the comment)
"""
def Warshall_mat(Mat,init_subscript:int):
    first_pair=Mat[:,init_subscript]
    # second_pair=Mat[init_subscript,:]
    # valid_second_pair=[col_index for col_index,i in enumerate(second_pair) if i==1]
    for row_index,i in enumerate(first_pair):
        if i==1:
            # for col_index in valid_second_pair:
            #     if Mat[row_index,col_index]==0:
            #        Mat[row_index,col_index]=1
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
for i in range(row_size):
    if np.array_equal(Warshall_mat(Mat,i),Check_Mat_list[i])==False:
        print("calc err")