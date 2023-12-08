I can solve the above problem by another generating function form: 
$$
a(x)=\sum_{i=0}^n a_i x^i\\
xa(x)=\sum_{i=0}^n a_i x^{i+1}\\
x^2a(x)=\sum_{i=0}^n a_i x^{i+2}\\
(1-x-x^2)a(x)=a_0+(a_1-a_0)x=1+x\\
a(x)=\frac{1+x}{1-x-x^2}
$$
the form is same as the above one. But how does these two become same? Based on $a_1=2,a_2=3$, what does the above coefficient $1$ in $x$ and $x^2$ mean? Since $x^2=x*x$, does "0" and "01" also has this relation? And what does the ending "removing the rightmost '0'" mean?

@Henry Thanks for your comments. With your clarification help, I found my original generating function reference link may not fit in this specific problem. Then I refer to [this about Generating Function for recurrence](https://math.libretexts.org/Bookshelves/Combinatorics_and_Discrete_Mathematics/Combinatorics_(Morris)/02%3A_Enumeration/08%3A_Generating_Functions_and_Recursion/8.03%3A_Using_Generating_Functions_to_Solve_Recursively-Defined_Sequences).

1. Yes. It seems these two generating functions are different. Since in my above equations which is based on the original answer link "Recurrence" part referenced in the question, I let $a_0=1$ and $a_1=2$ which corresponds to "0" and "1". Then $a_2=3$ corresponds to "10","01","00". Then could you say in detail how the above $x+x^2$ deals with length 3 maybe and $(x+x^2)^2$ deals with length 6 maybe (why can we multiple $x+x^2$ to get the corresponding coefficients $a_i$ here)? And why does $x$ and $x^2$ both has coefficient "1" when length 1 and length 2 have more than 1 related strings? Thanks beforehand.

2. After expanding $\frac{1+x}{1-x-x^2}$, it is $1+2x+\ldots+8x^4$ which doesn't multiple $\frac{1}{x}$, so why does the answer emphasize that $\frac{1}{x}$ corresponds to "removing the rightmost '0'"?

check p10 whether the ideas of each chapter are mastered.
# outline
much of chapter 2,5,6 have been learned before.
# [online resources](https://highered.mheducation.com/sites/125967651x/student_view0/web_resources_guide.html) from [this](https://highered.mheducation.com/sites/125967651x/information_center_view0/)
- Discrete Mathematics and Its Applications [Student’s Solutions Guide](https://www.academia.edu/36410920/Students_Solutions_Guide) pdf with the unavailable version.
- [test bank](https://www.stuvia.com/en-us/doc/2018491/discrete-mathematics-and-its-applications-8th-edition-rosen-test-bank.pdf)
# markdown notice
- "- [ ]" can't be ended with one space.
- not use number bullet list inside "-" bullet list which may be changed to "a,b,c"
- use number bullet list instead of "a,b,c" to help the indentation.
# miscs
- Linux soft link should [not use relative path](https://www.baeldung.com/linux/too-many-levels-of-symlinks)
```bash
$ ln -s latexindent_pl.yaml miscs_learning/latexindent_pl.yaml
$ ls miscs_learning/latexindent_pl.yaml                       
ls: cannot access 'miscs_learning/latexindent_pl.yaml': Too many levels of symbolic links
$ tree --noreport -fp
├── [drwxr-xr-x]  ./miscs_learning
...
# this means self "./miscs_learning/latexindent_pl.yaml" based on the relative path
│   └── [lrwxrwxrwx]  ./miscs_learning/latexindent_pl.yaml -> latexindent_pl.yaml
# should use the absolute path.
$ ln -s $(pwd)/latexindent_pl.yaml miscs_learning/latexindent_pl.yaml
```
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
## book recommendation
- [KlTa05] algorithm design which referenced in p260.
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
  > referring to The Art of Computer Programming, has come to mean the reference that answers all questions about such topics as data structures and algorithms.
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
- the bubble sort just uses the pair chains to select the **maximum** in the list in each pass, so $i$ plus one and $j$ minus one in each pass in ALGORITHM 4.
- the [insertion sort](https://en.wikipedia.org/wiki/Insertion_sort#Best,_worst,_and_average_cases) just tracks one more item which creates one ordered sublist beginning from the first item.
  the 2nd ~~is similar to the 1st except that it moves `x` directly to the correct place instead of propagating (the swap counts are same).~~ avoids many unnecessary swaps which uses 3 assignments by using all one assignment each time with one additional $x \leftarrow A[i]$ which is same as ALGORITHM 5 does.
  the 3rd is the recursive version of the 2nd.
- ~~TODO~~
  since "ALGORITHM 3" $j\coloneqq m$ doesn't exclude one element.
  > The search has now been restricted to a list with no more than $\lceil n/2\rceil$ elements
  if n is odd, then after comparison, either $\frac{n+1}{2}=\lceil n/2\rceil$ or $\frac{n-1}{2}$ is left
  if n is even, ~~either~~ $\frac{n}{2}$ ~~or $\frac{n}{2}-1$~~ is left.
  - based on the above,
    p256 when n is odd, it may be always leave more than half elements, i.e. $\frac{n+1}{2}$
    so it may use $\lceil \log{n}\rceil$ comparisons.
### 3.2
- p241 $f=O(g)\wedge g=O(f)$ is possible, so relations in p247 need to be separately proven.
- p251 THEOREM 4
  similar to EXAMPLE 13, $x^n=O(f)$ is trivial. Then with THEOREM 1, proof finished.
- Notice $\log=\log_2$
- Since we only care about discrete maths, no fraction exponents, etc, are taken in account.
### 3.3
- EXAMPLE 2 is based on the Short circuiting, so $2i+1$.
- p258 should be $O(n^{\log[2]{7}})$
- P [diffs](https://en.wikipedia.org/wiki/NP_(complexity)) from NP
  >  P (all problems *solvable*, deterministically, in polynomial time) is contained in NP (problems where solutions can be *verified* in polynomial time)
  - [NP-complete](https://en.wikipedia.org/wiki/NP-completeness#Formal_definition) is ~~one *class* of problems which are combined together~~ one problem can be reduced from **all** NP, 
    e.g. the Boolean satisfiability problem by [Cook–Levin theorem (TODO strict proof)](https://en.wikipedia.org/wiki/Cook%E2%80%93Levin_theorem#Proof), "thus equivalent to the P versus NP problem" (i.e. $P\overset{?}{=\mathrel{\mkern-3mu}=}NP$).
    > *Every* problem in NP is *reducible* to $\scriptstyle C$ in polynomial time
    implies
    > if *any* of these problems can be *solved* by a polynomial worst-case time algorithm, then *all* problems in the class NP can be *solved* by polynomial worst-case time algorithms
## 4
### 4.1
- Also see [csapp_doc] "modular_overflow" for relations between modular arithmetic and 2's complement.
- THE [WELL-ORDERING](https://brilliant.org/wiki/the-well-ordering-principle/#:~:text=The%20well%2Dordering%20principle%20says,integers%20has%20a%20least%20element.) PROPERTY
  - TODO [not well-ordered set](https://math.stackexchange.com/a/392861/1059606)
  - EXAMPLE 5 in p385 uses induction to make $r\ge d$ become $r<d$.
- > some of these operators are defined when m < 0, and even when m = 0
  for python, `10%(-3)=-2`. While for C, it uses [`cdq;idiv   DWORD PTR [rbp-0x4]`](https://www.felixcloutier.com/x86/idiv#operation) to calculate resulting in `10%-3=1`.
  - See the [list](https://en.wikipedia.org/wiki/Modulo#In_programming_languages) of these [differences](https://stackoverflow.com/a/3883019/21294350) and the python one is [used](https://stackoverflow.com/a/1907585/21294350) in the number theory.
- > 17-sided regular polygon could be drawn using just a ruler and compass
  how this is [related](https://crypto.stanford.edu/pbc/notes/numbertheory/17gon.html#:~:text=In%201796%2C%20a%20teenage%20Gauss,quadratic%20equations%20over%20the%20rationals.) with number theory?
- [mathematical analysis](https://en.wikipedia.org/wiki/Mathematical_analysis#Main_branches)
- > there is no multiplicative inverse of 2 modulo 6
  [TODO](https://math.stackexchange.com/a/2670313/1059606)
- TODO why define [Multiplicative group](https://math.stackexchange.com/a/135928/1059606)?
- [Commutative ring](https://en.wikipedia.org/wiki/Commutative_ring#Definition_and_first_examples)
  > To form a ring these two operations have to satisfy a number of properties: the ring has to be an abelian *group* under addition as well as a *monoid* under multiplication, where multiplication distributes over addition
  where "abelian group" is group with [Commutativity](https://en.wikipedia.org/wiki/Abelian_group#Definition) and group is the monoid with [inverses](https://math.stackexchange.com/a/146902/1059606)
### 4.2
- p286 ALGORITHM 1
  when $q=0$, $0|a_k\ldots$ is the final representation (here $|$ is one delimeter), so after 
  $k=k+1$, we need $a_{k-1}\ldots$ to get the final representation.
- p288 ALGORITHM 2 which uses $div$ and $\bmod$ has been said in COD which has one better algorithm and csapp.
- EXAMPLE 9 uses the cache to avoid duplicate calculation of $a_j+b_j+c$
- in 2019 after the book published in 2018, one better [algorithm](https://en.wikipedia.org/wiki/Multiplication_algorithm#Sch%C3%B6nhage%E2%80%93Strassen) to calculate multiply of n-bit numbers was devised.
### 4.3
- Yitang Zhang's [career](https://en.wikipedia.org/wiki/Yitang_Zhang#Career) is a bit hard when after PHD he can't find one job because of maybe failure of the PHD paper.
- > Any two prime numbers are relatively prime to each other
  relatively prime [relation](https://www.splashlearn.com/math-vocabulary/relatively-prime#:~:text=Example%3A%20(2%2C%203),prime%20numbers%20will%20be%201.) with prime
- extended Euclidean algorithm [proof](https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Proof) by "follows by induction".
### 4.4
- a modulo n, i.e. $a\bmod n$
- > $t \equiv 5 (mod 6)$ (as the reader should verify).
  see EXAMPLE 1
  $6=1*5+1\Rightarrow -1*5+6=1\Rightarrow -1*5\equiv 1\pmod 6$
  - similarly
    $30u + 26 \equiv 3 (mod 7) \Rightarrow 6u\equiv 1\pmod 7\xRightarrow{similar to above} -1*6\equiv 1\pmod 7$
- example 8 is based on 4.1 COROLLARY 2.
- >  they were *incorrect* in concluding that n is necessarily prime if the congruence holds
  this doesn't mean the congruence is necessary condition for that n is prime
  i.e. n is odd prime -> congruence. This is correct.
- THEOREM 1 [iff proof](https://math.stackexchange.com/a/2670313/1059606) based on the Bezout's theorem.
### 4.6
- > $f(p)=(ap+b)mod\;m$ is bijective if and only if $gcd(a,m)=1$

  based on [this](https://math.stackexchange.com/a/2034684/1059606)
  we prove $(ap)\mod m$ is bijective. ~~Based on this [description](https://math.stackexchange.com/q/4817093/1059606) of the comment,~~
  ~~since both the domain and the codomain are $\mathbf{Z}_m$, so onto is equivalent to one-to-one, then in turn equivalent to bijective, so it is enough to prove only injective.~~
  ~~Then by contradiction, $ap_1\equiv ap_2\pmod m,p_1\neq p_2\Rightarrow a(p_1-p_2)\equiv 0\pmod m\xRightarrow{p_1-p_2\nmid m}a\equiv $~~
  See [this](https://math.stackexchange.com/review/suggested-edits/2044757)
  $$
  \begin{align}
  &ax\equiv 0\,\xRightarrow{\text{has only one solution}}\, x\equiv 0\\
  \iff&\gcd(m,a)=1(\text{otherwise there are one solution}x=m/\gcd(m,a))
  \end{align}
  $$
- p335 affine transformation is one [linear](https://math.stackexchange.com/a/1059233/1059606) transformation
- permutation is one-to-one because its inverse can't be one-to-mul.
- Euler's totient function [proof](https://en.wikipedia.org/wiki/Euler%27s_totient_function#Proof_of_Euler's_product_formula)
  - [basis](https://en.wikipedia.org/wiki/Euler%27s_totient_function#Phi_is_a_multiplicative_function)
    based on the ~~book~~ [SOLUTIONS_8th] p111 table for Chinese remainder theorem ->  bijection.
    $f:(a,b)\text{with }a\equiv a\pmod m,b\equiv b\pmod n\to k\equiv k\pmod mn$
  - TODO use inclusion-exclusion principle.
  - so in RSA, coprime probability is [higher](https://crypto.stackexchange.com/a/25649).
    [~~TODO~~ $P^{\varPhi(N)}\equiv 1\pmod N$](https://crypto.stackexchange.com/questions/25648/how-do-we-guarantee-plaintext-is-coprime-in-rsa#comment58896_25648) (i.e. [${\displaystyle (m^{e})^{d}\equiv m{\pmod {pq}}}$](https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Proof_using_Fermat's_little_theorem)) also [see](https://crypto.stackexchange.com/a/1006)
- RSA
  - ~~TODO~~ [$\gcd(m,N)=1$](https://crypto.stackexchange.com/a/58182)
    > either p  and q , and so that rather *leaks* the factorization of N
  - why p339 $\gcd(e,(p-1)(q-1))=1$
    see [this](https://en.wikipedia.org/wiki/RSA_(cryptosystem)#cite_note-24) because if the above condition is met, then we can use the **decryption** easily.
    - TODO also [this](https://math.stackexchange.com/questions/1123180/understanding-why-the-public-exponent-e-is-chosen-the-way-it-is-in-rsa#comment2294881_1123643)
      where "an element x of order r" implies [$x^r=x^0=1$](https://en.wikipedia.org/wiki/Cyclic_group#Definition_and_notation) <a id="RSA_Cauchy_theorem"></a>
      It shows if the above condition is not met, then **one-to-mul decryption**.
    - here $m\equiv 0\pmod p$ is the cases where $\gcd(m,p)=1$ doesn't hold. <a id="RSA_m_not_coprime_n"></a>
  - $2525$ is to ensure [injective](https://math.stackexchange.com/a/1148743/1059606) which can be decrypted.
- p341 although in [Euclidean algorithm](https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Description), $a<b$, i.e. here $d<(p − 1)(q − 1)$, but in the practical case, it may be not that case.
- EXAMPLE 11
  multiplication->encryption is same as encryption->multiplication.
- cryptographic program [obfuscation](https://en.wikipedia.org/wiki/Obfuscation_(software)) schemes
- cryptographic multilinear map is one [special multilinear function](https://en.wikipedia.org/wiki/Cryptographic_multilinear_map#Definition).
- [verifiable](https://en.wikipedia.org/wiki/Verifiable_computing#Motivation_and_overview) computation
  > with the client being able to verify the proof with *significantly less* computational effort
## 5
- [weak induction](https://www.cs.cornell.edu/courses/cs2800/2015fa/lectures/lec18-euclid.html) which can be transformed to strong induction trivially.
  from 5.2 introduction, mathematical induction in the book is same as above.
### 5.1
- inductive reasoning [diff](https://www.scribbr.com/methodology/inductive-deductive-reasoning/#:~:text=What's%20the%20difference%20between%20inductive,general%20premises%20to%20specific%20conclusions.) deductive reasoning
  the former is based on "Seeking patterns" ~~which may be not dependable~~.
  - > whereas inductive reasoning makes conclusions *only supported*, but not ensured, by evidence
    see [this](https://www.linkedin.com/advice/3/how-do-you-use-deductive-inductive-reasoning-1e#:~:text=Inductive%20reasoning%20is%20a%20process,do%20not%20guarantee%20its%20truth.)
- "co" [meaning 4](https://www.merriam-webster.com/dictionary/co#dictionary-entry-5) in codomain and coprime
- Template for Proofs by Mathematical Induction
  1. "for all n $\ge$ b, P(n)" by choosing the correct $b$
  2. 
  3,4,5 Inductive Step
  6,7 always done similarly.
  - So only 3~5 are the key steps.
- EXAMPLE 13
  case i: Here we assume each person has one pie.
- > this step requires that $k\ge 3$
  because
  ~~> the first k ... $p_1$~~
  ~~> the last k of these lines meet in a common point $p_2$~~
  ~~if k=2, then ~~
  > $p_1$ and $p_2$ were different points, all lines containing both of them must be the same line because two points determine a line
  if k=2, then $p_1$ and $p_2$ may be shared by *only one* line, so it is ok for "them must be the same line".
### 5.2
- TODO is p384 the proof of lemma 1 really right?
  - here b is ~~both~~ the least y-coordinate ~~and~~ based on the smallest x-coordinate
- Well ordering principle is [not for real](https://people.eecs.berkeley.edu/~daw/teaching/cs70-s08/notes/n6.pdf) but for integer.
  its main idea is the **least** exists.
### 5.3
- [Well-formed formula](https://en.wikipedia.org/wiki/Well-formed_formula) is related with compiler.
- structural induction is just one special "mathematical induction"
  without using definition to prove like EXAMPLE 10.
  - > if the statement is true for each of the elements used to *construct* new elements in the recursive step of the definition
    the main idea is to find the way to construct.
### 5.4
- TODO special-purpose recursive machines, maybe [this](https://www.cis.upenn.edu/~alur/toplas2005.pdf)
- recursion algorithm in p387
  > requires $f_{n+1} − 1$ additions to find $f_n$

  let S(n) denote addition count to calculate $f_n$
  Then
  $$
  \text{based on }S(n)=S(n-1)+S(n-2)+1,n\ge 2\\
  \begin{align*}
    \text{BASIS STEP:}&S(1)=S(0)=0=f_1-1=f_2-1\\
    \text{INDUCTIVE STEP:}&S(n+1)=S(n-1)+S(n)+1=f_n-1+f_{n+1}-1+1=f_{n+2}-1
  \end{align*}
  $$
- iterative begins from $0$ with only one upward pass
  while recursion may have multiple passes.
### 5.5
- EXAMPLE 5
  $p\{S_1\}q$,$q\{S_2\}r$ is trivial
  $r\{S_3\}s$ -> ~~when out~~ after each iteration, $x=mk'+m=m(k'+1)=mk$ where $k'$ is the last iteration $k$.
  $s\{S_4\}t$ because $product=mn=m|n|\text{ when n is positive or }-m|n|\text{ when n is negative}$
## 6
### 6.1
- [class D](https://www.meridianoutpost.com/resources/articles/IP-classes.php) class E ipv4
### number theory
- [Combinations with repetitions](https://math.stackexchange.com/a/128064/1059606) allowed
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
- frac in [big](https://tex.stackexchange.com/a/103358/308105) ceil
- mod [without](https://tex.stackexchange.com/a/169946/308105) leading space
- [sum multiple-lines](https://tex.stackexchange.com/a/80461/308105)
- [bmod -> binary mod](https://tex.stackexchange.com/a/42872/308105)
- [big equal sign](https://tex.stackexchange.com/a/35406/308105) needs extra package or self define length `\mathrel{\mkern-3mu}`.
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
  - > such macro names are automatically *protected* from regular users
    purpose
  - It is related with [`\catcode``](https://en.wikibooks.org/wiki/TeX/catcode) which is more convenient than the bare [`\catcode`](https://tex.stackexchange.com/a/3339/308105).
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
- check the package specific command definition with [`latexdef --package amsmath -f cases`](https://tex.stackexchange.com/a/591894/308105)
- why use [`\displaystyle`](https://www.overleaf.com/learn/latex/Display_style_in_math_mode#Overriding_default_mathematical_styles)
  - `\(\)` and `\[\]` are preferred for [better error messages](https://tex.stackexchange.com/a/513/308105) and [suitable](https://tex.stackexchange.com/a/69854/308105) for `amsmath`.
- "``" and "''" for [quotes](https://www.maths.tcd.ie/~dwilkins/LaTeXPrimer/QuotDash.html#:~:text=Single%20quotation%20marks%20are%20produced,by%20typing%20%60%60%20and%20''%20.)
- why use the starred version [`\alph*`](https://tex.stackexchange.com/questions/282172/arabic-enumerating-inside-an-alpha-enumerating#comment1157206_282173)
- [lof](http://www.emerson.emory.edu/services/latex/latex_162.html#:~:text=file%20is%20the%20extension%20of,lot%20(list%20of%20tables).)
### warning fixes
- [underfull/overfull](https://tex.stackexchange.com/a/395370/308105) hbox and vbox
  - their [meanings](https://www.overleaf.com/learn/how-to/Understanding_underfull_and_overfull_box_warnings#Overfull_and_underfull_boxes)
    > “stretch out” the content
    > exceeds the available space
### notice
- `mathtools` -> `cases*` use [**text**](https://tex.stackexchange.com/a/321661/308105) after `&`
- `$$` doesn't has the inherent [multiline](https://tex.stackexchange.com/a/520759/308105) support. It is [to](https://www.overleaf.com/learn/latex/Mathematical_expressions#:~:text=LaTeX,therefore%20put%20on%20separate%20lines)
  > write expressions that are not part of a paragraph
```tex
% must use \cr instead of \\ https://tex.stackexchange.com/a/520759/308105
$$\displaylines{
    a = b\cr
    c = d + e\cr
}$$
```
### miscs
- how to use the [plain tex](https://www.overleaf.com/learn/latex/Questions/Can_I_run_plain_TeX_on_Overleaf%3F)
  - [books](https://tug.org/interest.html#plain) 
    doc [list](https://ctan.org/topic/tut-plaintex)
    1. [Impatient](https://ftp.kddilabs.jp/CTAN/info/impatient/book.pdf).
- `\show` should be used in the [interaction mode](https://tex.stackexchange.com/a/11912/308105) because it is normally one error.
  we can avoid it by [`\typeout{\meaning\foo}`](https://tex.stackexchange.com/a/324915/308105).
  - Use `latex let_infinite_loop.tex` to check it.
- [`@protected@testopt`](https://ctan.math.illinois.edu/macros/latex/contrib/xpatch/xpatch.pdf) is related with `\protect`.
- use [`latexdef -o '\newcommand\test{hello}' test`](https://tex.stackexchange.com/a/638531/308105) to check self-defined cmd definition.
- [trace](https://latex.org/forum/viewtopic.php?p=83008#p83008)
- [`latex3` doc](https://ctan.math.illinois.edu/macros/latex/contrib/l3kernel/interface3.pdf) and source2e/latex2e.
  TODO [`NewExpandableDocumentCommand`](https://texdoc.org/serve/xparse/0) meaning.
- [named label](https://texblog.org/2012/03/21/cross-referencing-list-items/) or use `\href`
- check enumerate
  [this](https://tex.stackexchange.com/a/442187/308105) can't be used with `\newlist` 
  while [this](https://tex.stackexchange.com/a/108703/308105) can.
- [avoid page break](https://tex.stackexchange.com/a/94702/308105)
### algorithm2e
- change font for [all](https://tex.stackexchange.com/a/279202/308105)
### amsmath
- [left aligned](https://tex.stackexchange.com/a/145660/08105) equation.
### TODO
- try use [`fltrace`](https://tex.stackexchange.com/a/39020/308105) to debug the "floating"
- [x] how `##` [to `#`](https://tex.stackexchange.com/a/42464/308105) used in `\cases`
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
- [x] what is [RobustCommand](http://labmaster.mi.infn.it/wwwasdoc.web.cern.ch/wwwasdoc/TL8/texmf/doc/latex/base/html/clsguide/node36.html#:~:text=%5CDeclareRobustCommand*%20%7B,commands%20and%20make%20them%20robust.)
  maybe related with [`\protect`](https://tex.stackexchange.com/a/88007/308105) (See "Since \foo• was preceded by \protect, the last line is what's written ..." where `\foo` is kept without expansion) which is always use with the ["moving argument"](https://www.complang.tuwien.ac.at/anton/latex/fragile.html#:~:text=Arguments%20to%20some%20LaTeX%20commands,arguments%20of%20%5Ccaption%20commands)
```tex
\foo{BAR}
...
!\foo• {BAR}!
```
  - ~~the above code implies the loop if the `\protect` functioning as [`\noexpand`](https://tex.stackexchange.com/a/4747/308105).~~
    Also see this [example](https://tex.stackexchange.com/a/47372/308105)
  - TODO how does the following avoid the above problem
```tex
\def\oldfoo{\protect\oldfoo•}
\let\oldfoo•\foo•
```
  - Also see the related [codes](./algorithm_homework_tex/miscs_learning/let_protect_infinite_loop_and_underscore_redefinition.tex)
- [x] differences between `cases` and `cases*` since `\addtolength{\jot}{-5pt}` only applies to the latter.
  they are in different packages.
- [`lccode`](https://texfaq.org/FAQ-activechars)
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
- The following *skipped* ones are based on that after I thought of the exercise and checked the ans, the ans shows the same or similar to what I thought, so I didn't spend redundant time to record the more deeper understanding about the exercise.
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
      same as [wikipedia](https://en.wikipedia.org/wiki/Pigeonhole_principle)
      > if n items are put into m containers, with n > m
      
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
      - TODO [$0.d_1\ldots d_{n−1}\overline{1}$](https://math.stackexchange.com/questions/1641233/what-points-in-0-1-will-have-two-binary-expansions#comment3346986_1641252) is recurrent by [definition](https://en.wikipedia.org/wiki/Repeating_decimal), see 
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
- 4~34 see the [pdf](https://www.overleaf.com/read/fbychkzpsrff#459790).
- 14,38,40~42,54~56 skipped.
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
- [x] 36 the list shows the states after [each pass](https://en.wikipedia.org/wiki/Bubble_sort#Step-by-step_example)
  6, 2, 3, 1, 5, 4
  1. 2, 3, 1, 5, 4, 6 beacuse 6 > all
  2. 2, 1, 3, 4, 5, 6
  3. 1, 2 ...
  4. this step [no swap](https://en.wikipedia.org/wiki/Bubble_sort#Pseudocode_implementation), finish.
  - TODO
    - ~~The above 3rd step swaps 1st and 2nd, which is different from the book ALGORITHM 4, so the book one is probably wrong.~~
    - "two more passes" is because ALGORITHM 4 **doesn't stop** when not swapped.
  - Compared with the wikipedia [optimized one](https://en.wikipedia.org/wiki/Bubble_sort#Optimizing_bubble_sort)
    `newn` excludes the ordered ending sublist(i.e. the non-stopping sequence $A[newn]\ldots A[n]$)
    and `newn=1` implies all are ordered.
- [ ] 47 
  - see the ans
    since in ALGORITHM 5, it doesn't `break` the $\textbf{while }a_j>a_i$ when `j=i`, so $2,3,\ldots$
- [ ] 48 $n$
  if to sort as the non-increasing order, $n$ by the comparison pair sequence $(n,n-1),(n-1,n-2)\ldots$ where it compares with the item **one index before** in each iteration.
  else, also $n$ but the comparison codes are different from the above in that it always begins comparison with the **1st** item.

  The above comparison order always makes the already sorted list comparison count least.
  - the 1st doesn't need to be compared with self.
- [ ] 50 
  TODO see [this](https://en.wikipedia.org/wiki/Insertion_sort#Variants) for the swap and search complexity.
  1. inserting at the $i$th implies $i$ comparison counts.
    $1+1+4+1+4+3+2=16$
  2. here after each $\textbf{while}$, one **extra** comparison is needed.
    $2+2+3+3+4+4+4=22$
  Based on the above, for small list the linear is better.
  - the ans lacks the 2nd $4$ for the linear one.
  - the ans doesn't take $a_j<a_{left}$ in account.
    TODO then for $3$, it should only have one comparison $3<4$ which drops $7$ then. Why does the ans show one for it?
  - > not almost in decreasing order 
    
    see exercise 48.
- [ ] 52
  - b based on 50, comparison count: $1+1+1+4+1$
  - c,d see 47,48
  - see the ans
    where d excludes $i=0$, so it is $1,2\ldots$ instead of $2,3\ldots$ as 48.
- [ ] 58
  - see the ans
    56 only d uses one nickel.
    - Then similar to lemma 1,
      3 dimes can not be replaced with less than 3 coins, so it is possible. More specifically, at most 4 dimes are allowed.
- [ ] 62 see the ans where intentionally use many same schedules to increase the overlap.
  think of one optimal schedule -> use one overlap schedule to break it -> add overlap schedules to ensure the break before.
- [ ] 63 
  a. use the ALGORITHM 8 incursively until all talks are scheduled. 
  b. assume S(1) means that 1 hall is the minimum.
    1. S(1) is trivially true because 0 is impossible.
    2. assume S(n-1) is true.
      ~~Then if S(n) is wrong, then it can choose at least n-1~~
      Then for S(n), we first do S(n-1) which is **assumed optimal**, then for the rest at least one is required, so S(n) $\blacksquare$
  - TODO
    the above algorithm does the same as the ans because ALGORITHM 8 will be rerun if some talks **overlap** -> going on simultaneously
- [ ] 64
  To make one stable matching, try matching at least one side the highest rank, e.g. $(m_1,w_3),(m_2,w_1),(m_3,w_2)$.
  To make one not stable, just do the opposite, e.g. $(m_1,w_2),(m_2,w_3),(m_3,w_1)$
  - The ans
    for $(m_1,w_1),(m_2,w_3),(m_3,w_2)$ ~~is stable because~~ 
    $w_1,m_3$ has their most preferred match.
    Then to find the non-stable pair
    - $m_1$ must choose $w_3$ because it is the only one before $w_1$ but $w_3$ can't choose $m_1$ due to that it is the last.
    - TODO $m_2$ can only choose $w_2$ because $w_1$ is already satisfied, and $w_2$ also prefers $m_2$. So it is not stable
      The ans only takes in account 3 man/woman but not 6.
      - Here only taking in account one side is also ok, e.g. thinking about all men or women because the pair is **bidirectional**. So if one direction is not unable to be satisfied, then the pair can't exist.
- [ ] 70
  - **Hinted** by the ans, change "Halting" to "ever prints the digit 1".
    More specifically, $H(K,K)=1\Rightarrow K(K) \text{ ever prints the digit 1}$
    $K(K)\text{ prints the digit 1 if }H(K,K)=0$ contradiction.
  - The ans combines "halt" and "print 1" together.
    $(P,I)\xRightarrow{f:\text{make }P\text{ prints nothing except for 1 before halting}\to P'}(P',I)\xRightarrow{S\text{ checks whether prints }1\text{ based on the assumption}}\text{whether }P\text{ halts}$
    if $S$ can solve the halting of $P$ based on $P'$, then 
    $f\circ S$ can solve the halting problem, contradiction (here $f$ should be done *manually* because no program can be used to check whether halting). $\blacksquare$
    ~~- The above real order should be $\forall (P',I)$~~
    - IMHO, the above is not totally strict, beacuse $f$ is not done by program. It only shows $\text{manual}\circ\text{program}$ is impossible to solve the halting problem, but not for 
      something like $\text{program}\circ\text{program}$.
- [ ] 71
  > if it is still running after any fixed length of time has elapsed, we do not know whether it will never halt or we just did *not wait long enough* for it to terminate.
  TODO So how does the ans meet the requirement by "Run"ning?
- [ ] 72
  TODO Since [not all](https://en.wikipedia.org/wiki/NP_(complexity)) decision problems are solvable, how does the ans prove?
### 3.2
- 2~6,10~18,24,28~34,38~40,44~48,52~56,60~66,70,74,76 skipped
- [x] 8 just use the limit and check it to avoid some cases like the oscillation limit.
  1. 4
  2. 5
  3. 0
  4. -1
- [ ] 20 see the ans
  both are instead of only the 1st.
- [x] 22
  $(\log{n})^3<\sqrt{n}\log{n}<n^{99}+n^{98}<n^{100}<(1.5)^n<10^n<(n!)^2$
- [x] 26
  1. $n^3\log{n}$
  2. $6^n$
  3. $n^nn!$
- [ ] 36 see the ans, notice the $C>0$ requirement.
- [ ] 42 see the ans, ~~due to the absolute comparison, the symbol may make $2^g\to 0<2^f$~~
  the $C$ can't be lifted up to the exponent.
- [ ] 50 ~~WLOG, let $a_i>0$, then $$~~
  With the calculus limit, this is trivial.
  - ~~$\frac{a_{n-i}}{x^i}<\frac{a_{n-i}}{x}$~~
    The ans is probably wrong (see above it induces the $<$ instead of $>$)
    although the $k$ [choice is right](https://cs.stackexchange.com/a/71717/161388).
    - Assume $a_k>0$,
      $$
      \begin{align*}
        &\frac{a_k}{2k}*n^i+a_{k-i}\ge 0\\
        \Rightarrow& n^i\ge \frac{-a_{k-i}*2k}{a_k}\text{, i.e. }\frac{max(|a_{k-i}|)*2k}{a_k}\\
        \Rightarrow& n\ge \sqrt[i]{\frac{max(|a_{k-i}|)*2k}{a_k}}\\
        \text{just let }&n\ge \frac{max(|a_{k-i}|)*2k}{a_k}\text{, the above inequity must hold.}
      \end{align*}
      $$
      here $k$ is $n$ in the question.
      - If $a_k<0$, just think of $g(n)=-p(n)$, then 
        $|p(n)|\ge C|a_kn^k|\Rightarrow |g(n)|\ge C|-a_kn^k|$, the do the same as the above.
  - See [this][O_Theta_Omega_relation_with_limit] for the relation of limit with $o,\Theta,\Omega$.
    ~~TODO strict proof~~
    - based on the "Limits at infinity" [definition](https://en.wikipedia.org/wiki/Limit_of_a_function#Limits_at_infinity)
      $$
      \begin{align*}
      &c = \lim_{n\to\infty} |\frac{f(n)}{g(n)|} \\
      \Rightarrow&\forall \varepsilon >0\,\exists m>0\;(x>m\Rightarrow c-\epsilon<|\frac{f(x)}{g(x)}|<c+\epsilon)\\
      \text{So we can take }&C=c-\epsilon,k=m\text{ for }\Omega\text{ if }c>0(\text{if }c=\infty\text{, we can take arbitrary small positive c})\\
      \text{and }&C=c+\epsilon,k=m\text{ for }O\text{ if }c\neq \infty
      \end{align*}
      $$
      - Notice $o$ is [different](https://en.wikipedia.org/wiki/Big_O_notation#Family_of_Bachmann.E2.80.93Landau_notations) from $O$.
        TODO here it doesn't take absolute everywhere as the book does.
- [ ] 58 based on [O_Theta_Omega_relation_with_limit], it is trivial.
  - see the ans, it needs to recursively calculate the limit.
  - so $o\Rightarrow O\text{ but }O\nRightarrow o$
- [ ] 68 not based on $f=\epsilon g,x\to\infty\Rightarrow \lim\frac{\log{|\epsilon|}+\log{|g|}}{\log{|g|}}=-\infty+1\neq 0$
  here we [shouldn't compare infinity](https://www.scientificamerican.com/article/infinity-is-not-always-equal-to-infinity/#:~:text=For%20example%2C%20the%20number%20line,does%20not%20always%20equal%20infinity.)
  - the above is wrong because $\lim\frac{\log{|\epsilon|}}{\log{|g|}}\text{ can be }\frac{\infty}{\infty}$
- [ ] 72
  - see the ans
    - sum begins from 2 instead of 1
- [ ] 73
  - see the ans
    - take the exponent
    - $n+i(n-i-1)>n,i\in\{0,1,\ldots,n-1\}$
- [ ] 75
  - see the ans
    - at least $n-\lceil\frac{n}{2}\rceil+1=n-(\frac{n}{2}+0\text{ or }\frac{1}{2})+1>\frac{n}{2}$
### 3.3
- 2~8,14~20,30~36 skipped.
- [ ] 23
  TODO Based on [this](https://math.stackexchange.com/a/1629650/1059606) (i.e. probability), it should be 
  $\frac{2n+1}{2}+\frac{n+2}{2}=\frac{3n+3}{2}$
- [x] 10 
  1. clear one 1 bit each step.
  2. 1 bit count
- [x] 12
  1. is trivial by setting all $1\textbf{ to }n$
  2. $\frac{n}{4}+1\le\frac{3n}{4}\Rightarrow n\ge 2$ which is always held. so $\ge(\frac{n}{4})^3$
- [ ] 22
  3. the ALGORITHM 3 doesn't break when equal, so same as the worst case.
- [x] 24
  1. since max must be decided after taking all terms in account, so it can't be smaller than $n$.
  2. not.
- [ ] 26 $2\log[4]{n}$
  - see the ans
    - should plus 3
- [ ] 28
  if similar to 26, we ignore **while $i\le n$**
  let mode number size is $k<n$ with corresponding mode count $c_k$, then $\sum (c_k+2)<2n+n*c_k$ which is $O(n)$.
  - see the ans for better explanation.
- [x] 38
  1. $2n+2k<4n$
  2. sort is $O(n\log{n})$ and then 
    compare with $n$ action.
- [x] 40
  the worst is $3+n$ for all using pennies.
- [x] 44
  4. if only counting the comparisons, $\sum_{2}^{n}(2*\log{j-1}+1)=O(n\log{n})$ by taking comparison in the **while** condition.
- [ ] 46 For $C=A\times B$
  $c_{ij}=\sum a_{ip}b{pj},i\le p\le j$
  - see the ans
    - lack $i\le j$
### Supplementary
- 18 skipped
- [ ] 2
  based on ALGORITHM 1, appends $sec_max=max$ after $max\coloneqq a_i$ with the init $sec_max\coloneq a_1$.

  trivially, $O(n)$ because check $n$ items with each item check constant time.
  - see the ans
    - sometimes, $a_i>sec_max,\text{ but }a_i<max$
    - $sec_max\coloneqq-\infty$ to ensure all pairs are checked.
- [ ] 4 similar to ALGORITHM 1, check in order and then if find $x$, then loop and bookkeep the locations until it is not found, then exit all the loops.
  trivially $O(n)$.
  - see the ans
    - use $first\coloneqq 0$ to indicate not found.
- [ ] 7
  > A nonvirgin comparison must be between two elements that are still in the running to be the maximum or two elements that are still in the running to be the minimum
  because it is insane to compare between the maximum candidate and the minimum candidate where maybe no possibilities are eliminated which is inefficient.
  > For example, we might be comparing x and y, where all we know is that x has been eliminated as the minimum. If we find that x > y in this case, then only one possibility has been ruled out
  because $x$ is **still** the maximum candidate, so no possibility about $x$ is eliminated.
  - it is based on 
    1. what to do: eliminate $2n-2$ possibilities
    2. how to do: eliminate 1 or 2 possibilities at each step
  - TODO since exercise 5 is $2n-2>\lceil\frac{3n}{2}\rceil-2$,
    this exercise should be the best-case complexity and exercise 6 shows this best-case complexity is possible.
- [ ] 8 see 2.
  - hinted by the ans
    if similar to 7, each pair comparison can't exclude always one possibility.
  - proof of the lower bound [$n + \lceil \lg n \rceil - 2$][lower_bound_second_largest_element] from [this](https://stackoverflow.com/questions/3628718/find-the-2nd-largest-element-in-an-array-with-minimum-number-of-comparisons/3628777#3628777)
    1. tightness (this is just the [upper bound](https://users.csc.calpoly.edu/~dekhtyar/349-Spring2010/lectures/lec03.349.pdf) similar to ), i.e. it [can't be ~~smaller~~ larger](https://en.wikipedia.org/wiki/Infimum_and_supremum#Formal_definition).
      - > Firstly, you need to find the maximum, since one cannot be sure some element is the second maximum without knowing which element is the maximum
        this may be trivial because second is based on first. So $n-1$ which is the worst/largest.
      - > the adversary to pick a very *hard* instance of the problem
        then p5 is to make as more matches as possible, although the [best case](https://stackoverflow.com/a/13170419/21294350) is also $O(n)$.
        TODO see the graph or others where the best and worst differ.
        - $\lceil \lg n \rceil$ see [this](https://math.stackexchange.com/questions/1601/lower-bound-for-finding-second-largest-element#comment4297425_1672) which is based on the binary tree in [p11][second_largest_element_Adversary] (also see 6-c)
          use the following induction
          $$
          \left\lceil\frac{\lceil\frac{n}{2}\rceil}{2}\right\rceil=
          \left\lceil\frac{\frac{n}{2}+0\text{ or }\frac{1}{2}}{2}\right\rceil=
          \left\lceil\frac{n+1}{4}\right\rceil=
          \left\lceil\frac{n}{4}\right\rceil
          $$
          - Notice here is talking about the [**worst**](https://math.stackexchange.com/questions/1601/lower-bound-for-finding-second-largest-element#comment6530597_1672) <a id="worst_lower_bound"></a>
        - similar to the best pick among $n$ candidates, the best pick among $\lceil \lg n \rceil$ candidates to decide the second best, we **at least** need $\lceil \lg n \rceil-1$.
        - IMHO, here $\lceil \lg n \rceil$ losers to the best need to be bookkept for the following comparison.
    2. lower bound
      > Let the number of elements that lost to the maximum be m.
      The needed comparison:
      - either best ($n-1$) -> second ($m-1$)
      - or second ($n-2$) -> best ($m$ based on the assumption).
    3. $m\ge\lceil \lg n \rceil$ because at least $m$ at most is $n-1$.
      See the above or [second_largest_element_Adversary] p13 for the following:
      > with each comparison any weight can only double
      - > otherwise B says anything that does not disturb past answers
        i.e. it is impossible.
    4. The above process already shows that the worst case is possible.
    - For the relation with problem 7, [see p3,16](https://www.cs.rochester.edu/u/brown/282/oheads/C05.pdf) which is related with graph and the state machine.
    - ~~TODO~~ [medium][lec_13_Adversary_Arguments]
      - here the upper and lower bound in p5 should be the supremum and the Infimum.
        the lower bound is related with [$\Omega$](https://www-student.cse.buffalo.edu/~atri/cse331/support/lower-bound/index.html), similar upper with $O$.
        so upper bound only needs to prove existence as the above shows.
        - > the adversary sets that bit to whatever value will make the algorithm do the most work
          so the lower bound decided by the *adversary* argument **depends on the specific algorithm**.
        - Notice it is still based on worst cases, see [above](#worst_lower_bound).
      - Here in p6 proof of lemma 1 is based on
        1. It assumes the decision tree chooses the medium **without** knowing "elements smaller than the median", and then proves the contradiction.
          > Our decision tree gives the *wrong* answer for this *‘swapped’* input.
          i.e. after swapping the unknown comparison $(x_i,x_m)$, it is **still consistent** with "comparisons that we’ve already performed", but it is wrong.
        2. The choices of the "comparisons that we’ve already performed" implies the adversary argument.
      - > at least $2^{\frac{n}{2}−1}$ leaves
        - here it takes all nodes in account although some are [not leaves](https://yourbasic.org/algorithms/binary-search-tree/)
        - see [this p3](https://jeffe.cs.illinois.edu/teaching/algorithms/notes/12-lowerbounds.pdf), it means at least does $\frac{n}{2}−1$ comparison.
      - $\binom{n}{\frac{n}{2}-1}2^{\frac{n}{2}−1}$ is based on connecting all pruned trees to the corresponding leaves of the choice tree of the set L.
      - > depth at least
        here means possible but not available which is also indicated by
        > improves this lower bound to
        and
        > even the case k =3 is still **open**
    - Also see [the table](https://personal.utdallas.edu/~chandra/documents/6363/lbd.pdf) where the number indicates the information number
  - compared with 7, the latter needs to traverse all items to find the minimum, so it takes more than here.
  - In summary, the proof is based on proving **both** the upper and the lower bound to one specific number
    with 7 in [lec_13_Adversary_Arguments] and 8 in [lower_bound_second_largest_element] with a bit different algorithms.
- [x] 10
  similar to one exercise before. This is just 3.1-32
  here only take comparison in account, then $n-1$ steps to calculate the difference between adjacent pairs and compare with the $min$.
- [x] 14
  is same as the reason for the bubble sort because the reason has no relation with the direction.
- [x] 16 similar to 3.2-26, only the dominating terms are cared about.
- [ ] 19 Use limit as [O_Theta_Omega_relation_with_limit] shows.
  - see the ans
    - for the detailed constructed function
- [x] 20 similar to 19 $>n$
- [x] 22 $2^n,n^2,4^n,n!,3^n,n^4$, so no.
- [ ] 24 the ans nests the $2^n$.
- [ ] 25
  after log, $n\log{n},\log{\log{n}},\log{n},n,(\log{n})^\frac{1}{2},\log{n\log{n}}$
  after sorting, let $k=\log{n}$
  then $\log{\log{n}},\log{n\log{n}},(\log{n})^\frac{1}{2},\log{n},n,n\log{n}$ 
  (2,6,5,3,4,1 -> $(\log{n})^2,n(\log{n})^{1001},2^{\sqrt{\log{2}{n}}},n^{1.0001},(1.0001)^n,n^n$)
  - see the ans
    - the 6 should be $\log{n}+1001*\log{\log{n}}$
      then compared with 3, $\log{n}+1001*\log{\log{n}}<1.0001*\log{n},n\to\infty$
- [ ] 26
  similar to 25, $n,n^2,n!,2^n,\log{n}\log{n},\log{n}(+\log{\log{n}}+\log{\log{\log{n}}}),(\frac{3}{2}*)\log{n},\log{n}(+\frac{3}{2}*\log{\log{n}}),(\frac{4}{3}*)\log{n}(+\log{\log{n}})$ (here terms in the square brackets are not dominating terms)
  so 5,6,8,9,7,1,2,4,3
  - see the ans
    - 5 is $(\log{n})^2$ which should be after 7.
      then $n\log{n}\log{\log{n}},n(\log{n})^{\frac{3}{2}},n^{\frac{4}{3}}(\log{n})^2,n^{\frac{3}{2}},n^{\log{n}},2^{100n},2^{n^2},2^{2^n},2^{n!}$
    - it doesn't take logarithms for all ~~as the hint shows~~.
- [ ] 27 Use oscillating functions
  - see the ans for more detailed examples.
- [ ] 28 similar to lemma 1,
  1. at most $c^i$ coins and all $c^i,i<k$ can not exceed $c^k$.
  2. similar to THEOREM 1
    for each $c^i$, 
    at most is ensured by the algorithm
    at least is ensured by that if one $c^m$ is to be substituted by $c^i,i<m$, then it is impossible.
  - see the ans for the explanation based on base expansion
- [ ] 30 similar to 10 checking $O(n\log{n})+n-1$
- [ ] 32 what does "always" mean? Since if we artificially make all pairs with male optimal and female optimal, it is possible.
  - see the ans
    - Rita, Jan are women.
    - Ken are men.
  - ~~The question means *one* male optimal matching and *one* female pessimal matching.~~
    ~~Then it is trivial if understanding the 3.1-65 code.~~
    The ans uses contradiction by supposing that the woman can choose worse for proving "female pessimal". ~~I originally tried direct proof: that the woman can choose better is impossible.~~
    - hinted by the ans
      suppose the stable pair $(w,m)$ is broken and 
      $(w,m'),m'>m\text{ for }w$ with $(w',m),w>w'\text{ for }m$, then $(w,m')$ is better than $(w,m)$, so no unstable pair is created.
- [ ] 34 WLOG
- [ ] 35
  1. ~~Here assume the men are the priority as original~~
    ~~so~~ based on original definition, we add that for matched pairs $(m,w)$, if existing some new pair 
    $(m',w)$, the **unchanging** side $w$ prefers $m'$ to $m$,
    then the original pair is unstable.
  2. same as original and finish when the *less* gender completed the match. (here only the finished condition changes)
  3. proof is same as the original.
  - see the ans
    - the b "*fictitious* people" **bridges the gap**, so the following can directly use the original method.
      1. "at the bottom of everyone’s preference lists" corresponds to "prefers any mate to being *unmatched*" (this definition is trivial based on the **assumption** which is also reasonable).
        women choose fictitious people -> unmatched
      - Then the following original conditions are met:
        1. same number of men and women
        2. ranks, i.e. preference in all cases.
      - so direct use the original proof
- [ ] 36
  1. similar to 35 ans, if there are $k$ pairs forbidden, extend the list with $k$ forbidden man and woman and replace the original forbidden pairs at the preference list tail with the added ones.
  2. same as the 35.
  - the [paper][McVitie_stable_marriage]
    - breakmarriage
      - theorem 3
        it shows man i can't choose better $J$
        and $J$ will choose her better partner.
      - theorem 4
        here assume k is the **first** refused so k chooses worse $(k,k_s'),k_s'<k_s\text{ for }k$ while k_s chooses better $(k_s,l)$.
        since $l$ is not refused implied by the above first, so l also prefers $k_s$ to $l_s$, contradiction.
      - TODO why theorem 4 based on the recursive version can choose *all* possible when only choosing only man $\ge i$.
        or more specifically, why rule 2 thinks of $j<i$ as unsuccessful.
      - The recursive theorem just loops one man , one woman instead of all men, all women as 3.1-65.
    - based on the above, how does [Szwarcfiter_stable_marriage] p8 work?
  - IMHO, this can be done similar to 35.
- [x] 38 Don't these two times constant?
  - hinted by the ans
    the requiring time of the past jobs will overlap the following deadlines.
    so maybe:
    (requiring time, slackness): (30,10); (1,11); ...
- [ ] 40
  1. proof of the hint:
     TODO no idle time
     ~~is~~ ~~trivial~~, e.g. "(requiring time, deadline): (14,20), (1,10)" where 2nd will be late.
  2. since the lateness is $l_i=d_i-\sum_{k=1}^{i}r_k$ 
    (here use the initial of related terms to indicate the variable)
    the when $d_i$ is big, the $\sum$ should also be big to let the $l_i$ less.
    - here prove that this is also optimal, i.e. it will the possibility that lateness will be negative lowest.
      This is equivalent to prove that if the above scheduling $S$ has one negative lateness, then no other scheduling $S'$ can have all positive lateness.
      Suppose $s_i$ in $S$ has the negative lateness,
      1. if swap $s_i$ with $s_m,m<i$ (here order comparison is based on the order in $S$)
        then $l_m'=d_m'-\sum_{k=1}^{m'}r_k=d_m-\sum_{k=1}^{i}r_k<l_i<0$, then still one negative lateness.
      2. if swap $s_i$ with $s_m,m>i$
        similarly, $l_i'=d_i-\sum_{k=1}^{m}r_k<l_i<0$
      Based on the induction of the above process, $S$ can't be modified to $S'$. $\blacksquare$
  - see the ans
    - "idle time" has no relation with the choice.
    - the above definition of lateness is a bit wrong.
- [ ] 42 3+7=10
- [ ] 43 trivial
- [ ] 46
  - hinted by the ans
    - $T_{j^*}\le t_{j^*}+\frac{1}{p}*\sum_{i=1}^{p}T_{i}\le L+L$
## 4
### 4.1
- 2~6,
  10,14~18,
  26~36,
  46~ skipped
- [x] 3 trivially by $a\mid b\Rightarrow b=ak\Rightarrow bc=a*(ck)\Rightarrow a\mid bc$.
- [x] 8 $a=6,b=2,c=3$
- [ ] 12 similar to one exercise before
  $a^2=2(2k-1),k\ge 1\Rightarrow a=2m\Rightarrow 2m^2=2k-1$ contradiction.
  - see the ans
    - use modular arithmetic.
- [ ] 20 see the ans
- [x] 21 $a\bmod m=k\Rightarrow a=k+mp,\text{ similarly, }b=k+mq\Rightarrow m\mid (a-b)=m(p-q)\quad\blacksquare$
- [x] 22 suppose $b\bmod m=k$, then similar to 21.
- [ ] 24 use the definition.
  - see the ans
- [x] 38
  notice the order can't be changed.
  $(a\bmod b)\bmod c=d\Rightarrow a=bk+m=bk+ck'+d\text{ here maybe }c\mid (bk+d)$
  e.g. $(4\bmod 3)\bmod 4\neq (4\bmod 4)\bmod 3$
  2. $(6^3\bmod 13)\ldots\Rightarrow 8^2\bmod 11=9$
  3. similar for the following
- [ ] 40 take negative and then use THEOREM 5. This is also ok.
- [ ] 42 both are $kc,k=a\bmod m$
  - see the ans
    - better use their relation instead of separately operating on them.
- [ ] 43
  1. $c=0$
  2. $c=0,d=m$
  - see the ans
    - b doesn't need the special 0 to construct the counterexample
- [ ] 44 similar to 12.
- [ ] 48
  1. closure is trivial
  2. $LHS=(a+b-mk+c)\bmod m\text{ while }RHS=(a+b+c-mp)\bmod m$, trivially, they are same.
    $LHS=((ab-mk')*c)\bmod m=(abc-mk'c)\bmod m\text{ while }RHS=((bc-mp')*a)\bmod m=(abc-mp'a)\bmod m$, trivially, they are same.
  3. Commutativity is trivial
  4. Identity elements is trivial
  5. Additive inverses is trivial
  - see the ans
    - Based on $\mathbf{Z}$.
- [x] 49 see the above
- [ ] 50
  $LHS=(a*(b+c-mk))\bmod m=(a*b+a*c)\bmod m
  \xRightarrow{\text{COROLLARY 2 with 3 modular arithmetic operations}}RHS$
  - see the ans
    - convert all into range $\mathbf{Z}$
- [ ] 53
  both not one-to-one
  $f$ onto while $g$ doesn't.
### 4.2
- 2~12,
  13~16,
  18~24,
  28,34~42,
  46~52 (even number),
  54,56~6 skipped because of triviality.
- [x] 26
  - see the ans
    - ["reduced modulo"](https://stackoverflow.com/a/9103961/21294350)
- [x] 30 
  let $2*3^k=3^{k+1}-2^k$
  1. $5=3+2(12_{3})=2\;-1_{3}=1\;-1\;-1_{3}=9-3-1$
- [ ] 32
  - hinted by the ans
    - $x\bmod 11=\sum\limits_{\substack{i=1\\i\text{ is odd}}}^{n}x_i*10^i+\sum\limits_{\substack{i=1\\i\text{ is even}}}^{n}x_i*10^i\bmod 11=\sum\limits_{\substack{i=1\\i\text{ is odd}}}^{n}x_i\bmod 11*(-1)+\sum\limits_{\substack{i=1\\i\text{ is even}}}^{n}x_i\bmod 11*(1)\bmod 11\;\blacksquare$
- [ ] 44
  Need [carry of 1](https://en.wikipedia.org/wiki/Ones%27_complement#Negative_zero) when adding one negative number.
  i.e. overflow [back](https://en.wikipedia.org/wiki/Signed_number_representations#Ones'_complement) to the end
- [ ] 45
  by using carry from 44.
  - see the ans
    - > subtracting −m from 111 … 1 because subtracting a bit from 1 is the same as complementing it
      ~~because $-m+m=1\ldots 1$ when using 1's complement.~~
- [ ] 49
  > However, the answer is invalid if an overflow has occurred
  because of [overflow](https://stackoverflow.com/a/32960835/21294350) where borrow is similar to [this "The Same in Binary"](https://www.cs.cornell.edu/~tomf/notes/cps104/twoscomp.html) which is trivial.
```bash
    1
  0010
- 0001
------
  0001
```
- [x] 51 trivial based on $2^{n−1} − |x|$.
- [ ] 61
  - see the ans
    - here we don't need to check the remaining bits when $a_k=b_k$, because if the remaining are not same, then while loop should not stop at $k$
- [ ] 62 $O(n\log{n})$
  - see the ans
    - it doesn't take $k$ in account.
    - ~~$n+1$ is based on cache usage.~~
- [ ] 64
  trivially $0\le power<m$ based on $\bmod$ definition.
  here we only cares about the for loop, loop count is $k=\lceil\log{n}\rceil$
  and the block is less than 2 $(power\cdot power)\bmod m$
  - then multiplication: $<2*(\log{power})^2<2*(\log{m})^2$
  - $\bmod$ based on 65: $=O((power^2\;div\;m)\log{power^2})<O((m^2\;div\;m)\log{power})$ TODO this is wrong
    big-O [can be compared](https://stackoverflow.com/a/11940881/21294350)
  - see the ans
    - > consists of multiplying two integers, each at most log m bits long
      based on EXAMPLE 11, complexity is $O((\log{m})^2)$.
    - > followed by a division by m, which is also log m bits long.
      based on ALGORITHM 4, see above "based on 65" this may be $O(m\log{m})\neq O((\log{m})^2)$.
  - Based on wikipedia, it doesn't care about $\log{m}$ when $\log{n}$ is the target variable.
    - And its [reference p346](https://mrajacse.files.wordpress.com/2012/01/applied-cryptography-2nd-ed-b-schneier.pdf) doesn't assert the overflow check
      the reference use `fast_exp(x,y,n)` to return $(x^y)\bmod n$
      `y&amp1`: I guess that it checks whether the least bit is 1. Then the following is trivial based on the 2nd statement in COROLLARY 2.
      - the check is due to the code [assignment restriction](https://stackoverflow.com/a/27175175/21294350) based on variable type referenced in [this](https://stackoverflow.com/questions/62368211/what-does-it-mean-to-not-overflow-in-this-psuedocode-assert-modulus-1#comment110303632_62368317).
- [ ] 65
  if we are only to prove $O(q\log{a})$,
  obviously there are $q$ while loop and each loop $r-d$ uses maximum $\lceil\log{a}\rceil$ bit operations
  since $q=a\;div\;d<a$, so $q-1$ is also the above case
  then bit operation count $c<2*q*\log{a}+C(C\text{ corresponds to the ending if})\;\blacksquare$
### 4.3
- 4,8,12,16,20,26~30,
  38~44 skipped
- [x] 2 similar to example 3, try `[107%b for b in [2,3,5,7]]==[0]*4` in python
- [ ] 6
  - see the ans
- [ ] 9 the problem is not same as the ans one. It is probably 19.
- [ ] 10
  - see the ans
    - here "t is odd" is to ensure $+1$ ending.
    - here $t=1$ also applies for $m=2^n$.
- [ ] 11 $3^q=2^p,\text{where p,q are relatively prime}$ contradiction.
  - see the ans
    - > This violates the fundamental theorem of arithmetic
      because the factorization is not unique.
- [x] 13 $3,5,7$
- [ ] 14 notice $1$ should be contained.
- [ ] 18
  $\overbrace{1+2^p-1}^{\text{factor of }2^p-1}+\overbrace{2+\ldots+2^{p-1}}^{\text{factor of }2^{p-1}\text{ after excluding duplicate ones}}+\overbrace{(2^p-1)*(2+\ldots+2^{p-1})}^{\text{combine two}}=2*(2^p-1)+(2^p-1)*(2^p-2)=(2^p-1)*2^p$
  - see the ans
    - should minus self from the above.
- [ ] 22
  1. if: 
    obviously divisors of $n$ must be less than $n$.
    then $\varPhi(n) = n − 1$ implies all $0<k<n$ are relatively prime to n.
  2. only if similar to above.
  - see the ans
    - "conversely ..." doesn't prove the theorem.
- [ ] 24 notice e -> 5;
- [x] 31
  by definition of "gcd,lcm", $(a,b)=(max(a,b),min(a,b))\text{ or }(min(a,b),max(a,b))$
- [x] 32
  $\gcd(a,b)=\gcd(b,a\bmod b)\ldots$
- [x] 34 here $2,1,0,end$ with 0,end added, there are 8 divisions. 
- [ ] 36 see the ans
- [x] 37
  $\gcd(2^a-1,2^b-1)=\gcd(2^b-1,2^{a\bmod b}-1)\ldots$
  then obviously then exponent pair is $(a,b),(b,c=a\bmod b),(c,d=b\bmod c)$ which is just the 
  $\gcd$ process. $\blacksquare$
- [ ] 45
  at the last step, here assume $y'$, etc, are values after the second to last step and 
  $y_l$, etc, are values at the last step.
  $x'=q_ly'(=r'=\gcd(x,y))+r_l(=0)$
  so the corresponding $s,t$ of $\gcd(x,y)$ are also 
  $s',t'$, i.e. $olds,oldt$ in $s \coloneqq oldolds − q ⋅ olds$ and they are equal to $oldolds,oldoldt$ after $oldolds\coloneqq olds$
- [ ] 46
  - see the ans
- [ ] 48
  1. $a_i=\text{the biggest element}\le i$
  f. square of the prime 
  - see the ans
    - the a is a bit wrong
- [x] 50 both equals $\gcd(m,a\bmod m)$
  - see the ans
    - it uses the definition which is also ok.
- [ ] 51 see [this](https://math.stackexchange.com/a/865346/1059606) based on 
  $f(n)=(n-a)^2+b\Rightarrow f(k+f(k))-f(k)=f(k)(2k+f(k))\Rightarrow f(k)\mid f(k+f(k))$
- [ ] 52 similar to THEOREM 3 proof, since $p_{1\ldots n}\nmid (\Pi p_{i}+1)$, then prime factorization can be only itself and 1.
  - The above is wrong. See the ans
- [ ] 54 see the ans
- [ ] 55 it should be $(4k+1)(4k+3)=4*m+3$
- [ ] 56
  here $f(p,q)=10*10^{d_q}+q+p*10^{d_q+1},\text{where }d_q\text{ is the digit number of the decimal representation of q}$.
- [x] 57
  1. one-to-one:
    $$
    \begin{align*}
      &K(m'/n')=K(m/n)\\
      \xRightarrow{\gcd(m,n)=1\Rightarrow p_i\neq q_k}&a_i=a_i',b_i=b_i',p_i=p_i',q_i=q_i'\\
      \Rightarrow& m'=m,n=n'\tag*{$\blacksquare$}
    \end{align*}
    $$
  2. onto trivial based on the unique prime factorization.
  - see the ans
    - "exactly one positive" is more elegant which proves one-to-one correspondance at one time
      which is just the above "onto" but emphasizes "unique".
### 4.4
- 2~4,
  10~12,
  24,32~38,
  54 skipped
- [x] 6 we can also use the extended version.
- [x] 7 trivial after hinted
- [ ] 8 see the ans
- [ ] 14 see the ans: notice 11 simplies the problem.
- [ ] 15,17,18,26,42~44 see the ans
- [x] 16
  1. $(5,9),(7,8),(2,6),(3,4)$
  2. i.e. $10\equiv -1\pmod 11$
- [ ] 19
  1. if two are congruent, then $i*a\equiv 0\pmod p\xRightarrow{i\text{ and }p\text{ are relatively prime, which is 4.3 lemma 2}}a\equiv 0\pmod p$ contradiction
  2. 3
  3. "p does not divide (p − 1)!" this is trivial based on Lemma 3
    then since p is prime, so $\gcd(p,(p-1)!)=1\Rightarrow a^{p−1} \equiv 1 \pmod p$
  4. trivial by multiplication.
  - see the ans
    - b is based on $p-1$ possibilities to prove existence.
    - d is $\forall$
      $p\mid a\Rightarrow a\equiv 0\pmod p$
    - same as [this](https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#Proof_as_a_particular_case_of_Euler's_theorem)
- [ ] 20
  $$
  \begin{align*}
    4*5*(-1)\equiv 1\pmod 3\\
    15*(-1)\equiv 1\pmod 4\\
    12\equiv 2\pmod 5\Rightarrow 12*3\equiv 1\pmod 5\\
    -20*2+(-15)+3*36=53
  \end{align*}  
  $$
  - see the ans
    - better explicitly show the condition of the theorem is met
- [x] 22
  $$
  6t\equiv 1\pmod 7\\
  \Rightarrow t=7u+6\\
  \Rightarrow x=6(7u+6)+3=42u+39
  $$
- [ ] 28
  ~~Use general functional $f:S(n\text{ modular equations})\to T(n\text{-tuple})$~~
  ~~obviously this is one-to-one from the Chinese remainder theorem. If not, then $\exists k,t\in \mathbf{Z}_{m},k\neq t\xRightarrow{\text{based on the equation system}}k\equiv t\pmod m$~~
  ~~onto is also trivial by just doing the ~~
  if not unique, i.e. there are two n-tuples corresponding to $a$, then $\exists m_i,a\equiv t_1,t_2\pmod m_i$ contradiction.
  - see the ans
    - the ans may be wrong
      because "The Chinese remainder theorem" says $n\text{-tuple}\to\text{unique }a$ but not $\text{unique }n\text{-tuple}\leftarrow a$
- [ ] 29 by contradiction. 
  $$
  a=k_im_i+b\text{ contradicts with }a=km+t,t\neq b\\
  \begin{align*}
    &t\neq b\\
    \Rightarrow&t=k_i'm_i+b\equiv b\pmod m_k,k\neq i\\
    \xRightarrow{m_k|k_i'm_i,\gcd(m_i,m_j)=1\xRightarrow{\text{4.3 lemma 2}}m_k|k_i'.
    \text{ Use this for all }k\neq i\text{ and based on relatively prime with 4.3 lemma 3}}&\Pi_{k\neq i}m_k|k_i'\\
    \Rightarrow& k_i'=p*\Pi_{k\neq i}m_k\\
    \Rightarrow& t>m\text{ contradiction} \tag*{$\blacksquare$}
  \end{align*}
  $$
  - see the ans
    - ~~TODO $p\mid (a-b)\nRightarrow p*\ldots\mid(a-b)$~~
      It uses induction to show $\forall p_{ik}|m_i\Rightarrow p_{ik}|(a-b)\Rightarrow \Pi m_i=\Pi_{\text{all }i,k}p_{ik}|(a-b)$
    - Also see [this](https://math.stackexchange.com/a/289346/1059606) which also uses induction where $a,b=m_i,m_{i+1}$.
- [x] 30 based on 29, this is trivial to prove $x\equiv y\pmod m$, so unique.
- [x] 37 trivial
- [ ] 40
  $7\mid (n^7-n)$ is trivial
  - see the ans
    - use $2\mid\ldots$ as the basis.
- [ ] 41
  equivalent to prove $2p\mid 2^p-1-1=2kp$ where $2\mid$ is trivial and $p$ is based on the Fermat’s little theorem.
  - see the ans
    - The above proves the converse proposition.
- [x] 46
use [this](https://stackoverflow.com/a/22808285/21294350) to calculate the prime factorization of $1729$
similar to EXAMPLE 11.
$$
b^6\equiv 1\pmod 7\\
b^12\equiv 1\pmod 13\\
b^18\equiv 1\pmod 19\\
$$
```python
[ins] In [6]: x=1
         ...: quotients=[]
         ...: for i in prime_factors(1729): quotients.append(1728/(i-1))
         ...: quotients
Out[6]: [288.0, 144.0, 96.0]
```
- [x] 48 same as 46 but more general.
- [x] 49 trivial after computation
- [ ] 50 see the ans better to use the table for- calculation.
- [x] 52 similar to EXAMPLE 8.
- [x] 53 just as the usual cases to calculate with the Chinese remainder theorem.
- [ ] 56
  - see the ans
    - here is due to $r^i\equiv r^{i+p-1}\bmod (p-1)$
    - here log is not the discrete logarithm.
- [ ] 58
  - here $3^2\equiv 2\pmod 7$ can't use the same method as exercise 17 because $\sqrt{2}$ is not one integer.
  - $16>11,25>22,36>33$ so at least $5,3$ are.
  - see the ans
    - since $x\equiv k\pmod 11\xRightarrow{decides}x^2\ldots$, so we only need to care about $1\sim 10$
- [ ] 59
  see the ans use "at least" and "at most" to prove.
- [ ] 60
  based on 58, only care about $1\sim \frac{p-1}{2}$
  then if $i^2\equiv j^2\pmod p,i\neq j\Rightarrow (i+j)\equiv 0\pmod p$ contradiction.
- [ ] 62 use the "Fermat's little theorem"
  $a^{p-1}\equiv 1\pmod p\Rightarrow (a^{\frac{p-1}{2}}-1)(a^{\frac{p-1}{2}}+1)\pmod p$
  - see the ans
    - the above doesn't show that both sides take one of $\pm 1$ at the same time.
    - here "group" is due to $i*j\equiv i'*j\pmod p,i\neq i'\Rightarrow (i-i')*j\equiv 0\pmod p$ contradiction.
- [ ] 64
  1. $\equiv (-1)^{2n}\pmod p$
  2. $\equiv (-1)^{2n+1}\pmod p\equiv -1\pmod p$
- [ ] 66
  ~~3*3=9~~ $2^3=8$ combination choices
  $(x-4)(x+4)\equiv 0\bmod (3\text{ or }5\text{ or }7)$
### 4.5
- 2~24
  28,32 skipped
- [ ] 26
  - see the ans
    - use "relatively prime" to prove $\not\equiv$
- [ ] 27
  when not same odd or even, it can be checked.
  when one odd and one even, $-2(x_{odd}-x_{even})$, so 
  $5\nmid (x_{odd}-x_{even})$.
- [x] 30 similar to 22
- [x] 31 similar to 31
  $$
  9*10^{j-1}(a_j-a_{j-1})\text{ when }j,j-1
  \text{th items are swapped with 0th is the rightmost digit of the 14-digit number}
  $$
- [x] 34
  $ij\not\equiv 0\pmod 11\text{ when }11\nmid\text{both }i,j$
### 4.6
- 4,10,16~20,
  24 skipped
- [x] 2
```python
# https://stackoverflow.com/a/5927160/21294350
string.ascii_letters[string.ascii_lowercase.index('s')+4]
```
- [x] 6 see p336 for the frequency list
- [x] 8
```python
str="DVE CFMV KF NFEUVI,REU KYRK ZJ KYV JVVU FW JTZVETV"
max=1
index=0
for i in range(25):
    if max < str.count(string.ascii_uppercase[i]):
        max=str.count(string.ascii_uppercase[i])
        index=i
print(string.ascii_uppercase[index],index,max)
```
- [ ] 12
  $\frac{p-b}{a}\equiv(ap+b)\pmod 26\Rightarrow(a+1)[(a-1)p+b]\equiv 0\pmod 26\Rightarrow a=25$
  - see the ans
    - the above $\frac{1}{a}$ is wrong, 
      (TODO after abstract algebra) maybe with abstract algebra, this is right. 
    - > two different pairs (a,b) cannot give the same encryption function
      $\forall p,(a_1-a_2)p+(b_1-b_2)\equiv 0\pmod 26$ contradiction.
- [ ] 14
  $\mathcal{P,C}$,etc are same as RSA.
- [ ] 22 for each $i$th ($0\le i<m$) calculate related frequency $f_{iK}$ of each character 
  $K$ and then $f(K)=\sum f_{iK}$
  - see the ans
    - show "key string" instead of the "long string".
- [ ] 23 see the ans
- [x] 26 [Modular multiplicative inverse](https://stackoverflow.com/a/9758173/21294350)
  [CAS](https://en.wikipedia.org/wiki/Computer_algebra_system)
- [x] 28 see [this](#RSA_m_not_coprime_n)
- [x] 30 TODO [Finding primitive roots](https://en.wikipedia.org/wiki/Primitive_root_modulo_n#Finding_primitive_roots) [also](https://brilliant.org/wiki/primitive-roots/#finding-primitive-roots)
- [ ] 32
  encrypt with Alice's private and then Bob’s public.
- [ ] 34
  - TODO reasons of choices related with $\gcd$ by Paillier cryptosystem.
    here the 2nd is to ensure [inverse](https://en.wikipedia.org/wiki/Paillier_cryptosystem#Key_generation)
### supplementary
- 2,8,12,42~44,48 skipped
- [ ] 4
  $$
  q=\frac{a}{d}+\frac{r}{d}\in(\frac{a}{d}-\frac{1}{2},\frac{a}{d}+\frac{1}{2}]\\
  \Rightarrow q=\lceil\frac{a}{d}-\frac{1}{2}\rceil
  $$
  - by induction is also ok
    i.e. 
    $$
    q=0\Rightarrow a\in(-\frac{d}{2},\frac{d}{2}]\\
    q=1\Rightarrow a\in(\frac{d}{2},\frac{3d}{2}]\\
    \ldots
    $$
- [ ] 5
  $$
  ac-bc=m*k\\
  \Rightarrow (a-b)*p*d=d*\frac{m}{d}*k\\
  \xRightarrow{p\nmid }
  $$
  - see the ans
    - it uses $(a-b)\in\mathbf{Z}\Rightarrow\frac{k}{p}\in\mathbf{Z}$ $\blacksquare$
    - $e\nmid m\Rightarrow e\nmid\frac{m}{d}$
- [ ] 6,10,14~16,19,20~22,32,40 see the ans
- [ ] 18 direct proof: n,1 are enough to show prime.
- [ ] 21 see the ans
  > one of which is necessarily 2
  because the sum of 2 primes must be even.
- [ ] 23
  assume no composite (i.e. the opposite of the conclusion) we need to induct to the contradiction.
  $$
  (x_0+kp)^k=x_0^k+kp*F(k)\\
  \xRightarrow{\substack{p\mid f(x_0)=\sum_{i=1}^{n}(a_k*x_0^k)+a_0\\\\ p\mid kp*\sum_{k=1}^n F(k)}} p\mid\sum_{i=1}^{n}[a_k(x_0+kp)^k]+a_0
  $$
  - see the ans
    - we must show that $\sum_{k=1}^n F(k)$ is not always 0 based on "takes on each value at most n times."
- [ ] 24 similar to one exercise or example before.
  2: 50
  4: 25
  8: 12
  16: 6
  32: 3
  64: 1
  so 97
- [ ] 26 TODO it should only divide 10 times when break after the remainder is 0.
```python
# https://stackoverflow.com/a/21608837/21294350
a = int(input("What's the first number? "))
b = int(input("What's the second number? "))
i=0
while 1:
    i=i+1
    r=a%b
    if not r:
        break
    a=b
    b=r
    print(a,b,i)
```
- [ ] 28
  - a
  1. trivial
  2. bring the already known common divisor "2" out, and combine later
  3. similar to above, exclude 2 beforehand.
  4. $\gcd(a − b, b)\mid (a-b),b\Rightarrow\gcd(a − b, b)\mid [(a-b)+b=a]$
  - b
  comparisons: 4 cases
  $a/2$ -> shift
    - see the ans
  - c
- [ ] 30 $Q$ is not the same form.
  see the ans
- [x] 34 use different common divisors pair by pair
  e.g. $2*7*13,2*3*11,3*7*11,5*11*13$
- [x] 35 at least 1.
- [x] 36 $\bmod 3$ has 2 possibilities.
- [ ] 38
  1. only if: $x\equiv a_1\bmod(\gcd(m_1,m_2))\wedge x\equiv a_2\bmod(\gcd(m_1,m_2))\Rightarrow a_2\equiv a_1\bmod(\gcd(m_1,m_2))$
    if: $\frac{m_1}{\gcd(m_1,m_2)}=\Pi m_{1k}$ and 
      $\frac{m_2}{\gcd(m_1,m_2)}=\Pi m_{2j}$ are obviously relatively prime.
      Then based on the above $x\equiv a_1\bmod(\gcd(m_1,m_2))$
      valid system is constructed.
  2. based on the above "if", trivial.
    - see the ans which doesn't use "Chinese remainder theorem".
- [ ] 46
  $-4(d_2-d_1)\not\equiv 0\pmod 10\Rightarrow (d_2-d_1)\not\equiv 5\pmod 10$
  $-2(d_1-d_3)$ and the rest are similar.
## 5
### 5.1
- 2~46,50,56~60,74,78 skipped where 
  1. 18 is similar to 4.
  2. 36,37 similar to one example.
  3. 40,42,60(see the ans which can be also related with 43 because set can be described by proposition) need some basic lemmas to complete the proof (i.e. $n=2$).
  4. 46 $C_{n}^3$
  5. 47 trivial after hinted
- 61 see the ans
- [ ] 25
  need explicitly showing $(1 + h) > 0$ when inequality.
- [ ] 48
  begin from the minimum $x_1$ -> one $t_i$, 
  then add one consecutive each time, which may increase one $t_i$,
  then the algorithm from 47 is always the best.
  - the above may be wrong, because the global optimal may be not local optimal.
  - see the ans
- [x] 49 should begin at n=2 to ensure overlap.
- [x] 51 $x − 1\text{ maybe }\not>0$ 
- [ ] 52 pigeonhole principle
  - see the ans
    - the codomain may be not same as $\{1, 2, \ldots , n \}$.
- [ ] 53 TODO what does it do?
  - > the second person chooses the portion he *thinks* is *at least* 1∕2 of the cake
    what does this "think" mean?
  - why not just equally divide?
- [ ] 54
  1. choose n numbers from $\{1,2,\ldots,2n\}$
    > we can assume that both 2n + 1 and 2n + 2 are in A

     because if one is not in, then $n+1$ from $\{1,\ldots,2n\}$ which must have one non-coprime pair
  2. decide what n numbers are chosen.
    > Since B is a collection of n + 1 numbers from {1,2,...,2n}

     because $n+1$ is excluded, 
     TODO here we should choose $n$ numbers
  
     - Notice: since $2\mid 2k$, so if choosing $n+1$ numbers from {1,2,...,2n} to make divisibility ~~less~~ the least possible, we must choose **all odd** numbers, i.e. $T=(S=\{1,3,5,\ldots,2n-1\})\cup \{2\}$.
       Then there must be $p\mid q,\text{where }p,q<2n$
       ~~so there must be $k\mid (n+1)\mid (2n+2),k<2n$~~
       - since $n+1$ is excluded, we must choose the size-$n$ set $T'=(S-\{n+1\})\cup \{2\}$
  3. test divisibility
    - > If n + 1 is not one of these two numbers, then we are done
      because the above $(p,q)$ **divisibility pair** are still left in 
      $T'$ whose size is $n$.
    - > But now k and 2n+ 2 are numbers in A
      then we have $(k,2n+2)$ **divisibility pair**
  - From EXAMPLE 11
    it also uses all odd numbers.
- [x] 55
  index $(i,j)$ by one unique number 
  $i*n+j$.
  Then to plus $i$ by one, we can $(+1,+2),(-2,-1),(+2,-1)$, i.e. $(+1,0)$
  similarly $(+2,+1),(-1,-2),(-1,+2)$ i.e. $(0,+1)$
- [ ] 62 better see [this](https://math.stackexchange.com/a/209679/1059606)
  > Each time a line is added and it crosses k  other lines it adds k+1  regions and k  intersections.
  this is because cross 1 line will add 2 regions due to one line splitting the space half.
  TODO strict proof
  - > With n lines, there are $\binom{n}{2}$ intersections
    see [this](https://math.stackexchange.com/a/787324/1059606) which is based on each pair having one intersection.
    This can't be more because intersection is shared by at least 2.
  - see the ans
    - it adds one intersection at each step.
    - >  continue drawing from this first point of intersection to the second, the line again separates one region into two
      > leave the last point of intersection and draw our line off to infinity again, we separate another region into two
      here when only crossing infinite, one region is added.
      when reaching "this first point of intersection", still one
      when from this first point of intersection to the second, another one is added.
  - Also see [this](https://math.stackexchange.com/a/339853/1059606) with also conditions about circle
    - > the number of points, $\binom{n}{2}$, plus the number of lines, $\binom{n}{1}$
      because 
      > The number of regions it passes through is the *number of lines* it crosses *plus* one
    - > the number of regions added to the original one, (n0)
      this is just the condition without lines.
    - comparison with circle <a id="5_supplementary_49"></a>
      circle: 
      1. cross 2 points instead of 1 -> $2\binom{n}{2}$
      2. > For n  circles there can be up to $2\binom{n}{2}$  crossings
        each pair of points add one more region
        i.e. the ans in S-41
        > form 2k new arcs, each of which splits an old region
      3. > It divides all the regions *through* which it passes into two, thus adding one region for each region it passes through
        This is the **key difference** because it only cares about intersection *without caring number of circles*.
      it begins with $\binom{n}{0}$ when no circle, then 
      plus $\binom{n}{0}$ when adding the 1st circle, then
      plus $2\binom{n}{2}$ which is related with intersection.
- [ ] 63
  - [wikipedia](https://en.wikipedia.org/wiki/AM-GM_Inequality#Proof_by_induction_#1)
    the main idea is the reorder $x_{n+1}<\alpha$.
  - see the ans
    - It uses 2-power
      then for non-2-power cases, fill with average to use already proved cases.
    - It should be $(a_1\cdots a_n)^{\frac{1}{m}}\bar{a}^{1-\frac{n}{m}}\le \bar{a}$.
      Then after raising, $(a_1\cdots a_n)^{\frac{1}{n}}\bar{a}^{-1}\le 1$
- [ ] 64 see the ans
  $p\mid a_1\cdots a_n*a_{n+1}\nRightarrow p\mid a_1\cdots a_n\text{ or }p\mid a_{n+1}$
- [x] 66
  similar to 5.1.3, $\text{at least }m\subseteq S$
  then $(m-2,m-1)$ can imply that 
  $m$ is true.
  - IMHO we should assume *ordered* $S=\{a_1,\ldots,a_m\}$
    then $a_m-1,a_m-2$ must be not in $S$.
- [ ] 68 see the ans
  $n=2$, if the 1st knows the 2nd and the 2nd doesn't know the 1st, then the 2nd is the celebrity.
  1. exclude one by one question
    > Without loss of generality, assume that we have eliminated Alex as a possible celebrity
    This is due to at least one is excluded. Then we use the inductive hypothesis with the remaining $k$ people.
  2. maybe exclude the remaing k by $3(k-1)$
     1. if not, i.e. find one celebrity, use 2 more to ensure the remaining relations between the celebrity and the Alex.
- [x] 69
  $$
  G(1)=0\\
  G(2)=1\\
  G(3)=3\\
  G(4)=4
  $$
- [x] 70
  by hint, after the start call by the $(k+1)$th person with $i$
  then by hypothesis, with $G(k)$ all k people are shared with each other including i which has 
  $(k+1)$th person scandal.
  Then at the call, $(k+1)$th person got the remaining 
  $k$ people information.
- [ ] 71
  similar to 70, it has common difference $2$, then begin from $G(4)=4$.
  - [AHajnal_058] by [64] in [hedetniemi1988]
    - How it is related with this question.
      - lemma 2 implies after $2n-3$ calls, at most $n-1$ F-points are constructed.
        So we need **at least** $2n-4$ to get n F-points.
    - proof
      - > This  is   impossible  since  |E1| + l<k.
        more intuitively, at least k-1 edges more are needed to make isolated $x$ F-point.
        But $|E_1|=k-2<k-1$
      - > If  c(n+k—  p—3) is  not  adjacent  to  any  F-point,
        this interchanges $c(n+k—  p—3)$ with 
        $ c(n + k—p—2),\ldots, c(n +  k—4)$
      - here component implies [disjoint](https://en.wikipedia.org/wiki/Component_(graph_theory)) <a id="component_inherent"></a>
        so the sequence 3 can be constructed by interchanging $\bar{\bar{c}}(i)$ with 
        $\bar{c}(1),\ldots,\bar{c}(r)$
      - here lemma 1 is proved by graph because
        one line connecting all $n$ points must have at least $n-1$ edges.
      - > the first n—3 calls can be equivalently re-ordered so that the (n—3)-rd call is in a different component of G0 to c(n—2)
        if (n-3)rd already meets the requirement, then nothing needs to be done.
        if not, then suppose the $k$th meets the requirement, then interchange it with $(n-3)$rd, we are done.
      - > In fact, we can assume that $p<k$. For, ifp=k we can, by the last paragraph
        This is due to that the interchange can make the last $p—1$ calls "all between F-points".
      - ~~TODO the proof may be Begging the question~~
        ~~because~~
        > Suppose there are k F-points after the n+k—4 calls
        the above which has been proven available by the book ans is different from ~~what to be proved~~ the following
        > This shows that there can be *at most* k F-points.
      - > Therefore, by the induction hypothesis there must be exactly k—r such F-points
        TODO IMHO this is based on hypothesis
        > Suppose there are k F-points after the n+k—4 calls
        
        similarly
        > there is an equivalent re-ordering of these n+k—r—4 calls so that the last k—r are between the k—r .F-points not in C
        this is just based on the hypothesis of what to be proved "... in which the last k calls".
      - > In fact, we can assume that $p<k$ ...
        It can be ignored which doesn't influence the proof.
      - In summary
        To prove
        > if there are k F-points, then there is an equivalent calling sequence $c'\sim c$ in which the last k calls 
        1. > *Suppose* there are k F-points
        2. show $\{c(1),\ldots,c(n-2)\}$ "has no isolated vertex".
          ~~TODO this is not used later if not using "interchanging c(n—3) and c(n—2)".~~
          Then we can manipulate wit edges without considering "isolated vertex".
        3. suppose contradiction
          > the last k calls of the given sequence are *not all* between F-points
        4. prove "c(n+k— p—3) is ~~not~~ adjacent to any F-point" based on 3
          then construct the isolated component including $c(n+k— p—3)$, i.e. 
          $\{\bar{c}(1)\ldots\}$.
        
        5. one interchange based on component [inherent property](#component_inherent)
        6. prove $k-r$ F-points in 1~n+k-r-4 based on 4
        7. one interchange based on $k'=k-r<k$ induction hypothesis
        8. one interchange based on F-point disjoint property.
- [ ] 72 see the ans
  I tried $a_1,\ldots,a_n,2a_1,\ldots,2a_n$ to construct the sequence, but failed.
- [ ] 73
  here think of interval as set.
  ~~since $I_{n+1}\cap I_k\neq \varnothing,k=1\sim n\xRightarrow{IH: K=\bigcap_{i=1}^n I_i\neq\varnothing} I_{n+1}\cap K\neq\varnothing$~~
  here nothing shows $(I_{n+1}\cap I_1)\cap(I_{n+1}\cap I_2)\ldots\neq\varnothing$, so the above may be no sense.
- [ ] 76
  1. $<n(4n+3)$
- [ ] 77
  similar to the example
  exclude the closest pair which is ensured to be hit, then the rest are ensured by hypothesis.
  - > Have the people stand at mutually distinct small distances from their partners but far away from everyone else
    TODO this may be not achieved.
- [ ] 80
  1. trivial based on 3x2
  2. similar to a
  3. no
  4. see the ans, can be based on b
- [ ] 81 this is similar to EXAMPLE 14.
- [ ] 82 see [this](https://www.cut-the-knot.org/Curriculum/Games/TrominoPuzzleN.shtml)
  where 5x5 is trivial based on inspection.
  7x7 is based on 5x5 and 2x3 by "(1, 1), (1, 2), (2, 2), (2, 1) - removed".
  Then based on induction.
  because it has the cycle of 6, so 5 and 7 is enough.
- [ ] 84
  this is similar to one example before by step-by-step proof.
- [ ] 85 trivial
  - see the ans which uses one linear transform.
### 5.2
- 2~6,14,26,30~32,37 skipped
- [ ] 8 see the ans
  - it uses $8+2=5*2$ and $5*3+1=8*2$
- [ ] 9 it may still use the idea similar to before.
- [ ] 10,16 see the ans
  - ~~here "squares" may be not strictly nxn square.~~
- [x] 12
  - notice "distinct"
  - when k + 1 is even, just multiply 2 for each factor in $\frac{k + 1}{2}$
    when odd, just plus one with the factors of even $k$.
- [ ] 13 this question is weird ...
- [ ] 18 see the ans which splits into two smaller polygons as one example does.
  > (otherwise, the region containing $v_{m+n−1}$ would not be a triangle)
  more intuitively, the region contain the side $v_{m+n−2}v_{m+n−1}$ will not be a triangle.
- [ ] 19
proof of the hint without the additivity lemma
$$
\text{1. rectangle (with (0,0) as the bottom-left point):}\\
mn=(m-1)(n-1)+\frac{2(m+1)+2(n-1)}{2}-1\\
\text{2. right triangle, the bottom-left half of the above, with }k\text{ interior points on the diagonal}:\\
\frac{mn}{2}=\frac{m+n+1+k}{2}+\frac{(m-1)(n-1)-k}{2}-1\\
\text{3. arbitrary triangle with A(0,n),B(m,0),C(p,q) as vertices where (p,q) is the interior point in the rectangle}\\
\text{assume that }k_1,k_2,k_3\text{ points including vertices are on AB,BC,AC}\\
\text{let D(0,0),E(m,n),F(p,0),G(0,q) and split the big rectangle ADBE into AGC,ABE,CFB,GDFC}\\
S_{\triangle ABC}=mn-pq-\frac{mn+(m-p)*q+(n-q)*p}{2}\\
B_{\triangle ABC}(P)=\sum k_i-3\\
\text{3.1 based on the 1,2 cases, care about }I(P)\\
I_{RHS}(P)=I_{mn}(P)-\ldots=B_{\triangle ABC}(P)-2+p-1+q-1+I_{LHS}(P)\quad\text{-2 is to exclude A,B.}\\
\text{3.2 care about }B(P)\\
\frac{B_{RHS}(P)}{2}=\frac{-1-1-1-1-3-2(FC_i+CG_i)-(AB_i+BC_i+AC_i)}{2}=
\frac{-B_{\triangle ABC}(P)-4-2(p-1+q-1)}{2}\quad
\text{the 4 ``-1" are duplicate minuses of A,B,F,G, ``-3" corresponds to C, }AB_i\text{ means points inside the line AB}\\
\text{Then}\\
RHS=-1-(-4)+I_{RHS}(P)+\frac{B_{RHS}(P)}{2}=3+I_{LHS}(P)+\frac{\sum k_i=B_{\triangle ABC}(P)}{2}-2-2\tag*{$\blacksquare$}
$$
  - see the ans
    - > so by the additivity lemma, it holds for the triangle as well.
      this is because $S_{rect}=S_1+S_2=\ldots=I(P_1)+\ldots+I(P_2)+\ldots$
      although by theory, maybe $I(P_1)$ corresponds to $S_2$, but it is nonsense.
    - > To prove this, suppose there are k lattice points on the diagonal
      here the "diagonal" can be generalized to polyline diagonal
      Then the above $ABC$ case can use it by adding $AB,ACB,CF,CG$ diagonals which is one special induction.
- [ ] 20
  By lemma 1 split one triangle out with the $n+1$ case.
  Then use the furthest triangle of the pair in the $n$ case to pair with the above.
  - [meisters1975]
    - [Jordan curve](https://mathworld.wolfram.com/JordanCurve.html)
      where [non-self-intersecting](https://en.wikipedia.org/wiki/Curve#Jordan) implies simple.
    - ~~> at which the interior angle is less than $180^o$~~
    - > and hence forms another ear for P which is non-overlapping with the ear
      this will restrict the quadrilateral as combination of two triangles with one common side and two not common points in the different regions splitted by the common side.
    - TODO related with geometry
      - why must a Jordan polygon be left when removing one point?
      - > the two ears E,  and V_ VV+ are non-overlapping
        here implies that overlap -> adjacent.
    - in summary
      case 1
      1. two triangle -> basis step
      2. one triangle and 
        premise theorem: one polygon with $E_1$ excluding $V_{-}V_{+}$
      case 2
      3. choose $Z$ to split
      case 2.1 splitted into two triangles similar to 1.1 -> basis step
      case 2a one triangle similar to 1.2
      case 2b no triangle using premise theorem
- [ ] 21
  1. left
  2. right
  3. right
- [ ] 22
  - see the ans
    - ~~TODO why the side of "the smaller polygons" can be "two vertices that are not endpoints of any of these diagonals"?~~
      This is $n=3$
  - b
    the case $n=5$ needs to be respectively manipulated where for the triangle we doesn't choose $uv$
- [ ] 24
  - > because then Alice and Ted would form an unstable pair
    is similar to 3.1-67
    > Because m did not end up matched with w, she must have rejected him
    where w is paired with her rejected $m$. That case is same as (Alice,Bob).
  - This is same as 3-supplementary-32. 
- [ ] 28
  - maybe using $P(b), P (b + 1), ... , P (b + j)$ as the basis step is better.
- [ ] 31 similar to mathematical induction
  the least element in the false set is ensured True by induction leading to contradiction.
  - better show $P(1)$ is excluded by the basis step.
- [ ] 33
  1. just use many $(0,1),(1,0)$ steps to get to any point.
- [x] 34
  use b
  - P(1,k) is trivial
  - $P(n+1,k)=\frac{n(n+1)\ldots(n+k)}{k+1}+(n+1)\ldots(n+k)=\frac{(n+1)\ldots(n+k)[n+(k+1)]}{k+1}=RHS$
- [ ] 35 see the ans
  just reorder to make all those with parentheses before those without, 
  then for each pair with parentheses, multiplication count is not changed with parentheses. 
  By induction, if k parentheses can be removed, then $k+1$ can be also removed ~~because the last parenthesis is no use after no ~~
- [ ] 36
  1. trivial by setting $s=t=0$
  2~3 trivial
  1. $r=a-qc=(1-qs)a-qtb$
  2. 
  - see the ans
    - a. should be positive, so (0,0) is excluded.
- [ ] 38 see the ans
  $2m + 1 , m + 1 , 1 , 2 ,\ldots , m, 2m, 2m −1 , \ldots , m + 2 , 2m + 2 , \ldots , 3m$
  is based on the left-right mirror of 1.8-48 figure.
- [ ] 39 
  - see the ans
    - it has no relations with well-ordering
      but with combination.
- [ ] 41
  basis step is the minimum.
  see the ans
- [ ] 42 see the ans based on recursion from mathematical to strong
  use 41 from mathematical to well-ordering, then to strong.
  - > The strong induction principle clearly implies ordinary induction
    because $P(1)\wedge\ldots\wedge P(k)=T\Rightarrow P(k)=T$
    ~~IMHO, it ~~
  - > $\forall nP(n)$ is logically equivalent to $\forall nQ(n)$
    ~~because $P(n)$ is only valid when both ~~
    ~~$Q(n)$ and ~~
    This is based on "strong induction"
- [ ] 43 same as 41
  - see the ans or use 41,42.
### 5.3
- 2~4,12,15,16~20,26~28,36~38(38 similar to 34),46,52,58,59(similar to 58),60~62,66 skipped
- [ ] 6 c,d,e are not valid.
  see the ans where e is valid
- [ ] 8 d see the ans
- [ ] 10 $S_0(0)$ is also ok when recursive 
  $S_{m+1}(n)$ and $S_{m}(n+1)$.
- [x] 14
  begin from [$F_1$](https://en.wikipedia.org/wiki/Fibonacci_sequence#Definition)
  $f_{n+2}f_n-f_{n+1}^2=f_n^2+f_nf_{n+1}-f_{n+1}^2=f_{n+1}f_{n-1}-(-1)^n+f_nf_{n+1}-f_{n+1}^2=(-1)^{n+1}$
- [ ] 21
  1. 
  $$
  max(-a_1,\ldots,-a_{n+1})\overset{\text{definition by 20}}{=}max(max(-a_1,\ldots,-a_{n}),-a_{n+1})
    \overset{\text{IH}}{=}max(-min(a_1,\ldots,a_{n}),-a_{n+1})
    =-min(min(a_1,\ldots,a_{n}),a_{n+1})
  $$
  1. 
  $$
  max(a_1+b_1,\ldots,a_{n+1}+b_{n+1})= max(max(a_1+b_1,\ldots,a_n+b_n),a_{n+1}+b_{n+1})
  \overset{\text{let one factor larger}}{\le} max(max(a_1,\ldots,a_n)+max(b_1,\ldots,b_n),a_{n+1}+b_{n+1})
  \overset{\text{take = when both max factors of the sum are in one factor of max(p,q)}}{\le} max(max(a_1,\ldots,a_{n+1})+max(b_1,\ldots,b_{n+1}))
  $$
  - see the ans
    - better say $k\ge 2$ in a because $max(− min(a1, \ldots , ak),−a_{k+1}) = − min(min(a1, \ldots , ak), a_{k+1})$ needs it.
- [x] 22 similar to EXAMPLE 10.
- [ ] 24 just use sequence definition for a,b similar to EXAMPLE 1.
  - see the ans
- [ ] 30
  1. basis: $(a,a)$ are in.
    recursive: $(a,a*k),k\in\mathbf{N}_+$
  - see the ans
    - a
      since $\mathbf{Z}^+$, so $0+1$ should be excluded.
    - b
      - the above basis is not concrete to one specific number.
    - c similar to a
- [ ] 32
  - prove when $0$ is the rightmost digit, then $01$ can't be more than $10$.
    if $a_n\ldots a_0$ is this case where $a_0=0$
    when n is 1, $num_{01}-num_{10}=0\text{ or }-1$
    when 2, $num_{01}-num_{10}=0\text{ or }-1$
  - see the ans
  - hinted by the ans
    - basis step, length 2 with 4 cases $01,10,11,00$
    - inductive step:
      1. length 3 with the ending "1"
        if length 2 ends with 0, then at most 1 when we append 1
        if length 2 ends with 1, then still as before ,i.e. at most 1 when we append 1.
      2. length 3 with the ending "0", similar to the above.
- [ ] 34 similar to EXAMPLE 12.
  - see the ans
    - notice $ones(\lambda)$ needs to be defined.
- [ ] 40 notice $x$ is also considered besides $\lambda$
- [ ] 42 see the ans which maybe adds one $1$ at each step.
- [ ] 44 $(w^R)^{n+1}=(w^R)^n*w^R\overset{IH}{=}(w^n)^R*w^R\overset{38}{=}(w^{n+1})^R$
  - see the ans
    start at $\lambda$
- [ ] 48
  here we prioritize $n$ instead of $m$ as the 5.3.5 prologue shows.
- [x] 49
  1. trivial because positive implies "not exceeding m"
  2. 
  $$
  \begin{align*}
    m=1&\Rightarrow 1\\
    n=1&\Rightarrow 1+1+\ldots+1\\
    m<n&\Rightarrow \text{trivial}\\
    m=n>1&\Rightarrow 1\text{ corresponds to }m\\
    m > n > 1&\Rightarrow 
    \begin{cases}
      \text{either not includes }n &P_{m,n-1}\\
      \text{or includes }n
      \text{, then we select others after having one because the order doesn't matter}n &P_{m-n,n}\\
    \end{cases}
  \end{align*}
  $$
  1. 
  $$
  \begin{align*}
    P_{5,5}&=1+P_{5,4}\\
           &=1+P_{5,3}+P_{1,4}\\
           &=2+P_{5,2}+P_{2,3}\\
           &=4+P_{5,1}+P_{3,2}\\
           &=6+1=7\\
  \end{align*}
  $$
- [ ] 50
  - why Ackermann’s function [not primitive recursive](https://math.stackexchange.com/a/96492/1059606)
    because not having the form "f(n+1) as a function of f(n) only."
  - TODO 
    - [minimization operator](https://en.wikipedia.org/wiki/General_recursive_function#Examples) which differentiate General recursive from Primitive recursive.
    - relation with the [original definition](https://en.wikipedia.org/wiki/Ackermann_function#Definition:_as_m-ary_function).
- [ ] 53
  $$
  n\ge 2\\
  A(2,n)=A(1,A(2,n-1))=\ldots=A(\overbrace{1,A(1,\ldots,A(2,1))}^{(n-1) \; \text{one}})=2^{\ldots}\text{, where n twoes}\\
  A(3,n)=A(\overbrace{2,A(2,\ldots,A(3,1))}^{(n-1) \; \text{two}})\\
  A(3,3)=A(2,A(2,A(3,1)))=A(2,A(2,2))=A(2,2^2)=2^{2^{2^{2}}}=2^16
  $$
- [ ] 54 see the ans
- [ ] 55
  - > If m > 0, this is greater than 0 by the inductive hypothesis
    similar to before, by cycle, $A(m, A(m + 1, k − 1))=A(m, A(m \ldots A(m+1,1)))=A(m,A(m,\ldots A(m,2)))$, it is impossible at the last step to become 
    $A(m,0)$. Also based on $2n,2>0$, so bigger than 0.
    - the last A(m,2) implies $A(m + 1, k − 1)\ge 2.$
- [ ] 56 hinted by 55
  $$
  A(k,0)=A(l,0)=0\\
  \text{Assume }A(k,n)\ge A(l,n),k>l\\
  A(k,n+1)=A(k-1,A(k,n))\\
    \overset{55}{\ge}A(k-1,A(l,n))\\
    \overset{IH}{\ge}A(l-1,A(l,n))=A(l,n+1)
  $$
  - see the ans
    - the above $IH$ is wrong
      because $A(l,n)$ may be not 
      $0$, so we don't know $A(k,m)>A(l,m),m\neq 0$ when only knowing $ A(k,0)=A(l,0)$
- [x] 64
  5-tower of 2 $2^{65536}$ 
### 5.4
- 2~12(here the orders of 4,6 in the ans and the book differ),16~24,27,28,32,36~40,44~46,47 skipped
- [ ] 14 see the ans
  just by removing one mode and forming the recursive list.
  with two special cases, i.e. $n=1$ and mode occupying the entire list.
- [ ] 26 see the ans
  - "ALGORITHM 5" in p268 is not recursive.
- [ ] 30 similar to ALGORITHM 8
  see the ans notice here we don't need one extra $if\;n=1\; \ldots$
- [ ] 34 similar to FIGURE 1, recursive uses $2*4=8$ for $n=5$
  while iterative uses $2*(n-2)=6$
- [ ] 41
  similar to before,
  - n=1 is trivial
  - $n\ge 2$, remove three from the center except for the quarter which has already one missing
    then for the three, use IH,
    for the already missing, also use IH
    use one right triomino for the three removed.
- [ ] 42 here the ans doesn't state how to decide the diagonal.
- [ ] 48
  - see the ans
    - it implies the worst case by the ans
    - TODO 
      - decision tree -> $\lceil\log{n+1}\rceil$
      - b why not $C_{6}^{1}*C_{5}^{1}=30$ ways.
- [ ] 50
  - by [this](https://en.wikipedia.org/wiki/Quicksort#Lomuto_partition_scheme)
    ```bash
    if A[j] <= pivot then 
      ... 
      swap A[i] with A[j] 
    i := i + 1 
    swap A[i] with A[hi]
    ```
    just make all elements on the left side of the pivot are less than the pivot
    but not sort them when `partition`.
  - notice here swap can be done by many ways
    - [1](https://tutswiki.com/data-structures-algorithms/quick-sort/)
      $$
      3,2,\ldots,5,4,6\quad\text{swap 5,2}\\
      3,2,1,\ldots,7,9,5,\ldots\quad\text{swap 7,1}\\
      1,2,3,8,7,9,5,4,6\quad\text{swap 3,1}
      $$
    - [2](https://www.geeksforgeeks.org/implement-quicksort-with-first-element-as-pivot/)
      ~~it should `for (i = high-1; i > low; i–) {` to avoid duplicate swap between `high` self.~~
      $$
      6,4\text{ swap with self}\\
      3,\ldots,2,9,4,6\quad\text{swap 9,2}\\
      3,\ldots,2,1,8,9,4,6\quad\text{swap 8,2}\\
      3,\ldots,1,2,7,8,9,4,6\quad\text{swap 7,1}\\
      3,2,1,5,7,8,9,4,6\quad\text{swap 5,2}\\
      1,2,3,\ldots
      $$
- [ ] 52 see the ans
  if only one element, then $m=k=0$, just return back.
- [ ] 55 [different](https://en.wikipedia.org/wiki/Quicksort) from merge sort worst-case
  $n-1+\lceil\frac{n-1}{2}\rceil-1+\lfloor\frac{n-1}{2}\rfloor-1+\ldots=n-1+(n-3)+\ldots\le \frac{(1+n-1)(\frac{n-1}{2}+1)}{2}=\frac{n(n+1)}{4}=O(n^2)$
### 5.5
- 2~4,6,10 skipped
- [ ] 5 see the ans for formal description.
- [ ] 8 I just use $y=f_i$ this invariant.
  - see the ans
    - before the loop, $i$ is undefined
- [x] 12 I just use $a=dq+r$ this invariant.
### supplementary
- 2~10,14~18,19,20,22(similar to 21),28,32~34,42,70,74 skipped
- [x] 12 $(64k-56n-55)*9+(56n+55)+56=64*9k-64*7n+8*(7-55)=64(9k-7n)+64*(1-7)$
- [ ] 21 
  basis: k=0,1
  inductive: $(f_k+f_{k-1})f_n+(f_k+f_{k+1})f_{n+1}=f_{n+k-1+1}+f_{n+k+1}=f_{n+k+1+1}$
- [ ] 24
  $$
  \text{let }F(m,n)=\frac{m(m+1)\ldots(m+n-1)}{n!}\\
  \text{basis: }F(m,1)\text{ is trivial}\\
  F(m,n)=F(m-1,n)+F(m,n-1)=\ldots+F(m-1,n-1)+F(m,n-1)=F(1,n)+\ldots
  $$
- [ ] 26
  $$
  LHS=\frac{sin((n+\frac{3}{2})x)-sin((n+\frac{1}{2})x)}{2}
  +\frac{sin((\frac{2n+1}{2})x)-sin(\frac{1}{2}x)}{2}\\
  RHS=\frac{sin((\frac{2n+3}{2})x)-sin(\frac{1}{2}x)}{2}
  $$
- [ ] 30
  let $F(k):b^k\le n<b^{k+1}\Rightarrow n=a_k\ldots$
  Then the basis step $F(0)$ is trivial.
  if $F(k)$ then 
  also $F(k+1)$ because $n/b\in [b^k,b^{k+1})$
  - see the ans for uniqueness proof
- [ ] 31
  in summary,
  the $k+1$ lines for $x+y\le k$ can only contain more $k$ points at $x+y\le k+1$, so contradiction.
- [ ] 36
$$
\begin{align*}
  (x_{i-1}x_j+1)(x_{i+1}x_j+1)(x_{j-1}x_i+1)(x_{j+1}x_i+1)=&x_j^2 x_i^2 x_{i-1} x_{i+1} x_{j-1} x_{j+1}\\
  &+x_j x_i^2 x_{i+1} x_{j-1} x_{j+1}+x_j x_i^2 x_{i-1} x_{j-1} x_{j+1}
  +x_j^2 x_i x_{i-1} x_{i+1} x_{j+1}+x_j^2 x_i x_{i-1} x_{i+1} x_{j-1}\\
  &+x_j^2 x_{i-1} x_{i+1}+x_j x_i x_{i-1} x_{j-1}+x_j x_i x_{i-1} x_{j+1}
  +x_j x_i x_{i+1} x_{j-1}+x_j x_i x_{i+1} x_{j+1}
  +x_i^2 x_{j+1} x_{j-1}\\
  &+x_{i-1}x_j+x_{i+1}x_j+x_{j-1}x_i+x_{j+1}x_i\\
  &+1\\
  (x_{i-1}x_i+1)(x_{i+1}x_i+1)(x_{j-1}x_j+1)(x_{j+1}x_j+1)=&x_j^2 x_i^2 x_{i-1} x_{i+1} x_{j-1} x_{j+1}\\
  &+x_j x_i^2 x_{i+1} x_{i-1} x_{j+1}\ldots\text{ here we will get not equal items}
\end{align*}
$$
  - see [this](https://math.stackexchange.com/questions/4820561/how-to-prove-x-1-frac1x-1-cdotsx-n-frac1x-n-ge-x-1-frac1x-2?noredirect=1#comment10259361_4820561) for cyclic meaning and [this](https://math.stackexchange.com/questions/4820561/how-to-prove-x-1-frac1x-1-cdotsx-n-frac1x-n-ge-x-1-frac1x-2?noredirect=1#comment10259372_4820561) extra solution.
- [ ] 38 see the ans
  > Thus c and all the cities with a one-way road to c have a direct road to $c_{k+1}$.
  > All the remaining cities must have a one-way road from them to a city with a one-way road to c (that was part of the definition of c), and so they have paths of length 2 to $c_{k+1}$, via some such city.
  suppose $c_i$ reaches $c$ "via exactly one other city" $c_j$
  then $c_j$ can directly reach $c_{k+1}$ by the 1st quote.
  so $c_i$ reaches $c_{k+1}$ 
  "via exactly one other city" $c_j$.

  Then 3 cases $c$, ones which can directly reach  and ones reaching via one other are all considered.
- [ ] 40
  - here we can't directly add all fuel to prove that it is possible to "complete a lap by obtaining gas from other cars"
    beacuse it **may be not able to reach the next**
    > at least one car c in the group has enough fuel to reach the next car in the group.
  - > now pretend that the car d just ahead of car c is not present, and instead the fuel in that car is in c’s tank
    here the pretension is allowed because
    - > some car in this situation can complete a lap by obtaining fuel from other cars as it travels around the track.
      let this car be $k$
      the fuel of $c$ is $f_c$ and amount of fuel from $c$ to $d$ is $a_c$
      assume $c->d->e$
      - Then with the pretension, from $k$ to $e$, the fuel amount change is $f_{kc}-a_{kc}+(f_c+f_d)-(a_c+a_d)$
        without the pretension, similarly, $f_{kc}-a_{kc}+(f_c-c_c)+(f_d-c_d)$ which is same as the above.
- [ ] 43
  - see the ans
    - > $a_j = 2^{2^{a_{j−2}}}$ is a multiple of $2^s$ 
      here $a_{j-1} = 2^{a_{j−2}}$ is enough
    - TODO [proof of Euler's theorem](https://en.wikipedia.org/wiki/Euler%27s_theorem#Proofs)
    - > for some integer $t_i$ , $a_i = t_i r + c$.
      more specifically to say, $a_i = t_i r + c,i>k$, so we can use induction.
- [ ] 44
  1. trivial 
  2. if $np-q>p$ then we can choose smaller $n'=n-1$ with $n'p-q>0$, contradiction
    so $0<np-q<p$ then use IH.
  - see the ans
    - > The only thing left to check is that p′/q′ < 1/n
- [x] 46
  $$
  M(101)=91\quad\text{trivially}\\
  89<n<101,M(n+1)=91\Rightarrow M(n)=M(n+11-10)=M(n+1)\\
  78<n\le 89,M(n+11)=91\Rightarrow M(n)=M(91)=91\\
  \text{Then similar to above for the rest.}
  $$
  - see the ans for one more elegant description of the above to convey the same idea.
- [x] 48
  $R_{n+1}=R_{n}\oplus A_{n+1}$
  then either only in $R_{n}$, i.e. odd numbers of 
  $A_1,\ldots,A_n$,
  or only in A_{n+1}, then even numbers of $A_1,\ldots,A_n$ plus $A_{n+1}$
- [ ] 49 [see](#5_supplementary_49)
  - [generalization](https://math.stackexchange.com/q/4821113/1059606) to sphere similar to 50
    Then I *rethought* the 5-Supplementary-49 exercise which is about $n$ circles dividing the plane, and I **generalized it to $n$ spheres** with the following *generalized* constraints: every two spheres intersect in exactly one **circle** and no three spheres contain a common circle. Then each new added **arc plane** caused by intersection (similar to "the number of regions into which the previous $n−1$ planes divides plane $n$" in the above comment) between two spheres will divide the region the arc plane is inside.
    So we can also have the following equations for the sphere version:
    $$
    R_2(0)=1,R_2(n)=n^2−n+2,n\ge 1\\
    R_3(n)-R_3(n-1)=R_2(n-1),n\ge 1
    $$

    In short, the above maybe **generalizes plane to curve plane** (more specifically arc plane here).
- [ ] 50 
  - see [this](https://math.stackexchange.com/questions/339750/greatest-number-of-regions-we-can-get-when-dividing-with-lines-and-circles#comment4097417_339853)
    > the number of regions added by plane $n$ is the number of regions split by plane $n$ which is the number of regions into which the previous $n−1$ planes divides plane $n$
    "the number of regions split by plane $n$" is equivalent to "plane $n$ is *splitted into regions*".
    So just think as plane $n$ is fixed, then "the previous $n−1$ planes" interset with plane $n$,
    > any three of these planes have exactly one point in common
    this implis no plane pairs are parallel, then every plane will interset with plane n with one lines,
    so it becomes **$n-1$ lines**,
    then "three of these planes have exactly one point" becomes "two of these lines have exactly one point"
    This exactly means that $n-1$ lines split the plane $n$ into $R_2(n−1)$ regions.
    - [similarly](https://math.stackexchange.com/questions/339750/greatest-number-of-regions-we-can-get-when-dividing-with-lines-and-circles#comment4097420_339853) for $\mathbb{R}^4$ although it is not easy T visualize.
  - The above is same as the ans
- [ ] 51 see [this](https://math.stackexchange.com/a/1965091/1059606)
  - it should be $t\sqrt{2}-t=(t-s)\sqrt{2}>0$
    then $t-s<t$ is minimal, so contradiction.
    - This is just what the hint means
      > Then show that $a\sqrt{2} − a$ is a smaller positive integer of this form.
  - > then contradicting the fact it has a *minimal* element
    so there is no such a "nonempty set of positive integers" $S$ 
    - this is just [infinite descent](https://en.wikipedia.org/wiki/Proof_by_infinite_descent)
- [ ] 52 see the ans
  - checking the entire is enough.
- [x] 54 the algorithm to calculate $\gcd(a_{n-1},a_n)=c_{n-1}a_{n-1}+c_n a_n$ see 4.3-45
  - IMHO the induction should be
    $\gcd(a_1,\ldots,a_n,a_{n+1})=\gcd(\gcd(a_1,\ldots,a_n),a_{n+1})\overset{\text{IH, 4.3-45}}{=}\gcd(\sum_{i=1}^n c_i*a_i,a_{n+1})\overset{\text{4.3-45}}{=}c'(\sum_{i=1}^n c_i*a_i)+c''(a_{n+1})$
- [ ] 56 similar to one exercise before.
  - IMHO, $10x0$ and $0x01$ should be considered.
  - > If the graph stays above the axis, then the string must be of the form $00x1$
    ~~this is based on taking $x$ as one whole entity.~~
    ~~because $00111\overbrace{0\ldots 0}^{\text{six 0es}}1$ will cross the axis.~~
    The above can be splitted into $001$, $110000$, $001$.
- [ ] 58
  1. the basis set $abc,bac,acb$ are trivial
    - suppose $abcx$ and $abxc$, etc, coincide, then $bck$ or $cx_1k$ or $x$ where $k$ is one letter is in the basis set, then $abcabc$ is one case of this condition between $abcx$ and $xabc$.
    - $abxc$: 
      $abx_1$ -> $abc$ but no element starting with $c$ in the basis set, 
      $x_2x_3c$ ~~same as the above.~~ similarly not possible because no $ab$
      $bx_1x_2$ -> $abacbc$ with $axbc$.
    - $axbc$:
    - TODO the above method to find the duplicate seems to drop something.
  [x] 2. trivial.
- [ ] 60 ~~$2^{\frac{6}{2}-1}=4$ possibilities~~
  $()(),(())$ for 4 symbols
  - see the ans
    - the above should be $3^{\frac{6}{2}-1}=9$ by removing duplicates at each exponent calculation.
      so $3^1-1$ when 4 symbols
      and then $1*3+1*2=5$ because $()$ before or after $()()$ are same.
- [x] 62 ~~we can also~~ 
  > Otherwise x = (a) or x = ab
  IMHO, here we should say "use induction on the usage count of the rule".
- [ ] 64
  $$
  \begin{align*}
    \text{only if:}&\\
    &\text{basis step: }\\
    &N(\lambda)=0\\
    &\text{inductive step: }\\
    &N((x)):\\
    &\quad N((x))=1-1+N(x)=0\\
    &\quad N(()>0,N((substr(x))>N(substr(x))\ge 0\\
    &N(xy):\\
    &\quad N(xy)=N(x)+N(y)=0\\
    &\quad N(substr(x))\ge 0,N(x\; substr(y))=N(substr(y))\ge 0\\
    \text{if:}&\\
    &N(\lambda)=0,\text{let }u_1\text{ be the first prefix so that }N(u_1)=0\\
    &\text{trivially the 1st character must be (,then due to }N(u) \ge 0,\text{ we must have pattern }(x)\in B\\
    &\text{then with "(" after something like "(()" we also have pattern } xy \in B\tag*{$\blacksquare$}
  \end{align*}
  $$
  - see the ans
    - the above "only if" is right, while "if" is not strictly.
    - > there are two cases
      i.e. either $N(u)>0$ inside ($N(u)\ge 1$) or at some inside point $N(u)=0$ ($w=ab$).
    - > Furthermore $N(u)\ge 0$ for every prefix u of x, since if N(u) dipped to −1 , then N((u) = 0 and we would be in the first case
      This should be be based on IH because $length(x)<length(u)$
      here trivially we should be based on **even length**.
      - so "N(a) = N(b) = 0" implies even.
        - and
          > $N(u)\ge 1$ for all nonempty prefixes u of w, other than w itself
          implies $N(u_{last})=1,N(w)=0$, i.e. the last character is $)$ and 
          $N(x)=N(u_{last})-1=0$ implying x has even length.
    - 
- [ ] 65
  1. we can also $assert(\text{n is even})$
  2. IMHO $x \in T′ \wedge y \in T′ \cup S′$
- [x] 66 this is same as one exercise before.
- [ ] 68
  similar to p395
$$
\text{let q be outputing }factorial(n)\\
\begin{align*}
  &p\wedge (n=0)\{return\; 0\}q&\text{ basis step}\\
  &p\wedge \neg(n=0)\{return\; n \cdot factorial(n − 1)\}q&\text{ inductive step}\\
\hline\\
&p\{\ldots\}q
\end{align*}
$$
- [ ] 71 see the ans
  if "$a(n)$ is uniquely defined" isn't met, then 
  either $a(n-1)$ or $a(a(n-1))$ has two definitions.
  Then if $a(n-1)\le n-1$, then these two cases are same if using strong induction.
  Then based on strong induction, if $a(k),k\le n$ is well defined, then $a(a(n))$ is well defined, same for $a(n+1)$
- [ ] 72
$$
\mu^2n=1-\mu n\\
(1-\mu n)-\lfloor(1-\mu n)\rfloor\overset{\mu n>0}{=}-\mu n-(-\lfloor(\mu n)\rfloor-1)\\
\text{then combine all together, }(\mu n-\lfloor(\mu n)\rfloor)-\mu n+\lfloor(\mu n)\rfloor+1=1
$$
$$
0\le \alpha<1-\mu\Rightarrow (1 + \mu)(1 − \alpha)\in((1+\mu)*\mu=1,1+\mu<2]\\
\text{Then }\lfloor(1 + \mu)(1 − \alpha)\rfloor+\lfloor\alpha + \mu\rfloor=1+0=1\\
1-\mu\le \alpha<1\Rightarrow (1 + \mu)(1 − \alpha)\in(0,(1 + \mu)*\mu=1)\\
\text{Then }LHS=0+1=1
$$
  - see the ans
    - $\alpha\neq 1-\mu$ because otherwise $(n+1)\mu=1+\lfloor n\mu\rfloor$ contradiction.
    - in summary
      $$
      \alpha=n\mu-\lfloor n\mu\rfloor\in (0,1)\\
      \text{put }a(n) = \lfloor (n+1)\mu\rfloor\text{ in the recursive equation and substitute }\lfloor n\mu\rfloor
      \text{ with }\alpha\\
      \text{Then we need to prove }LHS=\lfloor n\mu+\mu\rfloor+\lfloor(\lfloor n\mu\rfloor+1)\mu\rfloor=n=RHS\\
      \Rightarrow LHS=\lfloor n\mu+\mu\rfloor+\lfloor n\mu^2-\alpha\mu+\mu\rfloor\\
      \text{since no terms can be cancelled, so we add }\lfloor\ldots\rfloor\\
      \begin{align*}
        LHS&=\lfloor n\mu\rfloor+\lfloor\alpha+\mu\rfloor+\lfloor n\mu^2\rfloor+\lfloor 1-\alpha-\alpha\mu+\mu\rfloor\\
        &=\ldots+\lfloor (1-\alpha)(1+\mu)\rfloor\\
        &=1+\lfloor n\mu\rfloor+\lfloor n\mu^2\rfloor\\
        &=1+n\mu+n\mu^2-1=(\mu^2+\mu)n=n\tag*{$\blacksquare$}
      \end{align*}
      $$
      - The key is to find $\alpha$
- [ ] 73
  1. $LHS=\lfloor n\mu\rfloor+\lfloor\alpha+\mu\rfloor=\overset{\alpha<1-\mu}{=}\lfloor n\mu\rfloor$
  - see the ans for how to prove without $\alpha$ as the media
- [ ] 76 see the ans
- [ ] 77
  - by the generation pattern, to get the last n, we need reach
    $a_1$ 1, $a_2$ 2, $\ldots$, $a_n$ n, so $f(n)=\sum_{k=1}^n a_k$
  - see the ans for the rest
## 6
### 6.1
- 2~12,18,22 (similar to 20),28~40,
  44,48~50,
  54~62,66,72 (similar to one exercise in chapter 5, TODO find this specific exercise),
  76~78 skipped
- [ ] 14 see the ans where we need care about $n<2$
- [ ] 16 $4*26^3$
  - see the ans
    - the above will duplicately count $x...$ and $.x..$, etc.
- [ ] 20 see the ans for calculation using detailed maths symbols
- [ ] 22
  h. if directly count, then $0$ should be manipulated specifically because the leading digit is not allowed as 0 automatically.
    $4+9*1+8*4+8*9*1+8*1*4+7*8*4=373$ where 1 corresponds to the corresponding location digit is 0.
- [ ] 24
  c. here if from right to left, then the last digit will be splitted into two cases, i.e. either 0 in the right 3 digits or no 0es in the right 3 digits.
- [ ] 26
  1. see the ans. Here it takes 3 or 4 times as also twice and also allows leading digit 0.
  2. here "exactly" excludes four 9s.
- [x] 42 $C_{4}^3*C_{3}^1*4*3$
- [x] 46 $C_{10}^4*\frac{4!}{4}$ is also ok.
- [ ] 52 see the ans this is similar to EXAMPLE 17.
- [ ] 53 similar to above $2^5+2^4*(6-1)+2^4+2^3*(5-1)-(2+2)*2-5$
  here $-5$ is due to
```bash
000yy
1000y
x1000
xx1000
xxx1000y # here xxx should exclude 000, then multiply by 2 choices of y, we minus 2*1
xxxx1000 # here we exclude 000y(2 choices),1000 so minus 3
```
  since $4*2\not<8$, so we don't need to minus more for "four consecutive 1s".
  The above just means same as [this](https://math.stackexchange.com/a/178610/1059606).
  - Also [see](https://math.stackexchange.com/a/922692/1059606) which uses induction so it doesn't need to care about the above trivial duplicates.
    - > With the initial conditions
      check with $n=3$
     - Also [see](https://math.stackexchange.com/a/4821956/1059606)
        ```python
        a=0
        b=0
        c=0
        sum=0
        for i in range(3,8+1):
          sum=a+b+c+2**(i-3)
          a=b
          b=c
          c=sum
          print("F({0})={1}".format(i,sum))
        ```
  - Also see [this recursion formula][consecutive_zeros_in_bit_strings]
    it is based on constructing with 
    either the first $n-1$ bits have $000$ ($2a_{n-1}$) or not ($2^{n-4}-a_{n-4}$)
    the latter case is due to that we must append 0, so the last 3 of the first ${n-1}$ bits must be 
    $100$ where $00$ is to ensure $000$ after appending and $1$ is to ensure no $000$ in $a_{n-1}$.
    So we only needs to care about $a_{n-4}$ because 
    $1000$ must be ended for $a_{n}$
  - TODO [Goulden Jackson method](https://math.stackexchange.com/questions/4170314/find-a-recurrence-relation-for-the-number-of-bit-strings-of-length-n-by-goulde)
- [ ] 64 see the ans
- [ ] 66
  see [this](https://math.stackexchange.com/a/3358299/1059606) (~~TODO~~ ~~generating function~~) which is similar to [consecutive_zeros_in_bit_strings]
  so in this exercise case 
$$
a_i=2^i,i=0,1,2\\
a_n=a_{n-1}+a_{n-2}+a_{n-3},n\ge 3\quad\text{here we append 1 for n-1,10 for n-2,100 similarly}
$$
  - [generating function](https://math.stackexchange.com/questions/4822021/how-to-use-generating-functions-to-solve-the-problem-number-of-bit-strings-of-l?noredirect=1#comment10263914_4822021)
    See this [code](./miscs_snippets/py_codes/usage.py) for calculation of taylor expansion coefficients.
    - here $(x+x^2)^k$ means
      we can concatenate multiple $0,01$ together.
      e.g. $(x+x^2)^2$ has $2x^3$ corresponding to $0|10$ and $10|1$ both having length 3 (here $|$ is one delimiter for denotation)
    - based on the above pattern, only one $0$ (so coefficient $1$ in $x$ which corresponds to length 1)
      and one $10$ (so coefficient $1$ in $x^2$ which corresponds to length 2)
      are enough to construct all possibilities.
      - It is better to "lop off" the ending "0" at the 1st step $x+x^2$ to help understanding.
    - it also explains [$0,01$ version](https://math.stackexchange.com/questions/4822021/how-to-use-generating-functions-to-solve-the-problem-number-of-bit-strings-of-l?noredirect=1#comment10263823_4822021)
    - This is one more [direct different interpretation of $a_n=a_{n-1}+a_{n-2}$](https://math.stackexchange.com/questions/4822021/how-to-use-generating-functions-to-solve-the-problem-number-of-bit-strings-of-l?noredirect=1#comment10263807_4822021)
    - > as you know the minimum and maximum numbers of strings consisting of 0  and 10  you need to get one with five bits (before you lop off the final 0 )
      i.e. get one with *four* bits corresponding to $x^4$ after lopping.
    - See this [summary](https://math.stackexchange.com/questions/4822021/how-to-use-generating-functions-to-solve-the-problem-number-of-bit-strings-of-l?noredirect=1#comment10262960_4822021) to verify understanding of the problem
      kw: stringing together, do not need that final 0
- [ ] 68 it is just [$2*C_{7}^4$](https://math.stackexchange.com/a/581540/1059606) which is same as [this](http://mathcentral.uregina.ca/QQ/database/QQ.09.01/michelle1.html) where $\frac{7!}{4!3!}$ 
  means all 7 games are labelled differently ($7!$) 
  then $4!$ and 
  $3!$ is based on the division rule to exclude duplicate ones.
- [ ] 70 similar to EXAMPLE 24
- [x] 74 $2^n$ rows where each row has two possibilities, so $2^{2^n}$
## 8
### 8.1
- [ ] 29
  TODO why not $C_{m}^n$
## 9
### 9.6
- [ ] 53
## 11
Redo 5.4-48
### 11
# TODO after abstract algebra
- [this](#RSA_Cauchy_theorem)
# TODO after Computer Networking
- 6.1 -> "1111111 is not available as the netid of a Class A network"
  also "hostids consisting of all 0s and all 1s are unavailable".
- 

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
[lower_bound_second_largest_element]:https://math.stackexchange.com/a/1672/1059606
[consecutive_zeros_in_bit_strings]:https://math.stackexchange.com/a/178613/1059606

<!-- cs stackexchange -->
[O_Theta_Omega_relation_with_limit]:https://cs.stackexchange.com/a/827/161388

<!-- paper or lectures -->
[second_largest_element_Adversary]:https://www.cse.unsw.edu.au/~cs2011/lect/2711_Adversary.pdf
[lec_13_Adversary_Arguments]:https://jeffe.cs.illinois.edu/teaching/algorithms/notes/13-adversary.pdf
[Szwarcfiter_stable_marriage]:https://core.ac.uk/download/pdf/82429549.pdf
[McVitie_stable_marriage]:./papers/McVitie_stable_marriage.pdf
[AHajnal_058]:./papers/AHajnal_058.pdf
[hedetniemi1988]:./papers/hedetniemi1988.pdf
[meisters1975]:./papers/meisters1975.pdf

[csapp_doc]:https://github.com/czg-sci-42ver/csapp3e/blob/master/asm/README.md