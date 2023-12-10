"""
here I let shot_list[9] to be the first one by A and shot_list[8] being first by B.
The reasons are shown in the following context of ""i//(2**left_rounds)" conveniently". 
"""
shot_list=[0]*10
round_combination_duplicate_list=[False]*(2**10)
possibilities=0
"""
whether to include Draw/Tied situations when counting.
"""
INCLUDE_TIE=False
"""
Here I traverse all possibilities with some skipped which may be not optimal.
Look forward for the improvement. Thanks beforehand.
"""
for i in range(0,2**10):
    """
    to skip duplicate counting like "101010xxxx", i.e. A(3,0) with B(3,0) in "Team B does not score goals"
    when "Team A wins"
    """
    if round_combination_duplicate_list[i]==True:
        continue
    A_score=0
    B_score=0
    A_round=5
    B_round=5
    for j in range(0,10):
        shot_list[j]=(i%2**(j+1))//2**(j)
        # print(i,shot_list)
    for j in range(0,10):
        if j%2==0:
            """
            here we assign from the MSB to use "i//(2**left_rounds)" conveniently 
            """
            A_score+=shot_list[9-j]
            A_round-=1
        else:
            B_score+=shot_list[9-j]
            B_round-=1
        """
        quote from the book solution:
        > the penalty kick round (or “group”) is over once one team has clinched a victory.
        i.e. one team A must win even if the other team B won the rest un-kicked round goals 
        while A lost all the rest un-kicked.
        """
        if (A_score>B_round+B_score) or (B_score>A_round+A_score):
            break
    left_rounds=A_round+B_round
    if left_rounds>0:
        """
        check the program correctness at one specific case.
        """
        if i//(2**4)==0b101010:
            print(bin(i),left_rounds,2**left_rounds,i//(2**left_rounds),i//(2**left_rounds)+2**left_rounds)
        start=i//(2**left_rounds)*(2**left_rounds)
        for tmp in range(start,start+2**left_rounds):
            round_combination_duplicate_list[tmp]=True
    if (A_score!=B_score) or INCLUDE_TIE:
        possibilities+=1
print(possibilities)