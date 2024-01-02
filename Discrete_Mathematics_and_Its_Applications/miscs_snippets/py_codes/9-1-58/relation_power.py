def composite(relation_1,relation_2):
    L=[]
    for pair_1 in relation_1:
        for pair_2 in relation_2:
            if pair_1[1]==pair_2[0]:
                L.append((pair_1[0],pair_2[1]))
    return L
def power(base_relation,pow):
    if pow==1:
        return base_relation
    return composite(power(base_relation,pow-1),base_relation)
target_relation=[(1, 1), (1, 2), (1, 3), (2, 3), (2, 4), (3, 1),
(3, 4), (3, 5), (4, 2), (4, 5), (5, 1), (5, 2), (5, 4)]
Total_set = list(range(1,5+1))
# https://stackoverflow.com/a/5898031/21294350 Also official https://stackoverflow.com/a/1482316/21294350
Max_relation=[(i,j) for i in Total_set for j in Total_set]
for i in range(2,5+1):
    pow_rel=power(target_relation,i)
    if len(pow_rel)<len(Max_relation)/2:
        print(i,pow_rel)
    else:
        complementary_rel=[pair for pair in Max_relation if pair not in pow_rel]
        print(i,"without",complementary_rel)