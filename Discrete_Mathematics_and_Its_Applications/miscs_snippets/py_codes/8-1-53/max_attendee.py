list_len=7
#########################################################################
# Data from exercise 54
#########################################################################
talk_attendee_list=[[20, 10, 50, 30, 15, 25, 40],[100, 5, 10, 20, 25, 40, 30],[2, 3, 8, 5, 4, 7, 10],[10, 8, 7, 25, 20, 30, 5]]
start_time_list=[8,9,10.5,9.5,8.5,11,13]
end_time_list=[10,11,12,13,14,14,14]
"""
here only T has T[0] for no talk, others like p[] use p[0] related with talk 1. (Ignore this)
"""
# def index_of_T_from_other_list(orig_index):
#     return orig_index+1
for k in range(len(talk_attendee_list)):
    p=[0]*list_len
    T=[0]*(list_len+1)
    S=[[0]]*(list_len+1)
    # j:0 ~ n-1
    for j in range(list_len):
        find=False
        for i in range(j-1,-1,-1):
            if end_time_list[i]<=start_time_list[j]:
                p[j]=i+1
                find=True
                # after finding the max, must break to avoid overwriting p[j].
                break
        if find==False: 
            p[j]=0
    T[0]=0
    # print(f"\np:{p}")
    """
    1. here j:1 ~ n only as the index of p and talk_attendee_list.
    2. zip https://stackoverflow.com/a/18648679/21294350
    """
    # print(f"{talk_attendee_list[k]}")
    for T_j,j in zip(range(1,list_len+1),range(list_len)):
        """
        1. here keep S[0] as 0 to ensure when p[j]=0, it appends the right S[].
        2. Then T_j and p[j] are consistent.
        3. change >= to > to get different answers maybe.
        """
        if talk_attendee_list[k][j]+T[p[j]]>=T[T_j-1]:
            T[T_j]=talk_attendee_list[k][j]+T[p[j]]
            S[T_j]=S[p[j]]+[T_j]
            # print(f"S:{S}\nT:{T}")
            # print(f"{talk_attendee_list[k][j]}+{T[p[j]]}>{T[T_j-1]}")
            # print(f"{j}th in talk_attendee_list {k}: {S[T_j]} after appending {S[p[j]]} with {T_j}")
        else:
            T[T_j]=T[T_j-1]
            S[T_j]=S[T_j-1]
    print(f"{k}th talk_attendee_list: {S[list_len]}")