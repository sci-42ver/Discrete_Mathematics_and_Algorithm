import math
def prime(n): return not any(n % i == 0 for i in range(2,int(math.sqrt(n))+1))
e_str='2.718281828459045235360287471352662497757247093699959574966967627724076630353547594571382178525166427427466391'
e_str=e_str.replace('.', '')
for i in range(len(e_str)-9):
  if prime(int(e_str[i:i+10])):
    print(f"find {e_str[i:i+10]}")
    break