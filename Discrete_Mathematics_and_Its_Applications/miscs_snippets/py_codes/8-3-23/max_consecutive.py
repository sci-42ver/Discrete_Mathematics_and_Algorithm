"""
based on https://docs.python.org/3/library/stdtypes.html#tuples, we use tuple for the heterogeneous data.
return (max_list,start_index,end_index,max_sum)
"""
def max_consecutive(input_list:list,list_size)->tuple[list,int,int,int]:
    if list_size==1:
        if input_list[0]<0:
            return ([],-1,-1,0)
        else:
            return (input_list,0,0,input_list[0])
    sub_size=list_size//2
    first_max_with_index=max_consecutive(input_list[0:sub_size],sub_size)
    second_max_with_index=max_consecutive(input_list[sub_size:list_size],list_size-sub_size)
    tmp_sum=0
    forward_max=tmp_sum
    forward_index=sub_size
    for i in range(sub_size,list_size):
        tmp_sum+=input_list[i]
        if tmp_sum>forward_max:
            forward_max=tmp_sum
            forward_index=i
    tmp_sum=0
    backward_max=tmp_sum
    backward_index=sub_size-1
    for i in range(sub_size-1,-1,-1):
        tmp_sum+=input_list[i]
        if tmp_sum>backward_max:
            backward_max=tmp_sum
            backward_index=i
    middle_max=forward_max+backward_max
    total_max=0
    first_max=first_max_with_index[3]
    second_max=second_max_with_index[3]
    begin_index=0
    end_index=0
    if first_max==0 and second_max==0:
        total_max=0
        begin_index=-1
        end_index=-1
    elif first_max==0:
        total_max=second_max
        begin_index=second_max_with_index[1]+sub_size
        end_index=second_max_with_index[2]+sub_size
    elif second_max==0:
        total_max=first_max
        begin_index=first_max_with_index[1]
        end_index=first_max_with_index[2]
    elif first_max>second_max:
        total_max=first_max
        begin_index=first_max_with_index[1]
        end_index=first_max_with_index[2]
    else:
        total_max=second_max
        begin_index=second_max_with_index[1]+sub_size
        end_index=second_max_with_index[2]+sub_size
    # this will not run for [-1,-5] where total_max=middle_max=0
    if total_max<middle_max:
        total_max=middle_max
        begin_index=backward_index
        end_index=forward_index
    if total_max!=0 and sum([elem for elem in input_list[begin_index:end_index+1]])!=total_max:
        print("err",input_list[begin_index:end_index+1],total_max,input_list)
    if total_max!=0:
        return [input_list[begin_index:end_index+1],begin_index,end_index,total_max]
    else:
        return [[],begin_index,end_index,total_max]
target_lists=[[-2, 4,-1, 3, 5,-6, 1, 2],[4, 1,-3, 7,-1,-5, 3, -2],[-1, 6, 3, -4, -5, 8, -1, 7]]
for target_list in target_lists:
    print(max_consecutive(target_list,len(target_list)),"\n")