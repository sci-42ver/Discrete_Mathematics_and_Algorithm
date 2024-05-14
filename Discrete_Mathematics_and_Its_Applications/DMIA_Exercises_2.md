# Exercises
## 9
### 9.1
- 2,8,12~18,22~34,40,44 skipped
- example 
  - 8
    - trivial
  - 12
    - $a=k_1\cdot k_2\cdot a,k_1,k_2\in \mathbb{N^+}\xRightarrow{a\neq 0} k_1\cdot k_2=1\Rightarrow k_1,k_2=1$
- [x] 4
  - Here I only cares about antisymmetric which is somewhat more difficult to prove than others.
    - a) is antisymmetric
      while the others having "and/as" aren't.
  - IMHO here should be "if" instead of "if and only if".
- [ ] 6
  - same as 4,
    a,b,c,e,f,h) are symmetric but not antisymmetric
    d) is neither symmetric nor antisymmetric
    g) is antisymmetric but not symmetric
  - see the ans
    - see d) about antisymmetric.
- [x] 10
  - a) combine $xRy\to yRx$ and $xRy\wedge yRx\to y=x$ together
    we get $y=x$ from $xRy$
    so either $\{(x,x),\dots\}$ when $xRy$ is True 
    or $\varnothing$ when $xRy$ is False.
  - b)
    just mix. Then $\{(1,1),(1,2),(2,1),(3,1)\}$
    so $(3,1)$ is the counterexample of symmetric
    and $(1,2)$ is the counterexample of antisymmetric
- [x] 20
  - since b,c,d) all have "and", they are not asymmetric.
- [ ] 36 see the ans
  - notice here c) is $R^2$ although only based on $a<b>c$ we can't decide the $a,c$ relation
    but $b$ can be **arbitrarily** chosen.
- [ ] 38 see the ans
  $R^2\subseteq R_6$
- [ ] 42 see the ans
  - b) notice here should consider negative and $0$
  - here $\{(0,b)\}\not\subset R_1$ while $\{(0,b)\}\subset R_2$
    So $R_1-R_2$ and $R_2-R_1$ don't need to consider $\{(0,b)\}$. (only considered when both sets *share* something)
- [ ] 46 see the [code][check_relations]
  - see the ans notice reflexive means **"every"**
- [ ] 48
  - c) we can also think as $n-1$ choices with the first element
    and $n$ for the 2nd.
  - see the ans
    e) here we can't use $A=\{(\not a,\not b)\}, B=\{(a,\not b)\},C=\{(x,\not b)\}\Rightarrow A\cup B=C$ (here $x$ can be any element of the $n$ elements)
    because $A$ only has subsets which *only contains* $(\not a,\not b)$ 
    and $B$ only $(a,\not b)$
    they *all drops one type of case*, i.e. $\{(\not a,\not b),\dots,(a,\not b),\dots\}$
    this can be checked $2^{(n-1)^2}+2^{n-1}<2^{(n-1)n}$, i.e. $2^{n-1}+1<2^n$
    - Notice here $A=\{(\not a,\not b)\}$ is not same as b)
      Here it excludes "has a as its first element *or* b as its second element"
      instead of only one $(a,b)$
    - ~~Also $A'=\{\text{no ordered pair has a as its first element}\}$~~
      ~~$B'=\{\text{no ordered pair has b as its second element}\}$~~
      ~~$C'=\{\text{no ordered pair has a as its first element and b as its second element}\}$~~
      ~~Then $2\cdot 2^{n(n-1)}-$~~
    - Based on the above we should use inclusion-exclusion for relations
      instead of subsets of relations.
    - As the above shows we have $n-1$ for each element, so $(n-1)^2$.
- [ ] 49
  - a) $2^{\frac{n^2-n}{2}+n}$ since each $\{(a,b),(b,a)\},a\neq b$ must occur at the same time
  - b) same as a)
  - c) hinted by b) $3^{\binom{n}{2}}$
  - d) $2^{n^2-n}$ after removing all $(a,a)$
  - e) since all $(a,a)$ must be contained. so $1$
    then based on a) $2^{\frac{n^2-n}{2}}\cdot 1$
  - f) obviously $(a,b),a\neq b$ doesn't influence "neither reflexive nor irreflexive", so $2^{n^2-n}$
    then we need exclude "reflexive" and "irreflexive", i.e. contain all $(a,a)$ or contain none.
    so $2^n-2$.
    then $2^{n^2-n}\cdot (2^n-2)=2^{n^2}-2\cdot 2^{n^2-n}$
  - see the ans
    - b) see [this][3_choices_for_each_element]
      which uses subset denotation by $0-1$
      then $(a,a)$ can be $0,1$
      while $(a,b),(b,a)$ may be $(0,0),(0,1),(1,0)$, so $3$.
- [x] 50
  - a) $2$ trivially
  - See [check_relations]
- [ ] 52 
  a,c,d,e) are True.
  - see the ans
    - b) is also True (I forgot how I made mistakes with this)
- [x] 54
  - by the [matrix](https://en.wikipedia.org/wiki/Converse_relation#Examples)
    it means $(a,b)\cap (b,a)=0 \forall a\neq b$
    then if and only if is trivial based on this
- [ ] 56
  only if: since "reflexive" $R$ contains all $(a,a)$
  then $\overline{R}$ excludes all $(a,a)$, so "irreflexive"
  if: similar
  - see the ans for one more elegant description.
- [x] 58 see the [code](./miscs_snippets/py_codes/9-1-58/relation_power.py)
- [ ] 60
  - see the ans
    This proves [this](#power_relation_associativity)
    $$
    \text{let }(a,b)\in T,(b,c)\in S,(c,d)\in R\\
    (R\circ S)\circ T=\{(b,d)\}\circ T=\{(a,d)\}\\
    R\circ(S\circ T)=R\circ\{(a,c)\}=\{(a,d)\}
    $$
  - the rest see the ans
- [ ] 62
  See [check_relations] `transitive` it use $O(n^2)$ for each subset
  then totally $O(n^2\cdot 2^{n^2})$
  - see the ans
    - the above should be $O(n^2(n^2+n\cdot n^2))=O(n^5)$ for each subset
    - the ans should be $O(n^3\cdot 3n^2)$ 
      if caring about *traverse* of the list for whether $R(x,y)$ is in if *also using the brute force search*.
      Which corresponds to the code `in L`.
### 9.2
- 4,6,10~24,
  28~40 skipped
- [x] 2 $\binom{4}{3}+\binom{4}{2}\cdot 2$
- [x] 8
  - > this could possibly not happen, although it is perhaps less likely than in part (b)
    this means c) is "less likely" to "not happen" than b)
    i.e. more likely to happen than b)
- [x] 26
  - Here if $R \cap S$ share less than $P_{i_1 ,i_2 ,...,i_m} (R) \cap P_{i_1 ,i_2 ,...,i_m} (S)$
    then the latter contain more than $P_{i_1 ,i_2 ,...,i_m}(R \cap S)$
- [x] 41
  - similar to [3_choices_for_each_element]
### 9.3
- 2~6(1. notice here 6 is asymmetric instead of antisymmetric),
  12~32(14 has some test codes) skipped
- [ ] 8
  - transitive see the ans, the rest is trivial.
  - See the [code][transitive_realtion_check]
- [x] 10
  - see the ans
    - a) we can also think as $a\le b$ make the *order* of the pair *fixed*, so $\binom{1000}{2}$
    - d) or $1000+999+\cdots+1$
- [ ] 34
  - split into $(a,b)$ with $a=b$ and $a\neq b$ 2 cases.
    then $(a,b)\to (b,a)$.
    $(a,a)\to \neg (a,a)$ and vice versa.
  - see the ans to combine 2 cases above.
- [x] 35
  - by EXAMPLE 9 in 2.6 Matrices,
    $M_{R^{n}}=M_{R^{n-1}\circ R}=M_{R^{n-1}}\odot M_R\overset{IH}{=}M_{R}^{[n-1]}\odot M_R\overset{\text{EXAMPLE 9 in 2.6}}{=}M_{R}^{[n]}$
    - see the ans
      As [this](#power_relation_associativity) shows, the corresponding matrix order is also associative. $M_{R^{n-1}}\odot M_R=M_R\odot M_{R^{n-1}}$
- [x] 36
  - symmetric difference = union - intersection
### 9.4
- 2~12,15,16,22~30,34 skipped
- [ ] 14
  - "intersection" implies minimal
    "with property P that contain R" implies the other 2 conditions.
  - also see the ans by 2 sides of $\subseteq$
- [ ] 18 see [Warshall_code]
- [ ] 20
  - here a) can be no stop or exactly one stop based on c).
- [ ] 32
  - TODO Is the following right?
    If using ALGORITHM 1, then the iteration number $i$ when $B[j,k]$ *firstly* becomes 1 can decide the the length because 
    $M^{[n]}$ only contains path of length $l\le n$
    so "*firstly* becomes 1" implies $i-1\gt l\le i\Rightarrow l=i$
    - Or more specifically, based on the definition of boolean product of matrices
      $[M\odot M]_{jk},shape(M)=(N,N)$ contains *all possible* $N$ tuples of $(M_{j t_i},M_{t_i k})$, i.e. it contains all possible length-2 paths.
      Then based on *induction* $[M^{[n]}\odot M]_{jk},shape(M)=(N,N)$ contains *all possible* 
      $N^{n-1}\cdot N=N^n$ tuples where $M_{j t_i}$ is length-$n-1$
      $M_{t_i k})$ is length-$1$.
      The above is *similar to FIGURE 4* where here the induction is based on the length instead of interior vertex count.
  - see the ans
    - it just uses weighed graph where $\infty$ can be any consistent weigh $w>1$ IMHO.
- [ ] 35
  - b) see the ans
    here minimal can't be met because their *intersection* may not have the property $P$.
- [ ] 36
  - based on [transitive_reflexive]
    "the reflexive closure of the transitive closure of R" must be transitive.
  - As the book says
    > Adding these pairs does not produce a transitive relation, because the resulting relation contains (3, 1) and (1, 4) but does not contain (3, 4)
    addition due to "the symmetric closure" may destroy the "transitive closure".
    - see the ans for examples.
### 9.5
- 6,
  14~20(similar to 12),
  22,26,30~38,42,
  46~50,68 skipped
- [ ] 2
  - see the ans
    - here "a ..." is at issue.
- [ ] 3
  - based on exercise 9 where $h$ here is $f$ there,
    a) think as $h:f(x)\to f(1)$
    b) see the ans $f(0)=g(0),g(1)=k(1)$
    The rest is trivial
- [ ] 4 see the ans where the 3rd is congruence.
- [ ] 8
  - > If f is a bijection from S to T , then f−1 is a bijection from T to S, so R is symmetric
    See [this](https://math.stackexchange.com/a/1515642/1059606)
  - see the ans for the detailed proof
  - $\mathbb{Z}$ is [countable](https://math.stackexchange.com/a/3463563/1059606)
    - [$\mathbb{Q}$](https://math.stackexchange.com/a/333289/1059606) which is based on prime factorization or the book one
    - $\mathbb{R}$ [uncountable](#rational_countable_real_uncountable). [Also for](https://math.stackexchange.com/a/733/1059606) [$\mathbb{I}$](https://math.stackexchange.com/a/450528/1059606)
    - [$\mathbb{P}\subset \mathbb{N}$](https://en.wikipedia.org/wiki/Prime_number#Definition_and_examples)
- [ ] 9
  - here $=$ implies the equivalence relation.
    This is same as the ans of 18
    > “a and b are equivalent if they have the *same whatever*” is an equivalence relation
  - b) see the ans 
    here $[a]=\{f^{-1}(f(a))\}$ where 
    $f^{-1}$ is one-to-mul ~~function which is not one function strictly speaking.~~ [relation](https://qr.ae/pKxqjx)
- [ ] 10
  - see the ans
    - > such that (x, y) ∈ R if and only if f (x) = f (y)
      here "if and only if" is only defined inside "such that ..."
    - $f$ is just $R$.
      then it becomes $xRy\leftrightarrow [x]=[y]$ which is already proved in THEOREM 1. 
- [ ] 12 see the ans
- [x] 24 see [transitive_realtion_check]
  - it should contain many submatrix which is **all ones**. <a id="submat_equivalence_relation"></a>

    Here prove it *based on the assumption of Equivalence Relation*.
    since one row imply the relation of one element with others, let it be row [$r_{i\cdot}$](https://math.stackexchange.com/a/2741774/1059606)
    then if $r_{ij}=1$
    then for $r_{j\cdot}$, it should be **same** as 
    $r_{i\cdot}$ because elements $e_j R e_{i}$, then by transitivity, 
    $\forall k,r_{ik}=1\Rightarrow e_{j} R e_{k}$.
    - As 9.5-62 says, this submatrix is just the **partition**.
- [x] 28
  - for d) we can think it like the plane pencil.
- [ ] 40 b) see the ans where all fractions are equivalent to the corresponding [Irreducible fraction](https://en.wikipedia.org/wiki/Rational_number#Irreducible_fraction).
- [x] 44
  - a,c,d) are.
    b,e) are not
- [ ] 52
  - > $R_n$ refers to the family of equivalence relations defined in Example 5
    [family](https://math.stackexchange.com/questions/3786044/partition-and-equivalence-relations-classes#comment7798229_3786044) means "collection of distinct"
  - see the ans the proof should be $x\in [y]_{R_4}\Rightarrow x\in [y]_{R_3}$
- [ ] 54 
  - ~~it is the definition of "refinement".~~ (This is wrong.)
    > A partition P1 is called a refinement of the partition P2 if every set in P1 is a subset of one of the sets in P2
    This means $[a]_{R_1}\in [a]_{R_2} \forall a\in A$ where A is the set related with partition $P_1$.
  - see the ans for detailed proof.
- [ ] 56
  - only a)
  - see the ans
    - a) based on the [submat_equivalence_relation] proof, (0,2)x(0,2) and (3,3)x(3,3) submat with 2 (0,1)x(0,1) submats will becomes
      ```python
      1110
      1110
      1111
      0011
      ```
      the the 3rd and 4th rows don't meet the requirements.
      i.e. for example $e_3 R_2 e_3, e_3 R_1 e_1\nRightarrow e_4 (R_2\cup R_1) e_1$ (This is trivial to see since $R_2\cup R_1$ only $\cup$ relations but not do transitive operation based on them).
    - b) since the intersection of submats must be the submat. So it is True.
      strict proof:
      $$
      \text{let arbitrary }(a,b),(b,c) \in R_1 \cap R_2\text{ on the set }A\\
      \begin{cases}
        \text{trivial because they share }(x,x)\forall x\in A &\qquad \text{reflexive}\\
        ((a,b)\in R_1)\wedge((a,b)\in R_2)\Rightarrow ((b,a)\in R_1)\wedge((b,a)\in R_2)
        \Rightarrow (b,a)\in R_1 \cap R_2 &\qquad \text{symmetric}\\
        \text{substitute }(a,b)\text{ with }(a,b),(b,c)\text{ in proof w.r.t. symmetric}\Rightarrow (a,c) \in R_1 \cap R_2 &\qquad \text{transitive}
      \end{cases}
      $$
    - c) use the same examples as a)
        $$
        \begin{bmatrix}
          0&0&1&0\\      
          0&0&1&0\\
          1&1&0&0\\
          0&0&0&0
        \end{bmatrix}
        \cup
        \begin{bmatrix}
          0&0&0&0\\      
          0&0&0&0\\
          0&0&0&1\\
          0&0&1&0
        \end{bmatrix}=\begin{bmatrix}
          0&0&1&0\\      
          0&0&1&0\\
          1&1&0&1\\
          0&0&1&0
        \end{bmatrix}
        $$
      - Also see the ans which is trivial. 
- [ ] 58 compare it with 6.4-exercise-42 where the elements must be distinct.
  - b) $1+3\cdot 2+3$
  - here corresponds to [$D_3$](https://en.wikipedia.org/wiki/Dihedral_group)
  - TODO generalize this to n-bead counting by combinatorics.
  - > The composition of any two of these operations is again one of these operations
    by [table](https://en.wikipedia.org/wiki/Dihedral_group#Group_structure) or [linear algebra](https://en.wikipedia.org/wiki/Rotations_and_reflections_in_two_dimensions#Mathematical_expression)
    > And transitivity follows from the group table
    i.e. product table / Cayley table shown in the above link.
  - Similar to 59
    here relatiton is the sequence of rotation or reflection operations.
    So
    > Each operation has an inverse
    i.e. let $a,b$ be bracelets of the same class, inverse is just swap the locations of $a,b$ in $a R b$.
  - > This would not be the case if there were four or more beads, however. For example, in a 4-bead bracelet with two reds and two whites, the bracelet in which the red beads are *adjacent* is not equivalent to the one in which they are not.
    See 59
  - a) is same as 59 a)
    - > The $0^o$ rotation plays the role of the identity
      corresponds to
      > R is reflexive because any coloring can be obtained from itself via a *360-degree* rotation
    - the rest is done by enumeration in 58 while by all map into reflections in 59.
- [ ] 59
  - b) $\overbrace{2}^{2R,2B}+\overbrace{2}^{\text{swap }R,B}\cdot(\overbrace{1}^{4B}+\overbrace{1}^{3B,1R})$
  - see the ans
    - here Reflection mat with [$y=mx+c$](https://math.stackexchange.com/a/3865554/1059606)
      let $l_1,l_2$ be the lines parallel to $AB$ including $P',P$ respectively and $NN',N'\in l_2$ perpendicular to x-axis
      then $\vec{N'N}=(0,mx-y+c)$
      then let $NM_1\perp l_2,M_1\in l_2$ and $M_1M_2\perp NN',M_2\in NN'$
      then $\vec{N'N}=(0,\frac{mx-y+c}{1+m^2})$ this corresponds to $\vec{PP'}_y/2$
      so $2\cdot \vec{N'N}=\vec{PP'}_y\Rightarrow 2\cdot \frac{mx-y+c}{1+m^2}=\frac{y'-y}{1}$

      We can let $m=tan\theta,\theta\in (0,\frac{\pi}{2})$ to think of the above graph
      - Here Reflection matrix without $c$ can be also got from [eigen](https://math.stackexchange.com/a/1137744/1059606) ([check](./miscs_snippets/py_codes/9-5-58/reflection.py)) or by [direct calculation](https://math.stackexchange.com/a/525112/1059606)
    - > each rotation is the composition of two reflections
      - proof 
        - [1](https://math.stackexchange.com/a/566333/1059606) <a id="abstract_algebra_2"></a>
          TODO reflexive axes
          - Maybe similar to [this](https://en.wikipedia.org/wiki/Rotations_and_reflections_in_two_dimensions#Process) [i.e.](https://math.stackexchange.com/a/487109/1059606)
            Assume $L_2$ is at the counterclockwise direction of $L_1$.
            (The following allows angle to be negative which means the opposite direction of the positive one). Assume $\angle POL_1=\alpha>0$ (This means $L_1$ is at the counterclockwise direction of $P$) then $\angle L_2OP'=\alpha-\theta$
            Then $\angle P''OL_1=\alpha-2\cdot \theta$. So $\angle POP''=2\cdot \theta$
        - Also [see](https://math.stackexchange.com/questions/2804893/show-that-the-composition-of-two-reflection-is-a-rotation#comment10305692_2804910)
    - > in the opposite order
      it can be also easily by conversing the order of rotation and reflection.
    - The above b) only shows class number
      - Here $\binom{4}{i},i\neq 2$ is in one class respectively.
        $\binom{4}{2}$ is splitted by adjacent same or not.
- [ ] 60
  - by [this][Big_O_Notation]
    $k_1=k_2=1,f=g$ -> reflexive
    $k_{1,2}>0$ so symmetric.
    $(k_{i}=k_{i1}\cdot k_{i2}) \wedge (n_{0}=max(n_{0i})), i=1,2$ -> transitive
  - see the ans
    - transitive is same as the proof in Exercise 17 of Section 3.2.
    - b) doesn't need to be polynomial.
      - > Another way ...
        just uses the definition of $\Theta$.
- [ ] 62
  - by [submat_equivalence_relation] The following $211$ means submatrix size sequence which can be reordered.
    $\overbrace{1}^{1111}+\overbrace{3}^{211}+\overbrace{1}^{22}+\overbrace{2}^{31}+\overbrace{1}^4$
  - see the ans
    - the above is wrong because the submatrix can be formed by disjoint parts like $(0,2)$ and 
      $(1,3)$ for 4x4 mat.
    - Then it is just the Stirling numbers of the second kind. See [Stirling_second_kind_code]
- [x] 63
  - Here the order matters.
    > the transitive closure of the symmetric closure of the reflexive closure
    the symmetric closure won't break reflexive because of only adding relations.
    similarly for "transitive".
- [x] 64
  - different from 63, symmetric will break "transitive". For example, $\{(a,b),(a,c)\}\xrightarrow{\text{reflexive closure by adding} (a,a)}\cdots\xrightarrow{\text{symmetric closure}}\{(a,b),(a,c),(b,a),\cdots\}.\text{ But }(b,c)\notin \{(a,b),(a,c),(b,a),\cdots\}$
    This is similar to one exercise before.
- [x] 66
  - By THEOREM 1 (i) and (ii) equivalence (i.e. one-to-one correspondence) and (iii) disjoint property.
    Here (i) -> relations (ii) -> partition.
    Then relation $R$ and partition $P$ also have the one-to-one correspondence property.
### 9.6
- 2 (Also see [transitive_reflexive]),14~20,
  24(1. inclusion -> $\subseteq$. 2. Notice Hasse diagram doesn't remove any element in the set)~26,
  28([Proper Divisor](https://mathworld.wolfram.com/ProperDivisor.html#:~:text=A%20positive%20proper%20divisor%20is,but%206%20itself%20is%20not.) means *less* than similar to [proper fraction](https://mathworld.wolfram.com/ProperFraction.html)),
  30(by just appending one element to $C_1$ or adding $1$ to $A_1$. calculated by `import math;sum([math.comb(3,k)*(3-k) for k in range(3+1)])*4+8*3` in `python`),
  34,42(similar to 40)~44,
  50~52,53(1. prove by finding such a least element. [Detailed](https://proofwiki.org/wiki/Lexicographic_Order_on_Pair_of_Well-Ordered_Sets_is_Well-Ordering) or [this more general (1. "It is clear that" is by definition which can be generalized to $T_k,k>1$ despite not the one-to-one mapping and $T_1=S$ 2. Here it thoughts $(x,x_1,\ldots,x_{k+1})$ as $(x,\vec{x'})$ where the total can be thought as 2-tuple, the former can be proved using $S$ and the latter can be proved using IH)](https://proofwiki.org/wiki/Finite_Lexicographic_Order_on_Well-Ordered_Sets_is_Well-Ordering) 2. total ordering is [implied by the definition (1. "Necessary Condition" means if 2. prove by examining all cases 2.1 Notice $x_2=y_2$ implies $x_2\preccurlyeq y_2,y_2\preccurlyeq x_2$)](https://proofwiki.org/wiki/Lexicographic_Order_on_Pair_of_Totally_Ordered_Sets_is_Total_Ordering) of the lexicographic order 3. [infinite case](https://proofwiki.org/wiki/Infinite_Lexicographic_Order_on_Well-Ordered_Sets_is_not_Well-Ordering) based on [padding](https://en.wikipedia.org/wiki/Lexicographic_order#Definition) where the induction fails for $T_{\infty}$ because $T_{\infty-1}=T_{\infty}$ although $T_{k+1},k\in\mathbb{N}$ still works),
  56,62~64 skipped
- [ ] 4
  - see the ans
    - a) although $no shorter$ seems to be $\ge$ which is the partial ordering
      but maybe $a=b,a\neq b$ -> not antisymmetric.
- [x] 6
  - a) is both equivalence relation and the partial ordering.
- [x] 8
  - a) similar to [submat_equivalence_relation]
    $M_{ij}=1\Rightarrow M_{i\cdot}\ge M_{j\cdot}$
    Then $M_{21}=1$ but $M_{23}<M_{13}$, so not transitive.
- [x] 10 b->d doesn't exist.
- [ ] 12 (just converse the order of each relation. Trivially proof is also the converse version)
  - detailed see the ans.
- [x] 22 
  - a) see the ans 
    here the ans may be wrong. It shouldn't include $(4,6)$
- [ ] 31 construct many sub-chains
  - hint:
    from covering relation to closure: reflexive transitive closure is trivially antisymmetric by the covering relation
    from closure to covering relation: closure -> contain the covering relation
  - see the ans for the detailed proof
    - it uses $\text{closure }\subseteq (\preccurlyeq)$ and converse to prove equivalence.
      - Here "sequence" is based on "transitive".
    - The above "from closure to covering relation" should prove why "a finite poset is closure".
- [x] 32
  1. [Maximal Element](https://mathworld.wolfram.com/MaximalElement.html) for partial ordering 
    Also see [this](https://en.wikipedia.org/wiki/Partially_ordered_set#Extrema) for the Upper and lower bounds where it [defaults that](https://en.wikipedia.org/wiki/Partially_ordered_set#Notation) the relation is $\preccurlyeq$.
  2. e) i.e. find $upper_bound(d,c)$ then 
    $upper_bound(k)$
  3. The rest is trivial.
- [x] 36 see FIGURE 6
  - see the ans
    - b) here $\preccurlyeq$ is $\ge$
      then $1$ is the **last** element in the sequence of $a\ge \cdots\ge 1$, so Maximal
      This is same as what 44 ans says
      > since here “greater” really means “less”!
- [ ] 38 similar to [lexicographic_order_partial_order_proof]
  we define $\preccurlyeq$ by modifying EXAMPLE 10 definition $m < n$ to $m\le n$
  - Also see this [QA](https://math.stackexchange.com/q/4840174/1059606)
    - > Then $a_1 \ldots a_l \preccurlyeq b_1 \ldots b_l \preccurlyeq c_1 \ldots c_l,a_1 \ldots a_l = c_1 \ldots c_l\Rightarrow a_1 \ldots a_l = b_1 \ldots b_l = c_1 \ldots c_l$
      is similar to 9.6-49 answer
      > which implies that $T = T′$ because 
        $T \subseteq T′ \subseteq T′′$.
  - see the ans
    - > Now if $a_1 \ldots a_l < b_1 \ldots b_l < c_1 \ldots c_l$, then clearly a1 ...am < c1 ...cp
      1. here if $l=n<m,p$
         then by lexicographic order definition, $a_1 \ldots a_l < c_1 \ldots c_l \xRightarrow{s\ge n} a_1 \ldots a_s < c_1 \ldots c_s$
      2. If $l=min(m,p)$ then 
        $a\preccurlyeq c$ trivially holds.
    - Here $m \le p$ should be $m<p$
      > If l = t, then m < n and m ≤ p
      here $l=min(m,n)=t=m$ so $l=min(m,n,p)\le p$
      Then the exclusion of $=$ is due to: 
      $p\le m<n\Rightarrow p\le n$ which will make $b_1 \ldots b_n<c_1 \ldots c_p$ only has the possibility of $b_1 \ldots b_r < c_1 \ldots c_r$. So we need excluding $p<m<n$
    - > In the former case, if r > l, then since p > m we have a1 ...am < c1 ...cp
      here ~~we~~ ~~may not need $p>m$ since $r>l, b_1 \ldots b_r < c_1 \ldots c_r \Rightarrow b_1 \ldots b_l < c_1 \ldots c_l$. Then based on the assumption $a_1 \ldots a_l = b_1 \ldots b_l$, we get $a_1 \ldots a_l < c_1 \ldots c_l$ which is what we want to prove.~~
      1. $r=min(n,p)>l\Rightarrow p>l=t=m$
      2. we may have $b_1 \ldots b_l = c_1 \ldots c_l$, so we need $p>m$.
      ~~we don't need $p>m$, since $r>l$ then $p>l$~~
    - TODO Since $m<n<p$ it is impossible for $r=l$ since $r\ge n,p >m=l$
    - > In the latter case, $a_1 \ldots a_s = c_1 \ldots c_s$
      here $s=l=m$
    - > If l < t, then we must have b1 ...bl < c1 ...cl
      since $l=min(t,r)<t\Rightarrow l=r$
      Then by $b_1 \ldots b_n < c_1 \ldots c_p$ we can get $b_1 \ldots b_r < c_1 \ldots c_r$, i.e. $b_1 \ldots b_l < c_1 \ldots c_l$
      ~~1. $r=n\Rightarrow n<t\Rightarrow t=m,n<m\Rightarrow p\le n<m$~~
    - In summary it splits cases based on $len(\{c_i\})=p$ (although not strictly) if assuming 
      $a_1 \ldots a_l = b_1 \ldots b_l$ -> $m<n$
      - $p<m$ ~~-> $l=min(t,p)<t$~~ corresponds to the ans $l<t$
        here $p\ge m$ can't exist. Since $l<t\Rightarrow l\neq m,n \Rightarrow l=p\le m,n$ (Here we only take in account $<$)
        ~~Assume $p\ge m$ then based on the above, ~~
      - $p=m\Rightarrow t=r\Rightarrow r=t=l$
      - ~~$m<p<n$~~
    - Here
      $$
      \text{assume } b_1 \ldots b_l = c_1 \ldots c_l\\
      t = min(m,n) , r = min(n,p) , s = min(m,p) ,l = min(m,n,p)\Rightarrow r,t\le l\\
      \begin{cases}
        1.\; l=r(\text{correspond to the original answer }l<t)\Rightarrow n<p,m\ge (r=n) \Rightarrow r=n \Rightarrow t=n=r=l\\
        \Rightarrow
          a_1 \ldots a_t<b_1 \ldots b_t\\
          \Rightarrow
          \begin{cases}
          t=l(\text{similar to the original ans "if r = l, then ..."})&\Rightarrow a_1 \ldots a_l<b_1 \ldots b_l \Rightarrow a_1 \ldots a_l<c_1 \ldots c_l \Rightarrow a_1 \ldots a_m = c_1 \ldots c_p\\
          t<l(\text{impossible})&
          \end{cases}\\
        2.\; l=min(m,r)<r(\text{correspond to }l=t \text{ but }r=l\text{ there is included in case 1})\\
        \Rightarrow (l=t) \wedge (p,n>m)
        \begin{cases}
          a_1 \ldots a_t<b_1 \ldots b_t &\Rightarrow a_1 \ldots a_l< c_1 \ldots c_l\Rightarrow a_1 \ldots a_m = c_1 \ldots c_p\\
          a_1 \ldots a_t=b_1 \ldots b_t,m<n &\Rightarrow a_1 \ldots a_l = c_1 \ldots c_l\Rightarrow a_1 \ldots a_m = c_1 \ldots c_p \text{ due to }p>m
        \end{cases}
      \end{cases}
      $$
- [ ] 40
  - ~~a) it can also be proved by contradiction for ~~
    here $a\preccurlyeq a$ is possible so no contradiction.
  - see the ans
- [ ] 45
  - see the ans 
    similar to [finite_chain_maximum_minimum]
- [ ] 46
  - $(S,R^{-1})$ is the converse version of $(S,R)$
  - better explicitly saying the existence of LUB and GLB
    see the ans
- [ ] 48 see the ans for the strict proof of the least upper bound and greatest lower bound.
- [x] 49 similar to 48, here we are based on $\subseteq$
  - > The greatest lower bound of the partitions P1 and P2 is the partition P whose subsets are the nonempty sets of the form $T_1 \cap T_2$ where $T_1 \in P_1$ and $T_2 \in P_2$
    ~~based on the refinement, it just means $GLB(T_1,T_2)=Refined_one(T_1,T_2)$~~
    See [this][refinement_lattice]
- [ ] 51 see 45 or supplementary 42
- [ ] 54
  - see the ans
    - notice d) is $\ge$.
- [ ] 58
  - due the *finite* alphabet -> neither well-founded nor dense
  - see the ans
    - It is to find the counterexample.
    - > there is no element between a and aa in this order
      to make $a$ bigger,
      1. next letter, so $b$, but $b\succ aa$
      2. length longer, then $ax$, $ax\prec aa\Rightarrow x=a$
        $axy$ is impossible because $x=a\Rightarrow axy\succ aa$ or $x\succ a\Rightarrow ax\succ aa\Rightarrow axy\succ aa$
- [ ] 60 see the ans where it shows it is same as the proof of LEMMA 1.
- [x] 66
  - $\overbrace{F\prec F\prec R\prec E}^{\text{the trivial minimal set}}\overbrace{\prec Exterior painting\prec Exterior fixtures}^{\text{one distinct straight line path}}\overbrace{\prec Plumbing \prec Wiring}^{\text{one convergent point from 2 paths}}\overbrace{\prec Flooring \prec Wall-board}^{\text{similar to the former}}\overbrace{\prec Carpeting}^{\text{one distinct path}}\overbrace{\prec Interior painting\prec Interior fixtures\prec Completion}^{\text{one straight line}}$
### supplementary
- 6~8,22,30,36(~~although the ANS exercise reference is wrong.~~),44 skipped
- [x] 2
  - Let $S$ be reflexive set, $f(T)$ is the symmetric corresponding relations of 
    $T$
  - a) $T=\{(a,b),(b,c)\}$, then 
    $T\cup S\cup f(T)$
  - b) $T=\{(a,b)\}$
    $T\cup f(T)\cup \{(a,a),(b,b)\}$
  - c) $T$ of a)
  - d) $T=\{(a,b),(b,a),(b,c)\}$, then by the transitive property, append 
    $(a,c)$
    so $T\cup S$
  - e) this has the least restriction, so easily $\{(a,a),(a,b),(b,a),(b,c)\}$ 
- [ ] 4 see the ans for the detailed proof
- [ ] 10
  - only if:
    - symmetric: let $c=b$
    - transitive: $cRa,aRa\Rightarrow aRc$
  - if:
    - $aRc\xRightarrow{\text{symmetric}}cRa$
  - see the ans
    - we can use the conclusion of "symmetric" when "transitive"
- [ ] 12
  since [the Natural join](https://en.wikipedia.org/wiki/Relational_algebra#Natural_join_(%E2%8B%88)) implies subset, so yes.
  - see the ans
- [ ] 14 b) is related with [refinement_lattice].
- [ ] 16 
  - a) "call ~~recursively~~ transitively", i.e. if $P$ calls $Q$, $Q$ calls $R$, then we think that $P$ calls $R$.
  - the rest is trivial
- [ ] 18 trivial by definition
- [ ] 19 
  - similar to 9.4-32, change $\infty$ to $x\in\mathbb{N^+},x>1$
    and change $min$ to $max$.
  - see the ans
    - it should init to $-1$ to indicate *no* path
    - the above lacks loop which will cause infinite long.
    - notice here $k$ can be $i,j$ *if possible*.
- [ ] 20
  - see the ans notice here c) is "have been"
- [x] 21 This is exactly [${5 \brace 3}$](https://en.wikipedia.org/wiki/Stirling_numbers_of_the_second_kind#Table_of_values)
- [x] 24 [See](https://math.stackexchange.com/a/4840776/1059606)
  - "smallest" because we can't remove something.
  - This is similar to one exercise 9.5-63 before based on "the transitive closure of the symmetric closure of the reflexive closure"
- [ ] 26 the partial ordering has been proved in [refinement_lattice].
  - see the ans
    - It uses one-to-one correspondence to another partial ordering.
- [ ] 28 see the ans 
  It is just find one sub-total-ordering.
- [ ] 29 see the ans
  It is to find the max subset which corresponds to *only one level*. 
  - Also see 30 which I did after writing the above line
- [ ] 31 
  - I didn't do this exercise
    but the term "maximal chain" is met when I was reading ~~chapter 10.~~ something
    See [this related QA](https://math.stackexchange.com/q/4840957/1059606)
- [ ] 32
  - trivially, it can be partitioned into chains,
    *assume* it can be partitioned into $k$ chains which is the *minimal* chain number. (This can be got from $R^{\ast}$ by constructing one sequence. It is similar to constructing one partition.)
    Then we can construct one antichain by choosing one from each chain. (This is same as the wikipedia $A_0\cap C_i\neq \varnothing$)
    And by the pigeonhole principle, $k$ can't be larger for the antichain.
    - This is wrong based on [Dilworth_theorem_proof_combination]
      because it needs to prove from "the largest number of elements in an antichain" to "partitioned into k chains" instead of the converse version.
  - [wikipedia][Dilworth_theorem_proof_wikipedia] same as [Dilworth_theorem_proof_combination] (similar to the [graph_theory] book proof p68) where the latter proof 2 has the exact same description as this exercise (Also same as the brilliant wiki).
    - > Clearly, $A_0\cap C_i\neq \varnothing$
      This is based on the hypothesis.
    - ~~TODO Here $x_i$ may be unique.~~
      > For $i=1,2,\ldots,k$, let $x_i$ be the maximal element in $C_i$ that belongs to *an* antichain of size $k$ in $P'$
      Here it doesn't mean $x_i\in A_0$
    - > since $x_i \not\ge y$
      this is due to *disjoint* chains
      TODO Then we can *directly* get $x_i \not\ge x_j$
    - Compared with [Dilworth_theorem_proof_combination]
      - > By interchanging the roles of i and j in this argument we also
        complement the proof there
      - > Then by the choice of $x_{i}$, $P\setminus K$ does not have an antichain of size $k$
        > since $A \setminus \{x_i \}$ is an antichain
        says in more details.
      - > since a is maximal in P
        so only $a\ge x_i$ is possible. Since it is already excluded, so $a$ has *no relation*.
      - [Duality](https://en.wikipedia.org/wiki/Dilworth%27s_theorem#Dual_of_Dilworth's_theorem_(Mirsky's_theorem)) Notice here partition corresponds to [brilliant_wiki_Dilworth_Theorem_antichain_ge_chain] "cover" (Here I refer to the more detailed brilliant wiki for the proof)
        - > Note that if $f(s)=f(t)$, then s and t cannot be comparable (why?).
          WLOG, suppose $s\prec t$
          then we can append the chain corresponding to $s$ with $t$, so it can be larger -> contradiction.
        - here $f^{-1}(n)$ is one one-to-mul ~~function~~ relation.
        - Notice here ~~"The size of a maximal chain"~~
          > The size of a maximal chain in S equals the size of a minimal antichain cover of S.
          better use "largest chain" as wikipedia because we can have multiple ["maximal chain"](https://proofwiki.org/wiki/Definition:Maximal_Chain), e.g. if some element is incomparable, then the maximal chain including it only has one element.
          - Then 
            > the size of a maximal chain whose largest element is s
            can have
            > then the sets $f^{-1}(1),f^{-1}(2),\ldots,f^{-1}(d)$ form an antichain cover of S
            - Here cover because the chain size is $1\sim d$.
          - TODO ["How to get one maximal chain based on one finite saturated chain"](https://math.stackexchange.com/questions/4840957/how-to-get-one-maximal-chain-based-on-one-finite-saturated-chain)
            Also [see](https://math.stackexchange.com/questions/4449496/are-all-incomparable-elements-in-a-set-considered-both-maximal-and-minimal#comment9317813_4449496) and [a finite chain always has a smallest and largest element][finite_chain_maximum_minimum]
        - > It is not immediately obvious that these sets are all nonempty (though they are), but this shows that there is an antichain cover of size at most d
          since maybe $\exists f^{-1}(i),i=1\sim d, f^{-1}(i)=\varnothing$, so "at most"
          Then based on "equals the size", they can't be $\varnothing$.
        - > as the horizontal "strips" of the Hasse diagram
          This is just similar to the strip in Dilworth's one (strip is one delimiter and connector)
          - > It is straightforward to check that the two Hasse diagrams in the above examples are constructed in that way.
            i.e. all elements at level k are incomparable. This is as as this textbook.
    - Its [reference_1][galvin]
      main idea is 
      > We have to show that P either contains an (n + 1)-element antichain, or else is the union of n chains
      - Also see [Dilworth_theorem_proof_combination]
      - It assumes 
        > he width of P is the *maximum* cardinality of an antichain in P. According to a celebrated theorem of Dilworth [2], the *width* of P is also equal to the *minimum* number of chains needed to cover P
      - > If $A \cap \{a\}$ is an antichain, we are done
        i.e. $a$ is incomparable to all the others
        Then $n+1$ *chains* and *antichains*.
      - > P. Let a be a maximal element of P
        so 
        > Otherwise, we have $a > a_i$ for some i
      - > there are no n-element antichains in P\ K,
        because $\{x\in C_i\}$ has been removed.
      - In summary
        Based on the above assumption, It proves possible equality of "width" and chain size.
        It uses the induction for $P\setminus \{a\}$
        then 2 cases for $a$ by proving *chain size based on antichain size*.
        1. $A \cap \{a\}$ -> antichain, so $a \not R x_i,i=1\sim n \Rightarrow a\not R c_i,c_i\in C_i$
          Based on this disjoint property, we get the chain $C_1,\ldots,C_n,a$
        2. $\{a\} \cup \{x\in C_i\}$ 
          This is done by removing one chain (implicitly one element in $A$)
          Then use the induction where $m=n-1$.
    - [graph_theory] proof
      [maximal chain](https://math.stackexchange.com/a/3444596/1059606)
      **One side**
      - > Since no two elements of an antichain can belong to the same chain, we need at least as many chains as the minimal size of an antichain
        it should be "maximal size of an antichain" $k$
        since it is possible for $k$ elements incomparable, so they should be in disjoint chains.
        It is same as [brilliant_wiki_Dilworth_Theorem_chain_ge_antichain]
      **Another side**
      Basic idea: 
        > If every antichain in a (finite) partially ordered set P has at most m elements then P is the union of m chains

        Here it proves the $k$ can be achieved, so by the inherent property of $min$, $k\ge$ "min chain size".
      - > since the maximal element of C does not belong to $S^-$ and the minimal element of C does not belong to $S^+$
        ~~Since $S^-=\{x\in P\vert x\le a_i\text{ for some }i\}$~~
        ~~it should be "minimal element ... not belong to $S^-$"~~
      - > For in that case the chains C;- and ct can be *strung together* to give a single chain
        ~~it can't be larger because by induction, it can only be ~~
      - In summary, compared with reference_1, it removes one more general thing a [maximal chain](https://proofwiki.org/wiki/Definition:Maximal_Chain) $C$ (So $C\cup \{x\}$ is not one chain) instead of one *maximal element*.
        ~~And its induction is based on antichain size $|P|$ instead of $P$ size [$n(P)$](https://en.wikipedia.org/wiki/Cardinality) which is shown in the brilliant wiki "So now suppose that the largest antichain".~~
        Then 
        1. $|P|<m$ directly induction.
        2. $|P|=m$ 
          - **TODO** by reference_1 "removing one chain", it seems impossible.
            This is also shown in [Dilworth_theorem_proof_combination] 
            > Now assume that ...
          - The key is to string $S^+,S^-$
            then $a_i< x\le a_j$ will lead to contradiction by transitivity.
            So based on
            > The proof will be completed if we show that a; is the maximal element of C;- and the minimal element of ct.
            finished.
          - Here we will construct $m+1$ chains, so $\ge min$.
        - [brilliant_wiki_Dilworth_Theorem_antichain_ge_chain] is similar but removing $\{m,M\}$ where the induction is based on $d$ (No reference here, so I didn't read it detailedly.) 
          (Since it removes elements, so it is similar to reference_1)
          - Since 
            > $m\le z$ for all comparable $z$
            ,so
            > $m\notin S^+$
          - ~~Here $C_{a}^{-}\cup \{a\}\cup C_{a}^{+}$ is more appropriate than [Dilworth_theorem_proof_combination].~~
          - Key sentences
            1. > it can't be larger because T is a subset of S
            2. > picture the Hasse diagram for S where the *largest antichain* consists of a *horizontal strip*. Take everything below the strip and everything above the strip, use *induction to cover these by chains*, and then link the chains together by *connecting them across the strip*.
          - [brilliant_wiki_Erdős_Szekeres_Theorem]
            The exact [definition](https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Szekeres_theorem#) uses "distinct real numbers"
            So
            > an antichain is a decreasing subsequence.
            assume $i\neq j, a_i<a_j\text{ or }a_i>a_j$
            - > the set has at most rs elements, which is impossible 
              It implies [Pigeonhole principle](https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Szekeres_theorem#Pigeonhole_principle)
    - ~~Notice reference_1 and the [graph_theory] don't prove "The *minimal* number m of disjoint chains"， so it is only half as~~ [Dilworth_theorem_proof_combination]
      - The first part same as [graph_theory] and [brilliant_wiki_Dilworth_Theorem_antichain_ge_chain]
        IMHO, This is one is the most detailed among these 3 versions (But better also view other 2 versions roughly).
        - Its [reference](https://core.ac.uk/download/pdf/82310575.pdf)
        - Notice here $C=\{0,1\}$ may [only have one element](https://math.stackexchange.com/q/1137771/1059606)
        - > has at most M−1 elements, ...
          so $m\le M-1+\overbrace{1}^{C}\Rightarrow m\le M$
        - Notice here $P^+,P^-$ is based on $P$ instead of $P\setminus C$.
          So $P^+ \cup P^- =P$
        - Here I give a summary of this method
          $$
          \begin{cases}
            m\ge M, \text{ trivial}\\
            m\le M
            \begin{cases}
              \text{all incomparable}:\text{ trivial}\\
              \text{some are comparable}:\text{ based on conditions of }Anti_chain_size(P\setminus C)
              \begin{cases}
                \le M-1,\qquad\text{IH}\\
                =M\quad\text{see brilliant Key sentences}\\
                >M\quad\text{see brilliant Key sentences}
              \end{cases}
            \end{cases}
          \end{cases}
          $$
      - The second part
        It proves chains can be $k\le r$ although the quote uses "partitioned into r chains".
        - > It is not difficult to see that A={a1,…,ak} is an antichain in P′
          It may be more easily by
          > By the *induction hypothesis*, P′ is the union of k disjoint chains C1,…,Ck
          This just means P' can't be into *less chains* than $k$. So $\forall (a_1,\ldots,a_k)\in C_1\times \ldots\times C_k$ (Here we use the Cartesian product) $(a_1,\ldots,a_k)$ is one antichain.
          - ~~Otherwise, if $A_i,A_j=A$ then $x=a_i$~~
            ~~Then **"hence by transitivity" can't be used**.~~
            Based on the assumption $a_i<a_j$ (Here based on the partial ordering, better $a_i=a_j$), $(A_i\neq A_j)\neq A\Rightarrow x\neq a_i$
        - > If $A\cup \{a\}$ is an antichain in P , then $k\le r−1$
          because $k$ corresponds to $A$
          $r$ is the *largest* antichain size of $P$, so $r\ge k+1$ where $k+1$ corresponds to one possibility $A\cup \{a\}$
        - > there are no k-element antichains
          otherwise $(P\setminus K)\cup \{x\in C_i:x\le a_i\}=P'$ will have 
          $k+1$ antichains -> contradiction.
- [ ] 33
  - See 32 same as [brilliant_wiki_Erdős_Szekeres_Theorem]
  - see the ans
    - but there all real numbers can be compared, so it is one total ordering
    while here it is only one partial ordering.
    - To prove $A\vee B$
      It proves $\neg B\Rightarrow A$.
- [x] 34
  - [Well-founded](https://en.wikipedia.org/wiki/Well-founded_relation#:~:text=In%20mathematics%2C%20a%20binary%20relation,not%20have%20s%20R%20m.)
    > every non-empty subset $S \subseteq X$ has a minimal element with respect to R
    this is same as the book exercise definition 
    > A poset $(R, \preccurlyeq)$ is well-founded if there is no infinite decreasing sequence of elements in the poset, that is, elements $x_1, x_2, \ldots , x_n$ such that $\cdots \prec x_n \prec \cdots \prec x_2 \prec x_1$.
    because minimal ensures the leftmost $\cdots$ can't exist.
  - by [this](https://math.stackexchange.com/a/2792079/1059606)
    > $\forall x(\forall y(y \prec x \to P(y)) \to P(x))$.
    means $\forall x((\forall y(y \prec x \to P(y))) \to P(x))$ which is also implied in chapter 1.
    - Also see 35 ans
  - This has been shown in the book [well_founded_diff_well_ordered]
    so this one is *more general*.
    since $y \prec x=F\Rightarrow (\forall y(y \prec x \to P(y)))=T\Rightarrow P(x)=T$
- [ ] 35
  - The finiteness of "well-founded" means "A has a least element a" same as 9.6 THEOREM 1 proof. Then the rest is same.
    - see the ans
      this is wrong because "least" is implied by total ordering in "WELL-ORDERED" which is not the case for "well-founded".
  - see the ans
    - It use contradiction that 
    - > This means that there is some x2 with $x_2 \prec x_1$ such that $P(x_2)$ is not true
      - Here $x_2 \prec x_1$ must exist due to
        Assume $x_2$ doesn't exist, then $x_1$ is [minimal element "not greater than any other element"][wikipedia_minimal_element] for $\preccurlyeq$, based on 34, it must be true -> contradiction.
      - Then if no $P(x_2)$ is not true.
        Then $P(x_1)$ is true, again contradiction.
- [ ] 37 different from [this](https://math.stackexchange.com/a/3671382/1059606)
  - see the ans
    here it mainly use $R^{-1}$ to construct the *duality of transitivity*.
- [ ] 38
  - reflexive and transitive are trivial
  - antisymmetric
    assume $C\neq D,cRd,dRc\Rightarrow dR^{-1}c,cR^{-1}d\Rightarrow c(R\cap R^{-1})d$
    which is contradiction because C and D are equivalence classes of $R\cap R^{-1}$ 
    (here the exercise $R$ may be wrong), i.e. Let $T=R\cap R^{-1},c \not{T}d$.
  - see the ans
    - the above $d R c$ needs to be proved.
      - Here $d (R\cap R^{-1}) d'\Rightarrow d R d'$
- [x] 39 Here I only proves a,c which is used in 40.
  - a) trivial by definition of glb,lub
  - c) let $x\wedge (x\vee y)=k$
    then $(k\prec x) \wedge (k\prec (x\vee y))$
    then $k$ at most be $x$
    tested by $x$, with lub definition, $x\prec (x\vee y)$.

    the other one is similar.
- [ ] 40
  $x \wedge y=x\Rightarrow x\prec y\Rightarrow ub(x,y)=y\Rightarrow lub(x,y)=y$
  the other side is similar.
  - see the ans which uses some already proved conclusion.
- [ ] 41 see the ans
- [ ] 42
  - By *recursively* calculating glb
    then we will finally get one element $k_1$. Then conversely, $k_1\preccurlyeq x,\forall x\in L$
    Then dual for the other.
  - see the ans
    - The above is similar to induction.
- [ ] 43
  - See [this][not_distributive_lattice]
    > I check if distributive law ...
    - Here ["every pair of elements has a unique supremum ... and a unique infimum"](https://en.wikipedia.org/wiki/Lattice_(order)#)
      1. They are in the same path from 1 to 0
        then the supremum is the ancestor ...
      2. if not in the same path
        then the supremum is 1 ...
    - [complements p20](https://profs.info.uaic.ro/~fliacob/An1/2016-2017/Resurse_2016-2017/R02/Calvin%20Jongsma_Discrete%20Mathematics-%20Chapter%207%20Posets%20Lattices%20&%20Boolean%20Alge.pdf) is done by generalization definition. 
- [ ] 46
  - based on [not_distributive_lattice]
    $b$ has 2 complements
    we add $0\prec c$, then $c$ has no complement.
  - see the ans
    - The above is wrong.
      $lub(c,x)$ may not exist.
    - similar to [this](https://math.stackexchange.com/a/509690/1059606)
      ```
        1
        |
        c
       /|\
      a | |
      | | |
      b d e
       \|/
        0
      ```
- [ ] 48
  - still [not_distributive_lattice]
    we finally $a=a\vee c$ which may not hold.
  - see the ans for the strict proof
- [x] 50
  - This is trivial by the hint.
    Also for the following:
    - > Actually all finite games have a winning strategy for one player or the other;
  - > This is a contradiction, because it is impossible for both players to have a winning strategy
    because it contradicts with the assumption "the first player does not have a winning strategy".
## 10
- For graphs in 10.4-26, 9.4-16, many graphs in 10.6 exercises, we can use opencv to [recognize](https://hub.packtpub.com/opencv-detecting-edges-lines-shapes/) the graph and generate the related matrices and other data structures.
  - Also maybe the schedule table in 8.1-FIGURE 5.
### 10.1
- 4~26 skipped
- [x] 2
  - a) Simple graph
  - b) Multigraph
- [ ] 28
  - It should be "tails" based on 26.
- [ ] 30
  - see the ans
    - based on practicality, no multiple edges.
    - > if there is a train going from u to v *without stopping*

      This assumption is one must otherwise we can construct one *[path_in_order_theory] loop*.
- [ ] 32
  - TODO this is one special simple graph.
- [ ] 35
  - see the ans
    - I missed $S_3\to S_6$ although I included $S_{1,2,5}\to S_6$
- [ ] 36 
  - just add the time to each edge which can be seen as 2-tuple.
  - see the ans for the formal definition
- [ ] 38
  - see the ans we need labels
### 10.2
- 2~18,
  22~24(22 can move $a$ to the side of $e,d$ to better view the *complete* bipartite graph, 24 similar),
  36~40,
  54~66,
  70,74,75
  skipped
- [x] 20
  - $Q_4$ see example 17.
- [ ] 26
  - see the ans
    - $W_1$ is impossible
      Also $C_2$
    - > since we can take one part to be every other vertex
      Assume 2 parts $A,B$. Then one for A one for B alternately for this cycle.
    - d) see the strict proof.
- [ ] 28
  - see the ans
    Notice here we use bipartite complete matching
- [ ] 30
  - > as well as from the men to the women
    compared with 28, here the number of men is bigger than that of women, so not a complete matching, but a maximum matching.
- [ ] 31
  - see the ans
    - > suppose that a man is willing to marry a woman if and only if she is willing to marry him.
      implies
      > with an edge between a man and a woman if they are *willing to marry each other*
    - ~~Here $N(S)\equiv k$ because 2 exactly k~~
    - Here it uses "edges" to connect $N(S),S$
- [ ] 32
  - Is not it just the pigeonhole principle where $2n$ days for $2n$ players we can select distinct player every day.
  - see the ans
    - here should be $2n-1$ days
    - The above doesn't use the assumption (i.e. $N(A)=P$)
      > Every player has exactly one match with every other player
      so if every day only *one same pair* has the match, then it is impossible to select distinct.
- [ ] 33
  - here if all people wants the same prizes, then contradiction.
    - So it seems that $2m$ must be all selected, then it is trivial that all $m$ people select without the overlap.
  - see the ans
    - here we should use the assumption
      > there are 2m prizes that every winner wants,
      where $N(A)=V_2$ is same as 32
- [ ] 34
  1. we show this number can be reached
    - Assume $A$ is the corresponding subset $\max_{A\subseteq V_1} def(A)$
      we can find the complete matching $(V_1-A,V_2-N(A))$
      if not, assume $K\subseteq V_1-A$ has $N(K),|N(K)|<|K|$ 
      (Notice $N(K)\cap N(A)$ can $\neq \varnothing$ which is the worse case than $N(K)\cap N(A)=\varnothing$, so we only think of the better case. Here better case means $|A+K|-|N(A+K)|$ will be *smaller*)
      then assuming $$N(K)\cap N(A)=\varnothing$, 
      we can find $A+K$ which has $|A+K|-|N(A+K)|= (|A|-|N(A)|)+(|K|-N(K))>|A|-|N(A)|$ -> contradiction.
      - so plus $|N(A)|$ we can find one bigger matching which has size 
        $|V_1-A|+|N(A)|=(|V_1|-|A|)+|N(A)|=|V_1|-\max_{A\subseteq V_1} def(A)$
  2. we show this is the maximum. TODO
    If there is one bigger matching $M$.
    based on the 1 process, we can find $A'=V_1^{(M)}-V_1^{(M_c)}$ where 
    $M_c$ corresponds to the complete matching.
    then $|A'|-|N(A')|=(|V_1^{(M)}|-|V_1^{(M_c)}|)$
    - by drawing the graph,
      ```
      V_1: ******************|*************+---
      V_2: ******************|*************+
      ```
      here the vertexes before `+` are $|V_1|-\max_{A\subseteq V_1} def(A)$ in 1
      then $|A'|-|N(A')|=\overbrace{3}^{3\;-}<|A|− |N(A)|(\overbrace{4}^{\text{plus one }+})$
      Then how to get the contradiction?
  - see the ans
    - it splits $V_1$ into 2 parts as the above step 1 to prove the above step 2.
      i.e. for $A$, it can only have $min(|A|,|N(A)|)$ edges in one matching.
    - > Then the condition in Hall’s theorem holds in G′, so G′ has a matching that touches all the vertices of V1
      Here $\forall A_i\in V_1,A_i\neq A\Rightarrow |A_i|-|N(A_i)|\le d$
      Then after
      > adding d new vertices to V2 and joining all of them to all the vertices of V1
      Let $|A_i'|-|N(A_i')|$ be the changed version.
      Then $|A_i'|=|A_i|$ but 
      $|N(A_i')|=|N(A_i)|+d$
      then $|A_i'|-|N(A_i')|\le 0$ so the Hall’s theorem hold.
- [x] 42 see the ans for the graph
- [ ] 44 see the ans
- [ ] 46
  - see the ans
    - here $u\neq w,x\neq v_1$
      so after
      > edges ux and v1w are removed and edges xw and v1u are added
      no loops are generated
      - Also since "edge v1u is not present" and "edge xw is not present"
      - So still simple graph.
- [x] 47
  - only if is same as 46
    we can get the induced graph by removing $v_1$
  - if is just the converse process
  - see the ans~~: the above corresponds to the last sentence in the ans.~~ which mean the same.
- [ ] 48
```python
# d_list=[d_1,...,d_n]
def graphic_sequence(d_list,n):
  # base
  if n==2 and d_1==d_2 and d_1==1:
    return True
  else
    d_list=sort(d_2-1,...,d_n) # this is one pseudo function
    return graphic_sequence(d_list,n-1)
```
  - see the ans
    - add `n< d_1+1` to ensure the existence of `d_2-1,...,d_n`
    - add "deleting all 0’s" to converge earlier.
- [ ] 50,52
```python
# https://math.stackexchange.com/questions/3346882/number-of-sub-graphs-of-a-complete-graph#comment10314589_3353435
import math
def subgraph_of_complete_graph(n):
  sum=0
  for k in range(1,n+1):
      sum+=math.comb(n,k)*2**(math.comb(k,2))
  return sum
print(subgraph_of_complete_graph(2))
print(subgraph_of_complete_graph(3))
print(subgraph_of_complete_graph(4))
```
- [ ] 68
  - see the ans
    - ~~we can also check after each coloring iteration among newly colored ones *and* between newly and already colored. Although this may have more overheads. But it will decrease iteration number somewhat.~~
    - > color all the vertices adjacent to blue vertices red
      > If we ever are in the position of trying to color a vertex with the color *opposite* to the color it *already* has
      each coloring step implies the inherent check.
      So at each step it ensures one subgraph which is one bipartite.
    - > If the process terminates (successfully) before all the vertices have been colore
      has more than one disjoint subgraphs.
- [ ] 72
  - we can also use for $V_1$, $n=n_2$
    similarly $n=n_1$
  - see the ans
    - The above assumes complete graph but it is not always this case.
### 10.3
- 2~26,
  30,34,
  38~40,
  44~46,
  50~54,
  66~68,
  75,76,78($n^2$ pairs more specifically) skipped
- [ ] 28
  - a) see the ans
  - b) 
    > so the number of edges will be a significant fraction of |V |2 ; the graph is dense
    here is only one rough guess.
- [ ] 32
  - see the ans
    - here degree is not same as the sum
- [ ] 36 see the ans for e) which uses the construction method for the n-cube.
- [ ] 37
  - a) each row has $n-1$ ones.
  - b) same as 36
  - c) see the ans: notice the sub-identity matrix.
  - d) TODO maybe should be like [this](https://www.overleaf.com/read/fgwkndckjhrg#2659a9)
- [ ] 42
  - see the ans
    Here although it seems that the degree-4 vertices $u_4,u_2$ on the left is adjacent while on the right the degree-4 vertices $v_5,v_3$ are *not* which have $v_1$ between them.
    But on the right $v_5,v_3$ *are adjacent* based on the edge $v_5 v_3$.

    Or more specifically, move $u_1$ to the right of $u_2 u_4$, we can get the right graph.
- [ ] 48
  - see the ans
    although each consists of degree-5 vertices, they are not isomorphic.
    - left complement: $V_{C_4}=\{\{u_i\vert i=2k,k=1\sim 4\},\{u_i\vert i=2k-1,k=1\sim 4\}\}$
      right just $8\to (8+3)\mod 8=3\to 3+3=6\to 1\to 4\to 7\to 2\to 5\to 8$, so only one cycle
    - > Since the complements are not isomorphic, the graphs are also not isomorphic
      This is because their union is all possible edges which must be isomorphic
      so if one subset is not isomorphic (i.e. different edges), then also for its complement.
      - Same as 50 ans
- [ ] 49
  - since one-to-one correspondence function $f$ is an equiva-lence relation.
  - see the ans
    - the above is a bit wrong
      better say that implies an equiva-lence relation or that $f$ ensures symmetric and transitive
- [x] 56 since $\frac{v(v-1)}{4}\not\in \mathbb{N},v\equiv 2,3\pmod 4$
- [ ] 58
  - See [this](https://math.stackexchange.com/a/1484987/1059606) which is related with [Number of subgraphs in one complete graph](https://math.stackexchange.com/a/472464/1059606)
    [asymptotically](https://mathoverflow.net/a/57478) with "no nice formula".
  - > If there are three edges, then the edges may form a triangle, a star, or a path, giving us 3 possibilities
    To strict prove only 3
    1. 2 vertices chosen: impossible
    2. 3 vertices chosen: $\binom{3}{2}=3$ so only one choice
    3. 4 vertices chosen: here there are 2 vertices duplicate
      so 
      1. adjacent 2 distinct vertices
        by symmetry, arbitrarily choose 2 adjacent distinct vertices, draw the 1st edge between them
        then draw the rest 2 by connecting one of the rest 2 vertices (not duplicately chosen because we need reach 4 vertices) and one of the already chosen (not duplicately chosen because there are only 2 degree-2 vertices).
      2. not adjacent 2 distinct vertices
        it is impossible
        let $v_1$ be the first duplicate vertex
        then 2 edges $v_1 v_2,v_1 v_4$ incident with $v_1$ are chosen
        
        - Then let $v_3$ be the 2nd not adjacent vertex
          But if choosing $v_3 v_{2/4}$ then 
          $v_3$ is not degree-2
          and ~~if $v_3 v_{1}$ then ~~ $v_3 v_{1}$ is excluded by the assumption.
          ~~$v_1$ is degree-3~~.
      3. not distinct vertices
        this is trivial because one vertex is at most degree-3 if only 4 vertices totally.
  - > Since graphs with four, five, or six edges are just complements of graphs with two, one, or no edges (respectively), the number of isomorphism classes must be the same as for these earlier cases
    see 50.
- [ ] 60
  - I tried using the edge category by distance between endpoints, but it may be not easy to proceed then.
  - see the ans
    - It is based on the graph type (i.e. the total isomorphism)
    - > one connected component
      connected means [path](https://www.baeldung.com/cs/graph-connected-components)
      it can have [cycle](https://qr.ae/pKmpiu)
      - > a path of length four, a path of length three with an edge incident to one of the middle vertices on the path, and a star
        let "connect back without isomorphism and duplicate with the former cases" be (*).

        Think of it as starting from "a path of length four"
        then remove one edge and (*)
        and then remove 2 edges from the original and do the same as (*).

        the above removal are all the removal of edges *not splitting* the path.
        TODO why this type of removal will traverse all possible cases.
- [ ] 61 See [this](https://math.stackexchange.com/a/4843160/1059606)
  - If loops are allowed, then [this][2_regular_graph_with_fixed_number_vertices] [connects](https://math.stackexchange.com/a/2742838/1059606) it with the partition of the number.
- [ ] 62
  - a 2-regular graph is cyclic or not?
    [proof](https://math.stackexchange.com/a/917051/1059606)
    - [connected graph](https://mathworld.wolfram.com/ConnectedGraph.html)
    - [this one](https://qr.ae/pKmFeQ) only uses the degree based on k-regular. So it is not better.
  - based on [2_regular_graph_with_fixed_number_vertices],
    we can't have 1 (to exclude loops) and 2 (to exclude parallel edges) in the partition of $7$
    so $7$ or $3+4$.
- [ ] 64
  - If they can be transformed to each other by the **column swap**, i.e. changing the edge order.
    then they are same.
    - See [this][check_isomorphism_by_matrix]
- [ ] 70
  - just map between vertices with the same in-degree and out-degree. See [check_isomorphism_by_matrix] which is also shown in 72 ans.
- [ ] 72
  - see the ans
- [ ] 74
  - compared with 58,
    a) $2+1$ due to direction
  - see the ans
    - based on TABLE 1 on p676, the ans assumes Directed *multigraph* instead of the Simple directed graph.
    - The [book](https://users.metu.edu.tr/aldoks/341/Book%201%20(Harary).pdf) just enumerates these simple graphs in p236.
    - digraph defaults to be [simple](https://doc.sagemath.org/html/en/reference/graphs/sage/graphs/digraph.html#methods)
  - See [this](https://math.stackexchange.com/a/354183/1059606) where this corresponds to the above book.
    > If I was pressed to find these numbers, I'd get my *computer* to find them by:
  - TODO counting method [1](https://math.stackexchange.com/a/3852701/1059606) and [2](https://math.stackexchange.com/questions/354062/how-many-nonisomorphic-directed-simple-graphs-are-there-with-n-vertices-when#comment10316336_3051861)
- [ ] 78
### 10.4
- 2~12,16,34,42,43,
  56~58,
  60,62, skipped
- [x] 4
  - there are 2 big paths
- [ ] 14
  - we exclude all vertices whose in-degree or out-degree are 0.
    so a) $a\to e\to b$
    b) we firstly exclude $f$ and edges incident with $f$
      then $a$ becomes out-degree 0, so remove $a$
      then $b$
      so only one triangle is left.
    c) after removing $e$
      there are ~~3~~ 2 $C_4$ connected by $bc,gh$,
      so $2+\overbrace{1}^{\text{2 cycles connected by bc,gh}}$
      ~~so $\sum_{i=1}^3 \binom{3}{i}$ choices.~~
  - see the ans
    - here the single-vertex connected component should be considered.
    - > The collection of strongly connected components forms a partition of the set of vertices of G
      - for c) the 2 small cycles can be connected, so they are *not component*
        so only 1
      - [partition](https://en.wikipedia.org/wiki/Strongly_connected_component#Definitions):
        1. since single vertex are included, so no empty
        2. cover $V(G)$ same as 1.
        3. disjoint because otherwise they can connected, so merged into one. <a name="connected_component_partition"></a>
        - This is [same](https://en.wikipedia.org/wiki/Component_(graph_theory)) as the proof for 
          > The components of any graph partition its vertices into disjoint sets
- [ ] 17
  - see the [above](#connected_component_partition)
- [ ] 18 see the ans
- [ ] 20
  - see the ans
    - it uses subgraph,
      we can also use the path based on the whole graph
      $u_1\to u_4\to u_3\to u_2\to u_6\to u_5\to u_8\to u_7$ (with degree sequence $32233322$)
      But for the right, either $323\ldots$ or $332\ldots$ are possible.
- [ ] 22
  - see the ans
    - > $u_1\leftrightarrow v_2$ and $u_8\leftrightarrow v_6$
      due to symmetry
    - > $u_2\leftrightarrow v_1$ and $u_3\leftrightarrow v_3$
      this is due to $v_3,v_1$ are symmetric.
    - > $u_5\leftrightarrow v_8$
      is due to $(u_5,u_2,u_4)\leftrightarrow (v_8,v_1,v_4)$ here 
      $v_8$ are the only vertex adjacent to both $v_1,v_4$ except for $v_3$
    - > $u_6\leftrightarrow v_7$
      $(u_8,u_5)\leftrightarrow (v_6,v_8)$
      same as the last point, only $v_7$ is possible.
- [x] 24
  - > Adjacent vertices are in different parts, so every path between them must have odd length. Therefore there are no paths of length 2
    because each edge will bring the point to *the other part*.
  - see the [code][counting_path]
- [x] 26 see [counting_path]
- [ ] 28 <a name="minimum_edge_number_connected_graph"></a>
  - Also [see](https://www.quora.com/How-do-I-prove-that-the-minimum-number-of-edges-in-a-connected-graph-with-n-vertices-is-n-1/answer/Abhijith-N-Raj-1?comment_id=385204198&comment_type=2)
    - Also see [this](https://qr.ae/pKdkCa) which seems to not shown when first reading [this](https://qr.ae/pKdkgK).
  - The book one is similar to [this](https://math.stackexchange.com/a/237136/1059606) where "smallest possible number" corresponds to here "a connected graph with n + 1 vertices and fewer than n edges" (This is shown in the note).
    - [This](https://math.stackexchange.com/questions/237134/prove-by-induction-that-every-connected-undirected-graph-with-n-vertices-has-at#comment525143_237136) shows the book [explicit counterexample](https://math.stackexchange.com/questions/237134/prove-by-induction-that-every-connected-undirected-graph-with-n-vertices-has-at#comment525194_237136) is not one must.
  - [general](https://math.stackexchange.com/a/457104/1059606)
    - > so G has at least v−(e−1)−1=v−e components as was to be shown.
      Think of the worst case,
      here adding one edge at most combines 2 components,
      so the minimum is one less.
      - > at most one component more than
        > so $G$ has at least $v-(e-1)-1=v-e$ components as was to be shown
        here "at least" corresponds to the worst where 2 components are combined into 1 by $ab$.
      Also [see](https://math.stackexchange.com/questions/457042/prove-that-a-connected-graph-with-n-vertices-has-at-least-n-1-edges#comment9596258_457104)
- [ ] 30
  - see the ans
    - here obviously $V(H)\ge 2$
    - The key idea is to use the connected component.
- [ ] 32
  - 2 $K_3$ connected with $cd$
    so $cd$
  - see the ans
    - here is asking the cut vertices.
      so $c,d$
- [ ] 35
  - "cut vertex" -> "not pendant"
    if "pendent", then it can't be one cut vertex -> contradiction.
    - Also proved by "pendant" -> "not cut vertex"
  - "not pendant" -> "cut vertex"
    since removing one edge $e$ incident with $v$ can disconnect leading to $v$ not isolated 
    then removing all edges also disconnect.
  - see the ans
    - > If an endpoint of a cut edge is not pendant, the connected component it is in after the removal of the cut edge *contains more than just this vertex*
      So removing $v$ will at least leave some isolated vertices which is one connected component after disconnection.
- [x] 36
  - "if" is trivial because $u,v$ are disconnected
  - "only if" is similar
    because "cut vertex" implies $\exists u,v$ where $u,v$ are disconnected.
    Then "every path between u and v passes through c"
- [ ] 37
  - The key idea is
    > Either s or t (or both) is a cut vertex
    which excludes both $s,t$ are not cut vertices.
    - Then 
      > Let w belong to the connected component that does *not contain t of the graph*
      implies
      > every path from w to t contains s,
      which causes contradiction
      - So the above means
        $s,t$ must be not cut vertices when $d(s,t)$ is maximum.
- [ ] 38
  - "only if" is trivial by proving "imple circuit" -> "not cut edge"
    because $u,v$ is still connected due to the circuit.
  - "if"
    then adjacent $u,v$ has only one path which is their incident edge,
    so disconnected.
  - see the ans
    which all uses cut edge as the condition which is different from the above.
    - it considers
      > Thus e appears twice in the circuit, so the circuit is *not simple*
      ~~i.e. $u,v$ multiedge is considered as one circuit.~~
      maybe [$u-v-k-u-v$](https://math.stackexchange.com/questions/4354945/non-simple-circuit#comment9091250_4354945)
- [ ] 40
  - 7: $d/b$ because one $C_3$ -> $bcd$
  - 8: $d$ (isolated) with one other due to $C_3$
  - 9: $e$ and one other same as 8
- [ ] 44 see the ans
  - > Since there are only a *finite number of possibilities* for the distribution of the ni’s , the arrangement we give must in fact yield the maximum
    TODO how to get this relation?
    Isn't "maximum" because $(a+ 1)^2 + (b−1)^2 −a^2 −b^2 = 2(a−b) + 2 \ge 2$?
  - Here should be $\frac{(\sum(n_i^2))-n}{2}$
- [ ] 45
  - To make $K_n$ disconnected,
    it has at most $\binom{n}{2}-(n-1)=\frac{(n-1)(n-2)}{2}$
    - so if more than $\binom{n}{2}-(n-1)=\frac{(n-1)(n-2)}{2}$, then to make it disconnected, all deleted edges are incident to the same vertex, But based on the above, it can't disconnect.
  - see the ans
    - The above is wrong because it can't ensure 2 components with one component being isolated must be the largest.
    - based on 44
      to have more edges based on the fixed number of vertices, we have *only one* component.
      so
      > The most edges G could have is C(k, 2) + C(n - k, 2)
- [x] 46
  - all entries beside the diagonal blocks are zeroes.
  - see the ans
    - ~~more specifically, diagonal "ones" blocks~~
- [ ] 48
  - c) This is $K_{m-1,n}$ or $K_{m,n-1}$
  - d) can be also based on symmetry
    so we only need to care about one specific vertex
- [ ] 50 
  - a) $\kappa(G)=1(b),\lambda(G)=2(\text{due to 2 }C_3)$
  - b) $\kappa(G)=1(c),\lambda(G)=3(\text{due to 2 }K_4)$
  - c) Here by symmetry, only check $b,e,f$ where all can't disconnect.
    - see the ans
  - d) by symmetry
    - removing one of $a,b,c$ can't disconnect
    - removing $a$, then by symmetry one of $b,d,e$ still can't disconnect
    - removing 3 vertices
      by symmetry when $a,b$ chosen, any one of the rest still can't disconnect (only check whether the rest have one path or others to connect them without drawing the graph after edges are removed)
    - $b,c,d,f$ will isolate $a$ hinted by $\min_{v\in V}\deg(v)$
- [ ] 51
  - "only if" is trivial.
  - see the ans
    - Here disconnect means [at least 2 vertices](https://mathworld.wolfram.com/DisconnectedGraph.html#:~:text=A%20graph%20is%20said%20to,has%20those%20nodes%20as%20endpoints.)
    - 
- [ ] 52
  - a) "if" is trivial.
    - "only if" by exercise 51, this means "it is *impossible* to remove vertices to disconnect G"
  - b) "if" is trivial 
    because think of the easiest way, to be splitted into 2 components with $V_1,V_2$ vertices, we at least need to remove $|V_1|\cdot |V_2|$ which has the minimum 
    $n-1$.
  - see the ans
    - > According to the discussion following Example 7
      i.e. VERTEX CONNECTIVITY discussion in p718
    - b) "only if" can be got from $\min_{v\in V}\deg(v)\ge n-1\Rightarrow K_n$.
- [x] 53 used by 10-supplementary-46
  - similar to $K_n$ to disconnect one vertex, we need $\min\deg v$, this is $\lambda(G)$
  - Also vertex connectivity needs to remove one subset of the two.
- [ ] 54
  - see the ans
- [ ] 55
  - see the ans and [comparison_edge_connectivity_vertex_connectivity]
  - obviously "a smallest edge cut" will construct 2 connected components
    if more than 2, then some edges can be not removed to construct only 2 connected components leading to the contradiction with "smallest".
- [ ] 59
  - see the ans
    - "do not contain the same set of edges" doesn't say "every edge is different"
    - > Otherwise we can suppose that x0 = y0, x1 = y1, ..., xi = yi , but $x_{i+1} \neq y_{i+1}$.
      This means
      > $x_0x_1=y_0y_1,x_1x_2=y_1y_2,\ldots,\text{but }x_{i}x_{i+1}\neq y_{i}y_{i+1}$
    - > since no edge among the xks or the yl s can be repeated (P1 and P2 are simple by hypothesis) and no edge among the xks can equal one of the edges yl that we used, since we abandoned P2 for P1 as soon as we hit P1
      firstly along the common path, then unique for $P_2$ and then unique for $P_1$.
    - > If they diverge only after one of them has ended, then the rest of the other path is a simple circuit from v to v
      notice this is based on DMIA path definition which is different from mcs. DMIA path is similar to the general walk.
      Simlarly "circuit" is closed walk in mcs.
    - > we follow it along— forwards or backwards, as necessary—to return to x
      "forwards" may occur, e.g. 2 paths can be $a-b-c-d$ and $a-b-c-e-f-b-g-h-d$ although one has duplicate vertices.
      ```
           g--------h
           |        |
      a----b----c---d
           |    |
           |    |
           f----e
      ```
    - > no edge among the xks can equal one of the edges yl that we used, since we abandoned P2 for P1 as soon as we hit P1.
      More specifically, no duplicate vertex $v\in P_{1,2}$ except for their cross $x_i,x_m$ where "forwards" occur when $m<i$ and "backwards" occur when $m>i$. Then no duplicate edge.
- [x] 61
  - This is same as [graph_link_with_relation]
- [ ] 63
  - "only if" is same as 24.
  - "if"
    for "circuits with an even number of edges", we can label *alternatively* vertices along the circuit into 2 parts, so bipartite.
    for vertices with no circuits. Since here allows multiedges, this means these vertices are isolated. Then we can arbitrarily put these vertices into either part.
  - see the ans
    - The above doesn't show explicit methods of which label to start.
      Although it is similar to
      > Let v be a vertex of the graph, and let A be the set of all vertices to which there is a path of *odd* length starting at v, and let B be the set of all vertices to which there is a path of *even* length starting at v
- [ ] 64
  - see the ans
    - b) is largely "restricted" to exclude multiedges and *duplicate* moves.
    - e) 1,3,4,7th edge use the toll.
- [ ] 65 see the ans
  - If using the same method like 64
    This may be one huge graph
    because
    1. Here *anyone* can be on the boat instead of the necessity to have the "farmer"
    2. the boat doesn't need to be with the farmer
      so $(H_1W_1H_2W_2<b>,\varnothing)\to (H_2W_2,H_1W_1<b>)\to (H_1H_2W_2<b>,W_1)$
      or $(H_1W_1H_2W_2<b>,\varnothing)\to (H_1H_2W_2,W_1<b>)$
    3. Here the *tree* is better to get the shortest path. Also see the following *uni link* where obviously it doesn't show the whole tree.
  - The following doesn't have many relations with the graph theory.
    - The [wikipedia](https://en.wikipedia.org/wiki/Missionaries_and_cannibals_problem#The_problem) uses 3 couples 
      > there cannot be both women and men present on a bank with *women outnumbering men*
      But it only ensures
      > any solution to the jealous husbands problem will also *become a solution to the missionaries* and cannibals problem
      but not vice versa
      because when equal number of women and men, $H_1H_2W_2W_3$ will also contradict with the requirements. This is also shown in 
      > In this case we may neglect the *individual identities* of the missionaries and cannibals
      and
      > they *cannot be outnumbered* by cannibals (if they were, the cannibals would eat the missionaries)
      - Notice the possible restriction
        > *only one man can get out* of the boat at a time
        and
        > If a woman in the boat at the shore (but not on the shore) counts as being by herself
      - I skipped the reference [4](./papers/From_China_to_Paris_Jealous_Husbands.pdf) (only give one solution without the explanation) and [5](https://sci-hub.se/https://doi.org/10.1145/144052.144106) (not using graph theory)
    - [geeksforgeeks](https://www.geeksforgeeks.org/puzzle-couples-crossing-river/) doesn't show how to think of this problem detailedly.
    - [This](https://aperiodical.com/2016/11/a-more-equitable-statement-of-the-jealous-husbands-puzzle/) only shows related problems but doesn't give one solution, similar to [this](https://www.math.utoronto.ca/barbeau/puzzles.pdf)
    - [This](https://sci-hub.se/https://doi.org/10.2307/3619658) has *islands*, not same as this exercise.
  - [This uni link](https://www.cs.uni.edu/~wallingf/teaching/cs3530/sessions/session23.html) one give one generalization for $n$-couple based on the *recursive* algorithm
    This seems to *not ensure the shortest*.
- [ ] 66 see the ans
### 10.5
- 2,6~10,14,17(similar to theorem 2),
  20~26,
  32~42(40 similar to EXAMPLE 5 $G_3$),50,
  54~58,
  60, skipped
- [ ] 4
  - use one cycle $fbcef$
    and then $faebad(c-f)$ where the last 
    $cf$ is added to form all even degrees.
- [ ] 12
  - By [unique_start_euler_path]
    > To find the Euler path (not a cycle), let's do this: if  $V1$  and  $V2$  are two vertices of odd degree, then just add an edge  $(V1, V2)$ , in the resulting graph we find the Euler cycle (it will obviously exist), and then remove the "fictitious" edge  $(V1, V2)$  from the answer.
    We just 
    ```python
    add (V1, V2)
    while H has edges
    ...
    remove (V1, V2)
    ```
  - see the ans
    - We need to check `if not (all even degree):` before `add` and `remove`
      and in this case "an arbitrarily chosen vertex" should be "odd-degree vertex in the original graph"
    - TODO 
      > Thereafter we follow Algorithm 1 *exactly*
      may be wrong.
      Also see [find_euler_path_based_on_circuit] and exercise 17.
- [ ] 16
  - "only if"
    "weakly connected" is trivial
    "in-degree and out-degree of each vertex are equal" same as the proof for Multigraph.
  - "if" same as the proof for Multigraph.
- [ ] 18
  similar to the Multigraph exercise
  we use the cycles first $abdca,cdbc$. By splicing them, we get $abd(cdbc)a$ (here $()$ means splicing)
  then append the $ad$, finished.
- [ ] 28
  - see the ans notice $K_{1,1}$
- [ ] 30
  - See [cut_vertex_Hamilton_circuit]
- [ ] 41 see the ans
  - > It is not hard to see that if there is to be a Hamilton path, exactly one of the inside corner vertices must be an end, and that this is impossible
    Obviously one end vertex needs to be at the outside cycle, otherwise the circuit will omit all other vertices similar to 34.
    Similarly one end is at the inside cycle.
    To connect these 2 almost-cycles, the edge like $bj$ needs to be included.
    
    More specifically, the process is as the following:
    1. By symmetry, choose $c$ as the end vertex.
      and by symmetry, choose $bc$ to be omitted,
      then $ch$ must be included
    2. The rest 3 vertices at the outside add 6 edges which constructs 1 almost-cycle with $ch$.
    3. Here after $chgfedab$, we must choose $bj$ because $bc$ already excluded.
    4. Here 
      - choose $jp$, by symmetry of the inside cycle, we choose $pq$
        then $k,l$ *can't be included both*.
      - by symmetry, choose $ji$ and then $jk$ exclusion means $k$ is the other end vertex.
        So similar to the point 3, we got to $k$ at the end *without including $p$*
- [x] 44
  - a~c) obviously by the cycle
- [ ] 46 see the ans
  - > By symmetry, it makes no difference which vertex we delete, so assume that it is vertex j.
    It should be "makes no difference which vertex" of the outside/inside cycle
    - Then for the outside, assume that $e$ is removed.
      $(gbaf)(idch)(j)g$ where the last $g$ is to go back to the start and $()$ is to mark the related group.
  - The 1st premature circuit is got from 4 degree-2 vertices.
    - The 2nd is similar from 3 degree-2 vertices $j,b,c$.
- [ ] 48 see the ans
- [x] 49
  - by removing the correspond 2 edges of $Q_n$
    the add 2 edges connecting the corresponding 2 vertices from each $Q_n$
    Then the circuit for $Q_{n+1}$ is constructed.
  - see the ans
    - The above added 2 edges correspond to $0_{c_k}\to 1_{c_k},1_{c_1}\to 0_{c_1}$ in the ans.
- [ ] 52
  - Since the subgraph is always connected,
    so if it can recursively go back to the start vertex,
    then the circuit is formed.
  - see the ans
    Here [Fleury_Algorithm_proof] is the most detailed, so the other 2 can be skipped if understanding this one.
    - the [book][Graph_Theory_with_Applications]
      - > the terminus Vn must be of degree zero in Gn • It follows that Vn = Vo
        - "must be of degree zero" because no edges are left to choose from.
        - since $\deg(v_0)=2k,k\in\mathbb{N^+}$
          so if $v_n\neq v_0$ then in $G_n$, $\deg(v_0)=2m-1,m<k\Rightarrow \deg(v_0)\neq 0$
      - > Let m be the *largest* integer such that $v_m \in S$ and $v_{m+1} \in \overline{S}$. Since Wn terminates in $S$
        here the "largest" means $\not\exists v_k \in S,k\ge m$ based on "terminate" in $S$ (otherwise $v_k$ should be the *largest*)
      - > unless there is no alternative, $e_{i+1}$ is not a cut edge of
        notice here $e_{i+1}$ can be the cut edge
        for example, in the $C_3$, the 2nd and the 3rd must disconnect one vertex each.
      - > e must also b.e a cut edge of G m
        because otherwise $e_m$ will not be chosen.
      - by p17 $G_m[S]$ means the *induced* subgraph.
      - > em+l is the only edge of [S, 5] in Gm
        because $\deg(v_i)=0,i\ge m+1$ when $G_n$
        so none of them are connected to $v_m$.
      - > hence of Gm[S]
        ~~TODO here should be because the endpoints of $e$ are both "positive degree in $G_n$".~~
        Here means "a cut edge" of the induced subgraph if "a cut edge" of the whole graph
      - > every vertex in Gm[S] is of even degree.
        Here it is also saying about $G_n[S]$.
        Then $G_n[S]$ is just 
        $G-\{e_{1\sim n}\}$ which obviously have all *even*-degree vertices because $G$ is *even* and the closed trail removes *2* degrees from each point passed.
        - > An even graph has no cut edge
          See [this][even_graph_no_cut_edge]
      - In summary, it proves
        1. closed trail -> circuit. (Similar to the proof of the euler circuit in the Rosen book)
        2. no "positive degrees in $G_n$", so traverse all edges.
    - I also found one [proof][Fleury_Algorithm_proof] which is same as the above because the book is written by the same pair of people.
      - I first read the [textbook][graph_theory_graduate_textbook] p96
        - by p69 ~~$\partial(X)$ means edge cut which will disconnect the graph.~~
          ~~so $\partial(X)\neq \varnothing$ means connected.~~
          > An edge cut $\partial(v)$ associated with a single vertex v is a trivial edge cut; this is simply the set of *all links incident* with v. If there are no loops incident with v, it follows that $|\partial(v)| = d(v)$
          This means *degree* if $X$ is one "single vertex".
        - by p59 here $F[X]$ is same as [Graph_Theory_with_Applications]
        - Although even graph has [multiple](https://math.stackexchange.com/questions/2907258/graph-theory-properties-of-even-graph#comment6008657_2907258) definitions
          by p66 it defines
          > A graph in which each vertex has even degree is called an even raph
        - Theorem 2.10 is more general than [even_graph_no_cut_edge]
      - [Fleury_Algorithm_proof]
        1. proves trail
        2. closed trail
        3. contradiction to prove "includes all edges".
        - Here $c(F)$ means "The number of components" by [graph_theory_graduate_textbook] 40
        - > graph F must have included edge e and edge e must be a cut edge of F
          here $F$ should not be the terminated graph because it includes $e$ and $y\notin X$
          > Let X be the set of vertices of *positive* degree in subgraph F at the stage when the algorithm terminates.
        - The key of 3
          > But this violates the algorithm since it will *not add cut edge e* to W since *non-cut edge e'* is available for inclusion in W
          where "cut edge e" is due to "$\partial_F(X)=\varnothing$"
          and "non-cut edge" ~~is due to $e$ is chosen as the last, so after $e$ is removed, all the rest is not cut-edge.~~ is due to "not a cut edge of $F \setminus e$", so also not one for one bigger [parent graph](https://docs.dgl.ai/en/0.2.x/generated/dgl.subgraph.DGLSubGraph.parent_nid.html) $G$.
- [ ] 59
  - TODO re-check after drawing the graph.
- [ ] 61
  - see the ans
    - > Without loss of generality, assume the path starts 1–10, 10–16, 16–7.
      Here only one edge of 4 based on "a pair of diagonally opposite corners" can be removed [because](https://python.plainenglish.io/where-chess-programming-and-math-meet-the-knights-tour-aac623abda09)
      > Since there are *two pairs* of these, the path must start at a corner square and end at an adjacent corner square.
      - > This movement needs the help of one of the two remaining middle squares
        <!-- $$
        \begin{aligned}
        &&1&&2&&3&&4\\
        &&5&&6&&7&&8\\
        &&9&&10&&11&&12\\
        &&13&&14&&15&&16\\
        \end{aligned}
        $$ -->
        ~~Assume the above labeling~~
        ~~then assume $1\to 10\to 16\to 7$~~
        Because if not using, then the circuit will be generated like $2-8-15-9-2$.
    - TODO ["4xm" case][4xm_knight_tour]
    - The main process can be seen [here][chapter_10_5_tex_code]
- [ ] 62
  - similar to [4xm_knight_tour], we can color so that bipartite.
  - see the ans which gives one strict proof
- [ ] 64
  - By the [code](./miscs_snippets/py_codes/10_5_64/8x8_knight_tour.ipynb)
    the `14` is wrong because
```bash
$ python -m pdb 8x8_knight_tour.py
<function save_history at 0x7f433b5814e0>
> /home/czg_arch/Discrete_Mathematics_and_Algorithm/Discrete_Mathematics_and_Its_Applications/miscs_snippets/py_codes/10_5_64/8x8_knight_tour.py(1)<module>()
-> import matplotlib.pyplot as plt
(Pdb) break 122
Breakpoint 1 at /home/czg_arch/Discrete_Mathematics_and_Algorithm/Discrete_Mathematics_and_Its_Applications/miscs_snippets/py_codes/10_5_64/8x8_knight_tour.py:122
(Pdb) c
> /home/czg_arch/Discrete_Mathematics_and_Algorithm/Discrete_Mathematics_and_Its_Applications/miscs_snippets/py_codes/10_5_64/8x8_knight_tour.py(122)<module>()
-> for edge in hamilton_circuit.edges:
(Pdb) p degree(index(3,dim_2-3,dim_1)-1,adj_mat,hamilton_circuit)
6
(Pdb) candidate_list(adj_mat,index(3,dim_2-3,dim_1)-1,hamilton_circuit)
[26, 28, 33, 37, 49, 53]
(Pdb) p degree(index(0,dim_2-2,dim_1)-1,adj_mat,hamilton_circuit)
2
(Pdb) candidate_list(adj_mat,index(0,dim_2-2,dim_1)-1,hamilton_circuit)
[33, 42]
```
  - Also see [chapter_10_5_tex_code]
- [ ] 65
  - a) maybe just $K_n$?
  - d) is trivial
  - e,f) see the ans
  - see the ans
    - a)
      - > we have obtained a (necessarily noncomplete) graph H
        We can start from one vertex $v$ which $\deg(v)<n-2$, then even at the last step $v$ is added with one edge, we still have $\deg(v)<n-1$, so not complete.
        - If none of $v$ has $\deg(v)<n-2$, then by Ore’s the-orem, it has one Hamilton circuit.
      - "adding missing edges" implies we can *reach all* vertices so that "a Hamilton path" and then one Hamilton circuit.
    - c) see the ans 
      here it uses the assumption.
    - In summary
      the key idea is c) which *uses the condition* and e).
    - Here the state $H$ is just the *last step* before $G$ can have a Hamilton circuit.
      Then it shows $H$ must *already have one Hamilton circuit* which is transformed from one Hamilton path.
- [ ] 66
  - only if is trivial
  - see the ans
    - > Then parts (c)–(f) of Exercise 65, with v1 = u and vn = v, show that G has a Hamilton circuit
      here c) is trivial
      d) is based on "nonadjacent vertices"
      e) is based on c).
      f) is based on e).
- [ ] 67
  - see the ans
    - > if either both bc and cd were in H, or both gh and hi were in H
      it should be "both bc and hi" and "both gh and cd"
    - > Because of the 120◦ rotational symmetry of the figure, it then follows that dl and gk are in H as well.
      because otherwise it will become the case "$aj\not\in H$".
    - > It is clearly now impossible to include all three of the vertices i, j, and k in the Hamilton circuit
      - It should be "j,k and l"
      - because if existing, ~~then we can start from $j$ WLOG,~~
        ~~then there is no way to go back to $j$.~~
        then $jk,kl,lj$ can be only chosen one.
        then one vertex of $j,k,l$ will have only one edge incident, so no circuit.
- [ ] 68
  - because remove 3 edges at one time (i.e. $C_3$)
    then $C\cdot\lceil\frac{n}{3}\rceil$ where $\lceil\frac{n}{3}\rceil$ is the loop count.
  - see the ans
    - It has more granularity
      - > All this takes O(m) time
        means the time for the "subcircuit"
        because at most removing $m$ edges.
        - This have done all before the 1st iteration of "while H has edges" which finds the 1st circuit.
        - TODO this may be wrong
          because the time will be less when most of edges are removed.
      - > For the while loop, finding a vertex at which to begin the subcircuit can be done in O(1) time by consulting the queue,
        i.e. check the adjacency list related with the vertices in the last `circuit`
        the 1st non-empty vertex is the begin vertex.
        - more specifically, $O(len(V(circuit)))$
      - > Furthermore, finding all the subcircuits takes at most O(m) time in total, because each edge is used only once in the entire process
        ~~TODO this may be wrong~~
        ~~because based on no loops in Multigraph, the above shows $\lceil\frac{m}{3}\rceil$ iterations, then multiplying by $O(m)$ in each step, we get ~~
        ~~$O(m^2)$~~
        - Maybe removing one edge uses $O(1)$ time because it is just checking one adjacency list of one vertex.
          then removing $m$ edges uses $O(m)$
          - This is implied by
            > because each edge is used only once in the entire process
### 10.6
- 8~14,18,23,26, skipped
- [ ] 2~6,16
  - see the [code](./miscs_snippets/py_codes/10_6_Dijkstra/Dijkstra.py)
- [ ] 19 see the ans
- [ ] 20 
  - Here it allows duplicate passes of one same vertex.
    Because it considers longest so not necessary to remove the loop.
    - But based on "simple", it should not allow revisit of the same vertex, so "Bellman-Ford" also [doesn't function](https://stackoverflow.com/a/63571123/21294350) (Here also fail due to the negative cycle).
      Then it can be [reduced from the Hamiltonian Path problem][longest_simple_path_NP_hard] which takes only [part of all vertices](https://cs.stackexchange.com/a/10734/161388). <a name="Hamiltonian_Path_NP_hard"></a>
      - Then since NP-hard has [no efficient algorithm](https://cs.stackexchange.com/a/139832/161388), so I skip it.
    - Floyd Warshall Algorithm which is just the Warshall’s Algorithm also doesn't function due to maybe not *simple*.
      - But if we think of the street cleaning as the 19 ans says, then allowing "duplicate passes of one same vertex" is reasonable.
      - Still the [negative cycles](https://stackoverflow.com/a/53436752/21294350) when negated make this method fail.
        for example with the targets $u\to w$
        at some iteration to add $a$, we update with $u\to a\to w$, $u\to a\to b$ and $b\to a\to w$ because we want the *longest*.
        then if $b$ after some time, then maybe $(u\to a\to )b( \to a\to w)$ which is longer.
        (Notice the above is impossible for shortest because $u\to a\to w$ is shorter.)
  - Here "Dijkstra’s Algorithm to find the longest" by using negative version is [impossible](https://stackoverflow.com/questions/8027180/dijkstra-for-longest-path-in-a-dag#comment137189941_73817049)
    Since it [doesn't have one optimal substructure](https://stackoverflow.com/a/40843559/21294350) which can be also seen the proof of (i) in p748 where "There is a path with length less than Lk(v) from a to u containing only vertices of S." *won't hold* because minus negative will be bigger instead of less (Also [see](https://stackoverflow.com/a/13159425/21294350) and [this](https://stackoverflow.com/a/22891500/21294350) which also compares with Floyd Warshall where "not negative weight cycles").
    - But if its *original* weights are negative,
      then we [can use the positive version](https://stackoverflow.com/questions/8027180/dijkstra-for-longest-path-in-a-dag#comment105193455_40843559) and use the Dijkstra’s Algorithm to calculate the shortest when positive which is just the longest when negative
    - As the above shows, [Bellman-Ford](https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/#) which has code implementation considers the negative weight condition.
      - $N-1$ because one path without the **revisit** "with N vertices can have at most N-1 edges".
      - > It is important to note that during the N-1 relaxations, we presumed that each vertex is traversed only once. However, the reduction of distance during the N’th relaxation indicates revisiting a vertex.
        notice here maybe more than one loop (i.e. more than one vertices revisited)
        But $N$ ensures at least one vertex is revisited.
      - If allowing the negative cycle,
        since this may occur at any iteration, so it will go to infinite negative.
        To avoid it, we need to remove visited edges. But the visited edges are different for different path, so we need to think *separately about each path*. So it is similar to brute force.
  - In summary, "Bellman-Ford" and "Floyd Warshall" can't be used here due to the negative cycle.
    And "Dijkstra’s" can't be used due to "not optimal substructure".
- [x] 22
  - based on induction at the $i$th step
    all distance are based on with interior vertices $v_{1\sim i}$ which either including 
    $v_i$ or not.
    - The above is just FIGURE 4 in p636.
- [ ] 24 see the above "optimal substructure".
- [ ] 28
  - > since each edge appears in six paths (and sure enough, 17,580 = 6 ·2930 )
    This is just the conditions where when we select $S$ fixed,
    then WLOG assume another $N$ is adjacent, then either $SNxxx$ ($SxxxN$ excluded due to already $/2$ by reversing the order). So $3!=6$
- [ ] 30
  - > equal to the minimum total weight of a path from u to v
    this just constructs one equivalence relation as Floyd-Warshall Algorithm does.
  - > It is now clear that finding the circuit of minimum total weight in G′ that visits each vertex exactly once is equivalent to finding the circuit of minimum total weight in G that visits each vertex at least once
    assume there is one circuit $v_1,\ldots,v_i,v_{i_1},v_{i_2},\ldots,v_{i_k},v_{i+1},\ldots,v_n$ in G where $i_{1\sim k}\in \{v_{1\sim i}\}$, then 
    $v_i,v_{i_1},v_{i_2},\ldots,v_{i_k},v_{i+1}$ must be shortest between $v_i,v_{i+1}$, otherwise contradiction with "*minimum* total weight".
    Then all paths visiting duplicate vertices which has been visited so far like $v_i,v_{i_1},v_{i_2},\ldots,v_{i_k},v_{i+1}$ can be combined into 
    $v_{i},v_{i+1}$ by $G'$.
- [ ] 31
  - > with no simple circuits
    Then isn't it [longest_simple_path_NP_hard]?
  - see the ans
    - Here "in a weighted directed graph with no simple circuits" means " directed *acyclic* graph"
    - DAG must have one Topological sorting
      [proof][DAG_to_topological_ordering_proof]
      - "not have any incoming edges" imply "minimal" in mcs
      - > there is some vertex that does not have any incoming edges
        if all have, then we can start from arbitrary vertex and back to its incoming vertex
        then since with the finite vertices, it will must back to one vertex which has been visited before.
        Then leading to the circuit which is contradiction.
      - notice here maybe more than 1 "vertices that does not have any incoming edges".
    - The ans is same as this [one](https://www.geeksforgeeks.org/find-longest-path-directed-acyclic-graph/#) where `dist[u]` must be the maximum when it is visited at the outside loop because it has *traversed all* edges to $u$.
      except:
      1. Here it mainly targets backwards by `P( j) + w( j, i)` over all j < i.
      2. Use `C(i)` to track the path.
    - the ans
      - > `P(i) = 0` if there are no such values of j.
        is the initial step.
      - The key is
        1. > let P(i) be the maximum of P( j) + w( j, i)
          traverse all possibilities to choose the best.
        2. it has [optimal substructure](https://blogs.asarkar.com/assets/docs/algorithms-curated/Longest%20Path%20in%20a%20DAG%20-%20Khan.pdf) where [Relax](https://www.baeldung.com/cs/dijkstra-edge-relaxation) means update the distance.
          This is because by the *ordering* we can just split the path into subpath and combine them. This is *intuitive*.
### 10.7
- 2~6,11,
  12~14,16,
  22~26,34,35(these 2 similar to 32,33) skipped
- [ ] 8 see the ans
- [x] 10
  - obviously, $v_3$ then can be only at the bottom-right of $v_2$ or at the top-left of $v_1$.
    then by symmetry, choose the bottom-right of $v_2$
    then $R_1$ is splitted into $R_{11}$ which is inside 
    $v_{4253}$ and $R_{12}$ otherwise.

    Then we have the map $\{R_2:v_3,R_{11}:v_1,R_{12}:v_2\}$ where 
    if $v_6$ is in $R_2$, then $v_6,v_3$ will cross, and the others are similar.
- [ ] 15 just algebraic calculation.
  - see the ans
- [ ] 17
  - ~~> the degree of the unbounded region is at least 4~~
    ~~This is based on $v \ge 3$~~
    ~~See [connected_planar_simple_graph] where $k$ edges in the unbounded region is degree $2k$.~~
  - see the ans
    - The above is wrong because maybe $C_5$ which has degree 5.
    - COROLLARY 1
      - here *at least 2 edges* because one edge at most connects 2 vertices.
        Then one edge contributes 1 (in one cycle) or 2 (not in one cycle) degrees.
        so 2~4 for 2 edges where 2 is the cycle (i.e. multiedge), 3 is one edge and one loop and 4 is similar. (But all is disallowed)
      - So at least 3 edges with the loop causing degree 3.
    - Corollary 3
      - similar to the above 4~5 is impossible because 1 or 2 vertices can't be one cycle when 3 edges.
      - 4 edges
        similarly 4($C_4$),5($C_3$ and one edge),8 are possible.
    - Here
      > no simple circuits of length 4 or less
      so the above all is impossible
      then for 5 edges, at least degree 5 ($C_5$).
    - ~~Or~~ see [this](https://math.stackexchange.com/a/4848127/1059606) which I posted as one answer.
      ~~we only needs to care about the smallest degree with the same edge number~~
- [ ] 18
  - $r=e-v+2k$ based on $r_i=e_i-v_i+2$ is wrong
    because the unbounded region is counted duplicately.
  - see the ans
    - The above should minus $k-1$ due to "counted duplicately".
- [ ] 20 see the ans
  - Or $fd$ doesn't exist.
- [ ] 27 see the ans
  - We can use COROLLARY 1 to restrict the range based on [this](https://math.stackexchange.com/a/3016505/1059606)
    - a) $e\le 3v-6$ where $v=5$ so $e\le 9$ while $e_{K_5}=10$, so $1$.
      example for 1 see [this](https://alexispenamth350.wordpress.com/2012/10/03/the-crossing-nu/)
    - b) 15->12 so 3 See [this p2](http://people.qc.cuny.edu/faculty/christopher.hanusa/courses/634sp12/Documents/634sp12ch9-2.pdf)
    - c) 21->15 so 6, but failed.
      one possible case for 9 see [this](https://math.stackexchange.com/a/369781/1059606)
    - Similarly we use COROLLARY 3 for $K_{m,n}$
      - d) 12->10 (2) 
        example for 2 see [this](https://www.math.ru.nl/OpenGraphProblems/Wouter/RichterThomassen.pdf)
      - e) 16->12 (4)
        [This](https://arxiv.org/pdf/1404.1222.pdf) just uses the theorem
      - f) 25->16 (9)
  - Based on [this](https://mathworld.wolfram.com/GraphCrossingNumber.html) "NP-complete problem", it may be difficult to prove the crossing number of the complete graph and the complete bipartite graph.
- [ ] 28 see the ans
  - Here to form the 3-cycle, all in the inside or outside is both impossible because for example for $f$ only $f-i,f-h$ inside but no $i-h$ and for $a$ only $a-e,a-b$ inside but no $e-b$.
  - $e=15,v=10$ here $e\le 2v-4$ is no use.
  - [proof by cut-the-knot](https://www.cut-the-knot.org/do_you_know/CrossingNumber.shtml#:~:text=Among%20the%20six%20incarnations%20of,with%20one%20or%20zero%20crossings.) of $\ge 2$
    - $2q\ge gr$ here uses one edge will contribute to 2 degrees in total
      and the smallest cycle is the smallest degree of the region (for example $C_3$ with one edge has degree 3 inside and 5 outside of the cycle, i.e. [connected_planar_simple_graph] figure row_4-col_3)
      Then based on this
    - girth equal to 5 see [this](https://math.stackexchange.com/questions/4052160/prove-that-petersen-graph-has-no-cycles-less-than-or-equal-to-4#comment10330122_4052197) although this [one](https://math.stackexchange.com/a/1464559/1059606) and the cut-the-knot I didn't understand.
    - Notice here $c-2\ge 0$, which may influence the inequity sign.
```python
from sympy import *
init_printing(use_unicode=True)
f,c,e,v,E,k = symbols('f c e v E k')
f=(2+e-v)
e=(E-k)
print(simplify(solve((2+E-k-v)*c<2*(E-k),k))) # this can't simplify to the final step
```
- [x] 29
  - This is one special case of [Zarankiewicz's Conjecture](https://mathworld.wolfram.com/ZarankiewiczsConjecture.html)
  - we can also iterate from $(0,1)$ to $(0,\frac{n}{2})$
    then for $(0,1)$ no intersections
    for $(0,i)$ it has 
    $(i-1)\cdot (\overbrace{m-2}^{(\pm 1,0)}+\overbrace{m-4}^{(\pm 2,0)}+\cdots+\overbrace{0}^{(\pm \frac{m}{2},0)})$
    Then $2\cdot \sum_{i=1}^{\frac{m}{2}-1}i \cdot \frac{(m-2)\frac{m}{2}}{2}=\frac{(m-2)m}{4}\frac{(n-2)n}{4}$
- [ ] 30
  - see the ans
- [ ] 31 see the ans
  - Still similar to 27, it is [difficult][wolfram_GraphThickness] to calculate.
  - So I use this [lower bound](https://math.stackexchange.com/q/2553376/1059606) and example split I didn't take time to find.
    this is more flexible than [this][wolfram_GraphThickness] exact form. From the [paper](https://core.ac.uk/download/pdf/82563356.pdf), the exception for 9,10 may be not strictly proved.
```python
complete_graph_edge=lambda x:x*(x-1)/2
thickness_lower_bound=lambda v:complete_graph_edge(v)/(3*v-6)
for i in range(5,8): print(thickness_lower_bound(i))
# all bigger than 1

bipartite_edge=lambda x,y:x*y
thickness_lower_bound_bipartite=lambda x,y:bipartite_edge(x,y)/(3*(x+y)-6)
for i,j in [(3,4),(4,4),(5,5)]: print(thickness_lower_bound_bipartite(i,j))
# only 5,5 bigger than 1

# Since the subgraphs of complete bipartite graph can't have a circuit of 3. so we can use e<=2v-4
# This is also shown in [wolfram_GraphThickness] "The thickness of a complete bipartite graph"
bipartite_edge=lambda x,y:x*y
thickness_lower_bound_bipartite=lambda x,y:bipartite_edge(x,y)/(2*(x+y)-4)
for i,j in [(3,4),(4,4),(5,5)]: print(thickness_lower_bound_bipartite(i,j))
```
- [ ] 32 see the ans
- [ ] 33 see the ans
  - > The formula is valid for n ≤ 4.
    Because they are plannar so $\lfloor\frac{n+7}{6}\rfloor=1$
  - $C(n, 2)/(3n − 6)=\frac{n(n-1)}{6(n-2)}=\frac{n}{6}+\frac{n}{6(n-2)}$
    Then $\lceil\frac{n+1+\epsilon}{6}\rceil=\lfloor\frac{n+7}{6}\rfloor,\epsilon\in (0,1)$
- [ ] 36,37 see the ans they are both symmetric.
### 10.8
- 2~8,16(duplicate with EXAMPLE 4)~24,28,32~34,38,40,42,43 skipped
- [ ] 10 can be tracked based on degree-3 when 4 colors and check at the end ~~for all vertices~~ whether the same color for adjacent vertices.
  - clockwise from $h$: B,R,O,G,O (where Blue,Red,Orange,Grenn)
    then g:R/G -> f:GB/RB -> d:GB/B -> 
    i must be different from f,d,i
    then we can have clockwise from $h$: B,R,O,G,O,G,B,G,R
    here 
    1. B:h,e
    2. R:i,g
    3. O:a,c
    4. G:b,d,f
- [ ] 12
  - 10: Here aihb and bihc shares also $b,i$
    - If only to change one vertex color,
      if removing $i$, h,f,c make $i$ still the fourth color.
      if removing $b$, c,g,e make $d$ still the fourth color.
      They are both more complex than $h$.
- [ ] 14
  - See [this](https://distributedmuseum.illinois.edu/exhibit/four-color-theorem/#:~:text=A%20map%20of%20the%20United,Nevada)%20with%20only%20three%20colors.) where considers $C_5$.
- [ ] 26 see the ans
- [ ] 30
  - see the ans
    - This algorithm doesn't track based on adjacency matrix, maybe having many time overheads.
      So each color it has `for i := 1 to n` instead of excluding vertices after each coloring.
    - After **trying** assigning one color 
      it will check contradiction based on `for j := 1 to n`
- [ ] 31
  - > Successively as- sign color 2 to vertices in the list that have not already been colored
    this may be better adjacent to $n$ vertices already colored when we are to assign color $n+1$.
    This can ensure we must have this color.
  - see the ans
    - The above still can't be optimal
      See [this](https://www.cs.cornell.edu/courses/cs3110/2012sp/recitations/rec21-graphs/rec21.html) "A greedy algorithm for finding a non-optimal coloring"
      here the coloring **order** matters where the right exclues 6 vertices maybe unnecessarily after coloring 1,2 as numbered.
- [ ] 36 see the ans
  - g) here we can add one color when adding one edge to differentiate.
    This is different from $K_n$ because when **targeted** at one specific vertex, we **at least** have $kn$ colors.
    Also $K_{m,n}$ which targeted at one edge is enough.
    - This is similar to d)
    - Here the union of 1,4th in the coloring sequence must at most have 5 (here it is obvious because we adds only one color at the 3rd step which already uses 2 colors in the 1st).
    - > they must have six different colors, so eight colors would be required in all.
      Here is because only 5 colors are left, so we must add one new.
- [ ] 37
  - a) use 36-c) so 6
  - b) same as a) but here after $W_4$, if only add one color, 3 colors can't be sufficient for $a-g$.
  - c) the $K_3$ causes already 9. This is sufficient similar to the shape of a).
  - d) similar to c) assign 9 colors for $b,d,e$
    then assume $c,f$ adds $k$ colors
    then we need 6 different colors for $a,g$
    obviously these new colors can be crossingly assigned to $a,g$ (e.g. c:45Y, f:12X, then a can have X and g can have Y).
    When $k$ added, we have $3+k=6$ so $k=3$
    Then $12$.
  - see the ans
    - b) based on a) 6 colors is impossible
      for 7, here $1X$ can be also $2X$ and others are changed correspondingly WLOG. then the 2rd 34 is one must. Then similarly $5X$ can be $6X$.
      ```
        12  34
          56
      ->
        12  34
      5X  56  62
        34  1X
      ```
    - d)
      Based on [this](https://math.stackexchange.com/a/2915593/1059606) we should use $C_5$ instead of $K_3$ to color more vertices.
      WLOG, let $b,e,g,f,c$ clockwise assigned the colors in 36-g).
      then d must have 3 new colors because $b,e,f,c$ will use all 5 colors.
      so $8+3=11$
- [ ] 41 see the ans
  - > then in the component containing a we can interchange these two colors
    > G′ will still be properly colored.
    "still properly colored" because when we change vertices with color azure to chartreuse, we **only** needs to ensure it won't be adjacent to chartreuse, but since "interchange", it is ensured and due to component no other vertices need to be cared about.
  - > with b in one of them and m in the other
    Here I assume this cycle is similar to the circle shape.
    here b must be inside of the region, otherwise based on clockwise, $vb$ must cross $ac$ (I didn't give one strict geometric proof)
    ~~based on clockwise, m must be outside~~.
    - Also see [this](https://math.stackexchange.com/q/2418524/1059606)
      if the $vc$ line is curved to the left such that $vd$ is on the right of $vc$. Then $BD$ is possible.

      But here maybe we should recolor interchange $C,D$ and others are changed correspondingly. Then $BC$ is impossible which corresponds to $m$ (i.e. C) must be outside.
      Also see this [comment](https://math.stackexchange.com/questions/2418524/5-color-theorem-proof#comment8974142_2418535)
  - > If we now interchange blue and magenta on all the vertices in the same region as b, we will still have a proper coloring of G
    obviously vertices inside the region can't have edges with vertices outside the region since the graph is planar.
- [ ] 44,45 see the ans
  - > The sets of locations from which the tips of different prongs are visible are disjoint
    this means to see each tip, we need at least one guard each.
- [ ] 46
  - obviously each triangle has one red
    then all red will cover all triangles, then the polygon, so it is sufficient to use only red colors.
  - see the ans
    - see the proof why 3 colors are enough and possible.
### supplementary
- 4(also can be checked by $C_4$),6,7,14,18,22,38,39,40,49,50,58,62 skipped
- [x] 2
  - one vertex: 1
  - 2 vertices: 2 with edge or not
  - 3 vertices: 4 $0\sim 3$ edges
- [ ] 5 see the ans
  - check the 2 $C_4$
    ~~Then $v_\{5\sim 8\}$ correspond to ~~
    ~~$u_\{8,2,4,6\}$~~
    then $u_8,u_6$ both adjacent with $u_7$
    so when $u_8,u_6\to v_5,v_7$ $u_7\to v_4$
    then let $u_2,u_4\to v_6.v_8$
    which causes $u_3\to v_2$.
    then $v_1\to u_1$ and $v_3\to u_5$
    - Obviously the above process considers 2 cycles first then 4 groups of 2 edges.
- [x] 8
  - a) for simple graph, this is duplicate of one former exercise.
- [ ] 10 b) see the ans 
  uses the one-to-one correspondence although we can also use exclusion by numeration.
- [x] 12
  - ~~Here $|\bigcup_{i\in I}S_i|\ge |I|$ only cares about the whole set ~~
    ~~$S$ instead of subsets~~
    - ~~basis step: $|S_i|\ge |i|=1$ is trivial~~
    - ~~inductive step: $|\bigcup_{i\in I_k\cup \{k+1\}}S_i|\ge |\bigcup_{i\in I_k}S_i|+1\ge k+1$~~
    - ~~So all subsets met the condition of the Hall’s marriage theorem.~~
- [ ] 16 see the ans
  - a) Here $6$ considers the path direction based on $P(7,3)$.
    so $6$ for each triangle.
  - f) 
    > can start with an edge of the cycle and then go to the center ( n ·2 of this type)
    > start at the center ( n ·2 of this type)
    these 2 should be combined because "start with an edge of the cycle" we can have 2 directions
    then each has only one spoke to choose.
    Then the whole direction has also 2 possibilities. So $4n$
- [ ] 20 see the ans
  - Here is the definition of [maximal clique](https://en.wikipedia.org/wiki/Clique_(graph_theory)#Definitions).
  - See the [code](./miscs_snippets/py_codes/10_supplementary_20_BronKerbosch1/BronKerbosch1.py)
    - Here `X` is to avoid find cliques inside of the maximal clique.
```bash
# when `Debug=True`
$ python BronKerbosch1.py | less
P_cap ['b', 'c', 'e', 'f'] []
...
one maximal clique a-b-c-e
...
after removing b, P: ['c', 'e', 'f']
P_cap ['e'] ['b']
P_cap [] ['b']
# Here 'b' can survive, so it means it is adjacent with all of "a,c,e". 
# This means it is not maximal.
['b'] [] ['a', 'c', 'e']
...
after removing c, P: ['e', 'f']
P_cap ['f'] ['b', 'c']
P_cap [] []
# 1. Similar to the above, "a,e,f" can't be more maximal since X=[].
# 2. Here X contains already visited vertices, so if it is not empty, maybe the subclique has been visited.
one maximal clique a-e-f
```
- [x] 24
  - see the [code](./miscs_snippets/py_codes/10_supplementary_22/minimum_dominating_set.py)
- [x] 26
  - this is same as the [queen in the chess](https://herculeschess.com/how-does-the-queen-move-in-chess/#:~:text=The%20Queen%20can%20move%20any,is%20out%20of%20the%20game.).
- [x] 27
  - This is not ["n queen problem"](https://www.geeksforgeeks.org/n-queen-problem-backtracking-3/)
  - Based on this [paper](https://dspace.library.uvic.ca/bitstream/handle/1828/8634/Bird_William_PhD_2017.pdf?sequence=3&isAllowed=y) from [OEIS](https://oeis.org/A075458) from [wolfram](https://mathworld.wolfram.com/QueensProblem.html)
    It just use the algorithm for the "Dominating Set".
    > described an algorithm for finding a minimum dominating set of a graph on n vertices in O(1.8021n ) time and exponential space
  - Also see [this](https://askfilo.com/user-question-answers-algebra-2/a-simple-graph-can-be-used-to-determine-the-minimum-number-35383434373830) although the answer is not totally right.
  - By the [code](./miscs_snippets/py_codes/10_supplementary_22/minimum_dominating_set.py)
    we find 
    ```
    [(1, 1)]
    [(0, 0), (2, 2)]
    [(0, 0), (1, 1), (3, 3)]
    ```
    - Here 5x5 case is similar to 4x4 where (3,3) function same as (2,2)
    - 4x4 (2,2) only skips the 0th row and column.
- [x] 28
  - Here the map of the $(V(G_1)\cap V(G_2))\to V(H_1)$ may be not same as 
    $(V(G_1)\cap V(G_2))\to V(H_2)$
    Then $|V(G_1\cap G_2)|<|V(H_1\cap H_2)|$ is possible.
- [ ] 30 see the ans notice the diagonal.
- [ ] 32
  - I didn't have time to systematically find the algorithm to solve each sub-problems.
    So just [brute-force](https://qr.ae/pK60sj).
    ~~Then only (1,8),(2,4),(2,8),(4,4),(4,8),(8,8) are connected.~~
  - TODO [counting nonisomorphic simple ~~connected~~ graphs](https://qr.ae/pK60bs)
  - see the ans
    - c) see [this](https://math.stackexchange.com/questions/3677100/are-all-the-subgraphs-of-k5-planar#comment10333226_3677100), we can also draw the [greatest planar](https://math.stackexchange.com/a/3677103/1059606) subgraph $G'$ which implies subgraphs of 
    $G'$ are planar.
    - [nonisomorphic_simple_connected]
  - a) also [See](https://math.stackexchange.com/q/4849754/1059606)
- [ ] 34
  - we can also use the mapping to prove.
  - see the ans
    - it uses already proved theorems.
- [ ] 36
  - We can use the [Robin's Theorem](https://sci-hub.se/https://doi.org/10.2307/2303897) (I don't have time to prove all theorems I met but not referred in the book)
    see the ans
    - by the paper 
      > we see that the necessity of the condition is **clear**
      or just trying draw assuming $cd$ one direction, the "only if" by contrapositive proposition which from "disconnected after the removal of any arc" to "not orientable"
      because "disconnected" -> only one path between $c$ and $d$, i.e. $cd$ -> adding the orientation to the path, only one orientation between $c$ and $d$.
      - For 35,36, the "necessity" which is same as exercise 39 is enough to prove "not orientable".
  - Also see one [more general example](https://math.stackexchange.com/a/2613909/1059606).
```python
from sympy import Interval, Symbol, S, sin, cos, pi, maximum,minimum
n = Symbol('n')
k = Symbol('k')
max_edges=lambda x:x*(x-1)/2
f = max_edges(k)+max_edges(n-k)+1
from sympy import solve
stationary_point = solve([f.diff(k)], [k], dict=True)[0][k]
import sympy
sympy.simplify(f.subs(k,n/2))
from sympy.calculus.util import *
from sympy import oo
ivl = Interval(3,oo)
max_k_when_bridge=n-1
target_func=(n**2-3*n+6)/2
if maximum(sympy.simplify(f.subs(k,max_k_when_bridge)-f.subs(k,stationary_point)),n,ivl)>0:
  max_edges=f.subs(k,max_k_when_bridge)
else:
  max_edges=f.subs(k,stationary_point)
Diff=sympy.simplify(max_edges-target_func)
print_latex(f)
print_latex(max_edges)
print_latex(target_func)
minimum(Diff,n,ivl)
```
- [ ] 42 see the ans
  - > Otherwise, there must exist a smallest i such that (vi,v) and (v,vi+1) are edges of G
    if not existing, then all must be $(v_{i},v)$ or 
    $(v,v_{i})$
- [ ] 44 see the ans
  - See [vertex_connectivity_less_than_minimum_degree]
- [x] 46 
  - a) $\kappa(G)=2=\min_{v\in V}\deg v=2n/n$ is trivial
    then by the [Inequality](https://math.stackexchange.com/a/1441429/1059606), we are finished.
  - b) similar to a) $\kappa(G)=(n-1)=\min_{v\in V}\deg v=\frac{2\cdot\frac{n(n-1)}{2}}{n}$
  - c) trivially $\kappa(G)=r=\min_{v\in V}\deg v=\frac{2r^2}{2r}=r$
- [ ] 47 see the ans
  - the [skeleton](https://www.researchgate.net/figure/The-1-skeleton-of-the-triangular-prism-has-a-unique-3-colouring-up-to-isomorphism-shown_fig5_365291391) of a triangular prism
    1. based on symmetry, removing one vertex has 2 possibilities. They can't disconnect.
    2. removing 2, all inner and all outer are both impossible.
      one inner and one outer (adjacent or not) are also impossible.
      The above 4 possibilities based on symmetry are excluded.
    3. removing 3 which is $\min\deg v$ must be possible.
- [ ] 48
  - see the ans
    - we need to prove "each path is nonempty."
- [ ] 51 see the ans
  - [NP-hard](https://en.wikipedia.org/wiki/Graph_bandwidth#Computing_the_bandwidth), so just use the enumeration method.
  - a) since all are connected, so $n-1=4$
  - b) it just means the choice of the $v$ which is $K_1$ part
    obviously when $v=a_2,a_3$, it has the answer $2$.
  - c,d) See the [code](./miscs_snippets/py_codes/10_supplementary_51/bandwidth.py)
  - e) I just use the [result](https://en.wikipedia.org/wiki/Hypercube_graph#Other_properties)
- [ ] 52
  - see the ans
    - b) notice here radius can be same as the diameter
- [ ] 53
  - a)
    - > Thus, v cannot be a or b
      because $ua$ has length 1 and $ub$ has $ua-ab$ length 2, both not greater than 3. 
    - > Either u or v, or both, is not in the set {a, b}
      if both in, then distance is $2$ not greater than 3.
      - Here "u not in the set {a, b}" -> "assume {a, u} $\in$ E" -> "v cannot be a or b"
        So "both not in the set {a, b}" is necessary.
        - Then since for both, " Either {a, u} or {b, u} belongs to E" or corresponding $v$
          so "this gives a path of length less than or equal to 3 from u to v in G, a contradiction"
  - b)
    - The main problem is that the above "u-a-b-v" length 3 is allowed in G here, not leading to the contradiction.
      ~~So we need to find another method to solve the problem.~~
      So here we need to more specific by showing this case won't make $\overline{G}$ failure.
- [ ] 54
  - trivially, Euler circuit can be applied to the multigraph.
  - > Suppose that we follow the given circuit through the multigraph, but *instead* of using edges more than once, we put in a new parallel edge whenever needed
    This is the key idea. This is similar to 48.
    ~~We should not be totally similar to 48 where after the removal we can't know "at least m edges more than once" easily.~~
- [ ] 56 see the ans <a name="second_shortest_path"></a>
  - ~~By [this](https://stackoverflow.com/questions/4971850/which-algorithm-can-i-use-to-find-the-next-to-shortest-path-in-a-graph#comment7392944_4972027) counterexample allowing the loop~~, the ans [~~may be wrong~~ similar to this link](https://stackoverflow.com/a/4972027/21294350) is based on that the path has *at least one* edge difference with each other.
    - > If G - E is not connected, continue for next edge
      If disconnected, there must not be one path connecting the start vertex and the ending vertex because no path to substitute the cut edge.
  - [This one](https://stackoverflow.com/questions/4971850/which-algorithm-can-i-use-to-find-the-next-to-shortest-path-in-a-graph#comment137297470_4975663) TODO.
- [ ] 59 see the ans
  - See [this](https://math.stackexchange.com/a/128665/1059606) which doesn't need the restriction of $11$.
- [ ] 60 see the ans
  - c) see this [proof](https://math.stackexchange.com/a/1922797/1059606) of "$Q_n$ is bipartite" based on parity which is referred to in one of former exercises.
- [ ] 64
  - see the ans c,f)
- [ ] 66
  - see the ans
## 11
Redo 5.4-48
### 11.1
- 2~10,
  18~22,
  28,30(This is same as 26-b) $m^{h-1}-1+m,h=4$ which is the worst case),
  32~36,
  42~46 skipped
- [ ] 12
  - see the code [nonisomorphic_simple_connected]
    ~~TODO DFS proof~~ [See](#DFS_checking_cycle_proof) and [this](https://stackoverflow.com/a/66074045/21294350)
  - see the ans
    - We can also see the middle 2 as variants of the length-3 path and the other 2 corresponding to the asterisk graph.
- [ ] 13
  - see the code [nonisomorphic_simple_connected]
    a) then 3
    b) $(5-4+1)+(5-2+1)+\lceil\frac{5}{2}\rceil=2+4+3=9$
  - Also [see](https://math.stackexchange.com/a/2682799/1059606)
- [ ] 14 see the ans
  - > as well as the fact that if there is a path from a vertex u to another vertex v , then there is a simple path from u to v by Theorem 1 in Section 10.4.
    Since 
    > Let {x, y} be an *edge* of T
    it must be simple, we don't need "Theorem 1 in Section 10.4".
  - The converse step is same as one exercise before which is that 2 related paths constitute one loop.
  - > If not, then T has a simple circuit
    Here the exercise assumes "connected" is one common condition.
- [ ] 15 see the ans
  - a)
    - > If G is not a tree, it contains, by Exercise 14, an edge whose removal produces a graph G′ , which is still connected
      Same as 14, it assumes "connected".
    - > Repeat this procedure until the result is a tree
      i.e. make all cycles disappear.
    - Also see this [proof](https://math.stackexchange.com/a/834901/1059606)
      > which is impossible as a connected graph on n vertices must at least have n - 1 edges.
      ~~because one edge except the 1st (add 2 new vertices) will at most add one vertex to have one vertex already added to keep the connectivity which is said somewhere in this note.~~
      See 10.4-28.
- [ ] 16,24 see the ans
- [ ] 25
  - similar to 24, $83/(m-1)\in\mathbb{N}\Rightarrow m=2,84$ both are impossible to be with "height 3".
- [ ] 26
  - a)
    - $i\in \mathbb{N}\Rightarrow n=mi+1\in \mathbb{N}$
      So we only need to care about $i$
    - > we can get as few as 4(m −1) + 1 leaves by putting only one internal vertex at each such level
      This is based on THEOREM 4 (ii) with $i=4$ due to the height.
      - This is the *lower bound* of the "internal vertices".
  - b)
    - see the ans
- [x] 31 trival based on THEOREM 2
- [x] 38
  - see [nonisomorphic_simple_connected]
    - a)
      - only 1 when unlabeled
        then we only need to choose for the middle. So $\binom{3}{1}=3$
    - b)
      - similar to a)
        when it is the path, we select 2 numbers for the middle and the rest are put in order.
        so $4*3=12$
        when asterisk, we select for the degree-4 vertex, so $4$.
  - TODO proof of the generalized theorem Cayley's formula
    [1](https://arxiv.org/pdf/0908.2324.pdf#:~:text=There%20are%20exactly%20nn%E2%88%922,set%20V1v1%2C%20v2%20...) [2](https://math.libretexts.org/Bookshelves/Combinatorics_and_Discrete_Mathematics/Applied_Combinatorics_(Keller_and_Trotter)/05%3A_Graph_Theory/5.06%3A_Counting_Labeled_Trees)
    - Better using [Kirchhoff's theorem](https://en.wikipedia.org/wiki/Kirchhoff%27s_theorem#Cayley's_formula)
      [induction proof p654 as wikipedia shows][the_nature_of_computation]
      - Notice it [only applies for the undirected graph](https://arxiv.org/pdf/1904.12221.pdf)
      - [Empty product](https://math.stackexchange.com/a/1762542/1059606) (i.e. Vacuous Product) implies "the determinant of the 0x0 matrix equals 1"
      - 13.3 [see this p6](https://www.csie.ntu.edu.tw/~kmchao/tree07spr/counting.pdf)
        Here $G\setminus e$ corresponds to "the number of spanning trees of G that contain e" because we can just reverse the contract of 2 vertices and it still be one spanning tree which contains the $e$ constructed by the reverse.
      - > Thus the vector consisting of all 1s is an eigenvector with eigenvalue zero, and L has determinant zero
        can be [generalized "eigenvectors of the Laplacian matrix associated with eigenvalue zero"](https://simonensemble.github.io/pluto_nbs/graph_connected_components.jl.html) to $C$ connected components where $1/\sqrt{|V_c|}$ can be anything to denote the "equal temperature".
        - The above shows the algebraic multiplicity of eigenvalue 0 is *at least* $C$
          TODO strict proof for [exactly](https://math.uchicago.edu/~may/REU2013/REUPapers/Marsden.pdf) $C$
          - The above $G_c$ corresponds to the block $A_r$ in Theorem 3.9.
      - in (13.4) we get the right by hypothesis and derive the left by the definition of the determinant.
      - application to [prove Cayley formula](https://math.stackexchange.com/a/1252851/1059606)
        - $\gamma _{A}(\lambda )\leq \mu _{A}(\lambda )$ [proof](https://math.stackexchange.com/a/458200/1059606) which is from this when I [prepares for the graduate_entrance_exam](https://bitbucket.org/czg980/graduate_entrance_exam_simplified/src/4c6a0d7d21c9f78af8f037fde20b271f90dfe88a/textbooks/review/linear%20algebra/README.md?at=master#README.md-158,281,391:393,396)
          - Also [see](https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors#Algebraic_multiplicity)
            - Due to the $R^n$ dimensional space property, we can find one "orthonormal set" to form ["an orthonormal basis"](https://en.wikipedia.org/wiki/Orthogonal_matrix#Matrix_properties), then we have $V^T V=I$.
            - > we get a matrix whose top left block is the diagonal matrix
              this can be seen as $[{\displaystyle {\boldsymbol {v}}_{1},\,\ldots ,\,{\boldsymbol {v}}_{\gamma _{A}(\lambda )}}]^T A [{\displaystyle {\boldsymbol {v}}_{1},\,\ldots ,\,{\boldsymbol {v}}_{\gamma _{A}(\lambda )}}]$
      - Notice when generalized to multigraph (here I skips the loop although in 639 it contains that)
        Then $G-e$ is same as before (also for loops. Matrix also stays same.)
        $G\cdot e$ also works by contraction because all the other edges among multi edges are excluded due to $e$. ($L_{G\cdot e}$ (0,0) entry should minus all multi edges although it doesn't influence the $T(G\cdot e)$ calculation.)
      - > The cofactor matrix of a laplacian matrix has all of its entries equal to each other
        [this](https://math.stackexchange.com/questions/4143714/find-cofactor-matrix-of-a-certain-matrix#comment10346567_4143719)
        - > $adj(Q)$ is symmetric
          if $Q=Q^T$, then $C_{ij}^T=C_ji\Rightarrow |C_{ij}|=|C_{ji}|,j\neq i$ (here means matrix).
        - [See][algebraic_graph_theory]
      - TODO cofactor [->](https://en.wikipedia.org/wiki/Kirchhoff%27s_theorem#) ${\displaystyle t(G)={\frac {1}{n}}\lambda _{1}\lambda _{2}\cdots \lambda _{n-1}\,.}$.
      - code implementation by geeksforgeeks may be [carelessly wrong](https://discuss.geeksforgeeks.org/comment/aca684bf-5367-4296-b306-caedb84f8f5c/gfg).
      - Trivially, here we doesn't think about isomorphism (e.g. for $K_3$ it should have $1$ tree when unlabeled by A000055. But here removing one edge $e=ac$ (2 edges in $G-e=\{ab,bc\}$) 
        or not (~~1 edge~~ 2 multiedge in $G\cdot e=\{a'b,a'b\}$. Here I use the edge set) will both have valid contribution to the tree number count). We can think it as we label all nodes first then we choose edges.
- [x] 40
  - if not choosing $e$, then it must contain one subtree which is the proper superset of $d-b-\{a,c\}$ and
    $f-\{g,h-\{i,j,k\}\}$
    So it must has one greater "eccentricity".
- [ ] 43
  - choose the middle vertex/vertices of the longest simple path.
  - see the ans
    - > Clearly, this path cannot contain both u and v or else there would be a simple circuit
      ~~This may mean .~~
      we can think of the path as one vertex string, then $c-\ldots-u-\overbrace{\ldots}^{\text{This can't pass c due to the properties of the path, so causing the circuit}}-v-\ldots-w$
      - "or else" may be "otherwise"
    - > In fact, this path from c to w leaves P and does not return to P once it, possibly, follows part of P toward either u or v
      Just draw it. It will cause one circuit if return.
    - Based on "vertex string", we just check the *common vertices* between $c-\ldots-w$ and $u-\ldots_1-c-\ldots_2-v$
      trivially, $c-\ldots-w$ can share with only one of $u-\ldots_1-c$ and $c-\ldots_2-v$ based on the above point.
      So we can
      > Without loss of generality, assume this path does not follow P toward u
- [ ] 48 see the ans
  - $n-N(h)=2^h-1\Rightarrow h= \log(n-N(h)+1)\le \log(2n-N(h))\le \log(2n)$
### 11.2
- 2~6,14,20~24, skipped
- [x] 8
  - we can use 2-ary tree with equal or unequal 2 cases.
  - see the ans
    - balance or not means it is just the 2-ary tree.
      i.e. lighter one doesn't mean it is counterfeit which is not same as example 3.
    - > We can put one, two, or three coins in each pan for the first weighing (no other arrangement will yield any information at all)
      obviously we need to have 2 pans with same number of coins.
      if four, it must be unequal so we don't do that.
    - Notice here the decision is inclusion or exclusion instead of selecting one part of two.
      - See 7
        > Begin by weighing coin 1 against coin 2. If they *balance*, weigh coin 1 against coin 3.
        trivially, here only 3,4 are possible to be counterfeit.
        > If coin 1 and coin 2 are not the same weight, again weigh coin 1 against coin 3
        here only 1,2
        - Notice the above what to compare at the 2nd step may have more than 1 choices.
- [x] 9 see the ans
  - similar to FIGURE 3,
    > If equal, apply Example 3 to coins 1, 2, 7, 8, 9, 10, 11, and 12.
    "7, 8, 9, 10, 11, and 12" is enough.
  - Based on the ans, it assumes *only* one is lighter than others which is same as the example 3.
- [x] 10
  - same as 8, $\log(4)=2$ to "determine whether there is a counterfeit coin" and 1 more for "whether it is lighter or heavier than the others".
    My thoughts are same as [this](https://qr.ae/pKEhmF) and more [generalized](https://qr.ae/pKEhqK) one although they don't offer why this will always give the *optimal* result with one extra weight to get the info about lighter or heavier.
  - see the ans
    - > three for each of the other two outcomes of the first weighing
      one is lighter, one is heavier or equal.
      - > If the pans balance, then we know that there is no counterfeit, and subsequent weighings add no information. 
        then totally 7, so "the first weighing involves two coins per pan" is impossible.
    - > If the scale does not balance, then we have not solved the problem
      This is to show 2 steps are not enough.
- [ ] 12 see the ans. Here assumes using binary tree has "the least number of comparisons".
  - > again relabel all four of these elements if necessary to have b < d
    i.e. if $d<b$, $c<d<b,a<b$ which has the same form as when $b<d$
  - > namely either that it is less than the largest among a, b, d, and e, or that it is less than the second largest.
    i.e. either $d$ is the largest or the "second largest."
- [ ] 16
  - we can also use $1+2+\cdots+2^{k-1}=2^k-1$ although it is more complex than the ans.
- [ ] 18
  - by figure (b), we need $(h-1)\cdot (n-1)$ to sort the rest 
    $n-1$ elements
    then plus the $n-1$ for the 1st element, we need $h(n-1)\ge \log(n)(n-1)\ge \log(n)\frac{n}{2}$
  - see the ans
    - Here we first have $f(n)\le 2n$ elements
      then (17 assumes full and balanced and complete, so $k-1=h-1$)
      we have $(f(n)-1)\cdot \log(n)\ge \log(n)(n-1)$
    - The above lacks the step of $f(n)$
- [ ] 26
```
# First
 /\
a /\
 b /\
  c /\
   d  e
# Second
    /\
   /  \
  /    \
 /\    /\
b  c  /\ a
     d  e
```
- [ ] 28
  - see the ans
    - Here `((N − 1) mod (m − 1)) + 1` is to remove 0
    ```python
    m=10
    for i in range(1,100):
        first=i%(m-1)
        second=(i-1)%(m-1)+1
        if first!=second:
            print(first,second,i)
    ```
    - Based on the [paper][huffman_1952_minimum_redundancy_codes] as [wikipedia](https://en.wikipedia.org/wiki/Huffman_coding#n-ary_Huffman_coding) "This approach was considered by Huffman in his original paper." shows
      - "0-probability place holders" may be just $-\infty$ in the former exercise.
        > If the number of source words is *congruent to 1* modulo n−1, then the set of source words will form a proper Huffman tree.
        - It is related with the above $\mod (m-1)$
          - > Therefore, mo (which, of course, is *at least two* and no more than D) must be of such a value that (N-n0)/(D-1) is an integer
            so when $N=D\Rightarrow n_0=1<2$ we should do nothing at the init step.
            Then
            > whose children from left to right are these k vertices in order by weight (from greatest to smallest), with labels 0 through k −1 on the edges to these children 
            does nothing when $n_0=1$ because no children.
            - This is to make the tree *almost full*, also see 32.
          - It just *reverse back* from the final step to get
            > then $(N_1-1)/(D-1)$ must be an integer
    - TODO [arithmetic coding](https://en.wikipedia.org/wiki/Huffman_coding#Optimality)
- [x] 29
```
  /|\
 / | \
A  E /|\
    / | \
   T  |  Z
     / \
    N   R
```
  - see the ans
    - It uses $2,1,0$ and $0,1$ from left to right for 3-ary and 2-ary each.
- [ ] 30
  - see the ans
    - Here we may not send odd number of characters using b).
- [ ] 32 see the ans
  - > then we can obtain a code that is at least as efficient by interchanging the symbols on some of the leaves to make a and b siblings at the bottom-most level (since moving a more frequently occurring symbol closer to the root can only help)
    WLOG, assume $p_a>p_b$
    then by the ALGORITHM 2, $a$ should be at the left of $b$
    Assume the bottom level $(c,d),p_c>p_d$ where c,d can't be both a,b.
    Then before interchange $a,c$ has length $len(a,c)=m p_a+n p_c,m<n$
    after interchange $len'(a,c)=m p_c+n p_a$
    then $len(a,c)-len'(a,c)=(m-n)(p_a-p_c)\ge 0,p_a\le p_c$
    so the interchange make the code more efficient.
    - The above interchange trivially can be used in the *generalized* one.
  - Here trivially $H_k$ and $H_k'$ has the same symbols with the same possibilities including 
    $(c,p_a+p_b)$
- [ ] 34
  - see the ans
    - > Note that if the cited reference was to a square vertex rather than a circle vertex, then the outcome is reversed
      This is because $+1$ when square just means the following steps will make the **current** player win,
      So it is changed to circle it means it will make the player corresponding to the circle win, so $-1$, which is reversed.
  - Also [see](https://www.overleaf.com/read/jswdgrdzsgfk#cea6e4)
- [ ] 36
  - > a player will *never want to move to a situation* with two piles, one of which has one stone, nor to a single pile with more than one stone.
    1. Assume player 1 moves to "a single pile with more than one stone"
      then player 2 can make player 1 lose by having only 1 left.
    2. the former is similar, player 2 can remove one pile and have only 1 left.
    - Then 22 must make player 2 lose
      1. combine -> 4
      2. 21
      3. 2
      All 3 cases are among the above 2, so they make player 2 lose.
      So 22 has value 1.
      Then the rest don't need to look at.
    - The level 1 omits 41,21,
      the level 2 omits 31,11,21 (for 211) and ...
- [ ] 38
  - a) trivially center $X$ will help both $X$, so will win
  - b) it will must mark $(2,1)$($(2,3)$)
    then circle will block $X$ at $(3,1)$,
    Use this process again for $(2,3)$($(2,1)$)
  - c) similar to a) $(2,3)$
  - d) trivially $X$ must mark $(1,3)$
    then circle $(1,2)$
    then cross $(3,2)$
    Then circle can't win at either left location, similar for cross.
  - see the ans
    - The above b) is wrong
      - > as long as the second player makes his third and fourth moves in the first and third columns
        if $(2,1),(2,3)$ then 2nd win
        otherwise, at least one is in the 3rd row,
        so *all rows* are occupied by the 2nd player
        diagonals are also occupied by the 2nd player
        So if "the first and third columns" are also occupied by the 2nd player plus the 2nd column already occupied, then the 1st player can't win.
- [ ] 39
  - By induction, the 2nd player can always make 2 piles with the same number
    then at the end, it will be reduced to $(2,2)$ 
    (because $(1,n)$ is not perferred by player 1)
    Then the player 1 will always cause the situations in exercise 36, so player 1 loses.
  - see the ans
    - > If first player takes *all* the stones from one of the piles, then second player takes all but one stone from the remaining pile and wins. If first player takes all *but one* stone from one of the piles, then second player takes all the stones from the other pile and wins
      > if first player takes *two* stones from a pile, then second player takes one stone from the remaining pile and wins. If first player takes *one* stone from a pile, then second player takes two stones from the other pile and wins.
      These 2 have been said in 36.
    - The above is more specific with $(2,2)$ although the ans just use the strong induction for 
      $(j,j),j\ge 2$
- [ ] 40
  - if either is 1, then trivially by exercise 36, player 1 wins
    two piles are $(m,n),m,n\ge 2$
    1. ~~$(2,2)$ remove one pile~~ impossible due to "different numbers of stones".
    2. $(m,n),m,n\ge 2$ but $m,n$ are not both 2
      then remove stones leaving $$
  - see the ans
    - it is based on 39.
- [ ] 42
  - see the ans
    1. > the actual number of moves is the sum of the *distinct* pile sizes
    2. > a position with just *one pile has one fewer* move
- [ ] 44
  - see the ans
    it just *pass the payoff up* by the recursive procedure.
### 11.3
- 2~18(similar to 16),
  22~24,28~29,30~34 skipped.
- [ ] 20 see the ans
  - since there is no symmetric method for this counting, so I didn't dig into the counting for $3,4,5$.
- [ ] 21
  - similar to 20 
    the following is based on choosing the delimeter one by one. 
    - By symmetry we can also count by $2\cdot(2+5)$
    $$
    A\cap (\cdots)
    \begin{cases}
      B-(\cdots)
      \begin{cases}
        A\cap(B-A)\\
        (A\cap B)-A  
      \end{cases}\\
      (B-A)\cdots
      \begin{cases}
        (B-A)\cap (B-A)
      \end{cases}\\
      (B-A\cap B)-A
      \begin{cases}
        (B-A)\cap B\\
        B-(A\cap B)
      \end{cases}
    \end{cases}\\
    (A\cap B)-(A\cap B-A)
    \begin{cases}
      (A \cap B)\\
      A\cap(B-A)
    \end{cases}\\
    (A\cap B-A)\cap(B-A)
    \begin{cases}
      (A\cap B)-A\\
      A\cap(B-A)
    \end{cases}\\
    (A\cap B-A\cap B)-A
    \begin{cases}
      A\cap(B-A\cap B)
      \begin{cases}
        (B-A)\cap B\\
        B-(A\cap B)
      \end{cases}\\
      (A\cap B)-(A\cap B)\\
      (A\cap B-A)\cap B
      \begin{cases}
        (A\cap B)-A\\
        A\cap (B-A)
      \end{cases}\\
    \end{cases}
    $$
  - See [this](https://math.stackexchange.com/a/2329865/1059606), so we can just use the formula in p556.
- [ ] 26
  - just as what example 7 does,
    we combine operands and operators together based on the specified number. 
  - > we can recognize the first leaf as the first vertex with no children
    more specifically, i.e. with no children which is one operator.
  - > The result is the preorder and child counts of a tree with one fewer vertex.
    preorder because we remove one *leftmost leaf*.
  - compared with FIGURE 11, all vertices have 2 children there, but we can't decide the tree form.
- [x] 27 similar to 26
- [ ] 30
### 11.4
- 2,6~8,
  16,20,26(where 9 is 2 $C_4$)~28,32,
  40~42(just think of doing $n$ times of find one spanning tree when one forest has $n$ trees),56,59(same as 58) skipped
- [x] 4
  - trivially here DFS or BFS is better to construct the spanning tree.
- [x] 10
  - here $ab,ef$ are cut edges
    Then we can only choose among the middle 4 edges.
    But any 2 (either adjacent or not) of the middle 4 are cut edge pairs.
    So we can only choose one among the middle 4 edges.
- [ ] 11
  - d) similar to 10 "any 2 (either adjacent or not) of the middle 4 are cut edge pairs"
    so $5$ when removing any one edge.
  - see "Kirchhoff's theorem" and the corresponding [code](./miscs_snippets/py_codes/11_4_spanning_tree_labeled/Kirchhoff.py) for systematic calculation.
- [ ] 12 see the ans
  - Since [no exact formula](https://math.stackexchange.com/a/396530/1059606) although maybe some complex [recurrence formula](https://www.researchgate.net/post/What_is_the_number_of_possible_non-isomorphic_trees_for_any_node/5e7b2d02842a473ee35a4176/citation/download) ([i.e.](https://qr.ae/pKQX03)) which needs the help of another somewhat complex sequence, we still just use the brute-force by computer. See [nonisomorphic_simple_connected]
    - It corresponds to [A000055](https://oeis.org/A000055) which has no root.
    - Back to 11.1-38,
      It corresponds to ["the number of spanning trees in a complete graph"](https://oeis.org/A000272) because here we think each vertex is different (i.e. labeled).
    - Here "nonisomorphic spanning trees" means "nonisomorphic unrooted trees" as 11.1-12,13 where "nonisomorphic" -> unlabeled.
- [x] 14
  $\overbrace{a-b-c}^{\text{trivially by the alphabetical order}}-\overbrace{h}^{\text{the only possibility}-\overbrace{g}^{\text{alphabetical}}-\overbrace{l}^{\text{the only possibility}}}$
  then alphabetically h-i-d-e-f
  only possibility f-k-j-n
- [ ] 18 see the ans
  - d)
    - > the result will always be the same (up to isomorphism)
      starting vertex WLOG can be arbitrary.
      - > From one of them we fan out to two more
        by symmetry this can be also arbitrary.
      - > pick up one more vertex from another neighbor
        i.e. choose either 3 or 4 to fan.
        in this case either can be transformed to the other by flipping by 1-7 line (i.e. the $45^o$ line) while keeping 5-2,2-6.
        - choosing 5-8 or 6-8 is similar.
- [ ] 22
  - by recurrence, breadth-first
    expand root $r$ to one node which is in one $Q_{n-1}^{(1)}$ 
    (let it be $v$) and the rest $S(v)$ are in the other 
    $Q_{n-1}^{(2)}$ .
    Then by symmetry we expand $v$ next and get $Ex(v)$.
    Then we expand the rest $S(v)$. But due to the mirror, they can't be expanded to 
    $Q_{n-1}^{(1)}$
    Then we expand $Ex(v)$ similar to 
    $S(v)$.
    Recursively, we get 2 tree $T_{n-1}$ 
    corresponding to $Q_{n-1}$ with their roots being 
    $r$ and $v$.
  - depth-first
    By induction, assume $Q_n$ corresponds to one path
    Then $Q_{n+1}$ can be one path which is first constructed for one 
    $Q_{n}^{(1)}$
    and then due to mirror, we have *one edge* to get to $Q_{n-1}^{(2)}$.
    by induction hypothesis, it is also one path.
  - see the ans
    - > can be obtained by changing one 0 that has no 1’s following it to a 1 .
      i.e. $10...$ is the "he root of a copy of $T_n$".
      Then all nodes $01...$ or $001...$ can't be expanded to $11...$ or $101...$ which is another $Q_n$.
      Then recursively do it because $Q_n$ is also constructed recursively. (More specifically, $0100...$ can go to $01100...$ which can be seen as they are in done in $Q_{n-1}$ by omitting the leading $0$ but $00100...$ can't)
      - This means same as the above
    - > However, if “bad” choices are made, then the path might run into a dead end before visiting all the vertices,
      e.g. in 18 ans, 1-3-5-8-6-2 will make all neighbors of 2 (1,5,6) have been visited, so "a dead end".
- [x] 24
  - we can also use the preorder (i.e. DFS) or others of the spanning tree.
    Since BFS has the root first, so it is not inorder and postorder and also [not preorder](https://stackoverflow.com/questions/55243105/breadth-first-search-traversal-vs-pre-order-traversal-vs-depth-first-search-trav#comment97220653_55243795)
- [ ] 25
  - As [BFS_radial] says, if there is one shorter path, it must be searched earlier, leading to the contradiction. (Here is based on "unweighed").
  - see the ans
    - > By the inductive hypothesis, u′ is at level l in the breadth-first spanning tree
      because it has "length" $l$, otherwise "a shortest path from v to u" can be shorter (u' has lenght $< l$) or doesn't include u' (u' has lenght $> l$)
    - > although the edge connecting u′ and u is not necessarily added
      i.e. maybe added before by other adjacent vertex of $u$ at level $l+1$.
- [ ] 30
  - a) it is one type of decision tree.
- [ ] 34
  - Assuming connecting $u,v$ with level difference $\ge 2$ and $u$ is shallower.
    And by radial structure `dist(root,v)\le dist(root,u)+1`.
    But the level of $v$ implies `dist(root,v)\ge dist(root,u)+2` as 25 shows, contradiction.
    - ~~This just means by radial structure,~~
      ~~if there is one edge between u and v~~
      ~~WLOG, u is visited first before v is visited, then v must be added by uv so level has difference 1.~~
    - > at the same level
      ```
        n
      / | \
      u v ...
      ```
      > at levels that differ by 1
      ```
          n
        / | \
      ... v ...
      /
      u
      ```
  - see the ans
    - > the algorithm processed u before it processed v
      so `level(u)<=level(v)` based on WLOG (~~`=` when they are added by different parents~~) and 47 visiting order implying the level order.
      - > the parent p of v must have already been processed before u
        otherwise $uv$ will be added.
        - Here rephrase by comparison expression.
          Then `level(p)<=level(u)`
          - Also by assumption, `level(p)=level(v)-1`
            Then Q.E.D.
    - > First notice that the order in which vertices are put into (and therefore taken out of) the list L is level-order
      i.e. the vertices are taken by group which are at *the same level*
      and the relative order at the same level depends on the sorting order for this level.
      See ALGORITHM 2 for the `L` meaning.
      - More specifically, we can see the orderr is from top to bottom and *stops at each level* where we then traverse from left to right.
  - This shows [back edges are impossible in BFS](https://stackoverflow.com/questions/20847463/finding-length-of-shortest-cycle-in-undirected-graph#comment31283237_20847998).
- [ ] 36
  - similar to [nonisomorphic_simple_connected],
    add nodes by level and check whether back edges occur by `parent != i`.
  - see the ans
    - ~~Here `w` can't be the ancestor of `v` when `w` is not the parent of `v` by ~~
      by 34, when `w` is not the parent of `v` ("at levels that differ by 1") and trivially not same as `v` ("at the same level")
      then `w` can't be the ancestor of `v`, so *"simple"* circuit when "followed by the path from the root to w traversed backward"
      - "simple" can be also implied by 
    - See [this](https://stackoverflow.com/a/40456213/21294350) which can find the shortest cycle.
      Also see [this](https://stackoverflow.com/a/77927343/21294350)
      - If finding one shortest cycle with 2 nodes. See [this](https://www.geeksforgeeks.org/find-any-simple-cycle-in-an-undirected-unweighted-graph/)
        we can first to prove its existence by DFS (notice it may be not the shortest, see [this](https://stackoverflow.com/a/20847998/21294350) which implies `A,B` has one cycle but the found `A-1...` is longer than `A-B-C-D`)
        Then use BFS for "the shortest path".
        - `ok = True;` is weird. Maybe `False` better.
        - `q.pop(0);` implies FIFO queue.
        - kw
          `# Ignoring the direct edge`.
- [ ] 38
  - BFS and DFS both have the following structure.
    ```
    root- n-1 leafs
        |
        - node - n-1 leafs
    ```
  - see the ans
    - It uses 2 colors to prove bipartite.
      And based on spanning tree traversing all vertices and we also checking all adjacent edges for all vertices, 
      So we will color considering **all edges** and vertices. If 2 color possible, then bipartite.
- [ ] 43
  - See [DFS_no_cross_edge] and see the ans
    - Notice here `(u,v)` is `(v,u)` in the above link.
    - Here it assumes u is *being processed* WLOG because we are considering "edge uv".
    - > because we are not finished processing u yet
      corresponds to
      > not "closed" yet
    - > On the other hand, if the processing of v had already begun *before we started processing u*
      ~~This is not case 2 in the above link~~
      This is the case 1 because the vertex being processed (i.e. `v` in SO) has the discovered node as the ancestor (i.e. "u is indeed a parent of v" in SO).
    - > v must appear in the subtree rooted at u (and hence, must be a descendant of u)
      Here it means v is in the subtree *rooted at one child* of u before u reaching v by uv.
      based on "~~we are processing vertex u~~ we are not finished processing u yet" (i.e. "not "closed" yet" -> "basically traversing a subtree which has u as a root" in SO although these `u` doesn't mean the vertex when considering the visiting order.).
      ~~corresponds to~~
      ~~> u was discovered and closed already.~~
      - This is case 2 (not ~~2.2 which is one deleted comment~~ case 1) in SO because `v` (i.e. the descendant) must be closed when visited ~~the second time~~ by `u` otherwise we can't backtrack to `u`.
    - > It must be that we had *not* finished processing v
      i.e. case ~~2.2~~ 1 ~~(if finished, then case 2.1. Rephrased for this exercise, `v` doesn't have `u` as te)~~ (i.e. the node being processed is the descendant)
      See [DFS_no_cross_edge_improvement] where excludes the case where "we *had finished* processing v" "before we started processing u", i.e. v is closed before processing u so "u doesn't have v as the ancestor".
    - **Notice** since SO is based on whether *closing* while here is based on the *visiting order* to be splitted into cases.
      So they have different ~~conditions~~ prerequisites to use for proving, which caused case 2 more difficult in SO and case 2 here more difficult.
      - case 2 here is implied by the split condition, i.e. whether "closed already", in SO.
        More specifically, in SO it implies "not "closed"" -> "had not finished processing v".
      - case 2 in SO can be [proved just as the book does](https://stackoverflow.com/questions/28942262/dfs-in-an-undirected-graph-can-it-have-cross-edges/28942405#comment137389358_28942405).
  - Here the exercise [combines forward and back edges together][DFS_only_2_types_edges].
- [ ] 44
  - at least for edges incident with one degree-1 vertex.
  - see the ans
    - The above is one special case for cut edge.
    - > If the edge is a cut edge, then it provides the unique simple path between its endpoints
      if not unique, then not one "cut edge", contradiction.
      - iff part is proved in 10.4-38 and [this][tree_imply_all_cut_edge_i_e_no_circuit]
      - > Therefore it must be in every spanning tree for the graph
        because we need to ensure *connectivity*.
      - > then it can be removed without disconnecting the graph
        i.e. in one circuit similar to the above proof
    - This is based on the process of removing edges to construct one spanning tree.
    - Here [$\neg\text{in every spanning tree}=\text{not in some}$](https://math.stackexchange.com/a/1651713/1059606)
- [ ] 46
  - see the ans
    - Here it connects the path with the depth in DFS, then the number of ancestors.
    - We can improve this bound
      when adding backedges to the spanning tree
      we count the number of ancestors for each vertex with one tree edge or back edge incident with both vertices from bottom to top (This can consider **both** tree edge and back edge),
      then we can't limit `k-1` more because we don't know the structure of the tree.
      But the root must have 0, so we can lower the upper bound to `(k-1)(n-1)` (If we can know the number of level-1 vertices, we can proceed one step more)
  - If we let *all* leaves with depth `k-1` (This trivially scales too much for the upper bound when `n` **leaves**)
    then backedges seems to be difficult to be considered then.
- [ ] 47 (i.e. 25) used by 34
  - Here visiting order is based on [frontier][Graph_space_complexity_vs_time_complexity].
  - If directly proved by the BFS process, this is more trivial because they are added to the tree when *first* visited and the tree is updated by [*level*][BFS_level_order] (1. This is just the rephrase of "visits vertices in order of their level" 2. so "We must show that v is at the lowest (bottom-most, i.e., numerically greatest) level of the tree" in the ans) different from DFS.
    - Maybe this is informal as 34 says.
  - see the ans
    - > Therefore, u must have been processed before w
      because
      > Then w is at a lower level than u
      - > therefore v would have joined the waiting list
        because by 
        > The last vertex to be visited during breadth-first search of this tree, say v, is the one that was *added last* to the list of vertices waiting to be processed. It was added when *its parent, say u, was being processed.*
        *only* $u$ in $T$ can add $v$, same for $T'$ after removing 
        $v$.
        Then $v$ will be at the same level as $w$ which is before $x$ contradicting with "added last".
- [ ] 48
  - based on [backtracking_AND_DFS_imply_preorder]
    DFS trivially use the [NLR](https://en.wikipedia.org/wiki/Tree_traversal#Pre-order,_NLR) *visiting order* where L is first expanded.
  - see the ans
    - > adding the statements “ m := m + 1 ” and “assign m to vertex v ” as the first line of procedure visit
      implies index starts from 1 as the exercise shows.
    - > if a vertex’s sibling has a smaller number, then it must have already been visited
      This is implied by the *strictly increasing* `m := m + 1` when calling `visit`.
- [ ] 50
  - This is same as 34.
  - see the ans
    - The proof before
      > so this directed edge goes from a vertex at one level to a vertex either at the same level or one level below
      are mostly same.
      - Here we assumes $u\to v$ is one directed edge.
        Then it is either one forward edge / cross edge when "processed u before it processed v" or back edge / cross edge when "processed v before it processed u".
- [ ] 51
  - This is just enumeration for all sub-cases when not the tree edge.
    1. between the ancestor and the descendant
    2. [not case 1 -> cross edge](https://en.wikipedia.org/wiki/Depth-first_search#Output_of_a_depth-first_search)
      - "connecting a vertex to a vertex in a previously *unvisited* subtree." where the subtree is the *child tree* (non-child unvisited one is impossible because that must be visited by the current node [to be expanded]()) -> tree edge
        see the ans
        > it must be the case that its head v had already been visited
        excludes this case.
  - see the ans
    - [tail](https://math.stackexchange.com/questions/1707407/what-is-the-correct-term-for-the-destination-tail-vertex-of-a-directed-edge#comment3484741_1707407)
    - It shows how the 3 possibilities are available more strictly instead of just the above *theorical* proof by thinking of the subsets of the set consisting of all possibilities.
    - Also see 43 for the first 2 possibilities.
- [ ] 52
  - This just means [postorder](https://en.wikipedia.org/wiki/Tree_traversal#Post-order,_LRN) by "when the algorithm is *totally* finished with this vertex"
  - see the ans
    - similar to 48
    - > the children have increasing numbers from left to right
      so we need to assume
      > assuming that each *new* child added to the tree comes to the *right* of its siblings already in the tree
- [ ] 54
  Notice 53~56 I assume all graphs are connected since they doesn't use the term "spanning forest".
  - distance is $D(T_1,T_2)=|E(T_1)\setminus E(T_2)|+|E(T_2)\setminus E(T_1)|$
    then we are to prove $D(T_1,T_3)\le D(T_1,T_2)+D(T_2,T_3)$
    This is just to prove $|E(T_1)\setminus E(T_3)|\le |E(T_1)\setminus E(T_2)|+|E(T_2)\setminus E(T_3)|$
    By the veen diagram, $LHS=\overbrace{(E(T_1)\setminus E(T_3))\setminus E(T_2)}^{g(T_1,T_3)}+\overbrace{(E(T_1)\setminus E(T_3))\cap E(T_2)}^{f(T_1,T_3)}$
    and $RHS=\overbrace{(E(T_1)\setminus E(T_3))\setminus E(T_2)}^{\text{corresponds to }|E(T_1)\setminus E(T_2)|}+f(T_1,T_2)+\overbrace{E(T_2)\cap (E(T_1)\setminus E(T_3))}^{\text{corresponds to }|E(T_2)\setminus E(T_3)|}+g(T_2,T_3)$
    So we get $LHS\le RHS$
  - see the ans
    - It uses the total edge number of one tree is *fixed*.
      So
      > Suppose that T1 contains a edges that are not in T2 , so that the distance between T1 and T2 is 2a
    - > Now at worst the only edges that are in T1 and not in T3 are those a + b edges that are in T1 and not in T2 , or in T1 and T2 but not in T3 .
      LHS are those "in T1 and not in T3" either in T2 or not.
      this just means $b$ edges in "T2 but not in T3" are *all* in T1 and $a$ edges "in T1 and not in T2" are *all* not in T3 (so it will cause two zeroes in the veen diagram).
      - we can connect it with the above veen diagram. [See](https://www.overleaf.com/read/zjrkgqwhhkhw#086ace)
- [ ] 55
  - Based on the construction process of spanning trees (Notice since it is done by *making all circuits disappear* to make one more condition met when already connected, it must be able to list all spanning trees by choosing which edge to remove),
    $E(T_2)\setminus E(T_1)\subset E(G)\setminus E(T_1)$ where the latter are edges removed to erase all *circuits* which constructs the spanning tree.

    Then when $e_1$ is removed (by exercise 44, $e_1$ is not one cut edge), then we must ~~add~~ have one edge *sequence* $S(e_1)$ which has one edge 
    $w\in E(G)\setminus E(T_1)$ (if all in $E(T_1)$ then plus $e_1$ we have one circuit, so we must have one not in $E(T_1)$)
    - Here I only shows *at least* one edge $w$
      but doesn't know how to choose $e_2$ from these edges.
  - see the ans
    - > Then T2 ∪ {e1} contains a simple circuit C containing e1. 
      See [this](https://math.stackexchange.com/a/2783785/1059606) which is [based on 11.1 theorem 1](https://math.stackexchange.com/questions/2783749/adding-an-edge-to-a-tree-creates-a-cycle-is-my-proof-correct#comment10350833_2783785). <a name="one_cycle_when_tree_plus_one_edge"></a>
      - The added edge function as one edge in the created circuits,
        since in the original graph, "Any two vertices in a tree are connected by exactly one path", so only one cycle is created by concatenating $e$ and the unique $p(v_1,v_2)$.
        - Also [see][tree_iff_add_any_edge]
    - > The graph T1 − {e1} has two connected components
      - See [this][cut_edge_2_components]
        - The 1st paragraph is trivial due to 2 paths -> 1 circle as the reference in 11.1 theorem 1 says.
        - > Therefore, all vertices in $V_1$ are connected to each other in $G'$.
          because we can use `u` as the medium to connect all vertices like `w`.
        - Based on logic, $(V_1\cup V_2=V)\wedge (V_1\cap V_2=\varnothing)$
        - Here we use path definition [not implying distinct](https://en.wikipedia.org/wiki/Path_(graph_theory)#Walk,_trail,_and_path) (i.e. walk) as the book 10.4 definition 1
        - > This is a contradiction
          because $u$ and $v$ are already disconnected.
        - Here T' may mean G'.
        - This proof shows *explicitly* for the 2 components.
      - We can also prove this [more easily](https://qr.ae/pKdIbP)
        > adding an edge may connect two of them but it can't do anything for the third.
        so if 3 or more after the removal, there must be 2 or more components in the original, contradiction.
    - > $T2 \cup {e1}−{e2}$ is a tree, because e2 was on C.
      trivially $T2 \cup {e1}$ has only circuits having 
      $e_1$ (if not having, then remove $e_1$, we won't remove all circuit.)
      Also only 1 this type of circuit, otherwise we will have one circuit $C_1-\{e_1\}+C_2-\{e_1\}$ left.
      Then $T2 \cup {e1}−{e2}$ will remove this *only* circuit, so one spanning tree (trivially still connected for all vertices).
    - > Travel C from u in the direction opposite to e1 until you come to the first vertex in the same component as v
      ~~For $C\subset E(T_2)$, it either in ~~
      ~~$E(T_2)\cap E(T_1)$ or $E(T_2)\setminus E(T_1)$~~
      This is the process to choose $e_2$ and it meets the following properties:
      1. $e_2\in C\subset E(T_2)$
      2. Using the symbols in [cut_edge_2_components],
        $e_2=(a,b),a\in V_1,b\in V_2$
        Then this edge can connect two components trivially.
        - Since we start from $u$ we must encounter $k\in V_1$ in the former process.
          And since the endpoint has $v$, we must have one such $e_2$ (in the worst case when inner vertices are in $V_1$, at least we have $e_2=(pred(v),v)$). <a name="circuit_connect_components"></a>
      - Notice this process doesn't need the used *edges* in $C$ "until you come to the first vertex" to be also in $E(T_1)$, 
        it *only* needs used *vertices* are in $V_1$.
        So this process aims to splitting the *inner vertices* into 2 categories *instead of inner edges* and each category has at least one member (i.e. u,v in each), then traversing the path $C-\{e_1\}$ from u to v, we must get from one category to the other.
      - $T1 − {e1}\cap {e2}$ is connected and with $n-1$ edges after $\cap$ -> tree.
  - IMHO this problem can't be easily use "dually" to prove "T2 remains a spanning tree if e2 is removed from it and e1 is added to it" when having already proved "T1 remains a spanning tree if e1 is removed from it and e2 is added to it" although it is truly dual.
    More specifically, we got $f(e_1,T_1,T_2)=e_2$ when having $e_1$ be the condition.
    If we just prove by dual, we can only show there is one $f(e_2,T_2,T_1)$ with the swap property with 
    $e_2$. But we *can't show $f(e_2,T_2,T_1)=e_1$ easily* because the symmetric property.
- [ ] 58
  - > Certainly there is a directed path *from the root to every other vertex*, since we only deleted edges that allowed us to reach vertices we could already reach.
    - Here we [only needs "weakly connected"](https://math.stackexchange.com/questions/1356193/how-to-define-a-directed-spanning-tree#comment10351049_1360491) when directed graph.
    - "Euler circuit" trivially covers all vertices.
  - removing "previously visited" implies no something like backedges -> no "a simple circuit".
- [ ] 60
  - "if" part is trivial
  - based on 59 and [this](https://stackoverflow.com/questions/67343170/output-a-spanning-tree-given-a-directed-graph#comment137397264_77649096), maybe no spanning tree exists (i.e. Arborescence when directed)
    - ["only if"][directed_graph_detecting_cycle_proof]
  - see the ans
    - > vertex vk must have been visited before the processing of v1 is completed.
      this should be "$v_1$ ... $v_k$" based on "v1 is the first vertex visited"
    - This proof is more elegant than [directed_graph_detecting_cycle_proof] because it doesn't ~~need~~ prove the path from $v_1$ to $v_k$ in the tree to be in the target cycle. It only shows the existence O the backedge which is just what the code in geeksforgeeks does by `recStack[neighbour] == True`.
    - > Therefore v1 is an ancestor of vk in the tree
      $v_1$ has 3 types of choices for its first child (similarly also for the rest childs) (*):
      1. $v_k$ if possible (i.e. there is one edge $v_1\to v_k$).
        This proves the "ancestor" relation.
      2. branch out to other vertices not in the path ~~when at $v_i,i=1,\cdots,k-1$~~
         1. this branch can reach $v_k$ -> proves the "ancestor" relation.
         2. can't.
            - we will reach $v_i,i=2,\cdots,k-1$
              Then we can do the process (*) again.
            - no $v_i,i=2,\cdots,k-1$ is reached.
              Then we backtracks.
      - The above proof is a bit stuck.
        See [this](https://www.cse.cuhk.edu.hk/~taoyf/course/comp3506/ex/ex11-sol.pdf) which is same as [lec_14] without using the "parenthesis theorem" transforming the following case enumeration problem to one algebraic problem for the another proof based on [white_path_3_colors].
        - > Let v' be the *first* vertex on π—in the order from u to v—that is not a descendant of u. 
          This is one more strong assumption which directly have *many descendants* while the above doesn't than the above enumeration of cases to construct the recursive check.
          - Also the *color cases* are more easy to analyse than the above.
            e.g. in the book we assume $v_2$ is not one descendant, then when $v_1$ is gray, we reach $v_2$ in the process `for each u adjacent to v`. Based on the 3 color cases proved in the following, we conclude that $v_2$ is the descendant of $v_1$.
        - > Consider the moment before u' turns black. As u' is a descendant of u in the DFS forest, we know that u is in the stack currently
          - it implies u' is gray. 
            **Notice** the assumption moment which means the [subtree](https://math.stackexchange.com/a/4294404/1059606) of u' is to be finished.
          - i.e. u is gray (i.e. in the stack). (white: then ~~either~~ u' gray before processing u which implies u' is the ancestor of u ~~or black which implies u can't visit u' further then can't be the ancestor of u'~~. black: u has constructed all descendants, so u' can't be its descendant)
            because only u is gray we are constructing its descendants.
        - > which is a contradiction of the fact that u' is turning black
          i.e. u' is gray which is constructing its descendant.
          then v' is the descendant of u', transitively of u.
        - > On the other hand, if v' is either gray or black, it means that v must have been pushed into the stack while u still remains in the stack
          - "v' black while u gray" trivial.
          - "v' gray while u gray"
            > Suppose that when a vertex u is discovered, there is still a white path from u to a vertex v
            so u must become gray first. <a name="u_first_in_the_white_path"></a>
            So v' is the descendant of u
        - Connected with the book,
          > suppose that G contains a circuit v1, v2, . . . , vk, v1 , and without loss of generality, assume that v1 is the *first* vertex visited in the depth-first search process.
          this implies $v_1, v_2,\ldots, v_k$ is one white path.
- [ ] 61 
  - See [Detect_cycle_Directed_Graph] where "can't reach (only this we ~~may not~~ won't find ~~the~~ this cycle)" means in 60 "assume that v1 is the first vertex *visited*" can't be met.
  - >  not yet seen (the initial situation), seen (i.e., put into T) but not yet finished (i.e., visit(v) has not yet terminated), or finished (i.e., visit(v) has terminated).
    `T` corresponds to `recStack`.
    1. initial -> `visited=False`
    2. `visited[v] = True; recStack[v] = True`
      related with
      > whether the status of v is “seen.”
    3. `visited[v] = True; recStack[v] = False`
### 11.5
- 2~8,14~16,22(same as 20),29(same as 28),31(implied by 30 although the ans mistakenly inversed the sign) skipped
- [ ] 9
  - all weights same.
  - see the ans
    - a graph with 1 edge is impossible here because we have only one choice and we must choose this edge.
    - 2 edges: since connected we have only [one choice](https://houseofgraphs.org/graphs/32234) by [houseofgraphs_search] with "Number of Edges between 2 and 2" and "Connected"
      again to connect them we must choose these 2 edges.
    - 3 edges with [houseofgraphs_search] "Number of Edges = 3,Number of Vertices between 1 and 3,Connected" -> [only one](https://houseofgraphs.org/graphs/1374)
- [ ] 10
  - Prim’s will stop when no incident edges to choose (i.e. one component has been finished).
    Then choose one arbitrary un-visited vertex and apply the algorithm again.
  - Kruskal’s won't be influenced by components. Let $G(n)$ be the edge sequence chosen by without choosing the component first.
    - This is same as choosing component first and choose *smallest edge sequence* inside it. Let the edge sequence chosen by this method be $C(n)$
      ~~Because at the last, we are choosing $n-i$ edges ($i$ is the component count number) with *no circuits*.~~
      - Because for $G(n)$,
        trivially we can only select $n_i-1$ for $i$th component where $\sum n_i=n$ (If more than this, choose $n_i-1$ among these edges. Trivially it still has no circuits. Then based on 11.1 THEOREM 2, it is one tree. Then adding edges to this tree will construct circuits, contradiction).
        
        Assume for the $i$th component, we have chosen $v\in G_i(n),v\notin C_i(n)$ 
        (Here the subcript $i$ means it is the edge sequence in the $i$th component).
        Then trivially we must have selected the edge $w\in C_i(n)$ instead of 
        $v$ because it has one *smaller* weight by the process corresponding to $C_i(n)$, contradiction.
- [ ] 12
  - just change minimum to maximum in the corresponding locations of the algorithm.
    - Proof also just change minimum to maximum, which is enough, because the main part *doesn't depend on the "minimum" condition*.
      ~~See the [scratch][MST_scratch].~~ See 32.
- [x] 17
  - Similar to [second_shortest_path],
    edge number for the "spanning tree" are same, so there is "at least one edge difference".
- [x] 18
  - Assume there is one tree $T$ with no such "an edge with *smallest* weight", let it be $(u,v)$.
    then based on tree, $T$ has one path $p(u,v)$ which is not 
    $(u,v)$.
    then choose one edge $w$ in $p(u,v)$
    $T-\{w\}+\{(u,v)\}$ has one *smaller* weight sum with no circuit and $n-1$ edges -> tree, contradiction.
- [x] 20
  - Just use Kruskal’s algorithm
    where $e_1$ is fixed.
    Then the proof should be
    > with e1, e2, … , ek as its edges *$k\ge 1$*
    and the rest are same because in the inductive proof we don't care about the properties of $e_1$.
- [ ] 24
  - > Thus the circuit can be thought of as the sequence e1 , T1 , e2 , T2 , . . . , er , Tr , e1 
    it should be $p(T_1)$ which is the path in 
    $T_1$ connecting $e_{1,2}$
    - At the start, $T_1$ is just the single vertex which is [also one tree](https://cs.stackexchange.com/a/40335/161388) (TODO how "[disjoint union](https://en.wikipedia.org/wiki/Disjoint_union) of trees" works for (1)) because it is [connected](https://mathworld.wolfram.com/ConnectedGraph.html#:~:text=A%20connected%20graph%20is%20graph,is%20said%20to%20be%20disconnected.) and has no circuits.
  - > However, let e be the shortest edge (after tie-breaking) among {e1, e2, . . . , er}. Then the tree at both of its ends necessarily picked e to add to the tree, a contradiction.
    The *key* part is that the *ordering* of edges is [*asymmetric*](https://qr.ae/pKddbZ) think it similar to $<$.
    So each tree has one [deterministic](https://en.wikipedia.org/wiki/Nondeterministic_Turing_machine) choice (e.g. we can't have 2 smallest edges for 2 trees and each tree select one of them without overlapping)
- [ ] 26
  - Here the spanning tree must be constructed at one stage immediately before going to the next iteration of the `while` loop.
    - If not, this means we have $n-1$ edges when adding some edges among $e_i$ but not finished. (Here since no circuits by 24, we already has one tree.)
      Then continuing adding edges, we will have circuits, contradicting with 24.
- [ ] 27 see 26.
  - hinted by the ans: we also need to prove minimum based on 26.
    - Similar to the proof of Prim's,
      let the edge added be $e_{11},\cdots,e_{1 i_1},\cdots,e_{m1},\cdots,e_{m i_m}$ where 
      $m$ are the stage count (i.e. iteration to run the `while` loop in 26).
      Then let $T$ be the spanning tree corresponding to maximum edge number $k$ sharing $e_{11},\cdots,e_{1 i_1},\cdots,e_{b c}$
      Then use the same process to construct $T'$ having edges until 
      $e_{b i_b}$ or $e_{b+1 i_{b+1}}$ when $c=i_b$
      
      Then we need to *prove* the weight sum of the sequence $e_{t 1},\cdots,e_{t i_t},\text{where }t=b,b+1$.smaller than the substituted edge sequence $w_{1},\cdots,w_{t i_t}$
      Let the forest $G$ be edge sequence $e_{11},\cdots,e_{1 i_1},\cdots,e_{b-1 i_{b-1}}$ when $c\neq i_b$ 
      ($=b$ is similar.)
      Then $w_i$ and $e_{t m}$ must be edge connecting between trees (otherwise when connecting inside the tree, we will cause one circuit)
  - see the ans
    - Here $e$ should be assumed the first edge added among $S-T$ to ensure
      > where prior to that stage *all* edges in S are also in T
    - >  Find an edge e′ ∈ S − T and an edge e′′ ∈ T − S on this circuit and “adjacent” when viewing the trees of this stage as “supervertices.”
      it should be $e\in S-T$
      and let this edge be choosed by tree $T_m$ at this stage *by the algorithm*.
      trivially $T_m$ must have one edge incident with the rest vertices by connectivity. ~~This edge must be incident to one vertex $w\notin T_m$ (because no circuits), let the edge be $(w,v_{T_m})$~~
      ~~- Notice here $(w,v_{T_m})$ can be in ~~
        ~~$S$~~ (The strike-throughed contents may be a bit unnecessarily complex)
      - > viewing the trees of this stage as “supervertices.”
        At *"this stage" before adding $e$*
        trivially, S,T have edges in common which will construct one *forest* and each tree can be viewed as one vertex by contraction.
        > Find an edge e′ ∈ S − T
        Then let $e\in S-T$ connects $u,v$ (where $u,v$ are the tree vertices and $u=T_m$),
        > an edge e′′ ∈ T ... “adjacent”
        since T doesn't have $e$, we must have one edge $w=e''$ incident with $u$ (otherwise $u$ will one *disconnected vertex*)
        > an edge e′′ ∈ T ... on this circuit
        1. $w=(u,v)$ then by [this](#multi_edge_circuit), we have $w$ in circuit
        2. $w=(u,k),k\neq v$
          by connectivity, there is one edge $a=(k,v)$
          then the circuit is constructed by $w,a,e$ and the related paths inside each tree.
        - > an edge e′′ ∈ T − S
          Since $e\in S$ and we see $(e,w),w\in T$ will must cause one circuit based on these *shared* paths (notice the above $a$ and the paths inside the tree may differ but that doesn't influence the *existence of circuits*).
          so $w\notin S$.
      - > “adjacent”
        we have
        > Then by the algorithm, w(e′ ) ≤ w(e′′)
      - > an edge e′ ∈ S − T and an edge e′′ ∈ T − S
        is to ensure
        > closer to S
        and the validity of
        > T − {e′′}∪{e′}
      - ~~"an edge $e'' \in T − S$ on this circuit"~~
        1. it must be in $T$ because we are caring about $T+\{e\}$
        2. this circuit can't be in a tree $S$
        So there is one $e'' \in T − S$
      - "“supervertices" is implied by the contraction in [Boruvka_proof]
      - [“adjacent” edges](https://en.wikipedia.org/wiki/Edge_coloring#Definitions)
  - [Boruvka_proof] ([i.e. Sollin's algorithm](https://en.wikipedia.org/wiki/Bor%C5%AFvka%27s_algorithm)) in [this](https://www-student.cse.buffalo.edu/~atri/cse331/fall16/recitations/Recitation10.pdf)
    - > finally, eliminate the self-loops and multiple edges created by these contractions.
      This is impossible
      1. self-loop -> one unmarked edge $w$ connecting vertices $a,b$ in the tree with one path $p(a,b)$
        Then $w+p(a,b)$ is one circuit
      2. multiple edges <a name="multi_edge_circuit"></a>
        choose 2 be $a_1,b_1$ and $a_2,b_2$
        Then similar to 1, we have $p(a_i,b_i),\text{where }i=1,2$ (Here $a_1=a_2$ is possible, also for $b_{1,2}$)
      - So the above edges can't exist to construct one spanning *tree*
    - Lemma: ~~3.2~~ (which seems to prove complexity which I dropped because the basic idea is same for calculating complexity of all algorithms and I don't have time to check for each algorithm), 3.3 are same which means ["*acyclic* undirected graph"](https://en.wikipedia.org/wiki/Tree_(graph_theory))
    - "a Boruvka phase" i.e. `while` loop in 26
    - Lemma: 3.1
      here $(v,u)$ should be in the circuit including 
      $(v,w)$ otherwise we may disconnect the tree if $v$ has degree more than 2.
    - based on the above "must be edge connecting between trees ..." which implies
      > eliminate the self-loops
      we can [contract edges](https://en.wikipedia.org/wiki/Edge_contraction) making each tree as one vertex which simplifies the graph greatly.
      - More specifically, at each stage, we add edges to *connect trees* aiming to construct *one* spanning tree.
        Think of the following sequence: <a name="MST_construction_process"></a>
        1. original graph G, we must include contracted edges by lemma 3.1 for MST.
        2. "must be edge connecting between trees ..." -> we can contract as one vertex, i.e. tree.
        3. Use lemma 3.1 again, i.e. back to step 1. By 26, at the end we have one tree. By lemma 3.1， it is MST.
      - > In a contraction, *only the minimum weight* edge needs to be retained out of any set of multiple edges.
        This is implied by lemma 3.1.
    - > Each marked edge eliminate a distinct vertex of G
      this is implied by contraction which combines 2 vertices into 1.
      > thus the uncovered vertices are still remained in G’
      think it as relabeling one vertex (i.e. uncovered which means unremoved) and remove one vertex.
    - >  Furthermore, since the MST of G’ will also be induced by Boruvka phases, the MST of G’ is also a subgraph of the MST of G
      This is the **key part**. Also see the [above][MST_construction_process]
      At each stage, we will include those *necessary edges* by lemma 1 and generates [one graph minor](https://en.wikipedia.org/wiki/Graph_minor) G' by removing edges (implementation 4) unable in one spanning tree.
      - "induced" means generated
      - "subgraph" shows how we can generate the spanning tree by using all *contracted* edges.
  - This [proof][safe_edge_MST] is based on safe edges which is also referred to in CRLS.
    TODO randomization to linear.
- [x] 28
  - each edge is at most shared by 2 vertices.
    So "at least $\lceil n/2 \rceil$ edges" to cover all vertices.
- [x] 29
  - see the ans which is also based on the worst case as 28
    - > Each of the r trees is joined to at least one other tree by a new edge
      i.e. maybe 2 edges are incident with one same vertex, then at least 3 trees are contracted together.
    - > there are at most r/2 trees in the result
      when r is odd, it is $\lfloor r/2 \rfloor$ (also see 30)
      - > To accomplish this, we need to add r − (r∕2) = r∕2 edges
        since one edge [at most decreases one](https://cs.stackexchange.com/a/116850/161388) (also implied by [$G-e$](https://math.stackexchange.com/a/1497029/1059606) where ["path component"](https://proofwiki.org/wiki/Definition:Path_Component) is related with topological space) component (i.e. tree here), then to decrease at least $r-\lfloor r/2 \rfloor=\lceil r/2\rceil$ components, we need at least $\lceil r/2\rceil$ edges.
        - [In SCC we can decrease more](https://stackoverflow.com/questions/59199701/can-the-number-of-scc-strong-connected-component-be-increased-if-only-one-edg#comment137425421_60133937) due to the direction
        - similar to 30, we can also get $\lceil\rceil$ by "at least".
- [ ] 30 see the ans "at most" implies $\lfloor\rfloor$.
- [ ] 32 proves "Kruskal’s algorithm"
  - > Some edge e in this simple circuit is not in S
    Here we only need this to ensure $-\{e\}$ won't delete the edge among 
    $\{e_1,\cdots,e_k\}$ which is already shown in [primsproof]
    - ~~Compared with Prim's we *don't need it to be incident* with one edge among $\{e_1,\cdots,e_k\}$ (The book proof of prim's has one [too strong condition][Prim_find_incident_edge])~~
      ~~so the problem ~~
      This proof is almost same as Prims's 3rd proof (because these 2 algorithms are almost same) above where $S$ is one special case of $S_{k+1}$.
- [ ] 33
  - Assume we have one spanning tree $T$ which doesn't have $w$ which is the maximum weight edge in the circuit $C$.
    Then as exercise 11.4-56 shows, we can transform to one spanning tree $T'=T+\{w\}-\{e\},e\in C,e\neq w$ which must have one greater weight sum.
    This implies having $w$ won't construct one MST.
    - TODO the above process may not construct all spanning trees containing such one edge $w$.
  - see the ans
    - Here $uv$ is one cut edge,
      so by [cut_edge_2_components], we have can partition vertices into $V_{1,2}$.
      - > At some point this path must jump from the component of T−e containing u to the component of T−e containing v, say using edge f
        See [circuit_connect_components] and the related notice.
    - This is one variant of 11.4-55
      We are transforming the graph $T_1$ with the maximum edge $e_1$ to one graph $T'$ 
      without $e_1$ which may be not $T_2$.
      Since $e_2\in C$ where $C$ is *one circuit "containing e1"*, we are finished.
    - "smaller" to construct the contradiction with the assumption "minimum"
      implies we need "distinct edge weights" (at least for this used cycle).
- [ ] 35
  - > doing so does not disconnect the graph
    implies in ont circuit. So we can use 33.
  - > because the algorithm never disconnects the graph and upon termination there can be no more simple circuits
    We can also think as the following: This graph start with [edge number $\ge n-1$][minimum_edge_number_connected_graph] and decrease 1 edge one time, so must terminate with $n-1$ edges.
  - IMHO this is the reverse process of Kruskal's algorithm from the maximum weight to the minimum where both ends with no circuits.
### supplementary
- 12,20(same as 14,16 where the binomial tree is one special Sk-tree where "the child" is specified as "the leftmost child"),28,32,36 skipped
- [ ] 1
  See `git log -p` where I may assume cycle as the definition in wikipedia ensuring distinct vertices when reading mcs.
  - > the addition of an edge connecting two *nonadjacent* vertices
    based on "a simple graph", only "nonadjacent" is possible.
  - "only if" [see][one_cycle_when_tree_plus_one_edge]
  - "if"
    ~~if *any* edge added will cause~~
    Here if the graph is *disconnected* and only one edge is not added and it will cause the circuit but not connect all vertices with the original edges after added, then it is not one tree.
    - see the ans
      - The above is wrong because the question says *any* edge "connecting two nonadjacent vertices" which may be not in the original graph will cause the circuit.
        But as the ans says, disconnected graphs doesn't meet this requirement.
      - Same as [this](https://math.stackexchange.com/a/1118188/1059606) and [this which *proves exactly one*][tree_iff_add_any_edge]
        - the former is based on "disconnected" -> "components".
        - TODO [weirdly I say](https://math.stackexchange.com/questions/1118176/proving-if-g-has-no-cycles-but-by-adding-one-edge-between-any-two-vertices-wil?rq=1#comment10355422_1118188)
          > IMHO Here "do not cross each other" may mean "are not same" based on isomorphism.
        - The latter is trivial when assuming cycle, path as the definition in DMIA book since they have no distinct vertex/edge restriction.
          - Also trivial when not using the above assumption since cycle is based on path where both assuming distinct vertices.
      - [changing "tree" to "connected"](https://math.stackexchange.com/questions/325279/proving-a-simple-connected-graph-is-a-tree-if-adding-an-edge-between-two-existin?rq=1#comment10355421_325279), the theorem is still valid.
        - See this comment in comment_backup.md. This is one weird comment which has been deleted.
      - This edge must connect [already existing vertices](https://math.stackexchange.com/a/1663569/1059606) to make the theorem work.
        The following links are from [this](https://math.stackexchange.com/questions/1663565/adding-one-edge-to-a-tree-creates-exactly-one-cycle/1663569#comment3393226_1663565)
        - This [proof](https://math.stackexchange.com/a/1569078/1059606) doesn't explicit show exactly one but at least one.
        - [This proof](https://math.stackexchange.com/a/325283/1059606) hint *proves exactly one*
          See [the stared messages](https://chat.stackexchange.com/rooms/7833/discussion-between-andrew-salmon-and-dj) where in the image dashed edge is added although it is different from that hint says. Here "connect two vertices of" $C_3$ is impossible when assuming simple graph kept.
- [x] 2
  - By [nonisomorphic_simple_connected], it has 6 unrooted trees.
    - Same as [houseofgraphs_search] "Number of Vertices = 6,Connected,Acyclic"
      - 208: 3(path length)+1
      - 288: 4+1 simlar to the above
      - 334: by symmetry only consider the half, 1+1
      - 496: by symmetry 4 by dropping the half part of 2 points in the symmetric part
      - 568: by symmetry 3
      - 598: 2
      - So $4+5+2+4+3+2=20$
  - The number of rooted tree based on one unrooted tree is similar to chromatic number. But not same, for example, the [Cross Graph](https://houseofgraphs.org/graphs/208) has 2 different rooted trees when rooted at the center and the furthest vertex from the center while these 2 vertices can be colored same.
  - see the ans
    - > If they are both attached directly to the original path, then there are C(3 + 2 −1, 2) = 6 ways to attach them (since there are three possible points of attachment).
      This is [stars and bars](https://en.wikipedia.org/wiki/Stars_and_bars_(combinatorics)#Proofs_via_the_method_of_stars_and_bars) shown before.
      - Here no length-2 branches.
        same as
        > If there are not two disjoint paths of length 2 from the root, then there are 4 ways that the other 3 vertices can be attached to a given path of length 2 from the root
      - > hen there are 4 ways that the other 3 vertices can be attached to a given path of length 2 from the root
        is one special similar case $\binom{n+m-1}{m-1}=n+m-1=4,n=3,m=2$.
    - here disjoint paths should be edge disjoint (i.e. [not sharing edges](https://math.stackexchange.com/questions/641978/showing-equivalency-between-vertex-disjoint-and-edge-disjoint-path-problems-in-u#comment1353774_641978)) based on connectivity instead of [vertex disjoint](https://research.nii.ac.jp/~k_keniti/quaddp1.pdf).
    - Here $x$-height will necessitate $x$ edges in one path trivially because one edge at most increase the height by 1, then *$x+1$ vertices*.
      For the rest vertices $S$, the subsequence of them *can't be added* to the path such that the *longest* length from the root *increases*.
      We can manipulate the rest vertices one by one and the vertices except for the first are *either* connected with the long path or vertices already added from $S$.
- [ ] 4
  - i.e. $n-1$ leaves if rooted at the degree-$n-1$ vertex, so isomorphic to K1,n−1
  - see the ans which shows explicitly for the 2 parts.
- [ ] 6
  - Here we just use [Havel–Hakimi Theorem](https://math.stackexchange.com/a/3082170/1059606) (~~TODO I skips the proof since I don't have time to read all proofs of theorems I met and~~ this theorem is a bit intuitive at least for "if" part) to prove this can be a *simple graph*.
    - the key part is "In the second case".
      kw: 
      > change the graph ${\displaystyle G}$ so that ${\displaystyle S}$ is adjacent to ${\displaystyle T_{i}}$
      > we have two possibilities:
      - $W\neq T_i,D_j$ is by "another vertex ${\displaystyle W}$ be adjacent to ${\displaystyle T_{i}}$ and not ${\displaystyle D_{j}}$"
        $W\neq S$ is by "${\displaystyle S}$ is not adjacent to some vertex ${\displaystyle T_{i}}$"
      - > This modification preserves the degree sequence
        because each vertex degree decreases by one then increases by one.
        - This implies the *adjacency matrix* may be different for one degree sequence, i.e. different graphs. This is also implied by isomorphism checking methods which only use degree sequence as one *necessary instead of sufficient* condition.
      - simple graph
        1. A' -> A by adding one vertex must be simple otherwise the added vertex is already in A'.
        2. A->A' 
          - first case: remove one vertex, similar to 1.
          - second case: 
            - $t_i=d_j$ by relabeling, trivially a simple graph.
            - $t_i>d_j$
              since $\{\{S,T_i\},\{W,D_j\}\}\not\subseteq G$ -> no multiedge.
              loop trivially doesn't exist.
  - [See](https://math.stackexchange.com/a/732428/1059606) this which says we can use induction.
  - see the ans
    - > The problem is trivial if n ≤ 2, 
      $n=1$ -> singleton
      $n=2$ -> $1,1$ by postive.
    - since $d_n=1$ we just inductively add one leaf.
- [ ] 8
  - See [tree_level_recursive]
- [ ] 10
  - > Computer files can be accessed efficiently when B-trees are used to represent them
    [B+](https://stackoverflow.com/a/45324533/21294350) is better
    > increase the fanout factor (number of children), *reducing the height* of tree and, thus, *reducing the number of disk access* that we have to make in order to find a leave
    > pack more keys in the internal nodes in order to *fill up one disk* ... The more keys you pack in a node *the more children* it will point to
    
    [key](https://en.wikipedia.org/wiki/B-tree#Definition)
  - > its root has at least two and at most k children unless it is a leaf, 
    
    [See](https://en.wikipedia.org/wiki/B-tree#Definition) because maybe "fewer than L−1 elements"
    > and every internal vertex other than the root has at least ⌈k/2⌉, but no more than k, children
    
    because "two half-full nodes can be joined to make a legal node ..." See how this help [Insertion and deletion](https://en.wikipedia.org/wiki/B-tree#Insertion_and_deletion) 
    - > would have been in the middle *to the parent* node
      "middle" is implied by "separation values" in the definition of "key".
    - > if an internal node and its neighbor each have ${\displaystyle d}$ keys, then a key may be deleted from the internal node by combining it with its neighbor
      what if only one node goes to $d$? TODO
      > plus one more key brought down from the neighbor's parent
      This is also due to "separation values" to *order* these 2 combined nodes.
      - TODO
        See 11 what if the root has 2d, then no parent for the root based on "moving the key that would have been in the middle *to the parent node*".
        similarly the root has no neighbors, so delete has problems.
- [ ] 11
  - Similar to [this][graph_based_on_explored_set_complexity]
    By [tree_level_recursive] choose for each level based on root/Internal.
    upper bound when complete k-ary tree so $k^h$
    lower bound $2\cdot \lceil k/2\rceil^{h-1}$
- [ ] 14
  - binomial trees seems to occur in older exercises.
- [x] 16
  - see the ans
    - "the basis step" is [$\binom{0}{0}=1$](https://math.stackexchange.com/a/2020891/1059606)
    - > This holds for j = k as well, and at the 0th level, too
      j=k: $C(k+1,k+1)=0+C(k,k)=1$
      at the 0th level: trivially one root.
- [x] 18
  - We can only use the hypothesis as the exercise "the vertex of largest degree in Bk is the root" which is enough.
    because each time we *only adds one degree* to the root and the other endpoint, so the root keeps "the vertex of largest degree".
- [x] 21
  - trivial by induction
  - see the ans
    - > The result is trivial for k = 0.
      here no $T_{k-1}$ since $k-1<0$
      so only one single $v$.
    - > the parent tree
      one tree having the same root as $T$
- [ ] 24
  - we just check the *path* as 11.3.2 says.
    1. all addresses are distinct.
    2. each index $x_i$ at level $i$ has $x_i\le k_i$.
  - see the ans
    - we need also check "prefix" as 11.2.4 says.
    - > we check that there is an address in the list with prefix a1:a2: · · · :ai−1:b.
      TODO this seems to include all internal vertices which is weird.
- [ ] 26
  - if no edges "in common"
    This means when removing the cut set, we can still construct one spanning tree.
    But the graph is already disconnected, contradiction.
  - see the ans
    - > If it is not, then the statement is *vacuously true*.
      think the exercise as "a graph" has "a cut set" -> "at least one edge in common with any spanning tree of this graph".
      Then the cut set is $\varnothing$, so F(alse).
- [x] 30
  - assume it is not one cactus
    then there are at least 2 circuits sharing one edge sequence $p(a)$, let its edge number be 
    $a$.
    Let the 1st circuit be $p(a)+p(b)$ and the 2nd be 
    $p(a)+p(c)$.
    Then $p(b)+p(c)$ is also odd.
    summing up all 3 circuit edge number we get $2(\sum_{k=a,b,c} p(k))$ is odd, but that is impossible.
- [ ] 34
  - start from the root
    it has at most 2 children
    either 2 or 1 child of the root, each child has only one child.
    Then recursively until we have $n-1$ edges, we construct one Hamilton path.
  - [This](https://math.stackexchange.com/a/3112861/1059606)
    "it is connected and has no vertices of degree greater than 2" -> "a path".
    - [relation](https://math.stackexchange.com/questions/3112683/proving-that-graph-g-is-a-path#comment10357165_3112683) with this exercise
    - "We know that ..." is one recursive process which will always include one *new* vertex $u_i$ due to acyclic.
    - > there cannot be any other vertices
      otherwise degree will maybe be 3.
    - This proof is very similar to the above construction process.
- [ ] 35
  - By viewing the ans, since the maximum difference is $n-1$ and the minimum difference is $1$, so probably we can assign these $n-1$ numbers to $n-1$ edges
    - It is the ["the Graceful Tree Conjecture (GTC)"](https://prideout.net/blog/graceful/)
- [ ] 38
  - a) trivially, $n$ must be adjacent to $1$ because it is the only choice for $n-1$.
    then by trial, $1-n-2-(n-1)-\cdots-\lfloor n/2\rfloor-\lceil n/2\rceil$ (The last 2 may be same).
    - TODO by this we may choose starting labeling one longest path by DFS for GTC.
  - see the ans
    - Here a) has the ending $\lceil n/2\rceil$ and $\lceil n/2\rceil+1$ because
      1. n is even. 
        Each part has the same size. so $\lceil n/2\rceil=n/2$
      2. n is odd.
        the middle one $\frac{n+1}{2}=\lceil n/2\rceil$ will be chosen by only one part.
        since $1$ starts first, so this number will be chosen by that part including $1$.
    - b)
      let the spine be with $k$ vertices.
      The $i$th vertex has $p_i$ adjacent vertices.
      ```
          1---------------------(n-p_1)-------------------2+p_2
         / \                      / \
        /   \                    /   \
       /     \                  /     \  
      n ... n-(p_1-1)          2       2+p_2-1
      ```
      the difference sequence from left to right is $n-1,n-2,\cdots,1$ with decreasing step 1 and decreases $n-2$ times due to $n-1$ edges.
      - relation with a)
        pay attention to the long path, it is one variable-step sequence similar to the alternating sequence but the sign is substituted by the relation of greater or smaller.
- [ ] 40
  - Since the [DFS implies preorder][backtracking_AND_DFS_imply_preorder] which always has the root preceding its children.
    - The above *doesn't consider* this is one directed graph, so not necessarily preorder as [DFS_directed_topological_sorting] shows where 4 precedes 1 but it is in *one separate tree* which causes it is visited at last.
    - As [this blog](https://eli.thegreenplace.net/2015/directed-graph-traversal-orderings-and-applications-to-data-flow-analysis/) shows
      > we have pre-order, which visits a node *before recursing into its children*;
      > However, for directed graphs, these orderings are not as natural and *slightly different* definitions are used.
      > Whereas in trees, we may assume that in pre-order traversal we always see a node before all its successors, this *isn't true for graph pre-order*.

      preorder *differs* for undirected and directed graphs.
      - Same as [this](https://qr.ae/pKLl8G)
        > preorder might visit one of the two parents first, and then visit the child before visiting the other parent.
      - Also implied in [backtracking_AND_DFS_imply_preorder] which is used in the code of [DFS_directed_topological_sorting]
        > **Reverse postordering** produces a topological sorting of any directed acyclic graph
    - Notice here we should use [this preorder definition][backtracking_AND_DFS_imply_preorder] as the [notice](https://en.wikipedia.org/wiki/Preorder#) before (Top) of wikipedia preorder shows.
  - Kahn’s Algorithm based on BFS
    - [proof][kahn_proof]
      - p6 the in-degree 0 vertex can be safely output earlier to ensure one Topological Sort because there are *no parents* of them.
        - > Remove all its outgoing edges ;
          to avoid removed vertices *influencing* the rest graph.
      - always at least one in-degree 0 vertex in the *induced* graph
        - [detailed proof](https://math.stackexchange.com/a/3232355/1059606) (same as [this](https://math.stackexchange.com/a/1196995/1059606) to prove at least one *source* vertex) where *finite* is assumed by the real-life problems which is same as p8
          it is reversing back up to one of the parent recursively constructing one cycle.
        - This can be used to [check cycles](https://www.geeksforgeeks.org/detect-cycle-in-a-directed-graph-using-bfs/)
          ~~since for one directed graph, cyclic -> recursively have "at least one in-degree 0 vertex" (This is one *necessary* condition although we can use ).~~
      - It also proves DFS's method to find one Topological Sort which is based on [lec_13_parenthesis_theorem].
        - here "neighbors" of $u$ means $u$ has edges *to* these neighbors.
        - kw: shall show $f(v)<f(u)$, two cases
          where "(u,v) be an edge" is one arbitrary edge.
  - see the ans
    - > in order of their finishing.
      implies postorder is the finishing order which is also shown in [kahn_proof]
    - > Clearly this is true if uv is a tree edge
      > if uv is a forward edge
      case 1 in [kahn_proof]
    - > consistent with our given partial order
      because we only needs ensuring ancestors before descendants.
    - > then v is in a previously visited subtree
      case 2 in [kahn_proof]
- [x] 41
  - see [Boruvka_proof] which is stronger to say *each MST must* contain this minimum edge.
- [ ] 42
  - This is related with 10.4-65 but ~~more general~~ ~~which needs one model instead of only one solution.~~ with *jealous wives* and 3 pairs.
  - see the ans
    - It draws the whole graph and uses Dijkstra’s algorithm.
    - It brings X,x,z,Y,y,Z almost alternatively in order to the other bank.
- [ ] 43
  - This is related with 41.
    see [Boruvka_proof].
- [ ] 44
  - based on 34, this is one Hamilton path.
  - a)
    So for $\triangle bcd$ we can only choose one 1 and one 2.
    For abef (three 2s are impossible), we delete ab or be and we choose the greater one be to delete.
    So $e-f-a-b-d-c$
  - b)
    we must choose ab
    - if choosing 1 incident with b, then 5,2,4 incident with b are removed. but choose one from 2,6,2 incident with g will make the graph disconnected.
      by symmetry we can't choose 4 incident with b as well.
      - Then we choose 2 incident with b, then remove 5,1,4.
        - For $\triangle efg$ we choose 4,2.
          (If choose 5 incident with b, similarly we choose 4,2 for $\triangle efg$. This path choice has the greater weight sum than the former.)
  - Tree can be one Hamiltonian path [only when $P_n$](https://math.stackexchange.com/a/2927153/1059606)
  - Since The Hamiltonian path problem is one [NP-complete problem](https://en.wikipedia.org/wiki/Hamiltonian_path_problem#), I didn't dig into one algorithm related.
  - see the ans
    - > Since b is a *cut vertex* we must include ...
      Here it splits the graph into 2 components, so we need 1 edge to connect to each component induced.
      - This is more elegant than the above.
    - b) is same as the above.
- [ ] 46
  - Also see 11.4-60
  - "only if" is trivial
  - "if" is the definition.
  - see the ans
    - use DFS for the "spanning tree"
      where we use [weakly connected](https://math.stackexchange.com/questions/1356193/how-to-define-a-directed-spanning-tree/1360491#comment10351049_1360491) to [ensure][DFS_construct_tree] by 11.4 theorem 1 we can have one spanning tree.
- [ ] 47
  - This is similar to [scc] but the latter uses DFS for each (connected) component while the former uses BFS.
## 12
### 12.1
- 2~28(20 where checks for all possible cases of LHS),30,31($2^{2^{n-1}}=2^4=16,n=3$),34([Juxtaposition](https://en.wikipedia.org/wiki/Juxtaposition#Mathematics)),40 skipped
- [ ] 29
  - we can also use $\Pi x_i=\overline{\sum \overline{x_i}}$ where 
    $x_i$ may be vacuously true or false (Then only all $x_i$ are 1 LHS will be 1, similarly for RHS).
    here $\Pi,\sum$ are all sum or multiplication related with Boolean algebra.
  - see the ans
    - [De Morgan's laws](https://en.wikipedia.org/wiki/De_Morgan%27s_laws)
      Here all operations in Boolean expressions in p849 are contained.
      - When we do $\neg$ again for both sides of ${\displaystyle \neg (P\lor Q)\iff (\neg P)\land (\neg Q)}$. we have the exercise form where F has only 
      $\land$.
        - If F has *both* $\lor$ and $\land$, we can manipulate 2 minimum operands at one time and continue until all operators are manipulated.
    - Better see [this detailed proof](https://math.stackexchange.com/a/2586662/1059606) where the contents before "CLAIM" is to show "the recursive definition of statements" which is used for the proof
      then each statement can be splitted into 1 or 2 parts so we can use "De Morgan's laws".

      definition_1 which is ~~same as this exercise by $\neg$ both sides again where $F^d=\neg \varphi'$.~~ ~~different from this exercise which takes 2 negations for different objects.~~ related with this exercise since it proves $F^d'(\overline{x_1},\ldots,\overline{x_n})=\overline{F(x_1,\ldots,x_n)}$ where $F^d'$ only swaps operators but doesn't swap 0 and 1.
      > The dual $φ$' of $φ$ is the formula obtained from $φ$ by replacing all occurrences of $∧$ by $∨$, of $∨$ by $∧$, and all propositional variables by their negations. Show that $φ$' is logically equivalent to $¬φ$.
      - This also shows why Duality Principle can be [rephrased](https://www.cs.ucr.edu/~ehwang/courses/cs120a/00winter/boolean.pdf) ~~different from~~ similar to this exercise (considering 0 and 1 while this exercise doesn't for LHS *explicitly* because De Morgan's laws doesn't consider it, ~~e.g. $F^d=x\cdot 0=\overline{\overline{x}+\overline{0}}$~~ e.g. if $F(x,0)=x+0$, then we want $F^d(x,0)=x\cdot 1$ but RHS is $\overline{F(\overline{x},\overline{0})}=\overline{\overline{x}+\overline{0}}$ and De Morgan's laws will get RHS to be $\overline{\overline{x}+\overline{1}}$) and same as 12.1.4
        > any algebraic equality derived from these axioms will still be valid whenever the *OR and AND* operators, and identity elements *0 and 1*, have been *interchanged*
        e.g. in 12.1 TABLE 5
        $\varphi:x+x=x$ will become $\neg \varphi \overline{x}\cdot \overline{x}=\overline{x}$
        but we can substitute $\overline{x}$ with $x$ and get $x\cdot x=x$

        similarly $x+0=x$ -> $\overline{x}\cdot 1=\overline{x}$, i.e. $x\cdot 1=x$
        - in sum, we can substitute $\overline{x}$ with $x$
          so we only need to interchange 0 and 1 but not interchange $x$ and $\overline{x}$
- [ ] 32
  - see the ans
    - enumeration and use transitive property of $=$.
- [ ] 35~42
  - [ ] 35
    1. $0\lor 0=0$ by Identity laws
      $1\lor 1$
    - see the ans
  - [ ] 36 see the ans
  - [ ] 37 use 36 and see the ans for the detailed.
  - [ ] 38 see the ans which thinks $\overline{x}$ as one variable.
  - [x] 39
    $(x\lor y)\land(\overline{x}\land\overline{y})=((x\lor y)\land\overline{x})\land\overline{y}=((x\land \overline{x})\lor(y\land \overline{x}))\land \overline{y}=(y\land \overline{x})\land \overline{y}=0\land \overline{x}=0$
    others related with 36 are similar.
  - [ ] 41
    - we can also exclude the other 3 possibilities and verify the only left to prove.
  - [ ] 42 same as 29 using De Morgan’s laws by 39.
    - see the ans which is based on since the *initial conditions are dual*, so all the induced identities are also dual.
- [ ] 43
  - See [this][lattice_boolean_algebra]
  - see the ans
    - 9-supplementary-41 shows identity where c),d) can be proved by dual here.
### 12.2
- 2~16(10 is dual of the [Disjunctive Normal Form](https://mathworld.wolfram.com/DisjunctiveNormalForm.html),14 also see the above 12.2 and c) can prove based on a) which then RHS equals $\overline{\overline{x}\overline{y}}$, 15 is similar to 14) skipped
- [x] 19
  - based on "idempotent laws", we can only get $x$ when $x+x$ and $x\cdot x$
- [ ] 20
  - ~~$x\oplus 0=\overline{x}$~~ $x\oplus 1=\overline{x}$
  - see the ans
    - a) shows one counterexample.
    - b) XOR operator is associative proof by [conditional flip](https://math.stackexchange.com/a/1534362/1059606) or [addition modulo 2](https://math.stackexchange.com/questions/293793/prove-xor-is-commutative-and-associative#comment9452408_293793) whose associativity can be proved [using](https://proofwiki.org/wiki/Modulo_Addition_is_Associative) [residue class $[x]_m$](https://proofwiki.org/wiki/Definition:Modulo_Addition) (i.e. [transformed](https://math.stackexchange.com/a/3563774/1059606) to $a+b+c$) <a name="xor_associative"></a>
      - > every expression involving these two operations and x and y can be reduced to an XORof the literals x, x, y , and y.
        here we can *use parentheses based on "associative"* to construct many pairs and manipulate each pair one by one which generalized one pair to any expression.
        
        For each pair, it either has $\overline$ for both variables or not
        then each variable has $\overline$ or not. (Here only $\oplus$ is one 2-ary operator.)
        So we have
        > an XORof the literals x, x, y , and y
        - Then based on "an XORof the literals x, x, y , and y", we only focus on one pair.
          > since x ⊕x = 0 , x ⊕x = 1 , x ⊕1 = x and x ⊕0 = x
          we care about the possible cases with 0,1 and only x or y.which will enumerate *all possible pairs* when doing xor pair by pair.
        - Since each term of $\oplus$ has 6 choices, i.e. $1,0,x,y,\overline{x},\overline{y}$.
          we have $6\cdot 6/2=18$ choices if considering symmetry.
          Then since $\overline{x}\oplus\overline{x},\overline{x}\oplus 1,\overline{x}\oplus 0$ and
          the corresponding $\overline{y}$ version are not considered, so 
          $18-3\cdot 2=12$ needs to be considered as the answer shows $4+4+4$.
      - > Since none of these has the same table of values as x + y
        because none has 3 ones or zeroes.
        - Also see [this](https://math.stackexchange.com/a/3331501/1059606) although it is a bit out of the range to the logic.
### 12.3
- 2~10,12,17~18(implied in 15~16) skipped
- [ ] 11 see the ans
  - TODO this seems to be covered in COD/[asm_doc] with one more complex example.
  - here $d=x-(y+d_i)$
    1. x=1,$y+d_i=0$ corresponds to the first 2 cases of the ans.
    2. x=0 ...
  - $b_{i+1}=x<y+d_i$
- [x] 13
  - $x_1\overline{y_1}+\overline{x_1\oplus y_1}x_0\overline{y_0}$
- [ ] 14 see the ans
  Here we think for each bit
  1. summand cases ($n$ summands -> $2^n$ cases)
  2. carry cases (whether or not)
  - Use the same rules as decimal
    ```
      11
    x 11
    ----
      11
     11
    ----
    1001
    ```
  - $s_1=1$ 
    ```
            x_1 x_0
          * y_1 y_0
    ---------------
            x_1 x_0 if y_0=1
        x_1 x_0     if y_1=1
    ---------------
    s_3 s_2 s_1 s_0
    ```
    we need $x_1\oplus x_0=1$ because the rightmost $x_0$ *can't carry*.
    when $x_1=1,x_0=0\Rightarrow y_0=1,y_1=0/1$, so we *at least have one zero* for $x_i,y_i$ when $x_1 y_0=1$.
    - $s_2=1\Rightarrow x_1 y_1=1$ and $x_0,y_0=0$ to avoid both $x_1,x_0=1$ which are sumed up to *carry*. see the ans
      - Here if $x_1=0$, then the middle $x_1 + x_0$ which equals $x_0$ at most can't carry so this case can't make $s_2=1$.
- [ ] 15 a)~c) have been said in 12.2
  - TODO how to prove using the minimal gates for 15,16?
  - d) $x\oplus y=x\overline{y}+\overline{x}y$ Then we can construct it using a)~c)
  - see the ans
    - d) is simpler than the above.
      it uses $w=\overline{x}\vert y=\overline{\overline{x}y}$
      then $u=\overline{x}+y$
      then $u\vert w=\overline{u}+\overline{w}=\overline{\overline{\overline{x}y}}+\overline{\overline{x\overline{y}}}=\overline{x}y+x\overline{y}$
- [ ] 16 d) see the ans which excludes all ones based on $x+y$.
  - Notice since here LHS has no 0,1 so we can use the formula of 12.1-29
    - 15-a) here dual of $\overline{x}$ is $\overline{x}$
      - dual of $x\vert y=overline{xy}$
        (see 12.1-29): $x\downarrow y=overline{x+y}$ -(Formula of 12.1-29)> $\overline{\overline{\overline{x}\overline{y}}}=\overline{x}\overline{y}$
        Then $x\downarrow x=\overline{x}\overline{x}=\overline{x}$
    - 16-d) 
      dual of $x\oplus y=x\overline{y}+\overline{x}y$ is $(x+\overline{y})(\overline{x}+y)=\overline{x}\overline{y}+xy$
      so we should calculate $x\oplus \overline{y}$ of 16-d) to get 
      $x\oplus y$ for 15-d)
      - take the dual for LHS $x\oplus \overline{y}$
        then the dual of RHS becomes $x\overline{y}+\overline{x+\overline{y}}=x\overline{y}+\overline{x}y$ which is just the above definition of $\oplus$ ...
        Use Formula of 12.1-29, RHS becomes $\overline{(\overline{x}+y)\overline{(\overline{x}y)}}=\overline{(\overline{x}+y)(x+\overline{y})}=\overline{\overline{x\overline{y}}\overline{\overline{x}y}}$ (notice the last step we stop expanding because it already has one outer NAND which is similar to the ans here where we add one outer NOR at the 2nd equal sign because we have one 
        $+$ already)
- [x] 19
  - $x_3c_1c_0+\ldots$
- [ ] 20
  - this depth is related with the delay as [full_adder] says.
### 12.4
- 2~12(10 see 10.5-FIGURE 14),16,22(because most are similar) skipped
- [ ] 14
  - see the ans
    - a) we have 4 essential prime implicants
    - b) we have 3 implicants which can't be groups with all 4 directions.
    - c,d) similar to a)
- [x] 18
  - > the first and fourth columns ...
    because 4 directions at most give 4 minterms with one literal difference
    so we need *one more*.
- [ ] 20
  Assume the binary code is $x_n\cdots x_0$
  - a) $x_0$
  - b) $$
  - c) $\neg (4\lor 5\lor 6)$
  - see the ans
    - TODO the ANS seems to be wrong with `d`
    - Here the ans assumes 4 variables with code $wxyz$ but the exercise doesn't (same for the 7th).
    - a)
      should be
      $$
      \begin{matrix}
        1&0&0&1\\
        1&0&0&1\\
        1&0&0&1\\
        1&0&0&1\\
      \end{matrix}
      $$
    - b)
      it should have 0 for $0000,0011,0110,1001,1100,1111$
      $$
      \begin{matrix}
        0&1&0&1\\
        1&1&1&0\\
        0&1&0&1\\
        1&0&1&1\\
      \end{matrix}
      $$
      The above will make $x\overline{y},xz$ fail.
      - [See](https://www.overleaf.com/read/sjjtkcdxcdzb#a34bc3)
    - c)
      it should add $+w$ TODO
- [x] 21
  - let it be $\overline{x}\overline{x}xyz$
    then $xyz=110,010,011,001$
    i.e. $y\overline{z}+\overline{x}z$
  - see the ans
    - This is not minimum
    - the above 2 gates in the ans corresponds to the above latter 3 implicants
      and the bottom gate -> 110
- [ ] 22 see the ans
  - a) all 3 are essential
  - b,c) same as a)
  - d) 2 prime implicants cover the rest 1
- [ ] 24
  - a) see the ans highlighted
  - b) here 
    1. using only one 2-literal block, we need one 3-literal block.
      although block num is same, 2-literal blocks use less literals
    2. using no 2-literal block, then we need $\lceil 5/2\rceil=3$ blocks which is worse.
  - c)
    here 2 3-literal blocks including $\overline{w}xyz,w\overline{x}yz$ are essential.
    then the rest 1-literal block is fine to fill in the rest.
- [ ] 26 [see](https://en.wikipedia.org/wiki/Karnaugh_map#Inverse) where $A\lor B$ corresponds the gray bar and others are similar.
- [ ] 30 see the ans
  - Here 2 is minimum since $\lceil 10/4\rceil=3$ if not using the 1-literal block.
  - see the ans
    - The above tries to include all `d` which is not necessary
    - Here 1 block is impossible
- [ ] 32 see the ans
- [ ] 33 implied by how $Q_n$ is defined recursively.
  - see the ans
    - > the Cartesian product of that subcube with the line segment [0, 1]
      "[0, 1]" corresponds to $x_{n+1}$ because 
      "$x_{n+1}$ (or its complement) is not part of the product"
### supplementary
- 14,18(see [xor_associative]. 1. Then $LHS=(y \oplus \overline{x})\oplus x=y\oplus(\overline{x}\oplus x)$ 2. based on 1, for b, 
  LHS=$(\overline{y}\oplus z)\oplus(\overline{y}\oplus \overline{z})=0\oplus 1=1$),20 skipped
- [x] 2
  - a,b) not (d,e similar to them)
  - c)
- [ ] 4 see the ans
- [x] 5 
  - there are $2^{n-1}$ pairs of 
    $((x_1,\cdots,x_n),(\overline{x_1},\cdots,\overline{x_n}))$
    each pair has 2 possibility value $0/1$
- [x] 6
  - Here $F\le G$ means G *includes all ones* in F
- [ ] 8
  - Use $F+G=1\Rightarrow F=1\lor G=1$
  - see the ans
    - Better use $\Leftrightarrow$
- [x] 9
  - Antisymmetry: $F\le G,G\le F$ means they have the same set of 1
    so they are same.
  - others are trivial
- [ ] 10 see the ans
  - 4-cube because each can *inverse one of 4* variables to get the adjacent set member which means it is $Q_4$.
    where $1\to 0$ will decrease the level and $0\to 1$ will increase.
    - > with two vertices adjacent when their subsets *differ in a single* element
      [construction](https://en.wikipedia.org/wiki/Hypercube_graph) same as the book says before.
- [x] 11
  - a) to test $\overline{x\overline{yz}}=\overline{\overline{xy}z}$
    (1,0,0) is one counterexample.
  - b) (1,x,x) LHS=$\overline{x+\overline{y+z}}=0$
    RHS=$\overline{\overline{x+y}+\overline{x+z}}=1$
  - c) same as b) (1,x,x)
- [x] 12 trivial
  - [XNOR](https://en.wikipedia.org/wiki/Circled_dot#Mathematics)
- [ ] 16
  - see 12.2-20 where $\oplus$ with one of $+,\cdot,\overline{}$ are all not functionally complete
    so based on 13, $\odot$ is not functionally complete.
  - see the ans
    - It is same as [this](https://copyprogramming.com/howto/functionally-complete-operations#how-to-determine-if-given-function-is-functionally-complete)
      > Determining if a given boolean function can *produce the negation* is a straightforward task
      i.e. if not, then we find *one counterexample* that it can't realize the $\neg$ function.
    - To prove *functionally incomplete*
      1. > has a property that not all truth functions do
        [see](https://math.stackexchange.com/a/2629618/1059606)
        > You cannot construct formulas with more than one variable.
        - Or find one truth table it can't form like [all falses](https://math.stackexchange.com/a/1481631/1059606) and [odd ones](https://math.stackexchange.com/a/2173070/1059606) which is used before.
- [ ] 17
  - [See](https://gateoverflow.in/18849/many-%2416%24-boolean-functions-variables-represented-using-only?show=18895#a18895)
    - a) since $\neg$ is one unary operator
      there are $2\cdot=8$ possibilities but $\overline{0/1}=1/0$ 
      so 8-2=6 possibilities
    - b) ~~since 2-ary, for each location we have 5 possibilities including $\varnothing$~~
      ~~based on symmetry, we have $\binom{5}{2}+5=10$ possibilities~~
      1. using one variable, 4
      2. using 2 variables, 
        x.x = x, x.1 = x, x.0 = 0 and x.y
        y.y = y, y.1,y.0 without y.x based on symmetry (WLOG based on x)
        1.1,1.0 (duplicate of 1,0)
        0.0 ...
      - Based on *idempotence* when using $+$ multiple times, the possibilities don't increase.
        Same for a),c).
    - c) duality by $\cdot\Leftrightarrow +,0\Leftrightarrow 1$ won't increase possibilities
    - d) 
      - Here maybe related with closed set TODO
  - We can also [enumerate](https://gateoverflow.in/18849/many-%2416%24-boolean-functions-variables-represented-using-only?show=18898#a18898)
- [ ] 22
  - see the ans
    - a~e) are trivial because only 4 possibilities.
    - f~g) we only need to ensure the *2 cases are met* where for example for
      f) "either x = 1 or y = z = 1" and the complement $x=0\wedge \neg(y=z=1)$ where trivially at most be 
      $1< \frac{3}{2}$ is also met.
    - h) here $w=y=1 \sum w_i x_i=2$ doesn't meet the threshold
      ~~here when $x=z=1$, $w=y=0$ has the same weight sum as ~~
      Since we need to exclude $w=0,y=1$ ($2-\frac{1}{2}$) we can set the threshold to be $2-\frac{1}{4}=\frac{7}{4}$.
      - Then if $x,z$ are not all ones, then at most $1+\frac{1}{2}<\frac{7}{4}$
        so $x,z$ must be all ones,
        Then use the above exclusion for the rest proof.
- [ ] 23
  - no solution for linear equations
    $$
    \begin{bmatrix}
      0&0\\
      0&1\\
      1&0\\
      1&1\\
    \end{bmatrix}
    \begin{bmatrix}
      w_1\\
      w_2
    \end{bmatrix}
    =
    \begin{bmatrix}
      0\\
      1\\
      1\\
      0\\
    \end{bmatrix}
    $$
  - see the ans
    - The above should be based on inequity instead of the equation.
- [ ] 24
  - see the ans which is one algebraic problem.
## 13
### 13.1
- 2,8~10(1. see the above 13.1 2. Here "Conversely" means from all strings $0^n 1^m$ to the all grammar production sequences where the original direction is from all production sequences to $0^n 1^m$ 3. Here when S disappears, $G_1$ stops while $G_2$ can't increase 0's) skipped
- [ ] 4 see the ans
  - c) here we *must make S disappear* by $S\to 00A$ while $S\to 1S$ will generate many 1's
    similarly many 0's by $A\to 0A$ and make A disappear by $A\to 0$.
- [ ] 6
  - c) here $A \to aB, A \to ab, B \to b$ can be combined into $A \to ab,B \to b$.
- [ ] 12 
  see the ans where implies using $S\to 0SAB,S\to \lambda$ 
  instead of $S \to C, C \to 0CAB, S \to \lambda$
  - similar to 10, if S doesn't disappear, rule 5~8 can't be used.
    so we should do as the following steps:
    1. make S disappear
    2. exchange AB because $2A$ will be stuck
    3. then rule 5~8 make $A\ldots AB\ldots B$ become $0\ldots 0 1\ldots 1$
  - how $012$ is generated? TODO
    Here maybe we need $C\to \lambda$ based on $C\to 0CAB$ to make the above possible.
  - > the number of 0’s, A’s, and B’s must be equal at the point at which S disappears with all the 0’s on the left (where they must stay)
    because trivially $(0,1,2)\Leftrightarrow (A,B,C)$
    and $C\to 0CAB$ ensures the $0$ location.
  - It proves
    1. 0,1,2 number same
    2. 0,1,2 locations are right.
    - As 11 shows 
      we can decide $n$ by choose $S$ disappear at which step.
      Here most of steps are determinant
      - $S \to 0SAB$ is determinant if we keep S (i.e. exclude $S\to \lambda$) 
        then $\to 00SABAB$ is determinant because 0S,SA,AB all can't be transformed.
        - Then we can *either transform $BA$ earlier or not*.
          Assume not and we *terminate S here*.
          Then $\to 00ABAB$
          - If we keep not terminating S,
            then we can *only* transform $BA$.
        - Assume transform $BA$ here
          - if not transform $BA$
            then we can only transform $0A$ i.e. $\to 001BAB$
            - ~~similarly if not transforming $BA$, $\to 0012AB$~~ (we are *stuck here*)
              This implies
              > therefore the *only* way to get rid of the A’s is for them all to *move to the left of the B’s* and then turn into 1’s.
              - So we must transform $BA$, $\to 001ABB$ 
                only $1A$ $\to 0011BB$, the rest is all determinant.
          - then $\to 00AABB$
            we can *only* transform $0A$
            then the rest is same as above "$\to 001ABB$ ..."
    - In summary which is related with [wikipedia_anbncn]
      we use the *first 2* rules to generate many 0,A,B (i.e. "blowing-up S") where we can use rule 3 (i.e. 3-6 in [wikipedia_anbncn]) to exchange BA
      - Notice here *all BA's must be exchanged*, otherwise, rule 4-7 will cause the above 2A unable to use rules for BA. (This is to ensure "provided it is in the right place")
      So we can assume *at some stage* we have $\overbrace{0\cdots 0}^{k\;\text{times}}\overbrace{A\cdots A}^{k\;\text{times}}\overbrace{B\cdots B}^{k\;\text{times}}$ after exchanging all BA's and making S disappear (this is a must to *end the production*).
      Then as the above says, the rest is determinant.
  - maybe related with [Type-1 languages][type_1_grammar] but it *doesn't restrict the details* of the grammar (referred in [this](https://dl.acm.org/doi/pdf/10.5555/1882757.1882777))
    [proof][wikipedia_anbncn]
    - Here rules 3 to 6 used for $CB\to BC$ is due to "wouldn't fit into the scheme"
    - > provided it is in the right place
- [ ] 14
  - a) trivial
  - b) $\langle S\rangle\Coloneqq 00\langle A\rangle,\langle A\rangle\Coloneqq 1\langle A\rangle\vert 1$ see the ans where we can have 2 or *more* 0's
  - c) $\langle S\rangle\Coloneqq 11\langle S\rangle\vert 0$
  - d) $\langle S\rangle\Coloneqq 0\langle A\rangle\vert 1\langle B\rangle,\langle A\rangle\Coloneqq 1\langle B\rangle\vert 1,\langle B\rangle\Coloneqq 0\langle A\rangle\vert 0$
    - see the ans the above lacks the possibility of $0/1/\lambda$.
      maybe $\langle S\rangle\Coloneqq 0\langle A\rangle\vert 1\langle B\rangle\vert \lambda,\langle A\rangle\Coloneqq 1\langle B\rangle\vert 1\vert \lambda,\langle B\rangle\Coloneqq 0\langle A\rangle\vert 0\vert \lambda$ is fine.
- [ ] 15
  - a) $\langle S\rangle\Coloneqq 00\langle S\rangle,\lambda$
  - b) $\langle S\rangle\Coloneqq 10\langle A\rangle,\langle A\rangle\Coloneqq \lambda\vert 00$
  - c) $\langle S\rangle\Coloneqq 00\langle S\rangle\vert 11\langle S\rangle\vert 00\vert 11 \vert\lambda$
  - d) $\langle S\rangle\Coloneqq \overbrace{0\cdots 0}^{10\text{ times}}\langle A\rangle,\langle A\rangle\Coloneqq \lambda\vert 0A\vert 0$
  - e~g) see the ans because these 0's,1's locations are too undetermined for me.
  - see the ans
    - a) should be $00\langle S\rangle,\vert \lambda$
    - b) should be $00A
    - c) is wrong because 0,1 may be alternate
      - Here when $S$ disappears
        it will have the sequence like $\displaystyle\overbrace{AA\cdots AA}^{2\cdot k_1\text{ times}}\overbrace{BB\cdots BB}^{2\cdot k_2\text{ times}}\cdots\overbrace{AA\cdots AA}^{2\cdot k_{m-1}\text{ times}}\overbrace{BB\cdots BB}^{2\cdot k_m\text{ times}},k_i\ge 0,1\le i\le m$
        Assume we want to exchange $p_1$-th B (denote it with $B_{p_1}$) 
        at the last $BB\cdots BB$ of the above sequence and $p_0$-th A (similarly denoted with $A_{p_0}$) 
        at the first $AA\cdots AA$ of the above sequence.
        1. we can make $B_{p_1}$ location filled with 
          $A$ by using $AB\to BA$ $p_1$ times which will make the last $A$ in the preceding $M:\overbrace{AA\cdots AA}^{2\cdot k_{m-1}\text{ times}}$ 
          filled with $B$.
          This is a bit like moving $B_{p_1}$ to the location of the last 
          $A$ in the preceding $AA\cdots AA$
        2. To make $A_{p_0}$ location filled with 
          $B$ and let the others unchanged, after doing point 1, we can use $AB\to BA$ $2\cdot k_{m-1}-1$ times to make the last $B$ of sequence $M$ moved to the first location of the original sequence $M$.
          Then use the operations of point 1, we can move this B again to the last location of $\overbrace{AA\cdots AA}^{2\cdot k_{m-3}\text{ times}}$ which also make 
          $M$ as its original view.
          Then iteratively, we can move $B_{p_1}$ to the last location of 
          $\overbrace{AA\cdots AA}^{2\cdot k_1\text{ times}}$ from where we can make $A_{p_0}$ location filled with 
          $B$.
        - Proof of [Any permutation breaks down into cycles](https://math.stackexchange.com/a/3995056/1059606)
          - > there only a *finite* number of values for it to pass through. It has to *repeat a value at some time*
            > the *predecessor of n* on its first and second visits would be *different*, and that is not allowed in a permutation
            because "predecessor of n" means what number is put at $n$-th location which is *unique*.
        - [Every permutation can be produced by a sequence of transpositions](https://math.stackexchange.com/a/4338566/1059606)
          - here $(a_ka_{k-1})(a_{k-1}a_{k-2})\cdots (a_2a_1)$ will move 
            the number at $a_k$ location to $a_{k-1}$ and then $a_{k-2}$, etc, until $a_1$.
            This is $(a_1 a_2\cdots a_k)$ which has the following result
            ```
            a_1 a_2 a_3 ... a_k ->
            a_k a_1 a_2 ... a_{k-1}
            ```
      - See [this](./13.1-15-c.md) which I originally wnat to post as one answer of [this QA][Proof_generate_Language] but it is Context-sensitive due to $AB\to BA$ not context-free.
        - TODO
          > If the conditions on the strings can be computed in bounded memory ...
        - [3_basic_tools]
          - [This](https://cs.stackexchange.com/a/11316/161388) "How to prove 1." may be same as the above [Proof_generate_Language]
          - [This](https://cs.stackexchange.com/questions/18524/how-to-prove-that-a-language-is-context-free/26159#comment67981_18524) is similar to [3_basic_tools]
          - iteration where $\epsilon$ is to end the construction process.
            similar to $\mid b$ in $B \to Bb \mid b$
          - [TODO](https://cs.stackexchange.com/a/19799/161388)
        - [formal_proof_generate_Language]
          "Exercise" and "What about non-linear grammars?" are skipped because the rest is enough.
          - Here $M_i$ are probably *all possible* generated words at *each phase*.
            > One strategy is to *investigate phases* the grammar works through
            where $\sent{G}$ is *all possible* generated words.
            - > While 2. is usually clear by definition of the  Mi
              here is because $\sent{G}$ is "the set of sentences that can be derived from S".
          - Both $\sent{G}\subseteq M$ and $M\subseteq \sent{G}$ are based on *induction*
            - Example
              Here only the final state $M_2$ corresponds to $L$
              And all $M_{0\sim 2}$ *can be generated* so all of them are in 
              $\sent{G}$
          - ~~TODO~~ ["non-linear grammars"](https://www.sanfoundry.com/compilers-questions-answers-right-left-linear-grammar-1/#:~:text=Explanation%3A%20Grammar%20is%20non%2Dlinear,on%20the%20right%2Dhand%20side.).
            means each production can *implicitly* add more than 1 *terminal sequences*.
            - Here we prefers linear
              > If we have control over the grammar, this teaches us to keep it simple
            - TODO "more than one variable parameter".
          - "The ansatz" shows the steps of the proof.
            it just proves $T^*\cap \sent{G}=L$ so that we can only end with $L$ where "end" is implied by $T^*$ and
            > The language *generated* by $G$ is $\lang{G} = \sent{G} \cap T^*$
            - It uses $M_i$ as *the medium*.
    - d) $\vert 0$ is unnecessary.
    - e) similar to c)
      - here $\lambda$ has same number of 0's and 1's,
        so the basic form should be $S\to A$ and then $A\to 0$.
      - based on the recursive process,
        S can be added by one $A$ or $AB$ (Then $BA$ by $AB\to BA$) which excludes one $B$ or $BB$ because "more 0s than 1s".
      - Here I don't give one strict proof for each sub-exercise because most of them are similar.
    - f) here we use the same notation as [3_basic_tools]
      $S\to ASB\mid \lambda,AB\to BA,BA\to AB,A\to 0,B\to 1$
    - g) same as Example 1 in [3_basic_tools]
      Here when $S$ disappears, we have $\overbrace{AB\cdots AB}^{k\text{ times }AB}T\mid \overbrace{AB\cdots AB}^{k\text{ times }AB}U$
      Then $T,U$ is same as $A,B$ in [3_basic_tools]
      Then we get unequal A,B.
      Then the rest is same as f).
      - **Notice** here the 3 parts splitted by yellow highlights in the ans *don't influence with each other* (e.g. if we do $AB\to BA$ *in* the 1st part, it is same as we do $AB\to BA$ *after* the 1st part. Others are similar).
        So *possible reordering* of operations across parts doesn't influence the result.
        So we can do *part by part*.
        - When 1st part -> 2nd part finishes, we have $\overbrace{AB\cdots AB}^{k_0\text{ times }AB}\overbrace{A\cdots A}^{k_1\text{ times }A}\mid \overbrace{AB\cdots AB}^{k_0\text{ times }AB}\overbrace{B\cdots B}^{k_2\text{ times }B}$
        - This can be also used in the former sub-exercises.
        - As 18 says, these parts are like different sub-machines. <a name="producuction_for_each_nonterminal_one_by_one"></a>
- [x] 16 much more trivial than 15.
  - a) $S\to 1S\mid \lambda$
  - b) $S\to 1A,A\to 0A\mid \lambda$
  - c) similar to a) $S\to 11S\mid \lambda$
- [ ] 18
  - a) similar to 16-b)
  - b) using [3_basic_tools]
    we first concatenate $S\to AB$
    then use 16-a,c)
  - c) $S\to 0S0\mid B,B\to 1B\mid \lambda$
  - see the ans
    - The above b) is wrong which outputs $0^m 1^{2n}$.
- [x] 20
  - $S\to 0S0\mid 1S1\mid 1\mid 0\mid \lambda$
- [ ] 21
  similar to [3_basic_tools] where a,b) are trivial with the similar notation and c) means same as "the language generated from S1 is repeated"
  proof can be done by *thinking $L(G_{1,2})$ as one single symbol*.
- [ ] 22
  - based on ["ordered rooted tree"][ordered_rooted_tree] where all children are from left to right w.r.t. each parent, so in all we can manipulate from left to right.
- [ ] 24
  - see the ans here b,c should be in different leaves because they are seen as 2 terminal symbols.
  - Here all productions are preceding symbols or end the production.
    so we can construct from left to right.
- [ ] 25 similar to EXAMPLE 12
  - here I only do d) because they are similar.
    d) trivially we must have $S\to AB\to CaB$ because there is only one choice at each step of the first two steps.
    since $C,B\not\to\lambda$ there must be one $a$ inside.
    so d) is impossible.
    - for c)
      we can have $CaB\to cbaB\to cbaBa\to cbaba$
- [ ] 26
  - d) only $B\to Ba$ is possible for the end ($A\to Ca$ is impossible due to $S\to AB$)
    then only $B\to Cb$ ($B\to b$ is impossible due to $S\to AB,A\to Ca$ but we have the ending $cba$ instead of $aba$)
    Here we have the ending $Cba$, but $C\to b\mid cb$ can't have $bc$.
  - see the ans
    - d)
      - > we may assume (without loss of generality) that the last step in the derivation was bbbCa ) bbbcba
        because $C\to cb$ ~~can't be derived more~~ are transformed into terminal symbols which are *independent* of the following productions. 
        ~~Moreover, even if it is done before the last step, since it is context-free which causes $C$ can't be eliminated by something like $\alpha C\beta$,~~ ~~from $CaB$ we must have one step $C\to cb$ which can be reordered.~~ 
        So if it is done before the last step, it can be moved to the end *without influencing others*.
        (Also if C is kept throughout the process, due to *context-free*, it will not be used by other productions like $\alpha C\beta$)
      - > Now the only way for Ca to have occurred is from the rule $A\to Ca$
        ~~because no production can output one single $a$~~
        because the only production to output the *terminal* symbol $a$ is $Ba,Ca$.
    - in summary
      "bottom-up parsing" focuses on the RHS instead of LHS.
- [ ] 29
  - IMHO we only need "⟨positive integer⟩ $\to$ ⟨nonzero digit⟩⟨Integer⟩" and "⟨positive integer⟩ $\to$ ⟨nonzero digit⟩" (Here I use "⟨Integer⟩" for the original form which allows leading zeroes.)
    because we only needs to exclude $0$, so "⟨integer⟩ → ⟨integer⟩⟨digit⟩" should also be "⟨integer⟩ → ⟨positive integer⟩⟨digit⟩" to avoid leading 0's.
  - Again, we can [producuction_for_each_nonterminal_one_by_one] independently (independence is trivial).
- [ ] 30 mostly similar to 29 where both are based on iteration in [3_basic_tools] by iterating digits, etc.
  - a) $S\to N/M,N\to SM,S\to +\mid -,M\to DM\mid D,D\to 0\mid \cdots\mid 9$ similar to EXAMPLE 15.
  - see the ans
    - ~~The above wrongly assumes integer.~~
    - the above is wrong because we should ensure $M\neq 0$.
- [ ] 32 is based on iteration in [3_basic_tools] by iterating $UC,FC$
  $$
  \begin{align*}
  S&\to \langle UC\rangle \langle F\rangle \langle UC\rangle \langle F\rangle,\\
  \langle U\rangle&\to \langle UC\rangle \langle U\rangle\mid \langle UC\rangle,\\
  \langle UC\rangle&\to A\mid \cdots\mid Z,\\
  \langle F\rangle&\to \langle FC\rangle \langle F\rangle\mid \langle FC\rangle,\\
  \langle FC\rangle&\to a\mid \cdots\mid z\mid \langle UC\rangle
  \end{align*}
  $$
  - see the ans
    - here initial can be not capital.
    - $\langle UC\rangle \langle F\rangle$ omits the mere $\langle UC\rangle$ wrongly.
- [ ] 34 trivial
  - This is just part of regex.
  - [ISO](./standards/s026153_ISO_IEC_14977_1996(E).pdf) is ~~same as~~ different from [this](https://www.w3.org/Notation.html) from [this](https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form#Related_work) which is similar to [ABNF](https://www.rfc-editor.org/rfc/rfc5234#page-9). (ISO has except but the latter 2 don't)
    - as [this](https://stackoverflow.com/a/38161979/21294350) says, ISO is used rarely.
  - book is same as [this version](https://www.garshol.priv.no/download/text/bnf.html#id2.3.) from [this](https://stackoverflow.com/a/29322862/21294350)
  - [this](https://www.cs.cmu.edu/~pattis/15-1XX/common/handouts/regularexpressions/regex.html) compares ~~ISO with this version~~ regex with ISO EBNF
- [ ] 36 $\text{bread(mustard|mayonnaise)lettuce?tomato?(turkey|chicken|roast beef)+(cheese*)?bread}$
  - see the ans
    - (cheese*) is enough.
- [ ] 38
  $$
  A?\to A\vert \lambda\\
  A*\to (M\to AM\vert \lambda)\\
  A+\to (M\to AM\vert A)
  $$
  - see the ans
    - Here we assume only ? has the group version.
- [x] 40
  - Here the preamble to Exercise 39 "⟨term⟩,⟨factor⟩,⟨expression⟩" can make any combination of add,mul.
  - modification
    ```
    ⟨term⟩⟨addOperator⟩⟨term⟩
    ⟨factor⟩⟨mulOperator⟩⟨factor⟩
    |(⟨expression⟩)
    ```
- [ ] 42
  - $R$
  - see the ans
    - notice the exercise says "directly".
    - [derivable](http://courses.ics.hawaii.edu/ReviewICS241/morea/computation-models/LanguagesAndGrammar-QA.pdf)
### 13.2
- 2(ans a,b corresponds to the book b,a),4(1. here a corresponds to the book a ... 2. Here I skip b because it is similar to a),6(similar to 4),20 skipped
- [x] 8
  - [see][overleaf_automata]
  - see the ans
    - omits penny
    - let all space be the final states which make the layout neat.
- [ ] 10 see the ans
- [ ] 12 sequence where if one step is wrong we go back to the initial state.
  - how is "second left" implemented?
  - [example lock](https://www.youtube.com/watch?v=-l20hR3O8w8)
  - why (8,L,2) has no loop but (10,R,1) has?
- [ ] 14
  - Here if thinking of 4 digits as one component
    then we have 4 states
- [ ] 16 inputs are categorized into 3 types and the states are also categorized into 3 types based on $\mod$.
  - see the ans
    - TODO what does input 0,1 mean?
      - if [binary](https://qr.ae/ps7P1n), then the 2 arrows should point to different nodes.
      - [endian](https://qr.ae/ps7Ppq) also needs to be considered.
- [ ] 18 similar to 14 where W means read 1 and R means read non-1. Then we needs 5 W's.
  - see the ans
    - We need one loop for $s_5$ and $s_0$
- [ ] 22 see the ans
- [ ] 24 similar to 16 see the ans 
### 13.3
- 6,18~22(similar to 16),
  32~36(32: same as EXAMPLE 7 $s_{0,2},s_{3}$ and 2 states are enough. 34: similarly with 4 states),39,
  40~48,54(1. trivial because 2 $01^n$ and $n\ge 0$ 2. the ans says: here $(s_1\xRightarrow{0} s_1,s_1\xRightarrow{0} s_2),(s_3\xRightarrow{0} s_3,s_3\xRightarrow{0} s_2)$ are duplicate pairs where we only keep productions related with the final states) skipped.
- [ ] 2 see the ans
- [ ] 4 see the ans for the strict proof of b)
- [ ] 8
  - a~e) are right and f) is wrong similar to 6.
    a) by definition
    b,c) proof by showing all cases.
    d,e) same as 4-b)
  - see the ans for a,b,e)
- [x] 10
  - in a,c,d) but not for b,e,f).
- [ ] 12
  - it recognizes $\{0^n,(0^n(10)^m)^*,(0^n(11(0,1))^m)^*\}$ 
    (Here $*$ means we see $(0^n(10)^m)$ as one symbol and * means words of it)
    here $s_3$ can't be reached because in-degree is 0 which can be removed.
  - so a,d) can be recognized. 
    b,c) can't.
- [ ] 15 see the ans
  - induction for the length of $y$.
- [ ] 16
  - $\lambda,1a,01^n0a$ where a means any bit string.
- [x] 26
  - 4 states including the initial state based on the consecutive 0 number.
- [x] 28 similar to 26 but 1 causes one loop but won't go back to the initial state.
- [ ] 37
  - see the ans
    - > so the transition from s0 on input 1 must be to s1
      because $s_1$ needs to be reachable.
- [ ] 38
  - > Since the string 01 is not accepted (but some longer strings that start this way are accepted), there has to be a transition from s1 on input 1 either to itself or to s2.
    here no next state is possible in the general case like EXAMPLE 9.
- [ ] 56
  - see the ans
    - based on [this][DFA_partial_transition_function], only removing the graveyard doesn't make the machine nondeterministic.
      > My answer is an unequivocal: No.
- [ ] 57 see the ans
  - since we need to track the number of 0's and 1's, there are infinite cases.
- [ ] 58~61
  - > two states are equivalent if every input string either sends both states to a final state or sends both to a state that is not final
    i.e. we only cares about whether final but not which non-final state.
  - [x] 58 trivial
    - [Refinements p24](https://www.isical.ac.in/~ansuman/flat2018/myhill-nerode-priti.pdf) of equivalence relation
      - same as in topological where cover ~~means~~ is similar to [partition](https://en.wikipedia.org/wiki/Partition_of_a_set) in relation but the former doesn't need empty intersection for each pair of subsets.
    - see the ans
      - d) is based on c) with $\subseteq$
      - f) assumes $l(x)>0$ is already met, then it manipulates the $l(x)=0$ case.
  - [ ] 59
    - It is to show every state has one matched *minimal*-length string which is unique for this state. This is trivial to be true.
    - see the ans
      - > But f (s, a) and f (t, a) are n-equivalent
        because 
        > states s and t that are (n + 1)-equivalent 
  - [ ] 60
    - a) only if is the definition of 0-equivalent
      if is similar.
      - ~~if $\overline{M}$ contains one non-final states ~~
        ~~$t$ and final state, then s and t aren't 0-equivalent.~~
        since final states can only be equivalent with final states. so conclusion ...
    - b) if is the definition
      only if is done by using exercise 15
    - c) constructs the partition for $R_{*}$ using exercise 59,
    - see the ans
      - b) ["well defined"](https://en.wikipedia.org/wiki/Well-defined_expression) is to show unique value.
        >  $\overline{f} ([s]R∗ , a ) = [f (s, a)]R∗$ for all states [s]R∗ of M and input symbols a ∈ I
        "the choice of representative" means what state to choose for [s]R∗
        since for $s,t\in [s]_{R_*}\Rightarrow s,t\in [s]_{R_k},k\ge 1$, 
        $f(s,a)_{R_{k-1}}=f(t,a)_{R_{k-1}},k-1\ge 0\Rightarrow f(s,a)_{R_{*}}=f(t,a)_{R_{*}}$
        so two RHS's are same -> well defined.
  - [ ] 61
    - [x] a) prove "string $w$ goes to the final state in $M$ if and only if it goes to the final state in $\overline{M}$"
      only if: ~~trivially starting from $[s_0]_{R^*}$ we get to the next state ~~
      ~~$k$ of $w$ which is same whether-final status as $f(w,a)$ one by one~~
      if $f(s_0,x)$ is the final/non-final state,
      then $f(s_0_{R^*},x)$ is also the final/non-final state by the definition of 
      $R^*$.
      if: similar to "only if" based on the symmetric property of $R^*$.
    - b) [proof][Introduction_Automata_Theory_Languages_and_Computation] see the ans
      - > The start states of M and N are indistinguishable because L(M) == L(N).
        this is by "indistinguishable" definition where if distinguishable, there is one string $w\in F(M)$ where F means final state such that 
        $w\notin F(M)$ contradicting with L(M) == L(N).
      - Mapping
        > Thus, every state of M is indistinguishable from at least one state of N
        is based on 
        > their successors on *any one input* symbol are also indistinguishable. The reason is that if we could distinguish the *successors*, then we could distinguish p from q.
        which is based on Theorem 4.20.
      - ~~because removing one state will at least destroy one indistinguishable pair $(u,v)$~~
        ~~Assume $u$ is removed, then $()$~~
        > Since N has fewer states than M, there are two states of M that are indistinguishable from the same state of N, and therefore indistinguishable from each other
        based on the pigeonhole principle and the transitive property (Theorem 4.23 and equivalence relation in 58-b).
        > But M was designed so that all its states are distinguishable from each other
        this is the step 1 in ihe contents after Theorem 4.24.
      - table-filling algorithm
        induction is from the longer string to the shorter string.
      - Theorem 4.20 is based on "the shortest strings" and then contradiction with one "shorter".
      - In summary
        L(M) = L(N) -(based on accepting split defines uniquely whether distinguishable in p169. OR *all* strings as input of the table-filling algorithm from the *start* state *won't differentiate* (not distinguished), so the start states of M,N are equivalent)> $s_{0}^{(M)}$ 
        and $s_{0}^{(N)}$ are indistinguishable -> the above "Mapping" -> pigeonhole principle.
        - Notice here we may probably ["*Remove all inaccessible* states" p32](https://people.csail.mit.edu/rrw/6.045-2020/lec5-before-class.pdf) which is implied by
          > Neither M nor N could have an inaccessible state
          This is implies as the exercise says
          > for every state s of M there is a string x ∈ I∗ such that f (s0, x ) = s,
        - **Intuitively** here just put states with the *same output for all strings* 
          (1. i.e. $R_*$ 
           1. it is also implied in $\overline{f}([s]_{R_*},a)$ are same for $[s]_{R_*}$ where the output states are combined correspondingly.)
          together because they *function same* for the final result.
          ~~And then all *corresponding functions* are also changed.~~
    - NFA related in [Introduction_Automata_Theory_Languages_and_Computation] p177
      - > Surely accepting state B is distinguishable from nonaccepting states A and c.
        based on 0-distinguishable.
  - [ ] 62
    - $k=0$ trivial
      $s_{0,1,2,4}$ are accepted.
      $s_{3,5,6}$ are not accepted.
      - $k=1$
        $s_0$ both not accepted for 0 and 1
        with 0(accepted) and 1(not accepted):
        1. $s_1$ 
        2. $s_{3,5}$ 
        with both 0 and 1 are accepted:
        3. $s_{2,4}$ 
        4. $s_6$
      - $k=2$ based on refinement and the single-element set can't be refined
        since $s_{3,5}\xRightarrow{(0,1)}(s_3,s_5)$, we have 
        $s_3 R_* s_5$
        similarly for $s_{2,4}$
        - This uses 60-b) where in
          > f (s, a) and f (t, a) are (k − 1)-equivalent
          k-1 is * since the transformed states are *same*.
      - $k=*$ same $k=2$
### 13.4
- 2~4,10,14 skipped
- [ ] 6
  - a) here $\{\lambda\cup 0\cup 1\}\cup \{00,01,10,11\}\ldots$ is a bit complex.
  - b) trivial by the exercise description.
  - c) I assume 1 is followed by exactly 2 zeroes. So $(100)^*$.
    - see the ans the above is wrong without considering the leading zeroes.
  - d) similar to c) 
    $0^* (10^*)^* 00$ ~~which can be transformed to $0^* (10\cup 0)^* 00$ trivially.~~
    - The above is wrong because $10^*$ can be 1 then 11 is allowed.
  - e) trivial see the ans.
- [ ] 8
  - a) based on [DFA_partial_transition_function], FIGURE 1 (a) is also fine.  
    The rest is similar.
  - Also see [overleaf_automata]
- [ ] 11
  - Based on [definition 1](https://en.wikipedia.org/wiki/Regular_expression#Formal_definition), trivial by definition.
  - see the ans
    - Here $B^*$ is based on [string concatenation](https://en.wikipedia.org/wiki/Kleene_star).
- [ ] 12
  - see the ans
    - TODO
      - ~~a) here 0 should be pointed to one nonfinal state.~~
    - ~~c) ~~
      ~~1. the arrow should point to the top row 1st accepting state instead of the 2nd.~~
      ~~2. ~~
      See [overleaf_automata]
- [x] 16 here $A$ is the final state $F$.
- [ ] 18 TODO strict proof
  - Here each transition has one **one-to-one correspondence** with the grammar production rule.
  - This is different from [formal_proof_generate_Language].
- [ ] 20 see the ans
- [x] 21
  - if
    by the pigeonhole principle, there is one state revisited when processing $x$
    this causes the loop, so infinite.
  - only if
    if $\forall x,l(x)<|S|$, then there are at most 
    $|I|^|S|$ possible recognized words which is finite.
- [x] 22
  - same as 21, here $uv$ is the sub-string which **firstly** meets with the revisited state which has at most $|S|+1$ states. Then $l(uv)\le |S|+1-1$.
  - see the ans
    - Here it may be intended to say "EXAMPLE 6".
- [x] 23 choose $n=|S|$ then 
  $0^{2n+k}1^n,k\le n$ (all 0s because $l(uv)\le |S|$) is accepted unnecessarily.
- [x] 24 same as 23's choice where $|S|^2+k\le |S|^2+|S|< (|S|+1)^2$ which is not one square.
  - see the ans
    - Here $n$ can be chosen very large or just meet the limit as the ans does.
- [x] 25 $N=|S|$
- [ ] 26
  - see Theorem ~~3.5.1~~ ~~Theorem 2.3.1 which is stronger.~~ 2.3.2 in [Elements_of_Theory_of_Computation_2ed_Lewis_Papadimitriou]
  - ~~TODO $|-$ symbol meaning in the proof of Theorem 2.3.1.~~
    - in p71, $|-$ means they have the same result at the end with *one* step difference. Then 
      $|-^*_M$ means with *any* step difference.
      And e in $(q,e)$ means ending ("M has consumed all its input").
      implied in p80
      > if a transition (q, e,p) is followed, then no input symbol is read
      - here e means [empty string (see $\epsilon$-Transitions)](http://mlwiki.org/index.php/Non-Deterministic_Finite_Automata) (also see [this](https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton#Formal_definition_2)) $\lambda=A^0$ (13.3.2 definition in the book) in the book.
        it is different from $\varnothing$ as [this](https://math.stackexchange.com/a/2000016/1059606) where $\varnothing$ accepted means accepting nothing (i.e. always the *unaccepted* state) but $\lambda$ means it is *already accepted* so we do nothing.
    - p80
      - $\triangle$ -> transition relation which corresponds to "*one* step difference".
    - p94
      - $k=0$ is based on the definition (1) of "regular" in p62.
        - here when i=j, $e\notin \triangle$ is possible, so we $\{e\}\cup \{a\in \Sigma \cup \{e\}\}$
      - $q_k$ may be passed multiple times where $R(i,k,k-1)$ is met the 1st time.
        - Here $R(k,j, k - 1)$ doesn't use 
          $q_k$ because that ~~will cause the cycle and *unnecessary steps* in the path.~~ is already contained in $R(k,k,k-1)$ which implies all cycles including 
          state $k$.
        - It is based on definition (2~4) of "regular" in p62.
      - compared with FIGURE 4 in section 9.4, here we considers $R(k, k, k - 1)^*$ which is necessary for considering whether reachable in the Warshall’s Algorithm.
        - This is also implied in reference "The O(n3) algorithm for the reflexive-transitive closure is from" in [Elements_of_Theory_of_Computation_2ed_Lewis_Papadimitriou]
        - these 2 algorithms are similar because we can see finite automaton as one *graph* where the string is similar to the path.
      - This proof uses the **recursive** property of the regular set.
    - In summary,
      it is based on $\cup\{R(l,j, n) : q_j \in F\}$ -> 
      $R(i,j,O)\xRightarrow{\text{induction}}R(i,j, n)$ where $R(i,j,O)$ is one step difference which doesn't pass any state intermediately and 
      $R(i,j,k+1)$ is similar to the Warshall’s Algorithm.
- [x] 28
  - "distinguishable" here is ~~different from~~ similar to  [Introduction_Automata_Theory_Languages_and_Computation] where it is based on whether accepting.
    Here it is based on accepting w.r.t. one specific $L$ instead of the recognized language.
  - use the contrapositive proposition.
  - Also see 13.3-61-b) where if $x$ and $y$ are indistinguishable then *possibly* $f(s_0,x)\neq f(s_0,y)$
- [x] 29
  - using 28, there are $n$ strings $x_{1\sim n}$ and 
    $f(s_0,x_{i})\neq f(s_0,x_{j}),(i,j)\in S\times S\wedge i\neq j,S=\{1,2,\cdots,n\}$
- [ ] 30
  - $2^{n-1}$ because only $n-1$ bits in $n$ bits can be chosen.
  - see the ans
    - end [meaning](https://cs.stackexchange.com/a/14009/161388)
    - Based on 31, here $xz\in L,yz\notin L\Rightarrow L\setminus x\neq L\setminus y$
      - > If x and y are two bit strings of length n that differ in bit i
        implies x and y are distinct and we choose *one arbitrary distinct bit*.
        So x and y are distinguishable based on the above $L\setminus x\neq L\setminus y$
- [ ] 31 see the ans
### 13.5
- 2,8,12~14,30 skipped
- [ ] 4
  - b) all ones
  - see the ans
    - notice here  (s0 , B, s 1, B, L ) instead of  (s0 , B, s 1, B, R ).
- [x] 6
  - $(s_0,0,s_0,0,R),(s_0,1,s_0,1,R),(s_0,B,s_1,1,R)$ where $s_1$ is accepted.
- [x] 10
  - $(s_0,0,s_0,0,R),(s_0,1,s_1,1,R),(s_1,1,s_2,0,L),(s_1,0,s_0,0,R),(s_2,1,s_3,0,L)$ where $s_3$ is accepted.
  - see the ans where it uses $(s_2,1,s_3,0,R)$ instead of 
    $(s_2,1,s_3,0,L)$
- [ ] ~~13~~ 15 corresponding to EXAMPLE 3.
  - Here $s_1$ means 0 in one pair is changed to M
    $s_2$ means we have meet the end of the left *unmatched* string
    $s_3$ means the rest 1 in one pair is changed to M
    $s_4$ means we still have 0 unmatched
    $s_5$ means we have no 0 unmatched
    $s_6$ means we have ~~$n\ge 1$~~ all 1s changed to M.
  - see the ans
    - > Otherwise, the initial 0 is changed to an M 
      (s0, 0, s 1, M, R ),
      > the machine skips past all the intervening 0s and 1s
      (s1, 0, s 1, 0, R ), (s1, 1, s 1, 1, R )
      > until it either comes to the end of the input string or else comes to an M. At this point, it backs up one square and enters state s2.
      (s1, M, s 2, M, L ), (s1, B, s 2, B, L )
      > there must be a 1 here if the string is acceptable.
      (s2, 1, s 3, M, L )
      > it stays in s3 as long as it sees 1s,
      (s3, 1, s 3, 1, L ), 
      > then *stays* in s4 as long as it sees 0s.
      (s3, 0, s 4, 0, L ), (s4, 0, s 4, 0, L )
      > Eventually either it encouters a 1 while in s4 at which point it halts without accepting or else it reaches the rightmost M that had been written over a 0 at the start of the string.
      Here $1$ is omitted
      ~~(s4, M, s 0, M, R )~~
      > so it had better be the case that there are *no more 1s* either; this is accomplished by the transitions (s3, M, s5, M, R) and (s5, M, s6, M, R), and s6 is a final state.
      (s5, M, s6, M, R) achieves "no more 1s either" by excluding the (s5,1) situation [here (s5,0) is impossible because (s3, M, s5, M, R) and (s3, 0, s4, 0, L) imply it doesn't change to s4 after skipping all 1s by (s3, 1, s3, 1, L), so no 0s left.], i.e. 1s are all changed to M.
      > If it is in s4 when this M is encountered, things start all over again,
      (s4, M, s 0, M, R )
    - In summary,
      0->1: it *only* accepts starting 0 [(s0, 0, s 1, M, R )],
      1->2: then moves right until the ending *B/M* [(s1, 0, s 1, 0, R ), (s1, 1, s 1, 1, R ), (s1, M, s 2, M, L ), (s1, B, s 2, B, L )],
      2->3: then *only* accepts ending 1 before the leftmost B/M [(s2, 1, s 3, M, L )].
      3->4/5: Then there may be 
      1. no 0s [(s3, M, s 5, M, R )] 
        - 5->6: There should be also no 1s, i.e. s5 *only* accepts M [(s5, M, s 6, M, R )].
      2. some 0s before 1s (if no 0s before 1s, then (s5, M, s 6, M, R ) will not accept it) and 1s should be more than 0s (if not, then (s2, 1, s 3, M, L ) will not accept this string because of (s2,0)) [(s3, 1, s 3, 1, L ), (s3, 0, s 4, 0, L )]
        - 4->0: trivially we *don't accept 1s* and want to traverse 0s where afterwards restart the above process, so only [(s4, 0, s 4, 0, L ), (s4, M, s 0, M, R )].
        - so 1s before 0s is impossible.
      3. Notice here due to in the middle of the string, so *no (s3,B)*.
    - Also see [this][cstaleem_0_n_1_n] where the basic idea is same as this exercise by manipulating with *one pair of 0 and 1* at each iteration.
- [ ] 16
  - compared with 15, here we add $(s_1, 0, s_2, M, R)$ and all later subscripts are added by 1.
  - see the ans which is solution_1 when exercise 15 is solution_0
    - Here $n\ge 0$ so "(s0; B; s5; B; R)" where $s_5$ is accepted.
    - and "(s3, 0, s4, 0, L), (s3, M, s5, M, R), (s4, 0, s4, 0, L), (s4, M, s0, M, R), and (s5, M, s6, M, R)" are changed to "(s4; 0; s4; 0; L), (s4; M; s0; M; R)" corresponding to "(s3, 0, s4, 0, L), ... (s4, M, s0, M, R)" after adding the subscript.
      Here "(s0; M; s5; M; R)" is to ensure the *correct pair* of 0s and 1s, i.e. the number of 0s are two times the number of 1s.
      - In summary, after transforming *one pair* of two 0s and one 1s after "(s3; 1; s4; M; L)"
        it traverses *back until one M* by "(s4; 0; s4; 0; L), (s4; 1; s4; 1; L), (s4; M; s0; M; R)"
        and then checks whether all strings are M by "(s0; M; s5; M; R)".
        If so then 0s are twice the numeber of 1s.
        - Notice the above "until one M" ensures "(s0; B; s5; B; R)" can only occur when empty string
          since $s_0$ either occur at the beginning
          or after "(s4; M; s0; M; R)" which ensure at least one pair where it must stop *inside* the string, so the latter case can't be $(s_0,B)$.
      - Then 15 can be also changed similarly as 16
        "(s3, 0, s4, 0, L), (s4, 0, s4, 0, L), (s4, M, s0, M, R)," are combined into "(s3, 0, s3, 0, L), (s3, M, s0, M, R)" and then adding the subscript "(s4, 0, s4, 0, L), (s4, M, s0, M, R)"
        and "(s3, M, s5, M, R)," are changed to "(s4; M; s0; M; R)" where s4 are kept after a sequence of 1s by (s4; 1; s4; 1; L) or a sequence of 1s and 0s by "(s4; 0; s4; 0; L), (s4; 1; s4; 1; L)".
        and "(s5, M, s6, M, R)." are changed to "(s0; M; s5; M; R)"
        - In summary, in exercise 15 s5 is to ensure no 0s unchanged to M and s6 is to ensure no 1s unchanged to M
          while here $(s4, M, s0, M, R),(s0; M; s5; M; R)$ is to ensure *all 0s and 1s* are changed to M.
          So the latter one uses one less state.
          - And here it doesn't use $s_{4,5}$ to differentiate between 0 and M before 1s, so *one less state again*.
            See the above "combined into ... changed to"
        - See exercise 15, there are also other ways to construct $0^n 1^n$, so I didn't dig into these equivalent ways.
    - [This one (let it be solution_2)][uchicago_0_n_1_n] is better which removes $(q_0,\$,q_4,\$,R)$ based on 
      [cstaleem_0_n_1_n] due to $n\ge 1$
      because it can be easily generalized to $0^n 1^n 2^n$.
      - (q1, X, R): marks the first 0 as X
        q0 Y (q3, Y, R): it moves to the right most symbol because all 0s has been changed to X
        
        (q1, 0, R),(q1, Y, R): goes to the first/second/... 1 
        (q2, Y, L): marks it as Y

        (q2, 0, ~~R~~L),(q2, Y, L):  goes left to the second 0,
        (q0, X, R): marks it as X

        q3 Y (q3, Y, R): it moves to the right most symbol
        (q4, B, R) : then accepts
      - Notice the above assumes the string is $0^n 1^n$
        if not 
        > All *undefined* transitions means stuck, and the input is rejected.
        - Since we think 0->X,1->Y as one valid operation, so we assign one state
          and "all the 0’s and 1’s are marked" is also one state
          and "it moves to the right most symbol and then accepts" is one state to ensure 1s *matching* 0s.
          ~~and all 1s is one state.~~
      - compared with [this](https://courses.cs.washington.edu/courses/cse322/04sp/Lect8.pdf) which uses only X and uses _(B) to mark the left end.
        Here 012012 becomes XYZ012 and we goes into $q_4$, and rejects when XYZ0 is not XYZB.
        But the latter link will go to the iteration "GOTO 3a" when 010010 becomes _XX010
        - ~~notice although 010001100 is accepted unnecessarily, 001100010 won't be accepted becomes $_\overbrace{XXXXXX}^{6\text{ times }X}10$ and is stuck at $q_{skip0}$.~~
        - "if w is not in $00^*11^*00^*$, REJECT; else," tests the form of the *whole* string at the beginning to be 
          $0^n 1^n 0^n,n\ge 1$ using $q_3,1,R,q_{REJ}$
          where $n=0$ is already cared by $q_0,_,R,q_{ACC}$.
          So concatenation of multiple $0^n 1^n 0^n,n\ge 1$ like $010001100,001100010$ is disallowed.
      - ~~TODO~~ ~~there may be [no one strict proof](https://cs.stackexchange.com/q/166978/161388) that one Turing machine recognizes one language, similarly for computing one function.~~
        [strict proof][proof_Turing_Machine_recognize_language] which is same as definition 2 
        > T is said to recognize a subset A of V∗ if x is recognized by T *if and only if* x belongs to A.
        This is ~~*different* from~~ same as [formal_proof_generate_Language] ~~which directly gets show equality by $\subseteq$ and $\supseteq$~~ where it use contrapositive proposition of one direction.
        - > $w = 0^n1^m0x$ for $n, m \geq 1$ and $x \in \Sigma^*$
          - $n=m$ which is similar to $w = 0^n1^m,m>n$
            $q_0w \mapsto^* X^nq_0Y^n0x \mapsto^* X^n Y^n q_30x$
          - $m>n$ similar to $w = 0^n1^m,m>n$
            with $q_0w \mapsto^* X^nq_0Y^n1^{m - n}0x \mapsto^* X^nY^nq_31^{m - n}0x$
          - $n>m$
            - $1\not\subseteq x$
              $$
              q_0w \mapsto^* X^mq_00^{n - m}Y^m0^k \mapsto^* X^{m + 1}0^{n - m - 1}Y^mq_10^k \mapsto^* X^{m + 1}0^{n - m - 1}Y^m 0^kq_1B
              $$
            - $1\subseteq x$
              $$
              q_0w \mapsto^* X^mq_00^{n - m}Y^m0x \mapsto^* X^{m + 1}0^{n - m - 1}Y^mq_10x \mapsto^* X^{m + 1}0^{n - m - 1}Y^m 0^k' q_1 1 \mapsto^* X^{m + 1}0^{n - m - 1}Y^m 0^{k'-1}q_2 0Y \mapsto^* X^{m + 1}0^{n - m - 1}Y^{m-1} q_2 Y0^{k'}Y
              $$
          
          Thanks for your patient explanation. 1. I add some correction of your answer based on my understanding. Hope the correction isn't wrong. 2. For the last case, I proved as the following hinted by your answer. Hope they are right. 2.1 $n=m$ which is similar to $w = 0^n1^m,m>n$: $$q_0w \mapsto^* X^nq_0Y^n0x \mapsto^* X^n Y^n q_30x$$ 2.2 $m>n$ similar to $w = 0^n1^m,m>n$: $$q_0w \mapsto^* X^nq_0Y^n1^{m - n}0x \mapsto^* X^nY^nq_31^{m - n}0x$$

          2.3 $n>m$ 2.3.1 $1\not\subseteq x$ we have $$q_0w \mapsto^* X^mq_00^{n - m}Y^m0^k \mapsto^* X^{m + 1}0^{n - m - 1}Y^mq_10^k \mapsto^* X^{m + 1}0^{n - m - 1}Y^m 0^kq_1B$$ 2.3.2 $1\subseteq x$ we have $$q_0w \mapsto^* X^mq_00^{n - m}Y^m0x \mapsto^* X^{m + 1}0^{n - m - 1}Y^mq_10x \mapsto^* X^{m + 1}0^{n - m - 1}Y^m 0^{k'} q_1 1 \mapsto^* X^{m + 1}0^{n - m - 1}Y^m 0^{k'-1}q_2 0Y \mapsto^* X^{m + 1}0^{n - m - 1}Y^{m-1} q_2 Y0^{k'}Y$$
      - compared with the book ans which uses $s_{1,2,3}$ to mark the pair of 0 and 1
        for $0^n 1^n$ while uchicago uses $s_{1,2}$.
    - TODO [using 2 tapes](https://cs.stackexchange.com/q/106557/161388)
- [ ] 17 see [uchicago_0_n_1_n] 
  - since the book ans for exercise 15,16 uses pair like $X0000\cdots 111\cdotsY$, it is not direct to be transformed to $0^n 1^n 2^n$
  - (s0, B, s9, B, L) for $\lambda$ empty string
    "(s0, 0, s1, 0, L), (s1, B, s2, E, R)" marks the left end.
    "(s2, M, s2, M, R), (s2, 0, s3, M, R)" changes the rightmost 0 to M (i.e. $q_0$ in [uchicago_0_n_1_n])
    "(s3, 0, s3, 0, R), (s3, M, s3, M, R), (s3, 1, s4, M, R)" changes the rightmost 1 to M (i.e. $q_1$ in [uchicago_0_n_1_n])
    "(s4, 1, s4, 1, R), (s4, M, s4, M, R), (s4, 2, s5, M, R)" changes the rightmost 2 to M (i.e. $q_2$ in [uchicago_0_n_1_n])
    - "(s5, 2, s5, 2, R), (s5, B, s6, B, L)" continues to the end and goes back
      Then "(s6, M, s8, M, L), (s8, M, s8, M, L), (s8, E, s9, E, L)" to check through the whole string backwards.
      - IMHO we can check forwards without "continues to the end and goes back" each time like [uchicago_0_n_1_n].
    - "(s7, 0, s7, 0, L), (s7, 1, s7, 1, L), (s7, 2, s7, 2, L),(s7, M, s7, M, L), (s7, E, s2, E, R)," continues back to the left end and redo the above *iteration*.
  - This one is very similar to [uchicago_0_n_1_n]
    - [uchicago_0_n_1_n] doesn't need the left end marker for $0^n 1^n$ because $X,Y$ can differentiate so the tape will stop at X (similarly for $0^n 1^n 2^n$)
      but here since all markers are M, so the tape *can't differentiate* between the markers for 0 and 1 and then *stop earlier* when meeting with the marker for 0.
- [x] 18 same as exercise 6 by adding two 1s instead of "a 1".
  - see the ans which achieves by preceding instead of appending.
- [ ] 20
  TODO strict proof of 20,22,25 for computing the function
  - ~~$(s_0,1,s_1,1,R),(s_1,1,s_2,1,R),(s_2,1,s_3,1,R),(s_3,B,s_4,N,R),(s_3,1,s_4,E,R),(s_4,1,s_5,B,L),(s_5,1,s_6,B,R),(s_6,B,s_6,B,R),(s_6,E,s_1,1,R),(s_6,N,s_7,B,R)$~~
    $$
    (s_0,1,s_1,B,R),(s_1,1,s_2,B,R),(s_2,1,s_0,B,R)\;\text{change all met 1s to B, and }s_i\text{ means i times 1s}\\ 
    (s_0,B,s_3,B,R),(s_1,B,s_3,1,R),(s_2,B,s_4,1,R),(s_4,B,s_3,1,R)\;\text{adds the corresponding number of 1s based on i for }s_i
    $$ 
    (Here $s_3$ is the accepted state)
    - This is similar to [this](https://www.youtube.com/watch?v=aQUc__pfjaM) which uses $(v_1,#,v_2,1,L)$ corresponding to 
      $(s_1,B,s_3,1,R)$
      and similarly $(v_0,#,v_2,#,L)$
  - see the ans ~~which is wrong because it erases nothing when $n=3$, i.e. $111$, where it halts at one nonfinal state $s_3$.~~
    - It recognizes 4 1s with $11[s_4]11$
      then $B[s_7]BB1$ and then $BB[s_8]B1\to BBB[s_0]1$
    - Here it only erase 1s and halts when less than four 1s.
      It *doesn't have one final state*.
    - It uses $n+1$ 1s for $n$ as EXAMPLE 4 instead of $n$ 1s as the above assumes.
- [ ] 22
    $$
    (s_0,1,s_1,E,L)\;\text{marks the right part of the pair of 1}\\
    (s_0,B,s_n,B,L)\;\text{no 1s to double}\\
    (s_1,B,s_2,1,R),(s_1,1,s_1,1,L)\;\text{adds the left part of the pair}\\
    (s_2,1,s_2,1,R),(s_2,E,s_0,1,R)\;\text{redo the iteration}\\
    $$
    - For $111$ it has $E11\to 1E11\to 1111\to E1111\to \cdots$
  - see the ans
    - > s2 , scan left to first 1
      means the rightmost 1.
    - > (s2; B; s5; B; R)
      means all 1s has been changed to 0 and all corresponding $n$ 1s have been appended
    - > (s5; B; s6; B; R)
      corresponds to $n=0$
    - Notice for 20,22 and later exercises, it is complex and trifling to prove the TM constructed by myself is equivalent with the ans *each*.
- [x] 24
  - $(s_0,1,s_0,1,R),(s_0,\ast,s_1,1,R),(s_1,1,s_1,1,R),(s_1,B,s_2,1,R)$
  - see the ans
    - The above should be $(s_0,1,s_0,B,R)$
    - It writes all 1s at the left.
- [ ] 25
    $$
    (s_0,1,s_1,B,R)\;s_1\text{ means the left part of the pair of 1s is changed to }B\\
    (s_1,1,s_1,1,R),(s_1,\ast,s_2,\ast,R)\;s_2\text{ means we go into }n_2\text{ part}\\
    (s_2,E,s_2,E,R),(s_2,1,s_3,E,L)\;s_3\text{ means the right part of the pair of 1s is changed to }B\\
    \text{Notice here we can't use B for }n_2\text{ marker of 1 because we want to skip all markers, so if all 1s  in }n_2 \text{ are changed to 1, we will go infinitely right}\\
    (s_2,B,s_7,B,R)\;s_7\text{ means all 1s in }n_2\text{ are matched, so }n_1\ge n_2\\
    (s_3,E,s_3,E,L),(s_3,\ast,s_4,\ast,L)\;s_4\text{ means we go back into }n_1\text{ part}\\
    (s_4,1,s_6,1,L),(s_4,B,s_5,B,R)\;s_5\text{ means }n_2\ge n_1\Rightarrow f(n_1,n_2)=n_1\\
    \text{Notice here we can use B for }n_1\text{ marker of 1 because we will stop at the }\textbf{rightmost}\text{ B}\\
    (s_6,1,s_6,1,L),(s_6,B,s_0,B,R)\;s_6\text{ means there are 1s in }n_1\text{ unchanged to }B\\
    $$
  - The above one is similar to [this][geeksforgeeks_max_f_n1_n2] where both match the *pair* of 1s at each iteration and goes to the final when *one side have no 1s* (geeksforgeeks uses 0 instead of 1 and C instead of $\ast$. It calculates max instead of min although they are similar), but it doesn't change B/E back to the correct number of 1s
    Also see [this](https://cs.stackexchange.com/q/166994/161388) which is based on [proof_Turing_Machine_recognize_language]
    > Therefore for each input w there's *only one sequence* of IDs (one computation) we need to consider
    so we can also have one **definite** sequence of mapping $\mapsto$ when $n_2</\ge n_1$
    - > Hence change all Xs to Os and stop on leftmost side.
      it implies changing Xs on the left side instead of all Xs including the right side.
      similar to
      > Hence convert all Xs to Os on *right-hand side* and stop.
    - $q_0$: starting state of the process $K$ to change the pair of 0s
      $q_1$: changing the left part of the pair
      $q_7$: the left side is all changed to Xs
      $q_2$: the process $K$ goes into the right side
      $q_3$: the right side is all changed to Xs
      $q_5$: changing the right part of the pair
      $q_6$: the process $K$ goes back into the left side
      $q_{4,9}$: final
      $q_8$: meet the right end when changing the right side Xs back to 0s.
    - > On receiving 0 in state q8, keep moving left and on receiving C move rightwards and change state to q9, accepting state for n2 >= n1.
      maybe we can let $q_8$ be the final state since we already changes all necessary Xs to 0s.
    - > But on receiving X replace it with 0 and move rightwards and change state back to q0.

      we should *not replace X with 0* for q6 because q7 will "change every X with 0 while moving rightwards" for *the right side*.
      If we also change *the left side* which is done by q6, then we will get $n_1+n_2$ 0s.
      so we have $(q_6,X,q_0,X,R)$

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
        As we can see, it has the wrong number of 0s.
      - If we use $(q_6,X,q_0,X,R)$, then based on the above process, we have
        $$
        q_0 0^{n_1}C 0^{n_2} \mapsto^* X^{n_1} q_0 C X^{n_1} 0^{n_2-n_1} \mapsto^* X^{n_1} C q_9 0^{n_2}
        $$
      - Then 
        > From state q3, keep moving left on receiving 0 or C and on receiving X, replace X with 0 and move leftwards.

        It also needs to be changed because this will change all X to 0s which also gets $n_1+n_2$ 0s.
        - To remove $C$ as the askfilo link does and remove the above error,
          we can use $(q_3,C,q_{10},X,L),(q_3,X,q_3,X,L)$ for 
          $q_3$ ~~which only changes the right side Xs to 0s.~~
          and $(q_{10},0,q_{10},0,L),(q_{10},X,q_{10},0,L),(q_{10},B,q_{4},B,R)$ ~~which stops earlier when meeting the rightmost X instead of going back until the left end.~~ It changes all 
          Xs in the $n_1$ original 0s to 0s.
          - Here I follow askfilo by removing the delimiter $C$.
            - So we should have $(q_0,C,q_7,X,R),(q_7,B,q_8,B,L)$,
              removes $q_9$ and let $q_8$ be accepted since we have already changed all necessary Xs to 0s when $q_8$ for 
              $q_{7\sim 9}$.
    - The special case $n_1=0$ or $n_2=0$ can be also verified similarly.
      Or in some way $n_2=0$ case is included in $n_2<n_1$ when $n_1\neq 0$ 
      $$
      q_0 0^{n_1}C B (X^{n_2} q_0 0^{n_1-n_2} C X^{n_2})
      $$
      which skips the 1st step $q_0 0^{n_1}C 0^{n_2} \mapsto^* X^{n_2} q_0 0^{n_1-n_2} C X^{n_2}$
      - and $n_1=0$ is included in $n_2 \ge n_1$
        $$
        q_0 C 0^{n_2} (X^{n_1} q_0 C X^{n_1} 0^{n_2-n_1})
        $$
        which also skips the 1st step
        if we also have $n_2=0$, then we also skips $X^{n_1+1} q_7 X^{n_1} 0^{n_2-n_1} \mapsto^* X^{n_1+1} 0^{n_2} q_7 B$ and have $q_0 C B\mapsto X q_7 B\mapsto q_8 X B$
      - Then when $n_{1,2}\neq 0$ we can get $X^{n_2} q_0 0^{n_1-n_2} C X^{n_2}$ or 
        $X^{n_1} q_0 C X^{n_1} 0^{n_2-n_1}$ and the rest sequence is **definite**.
  - Also see [this](https://askfilo.com/user-question-answers-algebra-2/construct-a-turing-machine-that-computes-the-function-for-35383437353333) which is same as the book ans
    - > If it's the former, then you know that the second input,
      similar to geeksforgeeks, it should be "latter" which meets $\ast$
    - > The five-tuples for this much are: ... $(s_0,\ast,s_5,B,R)$ ...
      This "erase the larger input entirely".
    - > The following transitions accomplish this: ... $(s_5,B,s_5,B,L)$
      it should be $(s_6,B,s_6,B,L),(s_6,0,s_7,0,L),$
    - The last 3 transitions should be $(s4, ∗, s8, B, L), (s8, 0, s8, B, L), (s8, 1, s8, B, L)$
    - In summary
      - when $n_1<n_2$
        the 1st sequence five-tuples removes $\ast,0,1$ of the $n_2$ part
        2nd sequence changes $n_1$ part back to 1s which will move until the rightmost B at the left of the $n_1$ part.
      - ~~continue the iteration~~ forwards to the end after changing the left part of the pair of 1s by the 3rd sequence
      - continue the iteration by the 4th sequence
      - $n_1\ge n_2$
        > change the  0′ s in the second input string back to 1's and then erase the asterisk and remnants of the first input string.
        similar to $n_1<n_2$
        where $(s_4, 0, s_4, 1, L)$ changes the 
        $n_2$ part back.
        Here again we "will move until the rightmost B at the left of the $n_1$".
- [ ] 26
  - similar to EXAMPLE 4, we just removes one less 1
    by $(s_1, ∗, s_3, B, R),(s_1, 1, s_2, B, R)\to (s_1, ∗, s_3, 1, R),(s_1, 1, s_2, 1, R)$
  - see the ans which removes two 1s and adds one 1 having the same result as the above where removes only one 1.
- [x] 28
  - IMHO, after doing $f_1$, we should ~~move to~~ halts at the **left end** which implies the "the *start* state 
  of T2".
    So it the machine halts at the right end or in the middle of the string as [geeksforgeeks_max_f_n1_n2] $q_8$ does.
    - Here exercise 18 will halt at the rightmost $B$ at the left of the original string.
      So if we follow the preamble, it will have $(s_2; B; s_{0}'; 1; L)$, but we may 
      go *left* unnecessarily for $B$ in the $B111\cdots$ due to $(s_0', B, s_1, B, L)$
    - It is said in the ans
      > The only catch is that the tape head needs to *be back at the leftmost 1*
  - TODO [more formal description](http://staff.um.edu.mt/afra1/teaching/coco3.pdf)
- [ ] 31
  - I tried
    $(s_0,B,s_1,1,R),(s_1,B,s_1,1,L),(s_1,1,s_0,1,L)$
    which has
    $s_0B\mapsto 1 s_1 B\mapsto s_1 11\mapsto s_0 B11\mapsto^* s_0 B1111$
    unluckily it doesn't halt because $(s_0,1)$ can't be met.
  - > $(s_0, B, s_1, 1, L), (s_0, 1, s_1, 1, R), (s_1, B, s_0, 1, R)$
    $s_0B\mapsto s_1 B1\mapsto 1 s_0 1\mapsto 1 1 s_1 B\mapsto 111 s_0 B\mapsto 11 s_1 11$
  - Also see [this](https://en.wikipedia.org/wiki/Busy_beaver#Visualizations) for the Visualization of the TM
    although [$BB(2)\le 4$ may be difficult (TODO)](https://mathoverflow.net/a/91524).
- [ ] 32
  - use the halting problem which ~~isn't dependent of~~ doesn't care about the state ~~number~~ count.
    - 1
      > The blank tape halting problem is equivalent to the standard halting problem
      see [this](https://cs.stackexchange.com/a/41240/161388)
      - trivially $\langle M_w \rangle$ *functions same as* $\langle M,w \rangle$
        so $T(\langle M_w \rangle)$ decides whether $M_w$ halts
        means same as $R(\langle M,w \rangle)$ decides whether $\langle M,w \rangle$ halts
        which is one contradiction.
        > But this would decide $HALT_{TM}$
    - [2](https://www.jeremykun.com/2012/02/08/busy-beavers-and-the-quest-for-big-numbers/) from [this](https://cs.stackexchange.com/q/52949/161388) (notice the reference has been changed after this QA is asked)
      - > M determines in finite time the number of states that T has
        same as [getting the cardinality of the set](https://cs.stackexchange.com/a/93326/161388)
        TODO so how to use one TM to implement this?
      - See [this](https://cs.stackexchange.com/a/167013/161388)
      - Also see [this](https://cs.stackexchange.com/a/75590/161388) which is same as [this](https://qr.ae/pstNsf) "If we could compute $\text{max_steps}(n)$".
  - [contradiction](https://cs.stackexchange.com/a/75615/161388) without using other prerequisite theorems for [$BB(n)/S(n)$](https://cs.stackexchange.com/questions/52949/understanding-proof-for-busy-beaver-being-uncomputable#comment345879_95517)
    - Here $n_0$ may be $f(n)$ hinted by The_New_Turing_Omnibus which doesn't influence "the phase of cleaning will continue at least S(N) steps".
    - > But the phase of cleaning will continue at least S(N) steps
      because at most remove [one symbol at one time](https://en.wikipedia.org/wiki/Turing_machine#Description).
      > move the tape left and right one (and *only one*) cell at a time
    - similarly for [$\Sigma(n)$](https://cs.stackexchange.com/a/57153/161388)
  - Notice both of the above 2 methods are included in [wikipedia](https://en.wikipedia.org/wiki/Busy_beaver#Proof_for_uncomputability_of_S(n)_and_%CE%A3(n))
  - [The book answer reference](https://proofwiki.org/wiki/Book:A.K._Dewdney/The_New_Turing_Omnibus:_Sixty-Six_Excursions_in_Computer_Science) -> problem 39 p281
    - This contradiction is based on the *growing* function instead of the *maximal* property for one *n-state* machine as the above.
    - $\Sigma(n)$ is finite because of [the halting assumption](https://en.wikipedia.org/wiki/Busy_beaver#The_busy_beaver_function_%CE%A3)
    - > since $\lceil \log n\rceil$ states are required by A
      [See](https://math.stackexchange.com/a/3067710/1059606)
      > The final state halts instead of moving the tape
    - > Turing machine write binary notation of one number
      [this](https://stackoverflow.com/a/4669482/21294350)
      after wring each symbol to "the output tape" we do one $>>$ operation
      e.g. $11(1011)>>1=5(101)$
      - ~~So we at least can have $\lceil \log n\rceil$ states where each state.~~ TODO
      - Here I only constructs one tape of the 2-tape machine
        $$
        (s_0,0,s_1,-,R),(s_0,-,s_4,-,R),(s_0,\#,s_2,\#,L)\\
        (s_4,-,s_4,-,R),(s_4,0,s_1,-,R),(s_4,\#,s_{11},\#,L)\\
        (s_1,0,s_6,-,R),(s_1,-,s_1,-,R),(s_1,\#,s_2,\#,L)\\
        \text{Here }s_0\text{ means the leftmost state}\\
        s_1:\text{means impossibly all -'s and find odd 0s}\\
        s_4:\text{means possibly all -'s and even 0s}\\
        s_6:\text{means impossibly all -'s}\\
        s_2:\text{meet the right end and go back}\\
        s_{11}:\text{the accepted state}\\
        (s_2,0,s_3,-,L),(s_2,-,s_8,-,L),(s_2,\#,s_0,\#,R)\\
        (s_8,-,s_8,-,L),(s_8,0,s_3,-,L),(s_8,\#,s_{11},\#,R)\\
        (s_3,0,s_{10},-,L),(s_3,-,s_3,-,L),(s_3,\#,s_0,\#,R)\\
        \text{similar to the above but with the reverse direction}
        $$
    - Then based on the above
      We go from right to left for `A`, then from left to right based on `B` assumption, and then from right to left until meeting the 1st blank symbol, and at last we use `C`.
    - $B_n$ writes $\Sigma(n)$ in *unary* notation while 
      $B$ is in *binary*
    - ~~TODO why here $q$ is constant which is related with the *busy beaver function*?~~
      Since $B$ can computes $\Sigma(n),n\in\mathbb{N}$
      its state count can't be $f(n)$ otherwise it can't compute 
      $\Sigma(n)$ which implies it is constant.
    - > let $C$ be ... turing machine converts binary to unary
      this has possibly the [constant state count](https://cs.stackexchange.com/a/156672/161388) -> [this](https://turingmachine.io/?import-gist=2787f81fa4b88c4eef65d4fd85c6423f)
    - In summary
      > prints as many 1s ...
      means $\Sigma(m)\ge \Sigma(n),n>m=\lceil\log n\rceil+q+r$ which contradicts with the trivial conclusion that adding the state count must *strictly* adding the corresponding $\Sigma(n)$.
      Here trivially we need $n$ much bigger so that $n-\lceil\log n\rceil$ can be much bigger so that 
      it is bigger than $q+r$.
    - non-computable may be slower by the [intentionally construction](https://mathoverflow.net/q/346853)
      similarly for the [fastest growing function](https://cs.stackexchange.com/questions/4678/is-busy-beaver-the-fastest-growing-function-known-to-man#comment9998_4678)
    - > For any integer n such that n > flog nl + q + r, machine ABCprints just as many ls as En and yet uses fewer states
      ~~Here ABC are all FTMs, so computable~~ See [this](https://www.physicsforums.com/threads/proof-that-bb-k-grows-faster-than-any-computable-function.945666/post-5986544)
      - The book seems to only prove
        > The busy beaver problem *cannot be solved* in general by a computer
    - miscs:
      the halting problem doesn't care about provability but [decide](https://en.wikipedia.org/wiki/Halting_problem#Background)/determine in the book.
### supplementary
- 16 skipped
- [ ] 2 see the ans
  here to generate $0^{2^n}$
  we doe as follows:
  $$
  \begin{align*}
    S&\to \overbrace{D\cdots D}^{n\;\text{times}}0E\\
      &\to \overbrace{D\cdots D}^{n-1\;\text{times}}00DE\\
      &\to \overbrace{D\cdots D}^{n-2\;\text{times}}0000DDE\\
      &\to \overbrace{D\cdots D}^{n-k\;\text{times}}\overbrace{00\cdots 00}^{k\text{ times }00}\overbrace{D\cdots D}^{k\;\text{times}}E\\
      &\to 0^{2^n}\overbrace{D\cdots D}^{n\;\text{times}}E\\
      &\to 0^{2^n}
  \end{align*}
  $$
- [ ] 4 here we use [formal_proof_generate_Language]
  $$
  \begin{align*}
    M_0=&S\mid A\mid \lambda\quad\text{Notice S to make I.A. work}\\
    M_1=[A]B^n\quad\text{Here [A] means 0 or 1 A}\\
    M_2=[A](A)^{n-k}B^k\quad\text{Notice here we assume the latter }B^k\text{ doesn't generate (A)}\\
    \text{Then for A we do as M_{0\to 1\to 2} as before while }B^k\text{ is trivially balanced.}
  \end{align*}
  $$
  Notice the above $M_i$ is not complete for all members in $\theta(G)$ due to nesting of 
  $A\to B,B\to (A)$
  - See [this](./13_supplementary_4.md) which has links [1][2_methods_for_balanced_parethesis] [2](https://cs.stackexchange.com/questions/153049/prove-that-the-grammar-s-rightarrow-sss-epsilon-generates-precisely-all-we#comment346785_153049) where [formal_proof_generate_Language] ~~can't be easily applied here.~~ needs to be combined with induction to show $\subseteq,\supseteq$
- [ ] 6 see the ans
  - initially I tried to show 2 derivations are same but it is not trivial.
  - either $S\to 0$ ends or $S\to 0S$ continues.
- [ ] 8 see the ans for the strict proof
  - d is wrong because AB is excluded for the right.
- [ ] 10 see the ans
- [ ] 12
  - a) $(0\cup 1)^\ast$
  - b) $0(01^\ast)0$ because the consecutive 2 0s can be anywhere.
  - c) $(0\cup 1)^\ast$ ~~since $10$ can be got from 0 and then 1. so all 2-bit strings are possible.~~ since $(0^\ast\cup 1^\ast)\ast$ has already contained all needed things.
  - Similar to [formal_proof_generate_Language] we can prove the equality.
  - TODO prove b) [can't be star height 1](https://core.ac.uk/reader/82286780). The above b) proof allows $01^\ast01^\ast$ which is wrong.
- [ ] 14
  - nondeterministic finite-state machine see [this p5](https://people.computing.clemson.edu/~goddard/texts/theoryOfComputation/3a.pdf) where we may end up at A or the accepted state D.
- [ ] 17
  - hinted by 18,
    a) $n^{nk}\cdot m^{nk}\cdot n$
    b) similar to a).
- [ ] 18 see the ans
  - a) should not use $|S|\cdot|I|\cdot|S|$ but 
    $|S|^{|S|\cdot|I|}$
  - b) similar to a) $(2^n)^{nk}\ldots$
- [ ] 20 see the ans here is not the question being wrong.
- [ ] 22 see the ans
  - a) here doesn't mean the 0's and 1's are interrupted by the other number.
  - c) here $\varnothing$ is to ensure the possible start of 1 or end of 0.
- [ ] 23 see the ans
- [ ] 24 see the ans
- [ ] 25
  - a) I lacks the loop of $s_5$ and adds $s_3\xRightarrow{0} s_7$ where $s_7$ is the sink non-final state.
  - b) I lacks 2 final states $s_{2,5}$
    here $s_{1,2,3}$ means odd-1,even-10,odd-101.
    similarly for $s_{5\sim 7}$
    then $s_{0}$ means even-no_pattern and $s_{4}$ means odd-no_pattern.
  - c) IMHO the answer is wrong because it allows 0110 as valid but not for 1010 where both have 0's or 1's interrupted.
    See [overleaf_automata]
- [x] 26
  Similar to [this](https://en.wikipedia.org/wiki/Pumping_lemma_for_regular_languages#Use_of_the_lemma_to_prove_non-regularity), let $w=0^{2^{\lceil\log p\rceil}}>0^{p}$. Then we can recognize 
  $0^{2^{\lceil\log p\rceil}+m},m<p<2^{\lceil\log p\rceil}$. So the power is not one $2^n$.
- [x] 27 same as 26 where the nonconstant difference implies 'not regular'.
- [x] 28
  - [proof](https://en.wikipedia.org/wiki/Pumping_lemma_for_context-free_languages#Formal_statement)
    > must contain some nonterminal ${\displaystyle N}$ twice on some tree path
    This is based on the left part can be [only one non-terminal](https://en.wikipedia.org/wiki/Chomsky_hierarchy#The_hierarchy).
  - $1^n\to 1^{n+k}$ while keep the number of 0 and 1.
- [x] 29 similar to 13.5-25.
- [x] 30 compared with 29, following [this](https://cs.stackexchange.com/q/166994/161388) we change all Xs to Bs to keep $n_2-n_1$ hhen $n_2\ge n_1$ and change all symbols to Bs (i.e. moves back to then left end from the right end when finding no 0) when $n_2< n_1$.
  - see the ans where it *just erases instead of marking first*.
    $(s3; B; s0; B; R)\to (s0,∗,s5,1,L)$ will "replace the asterisk by a 1" after erasing all necessary bits.
    $(s2; ∗; s4; B; L)\to (s4; 1; s4; B; L)\to^{*} (s4; B; s5; 1; L)$ will earse all and then add one 1.
    - Notice the mark is necessary to recover $n_{1,2}$ otherwise we will end up in one loop where all the left part is B (maybe we can add one left and right end mark instead of all X mark.)
## Appendix
### 1
- 1,2,3,10 skipped
- [ ] 4
  - we can also use $-1\cdot (x+y)$ to prove.
- [ ] 6 $(x+z)-(y+z)=0=x-y$
- [ ] 8 just add $y/-y$ for 2 sides.
- [ ] 12 notice the situation where $\frac{1}{x}=0$
- [ ] 14
  - Although we can prove by thinking of 3 situations where $x\cdot y =/</> 0$
    the answer is more elegant.
- [ ] 15
  - it suffices to show $(x-y)\cdot z<0$ which can be got from $z<0$.
  - see the ans
    > if z < 0, then −z > 0
    because $z+(-z)=0$
- [ ] 16 see the ans
  - Here assumes $x^2<0$ is impossible.
- [ ] 18 we can also prove by excluding the situations where $\frac{1}{x} =\text{ or }< \frac{1}{y}$
- [ ] 19,20 see the ans
- [ ] 21 see the ans
  - See p970 for how to construct 'the set of real numbers'.
  - see the ans
    Here 'well-defined' is to show whatever 'the representative of the equivalence classes chosen' the result is same.
  - Here $(w, x)$ 
    [means integer $x-w$](https://qr.ae/psobsD), also [see](https://math.stackexchange.com/a/413834/1059606)
- [ ] 22
  - similar to 21, this means rational $\frac{w}{x}$.
    the proof is also similar.
  - > the set of real numbers can then be constructed from the set of rational numbers
    use one [~~convergent sequence~~Cauchy sequence](https://en.wikipedia.org/wiki/Construction_of_the_real_numbers#Construction_from_Cauchy_sequences) whose difference trivially tends to be zero. 
    - Notice this is not same as convergent sequence due to [the set definition in metric space](https://www.math.nagoya-u.ac.jp/~richard/teaching/f2021/SML_LFJO_2.pdf)
      This implies
      > A standard procedure to force all Cauchy sequences in a metric space to converge is *adding new points* to the metric space in a process called completion.
    Here based on $(x_n)+(y_n)=(x_n+y_n)$ 'well-defined' is trivially proved.
    - from $l = u$ and $b<l\Rightarrow b<l_n$, we have
      > u is a least upper bound for S
### 2
- all skipped
### 3
- [ ] 2 trivially at least 2 for each assignment, but we need at least one more to ensure  correctness.

---

<!-- note inner link -->
[submat_equivalence_relation]:#submat_equivalence_relation
[equivalence_relation_definition]:#equivalence_relation_definition
[transitive_reflexive]:#transitive_reflexive
[lexicographic_order_partial_order_proof]:#lexicographic_order_partial_order_proof
[well_founded_diff_well_ordered]:#well_founded_diff_well_ordered
[graph_link_with_relation]:#graph_link_with_relation
[unique_start_euler_path]:#unique_start_euler_path
[find_euler_path_based_on_circuit]:#find_euler_path_based_on_circuit
[cycle_branch_out_WITH_proof_after_reaching_cycle]:#cycle_branch_out_WITH_proof_after_reaching_cycle
[directed_graph_detecting_cycle_proof]:#directed_graph_detecting_cycle_proof
[u_first_in_the_white_path]:#u_first_in_the_white_path
[one_cycle_when_tree_plus_one_edge]:#one_cycle_when_tree_plus_one_edge
[Prim_find_incident_edge]:#Prim_find_incident_edge
[MST_scratch]:#MST_scratch
[second_shortest_path]:#second_shortest_path
[MST_construction_process]:#MST_construction_process
[circuit_connect_components]:#circuit_connect_components
[minimum_edge_number_connected_graph]:#minimum_edge_number_connected_graph
[tree_level_recursive]:#tree_level_recursive
[DFS_directed_topological_sorting]:#DFS_directed_topological_sorting
[DFS_construct_tree]:#DFS_construct_tree
[lattice_boolean_algebra]:#lattice_boolean_algebra
[xor_associative]:#xor_associative
[producuction_for_each_nonterminal_one_by_one]:#producuction_for_each_nonterminal_one_by_one

<!-- textbook -->
[SOLUTIONS_8th]:./Discrete%20Mathematics%20and%20Its%20Applications,%20Eighth%20Edition%20SOLUTIONS.pdf
[SOLUTIONS_7th]:./discrete-structure-solution-student39s-solutions-guide_compress_7th.pdf
[A_Guide_to_Writing_Proofs]:./A_Guide_to_Writing_Proofs.pdf
[stirling]:./papers/stirling.pdf

<!-- codes -->
[miscs_ipynb]:./miscs_snippets/miscs.ipynb
[stirling_numbers_first_kind_simulation]:./miscs_snippets/py_codes/Stirling_numbers_first_kind/stirling_numbers_first_kind_simulation.py
[derangement_code]:./miscs_snippets/py_codes/8-6-12/derangement.py
[check_relations]:./miscs_snippets/py_codes/9-1-46/check_relations.py
[Warshall_code]:./miscs_snippets/py_codes/9_4_Warshall/Warshall.py
[transitive_realtion_check]:./miscs_snippets/py_codes/9-3-8/transitive.py
[Stirling_second_kind_code]:./miscs_snippets/py_codes/8_supplementary_40_Stirling_second_kind/Stirling_second_kind.py
[counting_path]:./miscs_snippets/py_codes/10_4_counting_path/counting_path.py
[nonisomorphic_simple_connected]:./miscs_snippets/py_codes/10_supplementary_32/nonisomorphic_simple_connected.py
[scc]:./miscs_snippets/py_codes/11_4_DFS_Strongly_Connected_Component/scc.py

<!-- exercise help pdf -->
[2_3_37]:./latex_misc_pdfs/Discrete_Mathematics_and_Its_Applications_2_3_37.pdf

<!-- wikipedia -->
[Cantor_diagonal_argument_string]:https://en.wikipedia.org/wiki/Cantor's_diagonal_argument#Uncountable_set
[Schröder_Bernstein_theorem]:https://en.wikipedia.org/wiki/Schr%C3%B6der%E2%80%93Bernstein_theorem#Proof
[Big_O_Notation]:https://en.wikipedia.org/wiki/Big_O_notation#Family_of_Bachmann%E2%80%93Landau_notations
[wikipedia_minimal_element]:https://en.wikipedia.org/wiki/Maximal_and_minimal_elements#Definition
[Depth_first_traversal_3_colors]:https://en.wikipedia.org/wiki/Tree_traversal#Depth-first_search
[backtracking_AND_DFS_imply_preorder]:https://en.wikipedia.org/wiki/Depth-first_search#Vertex_orderings
[full_adder]:https://en.wikipedia.org/wiki/Adder_(electronics)#Full_adder
[Quine_McCluskey_example]:https://en.wikipedia.org/wiki/Quine%E2%80%93McCluskey_algorithm#Step_2:_prime_implicant_chart
[wikipedia_anbncn]:https://en.wikipedia.org/wiki/Context-sensitive_grammar#anbncn
[type_1_grammar]:https://en.wikipedia.org/wiki/Chomsky_hierarchy#Context-sensitive_(Type-1)_grammars
[Chomsky_hierarchy]:https://en.wikipedia.org/wiki/Chomsky_hierarchy#The_hierarchy
[ordered_rooted_tree]:https://en.wikipedia.org/wiki/Tree_(graph_theory)#Ordered_tree
[13_2_definition_1]:https://en.wikipedia.org/wiki/Mealy_machine#Formal_definition
[Dilworth_theorem_proof_wikipedia]:https://en.wikipedia.org/wiki/Dilworth%27s_theorem#Inductive_proof

<!-- brilliant wiki -->
[brilliant_wiki_Dilworth_Theorem_antichain_ge_chain]:https://brilliant.org/wiki/dilworths-theorem/#proof-of-dilworths-theorem
[brilliant_wiki_Dilworth_Theorem_chain_ge_antichain]:https://brilliant.org/wiki/dilworths-theorem/#statement-of-dilworths-theorem-and-mirskys-theorem
[brilliant_wiki_Erdős_Szekeres_Theorem]:https://brilliant.org/wiki/dilworths-theorem/#applications

<!-- math stackexchange -->
[comparison_of_cardinality_for_infinite_must_use_onto_and_one_to_one]:https://math.stackexchange.com/a/4804647/1059606
[lower_bound_second_largest_element]:https://math.stackexchange.com/a/1672/1059606
[consecutive_zeros_in_bit_strings]:https://math.stackexchange.com/a/178613/1059606
[stirling_numbers_first_kind_proof]:https://math.stackexchange.com/q/4824460/1059606
[3_choices_for_each_element]:https://math.stackexchange.com/a/503992/1059606
[Lexicographical_order]:https://math.stackexchange.com/a/165425/1059606
[refinement_lattice]:https://math.stackexchange.com/q/4840241/1059606
[finite_chain_maximum_minimum]:https://math.stackexchange.com/a/3571343/1059606
[not_distributive_lattice]:https://math.stackexchange.com/questions/3198879/boolean-algebra-demonstrate-that-the-pentagon-lattice-is-non-distributive
[2_regular_graph_with_fixed_number_vertices]:https://math.stackexchange.com/a/2490901/1059606
[check_isomorphism_by_matrix]:https://math.stackexchange.com/questions/3899990/matrix-representation-of-graph-to-determine-if-two-graphs-are-isomorphic#comment10316280_3900007
[comparison_edge_connectivity_vertex_connectivity]:https://math.stackexchange.com/a/4843376/1059606
[cut_vertex_Hamilton_circuit]:https://math.stackexchange.com/questions/1958873/hamiltonian-cycle-need-assistance#comment4021120_1958873
[check_Hamilton_path]:https://math.stackexchange.com/a/2442781/1059606
[4xm_knight_tour]:https://math.stackexchange.com/questions/2195746/knights-tour-on-a-4-x-m-board#comment4518180_2195762
[vertex_connectivity_less_than_minimum_degree]:https://math.stackexchange.com/a/453732/1059606
[tree_iff_add_any_edge]:https://math.stackexchange.com/a/420543/1059606

<!-- stack overflow -->
[longest_simple_path_NP_hard]:https://stackoverflow.com/a/53399638/21294350
[BFS_radial]:https://stackoverflow.com/questions/8379785/how-does-a-breadth-first-search-work-when-looking-for-shortest-path#comment47336949_8379892
[BFS_level_order]:https://stackoverflow.com/questions/55243105/breadth-first-search-traversal-vs-pre-order-traversal-vs-depth-first-search-trav#comment137378786_55243795
[DFS_no_cross_edge]:https://stackoverflow.com/a/28942405/21294350
[DFS_no_cross_edge_improvement]:https://stackoverflow.com/questions/28942262/dfs-in-an-undirected-graph-can-it-have-cross-edges/28942405#comment137389481_28942405
[2_methods_for_balanced_parethesis]:https://stackoverflow.com/a/42565842/21294350

<!-- gateoverflow -->
[assign_different_jobs_to_different_employees]:https://gateoverflow.in/79804/permutation-combo?show=80049#a80049

<!-- cs stackexchange -->
[O_Theta_Omega_relation_with_limit]:https://cs.stackexchange.com/a/827/161388
[Graph_space_complexity_vs_time_complexity]:https://cs.stackexchange.com/a/165324/161388
[DFS_only_2_types_edges]:https://cs.stackexchange.com/a/11552/161388
[graph_based_on_explored_set_complexity]:https://cs.stackexchange.com/q/165308/161388
[DFA_partial_transition_function]:https://cs.stackexchange.com/a/12596/161388
[Proof_generate_Language]:https://cs.stackexchange.com/a/110858/161388
[3_basic_tools]:https://cs.stackexchange.com/a/26159/161388
<!-- formal grammars / phrase-structure grammar -> formal languages -->
[formal_proof_generate_Language]:https://cs.stackexchange.com/a/11316/161388
[proof_Turing_Machine_recognize_language]:https://cs.stackexchange.com/a/166984/161388

<!-- paper or lectures -->
[second_largest_element_Adversary]:https://www.cse.unsw.edu.au/~cs2011/lect/2711_Adversary.pdf
[lec_13_parenthesis_theorem_Adversary_Arguments]:https://jeffe.cs.illinois.edu/teaching/algorithms/notes/13-adversary.pdf
[Szwarcfiter_stable_marriage]:https://core.ac.uk/download/pdf/82429549.pdf
[McVitie_stable_marriage]:./papers/McVitie_stable_marriage.pdf
[AHajnal_058]:./papers/AHajnal_058.pdf
[hedetniemi1988]:./papers/hedetniemi1988.pdf
[meisters1975]:./papers/meisters1975.pdf
[Bar_Hillel_Falk]:https://sci-hub.se/https://doi.org/10.1016/0010-0277(82)90021-X
[Ruma_Falk_paper]:https://sci-hub.se/https://doi.org/10.1080/13546783.2011.613690
[a000108_11]:./papers/a000108_11.pdf
[stewart1941]:./papers/stewart1941.pdf
[Hardy_Ramanujan_Asymptotic_Partition_function]:./papers/ram36.pdf
[Hardy_Ramanujan_Asymptotic_Partition_function_orig]:./papers/ram36_orig.pdf
[Alternating_Sums_A_Method_to_DIE]:./papers/Alternating_Sums_A_Method_to_DIE.pdf
[graph_theory]:./papers/graph_theory.pdf
[galvin]:./papers/galvin1994.pdf
[Cynthia_and_Chahat]:./papers/Cynthia_and_Chahat.pdf
[huffman_1952_minimum_redundancy_codes]:./papers/huffman_1952_minimum-redundancy-codes.pdf

<!-- other misc links -->
[Dilworth_theorem_proof_combination]:https://web.vu.lt/mif/s.jukna/EC_Book_2nd/dilworth.html
[duality_onto_with_one_to_one]:http://www.randomservices.org/random/foundations/Functions.html#aoc
[path_in_order_theory]:https://math24.net/closures-relations.html
[find_euler_path_undirected_path]:https://cp-algorithms.com/graph/euler_path.html#:~:text=To%20find%20the%20Eulerian%20path%20%2F%20Eulerian%20cycle%20we%20can%20use,then%20remove%20the%20extra%20edge.
[cut_edge_2_components]:https://sharmaeklavya2.github.io/theoremdep/nodes/graph-theory/deleting-bridge-gives-2-components.html
[cstaleem_0_n_1_n]:https://cstaleem.com/turing-machine-for-0n1n/


<!-- wolfram -->
[connected_planar_simple_graph]:https://mathworld.wolfram.com/PlanarConnectedGraph.html
[wolfram_GraphThickness]:https://mathworld.wolfram.com/GraphThickness.html

<!-- lectures -->
[Fleury_Algorithm_proof]:./lectures/Proofs_BM_GT_3_3.pdf
[even_graph_no_cut_edge]:https://www.people.vcu.edu/~rhammack/Math591/Homework/M591Hw3.pdf
[find_euler_circuit_undirected_path]:https://math.unm.edu/~loring/links/discrete_f05/euler.pdf
[Fleury_Algorithm]:https://jlmartin.ku.edu/courses/math105-F11/Lectures/chapter5-part2.pdf
[incl_excl_n]:./lectures/incl_excl_n.pdf
[Kuratowski]:./lectures/Kuratowski.pdf
[Xuyifan_Kuratowski]:./papers/Xu,Yifan.pdf
[lec_13_parenthesis_theorem]:./lectures/Lecture-13.pdf
[lec_14]:./lectures/Lecture-14.pdf
[lecture10_notes]:./lectures/lecture10-notes.pdf
[tree_imply_all_cut_edge_i_e_no_circuit]:https://web.math.ucsb.edu/~padraic/ucsb_2013_14/math137a_w2014/math137a_w2014_lecture3.pdf
[white_path_3_colors]:https://www.clear.rice.edu/comp314/lec/week3/Depth-First.htm
[primsproof]:./lectures/primsproof.pdf
[Boruvka_proof]:./lectures/MST.pdf
[safe_edge_MST]:https://courses.engr.illinois.edu/cs374/fa2015/slides/18-mst.pdf
[kahn_proof]:https://www.cs.nthu.edu.tw/~wkhon/ds/ds11/lecture/lecture12.pdf
[uchicago_0_n_1_n]:https://www.classes.cs.uchicago.edu/archive/2015/winter/28000-1/Lec13.pdf
[yale_Fundamental_Theorem_for_Win_Lose_Games]:https://oyc.yale.edu/sites/default/files/blackboard15_0_0.pdf
[2_conditions_for_Balanced_Parentheses]:http://cse.iitkgp.ac.in/%7Eabhij/course/theory/FLAT/Spring21/scribes/CFG-balanced.pdf
[DAG_to_topological_ordering_proof]:http://www.cs.emory.edu/~cheung/Courses/253/Syllabus/Graph/DAG.html

<!-- csapp -->
[csapp_doc]:https://github.com/czg-sci-42ver/csapp3e/blob/master/asm/README.md

<!-- tex -->
[main_tex]:./homework_tex/algorithm/main.tex
[chapter_10_5_tex_code]:https://www.overleaf.com/read/nwtjtmjnxxtn#2223d5
[overleaf_automata]:https://www.overleaf.com/read/rbntjpdjrjmx#2a20cd

<!-- textbook -->
[Graph_Theory_with_Applications]:./other_related_maths_book/BondyMurtyGTWA.pdf
[graph_theory_graduate_textbook]:./other_related_maths_book/graph_theory.pdf
[Artificial_Intelligence_A_Modern_Approach_3rd]:./other_books/Artificial_Intelligence_A_Modern_Approach/Artificial_Intelligence_A_Modern_Approach_3rd.pdf
[Artificial_Intelligence_A_Modern_Approach_4th]:./other_books/Artificial_Intelligence_A_Modern_Approach/Artificial.Intelligence.A.Modern.Approach.4th.Edition.Peter.Norvig.Stuart.Russell.pdf
[the_nature_of_computation]:./other_books/the-nature-of-computation-1nbsped-0199233217-9780199233212_compress.pdf
[algebraic_graph_theory]:./other_books/algebraic_graph_theory.pdf
[Elements_of_Theory_of_Computation_2ed_Lewis_Papadimitriou]:./other_books/Elements_of_Theory_of_Computation_2ed_Lewis_Papadimitriou.pdf
<!-- J. E. Hopcroft, R. Motwani, and J. D. Ullman, Introduction to Automata Theory, Languages, and Computation -->
[Introduction_Automata_Theory_Languages_and_Computation]:./other_books/Introduction_Automata_Theory_Languages_and_Computation.pdf 
[introduction_to_number_theory]:./other_books/introduction-to-number-theory-bad-scan-3rd-printingnbsped_compress.pdf

<!-- geeksforgeeks -->
[Detect_cycle_Directed_Graph]:https://www.geeksforgeeks.org/detect-cycle-in-a-graph/
[geeksforgeeks_max_f_n1_n2]:https://www.geeksforgeeks.org/turing-machine-to-accept-maximum-of-two-numbers/

<!-- valuable links -->
[houseofgraphs_search]:https://houseofgraphs.org/result-graphs

[asm_doc]:https://github.com/czg-sci-42ver/csapp3e/blob/master/asm/README.md