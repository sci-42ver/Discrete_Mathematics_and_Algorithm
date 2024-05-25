1. One small error: we should say "$g(u)$ is bounded below by $c_1 g(x)$" 2. $M$ is one function of $x$ when $p(x)$ is strictly increasing. Then how do we know there is one upper bound for $M(x)$? 3. How do we have $c_1g(x)\le 1\Rightarrow c_1g(x)\le g(u)$? 4. How to get "the minimum polynomial value bounding $|g'(x)|$"? The problem says "upper bounded" but not "lower bounded". 5. I want to prove "polynomial-growth condition" instead of "already established ... satisfies the polynomial-growth condition" and then give one circular proof.

Thanks anyway for your answer. Hope you can clarify based on my doubts.

Why do you use this changed definition? IMHO the original definition is enough for application. Your definition is more general while the original paper needs $x_0\ge 1/b_i$, etc, to ensure the *induction* proof work (See p3 bottom).

# mcs
- Here I didn't care about more circuit knowledge than already learnt since it is too complex to design one by myself. (skip_circuit)
- Here * sections mean that they are not included in Discrete_Mathematics_and_Its_Applications.
- This book skips most of state machines and Turing machine with only one chapter 6.
- Theorem 8.2.2 is same as DMIA 3.1.6 which finds one *counterexample* using .
  ~~$lang(s)\to H(P,P)$~~ ~~and~~ $s_0=K$
  $s\in/\notin lang(P)$ means halt or not.
  - > Following the usual diagonal approach, we define the language No-halt:
    Here we *iterate over all recognizers* like $A_k$ in the original proof.
    And finds strings not ~~related with~~recognized by all these recognizers like $C$ in the original proof.
    Compared with the original proof
    $\exists m, C=A_m\iff C[k]\neq A_k[k]$ which is wrong because $C[m]=A_m[m]$ contradicts with RHS.
  - > A language is called recognizable when it equals lang.P / for some string procedure P 
    so 'not recognizable' -> 'not halt', i.e. no  program can halt when input such one string/language.
  - DMIA 3.1.6 is almost same as [this](https://math.stackexchange.com/q/867491/1059606) where `K(K)` is the nested `paradox()`.
    - > there must be a program e that computes g, by the assumption that the model of computation is Turing-complete.
      'Turing-complete' ensures the existence of `e`.
- TODO why 'No-halt' string set is 'non-halting Java programs'
  maybe it is probably one
  $\text{No-halt} \Coloneqq \{s\vert P_s \text{applied to s does not halting}\} = \{s \notin lang(Ps)\}:(8.3)$
- This books seems to have much more typos than DMIA (even wrong hints like Problem 6.6...) and it has many ambiguous description (TODO give one specific example of such one ambiguous description).
  - typo like "more than $\sqrt{n}$ steps" in p361.
## notice
- I only did problems *referred to in the main contents* because some of them are very interesting and Enlightening.
  IMHO they are probably not in IN-CLASS QUESTIONS and ASSIGNMENTS, so not in this [solution](https://github.com/spamegg1/Math-for-CS-solutions?tab=readme-ov-file).
- starting from checking problems in chapter 8 where I have read up to 9.3 finished in mcs.pdf,
  I began reading mcs_2018.pdf (difference between these 2 books see `compare_bmk.awk`)
  TODO compare these [2 files](https://www.adobe.com/acrobat/how-to/compare-two-pdf-files.html)
  - The migration may probably began from commit e7d0044d95aa8675c19af4745f24084e7080a59e to .
- From 9.6, if "Lemma 9.6.1", etc, are highlighted, it means their proofs are skipped because of  duplicity with DMIA.
- For some chapters like chapter 17 I read their prefaces (probably from 1 to 16 I all read their prefaces), but not for others. (The detailed list is not recorded since when reading mcs I forgot when I began reading prefaces and when I mistakenly discontinued.)
### relation with 6.042J 2019
- currently the following chapter_1-3 problems, chapter_2-2 problems are not in IN-CLASS QUESTIONS or ASSIGNMENTS.
### theorem
- proofs which I learnt in DMIA may be skipped.
  - Theorems proved in DMIA but not in mcs are also skipped.
### solution
- As [this](https://github.com/ossu/computer-science/issues/1090#issuecomment-1282535965) says, the problem may be easy although some are not. But most of them give one detailed hint sequence.
### Comparison with DMIA
- Although it skips some complex proofs like that for Kuratowski’s Theorem, it shows more infos about why we use some definitions or theorems, e.g. confidence (not said in DMIA) vs probability.
- mcs gives very useful hints for Problems, so that they are easier than DMIA exercises although they are harder without hints.
## diff between 2017 and mcs 2018
```bash
$ summary=0;id2c "./compare_bmk.awk -v summary=$summary mcs.bmk" "./compare_bmk.awk -v summary=$summary mcs_2018.bmk" | less_n
      1 /proc/self/fd/11                                                                              /proc/self/fd/12                                                                             1       
      2 last chapter-6.4:6                                                                            last chapter-6.4:6                                                                           2       
      3 7.1:4                                                                                         7.1:4                                                                                        3       
      4 7.2:4                                                                                         7.2:4                                                                                        4       
      5 7.3:2                                                                                         7.3:2                                                                                        5       
      6 7.4:5                                                                                         7.4:5                                                                                        6
      #  The diff is mainly the contents before Definition 7.5.1
      7 7.5:4                                                                                         7.5:6                                                                                        7       
      # The whole chapter is the diff
      8                                                                                               7.6:19                                                                                       8       
      9 last chapter-7.6:1                                                                            last chapter-7.7:1                                                                           9       
     10 8.1:9                                                                                         8.1:9                                                                                       10       
     11 8.2:4                                                                                         8.2:4                                                                                       11       
    #  8.3 diff is mainly at 8.3.2
     12 8.3:4                                                                                         8.3:5                                                                                       12       
    #  They are mostly same but with one different layout (i.e. one spreading 2 pages while the other spreading 3).
     13 last chapter-8.4:1                                                                            last chapter-8.4:2                                                                          13       
     14 9.1:5                                                                                         9.1:5                                                                                       14       
     15 9.2:7                                                                                         9.2:7                                                                                       15       
    #  A Prime for Google is put in one different location where the `icdiff mcs-unlocked.txt mcs_2018-unlocked.txt` shows as the diff of deleting and adding '9.4 The Fundamental Theorem of Arithmetic' preface at one different location.
     16 9.3:2                                                                                         9.3:3   
     17 9.4:3                                                                                         9.4:2
    #  The rest is same until 9.11: which I have not read when compare these 2 pdf's.
```
## 1.1~1.8 skipped except for some problems
- Problem 1.26
  - a) trivial
  - b) based on a)
  - c) see [this](https://math.stackexchange.com/q/3552533/1059606).
  - This is same as DMIA 4-supplementary-23 which is same as the [remark](https://math.stackexchange.com/a/304348/1059606).
- Problem 1.15
  splitting into cases are enough.
- Problem 1.16
  $n=4,m=8$
  $n=6,m=4$
- Problem 1.2 referred to by 9.1.3 Die Hard skipped due to that it is only to be as one reference of "the convention ... the nonnegative square root".
- Problem 1.13 is skipped due to triviality.
- 1.14
  - (a) if not even, then $n^2$ is odd.
  - (b) similar since $3=1\cdot 3$.
- ~~1.15~~
## 2.1
- p30 here 
  > the fraction m0=p n0=p cannot be in written in lowest terms either
  is because it equals $\frac{m_0}{n_0}$.
- Theorem 2.2.1 here the *minimal element* is similar to the *base* of induction.
## 2.3
- DMIA uses induction which is same as 5.2.3 (I only give one brief overlook) while the book uses WOP although they are equivalent.
## chapter 2 problems
- Problem 2.20
  $n_s$ is the main part,
  so $n_s+f$ is the minimal family among $n+f$
  then $n_s+f_s$ is the minimal element in this family.
- Problem 2.23 referred to in chapter 6.
  - see [this](https://math.stackexchange.com/a/3548169/1059606) which uses contrapositive to prove.
    - well ordered [implies](https://math.stackexchange.com/a/2756184/1059606) total order
## 3 preface
- > we’ll come across the most important open problem in computer science
  may mean SAT
  > It turns out that an efficient solution to SAT would immediately imply efficient solutions to many other important problems
## 3.1
- Here
  > mathematical implications ignore causal connections
  helps ignoring $C_i,i\neq 2,5$ which can therefore extract $C_i,i=2,5$.
## 3.5
- > as with testing validity, this approach quickly bogs down for formulas with many variables
  See 3.3.2
  > There is also a close relationship between validity and satisfiability: a statement P is satisfiable iff its negation NOT.P / is not valid.
- > validity testing is a special case of determining if a formula simplifies to T.
  i.e. all T is one subset of existing one T.
## chapter 3 problems
- Problem 3.16
  - a) 
    $$
    \begin{align*}
      \neg L&\to Q\\
      \neg L&\to B\\
      \neg L&\leftrightarrow N\\
      \text{the above is based on point 1}\\
      \neg Q&\to B\\
      \neg B\\
    \end{align*}
    $$
  - b,c) $B=F\Rightarrow (Q=T,L=T)\Rightarrow N=F$
  - [See](https://www.assignmentexpert.com/homework-answers/mathematics/discrete-mathematics/question-154751) although it only has the correct process for a) and the correct answers for b,c) but not with the correct process.
- Problem 3.6,7 are skipped because they are contained in COD and partly in DMIA.
  And these problems are far from *designing one real CPU* although they are the basis.
- Problem 3.17
  - a) $(A\iff B)=(A \text{ and } B)\text{ or }(\neg A \text{ and } \neg B)$
    xor is similar using the truth table
  - b) [see](https://stackoverflow.com/a/8374918/21294350)
  - c) see DMIA which also contains the above maybe.
- Problem 3.24
  - equisatisfiable diff equivalent see [lec_02](https://lara.epfl.ch/w/_media/fv20/lec02.pdf) from [this](https://lara.epfl.ch/w/fv20/top) ~~which is more readable than~~ which has one different structure but almost the same contents from [2019](https://lara.epfl.ch/w/fv19/top) listed in [this](https://lara.epfl.ch/w/fv)
    - 2019 [lec_03](https://lara.epfl.ch/w/_media/fv19/lec03.pdf)
      - in p14, the latter means $F=T\Leftrightarrow G=T$
        in p13, $FV$ means [all literals p14](https://lara.epfl.ch/w/_media/fv19/lec02-bmc.pdf)
      - propositional logic [compared with syllogistic logic](https://brilliant.org/wiki/propositional-logic/#:~:text=As%20the%20name%20suggests%20propositional,and%20connected%20via%20logical%20connectives.)
        - better see [this](https://lara.epfl.ch/w/sav08/predicate_logic_informally)
    - 2020
      - p17
        see p16 for definition of $FV$ where $\exists$ may introduce [one new variable p8](https://lara.epfl.ch/w/_media/fv20/lec01-main2.pdf).
      - notice here exponentially larger is [only possible][2020_lec_02] but not necessary.
  - b) trivial based on a).
  - notice ["a reduction from 3SAT to Circuit SAT"](https://en.wikipedia.org/wiki/Circuit_satisfiability_problem#Proof_of_NP-completeness) is much more trivial than the converse direction since the former *doesn't need to introduce new variables*.
    - proof based on [this structure](https://stackoverflow.com/a/4294435/21294350) where $P$ needs [one TM](https://en.wikipedia.org/wiki/P_(complexity)#Definition) and NP [doesn't see paragraph 3](https://en.wikipedia.org/wiki/NP_(complexity))
  - a)
    - [example](https://en.wikipedia.org/wiki/Tseytin_transformation#Simple_combinatorial_logic)
      - [CNF sub-expression](https://en.wikipedia.org/wiki/Tseytin_transformation#Gate_sub-expressions), take AND for example.
        - based on CNF sub-expression,
          if $C=T$ then we need $A=B=T$ based on the latter 2 components in conjunction.
          else, we need $(A=F) \lor (B=F)$ based on the 1st component.
          The above is same for "Operation".
      - linear is due to for each gate, we have one *decidable* number of the minimal operation.
        while normally we may [duplicate almost for all literals](https://en.wikipedia.org/wiki/Disjunctive_normal_form#..._by_semantic_means) (also can be got due to [recursive p25][2020_lec_02] [distributive property](https://en.wikipedia.org/wiki/Tseytin_transformation#Motivation)) instead of using one variable to substitute some groups of them.
        - also see [this](http://courses.csail.mit.edu/6.892/spring19/psets/ps4sol.pdf)
          > Each vertex and edge in the circuit leads to a *constant* amount of the formula, so the blowup is linear
        - [summary](https://en.wikipedia.org/wiki/Circuit_satisfiability_problem#The_Tseytin_transformation) where "net" may mean "pin". (I give one brief reading before "Conjoining"). This corresponds to the problem
          > to the number of wires
        - notice: based on [this p26][2020_lec_02], the transformed SAT formula has the *same output* as before because each CNF sub-expression is correct (also implied by "translate" in the later link) with that property but with [one *different* valuation](https://personal.cis.strath.ac.uk/robert.atkey/cs208/converting-to-cnf.html#:~:text=Because%20the%20original%20formula%20P,that%20they%20are%20equi%2Dsatisfiable.) $e$.
      - "constant 1" may mean "gate8" variable which needs to be T due to the satisfiability problem.
- Problem 3.25 [(b)](https://math.stackexchange.com/q/4910135/1059606)
  - > After padding all clauses, 2k-1 extra clauses[note 4] have to be appended to ensure that only d1 = ⋯ = dk=FALSE can lead to a satisfying assignment.
    TODO This seems to exclude one situation -> $2^k-1$. But why $2^k$ instead of $2^{k-j}$. and why all "FALSE"?
- ~~3.6 3.7~~
## 4.4 (rephrased using arrows)
- > bijective when it has both the [= 1 arrow out] and the [= 1 arrow in] property.
  See [this](https://math.stackexchange.com/questions/1945015/is-a-one-to-one-function-also-a-total-function#comment10454547_1945015)
- Definition 4.4.4 [see](https://en.wikipedia.org/wiki/Image_(mathematics)#Generalization_to_binary_relations)
## chapter 4 problems
- Problem 4.5 uses [element-chasing](https://web.math.ucsb.edu/~mikew/MAT145Page/Set_Theory_Review.pdf) in the [proof](https://math.stackexchange.com/a/2782336/1059606)
  - Show how union is [analogous](https://math.stackexchange.com/questions/4016966/show-how-union-is-analogous-to-logical-inclusive-or#comment8292345_4016966) to [logical inclusive OR](https://stackoverflow.com/a/22137436/21294350)
- Problem 4.21 (Problem 4.22 in mcs 2018) the reference of Lemma 8.1.3
  - a) trivial due to the transitivity of $\le$
  - b) trivial due to $|A|\ge |B|\Rightarrow |B|\le |A|$
  - c) trivial based on a,b)
  - d) 
    - ~~$\Rightarrow$~~
      do as the following process until $A=\varnothing$
      1. choose one arbitrary element $x$ from $A$ and $y$ from $B$
      2. let $f(x)=y,A=A\setminus \{x\},B=B\setminus \{y\}$
      then $f$ is "a total injective function from A to B".
    - Notice here is to prove from "relation" to "function"
      instead of proving iff.
- Problem 4.10 @#@ (Here @#@ means problems in mcs 2018 whose solution is not certain and not verified)
  $$
  \begin{align*}
    z&\in A-(B\cup C)&\\
     &\iff (z\in A)\land(\neg z\in B\cup C)&(\text{def of }-)\\
     &\iff (z\in A)\land(\neg (z\in B\lor z\in C))&(\text{def of }\cup)\\
     &\iff (z\in A)\land(z\notin B\land z\notin C)&(\text{De Morgan's laws})\\
     &\iff (z\in A)\land(z\in A)\land(z\notin B\land z\notin C)&(a\land a=a)\\
     &\iff (z\in A \land z\notin B)\land(z\in A \land z\notin C)&(\text{Associativity and Commutativity})\\
     &\iff z\in (A-B)\cap(A-C)&(\text{def of }\cap,-)
  \end{align*}
  $$
  - > Explain how, given a set-theoretic equality between two set expressions that is not valid, to *construct a counter-example using any truth assignment* that falsifies the corresponding propositional equivalence
    
    Since we get the final expression, it is easy to show the counter-example or directly show the equality "is not valid". If wanting to make connection with the "truth assignment" anyway, we can use $T\land F\neq T\lor F$ where $(\land,\lor)$ corresponds to $(\cap,\cup)$. Or more  specifically, let $(z\in A \land z\notin B)$ and $(z\in A \land z\notin C)$ have different boolean values.
    ~~We can also use the method implied in the following proof, i.e. .~~
  - > Conclude that any set equality that is valid in a domain of size one will be valid in all domains.
  
    Focus on the 2nd to last equation sequence in p107, we only need to care about each propositional literal like $z\in A$ and the above $\neg z\in A=z\notin A$.
    Then for "a domain of size one" like $\{1\}$ which the problem seems to assume including $\varnothing$
    we choose $z$ as the only element in that set, i.e. $1$ in the above. Then $1\in\{1\}=T,1\in\varnothing=F$. So that for each $z\in A$ we can choose $T$ or $F$.
    Then *all possible* truth assignment for the truth table can be tested in "a domain of size one".
    $\blacksquare$
## 5.1
- 5-choosable: see [2-choosable](https://en.wikipedia.org/wiki/List_coloring#Examples) which proves by giving one counterexample.
## 5.2
- > m + k is even IFF [m is even IFF k is even]
  this means m,k has the same parity.
## 5.3
- > Even so, there is a mechanical way to *reformat* any induction proof into a Well Or-dering proof, and vice versa
  [See](https://math.stackexchange.com/a/490249/1059606)
  - This is different from DMIA 5.2-{41~43}.
    where 41 tries getting one contradiction using one artificial set and induction
    This is similar to [ProofWiki](https://proofwiki.org/wiki/Equivalence_of_Well-Ordering_Principle_and_Induction/Proof/WOP_implies_PFI) but the latter gets the contradiction from induction hypothesis while the former is from assumption that there is no the least element in $S$.
## chapter 5 problems
- Problem 5.4 skipped which is referred to in chapter 14.
- Problem 5.8.
  $$
  \begin{align*}
    F(n)\cdot F(n+2)-F(n+1)^2&=F(n)^2+F(n)F(n+1)-F(n+1)^2\\
                             &\overbrace{=}^{IH}F(n-1)F(n+1)-(-1)^n+F(n)F(n+1)-F(n+1)^2\\
                             &=-(-1)^n
  \end{align*}
  $$
- 5.25 trivial by algebraic calculation
- 5.30 similar to 5.25.
- Problem 5.4 referred to in 11.2.2 is skipped due to triviality.
- ~~Problems 5.8, 5.25, and 5.30~~
## 6 preface
- > They also come up in many other settings such as designing digital circuits and mod-eling probabilistic processes.
  i.e. Sequential logic.
  - TODO the relation between [subshifts of finite type](https://math.stackexchange.com/q/3839480/1059606) same as [the wikipedia definition](https://en.wikipedia.org/wiki/Subshift_of_finite_type#Definition) and [SYMBOLIC DYNAMICS](https://s-schmieding.github.io/SDnotes.pdf)
  - compared with Markov chain, [probabilistic automaton](https://en.wikipedia.org/wiki/Probabilistic_automaton) has inputs.
## 6.2*
- this has the example of jug 5 and jug 3 which is shown in one job review and also in one exercise of the Discrete_Mathematics_and_Its_Applications book.
## 6.3*
- > The word “partial” comes from viewing a process that might not terminate as computing a partial relation.
  Maybe it means the starting state can't be recursively related to the termination state.
- > So it can’t be halved more than dlog be C 1 times
  ~~TODO IMHO merely $\lceil\log b\rceil$ is enough.~~
  ~~because~~ 
  Problem 6.6
  when $b=2^k$ (i.e. k-bit binary number), then $\lceil\log b\rceil+1=k+1$
  when $2^k<b<2^{k+1}$ (still k-bit binary number), then $\lceil\log b\rceil=k+1$ is enough instead of $\lceil\log b\rceil+1$.
  > involves at most two multiplications
  i.e. $x^2$ and $xy$
  - Also [see](https://math.stackexchange.com/questions/3625697/prove-that-the-fast-exponentiation-algorithm-halts-after-lceil-log-2n-rceil#comment10468349_3625726) -> https://math.stackexchange.com/a/678643/1059606
- Fast Exponentiation is same as DMIA ALGORITHM 5 where $x'=y,power=x,n=z$ (Here use $x'$ for $x$ in DMIA).
## 6.4*
- > If we think of the robot as a nondeterministic state machine, then Claim 6.3.4 is a termination assertion
  IMHO here 'nondeterministic' has no relations with 'termination assertion'.
  It is only related with the 2 choices for east/west.
- > An example of preferences among four people where there is *no stable buddy match* is given in Problem 6.22.
  Since compared with the stable marriage problem, Theorem 6.4.3 is not held any more.
- 6.4 the idea is almost same as Discrete_Mathematics_and_Its_Applications 3.1-65 and 3.3-31  although the latter doesn't show explicitly using the *preserved invariant*.
## chapter 6 problems
- Problem 6.6 See above
  - if using induction,
    base: $b=1$ then $\text{quotient}(b,2)=0$, so one transition is enough.
    step: after one step, we need to prove $\overbrace{(\lceil \log (\text{quotient}(b, 2)=\lfloor b/2\rfloor) \rceil+1)}^{IH}+1=\lceil \log b \rceil+1$
      ~~Here when  we can interpret $$~~
      TODO but that may be invalid.
      when `b=0b101`, then $LHS=\log(0b10)+1+1=3$
      while $RHS=\lceil\log(0b101)\rceil+1$
      The key problem is that one side is rounded up while the other isn't.
- Problem 6.22
  | Assignment | rogue couple  |
  | ---------- | ------------- |
  | A-B,R-M    | R-B           |
  | A-M,R-B    | A-R           |
  | ...        | ... similarly |
  The main part is $x-M$ is always the *least* preferable, so $x$ is probably rogue.
  Then only when the other 2 people has the *rank 1* for each other, then one of them $y$ must prefer $x$ more and trivially $x$ prefers $y$ more.
## 7.1
- cons is [not one official operation in Python](https://pypi.org/project/cons/).
- Definition 7.1.3 is based on induction of the length of $s$
  - since $a\in A$, $\langle a, s\rangle=a\cdot s$
    similarly for $a \cdot (t\cdot \lambda)=\langle a, t\cdot \lambda\rangle$
## 7.2
- Definition 7.2.1 Constructor case
  this is very similar to DMIA 13-Supplementary-4, but here the production is from the inner to the outer which is the converse direction.
  - notice Problem 7.20. means same as (ii) in p10 of link1.
  - In sum,
    Lemma after Lemma 7.2.3 and Problem 7.20 combined together have the same process as the [reference p10][2_conditions_for_Balanced_Parentheses] where 1 is trivial to prove.
- here $\cdot's$ means the plural of $\cdot$.
## 7.3*
- Problem 7.25. is not included in DMIA 5.3, 5.4 (exercise 50-57 doesn't show the "well-defined" property).
  See [this](https://math.stackexchange.com/q/96483/1059606) and [this](https://en.wikipedia.org/wiki/Ackermann_function#General_remarks)
  based on the above "terminate ..."
  for this problem, 
  (n goes down) $A(m,n-1)$ can be called infinitely until $A(m,1)=2$, 
  (m goes down) then go up one stack $A(m-1,2)=A(m-2,A(m-1,1))=A(m-2,2)=^*A(0,2)=4$. Then we go up one stack again and do $A(m-1,4)=A(m-2,A(m-1,3))=A(m-2,A(m-2,A(m-1,2)))=A(m-2,A(m-2,4))...$ trivially $m$ will always go to 0 and go back stack up.
  - Also see [the code](./others/mcs/codes/Ackermann_7_25.py)
  $$
  \begin{align*}
    A(m, n)&::=2n
    &&\text{if } m = 0 \text{ or } n \le 1,
    &(A-base)\\
    A(m, n)&::=A(m-1,A(m,n-1))
    &&\text{otherwise}
    &(AA)
  \end{align*}
  $$
- TODO Union-Find algorithm
- Definition 7.3.1 implies ordinary induction is almost same as structural induction but the latter allows multiple arguments and is more about *data structure construction* instead of increasing $n$ by one constant step.
  as 7.6 says
  > Structural induction then goes beyond number counting
  - Also see 'The Principle of Structural Induction.'
## 7.5 (maybe *)
- 7.5.2 is more general.
- notice [Theorem 7.5.3.](https://en.wikipedia.org/wiki/Zermelo%27s_theorem_(game_theory)#Details) is not same as 
  > *each* of the players will have a strategy that guarantees a *win or a stalemate*
  because the base will ensure one lose.
- 'Definition. A play of a WL-2PerGm game G' is based on 
  > the situation at any point during game play can itself be *treated as the start* of a new game.
  So the 'Constructor case' is based on length.
  - > Each game M 2 G is called a possible first move of G
    implies G has moves although 'win' and 'lose' moves in base may be insufficient.
- Theorem 7.5.3 Fundamental Theorem for Win-Lose Games
  - > the first player in G becomes the second player in M .
    is based on 
    > So this play of G is a length $n+1$ sequence that finishes with the same outcome
  - better [see this][game_as_decision_tree]
    - This means same as DMIA 11.2 EXAMPLE 6
    - Here Definition 7.5.1 means possible moves make win or lose instead of directly win/lose.
    - > pick M0 as the first move, and then follow the second player’s winning strategy for M0 .
  - Lemma 7.5.2 is same as the top-right part in p1 of [yale_Fundamental_Theorem_for_Win_Lose_Games]
  - > Each game M 2 G is called a possible first move of G.
    here move is generalized to one move which has many small child-moves.
    Then
    > Now if there is a move M0 2 G where the second player in M0 has a winning strategy, then the first player in G has a simple winning strategy: pick M0 as the first move, and then follow the second player’s winning strategy for M0 
    means 'the first player' do one move $k$ which gets to the state $M_0$(i.e. 'pick M0 as the first move').
    **notice** 'move M0' means one game as the above definition and 'as the first move' means one minimal unit move.
    > if the first player in G makes the move M
    means choose $M$ as the above 'pick M0 as the first move'.
  - > Of course only the first move in the meta-chess-tournament is infinite, but then we could set up a tournament consisting of n meta-chess-tournaments.
    choosing $n$ is infinite.
- > Insert ref to Conway’s nimbers.
  similarly use [induction](https://en.wikipedia.org/wiki/Surreal_number#Induction)
- > as in the once famous third game in the 1961 movie Last Year at Marienbad.
  [see](https://www.qedcat.com/moviemath/index.html) or [wikipedia](https://en.wikipedia.org/wiki/Nim#History)
- > The proof shows that even in infinite games, every play must have an outcome. This is not the same as saying that the length of play has a fixed bound.
  This means the former $\Rightarrow$ the latter but not conversely.
- TODO
  > reference TBA
  may mean ["to be announced"](https://dictionary.cambridge.org/us/dictionary/english/tba#:~:text=tba%20%7C%20Business%20English&text=written%20abbreviation%20for%20to%20be,on%20November%2012%2C%20venue%20tba.), i.e. maybe in the book *in the future*.
  - This has no relation with ['[21] Michael Garey and David Johnson. tba. tba, 1970. 68'](https://bohr.wlu.ca/hfan/cp412/references/ChapterOne.pdf)
## 7.6
- > It is then possible to prove properties of data by ordinary induction on their size.
  this is how the book proves 'Fundamental Theorem for Win-Lose Games' compared with [yale_Fundamental_Theorem_for_Win_Lose_Games] where the latter uses 'ordinary induction on their size'.
## 7.6@@
- Definition 7.6.1.
  based on the example of (7.25), the operation is from right to left.
  So when $f\cdot \vec{Q}$, we first do $subtree_T(\vec{Q})$
- proof that Figure 7.4 is one tree with no duplicate nodes.
  at $n$th row starting from 0, it has $2^n$ elements.
  the leftmost is $2^n-1$ and the rightmost is $2 \cdot 2^{n} - 2$
```python
from sympy import Function, rsolve, latex, simplify
from sympy.abc import n
from sympy import init_printing
init_printing()
a = Function('a')
f=a(n)-1-2*a(n-1)
leftmost=rsolve(f, a(n), {a(0):0})
print(latex(leftmost))
f=a(n)-2-2*a(n-1)
rightmost=rsolve(f, a(n), {a(0):0})
print(latex(rightmost))
print(latex(simplify(leftmost-rightmost.subs(n,n-1)))) # so strictly increase between rows.
rightmost-leftmost # strictly increase inside rows.
```
  Since until the rightmost node of the nth row, we have $2^{n+1}-1=\sum_{k=0}^n 2^k$ elements which start from 0 to $2 \cdot 2^{n} - 2$, so their step must be 1.
  - Also see Theorem 7.6.16 which is trivial.
- Compared with DMIA chapter 11, this book says a bit about 'the circular and infinite weirdness' in trees. The former DFS/BFS implicitly avoids 'circular' and it says most of games is finite same as mcs.
- recursive trees is similar to [game_as_decision_tree]
- Theorem 7.6.11
  - $Rec\subseteq Fin$
    > Next we show that T has no shared subtree.
    - focus on what tree is shared
      i.e. in (7.27), whether the $|A\cup B|=|A|+|B|$ (See Lemma 7.6.13.)
      1. $T$ (excluded by finite)
      2. After $T$ is excluded
        we only need to care about $left\cup right$ 
        1. inside left/right (excluded by IH)
        2. between (excluded by def)
  - $Fin\subseteq Rec$
    - Here "an infinite path $f_n,\ldots,f_0$" is possible because they are all not leaves, i.e. they are Branchings.
    - ~~Here we only need to prove one instance of "a shared subtree" for "... or ...".~~
      ~~Then follow the sequence of $\notin$.~~
      Here due to definition we need to check "shared subtree" at each step.
    - > there is no sharing or infinite path in f1.f0 .T //
      sharing implies infinite
  - intuitively `RecTr` decrease the node count at each row one by one until the count becomes 1.
    Notice "the infinite binary tree" ~~has~~ ~~no leaves~~ must have one infinite path down from root because otherwise it is finite. Then we can't get that tree with only leaves and its production backwards.
- See Definition 7.6.9 for `size(T)`.
- $\vec{P}$ in (7.35) is one n-tuple.
- "proof checker" is why we may need "some tedious manipulation" with "The structural induction".
- > searches need not be any longer than log2 of the size of the set of values.
  i.e. $d\le \log_2(s-1)$ in Theorem 7.6.18.
  Then with (7.39) $\log_2(s+1)-1\le d\le \log_2(s-1)$
  so the length can be limited to one small range for "fully balanced" trees which is intuitive.
- > has depth at most log2 n.
  here means $\lfloor \log_2 n\rfloor$
  - See DMIA 11.1 COROLLARY 1 and chapter 11 RESULTS.
- AVL compared with "a fully balanced tree":
  see [the 2nd paragraph](https://cs.stackexchange.com/a/131229/161388)
  where the latter cares about subtree while the latter is the entire.
  - This says mainly about [the "normal binary tree" and the "AVL tree"](https://qr.ae/ps5xc0).
- (7.41) assumes $a>0$
- Corollary 7.6.22. is based on `1/math.log((1+math.sqrt(5))/2,2)=1.44` where = means $\approx$
- Definition 7.6.24 is Inorder
- Theorem 7.6.26 proof exercise
  1. T is Leaf,
    "then ..." is included in $ r=num(T) $
    "Otherwise ..." is included in $ r\neq num(T) $ Base case.
  2. T is Branching
    induction based on depth.
    1. $ r=num(T) $ trivial
    2. $r\in nums(left(T))$ (right is similar)
      based on IH, $num(subtree_{left(T)}(srch(left(T),r)))=r(*)$
      then $(*)=num(subtree_{T}(srch(left(T),r)\cdot left))=num(subtree_{T}(srch(T,r)))$
    3. $r\notin nums(left(T))$
      similar to 2, $srch(left(T),r)=fail_l\cdot \vec{P_l}$
      Then we can choose $fail_l\cdot \vec{P_l}\cdot left$ or $fail_r\cdot \vec{P_r}\cdot right$.
### 7.6.4
- > there is a way to arrange the values so that no search takes any longer than this minimum amount
  See Theorem 7.6.18
- > So a first question to address is *how short* can we guarantee searches will be compared to the size of the set to be searched?
  explains 7.6.6
  > used it to explain why the connection between tree size and *depth* is important.
  since the above asterisked words are positively related.
### 7.6.7*
- Figure 7.5,6
  Here all 2 /'s or \'s means one length-1 branch, so they have the same labels/nums.
- > which is within one of depth .U /
  it means one is within.
- > depth .X/ is d C 2 or d C 3 which is within one of depth .T /.
  This is not needed for
  > the depths of subtrees of X and Y are properly balanced according to the AVL rule
- based on 
  > The basic idea behind search trees is simple. ...
  search trees means binary trees / "a kind of branching “tree”".
- Figure 7.6 corresponds to [avl_insertion_detailed] 3. Right Right Case where $z=N,y=S,x=U$
  Figure 7.14 similarly with $(z,y,x)=(N,S,R)$ corresponds to 4. Right Left Case
  - Notice the former means `r>mid(S)>max(B)`
    and in the latter if $r\in V$ it is possible `max(B)<r<min(S)`.
    So
    > max.B/ < r < min.S /; or max.S / < r < min.B/; 
    in Lemma 7.6.27. is incomplete.
- Lemma 7.6.27
  - TODO
    - > nums.rotate.B; r; S // D nums.B/ [ frg [ nums.S /;
      lacks num(N) and $\{r\}\cup nums(S)$ may be just $nums(S)$
      > The result of inserting r into A will be a new AVL tree S with the same labels as A along with r.
    - > size-three sets Snew , Sold
      maybe $S_{old}=\{N,S,r\}$ and $S_{new}=\{Y,X,r\}$
      IMHO, the relabelling is not necessary.
      especially for Theorem 7.6.29 which relabel for each level implied by '1:44 log2 size .T /'.
  - comparison with Red-Black Trees
    better see [wikipedia](https://en.wikipedia.org/wiki/Red%E2%80%93black_tree#Properties) instead of [this definition](https://www.geeksforgeeks.org/introduction-to-red-black-tree/#)
    where 
    - the latter property 4 and 5 are same
      > alternatively, it could be defined as the black depth of any leaf node
    - Rule 2 is not needed
      > Since the root can always be changed from red to black
      but maybe not the other direction.
    - Since 
      > The AVL trees are *more balanced* compared to Red-Black Trees
      so
      > but they may cause more rotations during insertion and deletion
      - See "How does a Red-Black Tree ensure balance?"
        where the root and the leaf color can have only 1 choice if assuming property 1.
    - TODO detailed in CRLS for Red-Black Trees.
    - one [example](https://www.geeksforgeeks.org/red-black-tree-vs-avl-tree/) where one Red-Black Tree is not AVL where normally we may color 3 as Red in AVL.
  - [See](https://cs.stackexchange.com/a/167872/161388)
    - > depth .S /  depth .rotate.B; r; S //  depth .S / C 1;
      Here just `depth(S)`.
- Definition 7.6.28
  - Here
    > N ... Subtrs.S / [ Subtrs.B/;
    This is to avoid shared subtrees.
## chapter 7 problems
Here I skipped verification of Problem 7.44,42 because they are about induction which may be tedious and without many creative ideas.
Although Problem 7.43 may be not trivial but it is still based on induction.
- Problem 7.9
  based on Definition 7.1.2 and Lemma 7.1.4 proof.
  - $s=\lambda$ trivial
  - IS (inductive step)
    $$
    #_c(s\cdot t)&=#_c(\langle a,r\cdot t\rangle)\\
                 &=1+#_c(r\cdot t)\\
                 &\overbrace{=}^{IH}1+#_c(r)+#_c(t)\\
                 &\overbrace{=}^{IH}#_c(s)+#_c(t)
    $$
- Problem 7.19
  - a)
    if $s\in \text{ RecMatch}$
    then $s=[t]\Rightarrow$
    - [See](https://math.stackexchange.com/a/2926966/1059606)
  - b) trivial based on a) similar to the proof of lemma after Lemma 7.2.3.
    - Also see c)
      $[s]t,t=\lambda\Rightarrow [s]$
      and $st$ of a)
      so RecMatch becomes AmbRecMatch ...
  - c) $s'=[s],s't=[s]t$
    so AmbRecMatch become RecMatch -> RecMatch $\subseteq$ AmbRecMatch
  - The above b,c) is similar to [2_methods_for_balanced_parethesis] but the latter doesn't need the strict equality because it cares about terminals instead of intermediate strings.
    > since you don't need to cover all of these, as long as strings of terminals are covered
- Problem 7.20
  - a) start from
    > If γ is a prefix of β1[S but not β1
    in [2_conditions_for_Balanced_Parentheses]
  - b)
    IMHO "ends with 0" implies $L=R$
    so "good count" is just the "Balanced_Parentheses".
    Then the proof is same as [2_conditions_for_Balanced_Parentheses].
  - Here I didn't prove $\Rightarrow$ as what is done in [2_conditions_for_Balanced_Parentheses] because they are very similar.
- Problem 7.26
  - a) 
    - Environment Model
      $$
      \begin{align*}
        eval(subst(3x, x(x-1)),2)&\to eval(x(x-1),eval(3x, 2))\\
                                 &\to eval(x(x-1),3*2)\\
                                 &\to eval(x,6)*eval(x-1,6)\\
                                 &\to 6*(6-1)
      \end{align*}
      $$
    - Substitution Model
      $$
      \begin{align*}
        eval(subst(3x, x(x-1)),2)&\xrightarrow{\text{See equations between (7.18) and (7.19)}} 
                                  eval(3x(3x-1),2)\\
                                 &\to eval(3x,2)*eval(3x-1,2)\\
                                 &\to (3*2)*((3*2)-1)\\
                                 &\to 6*(6-1)
      \end{align*}
      $$
    - trivially, the 1st one does 3*2 once
      and doesn't manipulate $3x$ many times when $subst(3x, x(x-1))$
      So here 'variable lookup's used in $subst$ is *totally* avoided and multiplication 
  - b) if not taking multiplication in $subst$ in account,
    then $(3*2)*((3*2)-1)$ compared with 
    $eval(x,6)*eval(x-1,6)$ plus $3*2$ has one more multiplication,
    i.e. $2-1$ where $2$ is the substitution count.
    So [$x^{\underbar{7}}$](https://en.wikipedia.org/wiki/Falling_and_rising_factorials) instead of $x(x-1)$ will work.
  - c) see [this](./others/mcs/7_26.md)
- I skipped the reference Problem 4.7 because it is only shown as one game where we don't care what it is detailedly.
- Problem 7.36
  - All of the following proof is a bit less trickier than [wikipedia](https://en.wikipedia.org/wiki/Nim#Proof_of_the_winning_formula)
    - "the usual associative and commutative" combined together means we can choose *any 2* of all elements to calculate firstly. So we have the 4th $=$.
    - Ignores "These strategies for normal play and a misère game are the same until the number of heaps with at least two objects is exactly equal to one. ..." part because it may be impossible. See the following SE answer.
  - This is implied very implicitly in DMIA 11.2-39,40.
  - Here I follow the terms used in Problem 8.42
  - I skip Problem 3.6 because it seems to be only one reference for the carry.
  - a) ~~trivial for the next player~~
    ~~for the ~~
    ~~assume not, i.e. after one move for one pile, then the changed pile number binary representation~~
    To keep still zero, we need each bit of the changed pile number kept *unchanged*. That's  impossible.
  - b) make that one become "the Nim sum"
    then $a\oplus a=0$
  - c) if equal, by b) that's impossible.
    See this
    this just means that pile has that "most significant binary digit" set but not for "the Nim sum of the all the other piles", so that pile is bigger.
  - d)
    as b) says, "the first player" does one move to let the "Nim sum" become zero.
    then the 2nd player will again let "Nim sum" "not zero"
    then recursively, since the total number of stones strictly decreases, at last "the first player" will have one move to get to the zero stones (i.e. one  special case of the zero "Nim sum")
  - e) 
    see [the last diagram](https://en.wikipedia.org/wiki/Nim#Mathematical_theory)
    trivially the piles disappear one by one.
    See [this](https://math.stackexchange.com/a/4906435/1059606)
- Problem 7.44
  - base case: trivially since $T$ is the leaf, so $\vec{P}=\lambda$
  - Constructor case:
    Suppose $\vec{P}=(f_n,\ldots,f_0)$
    $subtree_T(\vec{P})=subtree_{f_0\cdot T}((f_n,\ldots,f_1))$
    let $\vec{P'}=(f_n,\ldots,f_1)$
    Then
    $$
    \begin{align*}
      \text{depth}(T)&=\ldots&(7.35)\\
                     &=|(f_0)|+\max\{\vec{P'}\ldots\}&(\text{def of tuple})\\
                     &=1+\max\{\text{depth}(\text{left}(T))\ldots\}&(\text{see above})\\
                     &\overbrace{=}^{IH}\text{RHS of Constructor case}&\blacksquare
    \end{align*}
    $$
- Problem 7.40 (trivial so with no verification online)
  - Since in Figure 7.5, depth(R)=d/d+1, depth(U)=d+1
    So it included the case in Figure 7.13
  - In a summary here we just find one method to break the pair (B,S) by categorization.
  - Here the bottom level is d/d-1 where at most one is d-1. Then "AVL tree" is trivial. The rest is same as Figure 7.5
    While Figure 7.5 d/d+1.
  - Notice here we need to [ensure ~~inorder "Insertion in AVL Tree:"~~](https://www.geeksforgeeks.org/insertion-in-an-avl-tree/)
  - complement resources
    - ~~TODO~~ one *deletion* may need [more than 1 rotations](https://stackoverflow.com/a/14035092/21294350).
      - > You can verify that Tree (c) and Tree (d) have one rotation upon removal, in the worst case.
        if caring about the deletions of one node, then trivial.
      - > On the other hand, removing a node from the right subtree may ultimately imbalance the tree resulting in a rotation of the root. Therefore, the right subtrees are of prime interest.
        because in the example trees, the right depth is less than the left.
        So it may cause difference 2 after deletion.
    - [insertion][avl_insertion_detailed]
      1. ~~$(T_1,T_2)=(a,a\pm 1\text{ or }a)$~~
        Then $T_3=$
      - [This](https://cs.stackexchange.com/a/53559/161388) means [this](https://www.geeksforgeeks.org/introduction-to-avl-tree/)
        > By looking at the setup graphics of the four types of rotation
    - one [equivalent definition](https://stackoverflow.com/a/230966/21294350) of AVL
      where the former 2 allows the balance factor to be 0.
      The last one forbids 2.
    - [comparison (see the 2nd paragraph)](https://cs.stackexchange.com/a/118948/161388) of deletion and insertion
- Problem 7.42
  - a) follow [Inorder Traversal](https://www.geeksforgeeks.org/inorder-traversal-of-binary-tree/)
  - b)
    - Here I assume "Search tree" means same as BBTr which assumes branching when not leaves.
      > Search trees have a numerical label on each subtree. Abstractly, this means there is a total function num W BBTr ! 
      This is also implied in $(T \in Branching)$ of the def.
    - proof of (odd-label)
      based on the induction of `size(T)`
      base case: `size(T)=1`, then the only leaf is odd.
      - lemma: `size(T)` must be odd with the same induction.
        trivial for base case
        `1+odd+odd` is still odd.
      - Based on lemma, then the `num(root)` must be even
        then based on IH, `leaves(T_{[a,b]})=leaves(T_{[a,root-1]})\cup leaves(T_{[root+1,b]})`
        they are still odd.
    - > the updated tree can share all but proportional to log2 (tree size) subtrees.
      TODO doesn't totally 2 for example $[1,n]$ and $[2,n+1]$?
      ```
        2                     3
       / \                   / \
      1   3       ----->    2   4
           \
            4
      ```
      - But this can
        > Having this extra label at the leaves serves as a buffer that allows comprehensive relabelling to be *deferred*
        TODO better see the codes
- Problem 7.43
  I follow the [process](https://stackoverflow.com/questions/13367981/what-is-the-minimum-sized-avl-tree-where-a-deletion-causes-2-rotations#comment122365176_14035092) https://webdocs.cs.ualberta.ca/~holte/T26/tree-deletion.html
  base case: two labels -> delete one; one label -> delete node and rotate upwards
  constructor case: `r > num(T)? delete(right(T),r) : (r=num(T)? delete_label(T,r): delete(left(T),r));if(depth_diff <=1){}else{rotate_upward()}`
## 8 preface*
- In a summary, it is reasonable to solve with the general case like "infinite" instead of one special case "finite".
## 8.1
- infinite set ordinal see [$w$](https://www.ub.edu/topologia/seminars/Set_theory.pdf)
- Lemma 8.1.3 See Definition 4.4.2.
- See Definition 4.5.2 here inj *doesn't imply the necessity* of the injective total relation, but only shows *existence*.
- Problem 8.12.
  > might end at an element that has no arrow into it.
  - See [stopper](https://en.wikipedia.org/wiki/Schr%C3%B6der%E2%80%93Bernstein_theorem#:~:text=In%20set%20theory%2C%20the%20Schr%C3%B6der,function%20h%20%3A%20A%20%E2%86%92%20B.)
    or more specifically, assume $f:5\to d$ and $g:d\to 5$
    then we will end either at 5 or d.
  - > paths that are unending but finite.
    i.e. 'cyclic if it repeats' in wikipedia.
  - (b) here we just start from the end for (i,ii) to the infinite ending.
  - (a) 'infinite' is due to we are considering infinite sets.
  - (c)
    > if an element occurs in two sequences, all elements to the left and to the right must be the same in both, by the definition of the sequences.
    this is caused by 1-1 of f and g.
  - (d) see [this](https://math.stackexchange.com/questions/4068977/halmoss-proof-of-schr%C3%B6der-bernstein-theorem#comment8407122_4068977)
- TODO ordinal and other related proofs after the set theory.
- Problem 8.15 (b) is same as [this](https://math.stackexchange.com/a/2052106/1059606)
  (a) see [this](https://math.stackexchange.com/a/3696479/1059606)
  - (a) proof implies
    'there is a *total* surjective function $g:\mathbb{N}\to C$' is same as
    'there is a surjective function $g:\mathbb{N}\to C$'
  - This is also almost as DMIA 2.5-13 but only using one *total* surjective function.
- Problem 8.25 (same index for mcs 2017 and 2018) See [this](https://www.physicsforums.com/threads/i-proving-that-the-cross-product-of-2-countable-sets-is-countable.263517/post-1911104) or DMIA 2.5-28.
- > adding one new element to an infinite set doesn’t change its size,
  this is just how map [between $\mathbb{N}$ and $\mathbb{Z}^+$](https://math.stackexchange.com/questions/182459/an-infinite-set-having-one-more-element-than-another-infinite-set#comment420603_182459)
- Problem 8.10 (Problem 8.12 in mcs 2018). 
  - (b)
    [See link1](https://math.stackexchange.com/a/2495180/1059606)
    > e (hence X is equipotent to a proper subsets of itself
    i.e. [$n+k$](https://en.wikipedia.org/wiki/Hilbert%27s_paradox_of_the_Grand_Hotel#Finitely_many_new_guests) or [$2n$](https://en.wikipedia.org/wiki/Hilbert%27s_paradox_of_the_Grand_Hotel#Infinitely_many_new_guests)
    - For "surjective", $s(x)=n\ldots$ is enough.
  - a) 
    - [wikipedia](https://en.wikipedia.org/wiki/Dedekind-infinite_set#Proof_of_equivalence_to_infinity,_assuming_axiom_of_countable_choice)
      - > That every Dedekind-infinite set is infinite can be easily proven in ZF
        proved using the definition point 2.
        - TODO proof "any, and then *all*".
      - > namely that every infinite set X is Dedekind-infinite, as follows:
        - let $X=-1\cup\mathbb{N}$
          > f(n) is the set of finite subsets of X of size n
          then $f(1)$ may be $\{\{-1\},\{0\},\ldots\}$
          so this member implies
          > whose members are themselves infinite (and possibly uncountable) sets.
          - > may choose one member from each of these sets, and this member is itself a finite subset of X.
            i.e. we can choose $\{-1\}$ from $f(1)$. "finite subset" is implied by $n\in \mathbb{N}$.
            - "More precisely ..." is just one rephrase.
        - > the union of the members of G. U is an infinite countable
          see [union_countable_is_countable]
        - see [ProofWiki](https://proofwiki.org/wiki/Equivalent_Conditions_for_Dedekind-Infinite_Set#(1)_implies_(2)) which proves "an infinite countable subset" based on Dedekind-infinite
        - [See](https://math.stackexchange.com/questions/3255573/infinite-sets-a-is-infinite-iff-there-is-a-bijection-between-a-and-a-cup#comment10479328_3255606) -> https://proofwiki.org/wiki/Infinite_Set_has_Countably_Infinite_Subset/Proof_4
          - [this](https://proofwiki.org/wiki/Set_is_Infinite_iff_exist_Subsets_of_all_Finite_Cardinalities) is trivial.
    - This proof is [same as (This may be link1)](https://math.stackexchange.com/a/3255611/1059606) (also same as [this](https://math.stackexchange.com/a/3255606/1059606)) the book but highlights the *subset* where $a_{n+1}$ always exist by "*infinite* countable subset" $B$.
      - one-to-one is ensured by $a_{n+1}$
        - TODO 
          maybe this means
          > if not circular
          is impossible, i.e. the case that ~~we can't have one infinite sequence $$~~ we have no such a $a_{n+1}$ for one $a_n$ is impossible.
        onto is because the mapping starts from $a_1$.
      - Notice here if $A=\mathbb{N}$, due to the infinity, the function still works.
      - [detailed proof link2](https://math.stackexchange.com/a/3255651/1059606) about Dedekind-infinite sets.
        - b->c same as [ProofWiki](https://proofwiki.org/wiki/Equivalent_Conditions_for_Dedekind-Infinite_Set#(1)_implies_(2)).
          - > Let A be an element of S not in the image of F.
            may use [Axiom of Specification](https://proofwiki.org/wiki/Axiom:Axiom_of_Specification/Set_Theory).
        - a->b i.e. b) in this problem.
        - TODO "*the proof* of Lemma 8.1.7" may mean
          ~~where~~ 'the proof of Lemma 8.1.7', the link1, the link2 all defines one bijective function.
      - I skipped [this](https://math.stackexchange.com/a/911426/1059606) because they may probably be same.
    - TODO
      - [Cofinite Choice](https://math.stackexchange.com/a/3985542/1059606)
      - [cantor set](https://math.stackexchange.com/questions/524029/a-set-is-infinite-iff-there-is-a-one-to-one-correspondent-with-one-of-its-proper/#comment1120394_524029)
    - Also [see](https://math.stackexchange.com/a/250124/1059606) which is similar to the wikipedia proof.
      - [See](https://math.stackexchange.com/q/2750930/1059606)
- > Since any partial function with nonempty codomain can be extended to a total function with the same range (reader: ask yourself how)
  See Problem 8.13 (a)
- here $w$ is the ordinal corresponding to $\mathbb{N}$.
- > $\mathbb{N}\text{ surj }(\mathbb{Z}^+)^\ast$
  do calculation from right to left.
- Problem 8.14 (Problem 8.16 in mcs 2018).
  [proof](https://math.stackexchange.com/a/317522/1059606) using that $n$ can be *infinitely bigger*.
- Corollary 8.1.16.
  this shrinks the size largely because it *only considers binary* bits after the decimal digit.
- [$0.999\cdots=1$](https://en.wikipedia.org/wiki/0.999...#Intuitive_explanation) or [not](https://betterexplained.com/articles/a-friendly-chat-about-whether-0-999-1/#:~:text=In%20our%20current%20system%2C%20we,0.999%E2%80%A6%20is%20less%20than%201.)
  - TODO I have read one book which says about it but can't find the location temporarily.
- > This diagonal sequence C corresponds to the set fa 2 A j a ... g.a/g in the proof of Theorem 8.1.12.
  think $a=(idx:0/1),g((idx:0/1))=A_{idx}$
  - > Both are defined in terms of a countable subset of the uncountable infinity in a way that excludes them from that subset,
    i.e. subset $A_{1\sim k}$
    and a countable subset of *the power set* although the latter is not necessarily infinite.
## 8.2
- program [freezing](https://www.reddit.com/r/Windows10/comments/j83klk/comment/g88jw9g/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button) (i.e. store the program for the latter running)
- > simulate the program using an interpreter
  like [python](https://cs.stackexchange.com/a/148444/161388)
- each program can be thought as [one superset of the algorithm](https://qr.ae/ps4YWn).
- see this for [the Halting Problem](https://math.stackexchange.com/q/4900611/1059606)
## 8.3
- Russell’s paradox is also shown in DMIA 2.2-50. 
  notice this is ~~same as~~ similar to cantor's diagonal argument $\{a \in A\vert a \notin g(a)\}$. See 8.1.
### 8.3.2*
- description related with “pure” sets@@
  - $\{0,1\}^w$ where [$w$ definition](https://en.wikipedia.org/wiki/Ordinal_number)
- [First-order logic](https://en.wikipedia.org/wiki/First-order_logic#) just means not propositions but
  > there exists x such that x is Socrates and x is a man
  - compared with [Second-order logic](https://en.wikipedia.org/wiki/Second-order_logic) where $\forall P\forall x$ instead of $\forall x$
    > In first-order theories, predicates are often associated with sets. In interpreted higher-order theories, predicates may be interpreted as sets of sets.
- > range over sets
  i.e. ~~a~~ ~~member of the set~~ ~~function~~ it [can be one set](https://math.stackexchange.com/a/1568778/1059606). This is also implied by
  > For any two sets x and y
  Also see [this](https://en.wikipedia.org/wiki/Second-order_logic#Syntax_and_fragments) where 'over sets of individuals' -> one set of individuals -> [unary relation](https://en.wikipedia.org/wiki/Finitary_relation#Unary).
- proper class@@ (@@ means this is in 2018 but not 2017)
  - prove "the class ${\displaystyle C}$ of *all* ordinals" are not a set by [contradiction](https://qr.ae/psuWjO).
    - This is similar to [why we need "proper class"](https://math.stackexchange.com/a/139337/1059606).
      > However once axiomatic set theory came into play we have the seemingly *circular* definition
      i.e. contradiction.
- Theorem 8.3.2
  - [the class of all sets is a proper class](https://math.stackexchange.com/q/1096528/1059606)
  - > requires careful use of the Choice axiom to prove that T is a set.
    may [probably means](https://en.wikipedia.org/wiki/Axiom_of_choice)
    > Formally, it states that for every indexed family ${\displaystyle (S_{i})_{i\in I}}$ of nonempty sets, there exists an *indexed set* ${\displaystyle (x_{i})_{i\in I}}$ such that ${\displaystyle x_{i}\in S_{i}}$ for every ${\displaystyle i\in I}$
    Here let the family be
    $U,S,N_{0,\cdots}$ where $U$ is the universal set.
    Then let the choice function be
    $U\to S,S\to N_0,\cdots$
    - [indexed set](https://math.stackexchange.com/a/3427023/1059606)
  - This needs understanding of pure sets
    - > modelling a real number r 2R by the set of rationals *greater than* r
      [See](https://en.wikipedia.org/wiki/Dedekind_cut#Representations)
      > but each of A and B does determine the other
      - one [example](https://en.wikipedia.org/wiki/Dedekind_cut#Construction_of_the_real_numbers)
        - It only shows the [definition][Dedekind_cut_definition] part 4
          the rest [see](https://www.math.brown.edu/reschwar/INF/handout3.pdf)
          - as the pdf says
            > so really the main new input is that you need an idea for Property 5
            This is trivial because $b\in \neg B=\{x\vert x\le 0\lor x^2\le 2\}\overbrace{=}^{\text{Property 1}}\{x\vert x< 0\lor x^2\le 2\}$
            Then $a<b\Rightarrow a\in\{x\vert x< 0\lor x^2< 2\}$
            - This also says why multiplication definition [needs 2 cases](https://en.wikipedia.org/wiki/Construction_of_the_real_numbers#Construction_by_Dedekind_cuts)
            - It doesn't manipulate with multiplication explicitly but only give one reference.
        - $2-y^2\le \frac{\epsilon}{2}$
          see the code
          ```python
          from sympy import roots,nsolve,solve,reduce_inequalities
          from sympy.abc import x, a, b, c, y
          y=(2*x+2)/(x+2)
          func=2-y**2-(2-x**2)/2
          print(reduce_inequalities([func<0], x))
          ```
        - Here is [one summary](https://math.stackexchange.com/a/62868/1059606)
  - This is similar to [this](https://math.stackexchange.com/q/1370976/1059606) ($x=\varnothing$ here) but $x\subseteq y$ can let $y$ contain *anything* more than $x$
    while here we must choose from `Recset` which at the bottom can only have $\varnothing$
    - in the link
      $T=\bigcup$ implies class
      and $y\in S$ is similar to "*S* is a nonempty set of *Recset*"
  - See [this QA](https://math.stackexchange.com/q/4905904/1059606) similar to [this*](https://math.stackexchange.com/a/3544645/1059606)
- ZFC
  - Axiom of extensionality
    can have [2 forms](https://en.wikipedia.org/wiki/Zermelo%E2%80%93Fraenkel_set_theory#1._Axiom_of_extensionality)
  - Pairing.
    'z 2 u IFF .z D x OR z D y/' cares about $z$
    while wikipedia cares about $x,y$
    so the former uses OR while the latter uses AND.
  - Union
    here IFF is  implied by $=$ in $\cup F=$ in wikipedia.
  - Axiom of infinity
    - > the empty set  ${\displaystyle \varnothing }$, defined axiomatically
      i.e. $\forall z\,\neg (z\in e)$
      this constructs $0$
      - > applying the axiom of pairing
        we get $1$
      - Then use $S(w)$ to get the following $2,\cdots$
    - > if two elements are the same, the sequence will loop around in a finite cycle of sets.
      See the following QA_1 answer_2.
  - Axiom of regularity/the axiom of foundation
    - how this means the book "forbid any infinite sequence of sets of the form"
      $\forall y \in x. y \notin m\Rightarrow x\cap m=\varnothing$
    - > This (along with the axiom of pairing) implies, for example, that no set is an element of itself and that every set has an ordinal rank.
      - the [rank](https://mathworld.wolfram.com/Rank.html#:~:text=In%20set%20theory%2C%20rank%20is,214).) implies
        > *forbid any infinite* sequence of sets
        - Notice 'First several von Neumann ordinals' in this page is different from [this](https://en.wikipedia.org/wiki/Von_Neumann_universe#Finite_and_low_cardinality_stages_of_the_hierarchy) like in $3$ it lacks $\{\{\varnothing\}\}$
      - the axiom of *pairing* is to [allow something like $\{A\}$ in QA_1](https://math.stackexchange.com/q/2537526/1059606)
      - proof see this [in brief QA_1 comment](https://math.stackexchange.com/questions/2537526/axiom-of-regularity-allows-for-this-set-be-an-element-of-itself#comment5239977_2537526)
        or 
        - [QA_1 answer_1](https://math.stackexchange.com/a/2537553/1059606)
          this 1st paragraph says 'set' -> '... disjoint sets' doesn't mean the converse is also true.
        - [QA_1 answer_2](https://math.stackexchange.com/a/2537670/1059606) which is more readable.
        - Also [see](https://en.wikipedia.org/wiki/Ordered_pair#Proving_that_definitions_satisfy_the_characteristic_property) as one reference of Problem 8.38@@.
    - This is needed to [simplify/(make possible) well-ordered sets](https://en.wikipedia.org/wiki/Axiom_of_regularity#:~:text=However%2C%20regularity%20makes%20some%20properties,as%20the%20lexicographical%20ordering%20on).
      - And see [point 3 to avoid '*non-well-founded* sets'](https://math.stackexchange.com/a/4866373/1059606) and its point 2 says same as [this QA_2](https://math.stackexchange.com/a/213649/1059606) that we use this axiom to simplify and make it possible to prove some theorems.
        - point 1 may say something like $A=\{A,\{A,B}\}$ doesn't exist, (transitive is similar, e.g. the former $A\in \{A,B\}\in A$)
          - How [this definition of pair](https://math.stackexchange.com/a/62937/1059606) is valid
          - This is same as Problem 8.38 in mcs@@
            - b) either $(\{1\},2)$ or $(\{2\},1)$
              This is similar to [this](https://mathoverflow.net/a/32201).
            - c) see [this](https://en.wikipedia.org/wiki/Ordered_pair#Variants)
              where "the axiom of regularity" corresponds to the hint.
              - This problem targets at [functions](https://math.stackexchange.com/questions/25791/definition-of-an-ordered-pair#comment55654_25791) instead of sets
            - [This](https://math.stackexchange.com/a/308428/1059606) says normally we only need one formula $\varphi$ to keep the proof consistent / "the same".
        - QA_2
          if
          > Its users *couldn't care less whether or not ZF is the underlying theory* of the universe or some other theory
          then we can skip assuming this axiom.
  - [Axiom *schema*](https://qr.ae/pskBLY) of specification -> Subset
    - Notice 
      > This restriction is necessary to avoid Russell's paradox
    - > and ${\displaystyle y\in z}$ has not been established
      is just the assumption
      > we need to previously restrict the sets ${\displaystyle y}$ will regard within a set ${\displaystyle z}$ that leaves ${\displaystyle y}$ outside
      which is same as 'Axiom of regularity'.
    - > In some other axiomatizations of ZF, this axiom is redundant in that it follows from the axiom schema of replacement ~~and the axiom of the empty set~~.
      since they are both *mapping*s where the former codomain is *same* as domain.
      - See [QA_3 question](https://math.stackexchange.com/q/32483/1059606) for the mapping to the pairing axiom
        where similarly we can get [$\{Z_0,Z_1,Z_2,\cdots\}$](https://en.wikipedia.org/wiki/Zermelo_set_theory#Connection_with_standard_set_theory)
        by have the mapping $\varnothing\to Z_0,\{\varnothing\}\to Z_1,\cdots$
        - TODO this can't be implemented using 'Axiom schema of specification' because it is  *restricted* in $z$ (i.e. subset).
      - see [QA_3 answer](https://math.stackexchange.com/a/32493/1059606) which doesn't need 'the empty set'.
    - > the domain of discourse must be nonempty
      implies
      > at least one set is known to exist
      - > The axiom of extensionality implies the empty set is unique (does not depend on ${\displaystyle w})$
        this is because $z\in x\Leftrightarrow z\in y$ is vacuously true due to $F\Leftrightarrow F$, so we have $x=y$.
  - Replacement
    here the 1st equation is similar to one-to-one function.
    - > specifies a unique ${\displaystyle x}$-to-${\displaystyle y}$ correspondence
      is implied by $\exists !$
    - notice the image is similar to [collection](https://en.wikipedia.org/wiki/Axiom_schema_of_replacement#Collection) due to only $\Rightarrow$ instead of $\Leftrightarrow$
    - > and ${\displaystyle f(x)}$ is a set for every ${\displaystyle x\in A,}$
      is because both $x,y$ ranges over sets.
      > Two sets are equal
      Also see
      > Thus the axioms of Zermelo–Fraenkel set theory refer only to *pure sets* and prevent its models from containing urelements (elements of sets that are not themselves sets)
    - better see the above image.
  - powerset
    the book IFF combines the 2 lines in wikipedia into 1.
  - Axiom of choice
    - TODO prove it [1](https://math.stackexchange.com/q/1839913/1059606) [2](https://math.stackexchange.com/q/1628106/1059606)
    - Problem 8.35 (i.e. 8.39 in mcs 2018)
      - > Verify that the axiom of choice can be expressed as a pure formula
        trivial since 'pairwise-disjoint.s' and 'choice-set.c; s' can be described as one formula.
      - See the last line of [this 'first-order logic'](https://en.wikipedia.org/wiki/Axiom_of_choice#Variants)
    - [from AC to the well-ordering theorem](https://en.wikipedia.org/wiki/Well-ordering_theorem#Proof_from_axiom_of_choice)
      just choose *one by one* the elements of the ordered sequence.
      - ${\displaystyle \sup\{\alpha \mid a_{\alpha }{\text{ is defined}}\}}$ may mean the complement $\smallsetminus \{a_{\xi }\mid \xi <\alpha \}$.
      - Notice this use the original definition instead of the variant (i.e. the book one) although they are [equivalent](https://math.stackexchange.com/q/4532500/1059606).
        - TODO I saw [the idea "disjoint union"](https://math.stackexchange.com/questions/4532500/axiom-of-choice-equivalence-is-my-proof-correct#comment10481032_4532500) in one former math Stack Exchange link.
    - the converse
      - > require just as *many choices* as simply choosing an element from each ${\displaystyle S}$.
      - > making all uncountably many choices is not allowed under the axioms of Zermelo-Fraenkel set theory without the axiom of choice.
        IMHO 'countably' is not allowed let alone 'uncountably'.
    - [Why we need this axiom](https://math.stackexchange.com/a/1083058/1059606)
      - I skip the last part of 3
      - The Axiom of Selection is the "Axiom schema of specification".
        - IMHO In summary, we need "the Axiom of Choice" to manipulate with / constrain the infinity implied in the axiom schema where The Axiom of Replacement / Selection have (This is similar to [this answer](https://math.stackexchange.com/a/1243483/1059606) where it first chooses one choice function based on $\exists$). Notice its [difference](https://math.stackexchange.com/questions/1935724/why-is-axiom-of-choice-required-for-the-proof-of-countable-union-of-countable-se#comment3976215_1935724) from [$AC_w$](https://en.wikipedia.org/wiki/Axiom_of_countable_choice).
          - This is [similar to $AC_w$](https://math.stackexchange.com/questions/1935724/why-is-axiom-of-choice-required-for-the-proof-of-countable-union-of-countable-se#comment3974549_1935734).
        - It may be not needed for ["normal, informal mathematics"](https://math.stackexchange.com/questions/2617081/why-do-we-need-the-axiom-of-choice#comment5404959_2617081)
        - Also see [this](https://math.stackexchange.com/questions/2617081/why-do-we-need-the-axiom-of-choice#comment5404940_2617081) which means same as the answer to ~~prove~~ ensure "existence".
      - > it doesn't only say that there are choice functions out there, but also that we're allowed to pick one.
        it may mean possibly one choice function instead of multiple.
### 8.3.3*
- This is same as [this](https://en.wikipedia.org/wiki/Universal_set#Regularity_and_pairing)
## 8.4*
- TODO Banach-Tarski Theorem
- > In particular, every axiom system is incomplete: it cannot prove all the truths of mathematics.
  This means at least 'an ax-iom system like ZFC is consistent' can't be proven (This implies its negative is also unable to prove because then we can prove the original statement implicitly.)
  > In fact, while there is broad agreement that the ZFC axioms are capable of proving all of *standard* mathematics
## chapter 8 problems
- Problem 8.14,15,25 see above
- Problem 8.13
  - a) similar to 25
  - b) still similar but dropping some terms
    TODO see reference in [this](https://math.stackexchange.com/a/1312/1059606) which has no duplicity
- [Problem 8.24](https://math.stackexchange.com/questions/91366/proof-that-union-of-a-sequence-of-countable-sets-is-countable#comment10471525_91366) <a name="union_countable_is_countable"></a>
  - > For clarity, 1. the point 3 may mean "mapping ... *firstly*" and then we can use $g$ to map to the target $\mathbb{N}$. 2. "the Cantor-Bernstein Theorem" means not [the "Cantor–Bernstein theorem" entry in wikipedia](https://en.wikipedia.org/wiki/Cantor%E2%80%93Bernstein_theorem) but wikipedia "Schröder–Bernstein theorem" entry. 2.1 A "embeds into" B means $|A|\le |B|$.  "maps $\mathbb{N}$ to $X_1$ into the union" means firstly map to "$X_1$" and then map to "the union". 3. [proof](https://mathoverflow.net/a/100725) when ZF.
    This is one deleted comment of mine as the answer author thought it may be inappropriate.
    1. the original point 3 already combines $f_n$ and $g$ together which have codomain $\mathbb{N}$
    2. The wikipedia top has
      > the Wikipedia entry at the very top *directs you to the appropriate page* if you are looking for the theorem;
    2.1 the author doesn't say something about it.
    3. > Especially given your utterly cryptic "3" that appears to claim that you are linking to a proof of the original statement in ZF (i.e., without Choice), when in fact you are linking to a proof that the statement *need not hold* in ZF... exactly what I said.
      TODO maybe this is said detailedly in the book, but I only grasped
      > So we have that the real numbers are a countable union of countable sets.
  - Cantor Pairing Function
    - [from the graph to the polynomial](https://en.wikipedia.org/wiki/Pairing_function#Derivation)
      - [This](https://math.stackexchange.com/a/222646/1059606) is similar but from one algebraic view
        where when $s$ is fixed we are at the diagonal where when $a$ is changed we moved along the diagonal
        when $s$ is changed "function resets back to the x-axis".
        - This also says about the triangular number.
        - In summary, this shows $f$ is strictly increasing (so one-to-one) for one order of $(a,b)$ with step 1 (so onto).
    - [invertible](https://math.stackexchange.com/a/91323/1059606) where at last all are functions of $z\in\mathbb{N}$.
- > the real numbers are a countable union of countable sets
    TODO [this](https://mathoverflow.net/a/100725) -> [book THEOREM 10.6.](https://gwern.net/doc/math/1973-jech-theaxiomofchoice.pdf) / [paper](https://web.archive.org/web/20120109193548/https://www.illc.uva.nl/Research/Reports/MoL-2006-03.text.pdf)
- Problem 8.18
  - almost same as Lemma 8.1.7 but with beginning 
    $$
    e(b_i)=a_{i},b_i\in B,i\in\mathbb{N}\\
    e(a_n)=a_{n+|B|},b_i\in B\\
    \text{same as orig}
    $$
  - See [this](https://math.stackexchange.com/a/1967807/1059606) based on [union_countable_is_countable] where 'infinite' in 'countably infinite' is based on the cardinality.
    compared with above, it takes $A\cap B\neq\varnothing$ in account and use $T\cup B'\to T$ (i.e. the above $e(b_i,a_n)$) implicitly.
- Problem 8.16
  - by Definition 8.1.1 and Theorem 8.1.5, we know (a) and (b) means same.
- Problem 8.38 p311 See above
- Problem 8.39 See above
- Problem 8.42 in p234
  - This is really similar to ["von Neumann ordinals"](https://en.wikipedia.org/wiki/Zermelo%E2%80%93Fraenkel_set_theory#7._Axiom_of_infinity).
  - base case $Nim_{\langle \varnothing\rangle}$ 
    trivially "Next player" loses
  - Constructor step $Nim=Fmv=\{(x\vert x\in Recset)\land(x\text{ is possible for the next Fmv})\}$
    IH (Inductive Hypothesis) we know `Recset` can have one winner
    then trivially also for `Nim`
  - IMHO this is very similar to the proof of "Fundamental Theorem for Win-Lose Game". See the corresponding "better [see this]".
## 9.1.3* which says more about 'Jug Problem' (Also see 9.2)
- it should be $(0,3a-b)$ instead of $(3a-2b,b)$
## 9.2
- [Problem 9.14](https://math.stackexchange.com/q/3707612/1059606)
  here after 'n transitions', it get $(gcd(a,b),0)$, then one more step to terminate.
  so $n+1$ steps at all.
  since $F(n+1)\le a\le F(n+2)$, so we need 
  $\lceil \log_{\varphi} a\rceil$
  - TODO see [one variant](https://math.stackexchange.com/q/3734764/1059606)
- (9.3) also see [this 'Euclidean Algorithm Machine'](https://www2.math.binghamton.edu/lib/exe/fetch.php/people/grads/eppolito/state_machines_and_algorithms.pdf) which is more comprehensive
- 9.2.4 Lemma 9.2.6
  a) [see](https://math.stackexchange.com/a/705874/1059606) which starts from the conclusion and iff back.
  b) trivial by the definition of gcd ($\Leftarrow$) and the Bezout’s lemma ($\Rightarrow$)
  c) [multiply](https://math.stackexchange.com/a/675887/1059606) instead of add/minus to prove.
  d) see DMIA.
## 9.3
- [p-adic number](https://en.wikipedia.org/wiki/P-adic_number#Example)
- Problem 9.22. -> [Shoup's book](./other_books/ntb-v2_1.pdf) Also see [notes](https://crypto.stanford.edu/pbc/notes/numbertheory/)
  - Lemma 5.3 -> [Legendre's formula](https://en.wikipedia.org/wiki/Legendre%27s_formula)
  - EXERCISE 1.4: 2 cases
  - See [this](https://math.stackexchange.com/a/1890792/1059606)
    in 4) 
    - the 2nd $\le$ is based on the prime factorization where each takes the highest power $\log_{p} 2n$
  - > So we have ...
    the 3rd $=$ is from $N=\prod p^{v_p(N)}$
  - Then $\frac{\log 2}{2}>\frac{1}{3}$
- > about 1 integer out of every ln n in the vicinity of n is a prime.
  is implied by $n/\ln n$
  This implies 9.4
  > about 1 in $\ln 10^{10} =23$
  where $n=10^{10}$
## 9.4
- Problem 9.25.
  - a) hinted by [QA_1](https://math.stackexchange.com/a/1143135/1059606)
    $$
    \begin{align*}
      (m+\sqrt{5}ni)(p+\sqrt{5}qi)=29&\xRightarrow{\text{complex number calculation}} (m^2+5n^2)(m^2+5n^2)=29^2\\
                                     &\xRightarrow{\text{both can't be 1}} (m^2+5n^2)=29\\
                                     &\Rightarrow m=3,n=2\qquad\text{one possible solution}
    \end{align*}
    $$
  - b) [see](https://math.stackexchange.com/questions/94999/irreducible-in-mathbbz-sqrt-5#comment4635085_95005)
  - c) similar to b)
  - d) similar to a) we have $|x|\le|y|\Rightarrow |x|^2=1,|y|^2=9$
  - e) from d) $w=3,2\pm \sqrt{5}i,|xy|=|w|,|x|\le|y|\Rightarrow \ldots \pm 1\Rightarrow w=y$
    so irreducible
  - Also see [wikipedia_1](https://en.wikipedia.org/wiki/Quadratic_integer#Examples_of_complex_quadratic_integer_rings)
    > if they were not irreducible, they would have a factor of norm 3, which is impossible
    same as the above b)
  - [Irreducible element](https://en.wikipedia.org/wiki/Irreducible_element#Example)
    > that is, they are the factors that cannot be further factorized.
  - prove one number is [not prime](https://math.stackexchange.com/a/1143135/1059606) which is based on Euclid's lemma
    This lemma can also prove ['Irreducibles are prime in a UFD'](https://math.stackexchange.com/questions/257955/irreducibles-are-prime-in-a-ufd#comment10468066_1913111)
    - ~~TODO~~ the wikipedia [reference][introduction_to_number_theory] ~~doesn't say about ~~.
      [See](https://math.stackexchange.com/questions/1141412/mathbb-z-sqrt-5-is-not-a-ufd#comment10468076_1143135) 'Euclid's lemma' in wikipedia
- Lemma 9.4.2 is one rephrase of DMIA 4.3 LEMMA 2.
  - Lemma 9.4.3 is then also duplicate in DMIA 4.3.
    This means $\gcd(p,\prod a_i)=p$
## 9.5* (So also 9.8*)
- [comparison](https://en.wikipedia.org/wiki/AKS_primality_test#Importance) between the Miller–Rabin test and AKS.
## 9.6
- Lemma 9.6.4 skips the proof of DMIA 4.1 THEOREM 4.
## 9.7* (This is said in DMIA 4.1.5 Arithmetic Modulo m although not detailed)
- compared with DMIA 4.2.4 Modular Exponentiation which cares about simplifying the exponent, 9.7 cares about the base.
- > all of the following equalities
  these are those in [the ring definition](https://en.wikipedia.org/wiki/Ring_(mathematics)#Definition) plus commutativity of $\cdot$ where 2 rules of distributivity are combined.
  [proof](https://proofwiki.org/wiki/Ring_of_Integers_Modulo_m_is_Ring)
  - Addition
    - [Modulo Addition is Associative](https://proofwiki.org/wiki/Modulo_Addition_is_Associative) which is based on *Associative Law of Addition*.
    - [cyclic proof](https://proofwiki.org/wiki/Quotient_Group_of_Cyclic_Group/Proof_1)
      TODO Here $(gH)^k=g^kH$ is based on [this](https://proofwiki.org/wiki/Power_of_Coset_Product_is_Coset_of_Power)
      We can also prove by [inspecting](https://math.stackexchange.com/a/2602937/1059606) the [specific group](https://en.wikipedia.org/wiki/Quotient_group#Remainders_of_integer_division) (Notice [coset](https://en.wikipedia.org/wiki/Coset#Definition) depends on the operation/factor is $+$ or $\times$, etc.)
      - See the 1st paragraph of [this](https://math.stackexchange.com/a/69063/1059606) and [this](https://en.wikipedia.org/wiki/Quotient_group#Motivation_for_the_name_%22quotient%22) which shows why we name "quotient group".
      - TODO [prove](https://proofwiki.org/wiki/Cyclic_Group_is_Abelian) Cyclic Group is Abelian.
        Here for "Integers Modulo m", $\cdot$ should be substituted by $+$.
      - Abelian -> normal group because (binary) operation implies [closure](https://en.wikipedia.org/wiki/Binary_operation#Terminology) which combined with inverse we have [$gng^{-1}\in N$](https://en.wikipedia.org/wiki/Normal_subgroup).
    - [closure](https://proofwiki.org/wiki/Modulo_Addition_is_Closed) is implied by definition (See (9.11)).
      "Note" means $x,y\in\mathbb{Z}_m,\llbracket x\rrbracket_z+\llbracket y\rrbracket_z\notin \mathbb{Z}_m$.
    - Identity / Inverse can be proved similar to "Associative".
    - commutative can be proved based on cyclic or directly from definition.
  - Modulo Multiplication
    - closure use the [Division Theorem](https://proofwiki.org/wiki/Modulo_Multiplication_is_Closed) although we can still use the definition of modulo operation directly.
    - associative, identity, "commutative" and Distributivity is similar to the above.
      In summary they are all based on those properties in the *normal* addition and multiplication based on "Lemma 9.7.1".
      > The overall theme is that remainder arithmetic is a lot like ordinary arithmetic
    - Identity of Monoid/algebraic structure is Unique is based on [the definition of Identity][Identity_Unique].
- > the range [0..n)
  is due to [the modulo operation](https://en.wikipedia.org/wiki/Ring_(mathematics)#Example:_Integers_modulo_4)
- > polynomials with integer coefficients
  This ring [see](https://www.math.uci.edu/~ndonalds/math120b/2poly.pdf)
  similar to the above, it is ring because its operation is ~~based on~~ almost same as those operations in $\mathbb{N}$.
- > On the other hand, the set fT; Fg of truth values with OR for addition and AND for multiplication is not a commutative ring because it fails to satisfy one of these equalities.
  i.e. "inverse for $+$" because $T\lor X=T\neq F$
  All the others are satisfied [including distributivity](https://en.wikipedia.org/wiki/Principle_of_distributivity).
- > The n  n matrices of integers are not a commutative ring because they fail to satisfy another one of these equalities.
  i.e. commutativity
  Here "inverse for $+$" can be satisfied.
  [All the others](https://en.wikipedia.org/wiki/Matrix_multiplication#General_properties) are satisfied
- > But there are a couple of exceptions we’re about to examine.
  see 9.9
## 9.9
DMIA 4.1 only says in brief in th end.
- Lemma 9.9.1 see DMIA 4.4 THEOREM 1.
  - Here [$\gcd(0,n)=n$](https://math.stackexchange.com/a/1156819/1059606), so 0 and 1 are relatively prime.
- 0 [relatively prime](https://www.splashlearn.com/math-vocabulary/relatively-prime#:~:text=0%20and%201%20are%20relatively,is%20divisible%20by%20any%20integer.) to 1 based on definition.
- Theorem 9.9.5
  > if k is not relatively prime to n, then we can show it isn’t cancellable
  Assume this is $A\to B=\neg (A\land\neg B)=T$
  so $A\land\neg B=F$
  i.e. Assume A and $\neg B$ "it *is* cancellable", we need contradiction.
  - See [this](https://math.stackexchange.com/questions/4910592/textif-1-neq-gcdc-m-textthen-ac-equiv-bc-pmod-m-nrightarrow#comment10484446_4910592) where we only needs one counterexample.
- Riemann Hypothesis
  - [relation](https://math.stackexchange.com/a/1922389/1059606) with the prime distribution.
    - notice "The second Chebyshev function" has [2 $\sum$](https://en.wikipedia.org/wiki/Chebyshev_function) which causes $\log_p x$
    - $\ge$ is based on $\log_p x\ge 1$ and $x^{1-\epsilon}\le p$.
      TODO the last equality from $\pi(x)-\pi(x^{1-\epsilon})$
    - "The next step ..." is  temporarily dropped.
- Lemma 9.10.6 is proved by showing 1-to-1. "total" is implicit.
### 9.9.2*
- This is said in brief in DMIA 4.3 THEOREM 7.
## 9.10*
- Theorem 9.10.10(b) proof same as [wikipedia](https://en.wikipedia.org/wiki/Euler's_totient_function#Value_of_phi_for_a_prime_power_argument)
- proof of Corollary 9.10.11 using the inclusion-exclusion principle may be unnecessarily
- > This would be a much stronger theoretical assurance of RSA security than is presently known.
  TODO doesn't this share the same idea about factoring with the previous paragraph?
## 9.12*
This uses SAT to solve factoring [which is NP](https://stackoverflow.com/questions/2642476/is-the-integer-factorization-problem-used-for-many-cryptographic-applications#comment2657380_2642476) since SAT is NP-complete.
- > the remaining 2n inputs
  this is due to $(2^{n}-1)^2<2^{2n}-1$.
- > uses proportional to n2 gates
  skip_circuit
## chapter 9 problems
- Problem 9.2
  i.e. to prove $1+\ldots+2^{k-1}+(2^{k}-1)(1+\ldots+2^{k-2})=2^k-1+(2^{k}-1)(2^{k-1}-1)=(2^{k}-1)2^{k-1}$
  - [reference](https://t5k.org/notes/proofs/EvenPerfect.html)
    - proof that [odd and even are coprime](https://math.stackexchange.com/a/2251831/1059606).
    - [$\sigma(n)$](https://t5k.org/glossary/page.php?sort=SigmaFunction#:~:text=The%20sigma%20function%20of%20a,using%20the%20greek%20letter%20sigma.&text=Clearly%2C%20for%20primes%20p%2C%20%CF%83,(p)=p+1.) is [multiplicative](https://math.stackexchange.com/a/1948512/1059606)
      Notice here we add $n$ itself due to the definition which also makes the elegant $\Prod$ possible (otherwise we need to remove one term which will make it impossible to be expressed in  multiplication of sum).
    - > This means that m is prime and its only two divisors are itself (m) and one (M)
      because this is the minimal state. So prime.
- Problem 9.13 trivial here give one sketch.
  Also [see](https://math.stackexchange.com/a/4911211/1059606) which I only gives one overlook because that is not very helpful with much redundant information.
  - Inv1 is by [Euclidean algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm#Proof_of_validity)
  - Inv2,3 base trivial
    - Inv2
      $(u-sq)a+(v-tq)b\overbrace{=}^{IH}x-qy=rem(x,y)$
    - Inv3 probably same, skipped.
  - b) ~~TODO~~ [see](https://math.stackexchange.com/q/4909510/1059606)
  - c) See the above link maybe here "at most" can be stronger to = but it is enough to show polynomial.
  - Since the book only refer to 2 
- Problem 9.70
  - (a,b) are trivial. [See](./others/mcs/9_70.md)
  - (c) See [this](https://math.stackexchange.com/questions/1083751/prove-that-if-k-1-and-k-2-are-relatively-prime-to-n-then-so-is-k-1-n-k-2#comment10485470_1083751)
- Problem 9.61 is skipped due to duplicity.
- Problem 9.64
  - a) trivial based on the *unique solution* using the Chinese Remainder Theorem.
  - b) since $ab$ only has $1,a,b,ab$ factors
    $\gcd(k,ab)=\gcd(k,a)=\gcd(\text{rem}(k,a),a)=1$, so the function is well-defined.
    - Same as [Euler_Phi_multiplicative]
  - c) because $|\varphi|=|\mathbb{Z}^\ast|$ (Definition 9.10.2)
  - d) see the book
- Problem 9.85
  - a) See [RSA_Euler_theorem]
  - b) See [RSA_Fermat_little_theorem]
  - c) see [this](https://math.stackexchange.com/a/1942165/1059606) based on the definition of lcm. Then use $\text{lcm}(p_i,\ldots)=\prod p_i$ based on the Fundamental Theorem of Arithmetic
    - Also see [RSA_proof]
  - d) i.e. let $a=m^a$ in c).
    We can get $a\equiv 1\pmod{p_i-1}$, then use b) and then c), we get d).
- Problem 9.87
  - a) by definition of $ed$.
  - b) since both $p-1,q-1$ are even.
  - c) by Euler_theorem.
  - d) $\text{rem}(r^{c/2},n)=y\equiv r^{c/2}\pmod{n}\Rightarrow y^2\equiv r\pmod{n}$
    Then $n\mid y^2-1$
    Since $y\le n-2\Rightarrow y+1\le n-1$
    trivially $(p\mid y+1)\vee(q\mid y+1)$ since otherwise $n\mid y-1<n$ is impossible where $y\neq 1$.
    Then $0<y+1\le n-1$ also excludes $(p\mid y+1)\land(q\mid y+1)$
  - TODO why 4 square roots modulo n.
  - e) by probability, 1 in 2 *relatively prime numbers*.
- Problem 9.33 (chapter 16 reference) Also see [Identity_Unique]
  - (a) similar to [Identity_Unique]
    if $z_{1,2}\oplus r=r$
    Then $z_1\oplus z_2=z_1=z_2$
  - (b) $r\oplus r_1\oplus r_2=0\oplus r_2=r_2\tag{*}$
    similarly $LHS\text{ of }(*)=r\oplus r_2\oplus r_1=r_1$
  - similarly with the definition of 1.
    Here we don't need the "unique" property of 1 although that is held.
## 10.3
- Theorem 10.3.2 is same as DMIA 10.4.7.
- > will be the smallest value k for which .AG /kuv is nonzero
  same as DMIA 10.4-56.
- > its length will be $\le n - 1$
  It is also said in DMIA 9.4.
- > Refinements of this idea lead to methods that find shortest paths in reasonably efficient ways. ... and we won’t go into them any further.
  One different method (maybe not one refinement) based on Warshall’s algorithm (by adding $v_k$ successively) is said in DMIA 9.4-32.
## 10.4
- (10.9) Here it may think $G$ doesn't contain the "identity relation".
  $G\cup G^0$ is needed due to there is no length 1 walk from a to a except for the self-loop which doesn't always exist.
  But for length-k $k>1$ walks, they must be based on length-1 recursively.
  So $(G\cup G^0)^{|V(G)|-1}$ will contain all walks with length $1<n<|V(G)|-1$.
## 10.5* (not said in DMIA but is read in GeeksforGeeks)
- See [get_Topological_Sorting_from_DAG] and [DAG_to_topological_ordering_proof]
  and also [this](https://www.geeksforgeeks.org/topological-sorting-indegree-based-solution/) same as [kahn_proof] which is same as the former 2.
  - > If the queue is empty and there are still nodes in the graph, the graph contains a cycle and cannot be topologically sorted.
    since the nodes in the loop can't be removed because by removing minimal elements outside the loop we can't make one node inside the loop in-degree 0.
- > One peculiarity of this terminology is that a DAG may have no minimum element but lots of minimal elements
  [See](https://math.stackexchange.com/a/1047426/1059606)
  - So we can say
    > we could build a topological sort starting from maximal elements at the end of paths
    maybe in the reverse order.
    > picking vertices arbitrarily from a finite DAG and simply inserting them into the list *wherever they will fit*
    This seems to say nothing useful.
- > A finite chain is said to end at its maximum element.
  infinite may [not hold this property](https://math.stackexchange.com/a/2509331/1059606) where the order is lexicographic
- critical path is said in csapp although not giving one formal definition in mathematics.
- > Lemma 10.5.12 also follows from a more general result known as Dilworth’s Theorem, which we will not discuss.
  This is solved in DMIA [Dilworth_theorem_proof_wikipedia].
  "disjoint chains" -> "the smallest chain decomposition" is $n/t$ when "a chain of size not greater than t".
## 10.6
- Definition 10.6.7 may assume Asymmetry since it is based on digraph.
- Theorem 10.6.8 "only if" seems to be wrong since the domain of $R$ may be not vertices except that we geenralize everything as vertices like the former example seeing clothes as vertices.
- in Corollary 10.6.11 ~~may be~~ [~~not precise~~](https://en.wikipedia.org/wiki/Asymmetric_relation#Definition), it combines the [irreflexive, asymmetric](https://en.wikipedia.org/wiki/Partially_ordered_set#Strict_partial_orders) [together](https://en.wikipedia.org/wiki/Asymmetric_relation) since the definition of "asymmetric" includes $a=b$ case so that $aRa$ doesn't hold.
## 10.7
- [inverse images](https://en.wikipedia.org/wiki/Image_(mathematics)#Generalization_to_binary_relations) means $\{x\mid x\preceq y\}$.
## 10.8
- > You can think of a linear order as one where all the elements are *lined up* so that everyone knows exactly who is ahead and who is behind them in the line
  we can always transform from one total order into such one list.
  By [finite_chain_maximum_minimum], we can recursively choose minimum element similar to lexicographic sorting.
  - See [chain](https://en.wikipedia.org/wiki/Total_order#Chains)
## 10.10
- > the age-height relation Y is a partial order.
  implide by "AND".
- > an antichain of 11 students—that is, 11 students who get taller as they get younger,
  Since $(y_1,h_1)\not Y(y_2,h_2)\Rightarrow (y_1\le y_2\land h_1> h_2)\lor(y_1> y_2\land h_1\le h_2)$ where they both mean "get taller as they get younger".
- > any weak partial order is a total relation but generally won’t be linear.
  Since for each $a$ at least $b=a\Rightarrow aRb$
  - "total relation" [definition (see mcs Definition 4.4.2)](https://en.wikipedia.org/wiki/Total_relation) is different from [this](https://math.stackexchange.com/a/2656651/1059606)
## 10.11
- > R is transitive and irreflexive iff R is transitive and asymmetric
  "if" trivial
  "only if" suppose irreflexive but not asymmetric
  then [$\exists a,b\in X:aRb\land bRa$](https://en.wikipedia.org/wiki/Asymmetric_relation#Definition) based on $\neg(A\to B)=A\land\neg B$
  by transitivity, we have $aRa$ contradiction.
- > R equals the in-the-same-block-relation for some partition of domain.R/
  implied by 
  > being the relation of “having the same label” according to some labelling scheme.
## chapter 10 problems
Many of problems later are not verified. Only those I really have doubts may be verified on Stack Exchange / Stack Overflow.
- Problem 10.3 @#@
  - a) suppose by contradiction $x$ is not on.
    ~~then $dist (u, x) + dist (x, v)>dist (u, v)$ leading to the contradiction with "shortest path"~~
    ~~or $dist (u, x) + dist (x, v)<dist (u, v)$ leading to the contradiction with $dist(u,v)$.~~
    Since "dist (u, x) + dist (x, v)" defines one "shortest path" = dist (u, v). 
    Then $x$ is on that path.
  - b) if x is on a shortest path from u to v, then it must take the shortest from u to x and x to v (otherwise that path is not shortest).
  - the [proof](https://math.stackexchange.com/a/737495/1059606) of The Triangle Inequality similar to the book
- Problem 10.4
  - a) [see](https://math.stackexchange.com/a/498928/1059606) A->D->A
    - Also see wikipedia ["H–A–B–A–H" example](https://en.wikipedia.org/wiki/Cycle_(graph_theory)#Definitions)
    - Here cycle *uses book definition* not based on circuit.
  - b) [see](https://math.stackexchange.com/a/2938479/1059606)
    - [lazy](https://ocw.mit.edu/courses/18-409-topics-in-theoretical-computer-science-an-algorithmists-toolkit-fall-2009/100377025e8520aab9f61d8585e71cc5_MIT18_409F09_scribe4.pdf)
    - "nonbacktracking" may mean not going back by verbatim.
      This is implied by the example in the answer.
    - IMHO nonbacktracking ensures circuit and then non-lazy ensures cycle.
    - notice this answer is correct about the *necessary* additional conditions.
    - Here cycle *uses wikipedia definition* based on circuit.
  - IMHO here a) and b) seems to be in conflict.
    Since the definition of cycle may be not official. I skips digging into it.
  - Ignore the above see [this](https://math.stackexchange.com/a/4911852/1059606)
    - (a) imply positive length based on "including two vertices".
    - TODO is the following right?
      > a digraph that has a closed walk including *one* vertex *must* has *a* cycle including that vertex.
      - By
        > We need to forbid such closed walks, which by Lemma 10.2.6 is the same as forbidding cycles.
        the above seems to be true.
    - b) same as [this](https://math.stackexchange.com/a/3478309/1059606)
- Problem 10.11
  Notice the following are all boolean matrices.
  - (a) first walk $m$ then $n$ which is same as the Proof of Theorem 10.3.2.
  - (b) same as Corollary 10.3.3
    > which by convention is the identity matrix, is the length-0 walk counting matrix.
    > More generally, it follows by induction that
  - (c) If taken $\bigcup$ as $\lor$
    then trivial by $R^+$ definition where $|A|$ can be $|A|-1$ (See 10.3.1).
  - Also see the contents in 10.4 for (c)
- Problem 10.25
  - (a) suppose " when j < k, *one* vertex in Aj is reachable from any vertex in Ak"
    Then $A_j$ should has at least depth $k>j$ leading to the contradiction.
  - (b) almost same as (a) by contradiction when assuming "*one* walk exists between *some* two different vertices in the set.".
- Problem 10.26
  - (a) trivial by definition
  - (b) since we must do $n-(t-1)$ bottom tasks first if possible with $n-(t-1)$ number of processors
    and then follow the chain of $t-1$ tasks which is the minimal steps to do due to dependency.
    Since each step is determined, it is unique.
  - (c) 
    $$
    \lceil \frac{n-(t-1)}{p}\rceil+t-1\quad\text{Here we must finish n-(t-1) before t-1, so we can't take one from t-1 to the possible gap }\lceil \frac{n-(t-1)}{p}\rceil-\frac{n-(t-1)}{p}
    $$
    - $t,p\ge n-(t-1)$ is contained in the above.
  - (d)
    base: $t=1$ trivial since each step we have at most $p$ tasks.
    induciton: IMHO the above $M$ is specific for $D_{n,t}$ and doesn't work for other situations like the possibility for filling the above gap when some of the next level can be in parallel with the rest in the former level.
- Problem 10.31
  - See [this sol](https://dspace.mit.edu/bitstream/handle/1721.1/104426/6-042j-spring-2010/contents/lecture-notes/MIT6_042JS10_lec12_sol.pdf) from [this](https://dspace.mit.edu/bitstream/handle/1721.1/104426/6-042j-spring-2010/contents/lecture-notes/index.htm) -> [local sol copy](./others/mcs/sol/MIT6_042JS10_lec12_sol.pdf)
  - (a) see [this](https://math.stackexchange.com/q/4244719/1059606)
  - (b) following the QA link
    > If a covers b, then there is no longer path between a and b other than the edge itself.
    so if a doesn't cover b, then $ab$ will be removed. But since there is one longer path, positive walk relation $R^+$ doesn't change.
    - also [see](https://math.stackexchange.com/a/4244916/1059606)
  - (c) suppose not
    then use (b) to make them "consisting of only the covering edges".
  - (d) see sol.
  - (e) see sol.
  - (f) 
    - (i) remove one of 3 pairs like $1\to 2,2\to 1$.
    - (ii) nothing changed
    - (iii) same.
    - see sol where (i,) in the above are wrong.
- Problem 10.37
  - (a) 
    1-to-1: for each $L(a)$, there must be one maximum element which is $a$.
    onto: see the above.
  - (b)
    only if: $x\preceq a\preceq b\Rightarrow x\preceq b$ by transitive property.
      i.e. $x\in L(a)\Rightarrow x\in L(b)$, so $L(a)\subseteq L(b)$
    if: similarly we have $x\preceq a\Rightarrow x\preceq b (*)$
      if $\neg(a\preceq b)$, then either $a$ and $b$ are incomparable or $b\prec a$
      both cases can't ensure $(*)$
- Problem 10.38
  - (a)
    only if: similar to 37, first we prove $\subseteq$.
      $aRb\Rightarrow a\in L(b)$
      $xRaRb\Rightarrow x\in L(b)$
      then we show $\exists y\in L(b),y\notin L(a)$
      just choose $y=b$ since $bRa$ and $aRb$ can't hold ~~when $aRb\Rightarrow a\neq b$.~~ for Asymmetry.
    if: we have $a\in L(b)$, then $a\neq b$ (otherwise $L(a)=L(b)$ trivially), so we have $aRb$.
  - (b)
    similar to (a), we have $a\in L(b)$,
      if $a=b$, then all is fine.
      if $a\neq b$, we must have $aRb$. Then similarly $bRa$ leading to contradiction since $R$ is Asymmetric.
  - (c)
    if $A=\{1,2,3\},1R2,1R3$ where "asymmetric" and "transitive" hold vacuously, then $L(2)=L(3)$ but $2\neq 3$.
- Problem 10.52
  - (a)
    1. by definition $(a_1,a_2)(R_1\times R_2)(a_1,a_2)\text{ iff }[a_1 R_1 a_1\land a_2 R_2 a_2]$
      Since RHS is T, ...
    2. by definition $(a_1,a_2)(R_1\times R_2)(b_1,b_2)\land(b_1,b_2)(R_1\times R_2)(a_1,a_2)\Rightarrow (a_1 R_1 b_1\land b_1 R_1 a_1) \ldots\Rightarrow a_1=b_1\ldots\Rightarrow (a_1,a_2)=(b_1,b_2)$
    3. similar to 2 but use $a_1 R_1 b_1 R_1 c_1\ldots\Rightarrow a_1 R_1 c_1\ldots\Rightarrow (a_1,a_2)(R_1\times R_2)(c_1,c_2)$
  - (b)
    based on (a) $R_1\times R_2$ is ~~partial order.~~ transitive.
    WLOG suppose $R_1$ is strict.
    Then $a_1 R_1 b_1\Rightarrow \neg(b_1 R_1 a_1)\Rightarrow \neg((b_1,b_2)(R_1\times R_2)(a_1,a_2))$. So Asymmetry
    Then strict.
- Problem 10.58
  - (a)
    trivially by $=$ has all 3 properties.
  - (b)
    $f .a/ D R.a/$ is got from $f(a)$ definition.
    - See the [Math-for-CS-solutions](./others/mcs/sol/Math-for-CS-solutions/MIT6_042JS15_cp18_solutions.pdf).
      - > The proof of the converse a ≡f b IMPLIES aRb is very similar.
        $a\in f(a)$ trivially, so we have $a\in f(b)\Rightarrow bRa\Rightarrow aRb$
- Problem 10.57
  - This is shown in DMIA 9.5.4 THEOREM 1 context.
    - (a) trivial. at least $a\in [a]_R$
    - (b) trivial by the transitive property.
      - $a R b\Rightarrow [a]_R=[b]_R$ so every element is only in one $[a]_R$.
        by Definition 10.5.6, $[a]_R$ is a partition.
    - (c) both directions by transitive property.
       similar to (b) in Problem 10.58.
## 11.1
- Here is one *special* [complete binary tree](https://en.wikipedia.org/wiki/Binary_tree#Types_of_binary_trees)
- > In a tree there is a unique path between every pair of vertices
  This is proved in DMIA 11.1 THEOREM 1.
- $\pi(i)$ is to ensure bijection from $[0..N-1]$ to $[0..N-1]$.
## 11.2
- > This is nearly the best possible with 3  3 switches.
  - TODO see [this one with router](https://serverfault.com/a/150086/1032032) and [this](https://community.spiceworks.com/t/most-efficient-way-to-connect-three-network-switches/950173/2)
- > all paths are the same length
  ~~because all from the bottom level to the bottom level, the *longest* is trivially .~~
  $(IN_{0},OUT_{1})$ latency is different from $(IN_{0},OUT_{3})$.
- > By extending the notion of congestion to networks, we can also distinguish be-tween “good” and “bad” networks with respect to bottleneck problems.
  because congestion occurs when packets flood up which imply the bottleneck.
## 11.3
- 2-D
  - notice Theorem 11.3.1 is based on permutation. So $in_{0\sim 3}\to out_0$ is impossible which may cause the congestion to 4.
  - notice switch size of 2-D may only use 1x2 for some switches.
- Butterfly
  - TODO it seeems to be read in COD / csapp.
  - > 2nC1 .n C 1/ of columns.
    should be $2^{n+1}(n+2)$ for $F_{n+1}$.
    - Then $n+2$ columns -> $n+1$ length
      > from an input switch to an output is length-n C 1
  - By "new inputs" in Figure 11.5, we can get "switch size".
- Lemma 11.3.3
  - The book Beneš is not totally same as [the wikipedia one](https://en.wikipedia.org/wiki/Clos_network#Bene%C5%A1_network_(m_=_n_=_2)).
  - Theorem 12.8.3
    "only if" is trivial which is already shown in DMIA.
    "if" non-cycle must be colored by 2-colors.
    - 2. IMPLIES 3
      - > there will be a walk wu starting at u and ending at r
        this should be shortest walk to ensure uniquity.
        we can color radially from $r$.
      - > So there must be an edge between two nodes u and v with the same color.
        this implies $u,v$ are adjacent. So $|w_u|-|w_v|=2n,n\in\mathbb{N}$.
    - 3. IMPLIES 1
      - This is also implied in Lemma 10.2.6.
    - Notice here if using only "every cycle in it has even length" to show it can be "2-colorable" may be more difficult since it is more easy to find one counterexample than proving valid in all cases.
      i.e. $\exists$ ~~is~~ may probably be easy for $\forall$.
      See [this](https://math.stackexchange.com/a/4910599/1059606)
  - Case 1 ~~can be seen as a single edge as one connected component.~~ See $2-6$ in the  example.
  - > a unique edge hu—vi 2 E1 and a unique edge hu—wi 2 E2 .
    i.e. one in the leftmost and one in the rightmost column.
## chapter 11 problems
- Problem 11.8
  - Assume column 0 is the leftmost column
    then 
    > there is a path from ex-actly 2i input vertices to v
    is trivial by the recursive construction from $i=1$.
    And
    > a path from v to exactly 2n i output vertices.
    is similar.
  - Since the related input/output vertices w.r.t column $i$ is $\min(2^i,2^{n-i})$
    so the congestion will be $2^{n/2}=\sqrt{2^n}=\sqrt{N}$ at column $n/2$.
  - odd:
    similarly $\min(2^i,2^{n-i})$ will take max when $i=(n\pm 1)/2$
    so the congestion will be $2^{(n-1)/2}=\sqrt{N/2}$.
## 12.1
I may use $u-v$ as the edge notation in the following.
> scheduling, constraint satisfaction
This is by letting edge indicating conflict restriction, etc.
- > But a simple graph must have at least one vertex—jV .G/j is required to be at least one.
  This is to [simplify the following discussion](https://math.stackexchange.com/a/276692/1059606).
  And Null graph can be thought as simple graph or [digraph](https://www.sfu.ca/~mdevos/notes/graph/345_digraphs.pdf).
## 12.4
- > Notice that if f is an isomorphism between G and H , then f 1 is an isomor-phism between H and G.
  This is trivial based on bijective function.
  Similar for
  > Isomorphism is also *transitive* because the composition of isomorphisms is an isomorphism.
  Then the above is combined with reflexive, we have
  > In fact, isomorphism is an equivalence rela-tion
- > secure protocols for encryption and remote authentication can be built on the hypothesis that graph isomorphism is computationally exhausting.
  Actually they are [not used](https://crypto.stackexchange.com/questions/34198/are-there-any-crypography-schemes-which-rely-on-graph-isomorphism-not-being-in-p#comment79780_34198).
  - zero-knowledge proof is based on probability.
    > her chance of successfully anticipating all of Victor's requests would be reduced to 1 in 220, or 9.56 × 10−7.
    Here Prover needs to [solve graph isomorphism to be granted access](https://arxiv.org/pdf/1911.09329).
- Some books are [invalid](https://cstheory.stackexchange.com/a/32291).
  - [This](https://web.archive.org/web/20180117232426/https://funkybee.narod.ru/graphs.htm) seems to show the counterexample for [the book](https://web.archive.org/web/20171226183300/http://www.dharwadker.org/tevet/isomorphism/)
  - automorphism [vs](https://math.stackexchange.com/a/790119/1059606) isomorphism referred to in [this](https://algorist.com/problems/Graph_Isomorphism.html) by [this](https://funkybee.narod.ru/graphs.htm)
    [This one](https://www.geeksforgeeks.org/group-isomorphisms-and-automorphisms/#) which says the former doesn't have onto may be wrong.
## 12.5
- Definition 12.5.1 cares about vertice set instead of edge set compared Lemma 11.3.3.
- Compared with The Stable Marriage Problem, Hall’s Matching Theorem doesn't need every man likes *all* women and vice versa with *one list* for each person.
- I skip the proof of Theorem 12.5.2 since it is shown in DMIA.
- > The vertices incident to an edge in M are said to be covered by M
  This is different from [Covering graph](https://en.wikipedia.org/wiki/Covering_graph) and also vertex cover. And it is also different from that in Problem 10.31.
  IMHO here it means inclusion.
- Notice Theorem 12.5.6 is one sufficient condition for "a matching".
  For example we can construct one bipartite graph based on one matching by adding one edge.
  i.e. $E=\{\langle i-idx(i)\rangle\mid i\in A\}\cup\{\langle b-0\rangle,\langle c-0\rangle\}$ where $A$ is the alphabet and $idx(i)='i'-'a'$.
  So $\deg(0)=3>2=\max(\deg(l)),l\in L(G)$
  By the 1st paragraph in the proof of Theorem 12.5.2, we have "the matching condition holds".
- matching means [no one-to-mul or mul-to-one](https://en.wikipedia.org/wiki/Matching_(graph_theory))
  > no two edges share common vertices
## 12.6
- > Since only graphs with no edges—the empty graphs—have chromatic number 1
  - IMHO this has no relations with Lemma 12.6.2
  - This is because one edge must imply at least 2 colors.
## 12.7
- > The walk is a path iff all the vi ’s are different, that is, if i ¤ j , then vi ¤ vj .
  This implies [all edges are distinct](https://qr.ae/psUZgQ).
  > for if an edge is repeated, a vertex is necessarily repeated.
## 12.8
- "connected" definition is based on "path" although we can also define that based on ["walk"][walk_implies_path] generally.
- Definition 12.8.2 is based on radial shape of the component
  and the [wikipedia definition](https://en.wikipedia.org/wiki/Component_(graph_theory)#Definitions_and_examples) is based on
  > there are no paths between vertices in different pieces.
## 12.10
- Definition 12.10.1 also see [wikipedia](https://en.wikipedia.org/wiki/K-edge-connected_graph#Formal_definition)
  - "at least one of the paths" is thought as one set.
  - "max-flow min-cut theorem" is temporarily skipped.
## 12.11 (12.11.4* which generalizes Prim's and Kruskal’s algorithm)
- "circuit" can be one simple graph which is [different from simple circuit](https://en.wikipedia.org/wiki/Cycle_(graph_theory)#Circuit_and_cycle).
- > The forest in Figure 12.18 has 4 leaves
  here the root is also one leaf in ["an unrooted tree"](https://mathworld.wolfram.com/TreeLeaf.html).
- In Definition 12.11.2, "at most one" should be [just one](https://mathworld.wolfram.com/TreeLeaf.html)
  This is [the definition in maths graph theory](https://stackoverflow.com/a/33987475/21294350) instead of in CS.
- > A forest with an isolated vertex won’t be connected unless it consists of just the one vertex
  Here it can be still [thought as one tree](https://math.stackexchange.com/a/3909178/1059606).
- "edge-maximal acyclic" means [the edge number is maximal when acyclic](https://math.stackexchange.com/a/2116227/1059606). Similar for "edge-minimal connected".
  This [may be different from maximally edge-connected](https://math.stackexchange.com/q/4915005/1059606).
  - When vertex- and edge-connectivity can be [less than minimum degree](https://mathoverflow.net/a/423085)
- Lemma 12.11.3 proof is based on 2 cases where we assume $u-v_1,v_1\notin \textbf{k}$ or $u-v_2,v_2\in \textbf{k}$ where $\textbf{k}$ is the longest path.
- Theorem 12.11.4
  - (3) implies (4)
    - Here it drops the proof of *at least one* path which can be proved using cycle implies 2 paths between each pair of vertices.
    - [trivial graph definition](https://www.prepbytes.com/blog/graphs/trivial-graph-in-graph-theory/#:~:text=Trivial%20Graph%3A%20Contains%20only%20one,in%20a%20more%20complex%20structure.)
    - Based on [walk_implies_path] which also means trail (i.e. simple path in DMIA) implies path, we can use DMIA 10.4-59 to solve with the above directly using one method to *construct the cycle*.
      Since that proof doesn't need each walk / path in DMIA to have *distinct vertices*, so we can directly use that proof.
      That proof is based on *comparison* of these 2 walks/paths by inspecting vertices one by one.
      - Rephrase:
        - > If they diverge only after one of them has ended, then the rest of the other path is a simple circuit from v to v
          This is impossible here since $v$ is duplicate in the walk so the *longer* walk is not one path.
        - > we follow it along—forwards or backwards, as necessary—to return to xi
          here "forwards" is impossible since it implies the cross point *has been met* and then we forward to $x_i$ as before. Then the *longer* walk is not one path.
        - Similarly see "no duplicate vertex ..." in DMIA notes for the only case the cycle can occur.
    - Also see [this](https://chat.stackexchange.com/transcript/message/24773662#24773662) although it is incomplete.
    - The book proof is same as [this](https://math.stackexchange.com/a/1484818/1059606)
    - Notice this [doesn't prove for the infinite forest](https://math.stackexchange.com/a/98098/1059606).
      > the time would never come when the whole train would be in motion.
      - From now on, I  didn't focus comparison between finite graphs and infinite graphs since it seems to be [one heavy work](https://1stprinciples.wordpress.com/2008/03/11/infinite-trees-have-no-leaves/) as 12.4 says
        > In the rest of this chapter we’ll assume graphs are finite.
      - infinite graph [may not have leaves](https://en.wikipedia.org/wiki/Eulerian_path#In_infinite_graphs) as DMIA says.
- Theorem 12.11.5 is same as DMIA 11.1-31.
- Theorem 12.11.6
  - > G E has one component
    due to connected.
  - > So by WOP
    based on edge number and connectivity.
- Lemma 12.11.10: here "gray edge" is different from that in "white path theorem".
  - > Therefore at some point on the path there has to be an edge that starts with a black vertex and ends with a white one.
    This is said similarly in one DMIA exercise answer.
- Theorem 12.11.12
  - > decreases the number of connected components of S by one
    This implies still "spanning forest".
  - Lemma 12.11.11 is based on the assumption
    > assume there are no same-weight edges:
- Lemma 12.11.14 shares the same idea as DMIA proof of Prim's and Kruskal’s algorithm by constructing MST step by step based on adding and deleting one edge.
  - notice $+e$ only causes one cycle. See DMIA [tree_iff_add_any_edge] and "proves exactly one".
    This is enough to ensure "connected" although trivial since adding one edge must keep connectedness.
    Then "connected" + "acyclic" -> tree.
    - > if C is a spanning tree of G, then C g C e will also be a spanning tree
      We can also be based on Theorem 12.11.6 (3)->(1).
      Then "connected" + "edge number" -> tree.
  - Since we only manipulate with edges, so "spanning" is kept.
- > such that all the vertices in the same connected component of S have the same color.
  - Algorithm 1
    - Here "exactly one endpoint" ensures "acyclic" kept.
    - > This is the algorithm that comes from coloring the growing tree white and all the vertices not in the tree black.
      So it constructs one partition of size 2 based on the original component partition.
      So Algorithm 3 is similar to it.
  - Algorithm 2
    - > An edge does not create a cycle in S iff it connects different components of S .
      "only if" assume by contradiction that "it connects" the same component, then cycle ...
      "if" trivial.
    - > adding a minimum weight edge among the edges that do not create a cycle in S 
      This can be done by finding the "minimum weight edge" and then assigning different colors to  the 2 components which each endpoint is in.
  - Algorithm 3
    - > with limited communication between processors.
      [See](https://stackoverflow.com/a/46161900/21294350)
      > Higher L3 latency means bandwidth is limited by the number of outstanding L1 or L2 *misses / prefetch* requests.
      Here L1/2 miss will [cause L2/3 prefetch](https://developer.arm.com/documentation/ddi0488/h/level-2-memory-system/l2-cache-prefetcher). Also [see](https://community.intel.com/t5/Software-Tuning-Performance/Understanding-L1-L2-L3-misses/td-p/1056573)
      > where processor sends lot of L1 miss requests quickly to L2
## chapter 12 problems
Search "Problems" or "Problem ".
- Problem 12.31
  - (a)
    - Figure 12.30
    See [this][3_SAT_to_3_Coloring]
    we only needs triangle with $N$ to ensure only $T,F$ are assigned to literals.
    - Then the OR gate is based on $(P,Q,[P,P\lor Q],[Q,P\lor Q],P\lor Q)=(T,T,F,N,T),(T,F,F,N,T),(F,T,N,F,T),(F,F,T,N,F)$ where $[P,P\lor Q]$ means the vertex adjacent to both vertices.
      Here we ensure 
      1. only $T,F$ are assigned to $P,Q$
      2. inspect all $2^2=4$ cases for $P,Q$
      3. the output is OR.
      - Notice since 3-colorable is one possible minimum coloring, this doesn't mean we *must use 3 colors* but means we can.
        So the above gives one possible assignment of $T,F$.
  - (b) since here it doesn't need $P$.
    So we can [transform E into DNF which is NP-hard](https://en.wikipedia.org/wiki/Conjunctive_normal_form#Computational_complexity).
    Then follow [3_SAT_to_3_Coloring] but here we need $n-1$ OR gates for each clause.
  - (c) [3_SAT_to_3_Coloring] and [this](https://cs.bme.hu/thalg/3sat-to-3col.pdf) all assumes clause form is the prerequisite condition. So an efficient procedure for 3-colorable mean an efficient procedure for SAT with the DNF/CNF form.
  - Notice 3-colorable [maybe can't be reduced to 2-SAT](https://cs.stackexchange.com/a/13083/161388).
  - [This](https://math.stackexchange.com/q/2010628/1059606) is one a bit different problem since it cares about subset.
    [This](https://math.stackexchange.com/q/1032515/1059606) says about fixed color. But in [3_SAT_to_3_Coloring] it just use $T,F,N(one)$ where $N$ is interpreted by me as None.
  - See [sol_20]
    The above needs proving "iff".
    TODO (c) in that sol.
- 12.32
  - (a) [see](https://www.overleaf.com/read/skjcnqsbsjgf#ca8e3c)
  - (b) implied by (a).
    Since the crossing have only 4 cases, we are done.
  - By the replacement, "no easier" mean "same as".
- Problem 12.44
  - (a) based on in-degree and out-degree when following the walk.
  - (b) otherwise not one connected graph.
  - (c) Notice here we [need "finite"](https://en.wikipedia.org/wiki/Eulerian_path#In_infinite_graphs) to make the theorem work.
    - IMHO maybe the book use "longest" and "at most once" to prove exactly "once".
      But that doesn't use the "even" condition. TODO
    - Better see DMIA proof based on construction of such a tour.
  - (d) ~~This is not based on closed walk, so this means we can continuing the end to find one bigger walk if some edges incident to it are unincluded?~~
    Since we can add that unincluded edge to construct one longer walk, contradiction.
  - (e) trivial based on the degree equals $2n+1$ where $n$ is the pass count of the end vertex.
  - (f) based on (e,b) we know $w$ must be closed and then an Euler tour.
- Problem 12.35
  - $u-p-\textbf{w_{pq}}-q-v$
    If $w_{pq}$ can have more than 1 choices, then we are done.
  - > There is a five-vertex graph that exhibits this property.
    e.g. $u-p-q-v,p-k-q$
  - > Then either u and w, or w and v, must be a dpp
## 13.1
- Figure 13.2 This means is there one planar $K_5$ complete graph.
- > are helpful in displaying graphical data such as program flow charts
  See [this](https://stackoverflow.com/a/2593143/21294350) 
  TODO [linear time testing](https://stackoverflow.com/questions/2445313/provable-planarity-of-flowcharts#comment2600654_2445371)
- [This (See Figure 3)](https://digitalcommons.morris.umn.edu/cgi/viewcontent.cgi?article=1049&context=horizons) is different from [Conflict graphs](https://www.math.cmu.edu/~bkell/21110-2010s/conflict-graphs.html) in the book.
## 13.2*
- **Compared with DMIA definition** Definition 1 in 10.7 which doesn't restrict how we draw, mcs cares about "how we draw" by in Definition 13.2.1.
- connected region see [this "Definition"](https://math.mit.edu/~jorloff/suppnotes/suppnotes02/v5.pdf) which is related with complex analysis.
- Constructor case (split a face)
  Here we assume these 2 paths $\alpha,\beta$ are totally disjoint. So we can layout them like the bipartite graph.
  If they share some vertices except for $a,b$, then by WOP assume $k$ is the *first* shared non-adjacent vertex, then the 2 path from $b$ to $k$ constructs one cycle, contradiction.
  If adjacent, then we begin from $k$ and follow the above process again by seeing $k$ as the new $b$ OR we can say $b-k$ should not be considered inside that face.
  If all are adjacent, i.e. line graph in the footnote ...
- Constructor case (add a bridge)
  - > Suppose G and H are connected graphs with planar embeddings and disjoint sets of vertices
    i.e. 2 connected components based on "A planar embedding of a connected graph" in Definition 13.2.2 which causes "G and H" each to have only one connected component.
  - > suppose that $\gamma$ begins and ends at vertex a.
    As the example shows, $\gamma$ can have multiple different instances. But only one will consider the added $a-b$ due to that it is the "cut edge".
  - > as op-posed to once on each of two faces
    i.e. 2 sides.
- 2 Constructor case's are complete since adding one edge based on whether 2 endpoints are in the same component will only imply 2 cases.
  Here all assume adding such one edge is possible to keep "planar".
  But it is not always that case, e.g. adding one edge to one of the connected graphs in Figure 13.4.
  But we temporarily skipped that digging.
  > Of course we can’t prove this without an excursion into exactly the kind of continuous math that we’re trying to avoid.
- > a planar embedding could be drawn with any given face on the outside
  [See](https://mathematica.stackexchange.com/a/244393)
  > stretching the puncture hole to a circle around the rest of the faces, and flattening the circular drawing onto the plane.
  The above is just one "An intuitive explanation" instead of strictly considering all cases.
  TODO There are too many cases. For example, think of one very big map/grid.
  If we want to take the center square in one grid as the outer face, then how to ensure the edge relation is kept and the planar property is also kept at the same time?
## 13.3
- The proof of Theorem 13.3.1 in DMIA is based on adding one edge to *one connected graph*.
  But here we may connect 2 connected graphs based on the definition of "planar embedding".
  - The former skips the *trival graph*.
## 13.4
- > once in each of two different faces, or occurs exactly twice in one face.
  i.e. split or bridge.
- Lemma 13.4.2
  - base case
    based on [this](https://houseofgraphs.org/result-graphs)
    ```bash
    # adjacency list
    1: 2 3
    2: 1 3
    3: 1 2

    1: 3
    2: 3
    3: 1 2
    ```
    the inside face and outside face in the above 2 graphs are same with length 3 and 4 each.
  - Constructor case
    - Here it probably assumes simple graph since $a-b$ with 2 edges has one face of length 2.
      Then split in the extreme case has one triangle which has length 3.
    - bridge
      > these two graphs with a bridge merges the two bridged faces into a single face, and leaves all other faces unchanged.
      So the changed outer face length is $2+l(G_{sub})+l(H_{sub})$ where $G_{sub}$ means the changed face in $G$. Then still length at least 3.
- Theorem 13.4.3 is same as DMIA 10.7 COROLLARY 1 proof where it assumes without proof
  > (either in two different regions, or twice in the same region). Because each region has degree greater than or equal to three
## 13.5
- Theorem 13.5.3 is same as DMIA 10.7 COROLLARY 3 but the former targets at one more specific graph "connected bipartite graph".
## 13.6
- Lemma 13.6.1 has been proved in Problem 13.9 (d)
  - Lemma 13.6.2 ~~can be done by letting the merged edge length zero since the graph doesn't depend on edge length.~~ (The strikethrough sentence still keeps the edge constraint which can be stretched to make one planar graph. But merged graph doesn't have such one constraint. So they are not equivalent directly.)
    If using structural induction, then based on Figure 13.9 and Figure 13.10 we can merge that added edge (still this is not one strict proof).
    - Compared with DMIA 10.8-41 where it is based on interchanging color, here we merge until the adjacent vertices of v become 4.
## 13.7*
the green underlined words lack strict proofs.
- We can understand Figure 13.14 by projecting them onto the sphere.
  (c) can be seen as use one triangle face as the base then expand following the rest edges.
  - [The mere Stereographic projection](https://www.cosmic-core.org/free/article-42-geometry-platonic-solids-part-3-spherical-stereographic-solids/).
  - Also see [this by stretching][plus_math_polyhedron].
- [nondegenerate polygon](https://en.wikipedia.org/wiki/Degeneracy_(mathematics)#Triangle) i.e. at least the area is greater than 0.
- > at least 3 polygons must meet to form a corner, so $m \ge 3$
  if there is 2, then it can't be 3D.
  ~~one non-strict proof: 2 lines construct one plane, suppose there is one exception TODO~~
  ~~trivially each face is one cycle which already implies ~~
  Also we can use the claim in geometry that at least 3 planes are needed to decide one vertex.
- > m edges incident to each of the v vertices.
  implied by "Let m be *the number of faces* that meet at each corner of a polyhedron" without the strict proof
- $mv=2e$ is based on one edge will be counted twice by each endpoint and $nf=2e$ is based on one edge will be counted twice by the 2 faces crossed to decide that edge.
- > Checking the finitely-many cases that remain turns up only five solutions
  This can be also done by [checking the *corner angle*](https://www.reddit.com/r/explainlikeimfive/comments/nrxcds/comment/h0j9rcj/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)
  - > 3 regular hexagons connected by their corners form a plane and can’t actually fold into a corner
    i.e. $3\cdot 120=360$ which must be in one plane.
  - notice the total symmetry.
  - TODO why icosahedron has more faces than dodecahedron since the corner angle is $60\cdot 5=300$ vs $108\cdot 3=324$? (Use geometry proof instead of algebraic)
- > The largest polyhedron, the dodecahedron, was the other great mathematical secret of the Pythagorean sect.
  See [Platonic solid](https://www.britannica.com/science/Platonic-solid) although they are [not actually the first](https://www.math.lsu.edu/art/quantum-connections/pythagoras#:~:text=Pythagoreans%20discovered%20the%20dodecahedron%2C%20the%20fifth%20regular/Platonic,However%2C%20the%20Pythagoreans%20gave%20the%20mathematical%20proof.) to find that.
- > so that they uniformly blanket the globe—tough luck!
  this seeems to assume polyhedra since sphere may probably be uniformly split.
- Definition 13.8.2 is the reverse operation of [subdivision](https://en.wikipedia.org/wiki/Homeomorphism_(graph_theory)#Subdivision_and_smoothing) (i.e. remove $e_1$ and then merge $w,u$)
  remove vertex is implied by [subgraph](https://en.wikipedia.org/wiki/Kuratowski%27s_theorem)
## chapter 13 problems
- Problem 13.9
  - (a) 
    To make (c) work, we take all 4 cases in account although some may not "obtain a planar embedding" but multiple.
    Notice we only consider planar embeddings *changed* because those unchanged trivially won't influence the result.
    - ~~one~~ both of them is "split", trivially they are independent since the operation only operates *inside* the connected component. Then we can switch.
    - $e$ is "split" and $f$ is "bridge"
      Since the splitted component can't influence the "bridge" between 2 component (i.e. operation *inside* the component doesn't influence the operation *outside* (see 13.2.4) the component), then we can switch.
    - $e$ is "bridge" and $f$ is "split"
      one case is dual of the above
      - the other is "split" of the combined graph instead of one of 2 graphs to combine.
        Here it must split the *outer face* as Figure 13.10 shows (the strict proof may need geometry. I didn't dig into that.)
        Then we can switch that (still I didn't dig into that due to the need of geometry. We can use Figure 13.10 where we see the 2 components as one *big vertex*, then all is trivial). (1)
    - both are "bridge".
      - 2 outside non-crossing edges can be swapped. Same as (1).
  - (b) 
    - This is based on [each permutation can be done with swap of adjacent elements @%@ (@%@ means it is not read)](https://math.stackexchange.com/a/3791184/1059606).
      This is probably done in DMIA with one Stack Exchange link where the link is temporarily not found. TODO
    - IMHO "By induction on the number of switches" is not needed.
      Since the swap number must be finite based on the above proof, we are done using (a).
  - (c)
    if same as Minimum-Weight Gray Edge Procedure, we start with $n$ vertices,
    then based on (b) we can get one arbitrary set of planar embeddings which by 13.2.3 is a planar graph.
    Then if we want to delete edge $k$, we can use (b) to let it be the last edge and then revert the last operation we still get one planar graph.
  - (d)
    trivially deleting vertices doesn't influence "planar". Then with (c), we are done.
## 14.1
- > Perhaps surprisingly, but certainly not coincidentally, these two numbers are the same: 1820.
  $C_{12+5-1}^{4}=C_{16}^{4}=1820$
  Also see 15.1.1.
- > at most 2 log n multiplications
  here only keeps the main part (see p184)
- > $50,000 a year for 20 years ought to be worth less than a million dollars right now
  This assumes currency inflation.
- Notice (14.7) saying about $0.999\cdots$
## 14.4*
- Figure 14.5
  - physics [proof](https://www.mathscareers.org.uk/the-infinite-block-stacking-problem-or-the-leaning-tower-of-lire/) using "moment" from [wikipedia](https://en.wikipedia.org/wiki/Block-stacking_problem#Proof_of_solution_of_single-wide_variant)
    - Possible overhang with one block: trivial by symmetry although we can also prove using "moment".
    - Possible overhang with two blocks:
      - $l/2$ is got by seeing the 1st block and the table as one whole entity. Then follow "Possible overhang with one block".
      - Notice here we see 2 blocks each as one small entity giving the gravity force at the *center of mass*. So $x,l/2-x$.
        > The blocks can be modelled as point-masses located at the center of each block, assuming uniform mass-density.
    - Possible overhang with three blocks
      - "balance point" can be seen as "center of mass" (here I didn't give one strict proof.)
      - The above doesn't influence the proof
        we only need one equivalent of $2mg$ which is very trivial.
  - [more elegant proof](https://web.archive.org/web/20231204233816/http://wrean.ca/cazelais/block_problem.pdf) also from wikipedia
    - Here $d_{n,n-1}$ is calculated [based on center of mass](https://raptor-scientific.com/resources/center-of-gravity/#:~:text=M%20%3D%20W%20x%20d%3A%20Where%20M,of%20gravity%20of%20the%20object.)
    - We thought the right edge is the pivot vertical line generalized from pivot point.
      Also [see](https://www.ncl.ac.uk/webtemplate/ask-assets/external/maths-resources/mechanics/moments-main/moments.html#:~:text=The%20moment%20of%20a%20force%20about%20a%20point%20is%20(the,the%20force%20from%20the%20point).)
  - We can also use ["center of mass"](https://physlab.org/wp-content/uploads/2020/02/Stacking-4.pdf)
    The formula is same as mathscareers link.
    e.g. for (2) we have $mgx+mg\cdot(-(\frac{l}{2}-x))=0$.
    - (4) using mathematical induction
      Let $S_{n+1}-S_n=x$, then as mathscareers says, we have $nmgx+mg\cdot(-(\frac{l}{2}-x))=0\Rightarrow x=\frac{l}{2(n+1)}$. This is what Figure 4 shows.
  - wikipedia
    - > by assuming the inductive hypothesis
      i.e. all have the form $\frac{l}{2k}$.
  - mcs proof
    - > But now the center of mass of the bottom book has horizontal coordinate 1=2
      it uses "center of mass" coordinate. Here the positive direction is the left direction.
- > Moreover, the bottom book extends 3/4 of a book length past the end of the table
  i.e. $1-\frac{1}{4}$. In Figure 14.8 (a) we take the table edge as the pivot line. Then use the same  analysis process as mathscareers.
  > which is the same as the maximum overhang for the top book in a two book stack.
  Notice this doesn't hold the the 3rd and more.
  For 3rd, it is because $1-\frac{1}{6}\neq \sum_{k=1}^{3}\frac{1}{2k}$.
  ```python
  # trivial
  from fractions import Fraction
  Fraction('3/4')+Fraction('1/6')-Fraction('1/3')-Fraction('1/2')
  ```
- I skipped [this reference](https://sci-hub.se/10.1088/0031-9120/42/1/F05) because it seems to be [too more about physics](https://archive.org/details/GurskiiElementaryPhysicsProblemsAndSolutions/page/n87/mode/2up)
  also skipped [16], [Maximum Overhang](https://maa.org/sites/default/files/pdf/upload_library/22/Robbins/Patterson2.pdf) since it is one a bit heavy work.
## 14.5
- Theorem 14.5.1
  [See](https://en.wikipedia.org/wiki/Stirling's_approximation#Speed_of_convergence_and_error_estimates) -> [paper](https://sci-hub.se/https://doi.org/10.2307/2308012)
  - (7) is based on $3^k>2k+1,k\ge 2$.
    the last step 
    LHS=$\frac{1}{12(p^2+p+\frac{1}{6})}$
    RHS=$\frac{1}{12(p^2+p+\frac{p+(p+1)}{12})+\frac{1}{12}\cdot(1+\frac{1}{12})}$
  - ~~TODO how to get~~ (9) by canceling consecutive shared terms.
  - $\log(\frac{1+x}{1-x})$ see [this -> $\log(1+x)-\log(1-x)$](https://socratic.org/questions/how-do-you-find-the-maclaurin-series-expansion-of-ln-1-x-1-x) Then use [this](https://math.stackexchange.com/a/878376/1059606)
  - > may be shown by one of the usual methods to have the value V/2i
    This is based on $n!\sim {\sqrt {2\pi n}}\left({\frac {n}{e}}\right)^{n}$. See DMIA notes.
  - > The editor has pointed out ...
    - > Then the serie
      That is $\epsilon_p+1$.
    - $\frac{v_n}{v_{n+1}}=e^{\epsilon_n-(\frac{1}{12n}-\frac{1}{12(n+1)})}$
    - $\frac{u_{n+1}}{u_{n}}=e^{-\epsilon_n}$
      so $u_{\infty}=u_1\cdot e^{\sum_{n=1}^{\infty}-\epsilon_n}$. This is definition of $C$.
    - > where rn satisfies (2)
      This is from $v_n < C < w_n$. Then we have $u_n<Ce^{\frac{1}{12n}}$ ...
- > Theorem 14.5.1 can be proved by induction (with some pain)
  I skipped this due to that is probably mechanic.
- > For n  10, this means we will be within 1% of the correct value.
  ~~This means error~~
  ```python
  1/math.exp(1/120)
  Out[3]: 0.991701292638876
  1/math.exp(1/1200)
  Out[4]: 0.9991670137924582
  ```
  - Here we assume "the correct value" as the form without $e^{\epsilon_n}$ since that factor can't get the exact value.
  - > For n  10, this means that either bound will be within 0.01% of the correct value. For n  100, the error will be less than 0.0001%.
    ~~TODO What does this mean?~~
    ```python
    bound=lambda n:1/math.exp(1/144*n**2+12*n)
    bound(10)
    Out[6]: 3.8288537799628814e-53
    ```
  - Table 14.1
    ```python
    # Table 14.1 row 1
    acc=lambda n:(math.sqrt(2*math.pi*n)*(n/math.e)**n-math.factorial(n))/math.factorial(n)
    for i in range(4):
      print(acc(10**i))
    -0.07786299110421091
    -0.008295960443938127
    -0.000832983432148802
    OverflowError: (34, 'Numerical result out of range')
    ```
  - 
    ```python
    approx=lambda n:math.sqrt(2*math.pi*n)*(n/math.e)**n
    acc=lambda n:(approx(n)-math.factorial(n))/approx(n)
    for i in range(4):
      print(acc(10**i))
    -0.08443755141922758
    -0.008365359132399853
    -0.0008336778720039303
    ```
## 14.6
- (14.28) is one exact value which is close to $n\ln n-n+\ln n$ also close to $n\ln n-n+1$.
## 14.7
- Little Oh see DMIA 3.2-63.
- Lemma 14.7.3
  - ~~TODO How to ensure~~ $\sqrt{x^{\delta}}\ge 1$ since we considers $x\to \infty$
  - also [see @%@](https://math.stackexchange.com/a/601462/1059606)
- > Lemma 14.7.3 and Corollary 14.7.4 can also be proved using l’Hôpital’s Rule or the Maclaurin Series for log x and e x
  So I skipped the proof of Corollary 14.7.4.
- $\le c$ implies $\limsup\ldots<\infty$.
- > as large as 8d/c
  Does this mean "8d or 8c"?
- $\sim$ implies having limit but $\Theta$ same as $O$ may not.
  > We need lim sup’s in Definition 14.7.5 to cover cases when limits don’t exist.
- $\lim e^{\frac{1}{12n}}=1\Rightarrow e^{\frac{1}{12n}}+1=o(f(n)),\lim f(n)\neq 0$
- > For example, f  g in general does not even imply that 3f D ‚ .3g /
  See [this](https://math.stackexchange.com/a/4916846/1059606)
- Similar to from $o$ we can get $O$, we can get $\Omega$ from $\omega$.
## chapter 14 problems
- Problem 14.2 (trivial by algebraic calculation)
  $$
  \begin{align*}
    zT&=z^2+\ldots+nz^{n+1}\\
    (1-z)T&=z+z^2+\ldots+z^n-nz^{n+1}\\
    T&=\frac{1}{1-z}\cdot(\frac{1-z^{n+1}}{1-z}-1-nz^{n+1})
  \end{align*}
  $$
- Problem 14.10 (trivial by mirror the the plot with the middle vertical line as the axis) (Also see Math-for-CS-solutions)
- Problem 14.27
  - (a) see above
  - (b) see [this](https://math.stackexchange.com/q/2183605/1059606)
    notice if $\lim \ln g(x)=0$, then $\lim \frac{\ln f(x)}{\ln g(x)}=1$ may not hold as OP says.
  - (c) We have $\lim \frac{\log(2\pi n)^{\frac{1}{2}}+\log n^n-n}{\log(n!)}=1$
    - if we have $\lim \frac{n}{\log(n!)}=0$, then we have $\lim \frac{\log(2\pi n)^{\frac{1}{2}}}{\log(n!)}=\lim \frac{\frac{1}{2}\log(2\pi)}{\log(n!)}+\frac{\frac{1}{2}\log(n)}{\log(n!)}=\lim \frac{1}{2}\frac{\log(n)}{\log(n!)}\overbrace{=}^{\log n<n}0$
    Then we have $\lim \frac{\log n^n}{\log(n!)}=1$
      - [Proof of the assumption](https://math.stackexchange.com/a/4916905/1059606)
        - [This](https://math.stackexchange.com/a/4916904/1059606) is based on [this](https://math.stackexchange.com/a/704506/1059606)
        - Stolz–Cesàro theorem seems to be [not said in calculus](https://rodrigopacios.github.io/mrpacios/download/Thomas_Calculus.pdf). So I didn't follow [this ans](https://math.stackexchange.com/a/4916902/1059606).
    - Also see [this](https://math.stackexchange.com/a/377012/1059606) and [the comment using ${\displaystyle \ln(n!)=n\ln n-n+O(\ln n),}$ "one liner" directly](https://math.stackexchange.com/questions/376988/limit-of-frac-lognn-logn-as-n-to-infty#comment809135_377012)
      This can be proved using the equation above (14.24). Suppose we have $\ln(n!)=n\ln n-n+g(n)$ then $\limsup g(n)/\ln n<\frac{1+\ln n}{\ln n}=1<\infty$.
      Then we have $\lim O(\ln n)/n\ln n=0$ since although $O(\ln n)/\ln n$ may oscillate but it must be similar to one constant, then $0\cdot O(\ln n)/\ln n=0$.
      Then one liner $\lim \ln(n!)/n\ln n=\lim 1-1/\ln n+0=1$
    - Also see [this](https://math.stackexchange.com/a/377087/1059606) by step by step approximation.
    - [$\lim\limits_{n \to\infty} \frac{n!}{n^n}$](https://math.stackexchange.com/a/61741/1059606)
      is not equal to [$\lim_{n\to\infty}\frac{\sqrt[n]{n!}}{n}$](https://math.stackexchange.com/a/201911/1059606) since $\lim f/g= \lim \ln f/\ln g$ is not necessary.
- Problems 14.14 and 14.16 (chapter 19 reference)
  - 14.14
    - 7
      - Here we can let the sum be one arbitrary number. [See Riemann’s Theorem.][Rearranging_Alternating_Harmonic_Series] (This also proves the limit of the original "Alternating Harmonic Series".)
        - outline
          i.e. oscillate around the target $S$ and let the term absolute decreasing.
        - Abel's theorem
          - TODO after real analysis [proof of Abel's theorem](https://en.wikipedia.org/wiki/Abel%27s_theorem#Outline_of_proof)
          - p18 adds contrived zeroes into the sequence
          - TODO construction of "This idea works more generally:".
          - Based on the formula in p23 or p26 (they are same), if we use that formula then the solution is not one obvious fraction.
            ```python
            from sympy import *
            init_printing()
            x = Symbol('x')
            solve(ln(2)-1/2*log(x/(1-x))-7, x)
            ```
            ~~I skipped the contents after p~~
          - P29 Outline of the proof proves ~~"if" part.~~
            ~~"only if"~~ ~~is~~ "iff" part implied in p32 "partial sum" where only $\frac{p_k}{q_k}$ limit is undetermined.
          - TODO What is p36's purpose since it seems one arbitrary $\alpha$ is possible?
        - Here we should use Riemann’s Theorem to achieve one arbitrary number like 7 although the pattern is not known.
          - also see [this @%@](https://math.stackexchange.com/a/2721579/1059606) for the exact solution.
    - $\infty$
      See [this](https://math.stackexchange.com/a/2969950/1059606)
      Notice here scaling is more loosed.
      - IMHO here $N_2$ corresponds to $(3,5)$
        then $N_3$ corresponds to $x\in (2,3)$ which is added to the sum with the range is changed to $(4,5)$.
  - 14.16
    See [Rearranging_Alternating_Harmonic_Series]
## 15.1
sections using bijection (not complete): 15.6,7.
## 15.3
- > but how—even with assistance—could I put on all three at once?
  i.e. if 3 people assist, then those people putting on the socks must interfere with that one putting on the pants, so not "at once".
## 15.4
- Rule 15.4.1 assumes no 1-mul so these mappings of each element in the codomain is *disjoint*.
## 15.5
- Corollary 15.5.3 uses $\binom{n}{k}=\binom{n}{n-k}$
## 15.6
- > letting the 1st subset in the split be the first k1 elements of the permutation
  from unordered to ordered, so divide by $k_i!$.
- Definition 15.6.1
  if we use $\sum k_i=p<n$, then the equation becomes $\frac{P_{p}^{n}}{\prod k_i!}$. This is done by 2 steps where firstly choose p and permutate secondly take collision in account.
- [Application](https://en.wikipedia.org/wiki/Multinomial_theorem#Theorem) of Subset Split Rule based on generalization from [this](https://en.wikipedia.org/wiki/Binomial_coefficient#Definition_and_interpretations)
  See Theorem 15.6.5
## 15.7
- 15.7.3 "For example, the following sequences and hands correspond: ..."
  Here LHS have no *element groups* in the tuple which has the same structure.
  Compared with the 1st approach, step 1,2 and step 3,4 are duplicate actions.
## 15.8
- Here $|B|$ is one very vague estimate since we can't take every element in that range.
- > a math major figured out how to reformulate the sum problem as a “lattice basis reduction” problem;
  See [this point 1(I didn't dig into the codes)](https://stackoverflow.com/a/443950/21294350)
  - [this](https://hackmd.io/@alxiong/ssp-from-lll?utm_source=preview-mode&utm_medium=rec#Second-Attempts) or [this](https://web.stevens.edu/algebraic/Files/SubsetSum/p229-lagarias.pdf)
    TODO how to ensure we can reach one state where $c_i=0/1,i=1\sim n$ and $c_{n+1}=1$
  - notice lattice constructs one [integer grid Definition 1.1](https://uu.diva-portal.org/smash/get/diva2:1641300/FULLTEXT01.pdf).
- > One way is to use powers of two:
  This is based on binary representation (This is bijective to the subset) of the number in $[0,31]$.
  > For example, we could safely replace 16 by 17, but not by 15.
  just increase those sum numbers greater than 15 by one.
- Sets with Distinct Subset Sums can be constructed based on one [arbitrary set of subset sum](https://math.stackexchange.com/a/1074810/1059606).
  - I skipped [this paper](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v5i1r3/pdf) and [this reddit post](https://www.reddit.com/r/askmath/comments/4y2a0f/sets_with_certain_distinct_subsets/) is much less valuable
  - Notice here $T'$ or the typo $T$ mean "*generating* set", i.e. one version of $B$.
  - TODO [Conway-Guy Sequence](https://math.stackexchange.com/a/4079549/1059606) proof
  - Paul Erdős [conjecture](https://www.sciencedirect.com/science/article/abs/pii/S0166218X22004103#:~:text=Let%20%7B%20a%201%20%2C%20.%20.,c%20%E2%8B%85%202%20n%20%2F%20n%20.)
    TODO why [$min{max}$](http://www.openproblemgarden.org/op/sets_with_distinct_subset_sums) since that may allow $16$ for $n=5$ as the box shows.
- > Here is one:
  ```python
  from itertools import chain, combinations
  s=[6,9, 11,12, 13]
  sums=[]
  for i in chain.from_iterable(combinations(s, r) for r in range(len(s)+1)):
    sums.append(i)
    print(i,sum(i))
  # https://stackoverflow.com/a/1541827/21294350
  print(len(sums)==len(set(sums)))
  ```
  - TODO one more elegant proof that subset sums are distinct.
- > the Assistant must reveal the same sequence of three cards for at least
  This means *at least for one sequence* of three cards.
### 15.8.5
- > The more counterclockwise of these two cards is revealed first
  ~~This should be "clockwise".~~
  > The rank of the secret card is between 1 and 6 hops clockwise from the rank of the first card revealed
  ~~What if pair (10,6)?~~
  Here "counterclockwise" means the relation based on
  > one is always between 1 and 6 hops clockwise from the other.
  instead of starting from A.
- > It turns out that there is a method which they could actually learn to use with a reasonable amount of practice for a 124-card deck, but we won’t explain it here
  I skipped [this](https://www.apprendre-en-ligne.net/crypto/magie/card.pdf) since it may be one mere generalization from 52 to 124.
## chapter 15 problems
- Problem 15.59
  I read [one proof based on induction](https://math.stackexchange.com/a/1674481/1059606) before in one pdf (temporarily not found).
  - (a) choose $1/x_i$ for each multiplicand we get RHS.
  - (b) 
    (15.14) 2 cases for whether $x\in T$.
    (15.15) trivial based on the definition of $\cap$.
    (15.16) based on when one $M_i=1$, then LHS=1.
  - (c) 
    $LHS=1-\prod_{i\in I}(1-M_i)=1-\sum_{I\ldots}(-1)^{|I|}\prod_{j\in I}M_j=RHS$
  - (d) This means iterating for all elements and check whether in. If so contribute 1 to the size.
  - (e)
    $|U|=\sum_{u\in U}M_{U}(u)\overbrace{=}^{15.17}\sum_{u\in U}\sum_{\varnothing\neq \ldots}(-1)^{|I|+1} \prod_{j\in I}M_j(u)\overbrace{=}^{\text{swap the sum order and }(15.15)}\sum_{\varnothing\neq \ldots}(-1)^{|I|+1} \sum_{u\in U} M_{\cap_{i\in I}S_i}(u)\overbrace{=}^{15.18}\sum_{\varnothing\neq \ldots}(-1)^{|I|+1} |\cap_{i\in I}S_i|$
  - (f)
    trivial by pulling $|I|$ out with one variable assignment.
- Problem 15.72 (chapter 16 reference)
  - (a) trivial 1.
  - (b) 0 since if 1 must be swapped with another element which is greater than 1.
  - (c) choose positions for $k$ ($k-1$)
    then choose the permutation for the rest numbers ($(k-1)!$).
  - (d) as (b,c) implied.
  - This is same as [the reference][everywhere_divergent_generating_functions] "I like counting proofs" paragraph.
    This also uses induction as the alternative method.
    - Also see
      > If you buy that, then the first proof is just the repeated application of this identity.
    - relations
      kw: "either fixes n or does not", .
## 16.2
- > So for the series G.x/ whose coefficients are all equal to 1, the Product Rule implies in a purely formal way that
  This is due to $G(x)$ is one *infinite* series.
  See the derivation of (16.3) where we won't reach $x^n$ forever.
  Also [see](https://math.stackexchange.com/a/4918453/1059606)
- > we could have used this algebraic argument and the Convolution Rule to derive the donut-counting formula.
  "the Convolution Rule" is used to connect the coefficient with "the donut-counting" problem.
- > conversely, they can allow algebraic identities to be derived by counting techniques.
  i.e. the example in 16.2.5.
## 16.3
- Lemma 16.3.1 is said in control theory book which I learned when I was one undergraduate.
  Also for its generalization.
## 16.4
- > So, for example, picking up the whole stack of disks at once and dropping them on another post is illegal.
  i.e. reverse their order.
## 16.5
See [this QA](https://math.stackexchange.com/q/4918436/1059606) for more information. I skipped [1](https://math.stackexchange.com/questions/4918436/why-thinking-about-generating-function-algebraically-doesnt-care-about-converge#comment10504307_4918436), [2](https://math.stackexchange.com/questions/4918436/why-thinking-about-generating-function-algebraically-doesnt-care-about-converge#comment10504316_4918436) (TODO after abstract algebra)
I don't know why [$x>1$ -> Cauchy sequence](https://math.stackexchange.com/questions/4918436/why-thinking-about-generating-function-algebraically-doesnt-care-about-converge#comment10504365_4918436)
- > so H.x/ and F .x/ describe the same, trivial, partial function on the reals
  Here it may mean their properties of "partial function on the reals" since $H(0)\neq F(0)$.
- (16.19)
  - ~~TODO Here should be $n\ge 2$~~
    Here when $n=1$ the coefficient is 0.
  - This is almost same as [everywhere_divergent_generating_functions] (?).
    - > One important step was (4) where we used the identity (2).
      only part of (2).
- > not coordinatewise
  See [this](https://math.stackexchange.com/a/28553/1059606) which means $(G\otimes H)_i$ may depend one $G_k,k<i$ instead of $G_i$.
- > undefined over the real numbers or the ring Zn of Section 9.7.1
  the latter is implied by the division is "defined over the real numbers".
- > how do we justify the kind of manipulation in the previous section to derive the formula (16.19)
  Maybe it means (16.16) where we can cancel infinitely
## chapter 16 problems
- Problem 16.5
  - $a_n=\frac{k(k+1)\cdots(k+n-1)(1-x)^{-(k+n)}}{n!}_{x=0}=\binom{n+k-1}{n}$
  - Why the book has this problem since it is already said in p741.
- Problem 16.8
  - See 16.8.md.
- Problems 16.14, 16.15, 16.18, and 16.19
  - I skipped them since the theorem is THEOREM 6 in DMIA 8.2 which already has many exercises.
    This is also probably learnt in calculus. [See comparison of Thomas’ Calculus](https://www.physicsforums.com/threads/understanding-the-different-versions-of-thomas-calculus-12th-ed-textbooks.544722/) although I read that as one reference instead of the textbook.
    - Although they don't use generating function method.
  - The former 2 has more complex contexts than the latter 2.
- Problem 16.25
  - only if
    By definition of $\otimes$, we have $g_0+h_0=1$.
    if $g_0=0$, then $h_0=1$
    then $g_1=0$. Then similarly we have $g_ih_0=0\Rightarrow g_i=0$
    Then $G=Z$. But $Z$ doesn't have "a multiplicative inverse".
  - if
    we have $h_0=1-g_0$
    Then we have $h_k=\frac{-\sum_{i=1}^{k}g_ih_{k-i}}{g_0}$ which is well-defined.
## Section IV notice
- Notice the following theorems may not hold in Infinite Probability Spaces.
## 17.3*
- > But this intuitive idea is simply false:
  Here the result is based on comparison.
  We have $B\xRightarrow{3+2+0}C\xRightarrow{3+1+1}$
  - We can think it as 3 monsters with 3 ability values.
    When combining these 3 ability values based on comparison instead of directly sum,
    they may have the behavior like "inter inhibition of the five elements".
- TODO [Ron Graham paper](https://mathweb.ucsd.edu/~ronspubs/pre_nontransitive.pdf)
## 17.4
- > For d  n2 =2, the probability of no match turns out to be asymptotically equal to the upper bound (17.7).
  intuitively when $d$ becomes bigger, $\frac{i}{d}\to 0,0\le i\le n-1$.
- TODO [Birthday attack](https://en.wikipedia.org/wiki/Birthday_attack)
## 17.5
- Probability Space [definition](https://en.wikipedia.org/wiki/Probability_space)
  Here "event space" is implied by "sample space".
## chapter 17 problems
seemingly nothing.
## 18.2
- > The conditional probability would then be:
  IMHO not in all problems and then all constructed "conditional probability"s are same as "unconditional probability".
  See this QA
  - deleted comment entries
    - > "insensitive to the probability distribution of where the showrunners put the car ...": This means we can change something like $\Pr[(A,-,-)]$. Temporarily sticking to your calculation, then $\frac34\cdot\frac16\cdot 6$ will change the probability to $\frac34$. Can we understand that this is due to the symmetry? 
      - Yes.
        And $\frac34\cdot\frac16\cdot 6$ is impossible by
        > some of the conditional probabilities shrinking when other conditional probabilities grow.
    - > "assemble the $\frac23$ weighted average a list of different conditional probabilities" may mean we can have something like $\frac13\cdot\frac16+\frac23\cdot\frac16\ldots$ which may be not equal to. But "The only way that a weighted average of six equal numbers" means $\sum\frac23\cdot k_i=\frac23$ when $\sum k_i=1$. Could you say more detailedly about the second and third to last paragraphs?
      - "which may be not equal to." see the last comment entry.
        This is impossible.
## 18.4* (DMIA doesn't give one systematic method for solving with probability problems. Also see 17.2*)
- > which could be written in a form called the Product Rule for conditional probabilities:
  There are many places where "Product Rule" occurs.
- > Well, the probability that the smallest number in the random set is one of the k numbers in S is k=n.
  ~~Here "random set" is size $n$~~
  ~~$k/n$ is based on where we put "the smallest number" if the first $k$ positions correspond to the subset.~~
  Here we first fix one "size-k subset S", then we construct one "randomly chosen set" by choosing elements one by one.
  $k/n$ is because from $n$ numbers only $k$ numbers meet the expected property.
  $k-i/n-i$ because we have chosen $i$ elements.
- See 18.4.3 for what index should be considered.
  > So, if the test is positive, then there is an 84.6% chance that the result is incorrect, even though the test is nearly 95% accurate!
- > The number of healthy individuals is so large that even the mere 5% with false positive results *overwhelm* the number of genuinely positive results from the truly ill.
  This means although $0.05<0.90$ but $0.99>>0.01$ based on their ratio.
  so $0.99\cdot 0.05>>0.01\cdot 0.90$
- "Natural Frequencies" may mean these "Frequencies" are from the real life.
### 18.4.6
This is talking about how we interpret one probability. The following (*) means probability is not allowed.
1. The Prime Number Theorem
2. innocent view by "either prime or it isn’t".
3. "no randomness involved" -> "nonsense". (*)
4. "Bayesian"
  - See [this](https://en.wikipedia.org/wiki/Bayesian_probability)
    - > as a degree of belief in a proposition.
      i.e.
      > In the Bayesian view, *a probability is assigned to a hypothesis*, whereas under frequentist inference, a hypothesis is typically *tested* without being assigned a probability.
      which is also
      > perfectly willing to *assign a probability* to each possibility.
      > since the probability depends on one’s *initial be-liefs*
      > If you’re comfortable using probability to describe your *personal belief* about primality after such an experiment, you are being a Bayesian. A frequentist would *not assign a probability* to N ’s primality, but they would also be happy to bet on primality with tremendous confidence
5. repeatable processes (*)
6. "probabilistic primality test".
- > The Prime Number Theorem implies that only about 1 in 5 million numbers in this range are prime, so you might say that the probability is about 2  10 8
  - [5 million](https://www.wolframalpha.com/input?i2d=true&i=Log%5BPower%5B2%2C6972607%5D-1%5D)
  - Here should be $2\cdot 10^{-7}$
- > As an aside, it is not clear whether Bayes himself was Bayesian in this sense.
  TODO Maybe it means Bayes doesn't care about the *sequence* of conditions but [just one](https://en.wikipedia.org/wiki/Bayesian_probability#History)
  > then Bayesianism provides a convincing framework for updating your beliefs as *further information* emerges.
- > If a number N is composite, there is at least a 3=4 chance that the test will discover this.
  maybe Volker Strassen's test.
- > If you’re comfortable using probability to describe your personal belief about primality after such an experiment, you are being a Bayesian.
  See [this](https://en.wikipedia.org/wiki/Bayesian_probability)
- > the real world conclusions Bayesians and Fre-quentists reach from probabilities are pretty much the same
  TODO proof.
## 18.6
- > Since we don’t think the parity of a date is a cause for the outcome of an admission decision, we would most likely *dismiss* the “coincidence” that on *both* odd and even dates, women are *more frequently* admit-ted.
  > We interpreted the same numbers differently based on our implicit causal beliefs, specifically that departments matter and date parity *does not*.
  ~~i.e. the people are *uniformly* distributed in these 2 cases.~~
  Here maybe Simpson's paradox still occurs. But we won't care about one probability comparison result (i.e. based on date parity). So we will only care about one type of comparison.
  - > It is circular to claim that the data corroborated our beliefs that there is or is not discrimination.
    i.e. we assume the classification will show the trend (like "department" classification). So we will inspect the results (one direction: belief that trend is shown by the results -> we research the result.)
    Then the result may show the trend (the other direction: research -> verify the belief)
    - > never assume that correlation implies causation.
      So the other direction: correlation implies causation
      one direction: causation make us check the correlation.
## 18.7
- > The opposite is true
  i.e. "disjoint events are" not "independent" except for trivial case "one of them has probability zero" included in Definition 18.7.1 $\Pr[A]=0$ "An event with probability 0 ...".
## 18.9
1. 18.9.3,4 I only read the context of "fact" and "" each and related contents with these contexts.
2. The example in 18.9.2 shows that "conditional probability" has not much relation with "confidence".
   The confidence is used when calculating "Bayes-factor".
  > The 99% confidence level is not nearly high enough to overcome the relatively tiny probability of having TB.
  i.e. $100<<1/(1/9999)$.
3. TODO polling
4. confidence is normally [related with confidence interval](https://math.stackexchange.com/a/4605539/1059606)
  - As [this](https://math.stackexchange.com/a/1967239/1059606) says which is almost same as 18.4.6.
    > the frequentist *"long run"* approach to probability is in potential conflict with a naive interpretation of the interval. ... Either μ  lies in the interval *or it doesn't*. There is no "probability" about it.
    - I skipped "interval estimates" and [joshphysics's comment](https://math.stackexchange.com/questions/1966211/probability-vs-confidence#comment5628450_1967239) to insist on using probability.
      > Re: the third to last paragraph discussing the terms "confidence" v. "probability". To render it kosher to discuss the "95% coverage" in terms of probability instead of confidence, is it possible to consider, for a given sample size, the space of all possible confidence intervals one could compute (resulting from the set of all possible samples of the given size) and then put an appropriate probability measure on that space such that the measure of the subspace consisting of CI's that cover μ is 95%?
    - TODO what does 3rd to 4th paragraphs mean in [this](https://math.stackexchange.com/a/4605539/1059606)?
    - IMHO the *mere [johngreen's comment](https://math.stackexchange.com/questions/1966211/probability-vs-confidence#comment9029338_1967239)* doesn't sum up well.
      > "The process by which the interval is derived leads to coverage in 95% of cases over the long run.". That sums up the explanation pretty well. Thank you!
      because it doesn't even say about the differences between probability and confidence.
    - I read only the context of "freq", "conf" in this answer.
  - The above link used here:
    we can interpret "the test result is correct" is *either true or false*. So we use confidence.
  - The above link is also implied by
    > If we stick to confidence rather than probability, we don’t need to make any Bayesian *assumptions about the probability* of a fair coin being chosen.
    in preface of 20
    > how much con-fidence we should have that *our estimate is OK*
    in 20.4.3
    > what’s objectionable about this statement is that it talks about the probability or “chance” that a real world fact is true
    > being unknown does not make this quantity a ran-dom variable
- > So the either-or of Corollary 18.9.1 is really an either-or between some-thing happening that is extremely unlikely—having TB—and something that is only very unlikely—the diagnosis being wrong.
  ~~TODO their sum may be not 1.~~
  See 20.4.3 the above is one rephrase of confidence based on "If you test positive" which translate "test result is correct" to "you have TB".
  > how seriously to take a positive diagnosis
  i.e. think the diagnosis is right.
- > We have figured out that if a random person tests positive for TB, the probability they have TB is about 1/100.
  more specifically, if odds is 1/100, then probability is $(1/100)/(1+1/100)=1/101$.
- See 18.4.6
  - > but that does not mean it has some probability of being true. It is *either true or false*, we just don’t know which.
  - > or how serious he thinks the consequences of a mistaken diagnosis would be.
    Here it is a bit *subjective* and the doctor may become conservative if "the consequences" are "serious".
  - > we don’t need to make any Bayesian *assumptions about the probability* of a fair coin being chosen.
## chapter 18 problems
- Problem 18.1
  - (a) trivial $\cap_{i=1}^{n-1}E_i$.
  - (b) 
    ~~$\text{Pr}[\cap_{i=1}^{n}E_i]=\text{Pr}[E_1]\text{Pr}[\cap_{i=2}^{n}E_i\vert E_1]$~~
    Let $K=\cap_{i=1}^{n}E_i$
    Then $\text{Pr}[K\cap E_{n+1}]=\text{Pr}[K]\text{Pr}[E_{n+1}\vert K]$
    Then substitute the induction hypothesis formula for $\text{Pr}[K]$, we are done.
- Problems 18.3 and 18.4
  - 18.3
    - See the preface of 18.5
      Then we "splitting into cases" of size $n$
      Then use "the Sum Rule" due to "disjoint" and "whole".
      - This is based on $A=\bigcup(A \cap E_i)$
  - 18.4
    - just change the denominator.
- Problem 18.14
  - > This is easy to verify by plugging in the Definition 18.2.1 of conditional probabil-ity.
    See $C$ as the whole set.
    And divide by $\text{Pr}[C]$.
  - (a)
    Use Sum Rule, $\sum_{w\in B}\text{Pr}[w]=\text{Pr}[B]$
  - (b)
    $LHS=\sum_{w\in A}\text{Pr}_B[w]=\sum_{w\in A\cap B}\text{Pr}[w]/\text{Pr}[B]=RHS$
  - (c)
    i.e. to prove $\text{Pr}_B[C\cup D]\ldots$
    Then use "disjoint" which still holds when in the domain of $B$.
## 19.1
- TODO after real analysis [measurable function](https://en.wikipedia.org/wiki/Random_variable#Definition) in definition.
- > an nth bet is 2 n
  It should be $2^{-n+1}$.
## 19.3
- Figure 19.3 
  Here $L/n$ is due to "half-integers" choices which can be bijective with $n\in\mathbb{Z}\cap [0..n]$.
- [Las Vegas standards](https://en.wikipedia.org/wiki/Las_Vegas_algorithm)?
- > called quicksort, uses random numbers
  [pivot](https://en.wikipedia.org/wiki/Quicksort#Algorithm)
- TODO after algorithm Exponential backoff
## 19.4
Great ~~may mean the *useful linearity* property.~~ ~~may mean many types of Expectation?~~ may mean bigger due to countable infinite implied in Theorem 19.4.4.?
- Theorem 19.4.3
  Here $[R=x]$ one event which is one *set* of outcomes.
- TODO after real analysis [proof of Theorem 19.4.4][rearrangement_absolutely_convergent_series]
- "How to Win the Lottery" doesn't show one precise strategy but shows one possibility that "if he won, he’d likely get the whole pot" which is excluded in Figure 19.7.
  > Most lotteries now offer randomized tickets to help smooth out the distribution of selected se-quences.
  maybe force the overall distribution which doesn't allow artificial intervention.
## 19.5
- Theorem 19.5.1 Here we need to care about the infinite case where "rearranging terms" may not work.
  See Theorem 19.5.5.
  So here assume each $R_i$ must be finite so that Theorem 19.5.1 doesn't have the infinite case although ["Infinite Probability Spaces" / Sample spaces](https://www.statlect.com/glossary/sample-space#:~:text=and%20so%20on.-,Infinite%20sample%20space,a%20certain%20condition%20is%20met.) are possible (See 17.5.4).
  - By (19.2) it assumes "nonnegative" so that we can use Theorem 19.4.4.
  - TODO see [this](https://math.stackexchange.com/q/4920518/1059606)
- Theorem 19.5.4 is the  generalization of (19.10).
- > We leave it to the reader to verify that, under the given convergence hypothesis, all the sums in the following derivation are absolutely convergent, which justifies rearranging them as follows
  This is by [rearrangement_absolutely_convergent_series].
- ~~IMHO 19.5.6 may be wrong due to here maybe infinitely green.~~
## 19.6
Great mean bigger in number quantity.
- Simialr to Theorem 19.5.5, Theorem 19.4.6 (Law of Total Expectation) depends on "exchange order of summation", so it may not work for infinite series.
  ~~So 19.6.1 formula may not work.~~
  But here $r$ must be positive, so that is fine.
  Compared with 19.5.7 where $B_n$ may be negative to mean "lose".
## chapter 19 problems
- Problem 19.1
  - only if: trivial
    based on 19.2 paragraph 1, we have $[I_A=1]$ and $[I_B=1]$ are independent.
    Then $A$ and $B$ are independent.
  - if:
    we need to prove $\overline{A}$ and $B$ are independent.
    We already have $\Pr[A\cap B]=\Pr[A]\cdot \Pr[B]$ based on (18.5).
    Then $\Pr[\overline{A}\cap B]=\Pr[B]-\Pr[A\cap B]=(1-\Pr[A])\cdot\Pr[B]=\Pr[\overline{A}]\cdot\Pr[B]$
    The other 2 cases are similar.
- Problem 19.2 (chapter 20 reference)
  - (a)
    - > R takes whatever value S happens to have
      i.e. suppose $S$ takes $s\in V$, then $R$ also takes that *among all $|V|$ values*.
      So $\frac{1}{|V|}$.
    - following the hint,
      $\Pr[R=S]=\sum_{b\in V}\Pr[R=b]\Pr[S=b]$ by "disjoint" and "independent"
      then it equals $\frac{1}{|V|}\sum_{b\in V}\Pr[S=b]=\frac{1}{|V|}$.
      - Here $\sum_{b\in V}\Pr[S=b]$ implies we don't care what value $S$ is.
  - (b)
    - The argument means $\Pr[R=S\mid S=T]=\Pr[R=S]$ where LHS even doesn't care about whether $S=T$.
      > equals *the first coordinate* of whatever value S  T happens to have
    - Similar to proof of (a), 
      strict proof: we only need to change $\sum_{b\in V}\Pr[S=b]$ to $\sum_{b\in V}\Pr[S\times T=(b,b)]\overbrace{=}^{S=T}1$ because $R$ is independent of S  T but may not be for $S$. Then the rest is same.
    - If using $\Pr[R=S,S=T]=\Pr[R=S]\Pr[S=T]$
      then $LHS=\frac{1}{|V|}\sum_{b\in V}\Pr[S\times T=(b,b)]=\frac{1}{|V|}\Pr[S=T]=RHS$
  - (c)
    1. $\Pr[R=a,S\times T=(b,c)]=\frac{1}{6}=\frac{1}{2}\cdot\frac{1}{3}=\Pr[R=a]\cdot\Pr[S\times T=(b,c)]$
    2. TODO maybe (b) is "iff"?
      $\Pr[R=S=T]=\frac{1}{6}$
      $\Pr[R=S]=\frac{1}{3}$
      $\Pr[S=T]=\frac{1}{3}$
    3. similar to 2, we just calculate and each have $\frac{1}{|V|}$.
  - relation with 20.3.5
    Here $R$ is the probability for birthday which is trivially *uniform*. And "R is independent of S  T" trivially because one person's birthday must be independent from others.
    Then we can use (b) to prove "pairwise independent".
- Problem 19.36
  - $\forall a,b, \Pr[f(R)=a,g(S)=b]=\sum_{i,j}\Pr[R=r_i,S=s_j]=\sum_{i,j}\Pr[R=r_i]\Pr[S=s_j]=\sum_{i}\Pr[R=r_i]\sum_{j}\Pr[S=s_j]=\Pr[f(R)=a]\Pr[g(S)=b]$
  - > Lemmas 19.2.1 and 19.2.2 both extend straightforwardly to k-way independent variables.
    19.2.2 is trivial because that is changing the sum terms.
    19.2.1 is based on $\Pr[\overline{A}\cap (B\cap C)]\Pr[\overline{A}]\cdot \Pr[B\cap C]=\ldots$. The rest is probably similar.
- Exercise 19.31 (This is the 1st occurence using "Exercise" for "Problem")
  - (a) $LHS=xEx'_{x}=\ldots=RHS$
  - (b) trivial by substituting $x$ with $p$, etc.
- Problem 19.29
  - Weird the solution is already there.
## 20.1
### preface
- in summary, the 2rd paragraph says we need "confidence" to measure how correct is our *sampling* and the 3rd says application.
### main part
- > Then of course ExŒRç D1,
  Since $n\cdot \frac{1}{n}=1$
## 20.2
- Lemma 20.2.1 proof
  This is due to $x^z I_x\le |R|^{z}$, the rest is similar to Theorem 20.1.1 proof.
- > Now we see explicitly how the “likely” values of R are clustered in an O.R/-sized region around ExŒRç
  Here $g=O(\sigma_R)$ corresponds to $\limsup$ which then corresponds to $\ge c\sigma_R$ because although it may oscillate but $< c\sigma_R$ *keeps in the range* of $\sigma_R\cdot\limsup \frac{g}{\sigma_R}$.
- "The IQ Example" is based on
  > But let’s observe an additional fact (which may be true): *no* MIT student has an IQ *less than 100*.
## 20.3
- 20.3.2
  - Here $Ex[(C+1)^2]$ is same as 19.4.6.
- Theorem 20.3.5 can be done with one step $\text{Ex}[((R+b)-\text{Ex}[(R+b)])^2]=\text{Ex}[(R-\text{Ex}[R])^2]$.
- Notice $R$ in (20.11) is different from $R$ in (20.10) after replacement.
- > Bi D Bj , namely, 1=d .
  See Problem 19.2.
## 20.4
- (20.20) is based on $\text{Ex}[\frac{S_n}{n}]=p$.
- TODO [this difference](https://en.wikipedia.org/wiki/Law_of_large_numbers#Differences_between_the_weak_law_and_the_strong_law) is different from [this](https://bitbucket.org/anom_mony/graduate_entrance_exam_simplified/src/4c6a0d7d21c9f78af8f037fde20b271f90dfe88a/textbooks/review/b_probability%20theory/README.md?at=master#README.md-117) where strong can be based on different distributions for $X_n$.
  Maybe strong is more about "convergence".
- "our estimation procedure" can be one random variable which is different from "voter preference" proportion.
## 20.5
### 20.5.7
- > By considering the random variable n T , we can also use the Chernoff Bound to prove that the probability that T is much lower than ExŒT  is also exponentially small.
  $\Pr[n-T\ge c\text{Ex}[n-T]]$
  trivially $n-T\ge 0$
  so again we need $c$ to be great
  then we have 
  $$
  \begin{align*}
    n-T\ge c(n-\text{Ex}[T])&\Rightarrow (1-c)n+c\text{Ex}[T]\ge T\\
                            &\Rightarrow \frac{\text{Ex}[T]}{T}\ge \frac{T+(c-1)n}{cT}=\frac{1}{c}+(1-\frac{1}{c}\frac{n}{T})\\
  \end{align*}
  $$
  So when $c$ becomes bigger RHS becomes $\frac{n}{T}$ which may be *one great value*. TODO
  Then its corresponding probability is $e^{-(c\ln(c)-c+1)\text{Ex}[n-T]}$ which is small.
- > that the probability that there is no winner is less than e 10 < 1=22000.
  It should be $e^{-1k}$.
## chapter 20 problems
- Problem 20.3
  - (a) same as 20.1.2 example
    $\Pr[R-b\ge x-b]\le \frac{Ex[R]-b}{x}<\frac{Ex[R]}{x}$
  - (b) the greatest lower bound.
- Problem 20.19
  - reasons for Hint is same as Theorem 20.3.7
  - Similarly we have $\text{Ex}[(\sum_{i=1}^n R_i)^2]=\text{Ex}[\sum_{i=1}^n R_i^2+2\sum_{i\neq j,i,j=1\sim n}2R_iR_j]$.
    Then due to "pairwise independent", it equals $\text{Ex}[\sum_{i=1}^n R_i^2]=\sum_{i=1}^n\text{Ex}[R_i^2]=\sum_{i=1}^n\text{Var}[R_i]$.
## 21.1
As 21.1 preface says, here "walk" is just one interpretation which doesn't help analysing the process. So without "walk", all is fine with few changes.
- intuition why expection is zero See 
  > Bankruptcy costs him $1M, while when he wins, he wins only $100. The gambler’s average win remains zero dollars, which is what you’d expect when making fair bets.
  - strict proof
    See
    > The expected payoff of Albert’s first bet is worth
    Here it includes the normal case $p=q,r=1$
    - Then it uses 2 methods to calculate the expection
    - In summary it is based on
      > Pascal’s ingenious idea was to alter the worth of the chips to make the game *fair regardless of p*.
- (21.6)
  - > but there’s no harm in using (21.5) to define wnC1 for all n C 1 > 1
    because we only cares about $T$ terms in this sequence where all later terms can be arbitrary values.
  - 
    $$
    \begin{align*}
      rx^2W(x)=rw_0x^2+\ldots\\
      -\frac{x}{p}W(x)=-\frac{1}{p}w_1x^2+\ldots\\
      (rx^2-\frac{x}{p})W(x)=-w_2x^2-\ldots\qquad\text{This is due to the infinite series where we don't care about convergence}\\
      (rx^2-\frac{x}{p}+1)W(x)=w_1x
    \end{align*}
    $$
- > so his expected capital is n k.1 2p/
  by [linearity][linearity_of_expection_Infinite_Probability_Space]
- > 2p/. But from the formula (20.14), the binomial distribution has a standard deviation of only p kp.1
  Here expection is not $p$ in one standard binomial distribution but $p-q$.
  So following Lemma 20.3.1, $(p+q)-(p-q)^2=1-(p-q)^2$.
  - (20.14) is based on indicator variables
    but here [Probability mass function](https://en.wikipedia.org/wiki/Binomial_distribution)
    we have mean be $k(2p-1)$ but not $kp$.
    (Ignore this line) But the shape ~~is still like bell~~ because we can do as standard to calculate $p^kq^t$ probability and then have the ~~bijective~~ map to the "win".
  - See [this](https://math.stackexchange.com/a/163221/1059606) for the relation between "expected capital" and "binomial distribution" got from [the in-site search](https://math.stackexchange.com/search?q=gambler+binomial+distribution+lose).
    - Let "expected capital" be $M$
      then $M=n+X$ which keeps variance.
      Then $W\sim B(k,p)$ here.
      Then $D(X)=4D(W)$
      So the "standard deviation" is $2\sqrt{kp(1-p)}$
    - $\Theta(\sqrt{k})$ is got from the limit without using $\limsup$.
    - > In our study of binomial tails, we saw that this was extremely unlikely.
      By [this image](http://mlwiki.org/index.php/Binomial_Proportion_Confidence_Intervals) when $\Theta(\sqrt{k})=1.96D(X)=1.96\cdot 2\sqrt{kp(1-p)}$, the probability will be already small.
  - I skips [this variant](https://math.stackexchange.com/q/3108698/1059606) because here $\alpha$ is fixed as $\frac{1}{W_n}$ when we have $W_n$ money.
- Lemma 21.1.4
  - > must be at least as large as the probability that he loses when he has a target T > n.
    the former trivially has all cases in the latter.
    And the former also has the case like one may win $T+k,k\ge 0$ at most, but loses at last. Here the latter will win.
  - > Hence, the probability of his losing while playing without any target has a lower bound arbitrarily close to 1, which means it must in fact be 1.
    This is similar to prove $0.\dot{9}=1$.
## 21.2
I read almost all contents here because it is one real example.
- > vote early, vote often,
  here maybe only the latter where the former may cause the latter.
- (21.13) only considers one edge instead of one possibly lone walk.
- Definition 21.2.1 is same as [this](https://brilliant.org/wiki/stationary-distributions/) where at each step the whole state keeps.
  This is also implied in (21.15) where LHS corresponds to $\pi$.
  - > because the remaining constraints (21.15) could be satisfied by letting Rank.x/ WWD 0 for all x, which is useless.
    This implies matrix $P$ may be not full rank.
## chapter 21 problems
- Problem 21.2
  - > Let r be the probability that starting with n > 0 dollars, the gambler’s stake ever gets reduced to n 1 dollars
    Here assumes $r$ is independent from $n$ which is trivial based on the game facts.
  - (a) either directly $n-1$ or $n\to n+1\to n-1$
  - (b) $p=\frac{1}{1+r}\le \frac{1}{2}\Rightarrow r\ge 1$
  - (c) by (b), we have $r=1$, so "the gambler" must lose money one by one until zero.
  - (d) almost same as (a)
    - I skipped the different methods to prove [1](https://math.stackexchange.com/q/1586693/1059606) [2](https://math.stackexchange.com/q/4281073/1059606) [3](https://math.stackexchange.com/a/2154228/1059606)
      - [This](https://math.stackexchange.com/q/4319973/1059606) seems to care about *whether it is meaningful* to continue playing instead of the possibility to play forever.
    - [Proof](https://math.stackexchange.com/a/3856428/1059606) when $p>\frac{1}{2}$ similar to here.
      Here I skips the proof of "the correct solution is the minimal one".
      - This corresponds to
        > To illus-trate a situation where you really needn’t worry, think about mean time to failure with a really tiny probability of failure in any given second—say 10 100 .
        - > even though you will eventually fail with probability one.
          ~~is implied by $p_{1\to 0}$ where although we must go to infinity but we ~~
          This should not use probability. If use that, then by [Gambler's fallacy](https://en.wikipedia.org/wiki/Gambler%27s_fallacy#Coin_toss), the probability should keep $10^{-100}$.
          In real life, "mean time to failure" should be one dynamic value when using one object keeping aging.
  - > So infinite expected time is not much consolation to a Gambler who goes broke quickly with high prob-ability.
    This is same as [P.s.](https://math.stackexchange.com/q/4921154/1059606)
- Problem 21.12
  - (a) If $D=V$ then $\gamma=1$ to ensure $\sum d_1(x)=\sum d_2(x)=1$. This is impossible.
    Then $V-D$ and $D$ are 2 disjoint connected components
    "strongly connected" implies there is one edge between them which is $\langle y\to z\rangle$.
  - (b) 
- Problem 21.8
  - (a) due to the sum is 1, we have
    $$
    \Pr[x]=\Pr[y]\cdot 1\\
    \Pr[x]+\Pr[y]=1\\
    \text{So}\\
    \Pr[x]=\Pr[y]=\frac{1}{2}
    $$
  - (b) Assume $\text{Rank}(x)\neq \text{Rank}(y)$
    then they will keep swap without becoming $\frac{1}{2}$.
  - (c) 
    ```python
    import numpy as np
    from numpy.linalg import eig
    a = np.array([[0, 0.9],
                  [1, 0.1]])
    w,v=eig(a)
    print('E-value:', w)
    print('E-vector', v)
    a@ np.array([[v[0][1]],[v[1][1]]])
    Out[14]: 
    array([[-0.66896473],
           [-0.74329415]])
    
    from sympy import solve
    from sympy.abc import x, y, z, w
    solve([w+0.1*z-z, 0.9*z-w], w, z, dict=True)
    Out[2]: [{w: 0.9*z}]
    ```
    So we have $z=\frac{10}{19}$
  - (d)
    ```python
    import numpy as np
    from numpy.linalg import eig
    from fractions import Fraction
    a = np.array([[0, 0.9],
                  [1, 0.1]])
    init_state=np.array([[0.99],[0.01]])
    n=100
    state=init_state
    for i in range(n):
      state=a@ state
      if abs(state[0]/state[1]-0.9)<1e-4:
        break
      print(i,state,state[0]/state[1])
    ```
  - (e)
    ```python
    from sympy import solve
    from sympy.abc import a,b,c,d
    solve([a-a-1/2*b,b-1/2*c,c-1/2*b,d-d-1/2*c], a,b,c,d, dict=True)
    Out[1]: [{b: 0.0, c: 0.0}]
    ```
    So (a,d) can be arbitrary values meeting $a+d=1\land a,d>0$
  - (f)
    0 because $b\to \frac{1}{2}c\to \frac{1}{4}b\ldots$
  - (g)
    See Math-for-CS-solutions sol.
    The rest is almost same as the above.
## 22 preface
- > such as enumeration of structures and analysis of random processes.
  See 21.1.2 and 16
## 22.2
- > Step 3: Write Tn Using Early Terms with Known Values
  assume $k\in\mathbb{N}$.
## 22.3
- > The sizes of the spiral patterns on the face of a sunflower grow in proportion to Fibonacci numbers.
  See [this 0:55](https://www.youtube.com/watch?v=z9d1mxgZ0ag) and golden angle at 1:44.
- > The input values on which Euclid’s gcd algorithm requires the greatest num-ber of steps are consecutive Fibonacci numbers
  See Problem 9.14.
- > If r is a repeated root with multiplicity k
  This is proved in DMIA and the calculus textbook probably.
- 22.3.4
  Since it is just one guess I didn't give strict reasons why we guess that way.
## 22.4
- > jThe base case when j = 0 follows from the fact that T (x) = (1) when x 2 [1; x0] (provided that we choose c5 small enough).
  Since "c5 small enough",  we have $\Theta(1)\ge \ldots$.
- Theorem 22.4.1 [proof](./others/mcs/akrabazzi.pdf)
  - Lemma 2 proof
    - here $c_{4,5}$ have more complex forms but the proof is as it says similar.
  - TODO Since $|h_i(x)|= O(x/\log^2 x)\Rightarrow|h_i(x)|=cx/\log^2 x$
  - I skipped p8 "The inductive step is argued as follows: ..."
  - Theorem 2 
    both direction can be more strict by something like $\ge c_5 x^p(1+\int\ldots)$
  - relations with the book "where: ..."
    > nonnega-tive and bounded for 0  x  x0
    corresponds to
    > $T(x)=\Theta(1),1\le x\le x_0$
    1. > x0 is large enough so that T is well-defined,
      $b_i x_0\ge 1$ is to ensure $T(b_i x_0)$ has definition.
      $x0 \ge 1/(1 -b_i)$ is to ensure "prior intervals.".
      The latter can be always achieved when $x_0$ becomes larger.
    2. Same
    3. Same
    4. [See][part_proof_Akra_Bazzi_theorem]
      - Notice $f(x)$ is bounded [can't derive](https://math.stackexchange.com/a/4119457/1059606) $f'(x)$ is bounded. (I only checked the example $\sin(e^x)$ without reading all.)
      - [This title](https://math.stackexchange.com/q/4496012/1059606) is similar but the question seems to be written poorly.
    5. We have $\frac{|h_i(x)|}{x/\log^2 x}\le k\Rightarrow \frac{|h_i(x)|}{x/\log^{1+\epsilon} x}\le k/\log^{1-\epsilon} x,x\ge x_0$
      Then $\exists x_1>x_0, k/\log^{1-\epsilon} x\le 1$ by $\log^{1-\epsilon} x$ is strictly decreasing.
  - Better [not](https://math.stackexchange.com/a/3586870/1059606) to read [the original paper](https://sci-hub.se/10.1023/A:1018373005182)
  - I skipped [this lecture](https://people.mpi-inf.mpg.de/~mehlhorn/DatAlg2008/NewMasterTheorem.pdf) use the above as one reference
- Master Theorem proof see CRLS
  - TODO [use Akra-Bazzi method to prove](https://math.stackexchange.com/q/4749539/1059606)
  - why [3 cases](http://blog.geomblog.org/2014/10/on-master-theorem-vs-akra-bazzi.html)
    > This recurrence represents the "battle" between the two terms involved in a recursive algorithm: the effort involved in dividing (the aT(n/b)) and the effort involved in putting things back together (the f(n)). 
    - TODO what is [A/B](https://sci-hub.se/10.1145/2487241.2487242)
- > We can drop the 1=n term in the last step, because the log n term dominates.
  more strictly, $\lim_{x\to \infty} \frac{\log n+1/n}{\log n}=1$
### 22.4.2
The following is based on
> The Akra-Bazzi formula together with our assertions about boundary conditions and integrality all follow from the Akra-Bazzi Theorem,
- > But notice that Tn D ‚.n log n/ for every value of T1.
  $T_n\le c_2 n \log n$ is trivial since $\log n$ increases faster than the constant.
  $T_n\ge c_1 n \log n$ may let $c_1$ arbitrarily smaller similar to [part_proof_Akra_Bazzi_theorem].
- > For example, the solution to T .n/ D 2T .n=2/ is either ‚.n/ or zero
  This doesn't meet "polynomial-growth condition".
- > Fortunately, the asymptotic solution to a divide and conquer recurrence is un-affected by floors and ceilings.
  because we allow $h_i(x)$ in the Akra–Bazzi method.
  Also see
  > This justifies our earlier claim that applying floor and ceiling operators to the size of a subproblem does not alter the asymptotic solution to a divide-and-conquer recurrence.
### 22.4.3
- > other small adjustments to the sizes of subproblems
  like $h_{1,2}(x)$ which has division and *sum*.
### 22.4.4
Compared with DMIA 8.3 THEOREM 2,
1. if $a<b^d\xRightarrow{b>1} \log_b a<d$. So it corresponds to case 3 $f(n)=\Theta(cn^d)=\Theta(n^d)=O(n^d)$.
  Notice mcs is stricter than DMIA.
  The rest is similar.
2. The book proof in 8.3-exercise 29~33 is one constructive proof for one specific case for $g(n)$.
## 22.5
In summary, the key parts are (See the last paragraph)
1. > This suggests that generating *smaller subproblems* is far more important to al-gorithmic speed than reducing the *additional steps per recursive call*.
2. > Divide-and-conquer recurrences are *also* sensitive to the *number* of subproblems.
3. > How do boundary conditions affect the solution to a recurrence?
  > Boundary conditions matter greatly only when they give the *dominant term a zero coefficient*,
- > Here are some recurrences we solved earlier
  They can be derived using the *exact* solution.
- > Notice that the recurrence equations for Towers of Hanoi and Merge Sort are some-what similar,
  one is $T_{n-1}$ while the other is $T_{n/2}$. So they differ a lot.
- > while divide-and-conquer recurrences (which have small subproblems) usually have solutionsbounded above by a polynomial.
  See Akra–Bazzi method where $x^p$ is polynomial and $g(u)$ is bounded above by one polynomial indicated by $g'(u)$ upper bound. So RHS is polynomial. See [part_proof_Akra_Bazzi_theorem]
- > the Akra-Bazzi formula gives: ...
  - $a<2$ corresponds to case 3
    $$
    \exists\epsilon>0,\log_b(a)+\epsilon<1\\
    \Rightarrow n>n_0,n/n^{\log_b(a)+\epsilon}\ge k\\
    \Rightarrow n=\Omega(n^{\log_b(a)+\epsilon})
    $$
    And $a(n/2-1)<c(n-1)$ is possible due to $a/2<c<1$ is possible.
  - $a=2$ corresponds to case 2 where $k=0$.
    $n-1=\Theta(n)$ is trivial because $\lim (n-1)/n=1$.
  - $a>2$ similar to $a<2$.
- > For linear re-currences, the solution is usually dominated by an exponential whose base is de-termined by the number and size of subproblems.
  "size" correspond to ~~coefficients.~~ $n/b$ in $T(n/b)$.
  > Boundary conditions matter greatly only when they give the dominant term a zero coefficient, which changes the asymptotic solution.
  See p1005 if $f(0)=1,f(1)=\frac{1-\sqrt{5}}{2}$ then we have $s=0$ and then $f(n)=o(1)$.
## chapter 22 problems
seemingly nothing.
## TODO (use the book page number)
- p182
  TODO Maybe I wrote this due to the doubts about
  > viewing a process that might not terminate as computing a partial relation 
# mcs 2018 added/changed based on mcs 2017
## 4.1
- > for example by truth table or algebra
  "algebra" may mean [$\subseteq,\supseteq$](https://math.libretexts.org/Bookshelves/Mathematical_Logic_and_Proof/Book%3A_Mathematical_Reasoning__Writing_and_Proof_(Sundstrom)/05%3A_Set_Theory/5.02%3A_Proving_Set_Relationships#:~:text=this%20text%20first.-,Proving%20Set%20Equality,B%20and%20B%E2%8A%86A.).

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
[union_countable_is_countable]:#union_countable_is_countable

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
[Dedekind_cut_definition]:https://en.wikipedia.org/wiki/Construction_of_the_real_numbers#Construction_by_Dedekind_cuts
[Euler_Phi_multiplicative]:https://en.wikipedia.org/wiki/Euler%27s_totient_function#Phi_is_a_multiplicative_function
[RSA_Euler_theorem]:https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Proof_using_Euler's_theorem
[RSA_Fermat_little_theorem]:https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Proof_using_Fermat's_little_theorem
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
[game_as_decision_tree]:https://math.stackexchange.com/questions/3992275/if-a-winning-strategy-does-not-exist-for-player-2-does-it-exist-for-player-1#comment10457491_3993622
[Identity_Unique]:https://math.stackexchange.com/a/622845/1059606
[coprime_iff_invertible]:https://math.stackexchange.com/a/2326680/1059606
[walk_implies_path]:https://math.stackexchange.com/a/699805/1059606
[rearrangement_absolutely_convergent_series]:https://math.stackexchange.com/q/3734769/1059606
[linearity_of_expection_Infinite_Probability_Space]:https://math.stackexchange.com/questions/4920518/prove-the-formula-for-variance-when-assuming-infinite-probability-spaces#comment10509616_4920518
[part_proof_Akra_Bazzi_theorem]:https://math.stackexchange.com/q/4921759/1059606

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
[plus_math_polyhedron]:https://plus.maths.org/content/eulers-polyhedron-formula

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
[2020_lec_02]:https://lara.epfl.ch/w/_media/fv20/lec03-main2.pdf
[DAG_to_topological_ordering_proof]:http://www.cs.emory.edu/~cheung/Courses/253/Syllabus/Graph/DAG.html
[3_SAT_to_3_Coloring]:https://cgi.csc.liv.ac.uk/~igor/COMP309/3CP.pdf
[Rearranging_Alternating_Harmonic_Series]:https://math.iupui.edu/~ccowen/ButlerAHslides.pdf

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

<!-- GeeksforGeeks -->
[Detect_cycle_Directed_Graph]:https://www.geeksforgeeks.org/detect-cycle-in-a-graph/
[geeksforgeeks_max_f_n1_n2]:https://www.geeksforgeeks.org/turing-machine-to-accept-maximum-of-two-numbers/
[avl_insertion_detailed]:https://www.geeksforgeeks.org/insertion-in-an-avl-tree/
[get_Topological_Sorting_from_DAG]:https://www.geeksforgeeks.org/topological-sorting/

<!-- valuable links -->
[houseofgraphs_search]:https://houseofgraphs.org/result-graphs

[asm_doc]:https://github.com/czg-sci-42ver/csapp3e/blob/master/asm/README.md

<!-- proofwiki -->

<!-- crypto stackexchange -->
[RSA_coprime_guarantee]:https://crypto.stackexchange.com/a/25649
[RSA_proof]:https://crypto.stackexchange.com/a/1006

<!-- Math-for-CS-solutions -->
[sol_20]:./others/mcs/sol/Math-for-CS-solutions/MIT6_042JS15_cp20_solutions.pdf

<!-- mathoverflow -->
[everywhere_divergent_generating_functions]:https://mathoverflow.net/a/45873