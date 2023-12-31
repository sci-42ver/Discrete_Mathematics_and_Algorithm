# method 1 https://math.stackexchange.com/a/913318/1059606
import math
Sum=0
n=10
not_match_num=5
max_match_num=n-not_match_num
for i in range(n,not_match_num-1,-1):
    Sum+=(-1)**i*math.factorial(i)*math.comb(not_match_num,n-i)
print(Sum)
# Check by computer https://qr.ae/pKSPb3
from itertools import * 
 
l=[x for x in permutations([0,1,2,3,4,5,6,7,8,9]) if (x[0]!=0 and x[2]!=2 and x[4]!=4 and x[6]!=6 and x[8]!=8)] 

print(len(l))
# by formula which is what I thought firstly based on link_1 https://math.stackexchange.com/a/3850293/1059606
subfactorial=lambda n: n<1 or (-1)**n+n*subfactorial(n-1)
# this is the P_{N-k} in link_1
derangement_probability=lambda n:subfactorial(n)/math.factorial(n)
# def falling_factorial(n,k): 
#     if k==1:
#         return n 
#     elif k>1:
#         return n*falling_factorial(n-1,k-1)
"""
since we caring about one specific k people, so we need to divide by C_{k}^{n} with math.comb(total_num,match_num)
after multiplying N! with math.factorial(n).
"""
def derangement_when_specific_people_match(total_num,match_num):
    # return math.factorial(total_num)*derangement_probability(total_num-match_num)/(math.factorial(match_num)*math.comb(total_num,match_num))
    return math.factorial(total_num)*derangement_probability(total_num-match_num)/math.perm(total_num,match_num)
Sum=0
# here assume i is the non-matching number in max_match_num
for i in range(max_match_num+1):
    addend=math.comb(max_match_num,i)*derangement_when_specific_people_match(n,max_match_num-i)
    Sum+=addend
    # print(f"plus {addend} when {max_match_num-i} matches should equal to {math.comb(max_match_num,i)*subfactorial(n-(max_match_num-i))}")
print(Sum)

Sum=0
# here assume i is the matching number in max_match_num https://math.stackexchange.com/a/4836395/1059606
for i in range(max_match_num+1):
    addend=math.comb(max_match_num,i)*derangement_when_specific_people_match(n,i)
    Sum+=addend
print(Sum)
# method 2 https://math.stackexchange.com/a/912173/1059606
def constrain_pos(total_num,constrain_num):
    next_iter_num=total_num-1
    if constrain_num==0:
        return math.factorial(total_num)
    elif constrain_num==1:
        return (next_iter_num)*math.factorial(next_iter_num)
    return (constrain_num-1)*(constrain_pos(next_iter_num,constrain_num-2))+(total_num-constrain_num)*constrain_pos(next_iter_num,constrain_num-1)
print(constrain_pos(n,not_match_num))