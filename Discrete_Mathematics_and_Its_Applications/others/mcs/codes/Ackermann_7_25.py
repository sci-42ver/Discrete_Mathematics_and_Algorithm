def stack_print(level,m,n,val=None):
  if val!=None:
    print(level*'\t'+f"A({m},{n}):"+str(val))
  else:
    print(level*'\t'+f"A({m},{n}):")
track_state = True
def A(m,n,stack_level):
  if track_state :
    print('\nIn:',end='')
    stack_print(stack_level,m,n)
  val=0
  # if m==0 or n==0:
  if m==0 or n<=1:
    stack_print(stack_level,m,n,2*n)
    return 2*n
  else:
    val=A(m-1,A(m,n-1,stack_level+2),stack_level+1)
    stack_print(stack_level,m,n,val)
    return val
n=10
for i in range(n):
  for j in range(n):
    A(i,j,0)