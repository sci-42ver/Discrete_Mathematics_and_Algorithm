n=9
orig_order_sequence=range(1,n+1)
new_list=[]
# https://stackoverflow.com/a/986145/21294350 here default pass by reference, so `derangement_lists` will be changed.
def generate_new_derangement(maps:list[tuple],recursive_lists:list[list],orig_seq,derangement_lists):
    # print("before",recursive_lists)
    for tmp_list in recursive_lists:
        if type(tmp_list) is not list:
            print("err")
        # print("before insert",tmp_list)
        for Map in maps:
            tmp_list.insert(Map[0],orig_seq[Map[1]])
            # print("after insert",tmp_list)
        derangement_lists.append(tmp_list)
        # print(maps,"-",recursive_lists,"-",orig_seq,"-",derangement_lists)
def derangement(seq:list,size)->list[list]:
    derangement_lists=[] # not having one redundant [] due to [[]]
    # keep the type is list[list]
    if size==2:
        return [[seq[1],seq[0]]]
    elif size==3:
        return [[seq[2],seq[0],seq[1]],[seq[1],seq[2],seq[0]]]
    """
    1. since !1=0, we don't use it for derangements. https://en.wikipedia.org/wiki/Derangement#Counting_derangements
    """
    # elif size==1:
    #     # notice here not use [[seq]] to keep list[list]
    #     return [[seq[0]]]
    new_list=seq
    # choose for the 1st person
    for Index in range(1,len(seq)):
        # D_{n-1}
        recursive_list=new_list[1:Index]+new_list[Index+1:]
        recursive_list.insert(0,new_list[Index]) # not make the wrong order "(new_list[Index],0)"
        recursive_lists=derangement(recursive_list,len(recursive_list))
        maps=[(Index,0)] # new_list[Index]=seq[0] and new_list[0]=seq[Index]
        generate_new_derangement(maps,recursive_lists,seq,derangement_lists)
        # D_{n-2}
        recursive_list=new_list[1:Index]+new_list[Index+1:]
        recursive_lists=derangement(recursive_list,len(recursive_list))
        """
        Notice here must insert at the 1st location, to keep the insertion sequence correct.
        """
        maps=[(0,Index),(Index,0)] # new_list[Index]=seq[0] and new_list[0]=seq[Index]
        # for tmp_list in recursive_lists:
        #     for Map in maps:
        #         tmp_list.insert(Map[0],seq[Map[1]])
        #     derangement_lists.append(tmp_list)
        generate_new_derangement(maps,recursive_lists,seq,derangement_lists)
    return derangement_lists
derangement_lists=derangement(list(orig_order_sequence),len(orig_order_sequence))
for List in derangement_lists:
    if len(List)!=len(orig_order_sequence):
        print("err")
print(f"!{n}:{len(derangement_lists):,}")