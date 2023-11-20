@ArnoMittelbach Could I ask some small questions? 1. With only `\let\mylb\\ \renewcommand{\\}{& x \mylb[1cm]}` it only works for text instead of the `align*` block. What causes this weird result? 2. With yours, only `align*` but not text works. After some search especially https://tex.stackexchange.com/a/383381/308105, I know `\let` will make `\myhalign` expansion same as `\halign`. Then the above means `\let\myhalign\let\mylb\\...\myhalign` which is nested. So how does this nested block make `\\` in the `align*` block work?
After viewing this [reference Tex SX link](https://tex.stackexchange.com/a/39020/308105) referred to by many Tex SX links, I viewed the `ltoutput.dtx` file and found the `\makeatletter\setlength{\@fptop}{0pt}\setlength{\@fpsep}{3pt}\makeatother` can solve the above problem. See the [codes](https://www.overleaf.com/read/jfzppwscpxqm#375fa6) which is a bit different from the above in my 2nd comment. Hope this can help the future readers.

check p10 whether the ideas of each chapter are mastered.
# [online resources](https://highered.mheducation.com/sites/125967651x/student_view0/web_resources_guide.html) from [this](https://highered.mheducation.com/sites/125967651x/information_center_view0/)
- Discrete Mathematics and Its Applications [Student’s Solutions Guide](https://www.academia.edu/36410920/Students_Solutions_Guide) pdf with the unavailable version.
- [test bank](https://www.stuvia.com/en-us/doc/2018491/discrete-mathematics-and-its-applications-8th-edition-rosen-test-bank.pdf)
# markdown notice
- "- [ ]" can't be ended with one space.
- not use number bullet list inside "-" bullet list which may be changed to "a,b,c"
- use number bullet list instead of "a,b,c" to help the indentation.
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
## miscs
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
### added after reviewing
- modus ponens means by [**placing**](https://en.wikipedia.org/wiki/Modus_ponens) $P$, then $Q$
  modus tollens means ["taking away"](https://en.wikipedia.org/wiki/Modus_tollens) $Q$, i.e. $\neg Q$, then $\neg P$
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
      then $\notin$ becomes $\overline{A}$, etc, to convert *back* to the set theory.
    - The use the *equivalence of proposition* $\equiv$ to prove the $\leftarrow$ if having proven $\rightarrow$.
  - example 11 just uses the $\equiv$ implicitly.
### 2.3
- p170 function definition implies no one-to-mul and part-to-total/part (i.e. must total-to-...). <a id="default_total_function"></a>
  “one-to-one” means not mul-to-one, i.e. if *only use one in the domain*, then *no redundancy* in the *domain*.
  "onto" means no redundancy in the *codomain*, i.e. no total-to-part.
- > A one-to-one correspondence is called invertible

  ~~only needs one-to-one to make "invertible" possible.~~
  - one-to-one due to above p170 definition where $a$ as $f^{-1}$
    image needs to be *unique* for each $b$. -> " more than one such a"
  - onto due to "each element of A" which applying to $f^{-1}$ means "each element of B" in p170
    so no part-to-total
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
### 2.5
- p204 
  $a_n=f(n)\Rightarrow (f(n)\to a_n,\text{one-to-one from }\mathbf{Z^+})\wedge (f^{-1}(a_n)=n,\text{due to the \textbf{unique} index})$
- [Calculus of variations](https://en.wikipedia.org/wiki/Calculus_of_variations#Euler%E2%80%93Lagrange_equation)
  here "variations" are "small changes in functions and functionals". More intuitively, it means $\delta y(x)$ which means the difference for the **entire** function instead of at one specific point, see [profoundphysics](https://profoundphysics.com/calculus-of-variations-for-beginners/).
  - > Generally, a valid functional that takes in a full function and returns just a *single* number can be obtained by writing the functional as a *definite integral*.
    > crucially, the *same* number for all values of the variable *x*

    so it describes the property of the *entire* function, see [functional](https://en.wikipedia.org/wiki/Functional_(mathematics)#Duality) typically as one [definite integral](https://en.wikipedia.org/wiki/Calculus_of_variations#Example).
    - See the table in "Functions vs Functionals".
    - > a functional derivative considers the change in a functional *with respect to a function*
    - > **Similarly**, there is an important concept in calculus of variations called the variation of a functional.
    - "What Does The Euler-Lagrange Equation Tell Us?" where $\frac{\delta F}{\delta y}$ can be used to optimize for the maxima and minima.
      > The goal of these steps and of any calculus of variations problem is to *find the function y(x)* – the function making a given *functional stationary*.
    - steps:
      1. Write down a functional F(y) describing the problem in the form of a *definite integral* over some function f(x,y,y’).
      2. *Identify* the integrand function f(x,y,y’). You’ll need this for the Euler-Lagrange equation.
      3. Write down the Euler-Lagrange equation for the function f identified in the last step.
      4. Solve the resulting *differential equation* for y(x). This is the function that makes the original functional F(y) stationary.
    - [Beltrami identity](https://en.wikipedia.org/wiki/Beltrami_identity#Derivation)
  - TODO [Lagrangian mechanics](https://en.wikipedia.org/wiki/Lagrangian_mechanics) [diff](https://physics.stackexchange.com/a/265257/313379) with others
    > classical mechanics – or more precisely, Lagrangian mechanics
    > this formulation of classical mechanics where we use *calculus of variations and the action principle* is called Lagrangian mechanics.
    - > there is a formulation of classical mechanics that also uses calculus of variations, but instead of the Euler-Lagrange equation, it takes advantage of the *Beltrami identity*.
      > This formulation goes by the name of *Hamiltonian* mechanics
  - > This states that the dynamics of a field are obtained by *minimizing the action* – which being a functional, of course, requires the tools of variational calculus.
  - euler lagrange equation [derivation](https://mathworld.wolfram.com/Euler-LagrangeDifferentialEquation.html), [wikipedia](https://en.wikipedia.org/wiki/Euler%E2%80%93Lagrange_equation#Statement) and [libretexts](https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electro-Optics/Direct_Energy_(Mitofsky)/11%3A_Calculus_of_Variations/11.03%3A_Derivation_of_the_Euler-Lagrange_Equation) are similar which are less familiar for me.
    $dv=d(\delta q)$
    - > But we are varying the path only, not the endpoints

      see [this](https://en.wikiversity.org/wiki/Continuum_mechanics/Calculus_of_variations#Minima_of_functionals) where is to get the maxima/Minima based on the *conditions for endpoints*.
    - (7)~(16) finish the proof.
    - for [multi-dimensional](https://en.wikipedia.org/wiki/Euler%E2%80%93Lagrange_equation#Statement) just list *multiple one-dimensional* Euler–Lagrange equations, see $i=1,\ldots ,n$
- FIGURE 3 doesn't circle the $\frac{p}{q}\text{ due to }p,q\text{ are not coprime}$ and use the sequence property in p204 to prove countable.
- Cantor Diagonal Method for 
  1. [theory of "computation"](https://concretenonsense.wordpress.com/2011/07/12/cantors-diagonal-argument-and-undecidability/)
    - > Now, consider the Turing machine $M_{\text{bad}}$ which, given input $\langle M \rangle$, does the opposite of what $D$ does on input $\langle M, M \rangle$

      TODO here maybe the diagonal is not one must.  
      > But *we’ve enumerated all* the Turing machines, so we have a contradiction! Therefore, L is not decidable.

  2. real numbers
    - example 5
      is based on [**contradiction**][Cantor_diagonal_argument_string] between assumption that the set *can be listed* which is by sequence property and the result that one element is *not in the list*.
      - $\frac{m}{2^n}$ for $m$ is odd due to something like $\frac{3}{4}=\frac{1}{4}+\frac{1}{2}$, so the latter two have two binary expansions implies the 1st also has.
        - This is the book why
          > expansion has a tail end that consists entirely of the digit 9 is excluded
          - IMHO this exclusion **doesn't influence** the book proof because their decimal representation is not same although their eventual values are *same*.
            This is similar to the above where allows something like $0.1000\ldots$ and $0.0111\ldots=0.1000\ldots$ to both exist.
            but not the [following](https://en.wikipedia.org/wiki/Cantor's_diagonal_argument#Real_numbers)
            - But for the following wikipedia proof, it **influences** because it needs to construct one **bijection** map which doesn't allow *two* different decimal/binary representations mapped to the *same* real value.
      - ~~TODO meaning of~~
        > Also, f2 (t) is not a bijection to (0, 1) for the strings in T appearing after the binary point in the binary expansions of 0, 1, and the numbers in sequence r.

        TODO means same as
        >  These are called dyadic numbers and have the form m / 2n where m is an odd integer and n is a natural number
      - > Define the bijection g(t) from T to (0, 1): If t is the nth string in sequence s, let g(t) be the nth number in sequence r ; otherwise, g(t) = 0.t2.

        this just *scales* the subset $r$ with "two binary expansions" to *half*, but due to infinite, the scale doesn't take the effects for the cardinality.
        more specifically, it ensures *one-to-one index* for $s\to r,\text{ where }s\in T$.
        - then the rest $T-s$, it is trivial that they are one-to-one. <a id="binary_string_0_1"></a>
        - here one-to-one is trivial
          - [due](https://abstractmath.org/MM/MMRealNumbers.htm#:~:text=Every%20real%20number%20can%20be,for%20numbers%20such%20as%202.56.)) to
            > A real number is a number that can be represented as a (possibly infinite) decimal expansion

            even without the above map, the decimal expansion is onto to $R$, so also $(0,1)$.
      - Then use "composite function" to enlarge the bijection.
      - > He first removed a countably infinite subset from each of these sets so that there is a *bijection* between the remaining *uncountable* sets

        here assume that uncountable infinite can biject to each other.
- > It can be shown that the smallest infinite cardinal numbers form an infinite *sequence*

  [see](https://en.wikipedia.org/wiki/Continuum_hypothesis#Cardinality_of_infinite_sets)
  > Assuming the axiom of choice, there is a unique smallest cardinal number

  the function inherently implies "unique", i.e. only one $y$ for $f(x)=y$.
  - Also [see](#Axiom_of_choice)
- Continuum hypothesis is [not proven at present](https://en.wikipedia.org/wiki/Hilbert%27s_problems#Table_of_problems).
- Here from p203 definition 2, the "onto" to $|A|\ge |B|$ is not direct
  proof see [this](https://math.stackexchange.com/a/286800/1059606) and my [rejected edit](https://math.stackexchange.com/review/suggested-edits/2036195) <a id="onto_compare_cardinality"></a>
  - the 1st part of the proof is same as [this](http://www.randomservices.org/random/foundations/Functions.html#aoc) which referenced [here "duality"](https://math.libretexts.org/Courses/Monroe_Community_College/MTH_220_Discrete_Math/Appendices/A.1%3A_Cardinality-additional_info#:~:text=A%E2%89%88C.-,A%20one%2Dto%2Done%20function%20f%20from%20A%20onto%20B,the%20same%20number%20of%20elements.)
## [A_Guide_to_Writing_Proofs]
I read it after chapter 1,2 but when I read it I thought I should read it while reading chapter 1,2 although that may be with many obstacles if not having all knowledge from the chapter 1,2.
- maths [argument](https://bridges.education.uconn.edu/wp-content/uploads/sites/753/2016/03/ARP_Grade3_Fractional-Parts-of-Candy-Bars-Packet-Overview.pdf)
- p2
  assumption: just one step forward
  write out what it would mean for $Q(x)$: just one step backward
- [universe of discourse](https://en.wikibooks.org/wiki/Discrete_Mathematics/Logic/Page_2#Universe_of_Discourse) ,i.e. domain
- For the exercises here, I only reviewed them by thinking of how to prove them and don't write down the proofs to most of them because they are similar to the book exercises after each subsection which are enough to grasp the ideas.
- 1.1.3 exercise 1
  $$
  \forall x\in X \cup(Y \cap Z)\\
  \Rightarrow x\in X\vee (x\in Y\wedge x\in Z)\\
  \Rightarrow
  \begin{cases}
    \xRightarrow{\text{if }x\in X\text{ but }x\notin Y \cap Z} x\in X\cup Y\\
    \xRightarrow{\text{if }x\in Y\cap Z\text{ then }x\in X\cup Y\text{ due to }x\in Y} x\in(X\cup Y)\cap Z 
  \end{cases}\\
  \text{ the above case 1 may deny this conclusion and the \textbf{exercise 2 solves} this problem}
  $$
- 1.1.4 $\bigcup$ and $\overline{Z}\text{ with }Z$ may imply "proof by cases".
- section 2.2 EXAMPLE 11 uses **logic**, i.e. definition, to prove set equation.
- always "as desired" to mark as $\blacksquare$ which may end with $\blacksquare$ again ~~or not~~.
- ~~"specialization" means similar to "instantiation" in section 1.6 TABLE 2 p103 -> "in particular".~~
- contraposition is based on ~~"converse"~~ contrapositive.
- $(p \wedge \neg q) \to r$
  is based on
  $$
  \text{suppose }p\text{ is true. the following skip some trivial steps}\\
  \begin{cases}
    q=T
    \begin{cases}
      \xRightarrow{\text{left side, i.e. }(p \wedge \neg q) \to r} r=F/T\\
      \xRightarrow{\text{right side, i.e. }p \to (q\vee r)} r=F/T
    \end{cases}\\
    q=F
    \begin{cases}
      \xRightarrow{\text{left side}} p\to r\\
      \xRightarrow{\text{right side}} p\to r\\
    \end{cases}
  \end{cases}
  $$
  - or more intuitively
    the left side means if both p and **not q**, then r
    the right side means if p, then either q or **not q** which implies r simialr to p6. <a id="tautology_q_neg_q"></a>
    trivially they mean same.
- > have no way of using the hypothesis

  this is based on using the direct proof, i.e. $f(x_1)=f(x_2)$ and $x_1<x_2$ don't match.
  but if using WLOG and "proof by contradiction", $\neg(f(x_1)<f(x_2))=(f(x_1)=f(x_2))\Rightarrow\neg (x_1<x_2)=(x_1=x_2)$ which is just the "However ..." context.
- p9
  $(p\wedge\neg r\to\neg q)\equiv( q\to\neg p\vee r)$
  similar to [this](#tautology_q_neg_q), $q$ with $p$ correspond to $r$ after the $\vee$.
  - or think it as p is **the ~~assumption~~ hypothesis** as the doc says,
    then $\neg r\to \neg q$ contraposition is $q\to r$
- 1.2.1 exercises
  1. it is to prove $\forall x\notin B\to x\notin A$, this contraposition is just the hypothesis 
    $\forall x\in A\to x\in B\Rightarrow A\subseteq B$
  2. trivial by $M=0\to\ldots$
  3. $y=(x+y)-x$ is trivial
    it is to prove based on assumption $\forall x\in\mathbf{Z}$
    then $\forall y\notin\mathbf{Z}\Rightarrow x+y\notin \mathbf{Z}$, this contraposition is same as before.
  4. similar to 3 
    transform to $x\in A(x\in B\to x\in A\cap B)$
- Example 5 in Section 1.7 shows vacuously true proposition is featured of the negative premise, so $\varnothing \subseteq A \cap \overline{B}$ should be **trivially** true where the conclusion is true regardless of the premise.
- Proof by contradiction
  see p113,114 where
  $\neg q\to(r\wedge\neg r),q\text{ is the conclusion to prove}$ can be thought as $(p \wedge\neg q) \to F,\text{where }p\text{ is }r$ which is shown in "This leads to the contradiction $p\wedge\neg p$" and same as example 14 shows.
- 1.2.2 exercises
  1. trivial using the definition.
    or similarly as the example $\exists x\in A\wedge x\notin A$ contradiction.
  2. since "for all sets A and B"
    suppose select $B\ni A\subseteq B$
    then $B\cap \overline{A}=B$
    if $A\neq \varnothing$
    then 
    $$
    \exists a\in A\subseteq B\Rightarrow a\in B\\
    \text{ but }a\notin \overline{A}\Rightarrow a\notin B\cap \overline{A}\text{ contradiction }\tag*{$\blacksquare$}
    $$
  3. suppose $\neq\varnothing$
    then suppose $T=x\in A\cup B$
    let $S=(\overline{A} \cup \overline{B})\cap(\overline{A} \cup B)\cap(A \cup \overline{B})$
    then
    - if $x\in (A\cap \overline{B})$, then 
      $x\notin (\overline{A} \cup B)\Rightarrow x\notin S\Rightarrow x\notin S\cap T$
    - for $x\in (A\cap B)$ and 
      $x\in (B\cap \overline{A})$, it is similar.
- 1.2.3
  1. example 16
    $$
    \text{since }A\neq\varnothing\wedge B\neq\varnothing\\
    \Rightarrow\forall (a,b)\in A\times B\text{, i.e. } a\in A,b\in B\\
    \Rightarrow (a,b)\in B\times A\\
    \Rightarrow A\subseteq B,B\subseteq A\\
    \Rightarrow A=B
    $$
  2. the 2nd is similar to the above
  3. first assume $A\neq\varnothing$, then to prove $B=\varnothing$
    - then use contradiction
      if $B\neq\varnothing$
      then $A\times B\neq\varnothing$ which contradicts with the hypothesis $A\times B=\varnothing$
  4. 
    $$
    \forall x\in (X\cup Y)\cap Z\wedge x\notin X\\
    \xRightarrow{(X\cup Y)\cap\overline{X}} x\in Y\\
    \xRightarrow{\cap Z} x\in (Y\cap Z)\\
    $$
- strategies are [more ~~generalized~~ targeted at the long term](https://www.clearpointstrategy.com/blog/strategy-vs-tactics) than tactics.
  > Strategy defines your long-term goals
- p11 three examples are all $\forall x\forall y P(x,y)\to Q(x,y)\text{ here }x,y\text{ can be the generalized variable like } (m,n)\text{ or function }f$.
  See example 17 which is the above case
  - example 17~~has "rational" -> $\exists p,q\frac{p}{q}$~~,18 has $\exists$ inside the $P(x,y)$
- 2.1
  1. 
  2. $\exists m=1$
  3. $\exists n=m$
  4. trivial with the algebra arithmetic.
  5. similar to the above
- TODO 2.2
## 3
### 3.1
- "Kitab al-jabr w’al muquabala" may be [arabic](https://en.wikipedia.org/wiki/Languages_of_Iraq)
- TODO The Art of Computer Programming ([TAOCP](https://www-cs-faculty.stanford.edu/~knuth/taocp.html))
- sorting algorithm [complexity](https://web.archive.org/web/20181216080432/https://www.cs.cmu.edu/~adamchik/15-121/lectures/Sorting%20Algorithms/sorting.html)
- [insertion sort](https://www.geeksforgeeks.org/insertion-sort/) just compares each item with its former
  and **insert** it at the appropriate location.
  - compared with others
    TODO [this](https://www.cprogramming.com/tutorial/computersciencetheory/sortcomp.html) different from [wikipedia](https://en.wikipedia.org/wiki/Sorting_algorithm#Comparison_sorts) about best case complexity with the bubble sort.
- [quarters, dimes, nickels, and pennies](https://www.nbp.org/ic/nbp/programs/gep/lemon/lemon-money.html)
- ALGORITHM 7 better adds:
```python
  while 
    ...
  if n==0:
    break
```
- the lemma 1 just means always using the optimized choice.
- p369 to prove the example 7
  - $P(n)$ just means the greedy is the **optimal** when it selects $n$ talks
  - basis: uses the overlap implied by the greedy.
    "end after $e_1$" because $e_1$ is the 1st ending.
  - inductive: 
    1. prove the $e_1$ ~~will~~ can be always chosen **regardless** of whether to use the greedy algorithm. (prove the 1st step is optimal)
    2. assume $e_1$ has been chosen, then based on the compatible index set 
      $S=\{x|s_x>e_1\}$ which is also **regardless** of whether to use the greedy algorithm
      then $P(k)$ which is optimal to 
      $S$ based on the induction hypothesis, this constructs the $P(k+1)$ with $e_1$ $\blacksquare$.
      (prove the next k are also optimal which is just based reusing $P(1)$ k times after removing the uncompatible talks)
      - Also obviously $e_1$ is **always chosen** by the greedy algorithm because it is the *1st* ending.
- 3.1.6 is similar to one exercise which defines one very special function.
  - [halting problem](https://en.wikipedia.org/wiki/Halting_problem#Proof_concept) is
    > The halting problem is undecidable, meaning that no general algorithm exists that solves the halting problem for **all possible** program–input pairs.
    so finding one special counterexample is enough.
    - for example, in the above link, $g()$ 
      (i.e. $K(P)$ in the book) has no valid inputs to output, i.e. not one computable function.
    - the link $halts(P)=H(P,P)\text{ in the book}$
- 
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
- when `\begin{aligned}` is [preferred](https://tex.stackexchange.com/a/95408)
  to `\begin{aligned*}`
- "implies" arrow [location](https://math.stackexchange.com/questions/711817/mathematical-notation-arrow-sign)
- `&` in `\aligned` is to [alternate](https://tex.stackexchange.com/a/159724) between left-aligned and right-aligned, so `&&` will make alternate *again*, becoming the original one.
  for example for the 1st `&`, the *left* of it is *right* aligned and the right of it is left aligned
  but for `&&`, the left is kept *same* and the right is *alternated*.
- newline "\\" must be in the maths mode or something like "\begin{align*}".
- [multiline](https://tex.stackexchange.com/questions/36343/multiline-text-under-over-arrows#comment72468_36343) in xRightarrow using [`substack`](https://tex.stackexchange.com/a/63192)
- emptyset [preferred $\varnothing$](https://math.stackexchange.com/questions/917467/is-varnothing-an-empty-set#comment1893997_917472)
- not comma among [multiple](https://dept.math.lsa.umich.edu/~kesmith/295handout1-2010.pdf) $\forall,\exists$ and $\ni$ for "so that".
- representation for [capital](https://www.overleaf.com/learn/latex/Mathematical_fonts) letters where both $\mathbb{P}$ and $\mathcal{P}$ are ok.
  [detailed](https://tex.stackexchange.com/a/58124)
## katex
- available [packages](https://github.com/KaTeX/KaTeX/wiki/Package-Emulation)
- set latex arrow with [specific length](https://tex.stackexchange.com/questions/269935/arrows-of-arbitrary-length#comment647948_269935) by `\newcommand{\myrightarrow}[1]{{\overset{#1}{\xRightarrow{\hspace{3cm}}}}}`
  - `\makebox` [unavailable](https://tex.stackexchange.com/a/6840)
    Also [`\settowidth`](https://tex.stackexchange.com/a/37294)
    and [`\parbox`](https://tex.stackexchange.com/a/269950)
## related with algorithm writing
See the `texdoc latex-refsheet` help, [`lshort`](https://tex.stackexchange.com/a/34903/308105) which shows `\right.` usage.
Also [texfaq](https://tex.stackexchange.com/a/16439/308105)
- `\verb` [similar](https://tex.stackexchange.com/a/47760/308105) to [`\texttt`](https://tex.stackexchange.com/a/470806/308105)
- `\Return` should be preceded with one blank line to be separate from others.
- [`makeatletter`](https://tex.stackexchange.com/a/8353/308105)
  - `@` [inside](https://tex.stackexchange.com/a/9788/308105) the commands
    relation with [above](https://tex.stackexchange.com/a/6253/308105)
- [`\begin{fleqn}`](https://tex.stackexchange.com/a/390092/308105)
- sometimes we use [`aligned`](https://tex.stackexchange.com/a/54686/308105) instead of `align*`
- flushright means right aligned, i.e. all contents can't exceed the right side.
  See [1](https://en.wikibooks.org/wiki/LaTeX/Boxes#framebox_and_fbox) [2](https://tex.stackexchange.com/a/116781/308105)
- [differences](https://www.overleaf.com/read/jvcqvktqhbmm#725f7c) between different `\def` and `\let`
- `expandafter` [1](https://en.wikibooks.org/wiki/TeX/expandafter) [2](https://tex.stackexchange.com/a/519/308105)
  - `\expandafter{...}` [usage](https://tex.stackexchange.com/a/594356/308105) which expands something first after `{`.
- whether `\let` is with `=` is all ok.
- align* implementation in [amsmath](https://tex.stackexchange.com/a/4389/308105) and maybe [others](https://tex.stackexchange.com/a/4388/308105)
- cases with [`[]`](https://tex.stackexchange.com/a/41429/308105)
### warning fixes
- [underfull/overfull](https://tex.stackexchange.com/a/395370/308105) hbox and vbox
  - their [meanings](https://www.overleaf.com/learn/how-to/Understanding_underfull_and_overfull_box_warnings#Overfull_and_underfull_boxes)
    > “stretch out” the content
    > exceeds the available space
### miscs
- how to use the [plain tex](https://www.overleaf.com/learn/latex/Questions/Can_I_run_plain_TeX_on_Overleaf%3F)
  - [books](https://tug.org/interest.html#plain) 
    doc [list](https://ctan.org/topic/tut-plaintex)
    1. [Impatient](https://ftp.kddilabs.jp/CTAN/info/impatient/book.pdf).
### TODO
- try use [`fltrace`](https://tex.stackexchange.com/a/39020/308105) to debug the "floating"
- how `##` [to `#`](https://tex.stackexchange.com/a/42464/308105) used in `\cases`
```bash
$ latexdef -t latex -s -f -E cases  
% latex.ltx, line 12595:
\DeclareRobustCommand*\cases[1]{\left\{\,\vcenter{\normalbaselines\m@th
    \ialign{$##\hfil$&\quad{##}\hfil\crcr#1\crcr}}\right.}
```
  - [`hfil`](https://tex.stackexchange.com/a/528921/308105)
  - [`vcenter`](https://www.tutorialspoint.com/tex_commands/vcenter.htm)
  - reasons why use [`\crcr`](https://tex.stackexchange.com/a/132586/308105)
  - [`ialign`](https://tug.org/TUGboat/tb07-1/tb14beet.pdf)
    ```bash
    $ latexdef -t latex -s -f z@skip   
    % latex.ltx, line 502:
    \newskip\z@skip \z@skip=0pt plus0pt minus0pt
    $ latexdef -t latex -s -f ialign   
    % latex.ltx, line 640:
    \def\ialign{\everycr{}\tabskip\z@skip\halign} % initialized \halign
    ```
    - TODO `everycr`
    - [`halign`](https://plain-xetex.neocities.org/misc/misc.pdf) `\halign{\it#\hfil&#&#&\bf#&#&#&\hfil\tt#\hfil\cr abc & d & e & f & g & h & i\cr a & b & c & d & e & f & ghj\cr}`
    - [`m@th`](https://tex.stackexchange.com/a/153398/308105)
    - [`\crcr`](https://tex.stackexchange.com/a/229792/308105)
- what is [RobustCommand](http://labmaster.mi.infn.it/wwwasdoc.web.cern.ch/wwwasdoc/TL8/texmf/doc/latex/base/html/clsguide/node36.html#:~:text=%5CDeclareRobustCommand*%20%7B,commands%20and%20make%20them%20robust.)
- differences between `cases` and `cases*` since `\addtolength{\jot}{-5pt}` only applies to the latter.
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
  c) see b), $99-n=n$ is impossible for $n\in\mathbf{Z}$
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
- [ ] 68 $Q\wedge\underset{i\in odd}{\vee}p(i,1)$
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
  - b. ~~-> $\neg D(logic)$,~~
    ~~but both $T\to T$ and $F\to T$ is possible, so~~
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
  so $a=\frac{3}{2},b=\frac{1}{2}\Rightarrow a,b\notin \mathbf{Z}$, 
  obviously $F$
  - Also see ans where use the *consecutive* square to prove.
- [ ] 12
  similar to 8
  [irrational numbers latex](https://texblog.org/2007/08/27/number-sets-prime-natural-integer-rational-real-and-complex-in-latex/)
  $\frac{p}{q}*k=\frac{m}{n},k\in \mathbf{I}$
  then $k=\frac{mq}{pn}\in \mathbf{Q}$ (why [Q for rational](https://math.libretexts.org/Bookshelves/Analysis/Real_Analysis_(Boman_and_Rogers)/01%3A_Numbers_-_Real_(%E2%84%9D)_and_Rational_(%E2%84%9A)/1.01%3A_Real_and_Rational_Numbers#:~:text=The%20set%20of%20rational%20numbers%20is%20denoted%20Q%20for%20quotients,Figure%201.1.)) -> contradiction.
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
- [x] 32 just use $\equiv$ based on axioms with the $\mathbf{R}$
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
    ```bash
    1. 111
         1
    2. 111
        1
    ```
    3. move two squares around
    ```bash
      1. 11
         11
      2. 11
        11
    ```
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
    ~~odd horizontal + even vertical ->~~
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
- 2~6,
  10,14~18,
  22,34~38,46 skipped
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
- 2~4,
  22~24,
  28,34,40~42,
  54~66,74 skipped
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
  1. the latter means "in A and in U but not in B"
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
      so $(A\Delta B)\Delta (B\Delta C)=A\Delta C$
      - similar to above, definition 1~3 are trivial.
    - "third observation above" then use [Steinhaus Transform](https://mathoverflow.net/a/18090).
### 2.3
- 4~6,
  10,18,28,30~32,
  38,44,60~66(64,66 notice the domain) skipped
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
- [ ] 33b because 2.5-22 needs it.
  b. due to the definition $\forall c\in C,\exists b\in B,f(b)=c$, then $\exists a\in A g(a)=b\Rightarrow f(g(a))=c\blacksquare$
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
  f(S\cup T)=&\{f(x)|x\in(S\cup T)\}\\
  =&\{f(x)|x\in S\vee x\in T\}\\
  =&\{f(x)|x\in S\}\cup\{f(x)|x\in T\}\\
  =&f(S)\cup f(T)
  \end{align*}
  $$
  b. similar to above but
  - $\{f(x)|x\in S\wedge x\in T\}\neq \{f(x)|x\in S\}\cap\{f(x)|x\in T\}$
    because maybe 
    $$
    \exists s\in S,\exists t\in T,s,t\notin S\cap T\Rightarrow (f(s)=f(t))\wedge
    (\forall k\in S\cap T,f(k)\neq f(s))
    $$
  - then $\subseteq$ is by definition
  - see ans for the detailed proof
- [ ] 46
  a. similar to 42, here only show one side.
  $$
  \begin{align*}
  &\text{suppose }b\in S\cup T,f^{-1}(b)=a\\
  &b\in S\to a\in f^{-1}(S)\quad\text{or}\quad b\in T \to a\in f^{-1}(T)\\
  \Rightarrow& a\in f^{-1}(S)\cup f^{-1}(T)
  \end{align*}
  $$
  b. all "if and only if" are by definition.
    compared with 42, here inverse *back* -> *break* $\bigcap$ -> inverse -> $\bigcap$
    but 42 can't do something similar to this.
    - intuitively 
      use one example,
      $$
      S=\{1,2\},T=\{2,3\},f(0)=1,f(1)=f(2)=2,f(3)=3\\
      \Rightarrow f^{-1}(S)={0,1,2},f^{-1}(T)={1,2,3},f^{-1}(S\cap T)={1,2}
      $$
      - compared with 42(b), 
        - here the function inherent property doesn't allow the **one-to-mul** mapping, so 
          $\nexists a\in S\cap\overline{T},b\in T\cap\overline{S},f^{-1}(a)=f^{-1}(b)$
          then nothing added to $f^{-1}(S\cap T)$ based on $f^{-1}(S)\cap f^{-1}(T)$
        - the 42(b) allows **mul-to-one** mapping, so 
          $\exists a\in S\cap\overline{T},b\in T\cap\overline{S},f(a)=f(b)$
          then maybe something added to $f(S\cap T)$ based on $f(S)\cap f(T)$
    - algebraical proof:
      $$
      \newcommand{\myrightarrow}[1]{{\overset{#1}{\xRightarrow{\hspace{7cm}}}}}
      \begin{align*}
      & & f^{-1}(S)&=&&f^{-1}((S\cap T)\cup(S\cap \overline{T})),\text{let }A=(S\cap T)\cup(S\cap \overline{T})\\
      & & f^{-1}(T)&=&&f^{-1}((S\cap T)\cup(\overline{S}\cap T)),\text{let }B=(S\cap T)\cup(T\cap \overline{S})\\
      &\myrightarrow{\text{use (a) result}}& f^{-1}(S)\cap f^{-1}(T)&=&&(f^{-1}(S\cap T)\cup f^{-1}(S\cap \overline{T}))\cup(f^{-1}(S\cap T)\cup f^{-1}(T\cap \overline{S})),\\
      & & (\overline{S}\cap T)\cap(\overline{S}\cap T)&=&&(\varnothing)\cap(\varnothing)\\
      &\myrightarrow{\text{due to function mapping any preimage to one \textbf{unique} image}}& (f^{-1}(\overline{S}\cap T))\cap(f^{-1}(\overline{T}\cap S))&=&&\varnothing\\
      &\text{similarly }& (f^{-1}(\overline{S}\cap T))\cap(f^{-1}(T\cap S))&=&&\varnothing\\
      &\text{and }& (f^{-1}(\overline{T}\cap S))\cap(f^{-1}(T\cap S))&=&&\varnothing,\\
      &\text{then due to only \textbf{one} of four combinations between } A \text{ and } B& f^{-1}(S)\cap f^{-1}(T)&=&&f^{-1}(S\cap T)\tag*{$\blacksquare$}
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
      $(f^{-1}\circ f)(x)=x$ while $(f\circ f^{-1})(1)=2$ (the above example can be generalized to $\mathbf{R}$ domain with added $f^{-1}(x)=x-1,x\neq 1$).
  - use [associative property](https://math.stackexchange.com/a/1267985/1059606) same as the ans
    - the ans uses the nested function property.
- [x] 74 by contradiction
  - if not one-to-one but onto, then "not one-to-one" means $\exists a_1,a_2\in A,\exists b\in B,f(a_1)=f(a_2)=b$, then with $|A|=|B|$, it is impossible to be onto 
    because even the rest except $a_1,a_2$ is one-to-one, *one* element in $B$ is not onto.
    - this means same as the ans which is similar to the following $|A|<|B|$.
  - if one-to-one but not onto, then $|A|<|B|$ -> contradiction.
- [x] 76
  1. T definition based on $n\lt n\le n+1$
  2. F $0.5+0.5$
  3. T $n\le\frac{x}{2}\le n+1$ then two cases for n odd($\frac{n+1}{2}$)/even($\frac{n+2}{2}$), $\blacksquare$
    - the ans, here assume use $n'$ in ans
      - $k=0$ corresponds to odd $n=2n'-1$
      - $0\lt k\le 2$ corresponds to even $n=2n'$
      - $2\lt k\lt 4$ corresponds to odd $n=2n'+1$
  4. F let 
    $x=(n+1)^2-\epsilon,\epsilon\in[0,1)$
    the right is $n$
    while the left is $n+1$
  5. three different cases after using "without loss of generality".
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
      
    b. just define one [choice function](https://en.wikipedia.org/wiki/Axiom_of_choice#Statement) (i.e. self-mapping function) <a id="Axiom_of_choice"></a>
      - Also [see](https://plato.stanford.edu/entries/axiom-choice/) where $f(X)\in X$ implies choose **inside** each subset
        or see wikipedia
        > given the sets {{4, 5, 6}, {10, 12}, {1, 400, 617, 8000}}, the set containing each smallest element is {4, 10, 1}

    $$
    f(a_i) = a_{i+1}\\
    f(x)=x\text{ when }x\in S-{a_{i},\ldots}
    $$
      which is **infinite**, the $a_{i+1}$ avoids duplicate -> *one-to-one*
      since 
      $a_{i+1}$ starts from $a_1$, so *onto* for $A= S − \{a_0\}$
    - This is similar to p197 how to sum the infinite series and p204 example 2.
### 2.4
- 2~4,
  10~12,
  18~22,
  30~32,
  36,40~42,
  46~48 skipped
- [x] 6
  d. due to $(k+1)^2-k^2=2k+1$
- [ ] 8 see the ans
- [ ] 14
  here doesn't show the initial condition.
- [x] 16
  g. just two cases
    $$
    \begin{equation*}
      a_n=
      \begin{cases}
        \frac{n}{2}, & \text{if n is even} \\
        \frac{n-1}{2}, & \text{otherwise}
      \end{cases}
    \end{equation*}
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
  - this method can be generalized with induction for all $\sum_{k=1}^{n}k^n,n\in\mathbf{N}$
- [ ] 43
  $\text{let }\lfloor\sqrt{m}\rfloor=t,\sum=1*3+2*5+\ldots+(t-1)*(2*(t-1)+1)+t*(m-(t-1)^2)$
  then hinted by the ans, $\sum_{k=1}^{t-1}(2k^2+k)+t*(m-(t-1)^2)\blacksquare$
  - see the ans here should be $t*(m-t^2+1)$ where 
    $t^2$ means the start index of $\lfloor\sqrt{m}\rfloor$
    and $+1$ means take in account the integer index $\lfloor\sqrt{m}\rfloor^2$.
- [x] 44 similar to 43.
### 2.5
- ~~TODO~~ why THEOREM 2, i.e. exercise 41, can't be proven using $a\le b,b\le a\Rightarrow a=b$?
  see example 6 where uncountable, so $|A|$ is not one number at all.
- [ ] 2
  a. countably infinite. $f(n)=n+10$
  b. countably infinite. $f(n)=-2n+1$
  c. finite
  d. uncountable, similar to the above [Cantor_diagonal_argument_string]
    then $(0,1)\subset(0,2)$, so also uncountable for the latter
  e. countably infinite
    $$
    \begin{equation*}
      f(n)=
      \begin{cases}
        (2,\frac{n+1}{2}),n\text{ is odd}\\
        (3,\frac{n}{2}),n\text{ is even}\\
      \end{cases}
    \end{equation*}
    $$
  f. countably infinite $f(n)=10n$
  - better use "one-to-one correspondence" symbol $\leftrightarrow$
    although by p204 write in sequence $f(n)$
    - f. notice the negative ones.
- [ ] 4
  a. subset of integers -> countable by exercise 16 or example 5.
    $f(n)=3*\lfloor\frac{n-1}{2}\rfloor+n\%2$
  b. similar $\text{but not } k\Rightarrow (k*\lfloor\frac{n-1}{k-1}\rfloor+n\%(k-1))$
    so $f(n)=5*(k*\lfloor\frac{n-1}{k-1}\rfloor+n\%(k-1)),k=7$
  c. since only one digit is allowed, so "Cantor's diagonalization argument" doesn't apply.
    - countable infinite
      here I only gives the sequence pattern $\{1,11,1.1,111,11.1,1.11,\ldots\}$

  d. similar to c
    $\{1,9,11,1.1,99,9.9,19,1.9,91,9.1,\ldots\}$
    number count sequence of the same pattern: $1*(2^1),2*(2^2),3*(2^3)$ where 
    $i*$ means (c) pattern number
    $2^i$ means possible ~~combination~~ types of i-length digit string if only 2 digit numbers are allowed.
  - ans
    - similar to 2, negative ones need to be considered.
    - c. needs [$.\overline{1}$](https://math.stackexchange.com/a/1309970/1059606)
    - d. is **not similar** to c
- [ ] 6
  move to the next odd number
  - see the ans
    here doesn't tackle with the new added guest when already only even
    but from the original to only even.
- [ ] 8
  do as example 2 does "countably infinite" times
  - ans is related with 6.
- [ ] 9 similar to 8
  the above three move processes are similar to how the **turing machine** works by step-by-step running.
  - the ans maps all to the even number
- [x] 10 
  $B=\mathbf{R}$
  a. $A-B=\{"a"\}$
  the rest are similar.
- [x] 12
  $A \subset B\Rightarrow A\to B\text{is one-to-one}$
- [ ] 14
  $|A|=|B|\blacksquare$
  - notice the infinite set.
    [See](https://math.stackexchange.com/a/4804634/1059606) where $\mathfrak{n}_100$ is due to the [generalized](https://en.wikipedia.org/wiki/Continuum_hypothesis#The_generalized_continuum_hypothesis) continuum hypothesis.
- [ ] 15 contradiction
  - see the ans use ordered list (i.e. sequence) to prove.
- [ ] 16 contradiction that subset can't be listed but the superset can.
  - better direct proof which is similar to 15
- [ ] 18 based on the one-to-one correspondence definition.
- [ ] 20 just use the one-to-one correspondence chain
  - see the ans for the more formal description.
- [ ] 22 [$|A|\ge |B|$](#onto_compare_cardinality) and 
  ~~countable of A -> $|A|\in \mathbf{N}$~~
  - see the ans countable infinite won't imply $|A|\in \mathbf{N}$
    but map $\mathbf{Z^+}\to A$ (see this as indexing one infinite series)
    - it uses onto from $\mathbf{Z^+}$ to the target, so the target size must be
      $\le\mathbf{Z^+}$ -> countable.
  - ~~TODO similar to mapping $\mathbf{Z^+}\to B$, is mine solution right?~~
    see the p203 definition, "has the same cardinality as the set of positive integers" means that we must show explicity **equal**
    - also [see][comparison_of_cardinality_for_infinite_must_use_onto_and_one_to_one]
      > When working with infinite sets there is very little reason to think that any coherent notion of "size" exists in the first place.

      comparing two countable infinite sets $A,B$ by $|A|\ge |B|$ is no use.
  - see p204 here more strictly $g$ is one-to-one correspondence, but onto is enough to construct the sequence.
- [ ] 24
  suppose $\exists A,|A|\le |\mathbf{Z^+}|\text{ by one-to-one}$ then how to prove 
  $|A|\neq |\mathbf{Z^+}|$?
  - see the ans
    - the problem needs to prove impossibility of $<$ instead of possibility of $<$
      so maybe should prove $|A|= |\mathbf{Z^+}|$ 
      (since $<$ is excluded) or 
      $|A|> |\mathbf{Z^+}|$
    - after being hinted, use $\mathbf{Z^+}$ to index (one-to-one map)
      $A$, then $|\mathbf{Z^+}|\le|A|$
      - This is same as $g(n) = f^{−1}(m) =k\in A,\text{here k is unknown}$
        - where "$n^{th}$ smallest element" sequence means injective and the infinite length of the sequence means [surjective](https://en.wikipedia.org/wiki/Bijection,_injection_and_surjection), so bijection -> $|A|=|\mathbf{Z^+}|$
    - the key idea is the indexed sequence by $\mathbf{Z^+}$
- [ ] 25
  just similar to index with positive numbers
  $K\to S$ is one-to-one due to "where *no two* elements of S have the same label"
  then $\mathbf{Z^+} \to K$ is also one-to-one for the same reason $\blacksquare$.
  - see the ans
    - the a finite string of keyboard characters $K$ is not finite but infinite countable due to **maybe infinite length**.
      countable because for each length-$k$ we can list $24^k$ which is finite -> infinite series/sequence -> countable.
- [ ] 26 
  ~~by using key "0~9" and "." which are "a finite list characters" to construct "a finite string of keyboard characters", then one-to-one map to $\mathbf{R}$~~
  above is not always one "finite string".
  - hint has finished the proof by chaning the above strikethroughed ones to the context of "0~9" and "/".
    - see the ans "negative" -> "-"
- [ ] 27
  $A_1,A_2-A_1,\ldots,A_n-\sum_{k=1}^{n-1}A_{k}$
  this sequence each $A_i$ can be listed, then $A_n-\sum_{k=1}^{n-1}A_{k}$ can also be listed, so the sequence can be listed
  $\blacksquare$
  - the ans just uses another list method similar to 2.5-4.
- [ ] 28
  write them in one matrix
  then zigzag similar to 2.5-4,27.
  - see the ans using 27 directly.
- [ ] 29 using 25 with "0,1".
  compared with here, [Cantor_diagonal_argument_string] can always add one new element by **appending digit "1"** to $s$ to differentiate with all the rest due to the property of infinity.
  - the ans just use $\underset{i=1}{\overset{n}{\bigcup}} S_i,|S_i|=2^i$
- [ ] 30 
  similar to 28 $S={(a,b,c)|a\neq 0}\subset \mathbf{Z^+}\times\mathbf{Z^+}\times\mathbf{Z^+}$ is ~~finite~~ countable.
  then for each $(a,b,c)$, max 2 solutions construct the solution set
  $T={x_1,x_2}$
  - so a union of $|S|$ number of 
    $T_i$, by exercise 27, countable. 
  - see the ans it just reprove 28 by 27
- [x] 31
  one-to-one is trivial
  onto:
  $$
  \begin{align*}
    \text{1. let } m+n=2t+1,t\in\mathbf{N}&\Rightarrow m\in(0,2t+1)\\
    f(m,n)=t(2t-1)+m\in(2t^2-t,2t^2+t+1)&\Rightarrow f(m,n)\in[2t^2-t+1,2t^2+t]\\
    \text{2. let } m+n=2t+2,t\in\mathbf{N}&\Rightarrow m\in(0,2t+2)\\
    f(m,n)=t(2t+1)+m\in(2t^2+t,2t^2+3t+2)&\Rightarrow f(m,n)\in[2t^2+t+1,2t^2+3t+1]\\
    \text{3. since when }m+n=2(t+1)+1&\Rightarrow f(m,n)\in[(t+1)(2(t+1)-1)+1,(t+1)(2(t+1)+1)]\\
    &\Rightarrow f(m,n)\in[2t^2+3t+2,2t^2+5t+3]\\
    \text{notice here }2t^2+3t+2\text{ is after }2t^2+3t+1,\text{,then the sequence is constructed beginning from }1&\tag*{$\blacksquare$}\\
  \end{align*}
  $$
  - the ans doesn't prove by cases, which is more elegant.
- [ ] 32
  $(3n + 1)^2\in{1,16,7^2,\ldots}$ which lacks many numbers, how to achieve as the problem says?
  notice here is one-to-one but not onto, so $\blacksquare$
  - see the ans for the strict proof which use three cases including one case that one is negative and one not.
    better use the other two cases that 
    1. both nonnegative.
    2. both negative.
    ~~here $(3n + 1)^2$ is monotonically increasing for $\mathbf{Z}\to\mathbf{Z^+}$, i.e. one-to-one.~~
  - $\mathbf{Q}\times\mathbf{Q}\to\mathbf{Q}$ is obvious by using the one-to-one map $S=\mathbf{Q}\to\mathbf{Z^+}$ which is obtained from the index due to the countability of 
    $\mathbf{Q}$
    then the composite $S\times S$ is also one-to-one
    - TODO [this](https://mathoverflow.net/a/228288) offers one explicit equation, referenced in [this](https://math.stackexchange.com/questions/1061115/on-the-problem-of-polynomial-bijection-from-mathbb-q-times-mathbb-q-to-math#comment2159965_1061115) stating that the bijection is much nontrivial.
      - > That problem has a negative solution: *no algorithm* can take a polynomial and determine whether it has integer roots.
        > The *undergraduate*-level references for this seem *limited*. Most papers on H10Q approach it differently, via Diophantine definitions of the integers in the rationals, so they motivate this problem but don't help to solve it.
- [ ] 34
  - [x] a. $f(x)=\frac{1}{2}(\frac{1}{x}-\frac{1}{1-x})\Rightarrow f'(x)=\frac{1}{2}(-\frac{1}{x^2}-\frac{1}{(1-x)^2})$, so one-to-one
     then use $\lim$ to prove onto, i.e. codomain is $\mathbf{R}$.
  - [ ] b. use above $f(x)$ and 
    $g(x)=\frac{2}{\pi}*arctan(x)$
    - see the ans whose codomain is the subset of $(0,1)$
      the above codomain is $(-1,1)$
      so it should be $g(x)=\frac{1}{\pi}*arctan(x)+\frac{1}{2}$ <a id="map_R_0_1"></a>
- [x] 35 is just [Cantor_diagonal_argument_string]
  - > Represent a subset of the set of positive integers as an infinite bit string with ith bit 1 if i belongs to the subset and 0 otherwise.

    this is trivial by the bit string definition.
  - > Suppose that you can list these infinite strings in a sequence indexed by the positive integers.

    is due to the assumption of that the conclusion is right.
    > Assume that there is such a one-to-one correspondence.
  - the rest see the above link and [this](#binary_string_0_1) for the binary string set to $(0,1)$.
- [ ] 36
  - the wikipedia proof is similar to the ans after "There is one technical point here"
  - then $S={x|x\in(0,1)}|,\aleph_0\overset{\text{exercise 35 due to "cannot appear"}}{\lt}\mathcal{P}(\mathbf{Z^+})| \xlongequal{\text{exercise 36}}|S|\xlongequal{\text{exercise 34}} |R|$
  - the ans
    - > We can encode subsets of the set of positive integers as strings of, say, 5’s and 6’s
      similar to 35 0/1
    - [Terminating](https://www.cuemath.com/numbers/terminating-decimal/) Decimal Definition
      > A number has a terminating decimal expansion if the digits after the decimal point terminate or are *finite*
      - [proof](https://math.stackexchange.com/questions/1404291/whether-a-real-number-is-a-dyadic-rational-iff-its-binary-expansion-terminates#:~:text=A%20real%20number%20is%20a%20dyadic%20rational%20if,if%20its%20binary%20expansion%20terminates.&text=Since%20this%20is%20base%2D2,x%20is%20a%20dyadic%20rational.) where
        1. "if" just use the definition
        2. "only if" uses $|a|\neq+\infin$
        > Another equivalent way of defining the *dyadic* rationals is that they are the real numbers that have a *terminating* binary representation
      - TODO [$0.d_1\ldotsd_{n−1}\overline{1}$](https://math.stackexchange.com/questions/1641233/what-points-in-0-1-will-have-two-binary-expansions#comment3346986_1641252) is recurrent by [definition](https://en.wikipedia.org/wiki/Repeating_decimal), see 
        $\frac{593}{53}$
        - this is also shown in the ans
          > we can *decide* to always *use* the terminating form
- [ ] 37
  > a string of symbols from a finite alphabet
  similar to 29, here the string is obviously finite to be stored on the computer.
  then the number is $\underset{i=1}{\overset{n}{\bigcup}} S_i,|S_i|=26^i$ by changing 2 to 26.
  - ans
    - > all computer programs in a particular language is a *subset* of the set of all strings of a finite alphabet
      because *valid word strings* are limited.
      - > which is a countable set by the result from Exercise 16, it is itself a countable set
        should be 
        > which is a countable set, it is itself a countable set by the result from Exercise 16
- [ ] 38
  > associating to the real number $0.d_1 d_2 \ldots d_n \ldots$ the function f with $f (n) = d_n$
  this map $(0,1)\to f$ is one-to-one trivially ~~even for binary decimal representations $0.1\overline{0}$ and $0.0\overline{1}$~~
  - it must be onto to the *subset* $S$ of the set of all functions $T$.
  - then $|\mathbf{R}|=|S|<|T|$ so T is uncountable.
  - as the ans said, here must forbid one of $0.1\overline{0}$ and 
    $0.0\overline{1}$
    since $0.1\overline{0}=0.0\overline{1}\Rightarrow f(0.1\overline{0})\neq f(0.0\overline{1})$ contradict with the function inherent property that each preimage has one **unique** image.
- [x] 39
  "com-puter program" number is countable, i.e. the set $S$ of com-puter programs.
  but the subset $T$ corresponding to 38 in the set $V$ of all functions may be not countable.
  then $|S|<|T|<|V|$ 
  so the onto map from $S$ to $V$ is unavailable.
  - > We say that a function is computable if there is a com-puter program that finds the values of this function
    > Consequently, there are only a countable number of computable functions
    so for the set $P$ of computable functions, i.e. com-puter program that finds the values of one function, $|P|<|S|$.
- [ ] 40
  hint's proof
  $\text{suppose }f(s)=T\Rightarrow \exists s\in T=f(s),s\notin f(s),\text{ then contradiction}\blacksquare$
  this proves $f$ exists that doesn't map to $T$, but how to prove that no $f$ can't map to $T$?
  - after hinted by the ans
    just use the above for each $f$, then always $\forall f:S\to \mathcal{P}(S)\exists T\in \mathcal{P}(S),f\not\to T,\text{ f is not onto}\blacksquare$
  - see the ans
    [comparison_of_cardinality_for_infinite_must_use_onto_and_one_to_one] shows not onto doesn't mean the opposite $|S|\le |\mathcal{P}(S)|$
    - here should be $|S|\neq |\mathcal{P}(S)|$
  - this is same as the wikipedia [proof](https://en.wikipedia.org/wiki/Cantor%27s_theorem#Proof), see "Equivalently, and slightly more formally" if having questions after reading the proof.
- [ ] 41
  1. $\forall a\in A$
    based on the assumption, let $a$ be the first the element, then because both $f$ and $g$ are injective, so the sequence is [well-defined](https://en.wikipedia.org/wiki/Well-defined_expression) which is same as what [Schröder_Bernstein_theorem] shows where [the partition](https://en.wikipedia.org/wiki/Partition_of_a_set#Examples) imply this.
    > A function is well defined if it gives the same result when the representation of the input is changed *without changing* the value of the input
    - the ans
      > Thus, if x is in both the chain generated by y1 and the chain generated by y2, then the chain generated by y1 and the chain generated by y2 are both the same as the chain generated by x and are therefore the same chain.
      here suppose $y_1$ and $y_2$ are two different chains, i.e. $x$ in two different. Then based on $x$ conversely (see book p32 for "converse" meaning), they should be same, contradiction $\blacksquare$.
  2. first split into ending or not
    then not ones is splitted into definite or not.
    ending ones trivially end with $A$ or $B$
    For infinitely not ending, think as $f:a_i\to b_i+1,g:b_i+1\to a_i+1,i\in \mathbf{N}$, then one infinite sequence is constructed.
    - the ans
      > if there is a b ∈ B with g(b) = a
      implies loop possibility (type 1)
      this just means backward to self.
      - > g may not be a surjection
        implies possible stopping, also maybe all not stopping. (type 2)
        > This means that there are injections $f : A\to B$ and $g : B\to A$
        since their statuses are same. both A and B are possible to end at. (type 3,4)
  3. 1,4 is trivial because of existence
    - based on d,e. This function selection is due to
      1. type 4 with $g^{-1}(a)$ 
        is to select the end element $b\in B$ of type 4 when **onto**
      2. similarly type 3 must be with $f(a)$ to map the end element 
        $a\in A$.
      3. the rest can be either $f$ or $g$ because both side (forward/backward) can be run.
        This is also shown in [Schröder_Bernstein_theorem]
  4. by injection of $f$ 
    and partial function $g^{-1}$ (this line is hinted by the ans) <a id="injective_f_g_inverse"></a>
    - the ans use (a) result
      $$
      \text{suppose not one-to-one, then }\exists a_1,a_2\in A\exists b\in B a_1\neq a_2\ni h(a_1)=h(a_2)=b\\
      \text{then }b\text{ is in two different chains, contradiction}\tag*{$\blacksquare$}
      $$
      - similar to e, since A can be always inside the chain (1,2,4) or at the end (3), so forward always works.
        i.e. use the injective property $f$
    - ~~since 3 has taken all $a$ in account, so $h(a)$ must exist without caring about whether $h(a)$ has its meaning,~~
      ~~which is different from 5 where it begins from $B$, so two cases must be separate to solve with.~~
      since one-to-one needs to prove $\forall x_1\neq x_2,h(x_1)\neq h(x_2)$, so no need to care about the detailed infos about 
      **what is exactly $x_1,x_2$**,
      but onto needs to prove $\forall y,\exists x,h(x)=y$ this needs **exact** equation of $x$ <a id="comparison_proof_onto_with_one_to_one"></a>
  5. type 4 is enough because $g$ is injective so **partial** function $g^{-1}$ is onto.
    ~~so p207 is based on the strict total function shown in p170 [default_total_function](#default_total_function)~~
    ~~> However, this is not the case because when you have an injection from a set A to a set B *that may not be onto*, and another injection from B to A that also may not be onto~~
    - the above is wrong because not use one same single function definition of $h$ with (d),(e)
      see the ans
    - the ans just use the chain locality
      where 1~3 doesn't ends with B, so backward or forward.
      4 ends with B, so the end is backwarded from $g(b)$ with $g^{-1}$ to get.
  - after hinted by this solution
    This is wrong [see](#care_about_construction_of_func) 
    $$
    \text{here }g^{-1} \text{ first to make onto can take effect, otherwise }\quad f\quad\text{ always has its definition , then }g^{-1}\text{ can't take effect.}\\
    \begin{equation*}
      h(x)=
      \begin{cases}
        g^{-1}(x)&\text{if this \textbf{partial} inverse function has definition at}\quad x,\text{mark this as}x\in S,f(S)=T\\
        f(x)&\text{otherwise}
      \end{cases}
    \end{equation*}
    $$
    - one-to-one
      1. if both $x_1,x_2\in S\vee x_1,x_2\in A-S$, then by [this](#injective_f_g_inverse), they are one-to-one
      2. WLOG, if $x_1\in S,x_2\in A-S$, suppose $f(x_2)=g^{-1}(x_1)\in T$ then $x_2$ should be in $S$ because it is mapped to $T$, contradiction
        - This is wrong, although this contradiction is right, but the above $g^{-1}$ is wrong because it has priority of <a id="care_about_construction_of_func"></a>
          $g^{-1}$ over $f$ and doesn't make sure that they don't overlap.
          See [Schröder_Bernstein_theorem] example [1](https://en.wikipedia.org/wiki/Schr%C3%B6der%E2%80%93Bernstein_theorem#Examples) where $C_k$ ensures non-overlap which is just ~~B~~A-stopper because it can only starts from $[0,1]$ which is f domain.
          ~~This implies A/B-stopper has the priority over the doubly infinite.~~
      with 1,2 $\blacksquare$
    - onto
      $g^{-1}$ is enough to map to all $B$.
      ~~this also shows that the above $f(x)$ is **fake** which can't happen here.~~
    - here we can also use the graph similar to [2_3_37] to help understanding this problem.
  - this one is same as [wikipedia][Schröder_Bernstein_theorem]
    - TODO meaning
      > each a in A and b in B is in exactly one such sequence to within identity
    - the book problem definitions of A-stopper and B-stopper are same as here where both cares about the **very beginning** one.
    - it shows bijection by using partial $f^{-1}$ and 
      $f$
      > between its elements in A and **its** elements in B.
      - so with *all* three cases, then the *partial* ones can be combined to get the *onto* although this isn't said explicitly.
    - the figure shows onto with $a\sim f$
### 2.6
- most of them are skipped because I have learnt linear algebra.
  2~16,
  20~28
  32~34 skipped
- [ ] 17 b after hinted
  here $\sum_{q}b_{qi}a_{jq}$ is based on $B=[b_{ji}]$
  $[\sum_{q}a_{jq}b_{qi}]=[c_{ji}]\xlongequal{\mathbf{AB}=[c_{ij}]}(\mathbf{AB})^t$
- [ ] 18 notice both sides or use the $\mathbf{A}^{-1}$ definition.
- [ ] 30 notice $\mathbf{A}\wedge\mathbf{B}$ or 
  $\mathbf{A}\vee\mathbf{B}$ don't need $\mathbf{A,B}$ to be the square.
### Supplementary
- 4,38 skipped
  the following without "see the ans" and the tick default to need to see the ans, e.g. 10.
- [x] 2
  $$
  \forall a\in A\Rightarrow a\in B\\
  \forall S\in \mathcal{P}(A),(\forall k\in S\Rightarrow k\in A\Rightarrow \exists T\in\mathcal{P}(B),k\in T)\tag*{$\blacksquare$}
  $$
  (this one is not strict because that $T$ is one-to-one map from $S$ is not shown.)
  or based on power set definition
  or based on this [$\Leftrightarrow$](https://en.wikipedia.org/wiki/Power_set), this is same as the ans says.
  $$
  \forall S\in \mathcal{P}(A)\Leftrightarrow S\subseteq A\subseteq B\Leftrightarrow S\in \mathcal{P}(B)\\
  \text{then } \mathcal{P}(A)\subseteq \mathcal{P}(B)
  $$
- [ ] 6
  - see the ans for how to use the description of words as the media to prove.
- [ ] 8 removal order doesn't influence the result.
  - similar to 6 see the ans
- [ ] 10 use $\le B\le$ as the media
  then the second $\le$ only becomes $=$ when 
  $A=B$.
- [x] 12
  by definition, $|\overline{A}\cap\overline{B}|=|U-A-B| \xlongequal{\text{principle of inclusion–exclusion}} \text{right-side}$
- [x] 14 [see](#default_total_function), because $\forall x\in S\exists \text{ unique } y\in f(S)\ni y=f(x)$
- [ ] 16
  as the problem says, p172 definition 4 use the same $f$ for different domains,i.e. both $A\to B$ and $\forall S\subset A \exists T\subset B,S\to T$
  the following ~~is based on that *both domains conform to* the one-to-one property of $f$, etc,~~ ~~which is trivial due to $f(S)=f(\cup s_i)=\cup f(s_i)=\cup t_i=T$~~ ~~see~~ a,b proves that $f(x):A\to B$ and $S_f(X) = f(X)$ have the **same** property w.r.t. one-to-one and onto where they use only the property of 
  $f(x)$ but not $f(X)$.
  a. let $X=\cup a_i$
    then $S_f(X)=f(X)=f(\cup a_i)=\cup b_i$
    - see the ans which focus on one specific element.
  
  b. $\forall X_2\exists X_1,f(X_2)=X_1=S_f(X_2)\blacksquare$
    - better see the ans where doesn't use the **direct generalization** the onto to the function of one *set*
    - $ X = \{ x \subset A | f(x) \subset Y \}$ implies $S_f (X) \in Y\Rightarrow S_f (X) \subset Y$
      - $ X = \{ x \subset A | f(x) \subset Y \}$
        it is due to the onto property, so each $f(x)$
        must have at least one corresponding $x$
        - but see p186 definition, it allows more than one $x$.
      - here doesn't imply because if $f(x)$ is not onto, then
        $\exists y\in Y,\nexists x\in A\ni f(x)=y$
        which is just what the $ Y \subseteq S_f (X)$ says.
    - here there is no way for $f(x)=Y$ to be in the set definition $ X = { x \in A | f(x) \in Y }$ 
      since the problem only shows "f is a function from A to B" but not "f is a function from $\mathcal{P}(A)$
      to $\mathcal{P}(A)$", 
      so the domain w.r.t. $x$ and $X$ are **not same**.
    - $S_f(a)=f(a)=b\wedge a\in X\Rightarrow b\in S_f(X)$
  
  c. ~~TODO $f^{-1}$ may not exist if not one-to-one correspondence.~~
    - the ans
      See p186 where the definition is "precisely *all preimages* of all elements of S".
      So $a\in S_{f^{-1}}(Y_1)=f^{-1}(Y_1)$ means a is one **preimage** of 
      $b\in Y$.
      - $Y_1\neq Y_2\Rightarrow f^{-1}(Y_1)\neq f^{-1}(Y_2)\Rightarrow S\subset Y_1-Y_2\ldots?$
      - The onto ensures $f^{-1}(Y_1-Y_2)\neq\varnothing\Rightarrow f^{-1}(Y_2+(Y_1-Y_2))=f^{-1}(Y_1)\neq f^{-1}(Y_2)$
      - intuitively but not strict (at least for the uncountable infinite set)
        $f:A\to B\text{ is onto}\Rightarrow |A|\ge|B|\Rightarrow |B|\le|A|\Rightarrow f^{-1}:B\to A\text{ is one-to-one}$

  d. similar to b
    $$
    \begin{align*}
      \text{we claim that }\quad&\forall X\in B,\exists Y=f(X)\Rightarrow S_{f^{-1}}(Y)=X&\\
      \text{1. trivially, }X\text{ is mapped from }A\text{ to }B\text{ by }f\text{, then back by }S_{f^{-1}}\quad&S_{f^{-1}}(Y)\supseteq X&\\
      \text{2. suppose }\quad&\forall a\in S_{f^{-1}}(Y)\Rightarrow a\in f^{-1}(Y)&\\
      \text{due to one-to-one of }f\quad&a\in X&\text{otherwise, }\exists b\in Y a_1\in X a=a_2\notin X\ni f(a_1)=b,f(a_2)=b,\text{ contradiction with one-to-one}\\
      &\Rightarrow S_{f^{-1}}(Y)\subseteq X&\\
      \text{based on 1. 2. ,}\quad&S_{f^{-1}}(Y)= X&
    \end{align*}
    $$
    - the ans
      ${u \in A |f(u) \in {f(x) |x \in X }}$ is based on one-to-one property because $Y = {f(x) | x \in X }$ maps each 
      $x$ to one unique $f(x)$, similarly for the former, each 
      $f(u)$ is mapped to one unique $u$, so one-to-one
- [x] 18,22 prove by two cases
- [ ] 20
  let $\{x\}$ be the [fraction part](https://en.wikipedia.org/wiki/Floor_and_ceiling_functions#Notation).
  - hinted by the ans
    notice here should both use [$x-\lfloor x\rfloor$](https://en.wikipedia.org/wiki/Fractional_part#For_negative_numbers) to help generalize the ideas to negative from positive, then $\{x\}\in(0,1)$
    1. then if $\{x+y\}\in(0,1]$ then round up one
      both $\{y\}$ and $\{x\}$ will round up one -> $\neq$
    2. if $\{x+y\}\in(1,2)$ -> ok.
    - see the ans 
      for case 1 maybe $\{y\}$ or $\{x\}$ be 0, then equal.
- [x] 24
  similar to 20, let $\frac{x}{4}=n+\epsilon$, but here $\epsilon\in[0,1)$ 
  then the right side is $n$
  the left side is $\lfloor\frac{\lfloor 2n+2\epsilon\rfloor}{2}\rfloor=\lfloor\frac{2n\text{ or }2n+1}{2}\rfloor=n$
- [x] 26
  similar to 20,
  $x=k+\epsilon,\epsilon\in[0,1)$
  then it is to prove $t=n+k,\lfloor \frac{t+\epsilon}{m}\rfloor=\lfloor \frac{t}{m}\rfloor$
  since $m\ge 1\gt\epsilon\Rightarrow\frac{\epsilon}{m}\in[0,1)$
  to make $\frac{t}{m}$ to round up *another* one based on $\lfloor\frac{t}{m}\rfloor$, we need at least $\frac{1}{m}\gt\frac{\epsilon}{m}$, then it is impossible. $\blacksquare$
- [ ] 27
  similar to 20
  $\text{let }x=n+\epsilon,\epsilon\in[0,1),m\epsilon\in[k,k+1),\text{where }k\in\mathbf{N}\wedge k\in[0,m-1]$
  left side: $mn+k$
  right side: $\text{to let }\lfloor x+\frac{i}{m}\rfloor=\lfloor \frac{mn+m\epsilon+i}{m}\rfloor\text{ round up based on} n$
  we need $m\epsilon+i\ge m\Rightarrow k+i\ge m,i\ge m-k$, since $i$ stop at $n-1$ so there are $k$ right terms rounding up.$\blacksquare$
  - see the ans how to be tuned with this specific sum sequence.
    where small error: should be $\text{through }\lfloor x + (m - r − 1)/m\rfloor$
- [ ] 28
  pattern: $1\xrightarrow{}2\xrightarrow{+u_1}3\xrightarrow{+u_1}4\xrightarrow{+u_2}6\xrightarrow{+u_2}8\xrightarrow{+u_3}11\ldots$
  proof of this pattern:
  $$
  \begin{equation*}
    u_n=
    \begin{cases}
      u_{\frac{n-1}{2}}+u_{n-1},n \text{is odd}\\
      u_{\frac{n}{2}}+u_{n-1},n \text{is even}\\
    \end{cases}
    ,n\ge 3
  \end{equation*}
  $$
  without the proof let $u_{n+1}=u_{n}+u_{n-1},n\ge 3$ this is always one subset of Ulam numbers, which is infinite series,$\blacksquare$
  - this pattern is wrong, from [this](https://en.wikipedia.org/wiki/Ulam_number#Properties) maybe there is no well-defined function for this.
    TODO maybe [related](https://math.stackexchange.com/q/4199847/1059606)
- [ ] 30
  [see](https://testbook.com/question-answer/the-next-term-of-the-sequence-1-3-4-8-15-27--609237f563fb2bc627007d50)
- [ ] 31
  $$
  10=2*5\\
  13=3+10\\
  39=3*13\\
  43\neq 5+39\text{ here I start from 5th term, and associate with distance 3}
  $$
  - [see](https://www.european-rubber-journal.com/article/2093179/erj-brainteaser-april#:~:text=Question%203%3A%20What%20comes%20next,numbers%20are%20177%20and%20885.)
- [ ] 32
  since by [this](https://mathspace.co/textbooks/syllabuses/Syllabus-999/topics/Topic-19889/subtopics/Subtopic-263668/#:~:text=An%20irrational%20number%20is%20a,nor%20recurring%20are%20irrational%20numbers.), 
  so "A non-terminating, non-repeating decimal" is irrational, then by [Cantor_diagonal_argument_string] $\blacksquare$
  - notice [$\mathbf{R}=\mathbf{Q}\cup\mathbf{P}$](https://math.stackexchange.com/a/1435320/1059606), irrational [symbol](https://byjus.com/maths/irrational-numbers/#:~:text=Generally%2C%20the%20symbol%20used%20to,the%20real%20and%20rational%20number.)
  - see the ans $\mathbf{Q}$ is countable.
- [ ] 34 
  since the count of subsets with size $i$ is $|\mathbin{Z^+}|^i$
  - the above $|\mathbin{Z^+}|=\aleph_0$ so $|\mathbin{Z^+}|^i$ has no real meanings, see [comparison_of_cardinality_for_infinite_must_use_onto_and_one_to_one].
  - the ans first limit it to $S_n$.
- [ ] 35
  injection from $(0,1)$ to $(0,1)\times(0,1)$ is trivial by using $f:x\to(x,x)$
  - injection $R\to (0,1)$, etc see [2.5-34](#map_R_0_1) which uses the ans 
    $arctan(x)\ldots$, similarly for 
    $R\times R\to(0,1)\times(0,1)$.
  then the injection chain proves the theorem $\blacksquare$.
  - > do not end with an infinite string of 9s
    see 2.5-38 just forbid this pattern.
- [x] 36 $\text{since }\forall x=a+bi\in\mathbf{C},f:x\to(a,b)\text{ is one-to-one correspondence}\Rightarrow|\mathbf{C}|=|\mathbf{R}\times\mathbf{R}|\text{ with the 35 conclusion}\blacksquare$
## 3
### 3.1
- 4~ see the [pdf](https://www.overleaf.com/read/fbychkzpsrff#459790).
- [ ] 2
  a.
  - [x] input
  - [ ] output
  - [x] Definiteness
  - [ ] Correctness
  - [ ] Finiteness
  - [ ] Effectiveness
  
  b. TODO what does this purpose to do?
  - [x] input
  - [ ] output
  - [x] Definiteness
  - [ ] Correctness
  - [x] Finiteness
  - [ ] Effectiveness
  
  c.
  - [x] input
  - [ ] output
  - [x] Definiteness
  - [ ] Correctness
  - [x] Finiteness
  - [x] Effectiveness
  
  d.
  - [x] input
  - [ ] output
  - [ ] Definiteness
  - [x] Correctness
  - [x] Finiteness
  - [x] Effectiveness

  - see the ans where c is wrong.
- [ ] 6
  here $:=$ should be only used in the definition.
- [ ] 

---

[SOLUTIONS_8th]:./Discrete%20Mathematics%20and%20Its%20Applications,%20Eighth%20Edition%20SOLUTIONS.pdf
[SOLUTIONS_7th]:./discrete-structure-solution-student39s-solutions-guide_compress_7th.pdf
[A_Guide_to_Writing_Proofs]:./A_Guide_to_Writing_Proofs.pdf
[stirling]:./papers/stirling.pdf
[miscs_ipynb]:./miscs_snippets/miscs.ipynb

<!-- exercise help pdf -->
[2_3_37]:./latex_misc_pdfs/Discrete_Mathematics_and_Its_Applications_2_3_37.pdf

<!-- wikipedia -->
[Cantor_diagonal_argument_string]:https://en.wikipedia.org/wiki/Cantor's_diagonal_argument#Uncountable_set
[Schröder_Bernstein_theorem]:https://en.wikipedia.org/wiki/Schr%C3%B6der%E2%80%93Bernstein_theorem#Proof

<!-- math stackexchange -->
[comparison_of_cardinality_for_infinite_must_use_onto_and_one_to_one]:https://math.stackexchange.com/a/4804647/1059606