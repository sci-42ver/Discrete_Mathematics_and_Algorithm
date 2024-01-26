import itertools
import copy
def K_m_n(m,n):
  num_list=list(range(1,1+m+n))
  minimum=m+n
  first_subset=[]
  second_subset=[]
  for subset in itertools.combinations(num_list, m):
    the_other_subset=[num for num in num_list if num not in subset]
    diff=[abs(num_1-num_2) for num_1 in subset for num_2 in the_other_subset]
    if minimum>max(diff):
      minimum=max(diff)
      first_subset=copy.deepcopy(list(subset))
      second_subset=copy.deepcopy(the_other_subset)
  return minimum,first_subset,second_subset
# Also see https://scholarworks.wmich.edu/cgi/viewcontent.cgi?article=2664&context=dissertations
print(K_m_n(2,3))
print(K_m_n(3,3))

import math
# https://sci-hub.se/https://doi.org/10.1016/S0021-9800(66)80059-5
Q_n=lambda n:sum([math.comb(i,i//2) for i in range(n)])
print(Q_n(3))

def C_n(n):
  num_list=list(range(1,1+n))
  minimum=n
  perm=[]
  for subset in itertools.permutations(num_list, n):
    diff=[abs(subset[i]-subset[i+1]) if i!=n-1 else abs(subset[i]-subset[0]) for i in range(n)]
    if minimum>max(diff):
      minimum=max(diff)
      perm=copy.deepcopy(list(subset))
  return minimum,perm
print(C_n(5))