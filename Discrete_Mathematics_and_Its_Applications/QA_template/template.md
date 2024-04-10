I have asked one similar question QA_1 "The formal proof that one Turing Machine recognizes one specific *language*" and [the answer][1] fills the part "It does not generate any string that is *not* in $L$." of [this QA_2 answer][2].

---

For one *general* function, the Halting Problem tells us it is [impossible][3] to "prove that the machine actually computes the function", so we need one specific function to investigate. 

Recently when I self-learnt Discrete Mathematics and Its Applications 8th by Kenneth Rosen, I did the even-numbered exercises which the author offers the detailed description and the asterisk odd-numbered exercises which are more difficult than those exercises without the asterisk. Since the odd-numbered ones are very similar to the corresponding even-numbered ones and the book doesn't give the detailed answer for odd-numbered exercise, I skip all odd-numbered exercises without the asterisk. The exercise 13-5-25 in the book:
> Construct a Turing machine that computes the function $f(n_1,n_2)=\min(n_1,n_2)$ for all nonnegative integers $n_1$ and $n_2$

Since this is one *asterisk odd-numbered* exercise, the book answer is simple without detailed explanation, so I searched for the internet and found [one askfilo link][4] which has the same answer as the book although the askfilo link has some small typo errors.

The book answer uses "definition 2" in the wikipedia ["Turing machine" entry][5] for the transition function ("Turing instruction" in the wikipedia context). I use the same symbol convention as the book for the following.
> $(s_0, 0, s_0, 0, R), (s_0, ∗, s_5, B, R), (s_3, ∗, s_3, ∗, L),
(s_3, 0, s_3, 0, L), (s_3, 1, s_3, 1, L), (s_3, B, s_0, B, R), (s_5, 1, s_5, B, R),
(s_5, 0, s_5, B, R), (s_5, B, s_6, B, L), (s_6, B, s_6, B, L), (s_6, 0, s_7, 1, L),
(s_7, 0, s_7, 1, L), (s_0, 1, s_1, 0, R), (s_1, 1, s_1, 1, R), (s_1, ∗, s_2, ∗, R),
(s_2, 0, s_2, 0, R), (s_2, 1, s_3, 0, L), (s_2, B, s_4, B, L), (s_4, 0, s_4, 1, L),
(s_4, ∗, s_8, B, L), (s_8, 0, s_8, B, L), (s_8, 1, s_8, B, L)$

---

I also found [one geeksforgeeks link][6] computing $f(n_1,n_2)=\max(n_1,n_2)$ although it has some errors for me.

The geeksforgeeks and askfilo links share the same basic idea that we match *pairs* of numbers for the $n_{1,2}$ part and *change back the matching markers to the number markers* (in the geeksforgeeks link, matching marker is $X$ and the number marker is $0$) when finding the relation between $n_{1,2}$ (the askfilo link adds the step of only keeping the blank symbol $B$ and the number marker while the geeksforgeeks link leaves some matching markers unchanged). But the geeksforgeeks link has one TM figure to help understanding and it has no typo errors. So I take the geeksforgeeks link as the example here.

TM(Turing machine):
[![7]][7]

My understanding of the states used by the geeksforgeeks link:
- $q_0$: the starting state of the process $K$ to change the pair of 0s
- $q_1$: change the left part of the pair
- $q_7$: the left side is all changed to Xs
- $q_2$: the process $K$ goes into the right side
- $q_3$: the right side is all changed to Xs
- $q_5$: change the right part of the pair
- $q_6$: the process $K$ goes back into the left side
- $q_{4,9}$: final
- $q_8$: meet the right end when changing the right side Xs back to 0s.

My correction of possible errors in the geeksforgeeks link (I use the similar symbol notation as the QA_1 answer in the following):
1. > But on receiving X replace it with 0 and move rightwards and change state back to q0.

      we should *not replace X with 0* for q6 because q7 will "change every X with 0 while moving rightwards" for *the right side*.
      If we also change *the left side* which is done by q6, then we will get $n_1+n_2$ 0s.
      so we have $(q_6,X,q_0,X,R)$.
      
      - If we use the same machine as the original geeksforgeeks link, when $n_2\ge n_1$,
        we have 
        $$
        q_0 0^{n_1}C 0^{n_2}\mapsto X q_1 0^{n_1-1}C 0^{n_2}\mapsto^* X 0^{n_1-1}q_1 C 0^{n_2}\mapsto X 0^{n_1-1} C q_2 0^{n_2} \mapsto X 0^{n_1-1} q_5 C X 0^{n_2-1} \mapsto X 0^{n_1-2} q_6 0 C X 0^{n_2-1} \mapsto^* q_6 X 0^{n_1-1} C X 0^{n_2-1} \mapsto 0 q_0 0^{n_1-1} C X 0^{n_2-1} 
        $$
        This means we have $q_0 0^{n_1}C 0^{n_2} \mapsto^* 0 q_0 0^{n_1-1} C X 0^{n_2-1},n_{1,2}\in \mathbb{N}^+$
        Then 
        $$
        n_2\ge n_1\Rightarrow q_0 0^{n_1}C 0^{n_2} \mapsto^* 0^{n_1} q_0 C X^{n_1} 0^{n_2-n_1}\mapsto 0^{n_1} C q_7 X^{n_1} 0^{n_2-n_1} \mapsto^* 0^{n_1} C 0^{n_2} q_7 B\mapsto 0^{n_1} q_8 C 0^{n_2} \mapsto 0^{n_1} C q_9 0^{n_2}
        $$
      - If we use $(q_6,X,q_0,X,R)$, then based on the above process, we have
        $$
        q_0 0^{n_1}C 0^{n_2} \mapsto^* X^{n_1} q_0 C X^{n_1} 0^{n_2-n_1} \mapsto^* X^{n_1} C q_9 0^{n_2}
        $$
2. Similarly
     > From state q3, keep moving left on receiving 0 or C and on receiving X, replace X with 0 and move leftwards.

     It also needs to be changed because this will change all X to 0s which also gets $n_1+n_2$ 0s.

     - To remove $C$ as the askfilo link does and remove the above error,
       we can use $(q_3,C,q_{10},X,L),(q_3,X,q_3,X,L)$ for 
       $q_3$
       and $(q_{10},0,q_{10},0,L),(q_{10},X,q_{10},0,L),(q_{10},B,q_{4},B,R)$. It changes all 
       Xs in the $n_1$ original 0s back to 0s.

       Then we have 
       $$
       n_2< n_1\Rightarrow q_0 0^{n_1}C 0^{n_2} \mapsto^* X^{n_2} q_0 0^{n_1-n_2} C X^{n_2} \mapsto^* X^{n_2+1} 0^{n_1-n_2-1} q_1 C X^{n_2} \mapsto^* X^{n_2+1} 0^{n_1-n_2-1} C X^{n_2} q_2 B \mapsto^* X^{n_2+1} 0^{n_1-n_2-1} q_3 C X^{n_2} \mapsto X^{n_2+1} 0^{n_1-n_2-1} q_{10} X^{n_2+1} \mapsto^* q_{10} B 0^{n_1} X^{n_2+1} \mapsto q_4 0^{n_1} X^{n_2+1}
       $$
       - Similarly we should have $(q_0,C,q_7,X,R)$ to remove 
         $C$,
         remove $q_9,(q_8,0,q_8,0,L),(q_8,C,q_9,C,R)$ 
         and let $q_8$ be accepted since we have already changed all necessary Xs to 0s when $q_8$ for 
         $q_{7\sim 9}$.

         Then we have 
         $$
         n_2\ge n_1\Rightarrow q_0 0^{n_1}C 0^{n_2} \mapsto^* X^{n_1} q_0 C X^{n_1} 0^{n_2-n_1}\mapsto X^{n_1+1} q_7 X^{n_1} 0^{n_2-n_1} \mapsto^* X^{n_1+1} 0^{n_2} q_7 B\mapsto X^{n_1+1} 0^{n_2-1} q_8 0\\ (\text{ if }n_2=0=n_1,\text{ then we end up }q_8 X B\ )
         $$


In summary my correction is:
$$
(q_6,X,q_0,0,R)\to (q_6,X,q_0,X,R);\\
(q_3,X/0,q_3,0,L),(q_3,C,q_3,C,L),(q_3,B,q_3,B,R) \to (q_3,C,q_{10},X,L),(q_3,X,q_3,X,L)\quad\text{Here }/\text{ means or};\\
\text{Add }(q_{10},0,q_{10},0,L),(q_{10},X,q_{10},0,L),(q_{10},B,q_{4},B,R);\\
(q_0,C,q_7,C,R) \to (q_0,C,q_7,X,R);\\
\text{Remove }q_9,(q_8,0,q_8,0,L),(q_8,C,q_9,C,R).\\
$$

and 
- $q_{10}$: begin changing back Xs in the left side to 0s when $n_2< n_1$
- $q_{8}$ substitutes $q_9$ and become the final state after converting the necessary Xs.

Q:

Is my correction for the geeksforgeeks link right? 
Can we prove that the TM computes the function $f(n_1,n_2)=\max(n_1,n_2)$ by considering the 2 cases $n_1> n_2$ and $n_1\le n_2$ as the above "Similarly ... To remove $C$ ..." does similar to the QA_1 answer (IMHO, this is fine)?


  [1]: https://cs.stackexchange.com/a/166984/161388
  [2]: https://cs.stackexchange.com/a/110858/161388
  [3]: https://math.stackexchange.com/questions/1643850/is-there-a-way-to-prove-that-a-turing-machine-computes-the-function-we-designed#comment3352654_1643850
  [4]: https://askfilo.com/user-question-answers-algebra-2/construct-a-turing-machine-that-computes-the-function-for-35383437353333
  [5]: https://en.wikipedia.org/wiki/Turing_machine#Alternative_definitions
  [6]: https://www.geeksforgeeks.org/turing-machine-to-accept-maximum-of-two-numbers/
  [7]: https://i.stack.imgur.com/IjaE8.png