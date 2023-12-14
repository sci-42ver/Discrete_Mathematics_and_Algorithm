# https://math.stackexchange.com/a/4349892/1059606
import math
n=6
def round_to_list_index(i):
    return n-1-i
def iteration_number_to_sequence(iteration,n)->list:
    seq_list=[0]*n
    """
    1. skip the last because it can only be 1
    2. the kth (beginning from 1) item from right can at most take k possibilities.
        then we use the base form like
        n n-1 n-2 ... 3 2 1 0 (i.e. the rightmost can be only 0)
        instead of
        b^n b^{n-1} ... b^1 b^0

        Then to let kth term be the first 1 when incrementing from 0, we need at least (k-1)! increments. 
        So we "//math.factorial(i)". Then to make it fit in the range of 0~k-1, we "%(i+1)". 
        (Here i=k-1 beginning from 1)
    """
    for i in range(1,n):
        seq_list[round_to_list_index(i)]+=(iteration//math.factorial(i))%(i+1)
    for i in range(n):
        if seq_list[round_to_list_index(i)]>i+1:
            print("error")
    # print(iteration,seq_list)
    return [i+1 for i in seq_list]
target_cnt=3
for i in range(math.factorial(n)):
    x_count=0
    origin_sequence=list(range(1,n+1))
    # print(iteration_number_to_sequence(i,n))
    tmp_seq_list=iteration_number_to_sequence(i,n)

    for j in tmp_seq_list:
        if j==1:
            x_count+=1
    if x_count!=target_cnt:
        continue
    
    for j in tmp_seq_list:
        print(j,end="")
    print()
    print("(",end="")
    for j in range(n):
        if tmp_seq_list[j]!=1:
            print(origin_sequence.pop(tmp_seq_list[j]-1),end="")
        elif j!=n-1:
            print(f"{origin_sequence.pop(tmp_seq_list[j]-1)})(",end="")
        else:
            print(f"{origin_sequence.pop(tmp_seq_list[j]-1)}",end="")
    print(")")