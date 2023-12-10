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
A_zero_win_B_finally_win=0

def Round_To_BitLocation(bit):
    return 9-bit
def BitLocation_To_Round(bit):
    return 9-bit
A_win=0
B_win=0
A_two_win_B_finally_win=0

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
            A_score+=shot_list[Round_To_BitLocation(j)]
            A_round-=1
        else:
            B_score+=shot_list[Round_To_BitLocation(j)]
            B_round-=1
        """
        1. quote from the book solution:
            > the penalty kick round (or “group”) is over once one team has clinched a victory.
            i.e. one team A must win even if the other team B won the rest un-kicked round goals 
            while A lost all the rest un-kicked.
        2. This implies that they can't have same ticks (scores) even after filling the left un-kicked goals of one side with ticks
            So to calculate "draw" condition, we only need to care about:
            > both teams must score the same amount of penalties at the end of the shoot-out.
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
        # """
        # check "Team B wins" with "Team A does not score goals"
        # """
        # if (i&(0b101010<<4)==0) and (A_score==0):
        #     A_zero_win_B_finally_win+=1
        #     # https://note.nkmk.me/en/python-f-strings/ https://peps.python.org/pep-0498/
        #     print(f"{i:#010b}",left_rounds,2**left_rounds,i//(2**left_rounds),i//(2**left_rounds)+2**left_rounds)
        #     for j in range(0,10):
        #         if i&(1<<Round_To_BitLocation(j))!=0:
        #             if j%2==0:
        #                 print(f"A win at {j+1} round")
        #             else:
        #                 print(f"B win at {j+1} round")
        if A_score>B_score:
            A_win+=1
        elif A_score<B_score:
            B_win+=1
            if A_score==2:
                A_two_win_B_finally_win+=1
            if A_score==0:
                A_zero_win_B_finally_win+=1
print(A_win,B_win,A_two_win_B_finally_win,A_zero_win_B_finally_win)
print(possibilities)