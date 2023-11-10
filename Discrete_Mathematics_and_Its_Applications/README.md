check p10 whether the ideas of each chapter are mastered.
# [online resources](https://highered.mheducation.com/sites/125967651x/student_view0/web_resources_guide.html) from [this](https://highered.mheducation.com/sites/125967651x/information_center_view0/)
- Discrete Mathematics and Its Applications [Student’s Solutions Guide](https://www.academia.edu/36410920/Students_Solutions_Guide) pdf with the unavailable version.
- [test bank](https://www.stuvia.com/en-us/doc/2018491/discrete-mathematics-and-its-applications-8th-edition-rosen-test-bank.pdf)
# markdown notice
- "- [ ]" can't be ended with one space.
# TODO
- [QA 164](https://highered.mheducation.com/sites/dl/free/125967651x/1106131/Advice_on_the_Writing_Projects.pdf)
- how is the p20 list related with discrete mathematics?
- [April 1984 issue of Annals of the History of Computing](http://ftp.math.utah.edu/pub/tex/bib/toc/annhistcomput.html#6(2):April/June:1984) relation with John W. Tukey.
- G  ̈odel [impossible](https://en.wikipedia.org/wiki/G%C3%B6del%27s_incompleteness_theorems) to write a computer program that can solve all mathematical problems
- p75 the sign in the middle of the page meaning which is first shown in p59.
- where is "Exercise 11 in Section 4.3 provides a constructive existence proof"?
- p126 just prove the existence by letting the 1st player *follow* the 2rd winning strategy if the 2rd is to win.
  Does it mean do the *same as 2rd 1st step* which seems weird because its strategy is based on the next is 1st player who will change the board?
- p128 $q\to r$ is different from p117 "begging the question" where the latter is to prove $r$ by $r$ and the former is to prove $q$ by $r$.
## number theory
- > Every positive integer is the sum of the squares of four integers
  [proof p5](https://www.math.uchicago.edu/~may/VIGRE/VIGRE2008/REUPapers/Ng.pdf)
- Fermat's last theorem [proof page 111](https://semmedia.mhhe.com/math/Rosen_8e/CHAPTER_1_LINKS.html)
## cs program
- p132
# proof method arsenal by p136
- see 1.7~8
# contents
## prologue
- some highlights are lost due to failure to save.
- data networking [diff](https://www.geeksforgeeks.org/difference-between-network-and-internet/) the Internet
- [formal languages](https://www.oreilly.com/radar/formal-informal-languages/) are more stuctured where [DALL-E](https://en.wikipedia.org/wiki/DALL-E#:~:text=The%20original%20DALL%C2%B7E%20was,3%20modified%20to%20generate%20images.) talks to the person.
  > the language you need to know to talk to DALL-E. Right now, it’s an informal language, not a formal language with a specification in *BNF* or some other metalanguage.
  BNF adds [much limitation](https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_form).
## 1
### 1.1
- [Atomic propositions p2](https://www.cs.cmu.edu/~emc/15414-f12/lecture/propositional_logic.pdf)
- [logic](https://web.archive.org/web/20071218193638/https://www.utm.edu/research/iep/a/aristotl.htm#H5)
  > The heart of Aristotle's logic is the syllogism, the classic example of which is as follows
- "p only if q" means only if q is true, p can be true.
- compare TABLE 5 and TABLE 6, the $p\leftrightarrow q$ changes one `F` to `T`.
### 1.2
### 1.3
- p54
  $p\to q\equiv \neg p \vee q$ because they are both 3 false and 1 true property.
- p57
  $Q_4$ implies all [anti-diagonals](https://www.geeksforgeeks.org/return-an-array-of-anti-diagonals-of-given-nn-square-matrix/)
- p59
  - the duplicate numbers in each row is not taken in account because nine cells must not be duplicated if to assign 1 to 9 into them.
### 1.4
- the philosophy of mathematics -> [Four schools](https://plato.stanford.edu/entries/philosophy-mathematics/).
- p77 similar to $\exists$ ones, why the 1st ~~isn't true for $P(x)=F$~~ uses $\to$ instead of $\wedge$.
  See p75 caution
- [disjunction](https://en.wikipedia.org/wiki/Logical_disjunction) means either one (i.e. disjunction) is true -> true.
  > Because this semantics allows a disjunctive formula to be true when both of its disjuncts are true, it is an *inclusive* interpretation of *disjunction*
  - [Disjunctive syllogism](https://en.wikipedia.org/wiki/Disjunctive_syllogism) based on $\vee$
    while [Hypothetical syllogism](https://en.wikipedia.org/wiki/Hypothetical_syllogism) based on $\to$
### 1.5
### 1.6
### 1.7
- p114
  since $p\to q\equiv (p\wedge \neg q)\to F$
  so *assume* $p=T,\neg q=T$ to result in $F$ then.
  Then $\neg q\to \neg p$ so contradiction -> $F$.
- p115 
  The chain just uses $n$ instead of $n^2-n$ conditional statements.
### 1.8
- [tiling](https://en.wikipedia.org/wiki/Domino_tiling) checkerboards with dominoes
- p122 limits the cases by 2 steps in the "EXAMPLE 5".
  1. to the final digit
  2. to the symmetric property.
- example 14 is one special backward using $\leftrightarrow$.
- p134 FIGURE 7 color line by line which can allow right triominoes cover three colors.
  - here "without loss of generality" is [based on the *same* location after rotation](https://people.math.osu.edu/shapiro.6/tiling.pdf).
    > However if there is a tiling for the board with a *missing upper left* corner, we can turn the picture by a 90 degrees to exhibit a tiling for a board with a *missing upper right* corner. Since that case was *already proved impossible*, the board with a missing upper left corner is also impossible to tile.
### TODO
## 2
### 2.1
- Epistemology [diff](https://qr.ae/pKAULY) logic
  > Epistemology, the study of how we know things and what counts as justification, tells us when we have a *false premise*
  - [Metaphysics](https://en.wikipedia.org/wiki/Metaphysics) -> What is it that exists.
- Venn diagram realtion with logical arguments based on [subsets](https://math.libretexts.org/Courses/Mt._San_Jacinto_College/Ideas_of_Mathematics/03%3A_Set_Theory_and_Logic/3.05%3A_Using_Venn_Diagrams_to_Analyze_Arguments).
- notice "more than once" in p147 EXAMPLE 6 is ~~not same as this~~ [definition of "set"](https://math.stackexchange.com/a/223506) ~~but means~~.
  - TODO can't find when the "are identical" [removed](http://wikipedia.ramselehof.de/wikiblame.php?user_lang=en&lang=en&project=wikipedia&tld=org&article=Set+%28mathematics%29&needle=are+identical&skipversions=0&ignorefirst=0&limit=&offmon=11&offtag=5&offjahr=2023&searchmethod=int&order=asc&binary_search_inverse=on&user=) but at least find the relative time when it still exists.
    tool from [this](https://webapps.stackexchange.com/a/35914)
  - It is now "For example, {2, 4, 6} ..." showing that duplicate is allowed.
### 2.2
- "complement of B with respect to A" means 
  1. based on A, i.e. in A
  2. "complement of B" -> not in B
- superset [definition](https://en.wikipedia.org/wiki/Subset#Definition)
- 2.2.2 TABLE 1
  - just think propositional variables as one special set $\{T,F\}$
  - it is the general case of [Boolean algebra](https://en.wikipedia.org/wiki/Boolean_algebra#Values).
    - See example 10 "De Morgan’s law for propositions" for how this generalization works based on using the property, i.e. [Set-builder](https://en.wikipedia.org/wiki/Set_(mathematics)#Set-builder_notation), as the *proposition* ~~in some way~~.
      then $\notin$ becomes $\bar{A}$, etc, to convert *back* to the set theory.
    - The use the *equivalence of proposition* $\equiv$ to prove the $\leftarrow$ if having proven $\rightarrow$.
  - example 11 just uses the $\equiv$ implicitly.
### 2.3
- p170 function definition implies no one-to-mul and part-to-total/part (i.e. must total-to-...).
  “one-to-one” means not mul-to-one, i.e. if *only use one in the domain*, then *no redundancy* in the *domain*.
  "onto" means no redundancy in the *codomain*, i.e. no total-to-part.
- > A one-to-one correspondence is called invertible
  ~~only needs one-to-one to make "invertible" possible.~~
  - one-by-one due to above p170 definition where $a$ as $f^{-1}$
    image needs to be *unique* for each $b$. -> " more than one such a"
  - onto due to "each element of A" which applying to $f^{-1}$ means "each element of B" in p170
    -> "no such a"
- Stirling's approximation proof
  - [1](#stirling)
  - [2](https://en.wikipedia.org/wiki/Stirling%27s_approximation#Alternative_derivations)
    - [Laplace's method](https://en.wikipedia.org/wiki/Laplace%27s_method#Formal_statement_and_proof) applied for $M=n,f(x)=lnx-x$
      1. $f'(x)=\frac{1}{x}-1,x>0$ so $f(1)=max$ which implies $f''(x)<0$
      - in [this](https://en.wikipedia.org/wiki/Laplace%27s_method#General_theory_of_Laplace's_method), inspired by "Formal statement and proof",
        ${\displaystyle \int _{a}^{b}e^{Mf(x)}\,dx\approx {\sqrt {\frac {2\pi }{M|f''(x_{0})|}}}e^{Mf(x_{0})}{\text{ as }}M\to \infty .}$
        is due to:
        by using $y=\sqrt{M|f''(x_0)|}(x-x_0)$, since 
        $a-x_0\neq 0,b-x_0\neq 0$
        so $\underset{M\to\infin}{\lim}\int_{\sqrt{M|f''(x_0)|}(a-x_0)}^{\sqrt{M|f''(x_0)|}(b-x_0)}\frac{e^{-\frac{y^2}{2}}}{\sqrt{M|f''(x_0)|}}dy=\underset{M\to\infin}{\lim}\int_{-\infin}^{\infin}\frac{e^{-\frac{y^2}{2}}}{\sqrt{M|f''(x_0)|}}dy=\underset{M\to\infin}{\lim}\sqrt{\frac{2\pi}{M|f''(x_0)|}}$
        - the rest is trivial.
      - the bound proof
        is based on 
        1. the limit boundness and continuity, so ${\displaystyle f''(c)\geq f''(x_{0})-\varepsilon .}$ 
          or 
          - ${\displaystyle f''(x_{0})+\varepsilon <0.}$ which then ensures $f(x)\le f(x_0)$ based on $f'(x_0)=0$
            then ${\displaystyle |x-x_{0}|\geq \delta ,f''(x_{0})<0}\Rightarrow{\displaystyle f(x)\leq f(x_{0})-\eta }$
        2. similar to the above inspiration,
          substitute ${\displaystyle y={\sqrt {n(-f''(x_{0})+\varepsilon )}}(x-x_{0}).}$
        3. the rest is trivial for $a,b\neq\infin$
           1. $\underset{n\to\infin}{\lim}e^{-\eta n}\to 0$ is the dominant item in the limit.
        4. if 
          - > Note that the above proof obviously fails
            - because $b-a=\infin$ which is independent from $n$, so $\underset{n\to\infin}{\lim}(b-a)e^{-\eta n}$ is undetermined.
          - sufficient but *not necessary* assumption ${\displaystyle \int _{a}^{b}e^{nf(x)}\,dx<\infty ,n=1}$
            see above "in [this]"
            - $e^{R+Mf(x_0)}$ is factor, it can be ignored when compared with $\infin$
              then the rest is just $\sqrt{\frac{2\pi}{|f''(x_0)|}}$
            - > but it is enough to demand that the integral is finite for some ${\displaystyle n=N.}$
              
              i.e. use $e^{-(n-N)\eta}\int_{a}^{b}e^{Nf(x)}dx$ where $0*A=0,A=\int_{a}^{b}e^{Nf(x)}\neq\infin$
          - TODO 
            - "the maximum of the function at $x_{0}$ must be a "true" maximum 
            (the number ${\displaystyle \eta >0}$ must exist)"
- see [miscs_ipynb] for related infos about quadrature.
- compared with p173, 
  partial function $\exists a\in A\exists b_1,b_2\in B,f(a)=b_1\wedge (f(a)=b_2\Rightarrow b_1=b_2)$
  total function $\forall a\in A\exists b_1,b_2\in B,f(a)=b_1\wedge (f(a)=b_2\Rightarrow b_1=b_2)$ this is a bit contrary to the definition of the onto function, while the latter doesn't need uniqueness.
- 
#### [stirling]
- Theorem 3.3
  - here assume that $t \ge -\sqrt{n}$ because 
    $t\le -\sqrt{n},f_n=0\Rightarrow e^{-\frac{t^2}{2}}$ is trivial.
  - [dominated convergence theorem](https://en.wikipedia.org/wiki/Dominated_convergence_theorem#Statement)
    needs 2 predicates
    1. the sequence converges pointwise to a function f
    2. dominated by some integrable function
    - TODO Lebesgue integral
      - why $\int_S \limsup_{n\to\infty} |f-f_n|\,d\mu = 0,$
  - TODO
    - how [this](https://en.wikipedia.org/wiki/Stirling%27s_approximation#Derivation) uses trapezoid rule by skipping $lni,i\in[2,n-1]$.
    - how [this](https://faculty.washington.edu/moishe/hanoiex/counting/Stirling.pdf) skips $-log(n+1)$ in $d_n-d_{n+1}$
  - bell curve inflection points [analogy](https://flexbooks.ck12.org/cbook/ck-12-probability-and-statistics-concepts/section/7.5/related/lesson/density-curve-of-the-normal-distribution-adv-pst/#:~:text=The%20points%20at%20which%20the,deviation%20away%20from%20the%20mean.)
### 2.4
- the Lucas sequence [relation](https://en.wikipedia.org/wiki/Lucas_number#Relationship_to_Fibonacci_numbers) with the Fibonacci sequence and other [interesting](https://brilliant.org/wiki/lucas-numbers/#applications-in-nature) properties.
- sphere packing [relation](https://en.wikipedia.org/wiki/Sphere_packing#Other_spaces) with Hamming code
  > with the spheres defined by Hamming distance
  [figure](https://www.myreadingroom.co.in/notes-and-studymaterial/68-dcn/800-hamming-distance.html)
  - [so](https://en.wikipedia.org/wiki/Hamming_distance#Error_detection_and_error_correction) 
    > a code C is said to be k error detecting if, and only if, the minimum Hamming distance between any two of its codewords is *at least k+1*
    means these spheres don't overlap to *differentiate* among them. 
- TODO
  Kissing Problem seems to associate with [traverse problem](https://www3.cs.stonybrook.edu/~bender/newpub/2012-BenderBoCh-fun-kissing.pdf) but this doesn't relate with the [spheres](https://en.wikipedia.org/wiki/Kissing_number#One_dimension)
# miscs links from [this](https://semmedia.mhhe.com/math/Rosen_8e/CHAPTER_1_LINKS.html)
- [atlas](https://web.archive.org/web/20060106014447/http:/www.math.niu.edu:80/~rusin/known-math/index/03-XX.html)
# how I read the information center
- [links](https://semmedia.mhhe.com/math/Rosen_8e/CHAPTER_1_LINKS.html) are too miscellaneous so I skipped them except when I can't understand the book reference point.
- most of [Extra Examples](https://highered.mheducation.com/sites/125967651x/student_view0/extra_examples.html) are similar to book corresponding ones based on chapter 1 observation, so I skipped all of them.
# anecdotes of famous mathematicians, etc
- [John Tukey](https://mathshistory.st-andrews.ac.uk/Biographies/Tukey/)
  > Their educational method was to respond to John's queries by providing clues and asking *further* questions rather than giving a direct answer, a characteristic that John inherited and used throughout his career.
  > John also had the benefit of an excellent *public library* in New Bedford which even possessed *journals* such as the Journal of the American Chemical Society and the Transactions of the American Mathematical Society. He was able therefore to take his education to a high level *before* entering university
# latex miscs
- find symbol codes by [detexify](http://detexify.kirelabs.org/classify.html) from [this](https://tex.stackexchange.com/a/450709)
- align math proof with [comments](https://tex.stackexchange.com/a/47691)
- [qed](https://stackoverflow.com/a/1910526/21294350) [location](https://tex.stackexchange.com/a/34018) to the [default](https://tex.stackexchange.com/a/564722) [end](https://tex.stackexchange.com/a/144984)
- nice [emptyset](https://tex.stackexchange.com/a/22799)
- arrow $\Rightarrow$ is [preferred](https://oeis.org/wiki/List_of_LaTeX_mathematical_symbols) to be separate from $\rightarrow$ used in the conditional statement although [this](https://www.actual.world/resources/tex/doc/Proofs.pdf) doesn't use the former and p173 also use $\to$.
  So in the following exercises, when using the strict abstract propositional logic, I probably still use the $\to$ instead of $\Rightarrow$.
  Also [see](https://math.stackexchange.com/q/711817/1059606)
- text [above](https://tex.stackexchange.com/a/103993) arrow
- when $\begin{aligned}$ is [preferred](https://tex.stackexchange.com/a/95408)
  to $\begin{aligned*}$
- "implies" arrow [location](https://math.stackexchange.com/questions/711817/mathematical-notation-arrow-sign)
- `&` in `\aligned` is to [alternate](https://tex.stackexchange.com/a/159724) between left-aligned and right-aligned, so `&&` will make alternate *again*, becoming the original one.
  for example for the 1st $&$, the *left* of it is *right* aligned and the right of it is left aligned
  but for $&&$, the left is kept *same* and the right is *alternated*.
- newline "\\" must be in the maths mode or something like "\begin{align*}".
- [multiline](https://tex.stackexchange.com/questions/36343/multiline-text-under-over-arrows#comment72468_36343) in xRightarrow using [`substack`](https://tex.stackexchange.com/a/63192)
## katex
- available [packages](https://github.com/KaTeX/KaTeX/wiki/Package-Emulation)
- set latex arrow with [specific length](https://tex.stackexchange.com/questions/269935/arrows-of-arbitrary-length#comment647948_269935) by `\newcommand{\myrightarrow}[1]{{\overset{#1}{\xRightarrow{\hspace{3cm}}}}}`
  - `\makebox` [unavailable](https://tex.stackexchange.com/a/6840)
    Also [`\settowidth`](https://tex.stackexchange.com/a/37294)
    and [`\parbox`](https://tex.stackexchange.com/a/269950)
# QA miscs
- see the self-designed [template](./QA_template/template.md).
- [mathjax](https://math.meta.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference)
- search [help](https://math.stackexchange.com/search)
# Exercises
I only read even ones because [they][SOLUTIONS_8th] have detailed explanation as [7th][SOLUTIONS_7th] and also odd ones are very similar to even ones at least for 1.1 (except for some cases that even ones are a little hard whether having asterisk marks or not).
I also read the asterisked ones.
- I skipped all [assessments](https://highered.mheducation.com/sites/125967651x/student_view0/self_assessments.html) because examples plus exercises are enough.
- I skipped all REVIEW QUESTIONS due to 
  1. not finding valuable answers although [SOLUTIONS_7th] has some tips.
  2. exercises are enough large to help the learning.
- COMPUTER PROJECTS , COMPUTATIONS AND EXPLORATIONS and WRITING PROJECTS are a bit off the topic with the goal to learn the **maths** fundamental knowledge.
## 1
### 1.1
- [x] 
  a,b,d,f not.
- 4~16,
  24~40,46 skipped for it to be a little too unnecessary and trivial.
- see answer for 18
- [ ] a,b true because premise is false.
- [ ] a,b,c -> inclusive or
- [x] 42 assume one pair is different, then can be proved easily.
  if they are all same, it is also easy to prove the equation holds.
- [x] 44 because if not, then one pair of all true will make the statement false.
- [ ] 45 $\underset{i=1}{{\overset{n-1}{\bigvee}}}\underset{j=i+1}{{\overset{n}{\bigvee}}}$
- [ ] 52 yes
- [ ] 53
  a) only one is true
  b) undetermined value
  c) 
  modification after reading the answer
  a) so 99th is true
  b) if "at least n" is true, then true for all $i<=n$ (i.e. n false and $100-n$ true -> $100-n=n$ -> $n=50$)
  c) see b), $99-n=n$ is impossible for $n\in\mathbb{Z}$
### 1.2
- 2,6~8,12 skipped because similar to 10,
  14 just based on keywords
  18 (because not automatic proof, it just traverses all conditions)
  24 (just use the exhaustion method)
  28~35 they are similar to 24,26 and they have little differences among themselves.
- [ ] 4 $d\vee s \to w$
- [ ] 10 yes TFT (maybe true)
- [ ] 19 the 2rd subquestion is to test [whether the man is liar](https://math.stackexchange.com/a/2346364/1059606) based on 1st, [detailed](https://stackoverflow.com/a/34574728/21294350).
  more [intuitive](https://math.stackexchange.com/a/3021648/1059606) where no/yes from whether liar or TRUTHTELLER is *same*.
- [ ] 20
  1. if "yes", then he is liar -> he is not liar based on contrary "yes", i.e. no. (Then contradiction)
    "no" is ~~similar~~.
  2. 
  - Ans
    1. Above is wrong.
    2. similar to 19.
- [ ] 22 TFF
  ~~TODO how~~ “unless” 
  1. means “or.”
  2. `->` based on p30.
  TODO IMHO, should be $p\to q$, i.e. $\neg j\to \neg k$
- [ ] 26 two cases (both knights / both knaves) are possible.
- [ ] 36
  since what Smith said is neutral, so assume he is true.
  if Jones is true, then Williams is wrong.
  - ans
    ~~b) just same as a) because the added statements is obvious.~~
- [ ] 38 can also use $\oplus$
- [ ] 40 also "the exhaustion method".
- [ ] TODO 42 [unavailable](https://web.archive.org/web/20020401000000*/http://mathforum.org/dr.math/problems/joseph8.5.97.html)
  based on [wikipedia](https://en.wikipedia.org/wiki/Zebra_Puzzle#Solution), just step by step solve the problem.
  TODO where is in [Life International](https://books.google.co.jp/books?id=elIEAAAAMBAJ&q=zebra#v=onepage&q=zebra&f=false)
### 1.3
- 2~12,18,
  50~52 are skipped.
  14,16 I only read the 1st one.
  20~37 I only read 20 because they are probably similar.
- [x] 19 $p=T,q=F$
  $p\to q$ is $F$
  then $F\to F$ is true
- [ ] 40 has no referenced symbols.
  TODO
  1. the ans doesn't show the compound proposition, also for the above self answer.
- [ ] 42 TODO why they are held simultaneously.
- [x] 44 obviously by $\wedge$.
- [ ] 46 just based on the meaning of disjunction and conjunctions
  where disjunction allows all possibilities
  and conjunction ensures the needed conditions with one specific possibility.
- [x] 48 the hint has given the answer.
  49 just the opposite step of 48.
- [x] 54
  a. truth table
  b. $\neg (p\downarrow q)\ldots$
  c. based on 49 and the above is enough.
- [x] 55 $\neg(\neg p\downarrow q)$
  then $((p\downarrow p)\downarrow q)\downarrow((p\downarrow p)\downarrow q)$
- [x] 56 same as $\downarrow$
  $p|p=\neg p$
  $(p|q)|(p|q)=\neg (p|q)=p\wedge q$
  - the ans based on $\vee$ is also ok.
- [ ] 58 see the answer.
- [x] 59 $2^4$
- [x] 60 transitivity.
- [x] 62 5
- [x] 64 $\neg F=T; \neg T=F$
- [x] 66
  a($p=T,s=F$),b($p=F=s,q=T$),c($p=T=q=s,r=F$)
- [ ] 68 $Q\bigwedge\underset{i\in odd}{\bigvee}p(i,1)$
  all is not in even -> in one of odd.
- [x] 70 $\underset{i=1}{\overset{9}{\bigwedge}}\underset{j=1}{\overset{9}{\bigwedge}}\underset{n=1}{\overset{9}{\bigvee}}p(i,j,n)$
- [x] 72
  where $r,s$ traverse the 9 blocks
  $n$ ensures each number is assigned
  $i,j$ traverse inside the block
### 1.4
1. [null quantification](https://gateoverflow.in/130504/null-qunatification-rule#:~:text=Null%20Quantification%20mean%20when%20a,in%20part%20of%20a%20statement.) means some statement like $A$ in 48 doesn't have quantified variable like $x$ in 48.
- 2~6,
  12~16,
  22,26,
  28~30(similar to exercises before),
  32~44,54,
  58~64 skipped
- [x] 8
  a. rabbit hops
  b. all animals are rabbits and hops
  c. there is some animals are rabbits and they hop.
  d. there is some animals are rabbits which hop.
- [ ] 10 better with parentheses
  a. $\exists xC(x)\wedge D(x)\wedge F(x)$
  b. $\forall xC(x)\wedge D(x)\wedge F(x)$ wrong ("or")
  c. $\exists xC(x)\wedge \neg D(x)\wedge F(x)$ 
  d. $\neg (\exists xC(x)\wedge D(x)\wedge F(x))$
  e. $\exists xC(x)\vee D(x)\vee F(x)$ This is same as the answer.
- [x] 18
  $\exists \Rightarrow \vee$
  $\forall \Rightarrow \wedge$
  $\neg$ just assign to each predicate
- [x] 20 
  a,b similar to 18
  c~e see the ans is enough.
- [x] 24
  same as the examples,
  $\forall \Rightarrow \to$ to exclude the result as the condition
  $\exists \Rightarrow \wedge$ to include the result as the condition -> b,c,e
- [ ] 46 yes based on 45.
  45 is by definition.
  - 45 ans
    $T/F \to  F$ false because $T\to F$ is false
    $F\to F$ true
  - 46 similar
- [ ] 48 by definition
  a. any ... or ... means any (... or ...)
- [x] 50
  a. only A is T and P(x) is F -> false
    same for the right side, Q.E.D.
- [ ] 52 -> ans
- [ ] 56
  inspired by p57
  at least $\underset{i=1}{\overset{3}{\bigvee}}P(i)$
  at most $\underset{i=1}{\overset{2}{\bigwedge}}\underset{j=i+1}{\overset{3}{\bigwedge}}(\neg P(i)\wedge \neg P(j))$
  - ans just the exhaustion method
### 1.5
- 2~8,
  14~32,
  36~42,46,52(similar to 17) are skipped
- [ ] 10
  PO IMHO here $\rightarrow$ can also be $\leftrightarrow$
- [ ] 12
  j. here chat -> connection is wrong so no $\leftarrow$
  k. maybe here ~~assume~~ self has chatted with self is nonsense. ~~so not chat ~~can't~~ -> $x\neq y$~~
  so $x\neq y$ is just the condition and should be thought as the result, so no $\leftarrow$
- [ ] 17
  d. $\exists x \exists y (x\neq y\wedge\forall z(M(x,z)\wedge M(y,z)))\wedge \forall a(\forall z M(a,z)\to (x=a\vee y=a))$
  - the ans is more elegant.
- [x] 34
  just $1,2$
  and $1,2,3$
- [ ] 44
  also can use methods similar to 17.
- [x] 48 replace $x$ with $y$ and then truth table
- [ ] 49 similar to 48
  a. since $P(x)=T$, so become $\exists xQ(x)$ -> $\exists yQ(y)$
  b. similar to a
- [ ] 50
  a. $\exists x(P(x)\vee Q(x) \vee A)$
  | x   | P(x) | Q(x) |
  | --- | ---- | ---- |
  | x1  | T    | F    |
  | x2  | F    | T    |
  | ... |      |      |

  b. $\exists x \neg(P(x)\vee Q(x))$
  c. see ans.
  $\neg (\exists xP(x)\wedge(\neg \exists xQ(x)))$ ->
  $\neg (\exists xP(x)\wedge(\forall x \neg Q(x)))$ ->
  $\forall x \neg P(x) \vee(\exists x Q(x))$
- [ ] 51
  by 50 and exercises before
  1. connectives are enough for $\neg,\vee$
  2. 50 has includes $\exists,\forall,\to$
  then Q.E.D.
  - The ans proves that 
    1. $QxP(x)$
    2. $\neg P(x)$
    3. $P\vee Q$
    all be transformed into PNF
    Then based on the *order*, just one by one transform is enough.
### 1.6
- 2~6,10,14&16&20(I only read a),30 skipped
  here 12,22 is a little different from the ans but the logic is not wrong IMHO.
- [ ] 8
  can also based on "if x is an island, then x is No man".
  so Hypothetical syllogism
- [ ] 12
  (p ∧ t) →(r ∨ s), q →(u ∧ t), u →p, and ¬s and conclusion q →r
  $q\to u\to p$
  $q\to t$
  so
  $q\to (p ∧ t) \to (r ∨ s)$, since $\neg s$, so $q\to r$
  - see ans better use 11 based on what the exercise says.
- [x] 18 why $S(M,M)$
- [ ] 22
  based on $p\to q\equiv \neg p\vee q$ based on the *unique false* result
  $$
  \newcommand{\myrightarrow}[1]{{\overset{#1}{\xRightarrow{\hspace{7cm}}}}}
  \begin{align*}
  \neg \exists x(Q(x)\wedge  R(x))&\myrightarrow{\neg(T\wedge T)=F\Rightarrow T\to \neg T=F}\forall x(Q(x)\to \neg R(x))\\
  \text{with }\forall x(\neg R(x)\to \neg S(x))&\myrightarrow{\text{Hypothetical syllogism}}\forall x(Q(x)\to \neg S(x))\\
  &\myrightarrow{\begin{align*}\text{only }(T,T),Q(x)\to \neg S(x)=F\\\Rightarrow \text{only }(T,T),\neg Q(x)\vee \neg S(x)=F\end{align*}}\forall x\neg Q(x)\vee \neg S(x)\\
  \text{similarly,} \forall x\neg P(x)\vee S(x)&\\
  \text{then} &\myrightarrow{\text{Resolution}}\forall x\neg P(x)\vee\neg Q(x)\\
  &\myrightarrow{}\forall xP(x)\to \neg Q(x)
  \end{align*}
  $$
- [x] 24 3->4
- [ ] 26 by definition.
- [ ] 28 similar to 26
  *based on any variable* $a$
  then $(\neg(\neg P(a)\wedge Q(a)))\vee R(a)$, i.e. 
  $(P(a)\vee \neg Q(a))\vee R(a)$
  since only one of $Q(a)$ and $\neg Q(a)$ can be true, 
  then either $P(a)$ or $P(a)\vee R(a)$ is true.
  so $P(a)\vee R(a)$, i.e. $\neg R(a)\to P(a)$ is true.
  - The ans takes $\neg R(a)$ as the precise same as one of exercise before.
- [ ] 32
  TODO IMHO how the tautology proved without $p\wedge\neg p\equiv F$
  ~~it is same as to prove $F\vee(p\wedge\neg p)$~~
- [ ] 34
  D(x): x is difficult
  L(x): many students like x
  E(x): x is easy
  1. $D(logic)\vee \neg L(logic)$
  2. $E(mathematics) \to \neg E(logic)$
  a,~~b~~,d, T
  ~~c~~,e F
  - b. ~~-> $\neg D(logic)$, ~~
    ~~but both $T\to T$ and $F\to T$ is possible, so ~~
    $F\to T/F$, so $D(logic)$ is not determined, so nothing can be determined.
  - c same as b.
  - ~~-> $D(logic)$~~
    e $E(mathematics) \to \neg E(logic)$ -> $\neg E(mathematics) \vee \neg E(logic)$
    so the result is always T
    then $F/T \to T$ always holds.
- [x] 35
  p: Superman were able to prevent evil
  q: Superman were willing to prevent evil
  r: Superman would do so
  s: Superman would be malevolent
  t: Superman exists
  u: Superman is impotent

  1. $p\wedge q \to r$
  2. $\neg p \to u$
  3. $\neg q \to s$
  4. $\neg q$
  5. $t \to (\neg u\wedge\neg s)$
  if $t$, then $\neg s$ contray to $\neg q \to s$
  so $\neg t$.
### 1.7
Most of them are similar to proofs in the junior/senior high school.
- 2,4~6&10(similar to 2) skipped
- [ ] 8
  $p\wedge\neg q\to F$
  here $n=a^2,n+2=b^2$
  then $2=(a+b)(a-b)$
  $a+b=2\\ a-b=1$ 
  so $a=\frac{3}{2},b=\frac{1}{2}\Rightarrow a,b\notin \mathbb{Z}$, 
  obviously $F$
  - Also see ans where use the *consecutive* square to prove.
- [ ] 12
  similar to 8
  [irrational numbers latex](https://texblog.org/2007/08/27/number-sets-prime-natural-integer-rational-real-and-complex-in-latex/)
  $\frac{p}{q}*k=\frac{m}{n},k\in \mathbb{I}$
  then $k=\frac{mq}{pn}\in \mathbb{Q}$ (why [Q for rational](https://math.libretexts.org/Bookshelves/Analysis/Real_Analysis_(Boman_and_Rogers)/01%3A_Numbers_-_Real_(%E2%84%9D)_and_Rational_(%E2%84%9A)/1.01%3A_Real_and_Rational_Numbers#:~:text=The%20set%20of%20rational%20numbers%20is%20denoted%20Q%20for%20quotients,Figure%201.1.)) -> contradiction.
  - See ans notice the nonzero to ensure validity of division by $p$.
- [x] 14,34 direct proof.
- [x] 16,18,41 proof by contradiction.
- [ ] 20 
  - [x] a is obvious
  - [ ] b is similar to a essentially.
- [x] 22 trivial proof.
- [ ] 24 see ans
- [x] 26 same as the example.
- [x] 28
  if: by contradiction.
  only if is easy
- [x] 30
  if is easy
  only if: $(m-n)(m+n)=0$
- [x] 32 just use $\equiv$ based on axioms with the $\mathbb{R}$
- [x] 36 (5) is wrong.
- [x] 38 4->1->2->3 chain, then use $\leftrightarrow$ to $3\to4$
  - ans not use chain is also ok
- [x] 40 7 by trying up from 3.
- [ ] 42 see ans
- [x] 44 i -> n is odd -> the rest.
### 1.8
- 2,8,12,24,32~34,42 skipped.
- [x] 4 exhaustion.
- [ ] 6 by definition is faster.
- [ ] 10, 3
  - see ans
- [ ] 14 a bit like one riddle.
- [ ] 16 see the ans.
  I was wrong to prove it is right.
- [ ] 18,20,22 contradiction. 
  - 18 similar to example 13
    - also see the ans.
  - 20 if there is 2 then $r-a<\frac{1}{2},(a+1)-r<\frac{1}{2}\Rightarrow1<1$
  - 22 similar to 20 $\lfloor x\rfloor$ 
    - latex [see](https://oeis.org/wiki/List_of_LaTeX_mathematical_symbols)
- [ ] 27 use one invariant.
- [x] 28 otherwise always all zeros (all ones is impossible)
- [ ] 30 exhaustion and then find the pattern.
- [x] 36
  similar to the example
  $\sqrt[3]{2}=\frac{p}{q},q\neq 0$, then $3\mathrel{|}p,q$
  - symbol [$\mathrel{|}$](https://tex.stackexchange.com/a/116589)
- [ ] 38
- [ ] 39
  a. from sorted one, each swap would decrease.
  b. 
  - ans
    a. "Without loss of generality," because we can swap among all $x_iy_i$ to keep $x_i$ sorted.
      the rest is same as above
    b. as the ans says, changing $y_i$ to the *increasing* order when $x_i$ increases will *increase* the sum, similarly, changing $y_i$ to the *decreasing* order when $x_i$ increases will *decrease* the sum.
- [x] 40 this is one school recruitment interview problem I encountered.
  | time                      | 8   | 5   | 3   |
  | ------------------------- | --- | --- | --- |
  | 0                         | 8   | 0   | 0   |
  | 1                         | 3   | 5   | 0   |
  | 2                         | 3   | 2   | 3   |
  | 3 (skipped one step here) | 6   | 0   | 2   |
  | 4                         | 1   | 5   | 2   |
  | 5                         | 1   | 4   | 3   |

- [x] 44 just all horizontally.
- [ ] 46 white less than black ones because all corners are white.
  - the ans
    1. if 3-8, then with 4-9,10-15,19-20,13-18, they surrounded 14 so contradiction.
    2. then 3-4
      - three vertical -> 17-22, 18-23, and 19-24
        > then we are again quickly forced into a sequence of placements that lead to a contradiction
        i.e. 11-16,7-12 will make 6 surrounded.
      - one vertical
        > Therefore without loss of generality, we can assume that we use 22-23
        either 21-22 or 22-23 which are same due to symmetry.
        > we are stuck once again
        18 was surrounded.
- [ ] 48
  - [x] after "path" hint of the ans
    the circular path is cut by two cells where their distance is *even* due to "a white square and a black square" so dominoes can cover.
- [ ] 50
  - after hint of FIGURE 7
    - the 1st line white mirrors to blue, etc, so not possible.
    - the 2nd only blue is possible after the mirror test, but after anticlockwise 90-degree rotation, it becomes black, so also not possible.
    - the 3rd, only (3,3) possible after both rotation and mirror.
      TODO constructive proof of (3,3).
    - the 4th line similar to the 2nd line.
  - the ans
    1. must remove *white*
    2. the white will be white in all cases after the rotation, etc.
- [ ] 51
  a.
    1. straight
    2. move one square around
      1. 111
           1
      2. 111
          1
    3. move two squares around
      1. 11
         11
      2. 11
        11
  b.
    - straight ones are obvious.
    - by similar coloring with triominoes, 2.1, 2.2 and 3 can't
  - ans
    a. is right
    b. is wrong.
- [ ] 52
  - ans use the same coloring as FIGURE 7
    then
    1. horizontal -> one color each
    2. vertical -> either zero or two squares of each color.
    ~~odd horizontal + even vertical -> ~~
    - > assume without loss of generality that an even number of tiles are placed horizontally
      because rotation will swap horizontal with vertical.
      so "even number of horizontal" assumption is ok.
### Supplementary
Although "generally more difficult" said in p12, but it is not the case, at least for chapter 1.
- 2~8,38(contradiction or contraposition by the ans where they are same in the nature),44 skipped.
- [ ] 10
  1. if $q=T$, then all three is $T$ -> (A,A,A)
  2. $q=F$
     1. $p=T$, 1st is $F$ 
        2rd becomes $\neg r$ -> $T/F$ -> (R,A,R) / (R,R,R)
     2. $p=F$, 1st is $T$
        2rd becomes $F$ -> (A,R,R)
  - the ans seems to be wrong.
- [x] 12 because based on known propositional variables, the assertions $T/F$ are *fixed*.
- [x] 14
  Anita must be knave because if she is knight, then contradiction with "I am a knave".
  so Boris is a knave
  then Carmen is also a knave
- [ ] 16 based on the assumption from the real life that "unicorns do not live".
- [x] 18 F,T
- [ ] 19
  hinted by p58 EXAMPLE 11
  1. 
    $$
    \overset{16}{\underset{i=1}{\bigwedge}}\:\overset{16}{\underset{j=1}{\bigwedge}}\:
    \overset{16}{\underset{n=1}{\bigvee}}\:p(i,j,n)
    $$
  2. 
    $$
    \overset{16}{\underset{j=1}{\bigwedge}}\:\overset{16}{\underset{i=1}{\bigwedge}}\:
    \overset{16}{\underset{n=1}{\bigvee}}\:p(i,j,n)
    $$
  3. 
    $$
    \overset{3}{\underset{r=0}{\bigwedge}}\:\overset{3}{\underset{s=0}{\bigwedge}}\:
    \overset{4}{\underset{i=1}{\bigwedge}}\:\overset{4}{\underset{j=1}{\bigwedge}}\:
    \overset{16}{\underset{n=1}{\bigvee}}\:p(4r+i,4s+j,n)
    $$
  - IMHO either the $n$ or the index $i/j/(i,j)$ can be used for $\bigvee$.
  - latex [Spacing in Math Mode](http://www.emerson.emory.edu/services/latex/latex_119.html)
- [x] 20
  a. $\exists xP(x)$
  b. $\neg\forall xP(x)$
  c. $\forall xQ(x)$
  d. $\forall xP(x)$
  e. $\exists x\neg Q(x)$
- [x] 22 same as one example, i.e. one domain with only two distinct values.
- [ ] 24 ~~$\forall y\\(\forall x_3 G(x_3, y))\to\exists x_1\exists x_2 G(x_1, y)\wedge G(x_2, y)\wedge ((x_3=x_1)\vee(x_3=x_2))\wedge(x_1\neq x_2)$~~
  - (notice "three" instead of "two" hinted by the ans)
    so $\forall y(\forall x_4 G(x_4, y)\to\overset{3}{\underset{i=1}{\exists x_i}}\overset{3}{\underset{i=1}{\bigwedge}} G(x_i, y) \wedge (\overset{3}{\underset{i=1}{\bigvee}}(x_4=x_i))\wedge(x_1\neq x_2\neq x_3))$
  - "No one has more than three" doesn't mean "three" exactly.
- [x] 26 a,b,c T
- [ ] 28 by definition.
- [ ] 30 see 28 ans.
- [x] 32
  a. $p\wedge\neg q$, so "it snows today, and I won't go skiing tomorrow"
  b. "not ..." $\exists x\neg F(x)$
  c. "all ... like ..."
  d. $\neg x\forall y\neg F(x,y)$
    i.e. "In one mathematics class all students don't fall asleep during lectures"
- [ ] 34
  hinted by the ans, use two variables to represent "in *which* *every* room"
  $\exists x\exists y\forall zB(x,y)\wedge W(x,z)$
  $B(x,y)$ means "There is x on the campus of y in the United States"
  $W(x,z)$ means "z in x is painted white"
  - the ans splits $W(,)$.
    better move $\forall z$ after $\wedge$ to be based on $x$ instead of general.
- [ ] 36 this is duplicate of one exercise before.
  $\exists x\exists y(P(x)\wedge P(y)\wedge(x\neq y)\wedge(\forall z P(z)\to(z=x\vee z=y)))$
- [ ] 40 suppose two, then contradiction.
- [ ] 42
- [x] 46 $5+2\sqrt{6}$ is not a perfect square 
  -> $\sqrt{5+2\sqrt{6}}=\sqrt{2}+\sqrt{3}$ is irrational
## 2
### 2.1
- 2~6,10,14~18,22,34~38,46 skipped
- [ ] 8 notice self.
- [ ] 20
  $A=\{\varnothing\},B=\{\varnothing,\{\varnothing\}\}$
  - a little complex
- [ ] 24 by having the same singleton sets.
- [x] 26 a,b,d are.
  - a should be $\{\varnothing\}$
- [x] 28 
  $$
  \forall a\in A\to a\in C\\
  \forall b\in B\to b\in D\\
  then\\
  \forall (a,b)\in A\times B\to (a,b)\in C\times D
  $$
- [x] 30 courses taught by each professor.
- [ ] 32 $A=\varnothing;B=\varnothing$
  - should be "or"
- [ ] 40
  i.e. since nonempty for $A,B$ (hinted by the ans)
  $\exists a (a\in A\wedge a\notin B)\exists b\in B((a,b)\in A\times B\to(a,b)\notin B\times A)$
- [ ] 41 because the latter has something like $\{\{a,b\},c\}$ where $a\in A,b\in B\ldots$
  while the former $\{a,b,c\}$
  - [$;$ and $,$](https://faculty.nps.edu/ncrowe/book/ad.html#:~:text=Queries%20are%20things%20you%20type,and%20semicolons%20mean%20%22or%22.) in prolog although $;$ means "and" [somewhere](https://math.stackexchange.com/a/3092850/1059606).
  - ans here should be $\{((a,b),c),\ldots\}$ and $\{(a,b,c),\ldots\}$
- [x] 42 similar to 41
- [ ] 44 $\forall a\forall b\exists c \ldots b=c$, similarly $\forall a\exists b\forall c \ldots b=c$ Q.E.D.
  - ans
    symmetry.
- [ ] 50
  - ans
    a. if $S\in S$ then we don't conform to the condition $x\notin x$, so should $S\notin S$
    b. similar to a.
  - based on p147 where the *property*, i.e. $x\notin x$ here, may "leads to paradoxes".
- [ ] 51 $C_n^{i},i=1\sim n$ selection.
### 2.2
- 2~4,22~24,28,34,40~42,54~66,74\\\\\\\\\\\\\\\\\\\\\\\\\\ skipped
- [ ] 6 the membership table is more intuitive where $\varnothing$ always corresponds to $F$.
- [x] 8,10,12,20(e) similar to 6 ans, the "Set-builder notation" is intuitive.
  - 12
    $\{x|x\in A\vee(x\in A\wedge x\in B)\}=\{x|(x\in A\vee x\in A)\wedge(x\in A \vee x\in B)\}
    =\{x|x\in A\}=A$
  - here I only offer the 12 because the rest are really similar (in some way, no need to offer 12 at all).
  - ans of 12 is a bit complex.
- [ ] 14 by Venn
- [x] 16 by definition with "Set-builder notation".
- [ ] 18 
  see ans based on $T/F$ pairs of (A,B).
- [ ] 21
  definition
  a. the latter means "in A and in U but not in B"
    since in A -> in U
    so "in A but not in B", i.e. $A-B$
- [x] 26,36,52 by definition
  in A then remove C, then remove B or (B but in C) because the latter *has been removed* before.
- [ ] 30 TODO what is A~D exactly?
- [ ] 32
  a(C is superset of A,B),b(C is the subset of A,B) not
  c can based on the venn.
- [ ] 38, i.e. $A\oplus B=A\cup B-(A\cap B)$
- [ ] 44
  b see the ans by using proof by cases
- [ ] 46
  - can be seen as truth table of *exclusive or* $\oplus$, so associative.
  - [detailed](https://math.stackexchange.com/a/4343192/1059606)
    keywords: In the first of these cases, symmetric under permutation (so just permute among $A,B,C$),since Δ is commutative (IMHO no need if already permutation)
- [ ] 47 yes
  ~~if $A\neq B$, then $\exists x\in A\notin B\to\{x|x\in A\vee x\in C\wedge\}$~~
  - venn can be intuitive but not strict.
  - ~~TODO strict proof~~
    similar to the one exercise before
    1. $\forall x\in A\wedge x\notin C\to x\in B\oplus C\to x\in B$
    2. 
      $$
      \overline{A\oplus C}=\overline{B\oplus C},\\
      \forall x(x\in A\wedge x\in C, \text{i.e. } x\in \overline{A\oplus C})\to x\in \overline{B\oplus C},
      x\in C\to x\in B\cap C
      $$
    based on above $A=B$
- [ ] 48
  based on 46, 
  the left means odd, i.e. either $A\oplus B$ or $C\oplus D$, then $A/B$ based on $C,D/\varnothing$, so odd
  the right is similar.
- [ ] 50 $|A\cup B|\le |A|+|B|$
- [ ] 68 b,d T
  - see ans 
    allow duplicate.
- [x] 70
  a. ~~$A+B$~~ 
    $A\cup B$
  b. $A\cap B$
  c. $B-A$
  d. $A+B$
- [ ] 72
  a,b are trivial using available axioms
  c $A\cup B=(A-B)\cup(A\cap B)\cup(B-A)$ then 
    $A-B=\varnothing,B-A=\varnothing$
  d similar to c where $|A-B|\ge 0$.
  e 
  - see ans 
    c. need plus "if"
      and it proves $p\wedge\neg q$ is impossible to be $F$, so Q.E.D.
  - e. 
    - [Steinhaus Transform proof](https://mathoverflow.net/a/210750) where [metric definition](https://en.wikipedia.org/wiki/Metric_space#Definition) 1~3 are trivial.
      - where $\le$ numerator is based on applying $r$ and then metric definition 4 for $d(x,y)$.
    - prove [the cardinality of symmetric difference](https://math.stackexchange.com/a/2128814/1059606) is metric 
      based on exercise 48 conclusion, if $x\in B$, then in *even* sets
      so $(A△B)△(B△C)=A△C$
      - similar to above, definition 1~3 are trivial.
    - "third observation above" then use [Steinhaus Transform](https://mathoverflow.net/a/18090).
### 2.3
- 4~6,10,18,28,30~32,38,44,60~66(64,66 notice the domain) skipped
- [x] 2
  a. one-to-mul, so not
  b. yes
  c. $n=\pm 2$ no one corresponding image.
- [ ] 8
  g. $\lceil\frac{1}{2}\rceil$ (here the $\frac{1}{2}$ inside the $\lfloor\ldots\rfloor$ can be dropped)
  h. similar to g, $\lceil\frac{1}{2}\rceil+\lfloor\frac{1}{2}\rfloor=1$
  - the h is $\lceil\ldots\rceil$ so should be $+1$
- [x] 12 i.e. whether monotonic
- [ ] 14 let one variable be 0, and whether the unary function onto.
  a,c,d are
  - See ans d
- [x] 16 a,b
- [ ] 20 see ans
  c. just swap.
- [x] 22
  a,d are
  - see ans by the inverse function.
- [x] 24 definition.
- [ ] 26 
  a. $\ldots<\ldots\to\ldots=\ldots$
  b. function may equal somewhere.
  - see ans for the strict proof
- [ ] 34
  a. contradiction
    if f not then also $f(k),k=g(x)$, i.e. $f\circ g$
  b. similar to a
  c. 
    1. if g onto, then $f\circ g$
  - see ans for c
    here let -> $\forall$.
    - a,b is direct proof different from above.
  - here c 
    g is onto -> f is onto
    - intuitively, A can map to *all* B, if f is not onto, then B can't map to all C,
      also A can't map to all C, so $f\circ g$ is not onto, contradiction.
    - this doesn't need g is onto at all. See a ...
- [x] 36
  no need for f to be one-to-one
  $$
  \begin{align*}
  g(x_1)=g(x_2) &\Rightarrow\\
  f(g(x_1))=f(g(x_2)) &\Rightarrow &&&& f\circ g\ \text{are one-to-one}\\
  x_1=x_2 &
  \end{align*}
  $$
- [x] 37
  $$
  \begin{align*}
  &&&\text{let } g:A\to B,\forall y\in B,f(y)=k=f\circ g(x)&&&&&&f\circ g,f\ \text{are onto}&\\
  \overset{?}{\Rightarrow}&&&y=g(x)&&&&&&\text{this = needs f to be one-to-one}&
  \end{align*}
  $$
  - intuitively
    draw [map graph][2_3_37]
  - does $g,f\circ f\to f$?
    similar to 36, here the g is also one redundant predicate.
    $$
    \begin{align*}
    \text{let } f:B\to C,&g:A\to B\\
    \forall z\in C\exists x\in A,&g(x)=y,f\circ g(x)=z\\
    \Rightarrow&\exists y\in B f(y)=z. \tag*{$\blacksquare$}
    \end{align*}
    $$
- [ ] 40
  $f\circ g(x)=a(cx+d)+b=acx+ad+b$
  $g\circ f(x)=c(ax+b)+d=acx+bc+d$
  so necessary and sufficient: $b=d,ad=bc$
  - see the ans
- [ ] 42
  a. based on definition 4
  $$
  \begin{align*}
  f(S\bigcup T)=&\{f(x)|x\in(S\bigcup T)\}\\
  =&\{f(x)|x\in S\vee x\in T\}\\
  =&\{f(x)|x\in S\}\bigcup\{f(x)|x\in T\}\\
  =&f(S)\bigcup f(T)
  \end{align*}
  $$
  b. similar to above but
  - $\{f(x)|x\in S\wedge x\in T\}\neq \{f(x)|x\in S\}\bigcap\{f(x)|x\in T\}$
    because maybe 
    $$
    \exists s\in S,\exists t\in T,s,t\notin S\bigcap T\Rightarrow (f(s)=f(t))\wedge
    (\forall k\in S\bigcap T,f(k)\neq f(s))
    $$
  - then $\subseteq$ is by definition
  - see ans for the detailed proof
- [ ] 46
  a. similar to 42, here only show one side.
  $$
  \begin{align*}
  &\text{suppose }b\in S\bigcup T,f^{-1}(b)=a\\
  &b\in S\to a\in f^{-1}(S)\quad\text{or}\quad b\in T \to a\in f^{-1}(T)\\
  \Rightarrow& a\in f^{-1}(S)\bigcup f^{-1}(T)
  \end{align*}
  $$
  b. all "if and only if" are by definition.
    compared with 42, here inverse *back* -> *break* $\bigcap$ -> inverse -> $\bigcap$
    but 42 can't do something similar to this.
    - intuitively 
      use one example,
      $$
      S=\{1,2\},T=\{2,3\},f(0)=1,f(1)=f(2)=2,f(3)=3\\
      \Rightarrow f^{-1}(S)={0,1,2},f^{-1}(T)={1,2,3},f^{-1}(S\bigcap T)={1,2}
      $$
      - compared with 42(b), 
        - here the function inherent property doesn't allow the **one-to-mul** mapping, so 
          $\nexists a\in S\cap\overline{T},b\in T\cap\overline{S},f^{-1}(a)=f^{-1}(b)$
          then nothing added to $f^{-1}(S\bigcap T)$ based on $f^{-1}(S)\bigcap f^{-1}(T)$
        - the 42(b) allows **mul-to-one** mapping, so 
          $\exists a\in S\cap\overline{T},b\in T\cap\overline{S},f(a)=f(b)$
          then maybe something added to $f(S\bigcap T)$ based on $f(S)\bigcap f(T)$
    - algebraical proof:
      $$
      \newcommand{\myrightarrow}[1]{{\overset{#1}{\xRightarrow{\hspace{7cm}}}}}
      \begin{align*}
      & & f^{-1}(S)&=&&f^{-1}((S\bigcap T)\bigcup(S\bigcap \overline{T})),\text{let }A=(S\bigcap T)\bigcup(S\bigcap \overline{T})\\
      & & f^{-1}(T)&=&&f^{-1}((S\bigcap T)\bigcup(\overline{S}\bigcap T)),\text{let }B=(S\bigcap T)\bigcup(T\bigcap \overline{S})\\
      &\myrightarrow{\text{use (a) result}}& f^{-1}(S)\bigcap f^{-1}(T)&=&&(f^{-1}(S\bigcap T)\bigcup f^{-1}(S\bigcap \overline{T}))\bigcup(f^{-1}(S\bigcap T)\bigcup f^{-1}(T\bigcap \overline{S})),\\
      & & (\overline{S}\bigcap T)\bigcap(\overline{S}\bigcap T)&=&&(\varnothing)\bigcap(\varnothing)\\
      &\myrightarrow{\text{due to function mapping any preimage to one \textbf{unique} image}}& (f^{-1}(\overline{S}\bigcap T))\bigcap(f^{-1}(\overline{T}\bigcap S))&=&&\varnothing\\
      &\text{similarly }& (f^{-1}(\overline{S}\bigcap T))\bigcap(f^{-1}(T\bigcap S))&=&&\varnothing\\
      &\text{and }& (f^{-1}(\overline{T}\bigcap S))\bigcap(f^{-1}(T\bigcap S))&=&&\varnothing,\\
      &\text{then due to only \textbf{one} of four combinations between } A \text{ and } B& f^{-1}(S)\bigcap f^{-1}(T)&=&&f^{-1}(S\bigcap T)\tag*{$\blacksquare$}
      \end{align*}
      $$
- [x] 48,50 prove by case
- [x] 52,56 similar to one example $n\le x\lt n+1$
- [x] 54
  a. by definition
  b. similar to a
- [ ] 58
  $\lceil a\rceil\le n$
  - see the ans
    it is "the number of integers n" instead of "integers n".
    - after 1st hinted by the ans.
      the integers are $\{x|\lceil a\rceil\ge x\le\lfloor b\rfloor\}$, so 
      $\lfloor b\rfloor-\lceil a\rceil+1$
- [x] 68
  first draw $\lceil x\rceil$ then move up based on $\lfloor\frac{x}{2}\rfloor$
- [x] 70
  a,b similar to the methods to scale/move function along the axis learned in the senior high school.
  c,d draw original function and then transform it to splitted straight lines
  e $\forall k\in\mathbf{N},\frac{x}{2}=k\Rightarrow f(x)=k^2\\\frac{x}{2}\in(k,k+1)\Rightarrow f(x)=k(k+1)$
  f similar to e
  g based on one example before, $f(x)=2\lceil\frac{x}{2}\rceil$ then similar to b
- [ ] 72
  - notice we need to prove both $f\circ g$ and $g\circ f$ because they are not always same 
    - although for the inverse function they must be same by definition because let $g=f^{-1}$ 
      and applying the $f\circ f^{-1}$ with get the the other equation.
      but due to ["Begging the question"](https://en.wikipedia.org/wiki/Begging_the_question) we can't use it.
      > when an argument's premises *assume* the truth of the *conclusion*
    - based on [this](https://math.stackexchange.com/a/1234668/1059606) which is got in the QA recommendation when [asking](https://math.stackexchange.com/questions/ask) the question "Why does the proof of inverse function need the both ordering, i.e. $f\circ f^{-1}$?" but not after appending "and $f^{-1}\circ f$", 
      both $(f\circ g)\circ (g^{-1}\circ f^{-1})$ and $(g^{-1}\circ f^{-1})\circ (f\circ g)$ are needed to be proven because 
      $(f^{-1}\circ f)(x)=x$ while $(f\circ f^{-1})(1)=2$ (the above example can be generalized to $\mathbb{R}$ domain with added $f^{-1}(x)=x-1,x\neq 1$).
  - use [associative property](https://math.stackexchange.com/a/1267985/1059606) same as the ans
    - the ans uses the nested function property.
- [x] 74 by contradiction
  - if not one-to-one but onto, then "not one-to-one" means $\exists a_1,a_2\in A,\exists b\in B,f(a_1)=f(a_2)=b$, then with $|A|=|B|$, it is impossible to be onto 
    because even the rest except $a_1,a_2$ is one-to-one, *one* element in $B$ is not onto.
    - this means same as the ans which is similar to the following $|A|<|B|$.
  - if one-to-one but not onto, then $|A|<|B|$ -> contradiction.
- [x] 76
  a. T definition based on $n\lt n\le n+1$
  b. F $0.5+0.5$
  c. T $n\le\frac{x}{2}\le n+1$ then two cases for n odd($\frac{n+1}{2}$)/even($\frac{n+2}{2}$), $\blacksquare$
    - the ans, here assume use $n'$ in ans
      1. $k=0$ corresponds to odd $n=2n'-1$
      2. $0\lt k\le 2$ corresponds to even $n=2n'$
      3. $2\lt k\lt 4$ corresponds to odd $n=2n'+1$
  d. F let 
    $x=(n+1)^2-\epsilon,\epsilon\in[0,1)$
    the right is $n$
    while the left is $n+1$
  e. three different cases after using "without loss of generality".
    - see the ans to consider *only* the exceeding cases.
- [x] 78 three cases, here only show one, the rest is similar.
  $n\le x\lt n+\frac{1}{3}$ no right terms round up -> 0, also for the left.
- [ ] 80 
  let "the domain of definition" be $S$
  a. "u if f is *undefined* at a." by definition -> the corresponding elements in $A$ are in $A-S$ -> partial function
  - The ans shows $f^{*}$ is one *total* function although the question says "can be viewed".
- [ ] 81
  a. index function 
  - see cardinality of a set with [**repeating**](https://math.stackexchange.com/a/391522/1059606) elements
  b. make both sets as specific tuples, and index them.
  - see the ans for strict maths description where
    1. bijection is due to one-to-one (the conclusion to prove) and onto ($\{1, 2, \ldots , m\}$ is the entire codomain)
    2. bijection implies the existence of $g^{-1}$
- [ ] 82
  - ~~does "proper" mean infinite?~~
  - see the ans
    a. just prove not finite -> infinite.
      TODO [Pigeonhole principle](https://builtin.com/data-science/pigeonhole-principle) means mul-to-one but here the proper subset to the universal set means onto impossible but not for one-to-one which doesn't allow mul-to-one.
      > Case A is the case illustrating the essence of the pigeonhole principle
      
    b. just define one [choice function](https://en.wikipedia.org/wiki/Axiom_of_choice#Statement) (i.e. self-mapping function)
    $$
    f(a_i) = a_{i+1}\\
    f(x)=x\text{ when }x\in S-{a_{i},\ldots}
    $$
      which is **infinite**, the $a_{i+1}$ avoids duplicate -> *one-to-one*
      since 
      $a_{i+1}$ starts from $a_1$, so *onto* for $A= S − \{a_0\}$
    - This is similar to p197 how to sum the infinite series.
### 2.4
- 2~4,10~12,18~22,30~32,36,40~42,46~48 skipped
- [x] 6
  d. due to $(k+1)^2-k^2=2k+1$
- [ ] 8 see the ans
- [ ] 14
  here doesn't show the initial condition.
- [x] 16
  g. just two cases
    $$
    \begin{equation}
      a_n=
      \begin{cases}
        \frac{n}{2}, & \text{if n is even} \\
        \frac{n-1}{2}, & \text{otherwise}
      \end{cases}
    \end{equation}
    $$
- [ ] 24
  a. $B(k)=(B(k-1)-P)*(1+\frac{r}{12})$
  - see the ans.
- [ ] 26
  e. not $4^n\ldots$
- [ ] 27
  - see the ans
    ~~assume $k^2 \lt a_n \lt (k + 1)^2$~~
    - ~~here should be $k^2\le a_n \lt (k + 1)^2$ because $n+k$ numbers can contain $k^2$ but not $(k + 1)^2$ which is not in the square sequence.~~
      here we don't allow the sequence like $1,2,\ldots,n,(k+1)^2$, i.e. $1,2,\ldots,n,k^2$.
      so $k^2\le a_n \lt (k + 1)^2$ is impossible, i.e. something like $\{1,2,3,4\}$ not taken in account.
      - this can also be shown in $l=\{1, 2, \ldots, a_n\}$ where the last term $a_n$ is the nonsquare.
      - so $a_n=n+k$ by calculating the cardinality of the sequence $l$
- [ ] 28
  $$
  \newcommand{\myrightarrow}[1]{{\overset{#1}{\xRightarrow{\hspace{7cm}}}}}
  \begin{align*}
    \text{let }a_n=t,&&\frac{t(t-1)}{2}\lt n&\le \frac{t(t+1)}{2}\\
    \myrightarrow{}&&(t-\frac{1}{2})^2-\frac{1}{4}\lt 2n&\le (t+\frac{1}{2})^2-\frac{1}{4}\\
    \myrightarrow{t-\frac{1}{2}\lt 2n+\frac{1}{4},\quad 2n\lt(t+\frac{1}{2})^2}&&
    \sqrt{2n}-\frac{1}{2}\lt t&\lt\sqrt{2n+\frac{1}{4}}+\frac{1}{2}\\
    \myrightarrow{\substack{\text{the left implies }t\text{ can't be} \lfloor\sqrt{2n}-\frac{1}{2}\rfloor,\\\text{the right implies }\lfloor\sqrt{2n}+\frac{3}{2}\rfloor\text{ impossible }\\\text{because }(\sqrt{2n}+\frac{3}{2})-(\sqrt{2n+\frac{1}{4}}+\frac{1}{2})>\sqrt{2n+1}-\sqrt{2n+\frac{1}{4}}>0}}&&t&=\lfloor\sqrt{2n}+\frac{1}{2}\rfloor\tag*{$\blacksquare$}
  \end{align*}
  $$
  - the ans just find the alternate **exact** answer and prove equivalence with the question conclusion instead of proving by the result range.
    - ~~it assumes $\lfloor\sqrt{2n}\rfloor=m$~~
      if $\sqrt{2n}$ rounds up by becoming the **closest integer**, then 
      $\lfloor\sqrt{2n}+\frac{1}{2}\rfloor$ and $\lceil\sqrt{2n+\frac{1}{4}}-\frac{1}{2}\rceil$ must be same (see them on the number axis)
      - so $\sqrt{2n}$ rounds down, then 
        $\sqrt{2n}\le m+\frac{1}{2}$, see the ans
        - notice the "smaller" implies $\sqrt{2n+\frac{1}{4}}\gt m+\frac{1}{2}$ 
          not having $=$.
- [ ] 34
  a. $\sum_{i=1}^{3}(2i-3)=2*6-9=3$
    hinted by the ans (notice the $2i$ instead of $i$)
- [ ] 38
  - this method can be generalized with induction for all $\sum_{k=1}^{n}k^n,n\in\mathbb{N}$
- [ ] 43
  $\text{let }\lfloor\sqrt{m}\rfloor=t,\sum=1*3+2*5+\ldots+(t-1)*(2*(t-1)+1)+t*(m-(t-1)^2)$
  then hinted by the ans, $\sum_{k=1}^{t-1}(2k^2+k)+t*(m-(t-1)^2)\blacksquare$
  - see the ans here should be $t*(m-t^2+1)$ where 
    $t^2$ means the start index of $\lfloor\sqrt{m}\rfloor$
    and $+1$ means take in account the integer index $\lfloor\sqrt{m}\rfloor^2$.
- [x] 44 similar to 43.


---

[SOLUTIONS_8th]:./Discrete%20Mathematics%20and%20Its%20Applications,%20Eighth%20Edition%20SOLUTIONS.pdf
[SOLUTIONS_7th]:./discrete-structure-solution-student39s-solutions-guide_compress_7th.pdf
[stirling]:./papers/stirling.pdf
[miscs_ipynb]:./miscs_snippets/miscs.ipynb

<!-- exercise help pdf -->
[2_3_37]:./latex_misc_pdfs/Discrete_Mathematics_and_Its_Applications_2_3_37.pdf