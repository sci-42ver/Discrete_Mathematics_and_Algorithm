def reflexive(L:list,Total_set):
    find=0
    for relation in L:
        if relation[0]==relation[1]:
            find+=1
    if find==len(Total_set):
        return True
    return False
def irreflexive(L:list):
    find=0
    for relation in L:
        if relation[0]==relation[1]:
            find+=1
    if find!=0:
        return False
    return True
def symmetric(L:list):
    whether_symmetric=True
    for relation in L:
        if (relation[1],relation[0]) not in L:
            whether_symmetric=False
    return whether_symmetric
def antisymmetric(L:list):
    check=True
    for relation in L:
        if (relation[1],relation[0]) in L:
            if relation[1] != relation[0]:
                check=False
    return check
def asymmetric(L:list):
    check=True
    for relation in L:
        if (relation[1],relation[0]) in L:
            check=False
    return check
def transitive(L:list):
    check=True
    for relation in L:
        second_list=[second_relation for second_relation in L if second_relation[0]==relation[1]]
        for second_relation in second_list:
            if (relation[0],second_relation[1]) not in L:
                check=False
    return check

import itertools
# https://stackoverflow.com/a/2283243/21294350
funcdict = {0:reflexive,1:irreflexive,2:symmetric,3:antisymmetric,4:asymmetric,5:transitive}
check_map=['reflexive','irreflexive','symmetric','antisymmetric','asymmetric','transitive']
def check_relations(pair_list,num_set:list[int],Check_lists):
    index=1
    for L in range(len(pair_list) + 1):
        for subset in itertools.combinations(pair_list, L):
            subset_list=list(subset)
            print(subset_list)
            for check_index in range(6):
                if check_index==0:
                    # we can also keep consistent by use pointer https://stackoverflow.com/a/61505576/21294350
                    # or use inspect https://stackoverflow.com/a/41188411/21294350
                    if funcdict[check_index](subset_list,num_set):
                        Check_lists[check_index].append(index)
                else:
                    if funcdict[check_index](subset_list):
                        Check_lists[check_index].append(index)
            index+=1
Total_set = list(range(1+1))
# https://stackoverflow.com/a/5898031/21294350 Also official https://stackoverflow.com/a/1482316/21294350
stuff=[(i,j) for i in Total_set for j in Total_set]
# https://stackoverflow.com/a/12791510/21294350
Check_lists=[[] for i in range(6)]
check_relations(stuff,Total_set,Check_lists)
for tmp_index,check_str in enumerate(check_map):
    print(f"{check_str} {Check_lists[tmp_index]}")

Ans=[[8, 13, 14, 16],[1, 3, 4, 9],[1, 2, 5, 8, 9, 12, 15, 16],\
[1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 13, 14],[1, 3, 4],[1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 13, 14, 16]]
if Check_lists!=Ans:
    print("calculation err")

n=3
Total_set = list(range(n))
stuff=[(i,j) for i in Total_set for j in Total_set]
Check_lists=[[] for i in range(6)]
check_relations(stuff,Total_set,Check_lists)
for tmp_index,check_str in enumerate(check_map):
    print(f"{check_str} {Check_lists[tmp_index]}")
    if check_str=='transitive':
        print(f"{check_str} Len:{len(Check_lists[tmp_index])}")