Recently, when I self-learnt Discrete Mathematics and Its Applications 8th by Kenneth Rosen, I did only the even-numbered exercises which the author offers the detailed description instead of the odd ones because the odd ones and the corresponding even ones are very similar. 

I has some questions about exercise 13-4-30. The problem is
> Let $L_n$ be the set of strings with at least n bits in which the
nth symbol from the end is a 0. Use Exercise 29 to show
that a deterministic finite-state machine recognizing $L_n$ must have at least $2^n$ states.

and exercise 29 is 
> Suppose that $L$ is a subset of $I^∗$ and for some positive integer n there are n strings in $I^∗$ such that every two of these
strings are distinguishable with respect to $L$. Prove that 
every deterministic finite-state automaton recognizing $L$
has at least n states.

The answer of exercise 30 says:
> We claim that all $2^n$ bit strings of length n are distinguishable with respect to $L$. If x and y are two bit
strings of length n that differ in bit $i$, where $1\le i\le n$, then they are distinguished by any string z of length
i − 1, because one of xz and yz has a 0 in the nth position from the end and the other has a 1. Therefore
by Exercise 29, any deterministic finite-state automaton recognizing $L_n$ must have at least $2^n$ states.

Here I interpret "end" in exercise 30 as the right end same as [this QA](https://cs.stackexchange.com/a/14009/161388).

Here if $x,y$ differ in bit 1, e.g. $x=0\overbrace{0\cdots 0}^{n-1\text{ times}},y=1\overbrace{0\cdots 0}^{n-1\text{ times}}$, then $z=\lambda$ (Here I use $\lambda$ to interpret the empty string). But $yz\notin L_n$ because the nth bit from the end is *1 instead of 0*.

Q:

If the above answer offered by the book is wrong, then how to use the theorem proved in exercise 29 to prove 30 (i.e. how to find $2^n$ strings where *each pair* of these strings is distinguishable)? Any hint is also welcome.