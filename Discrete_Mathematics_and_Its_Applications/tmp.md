Okay. Let us think about it step by step. 

Step 1: What do we want? We want that EXACTLY $k$ specific people should have matches. The rest, i.e the remaining $N-k$ people should NOT have matches. So let $A$ = the event that **at least** $k$ specific people have matches (**Notice**: 1. here is not "**exactly** $k$" because otherwise $A=B\Rightarrow P(B\vert A)P(A)=1\cdot P(A)$ although the [original answer in the history_1][1] mistakenly use the wrong description and his internal idea is right where $P_k= \frac{1\times 1\times 1.......\times1}{N\times N-1 \times N-2.....\times N-k}$ implies "**at least** $k$ people" instead of "exactly". BTW, $P_{k} = \frac{1\times 1\times 1.......\times1}{N\times N-1 \times N-2.....1}$ seems to be wrong there. 2. In history_1, since at the end we will divide by $N!$ where it assumes the people order is **fixed**, i.e. the $i$th has $N-i+1$ choices. So $P_{k}^{n},n=N$ (Here we use the ["k-permutations of n"](https://en.wikipedia.org/wiki/Permutation#k-permutations_of_n) notation) in the edit of history_1 is wrong because it **re-chooses the order** the $k$ people chosen. It should be $\binom{N}{k}$ and then the order is decided by that the $m$th of the $k$ people is $i_{m}$th person in the $N$ people where $1\le i_{m}\le N$. It is same as [QA_1][2].) and $B$ = the event that exactly $N-k$ people have no matches. Based on this assumption, we want to know $P(A\bigcap B)$.

Now, notice that from the Bayes formula, we can calculate this probability by either $P(A|B)P(B)$ or $P(B|A)P(A)$. Note also that the first is much harder to calculate because $B$ will have more influences to $A$ than $A$ to $B$ (if $B$, then $A$ becomes exactly $k$ people while if $A$, $B$ is same as the original). Here we calculate the probability that $N-k$ don't have matches given that $k$ people have matches.

So let's do that! The probability that $P(B|A)P(A)$. Note that we know $P(B|A)$ like you mentioned from doing the earlier problem, because this is just the probability that $N-k$ people don't have a match which should just be $P(B|A)=\sum_{m=k}^{N}P(B\vert A_m)=P_{N-k}+\overbrace{0+\cdots +0}^{N-k \text{ times}} = \sum_{i=0}^{N-k}(-1)^{i}/i!$ (Here we use the [law of total probability][3] and $A_m$ is the event that exactly $m$ people have matches. Notice for **cases** where $k+1\sim N$ people have matches the probability is $0$). 

And all you need to calculate is the probability of **at least** $k$ specific people getting a match. Based on QA_1, if $C$ = the event that **at least** $k$ people have matches, then $P(C)= \frac{1}{k!}$. Then since
> Let us fix our attention on a **particular** set of $k$ people

we need to divide by $\binom{N}{k}$, so we got $P(A)=\frac{P(C)}{\binom{N}{k}}=\frac{1}{P_{k}^N}$

Then the result is $\frac{P_{N-k}}{P_{k}^N}$ which is elegant. Hope this helps!

---

This problem is duplicate of [answer_1][4] (then the result is $\frac{\binom{n}{k} D_{n - k}}{N!}=\frac{\frac{N!}{k!(N-k)!}P_{N-k}\cdot (N-k)!}{N!}=\frac{P_{N-k}}{k!}$ where [$D_{n - k}$][5] is the number of derangements) and [answer_2][6] which is based on the inclusion-exclusion for $N-k$ people where both care about "at least $k$ people" instead of "at least $k$ specific people".

One specific case when $n=1$ can be found in [answer_3](https://math.stackexchange.com/a/2449708/1059606) which is similar to answer_1.


  [1]: https://math.stackexchange.com/review/suggested-edits/2058828
  [2]: https://math.stackexchange.com/a/3787162/1059606
  [3]: https://en.wikipedia.org/wiki/Law_of_total_probability
  [4]: https://math.stackexchange.com/a/3785289/1059606
  [5]: https://proofwiki.org/wiki/Closed_Form_for_Number_of_Derangements_on_Finite_Set
  [6]: https://math.stackexchange.com/a/3786457/1059606