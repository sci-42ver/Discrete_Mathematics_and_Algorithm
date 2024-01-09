This one may be one duplicate of [QA_1][1], but its example $\{\{a,d\},\{b,c\}\}\wedge\{\{a\},\{b,c,d\}\}$ seems to not meet the definition in the book because $(\{a,d\} \not\subseteq \{a\}) \wedge (\{a,d\} \not\subseteq \{b,c,d\})$.

---

Recently, when I self-learnt Discrete Mathematics and Its Applications 8th by Kenneth Rosen, I did only the even-numbered exercises which the author offers the detailed description instead of the odd ones because the odd ones and the corresponding even ones are very similar. 

I has some questions about exercise 9.6-49 which is related with the [refinement][2] of the partition and the lattice. The problem is
> Show that the set of all partitions of a set S with the relation $P_1 \preccurlyeq P_2$ if the partition $P_1$ is a refinement of the
partition $P_2$ is a lattice. (See the preamble to Exercise 49
of Section 9.5.)

and the preamble to Exercise 49 of Section 9.5 is the definition of refinement:
> A partition $P_1$ is called a refinement of the partition $P_2$ if
**every** set in $P_1$ is a **subset** of one of the sets in $P_2$.

I have some questions about the proof related with the greatest lower bound (GLB) and the least upper bound (LUB) in the answer where it have proved the above relation $\preccurlyeq$ is one *partial ordering* and says:
> The greatest lower bound of the partitions $P_1$ and
$P_2$ is the partition P whose subsets are the nonempty sets of
the form $T_1 \cap T_2$ where $T_1 \cap P_1$ and $T_2 \in P_2$. We omit the
justification of this statement here. The least upper bound of
the partitions $P_1$ and $P_2$ is the partition that corresponds to
the equivalence relation in which $x$ in $S$ is related to $y$ in $S$
if there is a sequence $x = x_0, x_1, x_2, \ldots , x_n = y$ for some
nonnegative integer n such that for each $i$ from 1 to $n$, $x_{i−1}$
and $x_{i}$ are in the same element of $P_1$ **or** of $P_2$. We omit the details that this is an equivalence relation and the details of the
proof that this is the least upper bound of the two partitions.

Based on the "subset" definition of "refinement", it seems that there is one more elegant description of the GLB and LUB.
$$
\text{Without loss of generality, we set the assumption }T_1\text{ is the refinement of }T_2 (T_1\preccurlyeq T_2),\\
\text{ then we have the equations }\\
GLB(T_1,T_2)=T_1\qquad (*)\\
LUB(T_1,T_2)=T_2\qquad (**)\\
$$
Similar to another exercise 9.6-48 and this [comment][3] of one QA, we need to prove the above found is the lower bound (provided that it is partition here) and then the GLB, similarly for LUB.

1. I prove the equivalence of $(*),(**)$ equations with the book answer (The following is based on the **disjoint** property by partition, so we only need to care about the arbitrary equivalence classes $T_1,T_2$).
     - GLB: Based on the assumption, $T_1\cap T_2=T_1$, so they are equivalent.
     - LUB: What the book answer says is that if $x R y$ **transitively** among $P_1,P_2$ (Here I use $R$ for $R_i,i=1,2$ where $R_i$ is the corresponding relation of the $P_i$), then $x R y$ in $LUB(T_1,T_2)$. 
       But $T_1 \subseteq T_2$, so we only need to care about $T_2$, so they are equivalent.

2. Here I only proves $(*)$. Proof of $(**)$ is similar.
     - That "it is partition" is trivial.
     - Based on the reflexive property of $\preccurlyeq$ and the assumption, $(GLB(T_1,T_2) \preccurlyeq T_1)\wedge (GLB(T_1,T_2) \preccurlyeq T_2)$, so 
       $GLB(T_1,T_2)$ is one lower bound.
     - Assume that $T'$ is one arbitrary lower bound such that $(T' \preccurlyeq T_1)\wedge (T' \preccurlyeq T_2)$, then based on the assumption and the transitive property of the poset,
       $T_1 \preccurlyeq T_2$, we only needs to care about $T' \preccurlyeq T_1$ which means $T' \preccurlyeq GLB(T_1,T_2)$. So it is the GLB.

Q:

1. Is my above interpretation $(*),(**)$ of the book answer about the GLB and LUB right?

**Edited**:

1. Thanks for the comment by amrsa. My assumption is wrong which is one low-level error.

2. The above construction of LUB is same as the construction of the [path][4] which is related with the connectivity relation. $R^{\ast}$ is also implied in the following recursive process.

3. Then based on the above [QA_1][1], it has proved the GLB. But for LUB, it seems to only exclude one case but not show the exact form. Here I offer my understanding of the book and fill the details omitted by the book.

   The following uses $P'=P_1\vee P_2$ to denote the constructed LUB.
   1. It is a partition ([equivalence conditions to prove that one family of sets is partition](https://en.wikipedia.org/wiki/Partition_of_a_set#Definition_and_notation)).
     - trivially it will traverse all elements of $S$ and none of its elements is empty because $\varnothing \notin P_1,P_2$. 
       So the 1,2 of conditions hold.
     - Assume $\exists A,B\in P' \Rightarrow (A\neq B)\wedge (A\cap B\neq\varnothing)$, let $k\in A\cap B$
       then obviously $|A|>1$, otherwise $A=B$ leading to the contradiction.
       Then based on the above construction process, $k$ can **link** $A,B$ together, leading to the contradiction.
       So any two distinct sets in $P'$ are disjoint. the 3rd of conditions hold.
   2. upper bound
     - From the construction process, for any element $A_i\in P_1$, we must $\exists C_i\in P'\Rightarrow C_i\cap A_i\neq\varnothing$. Then by the "sequence $x = x_0, x_1, x_2, \ldots , x_n = y$" we get $A_i\subseteq C_i$, so we have $P_1\preccurlyeq P'$. Similarly, 
       $P_2\preccurlyeq P'$
   3. exactly least upper bound
     Here I follow the [QA_1][1] format and to prove "For any $w$ such that $P_1\preccurlyeq w$ and $P_2\preccurlyeq w$ we must have $P'\preccurlyeq w$"
     - $\forall A_i\in P_1, \exists B_i\in P_2, A_i\cap B_i\neq \varnothing$
       Then
       1. $A_i=B_i$, then $w\preccurlyeq P_1\Rightarrow \exists D_i\in w, A_i\subseteq D_i$
         Then we get $\exists C_i\in P', A_i,B_i=C_i\Rightarrow C_i\subseteq D_i$
       2. $A_i\neq B_i$
         - If $\exists D_1,D_2\in w, A_i\subseteq D_1,B_i\subseteq D_2\Rightarrow D_1\cap D_2\neq\varnothing$,
           so there must one **unique** $D_i\in w, A_i,B_i\subseteq D_i$.
         - Then take this process of $A_i$ **recursively** for $A_i\setminus B_i,B_i\setminus A_i$.
           Since this is exactly the process of construction of the "sequence $x = x_0, x_1, x_2, \ldots , x_n = y$", we get $\exists C_i\in P', A_i,B_i\subseteq C_i\Rightarrow C_i\subseteq D_i$
       
       Recursive process: Then based on 1,2 where we will also implicitly traverse $P_2$ although only assume $\forall A_i\in P_1$, we get $\forall C_i\in P',\exists D_i\in w,C_i\subseteq D_i\Rightarrow P'\preccurlyeq w$.
    
    Please point out errors if any. Thanks beforehand.


  [1]: https://math.stackexchange.com/a/937481/1059606
  [2]: https://en.wikipedia.org/wiki/Partition_refinement
  [3]: https://math.stackexchange.com/questions/2516124/is-this-poset-a-lattice-where-are-is-the-refinement-of-the-partitions-of-s#comment5196221_2516124
  [4]: https://math24.net/closures-relations.html