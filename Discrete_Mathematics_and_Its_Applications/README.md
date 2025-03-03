Please point out errors if any. Thanks in advance.

abbr:
DMIA -> Discrete_Mathematics_and_Its_Applications

# How long I have taken to read the book
- DMIA
  This book is read from Oct 30 to Feb 20 (3 months and 20 days with 3 days ill).
  Then from Feb 20 to Mar 2 (*12 days*) I got fever again. Then read the book up to Mar 9 (7 days).
  Then up to Apr 10 (*1 months*) I took time to config Rime and other misc things.
  Then Up to Apr 14 (4 days) I read the book.
  So totally I took almost 4 months to read DMIA and finish all necessary exercises without considering related days not reading the book, i.e. italic words.
- mcs
  TODO weird Apr 14 directly read up to chapter 7.
  Up to Apr 26 chapter 7 with necessarily problems solved.
  Up to May 2 migrate from 2017 to 2018 version book and finish before chapter 9.
  Up to May 26 finish the rest. (1 months and 12 days)
# Watching question
- https://math.stackexchange.com/questions/4911036/the-state-machine-for-extended-euclidean-gcd-algorithm-terminates-after-at-mos
- https://math.stackexchange.com/questions/4910633/the-ackermann-function-must-be-total-and-unique-based-on-one-specific-list-of-ru
# notice
- here I may confuse adjacent in trees where I think 2 nodes with the same parents as adjacent (They should be called "[sibling nodes](https://en.wikipedia.org/wiki/Tree_(data_structure)#:~:text=Child%20nodes%20with%20the%20same,case%20it%20is%20called%20empty.)")。
  This is trivially false when thinking such a tree as one graph.
- I skipped [sample tests](./discrete-structure-solution-student39s-solutions-guide_compress_7th.pdf) and test bank.
## errata (The following is added after finishing read. Too late.)
- [no official](https://github.com/lair001/rosen-discrete-math-materials) [Also see](https://overflow.host/posts/2021-02-09/85ad1792-2dfe-11ed-af28-d7ffc61dbf28/)
- [one error](https://www.researchgate.net/post/Error_in_Answer_Key_8th_Edition_Author_Kenneth_H_Rosen_Discrete_Mathematics_and_its_Applications) [Also see](https://math.stackexchange.com/a/4475134/1059606)
# Online Resources
## TODO
- Where is ["expanded table of contents (including subsection heads)"](https://highered.mheducation.com/sites/125967651x/student_view0/)?
  - "Applications of Discrete Mathematics This ancillary contains 24 chapters" may be Answers_to_Odd-Numbered_Exercises (6643.0K) or Crib Sheets (268.0K) which are the only 2 not contained in the "0.1.2 Student Site" list but in [this list on the left](https://highered.mheducation.com/sites/125967651x/student_view0/crib_sheets.html)
  - "immediately preceding this “To the Student” message." may mean "Online Resources" on page xvi.
    The above may also correspond to
    > These resources are described later in the front matter.
- psychology in page 11 has no related contents in the book by searching "psycholo"
- I didn't use "Interactive Demonstrations".
# tips
- [this boy](https://math.stackexchange.com/search?q=user%3A22335+application) reads mcs *many years* after reading DMIA. His QAs are valuable.
  - TODO where is [it](https://math.stackexchange.com/q/168214/1059606) in DMIA
# outline
much of chapter 2,5,6 have been learned before.
- By [this](https://www.reddit.com/r/learnmath/comments/s4hunt/how_long_does_it_take_for_average_person_to_learn/)
  2 months to learn this book may be hard because 1k+ pages of the book Although this says [1 month](https://qr.ae/pKx8wQ)
  > In the 3 months of class ... only covered up to chapter 6
  [Or](https://qr.ae/pKx8gm) which says Knuth is more detailed about this topic which is same as [mathoverflow](https://mathoverflow.net/a/103694) says
  > If you’re a fast reader you can probably get through this book with minimal effort on the exercises in *a few weeks* ... If you take it seriously, and you’re *not already familiar* with any of the contents, there’s easily *more than six months* of work here. Number of hours isn’t a useful metric.
  > In a more demanding textbook, these problems would show up early in the list of exercises, with *no asterisks attached* ... I originally wrote that this book provides over a year of work, but after sampling the exercises I reduced it to half of that, with the caveat that *more demanding* books would give you much better understanding.
  - > (normally they are kinda *duplicates of the even* numbered ones anyway).
- [review by someone](https://www.lesswrong.com/posts/TKguxsjPjXhjQGAqM/book-review-discrete-mathematics-and-its-applications-miri#What_should_I_read_)
- homework is shown in [UC-berkeley](https://math.berkeley.edu/~ribet/55/spring_13/) which only includes part of the book homework.
- I skip [Common Mistakes in Discrete Mathematics](https://highered.mheducation.com/sites/dl/free/125967651x/1106131/Common_Mistakes_in_Discrete_Math.pdf) because it may be a bit redundant.
## courses in some universities using this book
- [ucsd](https://cseweb.ucsd.edu/classes/sp16/cse20-ac/HW8_Sp16.pdf) uses self-designed homework.
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
- remove unnecessary files generated by latex
```bash
$ find . -regextype posix-extended -regex "[0-9a-Z_/\.]*\.(fls|aux|fdb_latexmk|log)" | xargs -I{} rm {}
```
- check filetypes used rarely `$ ls -1R . | grep -E -v ".*\.(md|pdf|bmk|txt)" | grep -E -v ":$" | grep -o -E ".*\..*" | grep -E -v ".*\.(py*|tex)"`
# where to find the detailed answer for odd exercises
- stackexchange
- [filo](https://askfilo.com/user-question-answers-algebra-2/construct-a-turing-machine-that-computes-the-function-for-35383437353333)
- **keywords** using google like "Turing machine function f(n1, n2) = min(n1,n2)" for exercise 13.5-25 "Construct a Turing machine that computes the function f (n1, n 2) = min (n1, n 2) for all nonnegative integers n1 and n2"
## not free
- numerade
- quizlet
- [chegg](https://www.androidauthority.com/what-is-chegg-3273806/)
# similar exercises
- 6-supplementary 32 with something in chapter 5.
- 
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
## prologue and preface
- some highlights are lost due to failure to save.
- data networking [diff](https://www.geeksforgeeks.org/difference-between-network-and-internet/) the Internet
- [formal languages](https://www.oreilly.com/radar/formal-informal-languages/) are more stuctured where [DALL-E](https://en.wikipedia.org/wiki/DALL-E#:~:text=The%20original%20DALL%C2%B7E%20was,3%20modified%20to%20generate%20images.) talks to the person.
  > the language you need to know to talk to DALL-E. Right now, it’s an informal language, not a formal language with a specification in *BNF* or some other metalanguage.

  BNF adds [much limitation](https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_form).
- [one-pass algorithm](https://en.wikipedia.org/wiki/One-pass_algorithm#:~:text=In%20computing%2C%20a%20one%2Dpass,each%20step%20in%20the%20process.) means no extra space needed for input.
  Also [see](https://stackoverflow.com/a/46304200/21294350)
  > The while loop traverses the tree *multiple times*, so no, it is not one-pass.
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
- EXAMPLE 12
  - > There are two possibilities, this is the first move of a winning strategy for the first player, or the second player can make a move that is the first move of a winning strategy for the second player
    i.e. either the 1st win or the 2nd.
    Then
    > instead of eating just the cookie in the bottom right corner, the first player could have made the same move that the second player made as the first move of a winning strategy
    the 1st can use the strategy of the 2nd to replace the 2nd, then win.
    - > , the proof is a nonconstructive existence proof. In fact, no one has been able to describe a winning strategy for Chomp that applies for all rectangular grids by describing the moves that the first player should follow
      i.e. the detailed what to do is not known. So *only prove existence*.
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
  $a_n=f(n)\Rightarrow (f(n)\to a_n,\text{one-to-one from }\mathbb{Z^+})\wedge (f^{-1}(a_n)=n,\text{due to the \textbf{unique} index})$
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
- Here we compare [Cantor_diagonal_argument_string] with ["rational numbers are countable"](https://www.homeschoolmath.net/teaching/rational-numbers-countable.php) <a id="rational_countable_real_uncountable"></a>
  if use the latter for the former, then it will be stuck at the string set $s_1$ if it is the digit which starts with one single zero, so it *can't* prove $\mathbb{R}$ is countable.
  
  If use the former for the latter, due to finite or [infinite **repeat** (the key is $\mod 7$ has finite results, so repeat)](https://math.stackexchange.com/a/1131628/1059606), we can't use the construction method because it *may generate one irrational*. (If taking something like $\overline{01}$ in account, then all can be seen as finite, the construction method can work but it can only generate finite 
  $s_i$ then, so countable) (This seems to be said somewhere in this note).
- > It can be shown that the smallest infinite cardinal numbers form an infinite *sequence*

  [see](https://en.wikipedia.org/wiki/Continuum_hypothesis#Cardinality_of_infinite_sets)
  > Assuming the axiom of choice, there is a unique smallest cardinal number

  the function inherently implies "unique", i.e. only one $y$ for $f(x)=y$.
  - Also [see](#Axiom_of_choice)
- Continuum hypothesis is [not proven at present](https://en.wikipedia.org/wiki/Hilbert%27s_problems#Table_of_problems).
- Here from p203 definition 2, the "onto" to $|A|\ge |B|$ is not direct
  proof see [this](https://math.stackexchange.com/a/286800/1059606) and my [rejected edit](https://math.stackexchange.com/review/suggested-edits/2036195) <a id="onto_compare_cardinality"></a>
  - the 1st part of the proof is same as [this][duality_onto_with_one_to_one] which referenced [here "duality"](https://math.libretexts.org/Courses/Monroe_Community_College/MTH_220_Discrete_Math/Appendices/A.1%3A_Cardinality-additional_info#:~:text=A%E2%89%88C.-,A%20one%2Dto%2Done%20function%20f%20from%20A%20onto%20B,the%20same%20number%20of%20elements.)
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
    it is to prove based on assumption $\forall x\in\mathbb{Z}$
    then $\forall y\notin\mathbb{Z}\Rightarrow x+y\notin \mathbb{Z}$, this contraposition is same as before.
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
- ~~TODO 2.2~~
## 3
- Based on ALGORITHM 3, we use "," to split parameters.
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
    - The wikipedia proof needs much prerequisite knowledge "relies on the following constructs", "Turing-complete", etc. 
      TODO this is out of my current ability.
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
    > *Every* problem in NP is *reducible* to $\scriptstyle C$ in *polynomial* time
    implies
    > if *any* of these problems can be *solved* by a polynomial worst-case time algorithm, then *all* problems in the class NP can be *solved* by polynomial worst-case time algorithms
    - [P](https://en.wikipedia.org/wiki/P_versus_NP_problem#Context) definition 
      kw: solved
      - TODO 
        why NP -> "whose solution can be *found* in polynomial time on a *non-deterministic* machine"
    - better see the [graph](https://en.wikipedia.org/wiki/P_versus_NP_problem#NP-completeness)
      where NP-hard cares about "reducible"
      and NP cares about "solve", i.e. "solved on a deterministic sequential machine" with "polynomial" time.
      Since NP doesn't explicitly say it can't be "solved on a deterministic sequential machine" with "polynomial" time, so $P\subseteq NP$.
- TODO [proof](https://en.wikipedia.org/wiki/Cook%E2%80%93Levin_theorem#Proof) of the Cook-Levin theorem
- [Not all problems are NP](https://qr.ae/psGMxs)
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
- [mathematical analysis](https://en.wikipedia.org/wiki/Mathematical_analysis#Main_branches) includes calculus.
- > there is no multiplicative inverse of 2 modulo 6
  [~~TODO~~](https://math.stackexchange.com/a/2670313/1059606)
- ~~TODO~~ why define [Multiplicative group](https://math.stackexchange.com/a/135928/1059606)?
  All the above 2 strikethroughed are shown in 4.4 .
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
- THEOREM 1 [iff proof (this link gives the proof based on the iff sequence of length 2)](https://math.stackexchange.com/a/2670313/1059606) based on the Bezout's theorem. (i.e. mcs Theorem 9.2.2)
  Also see [coprime_iff_invertible] -> [this (I skipped Remark ...)](https://math.stackexchange.com/a/3290965/1059606)
  - [coprime_iff_invertible]
    - Euler's Theorem seems to only prove one direction.
    - when $b=1$, we have $\gcd(c,m)\ge 1,\gcd(c,m)\mid 1\Rightarrow \gcd(c,m)=1$
    - ~~TODO~~ "conceptual proof" for [~~the "minimal" part~~ "the integers of the form az + bt are exactly the multiples of d." in wikipedia](https://math.stackexchange.com/a/664094/1059606)
      One direction.
      - "closed under subtraction" (trivial to prove) -> "multiple of the least" -> $d\mid a(a\cdot 1+b\cdot 0),b$
      - Proof 1 
        well-ordered is implied by $\{x\in\mathbb{Z}\mid x\ge \ell\}$
      - Remark ... skipped.
    - $3\Rightarrow 4$ since both is on $\mathbb{Z}_n$ (See mcs.)
    - 
  - Based on Extended Euclidean algorithm, $\alpha$/inverse is unique.
    Also see mcs Lemma 9.9.2 which is almost same as exercise 7.
    This basic idea is same as [Identity_Unique].
  - "only if there exist integers ..."
    - [See](https://en.wikipedia.org/wiki/B%C3%A9zout%27s_identity#Proof)
      - > Similarly d is also a divisor
        i.e. $r=b-q'd$
      - > this implies c ≤ d.
        at least $|c|\le |d|$. Since both are positive, we have the above.
- THEOREM 2
  - [alternative proof](https://en.wikipedia.org/wiki/Chinese_remainder_theorem#General_case) although "Case of two moduli" solution is maybe guessed or from [this link2](https://en.wikipedia.org/wiki/Chinese_remainder_theorem#Existence_(direct_construction)) same as the book
    Then see $n_1n_2$ as the new $n_1$ to use IH.
  - link2 
    - refers to Lagrange interpolation which solves the system of *equations* and *sum up sub-solutions* for each equation.
      They are similar.
  - based on [bijective](https://en.wikipedia.org/wiki/Chinese_remainder_theorem#Existence_(first_proof))
    - > Moreover, it cannot be generalized to other situations where the following proof can.
      TODO what are "other situations"?
- Definition 3 is one rephrase of cyclic group.
### 4.6
- > $f(p)=(ap+b)mod\;m$ is bijective if and only if $gcd(a,m)=1$

  based on [this](https://math.stackexchange.com/a/2034684/1059606)
  we prove $(ap)\mod m$ is bijective. ~~Based on this [description](https://math.stackexchange.com/q/4817093/1059606) of the comment,~~
  ~~since both the domain and the codomain are $\mathbb{Z}_m$, so onto is equivalent to one-to-one, then in turn equivalent to bijective, so it is enough to prove only injective.~~
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
  - [basis][Euler_Phi_multiplicative]
    based on the ~~book~~ [SOLUTIONS_8th] p111 table for Chinese remainder theorem ->  *bijection*.
    $f:(a,b)\text{with }a\equiv a\pmod m,b\equiv b\pmod n\to \exists! k\equiv k\pmod{mn}$
    - [$\exists!$](https://math.stackexchange.com/a/1241209/1059606) used in mcs
  - ~~TODO~~ use inclusion-exclusion principle.
    This may be unnecessarily complicate since $A_i\cap A_j$, etc, will rise up to $\bigcap^{i=k_r} A_i$
  - so in RSA, coprime probability is [very high][RSA_coprime_guarantee].
    [~~TODO~~ Euler's theorem $P^{\varPhi(N)}\equiv 1\pmod N$ is not totally same as RSA](https://crypto.stackexchange.com/questions/25648/how-do-we-guarantee-plaintext-is-coprime-in-rsa#comment58896_25648) ~~(i.e. [${\displaystyle (m^{e})^{d}\equiv m{\pmod {pq}}}$][RSA_Fermat_little_theorem])~~ 
    - also [see][RSA_proof] almost same as [RSA_Fermat_little_theorem]
      - > differ in length by a few digits.
        IMHO may to avoid brute-force guess. Otherwise if equal digits, then square $n$ we can almost get the length of the factors which can save some efforts.
        This is also implied in the 2nd "Note:".
      - the 1st "Note:" may be got when $e=\lambda(n)+1$.
      - [this comment](https://crypto.stackexchange.com/questions/1004/does-rsa-work-for-any-message-m#comment29353_1006) implies mcs Problem 9.85. (c).
      - I skip "following another question".
      - Addition 2 is same as [RSA_coprime_guarantee].
      - TODO Addition 3.
- RSA
  - ~~TODO~~ [$\gcd(m,N)=1$](https://crypto.stackexchange.com/a/58182) (This is only as one link to give [references](https://crypto.stackexchange.com/questions/58180/why-does-gcdm-n-have-to-be-1-in-rsa/58182#comment127827_58180))
    > either p and q , and so that rather *leaks* the factorization of N
    - As mcs Theorem 9.10.10 (b) says,
      so the probability of not relatively prime is $1-\frac{(p-1)(q-1)}{pq}$ which is really small.
      - This is same as [this reference][RSA_coprime_guarantee] starting from paragraph 3.
        kw: minuscule in comparison
        - > with overwhelming probability, not coprime to N
          may mean "coprime" instead of "not coprime".
  - why p~~339~~340 $\gcd(e,(p-1)(q-1))=1$
    see ~~[this](https://en.wikipedia.org/wiki/RSA_(cryptosystem)#cite_note-24)~~ [RSA_Fermat_little_theorem] because if the above condition is met, then we can use the **decryption** easily where it is used for $ed-1$.
    - TODO (This needs abstract algebra -> Cauchy's theorem) also [this](https://math.stackexchange.com/questions/1123180/understanding-why-the-public-exponent-e-is-chosen-the-way-it-is-in-rsa#comment2294881_1123643)
      where "an element x of order r" implies [$x^r=x^0=1$](https://en.wikipedia.org/wiki/Cyclic_group#Definition_and_notation) <a id="RSA_Cauchy_theorem"></a>
      It shows if the above condition is not met, then **one-to-mul decryption**.
    - ~~here $m\equiv 0\pmod p$ is the cases where $\gcd(m,p)=1$ doesn't hold~~. trivial <a id="RSA_m_not_coprime_n"></a>
    - TODO 
      - [proof of Carmichael's Lambda Function](https://brilliant.org/wiki/carmichaels-lambda-function/#proof-of-the-formulas)
      - [the 1st paragraph](https://math.stackexchange.com/questions/1552992/show-that-varphi-a-an-is-an-automorphism-of-g-if-g-is-abelian-and/1553015#1553015)\
        - > there it goes any possibility of (uniquely) *recovering* the orginal message.
    - [Proof using Euler's theorem][RSA_Euler_theorem] is almost same since Fermat's little theorem is one special case of Euler's theorem as mcs says.
      It directly manipulates with $n$ instead of $p,q$.
    - [This comment](https://math.stackexchange.com/questions/1123180/understanding-why-the-public-exponent-e-is-chosen-the-way-it-is-in-rsa#comment2291732_1123180) says why "not injective" is not as expected.
      > *Multiple plaintexts* can be encrypted to give the *same crypt* text, which would be bad
  - $2525$ comparison is to ~~ensure~~ check [injective](https://math.stackexchange.com/a/1148743/1059606) which can be decrypted (i.e. the number can be ).
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
- EXAMPLE 5 proof of the division algorithm.
  See [this](https://math.stackexchange.com/questions/499789/proof-of-division-algorithm-using-well-ordering-principle#comment10474315_499789) -> QA which means same.
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
### 6.2
- TODO [infinitely many primes in arithmetical progressions an + b when a and b are relatively prime](https://math.stackexchange.com/a/806948/1059606)
- [EXAMPLE 9](https://math.stackexchange.com/a/1552933/1059606)
  > This means that the remaining nine servers are not enough for the other 10 or more workstations to simultaneously access different servers.
  it means $S_{2\sim 10}$ can't afford the rest workstations, i.e. "10 or more workstations", after excluding "at most 5 workstations"
  > there’s no harm in assuming that the workstations to which $S_1$ is directly connected are among the last five, $W_{11},W_{12},W_{13},W_{14}$, and $W_{15}$
  this is trivial, or see [this](https://math.stackexchange.com/questions/4820561/how-to-prove-x-1-frac1x-1-cdotsx-n-frac1x-n-ge-x-1-frac1x-2#comment10259361_4820561) -> [this](https://en.wikipedia.org/wiki/Cyclic_permutation)
  Or it can be seen as that we can label workstations arbitrarily whatever we want to do.
- based on [this](https://math.stackexchange.com/a/42631/1059606) (also see [more graphs](https://en.wikipedia.org/wiki/Theorem_on_friends_and_strangers))
  > either three mutual friends or three mutual enemies
  so here two cases of "either or" can be achieved at the same time, i.e. we can draw *both* one red and one blue triangles among six vertices.
  More specifically, it means $p\vee q$ so $p,q=T$ can be contained. <a id="Ramsey_theory"></a>
- EXAMPLE 7 b
  here
  > We do not use the generalized pigeonhole principle to answer this question, because we want to make sure that there are three hearts, not just three cards of one suit.
  it means the "pigeonhole principle" doesn't care about what hole the pigeon is in, so when specifying hole (i.e. "hearts" here), we can't use the principle.
- > either $a_s < a_t$ or $a_s > a_t$
  implies "either strictly increasing or strictly decreasing".
- After all, the Pigeonhole Principle is based on chapter 1 contradiction proof, i.e. assuming not $at least$, then at most -> leading number contradiction.
### 6.3
- p457 
  > a bijection between subsets of S with r elements and subsets with n − r elements
  trivial due to each $n-r$ obviously has **only one** corresponding $r$
  and $n-r$ must has one $r$ corresponded.
- "poker hand" is just one basic counting unit.
### 6.5
- [Combinations with repetitions](https://math.stackexchange.com/a/128064/1059606) allowed
- example 6
  select $m$ elements -> reorder them in the nondecreasing order which corresponds to **one unique sequence**.
  since the reorder is done after selection, so selection is unordered.
- > Then cards dealt to the *first player* *correspond to* the cards in the *positions* assigned to objects of the *first type* in the permutation

  here "correspond" implies one-to-one from distribution of hands of 5 cards to permutations ~~positions~~ (i.e. the 2nd player, etc, can't be mapped to 1st). It also implies onto because the correspondance always holds so we can always find what to be mapped to the ith type. More intuitively, $\text{let }(i,a_i)\text{ means } i\text{th card goes to }a_i\text{th player},\text{while it can be \textbf{also} interpreted as }i\text{th location goes to }a_i\text{th type}$. See exercise 50 map.
  - The above means
    $a,b,c,d,e$ cards where the order doesn't matter correspond to the $a,b,c,d,e$ location where the order also doesn't matter. Here although indistinguishable items are *same*, their **locations are not**.
    - More specifically
      card -> location
      player -> type (one player has many cards -> one type has many locations)
    - Also [see](#comparison_6_5_theorem_3_with_4) and exercise 49,50 ans where 50 is similar to the above with the map corresponding to the above $\text{card/location}\to \text{player/type}$.
  - It is also shown in the relation between example 7 and theorem 3 where both use the same form of products among $C(n_i,k_i)$
- theorem 3 can be also seen as
  first thinking of all distinguishable, then $n!$
  then divide by duplicate situations, then $/\Pi n_i!$
- EXAMPLE 9 think it as map tuple $(ball,bin)$ where bin can be duplicately shown.
- Stirling numbers of the second kind formula proof
  - [Cynthia_and_Chahat] p9
    - We can use [inclusion-exclusion principle](https://en.wikipedia.org/wiki/Inclusion%E2%80%93exclusion_principle) based on [**the number of elements excluded**](https://math.stackexchange.com/a/550504/1059606) which is same as what [wikipedia](https://en.wikipedia.org/wiki/Stirling_numbers_of_the_second_kind#Explicit_formula) says, i.e. $X_j$. <a id="Stirling_number_second_kind_inclusion_exclusion"></a>
      - here $k^n$ contain all cases ~~including choosing $i,i=1,2,\ldots,k$ Ice Cream.~~ not excluding any ice-cream.
        - similarly $\binom{k}{1}(k-1)^n$ contain all cases ~~including choosing $i,i=1,2,\ldots,k-1$ Ice Cream.~~ excluding one specific ice-cream where we have $\binom{k}{1}$ choices to choose this excluded one.
        - based on this exclusion process and sum/minus them, we will get one set which **doesn't exclude anything** at the end.
      - one more [elegant description](https://math.stackexchange.com/a/436735/1059606) where $f^{-1}(b)=\varnothing$ denotes exclusion from the range.
    - [incl_excl_n]
      - here just append $P(\bigcup_{i=1}^n E_i)$ with related elements of 
        $P(E_{n+1})$ **based on $n=2$** version of inclusion-exclusion principle.
      - Also see the book p606 proof which is directly based on combinatorial view.
        - and the book 8.5-24 is same as the above paper where it uses n terms $A_i,\dots,A_{n-1},A_n\cup A_{n+1}$ <a id="inclusion_exclusion_mathematical_induction"></a>
          while here it uses 2 terms first $\bigcup_{i=1}^n A_i,A_{n+1}$
          - It uses basis at the end
            $\sum |A_{i_1}\cap\cdots\cap A_{i_m}\cap A_{n}|+\sum |A_{i_1}\cap\cdots\cap A_{i_m}\cap A_{n+1}|$ contributes to $\binom{n+1}{m+1}$
            and $\sum |A_{i_1}\cap\cdots\cap A_{i_m}\cap A_{n}\cap A_{n+1}|$ contributes to $\binom{n+1}{m+2}$
            and the sign depends on the sign of $\sum |(A_{i_1}\cap\cdots\cap A_{i_m})\cap (A_{n}\cup A_{n+1})|$
  - definition
    > Equivalently, they count the number of different *equivalence relations* with precisely k *equivalence classes* that can be defined on an n element set
    here 
    *equivalence* class -> "*indistinguishable* boxes" in the book
    - the above one is difficult to interpret $\genfrac\{\}{0pt}{}{n}{0}$ and 
      $\genfrac\{\}{0pt}{}{0}{n}$
      because n classes in 0 element set or 0 classes in n element set (intuitively there is at least one class).
    - use [this](https://en.wikipedia.org/wiki/Stirling_numbers_of_the_second_kind#Recurrence_relation) to
      interpret $\genfrac\{\}{0pt}{}{0}{n},\genfrac\{\}{0pt}{}{n}{0}$
      - > either *contains* the (n+1)-th object as a *singleton* or it does *not*
        i.e. either $\genfrac\{\}{0pt}{}{n}{k-1}$ or 
        $k\genfrac\{\}{0pt}{}{n}{k}$
      - Then $\genfrac\{\}{0pt}{}{1}{1}=\genfrac\{\}{0pt}{}{0}{1}+\genfrac\{\}{0pt}{}{0}{0}$
        - obviously here to split the rest 0 element into $k=1$ classes (i.e. 0 elements) ~~if not choosing the only one element~~, it is impossible, so $\genfrac\{\}{0pt}{}{0}{1}=0$ which can be generalized to $\genfrac\{\}{0pt}{}{0}{k},k>0$
        - Then if choosing the only one element, then nothing more needs to be done, so $\genfrac\{\}{0pt}{}{0}{0}$ should be [Vacuous Product](https://proofwiki.org/wiki/Number_to_Power_of_Zero_Falling_is_One)
          - here [$\Pi$](https://proofwiki.org/wiki/Definition:Continued_Product/Vacuous_Product) implies Vacuous Product should be 1.
      - Similarly, ${n+1 \brace 1}=1*{n \brace 1}+{n \brace 0}$
        Here selecting one element as the only one subset with leaving the rest in no class is impossible, 
        so ${n \brace 0}=0$.
      - Also let $n=k-1$ although it is disallowed, we can get ${k-1 \brace k}=0$. This is one [generalized one](https://en.wikipedia.org/wiki/Stirling_numbers_of_the_second_kind#Table_of_values) <a id="k_minus_one_k"></a>
    - The above *Recurrence* can be [related](https://proofwiki.org/wiki/Equivalence_of_Definitions_of_Stirling_Numbers_of_the_Second_Kind#Proof) with falling factorial powers definition
      - [elegant one](https://math.stackexchange.com/a/2471031/1059606) corresponding to [Induction_Step](https://proofwiki.org/wiki/Equivalence_of_Definitions_of_Stirling_Numbers_of_the_Second_Kind#Induction_Step)
        here step 1 is similar to [this](https://mathoverflow.net/a/413385) where both splits one term $x$ to make 2 more smaller terms.
      - falling factorial can be also [related](https://math.stackexchange.com/a/3418042/1059606) with the original *combinatorial* definition and *permutation with repetition* with *order*.
        so we use $m!$ in the link
      - here we only needs to be based on $k=1$, so the above elegant one use $\sum_{k=1}^{n-1}$
        $k=0,1$ are trivial.
    - [exponential generating function](https://math.stackexchange.com/a/2308579/1059606)
      - here $k=0$ is trivial where $LHS={0 \brace 0}*1$.
      - based on [this](#k_minus_one_k)
        $$
        \text{let }F(k,t)=\sum_{n=k}^\infty {n\brace k}\frac{t^n}{n!}\\
        \frac{\partial LHS}{\partial t}=\frac{\partial F(k,t)}{\partial t}\\
        =\sum_{n=k}^\infty (k*{n-1\brace k}+{n-1\brace k-1})\frac{t^{n-1}}{(n-1)!}\\
        \overset{{k-1\brace k}=0}{=}k*\sum_{n=k+1}({n-1\brace k}\frac{t^{n-1}}{(n-1)!})+F(k-1,t)\\
        =k*F(k,t)+F(k-1,t)
        $$
        Then we solve this partial derivative equation.
- Stirling numbers of the first kind
  - compared with the second kind
    It will reorder inside cycles self based on split into $k$ sets by ${n\brace k}$.
  - It is trivial from Algebraic or Combinatorial to [Recurrence](https://en.wikipedia.org/wiki/Stirling_numbers_of_the_first_kind#Recurrence_relation)
    - > inserting the new object immediately *following* any of the $a_{i}$ already present.
      because before $a_1$ or after $a_j$ are same.
  - "combinatorial definition of the signless Stirling numbers of the first kind" [*relation*](https://math.stackexchange.com/questions/4824460/combinatorial-proof-for-stirling-number-of-1st-kind#comment10270394_4824743) with "the definition of Stirling numbers of the first kind".
    This is same as the [answer_1](https://math.stackexchange.com/a/2704143/1059606) refered to
    - [Flagpoles with flags](https://www.chegg.com/homework-help/questions-and-answers/exercise-3-n-distinct-flags-row-k-flagpoles-job-put-flags-poles-may-leave-poles-empty-also-q114469081)
    - The key idea is that [canonical cycle notation](https://en.wikipedia.org/wiki/Permutation#canonical_cycle_notation) will "fix a certain order".
      - how this notation works
        [see](https://en.wikipedia.org/wiki/Permutation#Cycle_notation) $\sigma=265431$ and [this](https://en.wikipedia.org/wiki/Cyclic_permutation#Definition) which implies cyclic permutation.
        - notice in [product of cycles](https://math.stackexchange.com/a/484959/1059606),
          $(14)$ in $(1532)(14)\ldots$ means the number $1\to 4$ instead of index, i.e. after $(1532)$ we do at the 1st location $5\to 4$.
      - So $(9\,5)(3\, 4)(2)(1\, 8\, 6\, 7)$ and $(5\,9)(3\, 4)(2)(8\, 6\, 7\, 1)$ can't exist.
    - For answer_2, we can use the [stirling_numbers_first_kind_simulation] to find the pattern as the [edit][stirling_numbers_first_kind_proof] says.
    - This [comment](https://math.stackexchange.com/questions/3878162/why-are-stirling-numbers-of-the-first-kind-related-to-the-number-of-permutations/3878213#comment8001109_3878213) may mean for rows like the 1st row $x+\overbrace{1+\dots+1}^{n-1\; times}$. Then it means choices of $x$ from $x+\overbrace{1+\dots+1}^{n-(n-k+1)=k-1\; times}$ to $x$. But this is not what the answer author means.
  - TODO 
    - the [relationship](https://math.stackexchange.com/a/49496/1059606) between Stirling numbers of the first and second kind
### 6.6
- lexicographic (or dictionary) ordering is one type of canonical cycle notation.
- > It is left for the reader to show that this produces the next larger r-combination in lexicographic order.
  here "lexicographic order" implies that $a_i\le n-r+i$,
  so "locate the last element ai in the sequence such that $a_i \neq n − r + i$." will ensure all later elements $a_k,k\ge i$ are their corresponding **largest in their possible** choices. So we can only add $a_i$ if increasing from right to left similar to the **carry** in the normal addition process. Then the carry and the **increasing order** needs $j-i$ in $a_j=a_i+1+j-i$.
  - Also see exercise 11 which is same as the above.
- > (The verification of this fact is left as an exercise for the reader.)
  - Also see exercise 10
  - Similar to comparison between normal numbers, we begin from right to left.
    $a_{j+1}>a_{j+2}>\dots>a_n$ means they are **largest** using $a_{k},k=(j+1)\sim n$ since each digit from left to right is the largest possible one, so we can't rearrange them to get the next larger. This corresponds to exercise 10 ans
    > the old permutation was the **last** one with $a_1 , a_2 , \lodts , a_{j−1} , a_j$ in those positions

    $a_j<a_{j+1}$ means it can be enlarged.
    - Then use the above process again with $a_j$
      - ALGORITHM 1
        here after "interchange $a_j$ and $a_k$", $a_j'=a_k,a_{k-1}>a_k>a_j=a_k'>a_{k+1}$, so the decreasing order of 
        $a_{j+1}>a_{j+2}>\dots>a_{n-1}>a_n$ still holds.
      - ~~so $a_j$ with $a_{k+1},\dots,a_n$ can't be enlarged due to $a_j>$~~
        Since we need to find the next one adjacent number larger than original, it must be bigger than the original at $j$th digit, so we find the **smallest** $a_k>a_j$. Then to get the **smallest** next larger, we list increasingly from left to right for the rest digits. This corresponds to exercise 10 ans
        > Furthermore the new permutation is the **first** one (in lexicographic order) with $a_1 , a_2 , \lodts , a_{j−1} , a_k$ in positions 1 to j
        > Since $a_k$ was picked to be the **smallest number greater** than $a_j$ among $a_{j+1} , a_{j+2} , \ldots , a_n$, there can be no permutation between these two.
## 7
### 7.1
- [Full house](https://en.wikipedia.org/wiki/List_of_poker_hands#Full_house) Also [see](https://zh.wikipedia.org/zh-cn/撲克牌型#牌型)
### 7.2
- [such as days nine months after some holidays including New Year’s Eve](https://www.jpost.com/judaism/jewish-holidays/article-718814)
- TODO 
  - here
    > The probability that a chip is good, but that it came from an untested batch
    whether "from an untested batch" or not is both $0.9$. <a id="success_probability_whether_tested_or_not"></a>
  - > a composite integer n passes Miller’s test for fewer than n/4 bases b
    - why must fail
      > the procedures used to decrypt messages will not produce the original encrypted message
- theorem 3 is based on complementary set.
  - theorem 4
    - > we assume that it is equally likely for two people to be friends or enemies.
      This has one implicit possibility $p_1<1$ which needs to be multiplied.
      - so $p(\bigcup_{i=1}^{\binom{n}{k}} E_i) < 1$ should be $p(\bigcup_{i=1}^{\binom{n}{k}} E_i)*p_1 < 1$
      - Also $p(E_i) = 2*(1/2)^{k(k−1)/2}$ overcounts.
        so the real probability $p(\bigcup_{i=1}^{\binom{n}{k}} E_i)<\binom{n}{k}*2*(1/2)^{k(k−1)/2}$ instead of $\le$ although the final result is same.
### 7.3
- > suppose we know the percentage of people who have a particular disease
  we know $F=\{\text{people who have a particular disease}\}$, then we can know 
  $P(\overline{F})$
  > determine this probability, namely, the probability that a person has the disease given that this person tests positive for it
  $E=\{\text{this person tests positive for it}\}$ and we want to know $P(F\vert E)$
  > need to know the percentage of people who do not have the disease but test positive for it and the percentage of people who have the disease but test negative for it
  i.e. we know $P(E\vert \overline{F})$ and 
  $P(\overline{E}\vert F)$
  Then we can know $P(E\vert F)=1-P(\overline{E}\vert F)$
  - Then it becomes example 1.
  - > the percentage of incoming e-mail messages that are spam.
    we know $F=\{\text{incoming e-mail messages that are spam}\}$
    - > the occurrence of words in the message
      $E=\{\text{occurrence of words in the message}\}$ 
      > We will see that we can determine the likelihood that an incoming e-mail message is spam using the occurrence of words in the message
      and we want to know $P(F\vert E)$
    - > the percentage of spam messages in which each of these words occurs, and the percentage of messages that are not spam in which each of these words occurs
      we know $P(E\vert F)$ and 
      $P(E\vert \overline{F})$
    - Then it becomes example 1.
- [asymptotic](https://math.stackexchange.com/a/1238615/1059606) series
- Bayesian poisoning [type II error](https://en.wikipedia.org/wiki/Bayesian_poisoning) is based on [training](https://security.stackexchange.com/a/12592)
  > By sending lots of correct words and a few words which are used in spam, like viagra, those words get a lower spam notification (*over time*).
  > This means that *after a while* they can get real spam with links through to the filter.
  So for EXAMPLE 4 in the book, $p(stock)$ will be low. Then 
  $r=1-\frac{\Pi q_i}{\Pi q_i * \Pi p_i}$ will be low.
### 7.4
- > the expectation is defined only when the infinite series in the definition is absolutely convergent
  see [this](https://en.wikipedia.org/wiki/Expected_value#Random_variables_with_countably_many_outcomes) and [math_stackexchange](https://math.stackexchange.com/a/4116131/1059606) (TODO Lebesgue integral)
- THEOREM 2
  here "by Exercise 21 in Section 6.4" should be "by Exercise 25 in Section 6.4".
- EXAMPLE 6
  although as [this](https://math.stackexchange.com/q/2877418/1059606) says, $X_i$ are not independent where that $n-1$ people are [fixed](https://proofwiki.org/wiki/Closed_Form_for_Number_of_Derangements_on_Finite_Set) (this link about cases about "fix" is from [this link](https://proofwiki.org/wiki/Hat-Check_Problem) 2. here $D_n=n!-W=n!+\sum_{p=1}^n (-1)^p\frac{n!}{p!}=n!\sum_{p=0}^n (-1)^p\frac{}{p!}$) will also fix the $n$th. <a id="hat_check_Inclusion_Exclusion"></a>
  But based on [permutations count](https://math.stackexchange.com/a/4830206/1059606), we can easily get the expectation (Also see [this](https://math.stackexchange.com/questions/627913/question-on-the-hat-check-problem#comment5028877_628851) for why the order doesn't influence here)
- THEOREM 5
  here $\sum\limits_{r_2\in Y(S)}$ should have only one possible value.
- COROLLARY 1 is just by definition 1.
- > the Bienaym ́e-Chebyshev inequality, which provides a simple proof of the law of large numbers
  see [this](https://en.wikipedia.org/wiki/Law_of_large_numbers#Proof_using_Chebyshev's_inequality_assuming_finite_variance)
- TODO
  > a generalization of Laplace’s least square method
- Bienaym ́e’s [formula](https://en.wikipedia.org/wiki/Bienaym%C3%A9%27s_identity) for the variance of a sum of random variables
- > tells us that $V (X_1) = V (X_2) = 35/12$.
  due to $\frac{\sum\limits_{k=1}^6 k^2}{6}-(\frac{\sum\limits_{k=1}^6 k}{6})^2=\frac{6*7*13/6=91}{6}-\frac{49}{4}=\frac{91*2-3*49}{12}$
  [$\sum n^2$](https://brilliant.org/wiki/sum-of-n-n2-or-n3/#sum-of-the-squares-of-the-first-n-positive-integers)
- > he developed a new method for approximating the roots of equations
  it seems to be [degree-3 approximation](https://www.engineeringletters.com/issues_v28/issue_4/EL_28_4_35.pdf) based on the Newton’s method with $x_{n+1}-x_n$ approximation from (6) to (7).
## 8
### introduction
- > How many bit strings of length n do not contain two consecutive zeros?
  see [this](#no_two_consecutive_1s)
- > Many other kinds of counting problems *cannot be solved* using the techniques discussed in Chapter 6
  - > How many ways are there to assign seven jobs to three employees so that each employee is assigned at least one job? 
    TODO this can be done by bars and stars in section 6.5 $\binom{3-1}{(7-4)+3-1}$
- > though there can be recursive definitions that are not recurrence relations because they take *no numbers* or formulas, but *other objects*.
  the above is from [diff](https://qr.ae/pKaSy1) between recurrence relation and recursive definition.
  see [this](https://en.wikipedia.org/wiki/Recursion#Formal_definitions) for examples.
### 8.1
- > a sequence is called a solution of a recurrence relation
  So a recurrence relation can have [multiple solutions](https://math.stackexchange.com/questions/285134/can-a-recurrence-relation-have-more-than-one-exact-solution#comment10285188_285134).
  - [This](https://math.stackexchange.com/a/285139/1059606)
    - degree of [homogeneity](https://en.wikipedia.org/wiki/Homogeneous_function) should be 1
    - > the solutions form a two dimensional vector space
      this is based on the [map](https://math.stackexchange.com/a/3299728/1059606) $f:(T(0),T(1))\to (c_1,c_2)$
      here we need to exclude the condition that $(c_1,c_2)$ are all on one line.
      - ["isomorphism", i.e. "one-to-one correspondence",](https://www.britannica.com/science/isomorphism-mathematics#:~:text=isomorphism%2C%20in%20modern%20algebra%2C%20a,each%20natural%20number%20by%202.) is due to linear.
        For here, it is due to the inverse of the relation matrix exists.
        $$
        \begin{bmatrix*}
          1&1\\
          r_1&r_2
        \end{bmatrix*}^{-1}
        $$
- EXAMPLE 2 same as [wikipedia](https://en.wikipedia.org/wiki/Tower_of_Hanoi#Logical_analysis_of_the_recursive_solution)
  - > as long as a disk is never placed on top of a smaller disk
    The following is got before reading the book related contents:
    obviously we must move the above $n-1$ out before moving the $n$th to the bottom of one of the other rods, then based on the above [assumption, i.e. the wikipedia's 3rd](https://en.wikipedia.org/wiki/Tower_of_Hanoi#Origins) and the induction hypothesis, we at least need $H_{n-1}$.
    Then $1$ step to move $n$th.
    Then similarly another $H_{n-1}$ to move back above the $n$th.
  - > have already moved the n − 1 smaller disks onto a peg 
    not 2 because we need one spare to place the largest after $n-1$ above ones have been moved.
- > we will perhaps somewhat impertinently call it the “presumed optimal” algorithm for this puzzle
  the above is from [St94](https://www.cs.wm.edu/~pkstoc/boca.pdf) where the optimal solution may be invalid for the ["Frame–Stewart algorithm"](https://en.wikipedia.org/wiki/Tower_of_Hanoi#Frame%E2%80%93Stewart_algorithm) <a id="Frame_Stewart"></a>
- > dissecting a polygon into triangles using non-intersecting diagonals
  see [paper][a000108_11]
  - First argument
    - here $r=1$ one polygon corresponding to $r+1$ will disappear
    - here RHS is done by
      1. select one origin point.
      2. "Fix a side" which has $n-2$ possibilities based on the origin point.
      3. dissect "two polygons"
  - Second argument
    - $(n-3)\times 2$ is due to "one dissection" has $n-3$ diagonals, then based on "direction", $(n-3)\times 2$
    - it is based on choosing the "directional diagonal".
      - Then RHS 
        - $n$ is due to selecting diagonal for $D_{r+1}D_{n-r+1}$ by choosing two points with 
          $r-1$ points between clockwise
  - induction
    - $\frac{(2r-4)!}{(r-1)!(r-2)!}\overset{\text{cancel out }(r-2)!}{=}2^{r-2}*\frac{(2r-4-1)!!}{(r-1)!}$
      - for the rest 
        $D_n=2^{n-2}*\frac{(2n-5)!!}{(n-1)!}=2^{n-2}*(2*(-2)^{n-2})*\frac{\frac{1}{2}*\overbrace{(-n+\frac{5}{2})^{\overline{n-2}}}^{n-2\text{ terms}}}{(n-1)!}=2^{n-2}*(2*(-2)^{n-2})*\binom{\frac{1}{2}}{n-1}$ (Notice here is $-n+\frac{5}{2}$ instead of the paper $-n-\frac{5}{2}$)
        $D_{i+2}D_{r-i}=2^{r+2-2*2=r-2}*(2^2*(-2)^{r+2-2*2=r-2})*\binom{\frac{1}{2}}{i+1}*\binom{\frac{1}{2}}{r-i-1}$
    - Here we use [General Binomial Theorem](https://proofwiki.org/wiki/Binomial_Theorem/General_Binomial_Theorem/Proof_1) (see the related [question](https://math.stackexchange.com/q/4832012/1059606))
      - better see [proof 3](https://proofwiki.org/wiki/Binomial_Theorem/General_Binomial_Theorem#Proof_3)
      - Then we can get the relation between $\binom{\frac{1}{2}}{i+1}*\binom{\frac{1}{2}}{r-i-1}$ and 
        $(1+x)^{\frac{1}{2}}$
    - $D_{r+1}=4^{r-1}*2*(-1)^{(r-1)+(r-1)}*\frac{(\frac{1}{2})*(\frac{1}{2})^{\overline{r-1}}}{r!}\overset{\text{cancel }2^{r-1}, 2}{=}2^{r-1}\frac{(2r-3)!!}{r!}$
  - (4)
    - here we will get $D_{n}=\frac{2^{n-2}(2n-5)!!}{(n-1)!}$ <a id="a000108_11_4"></a>
      which is same as the second to last equality in "... as required"
  - $\frac{-1}{2}(1-4x)^{\frac{1}{2}}$
    coefficient of $x^{n-1}$ is
    $(-1)^n\binom{\frac{1}{2}}{n-1}4^{n-1}*\frac{1}{2}=(-1)^{n+(n-2)}\frac{\frac{1}{2}*(\frac{1}{2})^{\overline{n-2}}}{(n-1)!}4^{n-1}*\frac{1}{2}=\frac{2^{n-1}}{2}\frac{(2(n-3)+1)!!}{(n-1)!}$ which is same as the [above](#a000108_11_4).
- EXAMPLE 6
  - > exponential worst-case complexity
    at least $O(2^n)$ because 
    $max (w_j + T (p( j)), T ( j − 1))$ will have two sub-calculations for *each* $T(j)$.
  - > the maximum total attendance is found using the optimal solutions of the overlapping subproblems
    here "overlapping" is due to $T (p( j))$ may overlap among different 
    $T(j)$.
### 8.2
- [Homogeneous recurrence relation](https://math.unm.edu/~jvassil/Recurrence%20Relations.pdf) is similar to [Nonhomogeneous differential Equation](https://math.libretexts.org/Bookshelves/Calculus/Calculus_(OpenStax)/17%3A_Second-Order_Differential_Equations/17.02%3A_Nonhomogeneous_Linear_Equations)
  Also see this [more intuitive](https://calcworkshop.com/combinatorics/recurrence-relation/)
- > We know that {$a_n$} and {$\alpha_1 r_1^n + \alpha_2 r_2^n$ } are both solutions of the recurrence relation $a_n= c_1 a^{n−1} + c_2 a^{n−2}$  and both satisfy the initial conditions when n = 0 and n = 1
  This is due to both conform to "the recurrence relation" with $\alpha_1 r_1^n + \alpha_2 r_2^n$ proved in the "if" case.
  Then [based on induction](https://math.stackexchange.com/questions/3916854/how-to-prove-uniqueness-of-a-solution-to-a-recurrence-relation#comment8077968_3916854), they are same.
### 8.3
- > reduces the problem of the multiplication of two integers to three multiplications of pairs of integers with half as many bits
  see [this "Being Clever"](https://www.cs.cmu.edu/~cburch/pgss99/lecture/0721-divide.html)
  - Based on "IN Multiply(10, 5)" case
    here 
    > Let aL and aR be left and right halves of a.
    > Let bL and bR be left and right halves of b.
    should be both based on $n$.
  - See example 4.
- example 1: 2 -> $i<j$ and $x>a_m$
- example 3: $n$ is due to LEMMA 1 in section 5.4.
- > Each of the additions, subtractions, and shifts uses a constant multiple of n-bit operations,
  maybe based on $2n$ like in $2^n$.
- EXAMPLE 12
  - > This selection is a task that can be done with O(n) comparisons
    based on selection of the split point.
  - > at most eight points
    it is based on $d=min(d_L,d_R)$.
    - notice here 7 points may be larger than the practical.
    - why not use the circle instead of the rectangle?
  - $f(n)$ is the number used to find the largest.
  - sort ($2O(n\log{n})$) -> choose the split line (2 subsets) $O(n)$ by comparing the size of the subset with the half of the *current total* set
    at each step of $O(\log{n})$ steps 
    and then $f(n)=O(n\log{n})$.
### 8.4
- > Because the powers of x are only place holders for the terms of the sequence in a generating function, we do not need to worry that G(1) is undefined
  Based on [this](https://www.math.cmu.edu/~ploh/docs/math/2011-228/mit-ocw-generating-func.pdf), it means we normally doesn't assign one value to $x$.
  - So we can always care about only the convergent series.
    > However, when formal power series are convergent, valid operations carry over to their use as formal power series.
    and think $x^i$ as one term instead of one number
    > by picking a term in the first sum $x^{e_1}$ , a term in the second sum $x^{e_2}$ , and a term in the third sum $x^{e_3}$
- > Theorem 1 is valid only for power series that *converge* in an interval, as all series considered in this section do
  TODO why only valid for convergent series?
- table 1 [$\ln(1+x)$](https://math.stackexchange.com/a/878376/1059606)
- example 10 is similar to [this](https://math.stackexchange.com/q/4822021/1059606)
  - > Furthermore, a computer algebra system can be used to do such computations
```python
from sympy import *
import math
x, y, z,a = symbols('x y z a')
init_printing(use_unicode=True)

range_list=[(2,5),(3,6),(4,7)]
product=1
for Range in range_list:
    factor=0
    for i in range(Range[0],Range[1]+1):
        factor+=x**i
    product*=factor
p = Poly(product, x)
# https://stackoverflow.com/a/60549033/21294350
{x**m[0]:p.coeff_monomial(m) for m in p.monoms()}
# https://stackoverflow.com/a/24127329/21294350
p.coeffs()
# example 11
sum=0
for i in range(2,5):
  sum+=x**i
def coeffs(poly):
  print({x**m[0]:poly.coeff_monomial(m) for m in poly.monoms()})
coeffs(Poly(sum**3,x))
# example 12
base=x+x**2+x**5
sum=0
for i in range(0,8):
  sum+=base**i
coeffs(Poly(sum,x))
```
- > This example shows that the binomial theorem, which can be proved by mathematical induction
  See [this](https://en.wikipedia.org/wiki/Binomial_theorem#Inductive_proof)
  Here $j+k\neq n+1$ should be impossible because there are $n+1$ terms.
- EXAMPLE 14
  here $1+x+x^2+\cdots$ will automatically drop terms after $x^r$ when we only cares about the coefficient of $x^r$.
- EXAMPLE 15 
  based on chapter 6, it is $C((r-n)+(n-1),r-n)$
- EXAMPLE 17 `apart((1-9*x)/((1-8*x)*(1-10*x)))` in python.
- > by not assuming that the variable X denotes any numerical value
  ["formal power series"](https://en.wikipedia.org/wiki/Formal_power_series#Introduction) is just what the generating function assumes.
### 8.5
- > There are terms in this formula for the number of elements in the intersection of every nonempty subset of the collection of the n sets. Hence, there are $2^n − 1$ terms in this formula
  Here excludes $\varnothing$, so $-1$.
### 8.6
- > The well-known hatcheck problem can be solved using the principle of inclusion–exclusion
  see [this](#hat_check_Inclusion_Exclusion)
- > Many problems can be solved by counting the number of onto functions from one finite set to another
  see [this](#8_1_29)
- > we can use this principle to find the number of primes less than a positive integer
  see one exercise before 8.5-12.
- > In fact, this probability can be shown to be **within $1/(n + 1)!$** of $e^{−1}$.
  see [this](https://math.stackexchange.com/a/4835979/1059606) and "within" [meaning](https://math.stackexchange.com/questions/4835888/the-range-of-the-probability-of-the-derangement-for-n-people?noredirect=1#comment10297015_4835888).
  Also see Method 3 in this [detailed](https://math.stackexchange.com/a/83472/1059606)
- Probability that [exactly k](https://math.stackexchange.com/a/3850293/1059606) of N people matched their hats
- > The proof of this result is left as an exercise for the reader
  It is in exercise 27.
## 9
### introduction
- >  in some computer languages, only the first 31 characters of the name of a variable matter
  This is used in [C](https://cplusplus.com/forum/beginner/273069/#msg1177623)
### 9.1
- Here example 1~4 has set(s) where it assumes the relation is based on set(s).
- [antisymmetric](https://en.wikipedia.org/wiki/Antisymmetric_relation) is ${\displaystyle {\text{if }}\,aRb\,{\text{ with }}\,a\neq b\,{\text{ then }}\,bRa\,{\text{ must not hold}},}$
  With symmetric ${\displaystyle {\text{if }}\,aRb\,{\text{ with }}\,a\neq b\,{\text{ then }}\,bRa\,{\text{ must hold}},}$ 
  (Here $a=b$ case is trivial where $aRb\Rightarrow bRa$ must hold.)
  - Here can be seen as $A\wedge \neg B\to \neg C$ is equivalent to $A\wedge C\to B$ where $A$ can be seen as one hypothesis then the rest is contrapositive.
    Here the latter is more convenient to prove. 
- notice in EXAMPLE 11 -> EXAMPLE 5, $R_4$ is both symmetric and antisymmetric.
- example 7 some pairs are symmetric while some not, so not symmetric nor antisymmetric.
- > The reader should verify that R5 and R6 are transitive
```python
R_5=[(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]
def check(pair_seq:list[tuple[int]]):
  for pair in pair_seq:
      if pair[0]!=pair[1]:
          second_pairs=[second_pair for second_pair in pair_seq if second_pair[0]==pair[1] and second_pair[0]!=second_pair[1]]
          for second_pair in second_pairs:
              target_pair=(pair[0],second_pair[1])
              if target_pair not in pair_seq:
                  print("err")
              else:
                  print(target_pair,"from",pair,second_pair)
check(R_5)
R_6=[(3,4)]
check(R_6)
R_1=[(1, 1), (1, 2), (2, 1), (2, 2), (3, 4), (4, 1), (4, 4)]
check(R_1)
```
- $S\circ R$ starts from $R$ then $S$.
  so $(a,b)\in R,(b,c)\in S\Rightarrow (a,c)\in S\circ R$
- TODO Is $R^n\circ R=R\circ R^n$? Then how to prove if yes? <a id="power_relation_associativity"></a>
### 9.2
- TODO
  How is `FROM Teaching_assignments, Class_schedule` related with join?
- > Such algorithms first find *frequent* itemsets and then turn their attention to finding all the association rules with *high confidence* from the frequent itemsets that have been found.
  TODO why not let this be $J$ instead of $I$?
- > Support can be beneficial for finding the connection between *products* in comparison to the *whole* dataset, whereas confidence looks at the connection between one or more *items and another item*
  why define [Support and Confidence](https://en.wikipedia.org/wiki/Association_rule_learning#Support)?
### 9.3
- in FIGURE 2, the diagonal can be 0 or 1.
- EXAMPLE 5 says the usage of the Boolean product.
### 9.4
- For transitive closure, we only need to think about $(a,b),a\neq b$ because $(a,a)$ will always *do nothing* when composite. <a id="transitive_reflexive"></a>
  - This is also shown in 9.6-exercise-2 ans
    > the nonreflexive pairs will not introduce any violations of antisymmetry.
    and 9.6-exercise-8 ans
    > The only pairs that might present problems with transitivity are the nondiagonal pairs
- Here $R\cup \triangle$ *only adds necessary* pairs for reflexive closure.
  similarly, $R\cup R^{-1}$ also *only adds necessary* ones.
  So *minimal* and with *the related property*
  Then "contain" is ensured by $\cup$
  So the following 3 conditions are met.
  > Because this relation *contains R, is reflexive, and is contained within every* reflexive relation that contains R, it is called the reflexive closure of R
- > The only ordered pairs not in $R^{\ast}$ are those containing states that are not connected to the continental United States
  TODO here 
  > contains (a, b) if state a and state b have a common border.
  doesn't exclude $(a,b)$ where $a,b$ not have $n$ borders distant based on $R^n$.
  so it can contain " states that are not connected to the continental United States".
- > If (a, b) ∈ R∗ and (b, c) ∈ R∗, then there are paths from a to b and from b to c in R. We obtain a path from a to c by starting with the path from a to b and following it with the path from b to c. Hence, (a, c) ∈ R∗
  More specifically, $(a,b)\in R^{m}$ and $(b,c)\in R^{n}$
  so $(a,c)\in R^{m+n}\in R^{\ast}$ as [this](#power_relation_associativity) shows.
- > Because S is transitive, $S^n$ also is transitive
  [It](https://math.stackexchange.com/a/1701431/1059606) uses $R^n\subseteq R$
  - $R\subseteq S\Rightarrow R^k\subseteq S^k$ is trivial based on the definition of $\subseteq$.
    or more specially, $R^k=(f(S))^k$ where $f(S)$ only removes something from $S$
    Then $S^k=R^k+(\overline{R})^k+M$ where $M$ takes both $R,\overline{R}$ 
    for the composite operation after excluding $R^k\cup (\overline{R})^k$
    and $\overline{R}=S-R$
- > Suppose that a = b and that m > n, so that m ≥ n + 1 ... among the m vertices x0, x1, … , xm−1
  change this to $m > n-1$ 
  we can get the case $a\neq b$
  because here when $m=n$, there are $m+1=n+1$ vertex including $a,b$, then "the pigeonhole principle".
- > if and only if there is a path between these vertices in Ri, for some positive integer i with i ≤n
  if is trivial
  only if is from Lemma 1.
- [join matrix](https://math.stackexchange.com/a/2835565/1059606)
- > We now have paths from d to a, namely, d, c, a, and from d to d, namely, d, c, d
  here we only needs to check distance-1 case because the case
  > has only v1 = a, v2 = b
  has been contained in the before cases, e.g. after the before conditions, one path $(k_1,k_2)$ from 
  $(k_1,v_1),(v_1,k_2)$ is generated.
  Then for the path $k_1'-v_1-v_2-k_2'$ or $k_1'-v_1-Seq(k_i)-v_2-k_2'$
  it *only needs to add* $v_1-v_2-k_2'$ and 
  $Seq(k_i)_{end}-v_2-k_2'$ because the rest is *already generated*.
  - This is shown in Figure 4 after I thought of the above.
- EXAMPLE 8 Also see the [Warshall_code]
  - $W_n$ for $n\time n$ matrix doesn't always generate all-row-equal matrix.
    For example, diagonal matrix. 
- Here in Lemma 2, "if and only if" is by definition of $W_k$.
- Compare Algorithm 1 with Algorithm 2
  the former has $i:= 2 to n$ which function similar to $k := 1 to n$
  While the former does $2n-1$ ($n$ multiplication and $n-1$ addition) for each entry of $n^2$ entries of the matrix and the latter only has $2$. This is the key difference.
### 9.5
- If thinking of "equivalence relation" as "class"
  then it will imply "reflexive, symmetric, and transitive".
  Why "reflexive, symmetric, and transitive" $\to$ "equivalence"
  is related with [abstract-algebra](https://math.stackexchange.com/a/3299949/1059606) or is based on function <a name="equivalence_relation_definition"></a>
  > A relation $R$ on a set $A$ is an equivalence relation if and only if there is a function
- EXAMPLE 3 shares $a-b$ with EXAMPLE 2, so their proofs are similar.
- > The proof that $[b] \subseteq [a]$ is similar; it is left as an exercise for the reader.
  just swap $a$ and $b$.
- > it follows that these equivalence classes are either equal or disjoint,
  because $A\leftrightarrow B\Rightarrow \neg A\leftrightarrow \neg B$ where A,B corresponds to $i),ii)$
- > an index set is a set whose members label, or index, the elements of a set.
  It just have another set which only needs one bigger cardinality (["surjective"](https://en.wikipedia.org/wiki/Index_set#)) as [index](https://en.wikipedia.org/wiki/Index_set#Examples)
  > Any countably infinite set can be (injectively) indexed by the set of natural numbers $\mathbb {N}$.
- > We have seen that the equivalence classes of an equivalence relation on a set form a parti-tion of the set
  because $a\not R b\Rightarrow ([a]_{R},[b]_{R}\neq \varnothing) \wedge ([a]_{R}\cap [b]_{R}=\varnothing) \wedge (\bigcup_{a\in A}[a]_R=A)$.
  It also shows
  > by the definition of R, these are the subsets of S in the partition
  - Then
    > To see this, assume that {Ai ∣ i ∈ I} is a partition on S. Let R be the relation on S consisting of the pairs (x, y)
    is to show "Partition" $\to$ "equivalence relation".
    The books shows "subset" $\to$ "equivalence relation"
### 9.6
- > When we add all of the pairs of the form (x, x) to these relations, we obtain a relation that is reflexive, antisymmetric, and transitive
  i.e. if not $=$ just 
  $<$, it is asymmetric and the rest is same.
- > We do *not need a basis step* in a proof using the principle of well-ordered induction because if x0 is the least element of a well-ordered set, the inductive step tells us that P(x0) is true.
  i.e. the inductive step *includes* the basis step.
  > This follows because there are no elements $x \in S$ with $x \prec x_0$, so we know (using a vacuousproof) that P(x) is true for all $x \in S$ with $x \prec x_0$
  THEOREM 1 says $\forall x \prec y,P(x)=True\Rightarrow P(y)=True$
  since $\not\exist x\prec y$, the predicate is False, and $F\to T$ is [tautology](https://en.wikipedia.org/wiki/Tautology_(logic)#:~:text=In%20mathematical%20logic%2C%20a%20tautology,y%20or%20x%E2%89%A0y%22.), so $P(y)=True$
- > The verification of this is left as an exercise.
  Here I assume lexicographic order is same as [wikipedia definition][Lexicographical_order] ([link](https://en.wikipedia.org/wiki/Lexicographic_order#Cartesian_products)) (~~What "Added" wants to say: [preorder](https://en.wikipedia.org/wiki/Preorder) can be either symmetric or antisymmetric~~) <a name="lexicographic_order_partial_order_proof"></a>
  Here antisymmetric is trivial.
  - TODO what does "Added" mean for preorder.
- example 13 is processed by *adding one* element each time.
  example 12 is processed by multiplying the same multiplier each time. But it is not always this case as shown in example 14.
- example 18: we can find the bound by **traverse along the lines** beginning from *all* elements of the set.
  - $\{a,b,c\}$: 
    - upper bound: obviously we only needs to care about $\{b,c\}$
      then we find $e$ and transitively $\{f,j,h\}$
      For $\{d,g\}$ we can't include 
      $c$.
    - lower bound is trivial.
  - $\{h,j\}$
    - lower bound: similarly $f$ and transitively ...
    - upper bound: trivial
  - $\{a,c,d,f\}$ , i.e. $\{f\}$
- >  every pair of elements has both a least upper bound and a greatest lower bound,
  ~~it must contain *all* elements of the set~~
  ~~TODO So it is to say all elements *share* a least upper bound and a greatest lower bound~~
- Based on [this](https://math.stackexchange.com/a/2067965/1059606), it needs to find the exact least upper bound and greatest lower bound, so there may be no simple solution for EXAMPLE 21.
  The counterexample in FIGURE 8 (b) is that it has 4 pairs for $b\sim e$ but $d,e$ are incomparable.
- > The least upper bound and greatest lower bound of these two integers are the least common multiple and the greatest common divisor of these integers, respectively, as the reader should verify
  to find The least upper bound, we first find the upper bound for $(a,b)$
  then obvious they are $\{k\vert k=i\cdot lcm(a,b),i\in \mathbb{N^+}\}$
  then take the least.
  similarly the lower bounds are $\{k\vert k\vert gcd(a,b),k\in \mathbb{N^+}\}$
  - Similarly EXAMPLE 24 is done by $\cap,\cup$ definition.
- > A total ordering $\preccurlyeq$ is said to be compatible with the partial ordering R
  it can be seen as that $\preccurlyeq$ can be constructed from $R$
  Notice here $R\subset \preccurlyeq$ (See example 26 where the original one contain 3 chains $(1,2,4,12),(1,2,4,20),(1,5,20)$)
- > $(A − \{a_1\}, \preccurlyeq)$ is also a poset
  it is just $\subset$ the original $(A,\preccurlyeq)$
- [GLB,LUB](https://en.wikipedia.org/wiki/Infimum_and_supremum) abbr
- Topological Sorting is same as [what this QA says](https://math.stackexchange.com/a/574892/1059606)
- Definition 4
  why here we must have "every nonempty subset of S has a least element"
  because it needs to exclude the [infinite](https://math.stackexchange.com/a/1258854/1059606) case (Also [see](https://math.stackexchange.com/a/277170/1059606))
  - > And even more so, your argument if you look closely, should work for maximal
    means although the theorem *highlights minimal*, maximal also works.
  - [TODO](https://math.stackexchange.com/questions/3570899/every-not-empty-finite-subset-of-a-totally-ordered-set-has-a-maximum-and-minimum#comment10311443_3571343)
  - compared with [well-founded](https://math.stackexchange.com/questions/116642/is-well-founded-the-same-as-well-ordered#comment271123_116642) <a name="well_founded_diff_well_ordered"></a>
    The [ans](https://math.stackexchange.com/a/116647/1059606) (1. TODO example meaning. 2. Here $\sqsubset$ is just one [self-defined symbol](https://math.stackexchange.com/a/1569507/1059606))
    > "Well-ordered" means linearly-ordered and well-founded.
    means same as [wikipedia](https://en.wikipedia.org/wiki/Well-founded_relation#)
    > In order theory, a partial order is called well-founded if the corresponding strict order is a well-founded relation. *If* the order is a total order then it is called a well-order.
- [minimal element for the preorder][wikipedia_minimal_element]
  - here by [this](https://math.stackexchange.com/a/3177655/1059606)
    the possible [symmetric property](https://en.wikipedia.org/wiki/Preorder#) of preorder
    there may be $x\prec y, y\prec x$
    then it is not easy to say the [*strict order*](https://mathworld.wolfram.com/StrictOrder.html) (adding [connected](https://en.wikipedia.org/wiki/Total_order#Strict_and_non-strict_total_orders) it becomes the total order) (because not Asymmetric) between them which is used for partial order.
    > his means that there does not exist any element $s\in S$ such that ${\displaystyle m\leq s}$ and ${\displaystyle m\neq s.}$
    so we think of **both** $x,y$ are minimal.
- Definition 4 is same as [this](https://en.wikipedia.org/wiki/Well-order#:~:text=In%20mathematics%2C%20a%20well%2Dorder,called%20a%20well%2Dordered%20set.)
## 10
- [graph visualizer](https://math.stackexchange.com/questions/13841/online-tool-for-making-graphs-vertices-and-edges#comment10322484_13841)
- [List all possible graphs](https://math.stackexchange.com/a/2783775/1059606) with one specific property list.
  - Here ~~number of Vertices can be only set to~~ [one range](https://houseofgraphs.org/result-graphs)
    - Here default to be simple graphs.
    - vertex orbit -> ["automorphism"](http://www.cs.columbia.edu/~cs4203/files/GT-Lec2.pdf) which is related with permutation of vertices (then corresponding edge permutation) based on labeling, e.g. p20.
    - TODO 
      - [index](https://en.wikipedia.org/wiki/Topological_index)
      - group size
      - [genus](https://en.wikipedia.org/wiki/Genus_(mathematics)#Graph_theory) may be the number of spheres to be planar.
### 10.1
- > We can distinguish between two chemical compounds with the same molecular formula but different structures using graphs
  See [this](https://www.toppr.com/ask/question/compounds-having-the-same-molecular-formula-but-different-structures-are-called/)
- > we will show how graphs are used to represent the competition of different species in an ecological niche
  here one niche is characterized by [one species](https://www.khanacademy.org/science/ap-biology/ecology-ap/community-ecology/a/niches-competition)
- ~~TODO~~
  > Each edge has *either one* or two vertices associated with it
  ~~How only one?~~
  [loop](https://math.stackexchange.com/a/3259936/1059606) is with only one vertex
- why Directed multigraph can contain loops while Multigraph doesn't in table 1
  See [this](https://www.reddit.com/r/learnmath/comments/qv20qa/comment/hktvjxp/?utm_source=share&utm_medium=web2x&context=3) where the terminology depends on the context.
### 10.2
- $K_3$ see example 5.
- EXAMPLE 11
  here $a$ can be only with $c,d$ but then $b,e,f$ are connected -> contradiction.
- Theorem 4 is same as finding 2 disjoint subsets ~~...~~
  So we can use iterative coloring to prove. See example 12.
- > However, this is impossible because there are only two employees, Xuan and Ziegler, who have been trained for at least one of the three jobs of requirements, implementation, and testing.
  better interpretation:
  Washington and Ybarra only have architecture.
  - Using Hall's Marriage Theorem,
    Washington and Ybarra only has one corresponding neighbor, so $(|N(A)|=1) < (|A|=2)$
- In this book, bipartite graph defaults to be a [simple graph](https://math.stackexchange.com/q/3709826/1059606).
  > so I would assume they *only* care about bipartite graphs in the context of simple graphs
  - So 
    > We delete v and w and all edges incident to them from H
    is only one edge
  - [multigraph](https://mathoverflow.net/q/95011) is possible
- Theorem 5
  - > the inductive hypothesis tells us there is a complete matching from W1 − { v} to W2 − { w}
    This is due to
    > the vertices in every subset of j elements from W1 are adjacent to at least j + 1 elements of W2
    Since we only remove $\{w\}$, so still 
    at least $j$ elements of $W_2$. So $|N(A)|\ge |A|$ is met.
  - case (ii) obviously can be used multiple times until it can't be used.
  - $k\le k+1-j$ should be $k\le k-j$
  - [Combinatorial form](https://en.wikipedia.org/wiki/Hall%27s_marriage_theorem#Statement)
    - injective function implies complete matching.
      - TODO why [here](https://en.wikipedia.org/wiki/Transversal_(combinatorics)) use bijection
    - > the total unique elements they contain is at least as large as the number of sets in the group.
      See [example 2](https://en.wikipedia.org/wiki/Hall%27s_marriage_theorem#Examples)
    - > obtained by choosing a distinct element from each set in ${\mathcal {F}}$
      i.e. distinct inside the transversal.
    - [relation](https://en.wikipedia.org/wiki/Hall%27s_marriage_theorem#Equivalence_of_the_combinatorial_formulation_and_the_graph-theoretic_formulation)
      - > An ${\mathcal {F}}$-*perfect* matching in this graph defines a system of *unique* representatives for ${\mathcal {F}}$
      - kw: neighborhoods of the vertices
    - TODO infinite.
- > Hall’s marriage theorem is an example of a theorem where *obvious* necessary conditions are sufficient *too*.
  since it is not always this case, so I skip the [paper](https://www.cs.utep.edu/vladik/2019/tr19-75.pdf) trying to show this.
- Parallel processing implies why we use divide and conquer.
- > has the same vertex set V as G ... $E − \{e\}$
  TODO here it assumes $e$ is not one disjoint edge 
- > merges u and w into a new single vertex w
  should be "u and v"
- [maximal matching](https://en.wikipedia.org/wiki/Matching_%28graph_theory%29#Definitions) is one matching which *can't be added with one edge* to construct one new matching.
  - [bipartite perfect/complete matching](https://cs.stackexchange.com/a/50411/161388) is not totally same as perfect matching.
    same as [this](https://discrete.openmathbooks.org/more/mdm/sec_matchings.html)
    - > which will mean that every vertex in A is incident to an edge in the matching.
- Hall's Marriage Theorem alternative proof
  - only if / [Necessity](https://en.wikipedia.org/wiki/Hall%27s_marriage_theorem#Necessity) same as the book
  - Sufficiency
    Better see the [baeldung blog](https://www.baeldung.com/cs/augmenting-path) for the alternating path.
    - > whether each of its edges belongs to M or not.
      IMHO, it should be whether each points of the edge belongs to M or not.
      It corresponds to $cc'\to cd'$
    - > let u be any unmatched vertex in X
      here only need one $u$ although maybe many unmatched vertices.
    - TODO this seems to be wrong and it doesn't have any reference.
      because alternating path doesn't always exist which contains this maximum matching (e.g. $(x_i,y_i),1\le i\le |X|-1/|Y|$ and one isolated vertex $x_{|X|}$). 
      The maximum matching will use all <a name="alternating_path_Hall_Marriage_Theorem"></a>
      - Maybe see [this](https://math.stackexchange.com/a/414539/1059606)
- [graph union](https://mathworld.wolfram.com/GraphUnion.html)
### 10.3
- [represent](https://en.wikipedia.org/wiki/Sparse_matrix#Compressed_sparse_row_(CSR,_CRS_or_Yale_format)) sparse matrix
  here $0$ in `COL_INDEX` corresponds to `V`.
- example 10
  1. > each of these four vertices in H is adjacent to another vertex of degree two in H, which is not true for a in G
    they must be same if isomorphic because the one-to-one correspondence between vertices.
  2. > subgraphs of G and H made up of vertices of degree three
    similarly for the same reason as the above.
- example 11
  here $f (u_3) = v_4, f (u_4) = v_5$ is dual/one-to-one correspondence to $ f (u_1) = v_6$ and $f (u_2) = v_3$
  obviously due to symmetry the order of $(u_3,u_1)$ and 
  $(u_4,u_2)$ doesn't matter.
  - > the adjacency matrix of H with the rows and columns labeled by the images of the corresponding vertices in G
    It should be first getting $H$ with the default ordering $v_1\sim v_6$ and then moving the entries to use the ordering $v_6,v_3,\ldots,v_2$.
- > Even though no polynomial-time algorithms have been found for solving this problem, it can be solved by linear average-case time complexity algorithms
  TODO so even if $O(n^k),k\in \mathbb{N}$ is not possible, 
  [$O(n)$](https://en.wikipedia.org/wiki/Time_complexity#Linear_time) is possible.
- Here we only care about [Isomorphism of simple graphs](https://math.stackexchange.com/questions/3201645/expanding-definition-of-simple-graph-isomorphism-to-include-multigraphs#comment6590030_3202725)
### 10.4
- Here definition 2 is mostly same as p652 definition in chapter 9
  Here it highlights something as well with kw: no multiple edges, called simple.
- EXAMPLE 4 $G_1$ is trivial
  or more specifically, think it as 2 3-cycles which is connected inside and with $c$ connecting these 2 cycles plus 2 edges to be connected to cycles.
  - $G_2$ is one path plus one circuit.
- ~~TODO~~ Theorem 1 proof is same as one proof before where also removes some vertices away.
  i.e. p632 lemma 1. <a name="graph_link_with_relation"></a>
- > A graph G that is not connected has two or more connected components that are *disjoint* and have G as their union
  - "two or more connected components"
    the worse case is that all are disjoint vertices.
  - if not "disjoint", then we can combine them.
  - "disjoint" implies union.
- EXAMPLE 7
  > The cut vertices of $G_1$ are b, c, and e
  here they are somewhat inner vertices.
  > The cut edges are {a, b} and {c, e}
  they are edges similar to degree-1.
- [nonseparable](https://mathworld.wolfram.com/SeparableGraph.html)
- EXAMPLE 8
  - here $G_5$ is one graph with 2 complete subgraphs $K_4$ and there are 2 edges $bc,gf$ to connect them, so *removing one vertex is impossible* to cut
    - notice this graph is symmetric after 180 Degree Rotation
      so we only need to care about one side, i.e. one $K_4$
      - to cut it with 2 vertices, $b,g$ are more suitable.
        but $fh$ will connect then, so *removing 2 vertices is impossible* to cut.
- > $0 \le \lambda(G) \le n − 1$.
  This can be more specific [$\le min_degree$][vertex_connectivity_less_than_minimum_degree] with $v$ [isolated as one component](https://math.stackexchange.com/a/2516637/1059606).
- the minimum number of edges in a connected graph with 'n' vertices is (n-1)?
  [proof](https://qr.ae/pKmgtv) also see the comment.
- [proof][comparison_edge_connectivity_vertex_connectivity] of $\lambda(G)\le \delta(G)$
  - TODO
    > There's one for each edge, so there are $e_c$ total.
    why must be exactly $e_c$? What if many edges incur *2 new endpoints*?
- EXAMPLE 9
  - $G_2$ here it is composed of ~~2 ~~ 1 complete graph $K_3$ and one cycle $C_4$, so $\lambda(G)\neq 1$
    similarly for $G_3$.
  - we can use [$\lambda(G)\le \min \deg(v)$](https://math.stackexchange.com/a/1744562/1059606)
  - > The reader should verify that the removal of no two edges disconnects $G_4$
    - obviously if 2 edges are from the rightmost $K_4$, it can't disconnect
      similarly for one edge is from $K_4$ (this will be reduced to $G_3$ somewhat)
    - So we choose edges not from $K_4$.
      there are 6 edges related with $b,g$.
      - if not choosing $af$, then $a$ can connect to $c\sim f$
        so to disconnect, we must choose $ab,ag$ to disconnect from $a$, but that will still connect by $bc,gf$.
      - if choosing $af$, still reduced to $G_3$ somewhat
  - > Finally, the reader should verify that $\lambda(G_5) = 3$, because the removal of any two of its edges does not disconnect
    - similarly we can choose 2 edges from 2 $K_4$ because that would not even make these $K_4$ disconnected.
    - Then if choosing one edge from 2 $K_4$ and one outside 2 $K_4$, the 2 edges must be incident with one same endpoint. Obviously not possible to disconnect.
    - So we choose edges not from 2 $K_4$.
      - similarly choosing $bd,hf$ -> not disconnect
      - by symmetry, one from $bd$ or $hf$,
        obviously one more edge can't disconnect $\{b,g\}$ from 
        $\{c,f\}$
      - nothing from $bd$ and $hf$
        $\binom{3}{2}$ choices to choose 2 edges from $bc,cg,gf$. They all don't disconnect.
  - TODO use one program to check.
- EXAMPLE 10
  - there is one big cycle for the left
  - $a$ out-degree is 0, so not strong.
    based on the cycle, weakly connected.
- "strongly connected components" just finds the in-degree out-degree sequence.
- > H has a simple circuit of length three,
  there are $\binom{6}{3}$ choices
  we can find $H$ has a simple circuit of length *five*, then there are $\binom{6}{5}$ which is less.
- > show that f is an isomorphism
  i.e. [preserves the "edge structure"](https://en.wikipedia.org/wiki/Isomorphism#Applications)
- THEOREM 2 is same as p632 THEOREM 2.
### 10.5
- by [this][find_euler_circuit_undirected_path]
  - ~~TODO relation~~ See the book theorem 1
    > Buried in that proof is a description of an algorithm for finding such a circuit.
  - Then
    For EXAMPLE 1, $G_{2,3}$ can't "find a random cycle using *unmarked* edges" at the 2nd step
  - For path, 
    - see [this][Fleury_Algorithm] p65
      The key is to keep each *subgraph* after each step still has one Euler path
      - > If there are 2 odd vertices, start at one of them
        ~~IMHO Here we can also start from ~~
        ~~TODO~~ ~~[proof][Fleury_Algorithm_proof]~~
        - See the book theorem 2 <a name="find_euler_path_based_on_circuit"></a>
          > Consider the larger graph made up of the original graph with the addition of an edge {a, b}.
          because there must one cycle including them after adding the edge.
          So after *removing the added* edge, we can't return back if starting from the vertex in *other cycles* different from the cycle including the added edge.

          ~~Notice it only means the paths constructed by theorem 1,2 will fail if not starting from odd vertices, but it *doesn't exclude other paths*.~~ See [unique_start_euler_path]
          - Also see this [alternative][find_euler_path_undirected_path]
            ~~TODO~~ which is same as the book theorem 2
            > add the missing edge
      - ~~TODO why~~ p49 "BA is a bridge"?
        maybe because if ending at $A$, then $A$ will be disconnected with the rest.
      - Then for $G_3$ (Here we only needs to exclude "even-even" edge when 2-odd which will increase 2 odd vertices leading to 4 odd vertices)
        we start from $a$ with 2-odd-$(a,b)$
        to $b$ then with 0-odd
        to $e$ (2-odd-$(e,b)$)
        to $d$ 2-odd-$(d,b)$
        to $c$ 2-odd-$(c,b)$
        to $a$ 2-odd-$(a,b)$
        to $d$ 2-odd-$(d,b)$
        to $b$ finished.
- ~~TODO~~ prove [conditions for the directed graph](https://www.geeksforgeeks.org/euler-circuit-directed-graph/) to have the Euler Circuit. Also [this](https://www.topcoder.com/thrive/articles/eulerian-path-and-circuit-in-graphs) for Euler path.
  - $H_1$ has $a$ with in-degree 0, so no Euler path.
- THEOREM 1
  - NECESSARY CONDITIONS
    it splits edges into 3 cases:
    1. start (add 1 degree)
    2. end (add 1 degree)
    3. pass-through (add 2 degrees)
  - SUFFICIENT CONDITIONS
    Same as [find_euler_circuit_undirected_path]
    based on the assumption that the graph is *connected* (then with even degrees, it means "the degree must be at least two"), we can *splice* the graph by many cycles which always use *even* degrees

    Here many cycles are constructed by the algorithm 1 "while H has edges".
  - Notice here any even number of cycles can't share one edge
    basis step: 2 distinct cycles share edge $vw$
      then $v,w$ has degree 3
    for 3 distinct cycles, then 2 cycles can be combined into one.
    The rest is similar.
- > Hence, it has an Euler path that must have b and d as its endpoints
  Obviously the EULER circuit is *unique* which can be started from anywhere. (we can split the vertex with degree greater than 2 into distinct vertices all with degree 2, then the circuit become one *simple cycle*.) <a name="unique_start_euler_path"></a>
  Then after removing one edge, the euler path can be *only* started from the endpoint of the removed edge.
- > Euler circuits and paths are applied is in the layout of circuits
  TODO how apply?
  maybe [isomorphism](https://www.cs.wm.edu/~tadavis/cs243/ch10s.pdf) but that needs the *type* of EULER circuit [same](https://math.stackexchange.com/a/2762272/1059606)
- Although Hamiltonian cycle/path has [necessary conditions](https://math.stackexchange.com/a/3449552/1059606) (obviously have because it just means the properties of the Hamiltonian cycle/path), it is difficult to *find* due to [NP-complete](https://math.stackexchange.com/questions/4431330/what-is-the-necessary-and-sufficient-condition-for-a-graph-to-be-a-hamiltonian-c#comment9276260_4431330) one.
  - TODO undirected [to directed](https://math.stackexchange.com/a/81565/1059606).
- EXAMPLE 5
  - $G_2$ can use $b,c,d$ as one Hamilton sub-circuit which obviously *can't be less*, but to include $a$, $ab$ needs to included twice.
  - Here $G_3$
    - Hamilton path
      - we can use [this method][check_Hamilton_path] same as [this](https://math.stackexchange.com/q/1958887/1059606) 1,2 by *removing edges* which is similar to the main ideas of the euler path
      - since here we have 3 degree-1 vertex, we can't have one path connecting them, so no Hamilton path.
    - Hamilton circuit
      - We can also use the [cut-vertex][cut_vertex_Hamilton_circuit] to prove no Hamilton circuit exists
        because the cut-vertex $y$ will be passed "at least twice"
        Assume one Hamilton circuit exists and 2 connected components after the split are $V_{1,2}$, then we can start from *arbitrary* vertex 
        $v\in V_1$ due to the *circuit* property, then from $v$ to $w\in V_2$, we need to pass $y$ one time, then back from $w$ to $v$, we still need to pass $y$ one time (Here the must pass of $y$ is due to the cut vertex)
      - The above is same as the [ans](https://math.stackexchange.com/a/1959036/1059606) which I read after the comment
        kw: at least twice, *any* vertex as the starting and ending vertex
      - We can use [other properties](https://math.stackexchange.com/questions/1958887/proving-a-graph-has-no-hamiltonian-cycle#comment10320937_1958887) which is same as what the book says.in p735.
        - Also see their [relations](https://math.stackexchange.com/questions/1958887/proving-a-graph-has-no-hamiltonian-cycle#comment10322413_1958887) with [cut_vertex_Hamilton_circuit].
- The Icosian Game [relation](https://en.wikipedia.org/wiki/Icosian_calculus#Informal_definition) with the *noncommutative* algebra
  here $\lambda=\iota \kappa$ means $BC\xrightarrow{\kappa} DC\xrightarrow{\iota} CD$
  and $\kappa \iota$ means $BC\xrightarrow{\iota} CB\xrightarrow{\kappa} ZB$
  - > Two travellers set off visiting 4 *neighbouring towns. One returns home* and the other continues to travel around the world trying to visit all the remaining cities *once* only.
    [Travellers Dodecahedron](https://www.puzzlemuseum.com/month/picm02/200207icosian.htm)
    maybe some cities excluded.
- > Dirac’s theorem can be proved as a corollary to Ore’s theorem because the conditions of Dirac’s theorem imply those of Ore’s theorem.
  i.e. Dirac’s $\subset$ Ore’s
- FIGURE 14
  WLOG assume we start from 000
  then based on symmetry the 010 can be also at the upper or right of 000
  Then 110 adjacent with 100 can be *only* above 010 since it has distance 2 from 001.
  Then 011,111 are decide by 001,110 since only one choice is left.
### 10.6
- > has no interior vertices other than a
  based on p657, $a$ is not one interior vertex.
- ALGORITHM 1
  the key is "updates the labels of vertices" which are the minimal distance ~~using~~ staring from vertices in $S$.
  Then "u := a vertex not in S with L(u) minimal" based on the *greedy* algorithm.
  - here basis step (i) is vacuously true because nothing is in $S$.
  - Here "At the kth iteration" should be *before* the $k$th iteration.
    This is implied by
    > From the inductive hypothesis we see that the vertices *in* S *before* the (k + 1)st iteration are labeled with the length of a shortest path from a.
  - > so the length of a shortest path from a to a vertex other than a is $\infty$
    This is because
    > contains only (besides the vertex itself) vertices in S
    and
    > before any iterations are carried out
    so the label has not been updated, so all $\infty$
  - > because Lk (v) is the length of a shortest path from a to v containing only vertices in S *after* the kth iteration
    Then $L_k(v)$ corresponds to 
    $|S|=k$
    and $L_k(v)$ corresponds to 
    $v\not\in S$ and the path $a=s_1,\ldots,s_m,v,m\le k$
  - > There is a path with length less than Lk (v) from a to u containing only vertices of S. This contradicts the choice of v
    i.e. there is one path $a=s_1,\ldots,s_m,u,u_1,\ldots,u_i,v,m\le k$ which has less length where $u_1\sim u_i$ may not exist.
    Then $a=s_1,\ldots,s_m,u$ has less length,
    we should choose $u$ instead of $v$.
    - The contradiction is based on
      > u := a vertex not in S with L(u) minimal
    - > v must be labeled with the length of a shortest path to it from a
      The above proves this key idea where "shortest path" is based on *all possible paths*.
  - > A shortest path from a to u containing only elements of S
    based on the algorithm construction
    here it doesn't mean containing *all* of $S$.
  - > then by the inductive hypothesis its length is Lk (u)
    Here $L_k()$ only considers 
    vertices in $S$, so although maybe some path $a=s_1,\ldots,s_m,w,w_1,\ldots,w_i,u$ is shorter than 
    $a=s_1,\ldots,s_m',u$, we don't consider it.
    - This is just what (ii) states.
  - > then it must be made up of a path from a to v of shortest possible length containing elements of S other than v, followed by the edge from v to u.
    because if $v$ is not the last vertex before $u$,
    then the path must be $a=s_1,\ldots,s_m,v,s_{m+1},\ldots,s_{m+k},u$ which is longer than ~~original path $a=s_1,\ldots,s_m,v,u$ when $v$ is the last vertex~~ directly from $S$ to $u$ which at least removes $s_m,v$ and $v,s_{m+1}$.
- here should be "2(n − 1) comparisons" and "n − 1 additions".
- > the weighted graph satisfies the triangle inequality
  see [this](https://math.stackexchange.com/questions/4723437/why-is-the-triangle-inequality-in-a-weighted-graph-always-satisfied-why-is-this#comment10008188_4723437)
### 10.7
- EXAMPLE 3
  - > These four edges form a closed curve that splits the plane into two regions, R1 and R2
    This subgragh must exist due to the planar graph property.
  - > then the edge between v6 and v3 cannot be drawn without a crossing
    because must cross the square.
    - > then the edge between v2 and v6 cannot be drawn without a crossing
      similarly must cross the quadrangle $v_{4352}$.
- "simple" in THEOREM 1 excludes the loops.
  Also see the proof of COROLLARY 1.
- COROLLARY 1
  - > When an edge occurs twice on the boundary (so that it is traced out twice when the boundary is traced out)
    it may be based on the circuit around the boundary. so 
    $g-f-\ldots-f-g$ where $f-g$ is counted twice.
  - [connected_planar_simple_graph]
    Then
    > The degree of each region is at least three
    > note that the degree of the unbounded region is at least three 
    ~~maybe wrong because possible graph by 3 vertices $\cdot-\cdot-\cdot$~~
    See this for [the case $\cdot-\cdot-\cdot$](https://math.stackexchange.com/a/2414907/1059606)
    - > The degree of each region is at least three.
      either has the visible boundary
      then when the worst case, with 3 vertices it has degree 3.
      or not visible, i.e. unbounded
      > the degree of the unbounded region is at least three because there are at least three vertices in the graph
      This is the above $\cdot-\cdot-\cdot$.
    - > Because the graphs discussed here are simple graphs, no multiple edges that could produce regions of degree two, or loops that could produce regions of degree one, are permitted
      here
      1. "degree one" -> one edge ~~-> either connected (degree 1) or unconnected (degree 2). But both is impossible where the former is due to loop is not allowed while the latter is due to the degree unmatch.~~ impossible because $v\ge 3$ which indicates $e\ge 2$ by [connected_planar_simple_graph].
      2. "degree 2" -> two edges which must be unconnected. Based on the above, $\deg(R)=4$
      3. "degree 3" -> 3 edges (based on the above 1,2 edges are all excluded)
        3 possibilities in [connected_planar_simple_graph], i.e. 3-2,4-1,4-2 where 3-2 means row-3 and column-2. The latter 2 are unbounded one so $\deg(R)=6$
      4. Then 
        > there are no circuits of length three implies that the degree of a region must be *at least four*
- [Homeomorphism](https://en.wikipedia.org/wiki/Homeomorphism_(graph_theory)) which is related with the subdivision is different from [homomorphism](https://math.stackexchange.com/a/183142/1059606) which maps between vertices and *preserves edges* ([wikipedia](https://en.wikipedia.org/wiki/Graph_homomorphism#Definitions)).
- Kuratowski Theorem [proof][Kuratowski]
  - Figure 4
    > then create a cycle including both u and v by tracing around the exterior of the picture
    we can just replace one part of $C$ by part of $P$ where both are adjacent to $w$ and the latter also contains $v$.
  - > a graph is planar if and only if each of its blocks (*maximal 2-connected* subgraphs) is planar.
    See [this](https://math.stackexchange.com/a/840292/1059606)
    - [block p10](https://www.math.cmu.edu/~af1p/Teaching/GT/CH3.pdf)
    - [outer face](https://web.archive.org/web/20230519055753/http://cgm.cs.mcgill.ca/~athens/cs507/Projects/2004/Andrew-King/507planar.html)
    - > we draw this final block with the intersection point on the outer face, and similarly G' with the same intersection point on the outer face (this is *always possible*)
      [See](https://math.stackexchange.com/a/2026067/1059606) which is based on the stereographic projection.
      > make sure that you take N to be inside of a face that has u on its boundary
    - kw:
      1. > if they share two vertices, then the union of the two blocks must be two-connected, contradicting maximality
      ~~2. > we seek to remove a single block which intersects with only one othe~~
        ~~This is ensure we can remove such a block. See [this](https://mathworld.wolfram.com/Block.html) where the $\cdot-\cdot$ in the left graph can't be removed~~
    - Claim 3
      See [this][Xuyifan_Kuratowski]
      - Lemma 4.7
        - > Mi is $H_i \cap \{u, v\}$
          This implies
          > Since {u, v} and the edge uv are the only part Mi ’s share, we can merge the planar embeddings of Mi ’s and get a planar embedding of G + uv
        - Here If $uv\in E(G)$
          Then
          1. > with the addition of a new edge uv
            is necessary.
            - if $uv\not\in E(G)$, we just have 
              $G + uv$ as the following shows
          2. > get a planar embedding of G + uv (G ∪ {uv}),
            becomes directly $G$
            - if $uv\not\in E(G)$, see the above.
          3. > $\epsilon(Mj ) < \epsilon(G)$
            is trivial.
            - if $uv\not\in E(G)$, then based on 
              $\kappa(G)=2$, at least one $M_p$ has one edge with each of $u,v$, which is one more than $uv$.
              So still $\epsilon(Mj ) < \epsilon(G)$
          4. > we combine Mj − uv with Mp − uv where p 6= j, 1 ≤ p ≤ k 
            This means "the addition of a new edge uv" make all $M_i,1\le i\le k$ have $uv$
          5. > When we combine this path with Mj −uv, we get a subdivision of K5 or K3,3
            This is the key idea which *replaces* $uv$ in $M_j$ with the path $w_{1\sim k}$ in $M_p$ due to "connected". 
            "replace" implies subdivision.
      - Lemma 4.8
        - > Since G is 2-connected, there exists another path connecting u, v, which does not contain the edge uv
          ~~based on "2-connected", $G-\{u\}$ is still connected.~~
          ~~then~~ 
          This is [same](https://www.whitman.edu/mathematics/cgt_online/book/section05.07.html) as Lemma 3 in [Kuratowski]
        - > Show that if minimal nonplanar graphs without any subdivision of K5 or K3,3 as subgraphs did exist, they would be 3-connected and simple.
          simple is because can remove loops and multi-edge keeping only one to construct one smaller nonplanar graph.
          So "minimal" implies "simple".
      - Lemma 4.9
        - > Clearly $\mu(G)\ge 4$
          This can be relaxed to $\mu(G)\ge 5$
          because $\mu(G)=3,4$ are the worst when $K_{3,4}$ which is planar.
        - > a P3 avoiding v between c and u
          i.e. avoiding $v$ and $b$.
          Here only needs to ensure the $P_i$ connecting $v,w$ in the cycle like $v,w,a,b$ *doesn't pass $a,b$*.
        - > u-P1-c-P2-v-P3-d-P4-u.
          here $u,v$ must be inserted one vertex between
          then for example $u-P1-c$ where removing $v,d$ will must remove $uv$ so that $G-uv$ removing $v,d$ is same as $G$ removing $v,d$.
          - i.e. Here we must remove *one vertex including $u,v$*.
      - Theorem 4.10
        - > if G − uv does not contain any bridge of C0, then it is clear that with the addition of edge uv, the graph is still planar,
          This means no other edges, implied by the following
          > Now how do you *divide* the remaining edges into the "pieces" of G that still need to be embedded? These are the bridges.
        - > if an outer bridge of C0 has more than 2 vertices of attachment, we can always find a new cycle that contains parts of the outer bridge and has more edges in its interior.
          ~~let these vertices of attachment be ~~ There must be 2 among "more than 2 vertices" in the "same arc $uv$"
          then by 
          > not all vertices of attachment lie on the same arc uv
          i.e. if they are inside the same arc, then we can replace $vw$ in the cycle by the outer bridge
          But if they are not inside the same, then $vw$ must pass $u$ or $v$, so they can't be replaced.
        - > Also, if the size of an outer bridge is more than one, there exists a vertex that is not on C0 in the bridge. Then the two vertices of attachment form a 2-vertex cut of both G − uv and G
          i.e. isolate the vertex which is "a vertex that is not on C0 in the bridge".
        - overlap [meaning](https://www.math.arizona.edu/~glickenstein/math443f08/notes11.pdf)
          >  Two bridges avoid one another if the vertices of attachment of one bridge lie *entirely in one segment* of the other bridge. Otherwise they overlap
          for example, skew is one example of overlap.
        - > Overlapping bridges of a cycle in a connected graph are either skew or else equivalent 3-bridges.
          here "3-bridge" is [explicitly stated](https://faculty.etsu.edu/gardnerr/5340/Beamer-Bondy-Murty-GT/Proofs-BM-GT-10-4.pdf) because
          > If $k \ge 4$, then B and B 0 are skew
          there is no 4 vertices to choose, so impossible to be skew.
        - > Let G be a plane graph containing cycle C. The inner bridge of C avoid one another, and the outer bridges of C avoid one another.
          [TODO](https://faculty.etsu.edu/gardnerr/5340/Beamer-Bondy-Murty-GT/Proofs-BM-GT-10-4.pdf)
        - > If all bridges of C0 are inner (outer) bridges, then we can draw the edge uv in the exterior (interior) of C0 and achieve a planar embedding of G
          This is based on the assumption $G-uv$ is planar, then adding $uv$ at the different side must not cause the crossing, so still planar.
        - > We consider 4 cases in terms of the relative position of B1 and B2. Without loss of generality, we assume that u, x2, v, x1 lie on the cycle in a clockwise order
          trivially, $u,v$ can be drawn arbitrarily first,
          then since the label of $x_2,x_1$ is arbitrary and based on the overlap,
          we can put one point between $u,v$ at the different sides and label like $x_2,x_1$.
        - TODO
          - ~~why Case (1) and (2) don't consider $x_1,y_1,v,y_2$ and ?~~
            because overlap between $y_1 y_2$ and $x_1 x_2$.
          - Notice here cycle may have many vertices which implies subdivision.
          - why Case (3) and (4) can't be only one vertex duplicate?
          - [This](https://math.stackexchange.com/q/4848046/1059606)
          - > We know that *B2 overlaps* the arc uv, and is skew to B1
            B1 overlaps with B2 -> skew.
        - Summary:
          1. proves the cycle $C_0$ of $G − uv$ existence
            - > G − uv is 2-connected
              Lemma 4.9. using "3-connected" property Lemma 4.7
              - Lemma 4.7 proof
                "G is not planar" -> $M_j$ nonplanar
                Use it to construct one "subdivision of K5 or K3,3," -> contradiction.
            - > By Lemma 4.8, there are at least two internally-disjoint paths between u and v
              Use the induction for $u-w$ with the cycle and 2-connected for the path $P$ from $u$ to $v$.
              Which is shown in Lemma 3 in [Kuratowski]
          2. Based on "contain" we check the *subgraph* which is also shown in the statement of THEOREM 2 in the book.
          3. Based on "the most edges in Int(C0)." -> "2 vertices of attachment" and "overlap the arc uv."
            "3-connected" -> "the size 1"
            Notice here is for outer bridges.
          4. 4 cases.
### 10.8
- > We will assume that all regions in a map are connected. This eliminates any problems presented by such geographical entities as Michigan
  i.e. [2 peninsulas connected](https://en.wikipedia.org/wiki/Geography_of_Michigan).
- > For instance, for the map shown on the left in Figure 1, four colors suffice, but three colors are not enough. (The reader should check this.) In the map on the right in Figure 1, three colors are sufficient (but two are not).
  - the left
    because B ~~only~~ has 3 adjacent regions and D is adjacent to A.
    then C-E, (F,G)-(A,B) where - means same color sequence.
  - the right
    C,D,E must be different
    then E-A,B-D
- The key ideas of example 5~7
  are they can't use one same identy which can be represented as one color
  1. example 5: time
  2. 6: channel
  3. 7: register
## 11
### 11.1
- THEOREM 1 proof
  - We can also use the [leaf node](https://math.stackexchange.com/a/1334024/1059606)
    or the **sub**-cycle as the book says (Exercise 59 of Section 10.4) or the above link.
- > the reader should show that such a vertex is unique
  otherwise one cycle is constructed.
- Theorem 2 is similar to [QA link referred in this QA](https://math.stackexchange.com/q/4849754/1059606)
  - Notice it is possible for ["all cut edges"][tree_imply_all_cut_edge_i_e_no_circuit]
  - "a leaf of T" -> "the diameter of $G$"
- > Also, when (i) and (iii) hold, then (ii) must also hold, 
  This is due to that to keep the connectivity, the 1st can connect 2 vertices, while the rest can at most connect one more each. So $n-1$.
  > and when (ii) and (iii) hold, (i) must also hold.
- [complete "same"](https://en.wikipedia.org/wiki/M-ary_tree#Types_of_m-ary_trees) is stronger than balanced ["n/n-1" p15](https://w3.cs.jmu.edu/spragunr/CS228/lectures/trees/trees.pdf).
- > Rooted trees can also be defined *recursively*. Refer to Section 5.3 to see how this can be done.
  i.e. Definition 3 which is defined by *level*.
  We can do this by branch each node *down* instead of at the same level or up due to *no circuits*. <a name="tree_level_recursive"></a>
- see p785 rooted trees are *default to be ordered*.
### 11.2
- ALGORITHM 1
  - > If x equals the key of v, then the algorithm has found the location of x and terminates
    This implies $v\neq null$ and $label(v) = x$, obviously implying `root of T = null`.
    So it skips `if` and directly terminates.
  - `root of T = null` is the init step
  - for `while` there are 3 possibilities
    1. `v=null`, then no `label(v)` (to insert)
    2. $v\neq null$ and $label(v) \neq x$ (continue the `while` loop)
    3. $v\neq null$ and $label(v) = x$ (find one)
  - `v is null or label(v) \neq x` may be ~~wrong~~ not strictly right.
    because it contains
    1. `v is not null and label(v) \neq x` which is impossible due to the `while` loop
    2. `v is null and label(v) \neq x`
    3. `v is null and label(v) = x` impossible due to invalidity of `label(null)`
- > need only note that by Exercise 74 in Section 3.2 we know that ⌈log n!⌉is Θ(n log n)
  See [this](https://stackoverflow.com/a/2095472/21294350)
  where $\frac{n}{2}\cdot\log(\frac{n}{2})=\frac{1}{2}\cdot (n\cdot (\log(n)-1))\ge \frac{1}{2}\cdot (n\cdot (\log(n)-\frac{\log(n)}{2})),(\frac{\log(n)}{2}\gt 1)\ge \frac{1}{2}^2\cdot (n\cdot \log(n))$
- > We obtain the following estimate when we let N = n!
  Here $n!$ is the leaf number.
  Obviously sorting decision tree is A full 2-ary tree because each decision must generate 2 childs (Here we can take the situation $a=b$ into either case).
  so based on 11.1 THEOREM 4 (iii), we should use vertex number $2\cdot l-1=2n!-1$
  trivially, $g(n)=\Omega (\log(2n!-1))\Rightarrow g(n)\ge k\log(2n!-1),n>n_0\Rightarrow g(n)\ge k\log(2n!-n!=n!),n>n_0\Rightarrow g(n)=\Omega (\log(n!))$
- Definition 1
  - > the value of an internal vertex at an *even* level is the *maximum* of the values of its children
    because even -> first player to choose -> maximum
  - THEOREM 3 just pass "the payoff to the first player" from the bottom up.
    - > By extending the proof of Theorem 3, it can be shown that the minmax strategy is the optimal strategy for both players
      ~~i.e. from top to the bottom~~
      [This](https://stackoverflow.com/a/23041360/21294350) is really similar because minmax will ensure "the payoff to the first player" to be max when it is the first player's turn.
      - > maximize his profit.
        Here at each step the player always choose *the best for himself*. So optimal which at least maximize the current player's payoff.
      - optimal strategy [definition](https://socialsci.libretexts.org/Bookshelves/Economics/The_Economics_of_Food_and_Agricultural_Markets_(Barkley)/06%3A_Game_Theory/6.01%3A_Game_Theory_Introduction)
### 11.3
- Universal Address Systems is same as lexicographic order in p653.
- > each internal vertex the second time
  This implies the leftmost subtree has been traversed
  > listing a vertex the last time it is passed on the way back up to its parent
  all subtrees have been traversed.
  > list the vertices in preorder by listing each vertex the first time this curve passes it
  always root first.
  - The [online](http://www2.hawaii.edu/~takebaya/ics211/module8/objective2.html) one also doesn't give one detailed explanation.
- > An inorder traversal of a binary search tree, discussed in Section 11.2, visits the vertices in ascending order of their key values
  See [this](https://www.codecademy.com/resources/docs/general/binary-search-tree/inorder-traversal)
- > An expression in prefix notation (where each operation has a specified number of operands), is unambiguous, so no parentheses are needed in such an expression. The verification of this is left as an exercise for the reader.
  Here all operators are 2-ary operators
  Then based on
  > Both the preorder traversal and the postorder traversal encode the structure of an ordered rooted tree when the number of children of each vertex is specified.
  we can *encode* the tree.
  - The above means same as the contents after example 6 which I read after the above "verification".
  - > Because prefix and postfix expressions are unambiguous and because they can be evaluated easily *without scanning back and forth*, they are used extensively in computer science
    Based on FIGURE 11, the main reason is that in "prefix and postfix", the operator *range* is well defined.
    This is similar to the above.
- > The steps used to evaluate this expression by working right to left, and performing operations using the operands on the right,
  EXAMPLE 7 prefix:
  "working right to left" because leaves (operands) are on the right and we must leave the top root (i.e. the leftmost) at the end.
- > An inorder traversal of the binary tree representing an expression produces the original expression with the elements and operations in the same order as they originally occurred, ex-cept for unary operations, which instead immediately follow their operands
  "ex-cept for unary operations" mean not one at the left and one at the right of the operator
  but all after the operator.
- p837 
  > There are easy ways to list the vertices of an ordered rooted tree in preorder, inorder, and postorder
  can be seen intuitively [here][Depth_first_traversal_3_colors].
  - ~~red is first met because left-to-right searching order.~~
    See the comments like "Visit the current node (in the figure: position red)." which shows the correspondence between the book and wikipedia and also proves the relation between 3 orders and the walk (walk along the path in the figure to get why the above properties hold.)
- > Both the preorder traversal and the postorder traversal encode the structure of an ordered rooted tree *when the number of children of each vertex is specified*
  if not specified, we can use [other conditions][Depth_first_traversal_3_colors] to construct -> [this](https://cs.stackexchange.com/a/441/161388)
  Notice here we have *no operators* but just operands.
  - > No one sequentialisation according to pre-, in- or post-order describes the underlying tree uniquely.
    in-order alone is shown in the book or we [don't know what to choose for `[x]`](https://cs.stackexchange.com/q/439/161388).
    pre-order, post-order is due to
    ~~> can be either the left child or the right child.~~
    ~~So ~~ we don't know where to end `(post r)` or others similarly.
    - > even if we assume pairwise distinct keys/labels.
      TODO IMHO it can as the book says.
  - Notice
    > First, I'll assume that all elements are distinct.
    otherwise the algorithm to check for $x_2=y_i$, etc, fails.
  - Here pre-order traversal with post-order traversal is done by mapping (one-to-one correspondence) between each other.
  - Here $O(n^2)$ may assume using the naive searching algorithm.
    while $O(n\lg(n))$ assume for each 
    $x_i$ searching for $y_j=x_i$ takes $O(\lg(n))$ time.
    - Since maybe level $n-1$ for n vertices. So we may have $n$ iterations and each iteration uses some time to search.
      ```python
      def order([x_1,...,x_n],[y_n,...,y_1]):
        if len([x_1,...,x_n])==1:
          return [x_1,...,x_n]
        j=search(x_1,[y_n,...,y_1]) # {get left-subtree and right-subtree}
        L=order([x_2,...,x_{j-1}],[y_{i-1},...,y_2])+order([x_j,...,x_{n}],[y_{n},...,y_i]) # left appended with right
      ```
  - > Post-order plus in-order is of course symmetric.
    i.e. similar to the pre-order one plus in-order.
    Similarly they are based on mapping.
### 11.4
- > At least five roads must be plowed to ensure that there is a path between any two towns
  See 10.4-28.
- THEOREM 1 is also shown in the second to last paragraph in [this link](https://math.stackexchange.com/a/136265/1059606) ~~although it doesn't say "spanning"~~
- [Multicast](https://www.geeksforgeeks.org/difference-between-unicast-and-multicast/) is just mul-to-mul
- DFS
  - > All other edges of the graph must connect a vertex to an ancestor or descendant of this vertex in the tree.
    i.e. form one loop.
  - > we examine each edge at most twice to determine whether to add this edge
    i.e. once for each endpoint.
  - > Because the graph has a *finite number of edges* and is connected, this process ends with the production of a spanning tree
    1. trivially all edges are visited -> all vertices are visited, i.e. spanning <a name="DFS_construct_tree"></a>
    2. backtracking -> connected
    3. it must have $n-1$ edges based on this process because except for the 1st edge leading from the root, all the rest must add one *new vertex* based on "visited" -> tree with the plus of "connected"
      - Or since each is *visited once* -> no circuit, so tree.
    - > Each vertex that *ends a path* at a stage of the algorithm will be a *leaf* in the rooted tree, and each vertex where a path is constructed starting at this vertex will be an internal vertex
      "ends a path" -> no child -> leaf
  - [backtracking][backtracking_AND_DFS_imply_preorder]
    > Note that *repeat* visits in the form of backtracking to a node
    is generalized from [this](https://en.wikipedia.org/wiki/Backtracking#)
    - > incrementally builds candidates to the solutions, and abandons a candidate ("backtracks") as soon as it determines that the candidate *cannot possibly be completed to a valid* solution.
      i.e. when having one path which can't be extended (completed) to include all vertices (valid)
      It *abandons* this path by dropping the leaf and going backwards.
      > Any *partial* solution that contains two mutually attacking queens can be abandoned.
      - This is same as 11.4.4 says.
      - > Backtracking can be applied only for problems which admit the concept of a "partial candidate solution" and a relatively *quick test of whether it can possibly be completed* to a valid solution.
        > The backtracking algorithm enumerates a set of *partial* candidates that, in principle, could be completed in various ways to give all the possible solutions to the given problem.
      - > If it cannot, the whole sub-tree rooted at c is *skipped (pruned)*. Otherwise, the algorithm (1) checks whether c itself is a valid solution, and if so reports it to the user; and (2) recursively *enumerates all sub-trees* of c.
        i.e. either prune subtrees or not (leaf trivially).
  - > For example, it can be used to find paths and circuits in a graph
    - [path](https://www.geeksforgeeks.org/print-the-path-between-any-two-nodes-of-a-tree-dfs/) which shows DFS very clearly using `vis` and `del stack[-1]` to update the stack.
    - cycle in undirected. See [nonisomorphic_simple_connected]
      - Here `# Recur for all the vertices # adjacent to this vertex ... parent != i`
        checks the following ""DFS" with no back edges".
        - Here by combining the tree edges and the single back edge, we can get one **simple** cirucit, although it is not shortest as [this example](https://stackoverflow.com/a/20847998/21294350) shows.
          - ~~Also see [this](https://stackoverflow.com/a/77927343/21294350)~~ ~~which implies DFS can get one simple circuit where the shortest implies ~~.
      - `if(self.isCyclicUtil(i, visited, v)):` just *passes back* the result based on the recursive algorithm.
      - [comparison](https://stackoverflow.com/a/19115118/21294350) with the ~~above~~ directed.
        > An undirected graph has a cycle *if and only if* a depth-first search (DFS) finds an edge that points to an already-visited vertex (a back edge)
        "if" is trivial. <a name="DFS_checking_cycle_proof"></a>
        "only if" is due to that ["DFS" with no back edges is one spanning tree](https://cs.stackexchange.com/questions/11438/why-does-dfs-only-yield-tree-and-back-edges-on-undirected-connected-graphs#comment316453_11552). So its corresponding undirected graph is one tree which implies no cycle.
    - cycle in [directed][Detect_cycle_Directed_Graph]
      - As [this](https://stackoverflow.com/questions/19113189/detecting-cycles-in-a-graph-using-dfs-2-different-approaches-and-whats-the-dif#comment137343260_19115118) said, it just adds `recStack[v] = False` `recStack = [False] * (self.V + 1)`, etc.
      - Here the `visited` is not stack so it will construct one maximal possible tree similar to the spanning tree (i.e. it will reach the most possible vertices *without duplication*)
        - See the [code](./miscs_snippets/py_codes/11_4_61/geeksforgeeks_cycle_directed.py) which shows the code can detect the cycle when there are multiple cycles.
        - > So, we can conclude that a cycle exists. We can also find the cycle if we have traversed to vertex 2 from 0 itself in this same way.
          This is the "smaller" cycle in the following proof.
        - > So if 0 is checked first, we will get the answer that there is a cycle present.
          > On the other hand, if vertex 3 is checked first, then 3 will be marked in visited[] and recStack[].
          based on DFS is based on the stack, "vertex 3 is checked first" won't influence us to construct the circuit because it has *no intersection with the cycle* and then can't construct one cycle variant similar to the above "smaller" cycle (e.g. for $root\to 2\to 3\to root,2\to 4\to 3$, if we have $root\to 2\to 4$ first, then we have one bigger cycle reached before the smaller cycle).
          - Here either the subtree (trivially we assume this subtree has no cycles because if we find one cycle, then based on `return True` in `isCyclicUtil`, we will *end earlier*) of the branch point $v$ has no intersection (then it will be backtracked and we can continue following the cycle because of no intersection) or has. <a name="cycle_branch_out_WITH_proof_after_reaching_cycle"></a>
            For the latter case there are 2 possibilities:
            1. as the above example, intersection $w$ hasn't been visited.
            2. have been:
              Then we find one cycle shares $w\to v$ with the original one.
            - The above is the proof part after reaching the cycle.
        - > It is based on the idea that there is a cycle in a graph only if there is a back edge
          Proof: <a name="directed_graph_detecting_cycle_proof"></a>
          1. Notice this can only find the cycle *including* the root.
            e.g. when we have the in-degree-0 vertex $v$ as the root in $a\to b\to c\to a,a\to v$, we can't even proceed, let alone finding the cycle $a\to b\to c\to a$.
             ~~1. Assume we have one cycle $C:root,a,b,c,\cdots,v,root$~~
               - ~~Then assume $x$ is the first vertex have already been visited and we can't proceed further.~~ (This is one wrong proof)
                 Then trivially we can substitute the path $root\to x$ which may contains many inner vertices by path $p(x)$ 
                 which visits $x$ the first time.
                 Then we find one new cycle $p(x),next(x),\cdots,root$
                 - Use the above process recursively until no vertices in the cycle have been visited before.
                   Since these new paths to substitute the old paths are *inside the tree*, the new cycle is also contained in the tree.
          2. If the root can reach one vertex inside the cycle, then by 1.1, we can also find the cycle.
            If it can reach multiple vertices, we let the *first* vertex be $v$.
            Then when we reach $v$, we must be able to proceed until back to the root which constructs one cycle.
            - Then for the above 1.1 we can prove more elegantly by using "*first*".
              - The above proof is wrong because ~~it doesn't consider the branch point case, i.e.~~ we *may not follow $C$ at all*.
              - Assume we reach $C$ first by $w$ which *may not adjacent to $root$*.
                1. adjacent to $root$ (based on the directio, it has *only one* choice), then we can construct the *whole* $C$
                2. not adjacent. Then $C$ contains one *smaller* cycle which is $root,w,next(w),\cdots,root$.
                - This proof also has defects, because we may branch out inside the cycle as [cycle_branch_out_WITH_proof_after_reaching_cycle] shows which also shows one correct proof.
          3. In summary the cases are
            - root is in the circuit (*)
              - we may reach vertices not in the cycle while constructing the cycle
              - not "reach vertices not in the cycle"
            - not in
              - can reach the circuit then follow the proof of (*)
              - can't reach (only this we ~~may not~~ won't find ~~the~~ this cycle)
          4. The above shows we can follow the circuit where when back to the starting point of this cycle we have one back edge.
  - cross edge can't exist in an undirected graph
    - [1][DFS_no_cross_edge]
      here case 1 just means in the DFS process of $u$ we meet $v$
      case 2 means $u$ has been backtracked, so based on $(u,v)$ it must contain 
      $v$ before when meeting $u$ instead of currently
      - Here case 2 may fail in directed graph because maybe we only have v->u but not u->v and then we can't reach v when rooted at u.
        so based on [this][DFS_only_2_types_edges]
        > It might help to think of why the can occur in directed graphs
      - By [this](https://cs.stackexchange.com/a/95534/161388) (here the path in the "white path theorem" becomes one single edge), white path directly proves this
        - [white path][lec_14]
          - Here when $d(u)$, 
            $u$ is not colored [gray][white_path_3_colors]
            - based on `color[u] = black` is always done the last after `for each v adjacent to u`, it just means having *traversed all children*.
          - > before finishing w:
            because 
            ~~> ww’ be the first edge on this path where w is descendant of u but w’ is not.~~
            if after finishing $w$, then when $d(w')$ we should have been discovered 
            $w'$ *first when $w\to w'$* -> contradiction.
          - > discover w’ after starting u
            This is same as [this][u_first_in_the_white_path]
          - [Parenthesis Theorem][lec_13_parenthesis_theorem]
            Here $d(u)<d(v)<f(u)<f(v)$ is impossible because of the process of DFS
            i.e. discover later must means finish (backtrack) earlier 
            - > By parenthesis theorem, w’ is also a descendant of u, contradiction.
              so intersection and one part of $d(u) < d(w’)$ are enough to get the "descendant" relation.
        - Then here just choose arbitrary edge $uv$ to prove it is either a tree edge or a back edge.
          then $uv$ becomes one "white path".
      - Also see the book 11.4.5 a spanning *forest* implying the cross edge in the weakly connected directed graph.
- BFS
  - > The procedure ends because there are only a finite number of edges in the graph.
    "a finite number of" vertices may be better because that is our ending target.
  - > add each edge incident to this vertex to the tree as long as it does not produce a simple circuit.
    based on the above $n+1$ similar to DFS, we ensure it is one tree.
    - It is similar to one *star graph*.
  - > we see that we examine each edge at most twice to determine whether we should add this edge and its endpoint not already in the tree
    This is because "for each neighbor w of v" is bidirectional.
  - both [DFS (similar to the star graph)](https://www.geeksforgeeks.org/connected-components-in-an-undirected-graph/) and [BFS similar to DFS with `for each vertex w adjacent to x` adding all vertices and then calling the next sub-procedure](https://courses.washington.edu/css343/zander/NotesProbs/graphBFS.pdf) can be used to "determine the connected components of a graph" because each component has one spanning tree which is the *minimal* connected subgraph of $n$ vertices.
    - Also see [this proof][lecture10_notes] which is based on the *level* (i.e. recursive depth).
  - > find the path with the fewest edges between two vertices in a graph
    - why DFS [can't](https://qr.ae/pKj7Qr)
      > DFS can explore a long path *before* it finds a shorter path
      - > Performing a topological sort of a directed acyclic graph (DAG).
        See [this][get_Topological_Sorting_from_DAG]
        here `stack.append(v)` will only be done after `self.topologicalSortUtil(i, visited, stack)` for all adjacent vertices (in the directed graph, i.e. ~~parents~~ children) or `visited[i] == True` which implies `topologicalSortUtil(self, v, visited, stack)` have already been done. Then *all children are appended before itself*, so ensuring the Topological Sorting. <a name="DFS_directed_topological_sorting"></a>
        - [defaultdict](https://www.geeksforgeeks.org/defaultdict-in-python/) can have `list` as the type of "value"
        - adjacent means same as reachable in mcs 10.5.
      - the modification to [update the weight](https://stackoverflow.com/questions/54198910/cant-we-find-shortest-path-by-dfsmodified-dfs-in-an-unweighted-graph-and-if#comment137344391_54199609) is obviously more complex to find the shortest path.
    - [BFS](https://www.geeksforgeeks.org/shortest-path-unweighted-graph/) to find the shortest is trivial
      It just find len-$1,2,3,\cdots,n$ until find one with the target destination `if (adj[u][i] == dest):`.
      - `for i in range(len(adj[u])): ... ` with no BFS sub-calls implies BFS.
      - It is just [Dijkstra](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Pseudocode) where `for each neighbor v of u still in Q:` "each" implies BFS having the [~~star~~ radial graph][BFS_radial]. <a name="Dijkstra_BFS"></a>
        - But `min` in `u <- vertex in Q with min dist[u]` implies its traversal order is not totally same as BFS when in one **weighed** graph.
          - Also `prev[v] ← u` means the tree may be modified in progress while BFS won't do that by assigning one **new** parent if already assigning one parent to one node.
            But as [this comment](https://stackoverflow.com/questions/8379785/how-does-a-breadth-first-search-work-when-looking-for-shortest-path#comment27820665_8379892) says, for *unweighted* the parent [can't be changed](https://stackoverflow.com/questions/8379785/how-does-a-breadth-first-search-work-when-looking-for-shortest-path#comment137378028_8379892).
            - kw
              parent (i.e. `pred` in the geeksforgeeks code), **double** as marking them "discovered"
- > The choice for which to use often depends on implementation details, such as the data structures used
  see [this](https://stackoverflow.com/a/2626251/21294350) by [this](https://stackoverflow.com/questions/3332947/what-are-the-practical-factors-to-consider-when-choosing-between-depth-first-sea#comment26027586_3332947) where "stack" is implied by "backtrack" and "queue" is implied by breadth.
  - Also see the [space complexity](https://cs.stackexchange.com/a/328/161388) which implies the data structure.
    - BFS
      - Here "$O(b^d)$ space" for BFS is due to ~~at each level $k<d$ we must *keep all queues* because maybe we need to continue to level $k+1$ if not found in level $k$.~~
        See [Artificial_Intelligence_A_Modern_Approach_3rd] Figure 3.12 where the white circles are the FIFO queue.
      - why $b^d$ is [preferred](https://cs.stackexchange.com/a/64450/161388)
        > we're going to visit looks *sorta like a tree*: each vertex has on average about b edges leading out of it.
        - [proof](https://stackoverflow.com/questions/15489329/breadth-first-search-branching-factor#comment118834780_15489507)
          - > Since in the worst case breadth-first search has to consider all paths to all possible nodes
            the *unique* path to each node implies $b^k$ multiplied by 1.
          - > the number of nodes at the deepest level
            All these is same as [Artificial_Intelligence_A_Modern_Approach_3rd]
        - [Artificial_Intelligence_A_Modern_Approach_3rd]
          - > If the algorithm were to apply the goal test to nodes when selected for expansion, *rather than when generated*,
            This means first expansion then test, so having overheads.
            ~~> which is that the goal test is applied to each node when it is *generated rather than* when it is selected for expansion.~~
            ~~Here I think $O(b^{d+1})$ corresponds to "generated" because the last level has no expansion but they are generated, so it will add ~~
            ~~$$~~
          - > $b+b^2+b^3+\cdots+b^d=O(b^d)$
            This is due to $\frac{b(b^d-1)}{b-1}<b^d-1<b^d$ although we can trivially get $O(b^{d+1})$.
          - > There will be O(bd−1) nodes in the explored set and O(bd) nodes in the frontier
            "explored set" has at most $b+b^2+b^3+\cdots+b^{d-1}=O(b^{d-1})$ by the figure 3.12.
            "frontier" has at most $b^d=O(b^d)$.
          - > As for space complexity: for any kind of graph search, which stores every expanded node in the explored set, the space complexity is always *within a factor of b* of the time complexity
            See [this][Graph_space_complexity_vs_time_complexity]
            - Notice this sentence is not shown in [4th edition][Artificial_Intelligence_A_Modern_Approach_4th].
            - in the [chat](https://chat.stackexchange.com/?tab=site&sort=people&host=cs.stackexchange.com)
              - [1](https://chat.stackexchange.com/transcript/message/65094178#65094178) means same as "add the node on the other end of $e$ **not in $N_x$** to $N_x$"
              - [2](https://chat.stackexchange.com/transcript/message/65094172#65094172) is wrong based on [this](https://cs.stackexchange.com/questions/165308/prove-the-relation-between-space-complexity-and-time-complexity-of-the-graph-sea/165324#comment343617_165324)
                > You seems to think "expand the chosen node" as one inner loop contributing to the time complexity with at most iteration number b by "does the following repeatedly ..." *instead of thinking of the outer loop as one minimal unit* (this is what I thought before which may be wrong after rethoughts)
            - [this](https://cs.stackexchange.com/review/suggested-edits/104060)
              > by thinking of how edges are got from nodes.
              shows how $k\leq |N_x|\cdot b$ are got. This is *the main part to prove*.
              - The rest is [added with improvement](https://cs.stackexchange.com/posts/165324/timeline#history_5c5dd7b2-b744-40f4-bb97-46812b233c86).
              - Notice $S(n)\ge \frac{1}{b}\cdot R(n)$ doesn't conflict with 
                $S(n)=\Theta(R(n))$ when 
                $b$ is one constant.
              - Based on this we can **only** get one proportional relation but [not exactly something like $S(n) \ge R(n)/b$](https://chat.stackexchange.com/transcript/message/65108003#65108003)
                The proof for "proportional" is also there (read beginning from the small question "Is it that case ...").
    - DFS
      - "$O(h)$ space" for DFS is due to stack, similarly for [IDDFS](https://en.wikipedia.org/wiki/Iterative_deepening_depth-first_search#Proof_2)
      - > A non-recursive implementation of DFS
        ~~may be~~ is similar to BFS as wikipedia says due to [all adjacent vertices are pushed](https://en.wikipedia.org/wiki/Depth-first_search#Pseudocode) `for all edges from v to w in G.adjacentEdges(v) do `
        this is why $O(|E|)=O(bd)$ as the [top label](https://en.wikipedia.org/wiki/Depth-first_search#) says.
        - Also see [this](https://stackoverflow.com/a/36480122/21294350)
          > you can know which sibling to explore next.
          This implies no adjacency list available. This [comment](https://stackoverflow.com/questions/36479640/time-space-complexity-of-depth-first-search#comment69260697_36480122) shows this
        - Also see this [more detailed](https://cs.stackexchange.com/a/68371/161388)
    - [IDDFS](https://en.wikipedia.org/wiki/Iterative_deepening_depth-first_search#Algorithm_for_directed_graphs)
      - it just call DFS for *each depth* (Iterative deepening) by `DLS(root, depth)`
        1. `remaining` will be false when $any_remaining \leftarrow false$ and `foreach child of node do` has no child. More specifically, i.e. `DLS(leaf,1)` in `DLS(root, h+1)` -> ... -> `DLS(leaf,1)`.
        2. $found, remaining \leftarrow DLS(child, depth−1)$ checks the subtree.
        - So Time complexity [proof](https://en.wikipedia.org/wiki/Iterative_deepening_depth-first_search#Time_complexity) $(d+1-k)b^{k}$ where 
          $b^k$ is the vertex number at level $k$
          and $(d+1-k)$ is because each vertex is called with $DLS(v,i),i=0,\ldots,d-k$ which corresponds to $DLS(root,i),i=k,\ldots,d$
          - Also see the reference
        - notice here $b$ is one constant which is *not influenced by the vertex number*.
    - TODO [$\Theta(V+E)$](https://stackoverflow.com/questions/2626198/graphs-data-structure-dfs-vs-bfs#comment15686876_2626251)
- > One way to search systematically for a solution is to use a decision tree, where each internal vertex represents a decision and each leaf a possible solution.
  The reason why Backtracking works is due to it is based on the decision tree which is **exhaustive** trivially.
  Then DFS/Backtracking must find one **path** to the solution because DFS will construct the spanning tree which lists **all possibilities/vertices** including the solution.
- FIGURE 12
  - Here is using ["left and right diagonals"](https://www.geeksforgeeks.org/printing-solutions-n-queen-problem/) as `# Check upper diagonal on left side` shows which the left elements due to the strictly increasing `col` by `j = j - 1`.
    Or as the book says which I omits carelessly when first reading
    > a diagonal consists of all positions (i, j) with i + j = m for some m, or i − j = m for some m
    - `any placement` implies `or res`
    - `result` saves the list of column indices for each row.
    - `board[i][col] = 0` may be done after the ~~print~~ solution save `result.append(v)` in the leaf node.
  - Here due to symmetry, only 1,2nd row are considered.
- > it can also be used to find the strongly connected components of a directed graph
  It just uses DFS for the [both directions](https://www.geeksforgeeks.org/strongly-connected-components/).
  - `(n + 1)`,`len(adj) + 1` because the index starts from `1` instead of `0`
  - notice here `vis` will be changed in the recursive call
    so when backtracked, it won't access the other direction of the cycle if possible.
    See [scc] with `Use_vis_cp=True`
  - > . It can be used to determine whether a directed graph has a circuit, it can be used to carry out a topological sort of a graph,
    these have been said before.
- > web crawlers have limits to the depth they search in depth-first search.
  i.e. IDDFS
- EXAMPLE 6 can't use BFS because we color one by one instead of [by level][BFS_level_order].
  - Here `a red` must be one [unary node](https://www.cs.cmu.edu/afs/cs/academic/class/15499-s09/www/scribe/lec11/lec11.pdf) followed by `a red, b blue` because we can color one edge arbitrarily.
  - Here we just check the coloring with the **already colored** nodes, which is enough, because the edge is *bidirectional* so if contradiction we can find that when coloring the latter colored one.
- decision-tree related problems can always be solved by backtracking.
### 11.5
- ALGORITHM 1
  - Here after the process, we have 1. no circuits, so "no simple circuits" 2. "n-1 edges".
    "n vertices" is trivial because we haven't added vertices and vertex number keeps $n$.
    Then we prove "connected" by 11.1.3 THEOREM 2.
    ~~To use 11.1.3 THEOREM 2, we need "n vertices", i.e. each added edge adds *one more new vertex* when initially 1 vertex.~~
    ~~- Prove each graph after the iteration is connected.~~ (Ignore the following.)
      - inductive step:
        Since "an edge of minimum weight incident to a vertex in T", then when T is connected, $T+(u,v),u\in V(T)$ is connected because 
        $v$ can be connected with the rest using $u$ as the medium (then all vertex pairs are connected) when $v\notin V(T)$
        when $v\in V(T)$, this is one trivial case.
      - basis step: one edge is trivial.
    ~~- Based on "connected", old vertex will cause the circuit -> contradiction.~~
- > We solve this problem by finding a *minimum spanning tree* in the graph in Figure 1
  the minimum connected graph must be "a minimum spanning tree".
  If not, then it must contain one subgraph which is a spanning tree (See 11.4) with the smaller sum of weights.
- example 1 can't contain the $\$1000$ path.
- Prim’s algorithm proof
  - here $k=0$ is possible.
  - Since $S$ is one tree as the above "ALGORITHM 1" contents shows,
    $S_k,k=1,\cdots,n-1$ must exist.
  - > By starting at an endpoint of ek+1 that is also an endpoint of one of the edges e1, … , ek,
    by the algorithm process, this endpoint must exist.
  - > (it is a tree because it has no simple circuits
    because ~~connected () and~~ $n-1$ edges.
    and based on
    > This simple circuit must contain ek+1
    this (~~although maybe more than one~~) [only one][one_cycle_when_tree_plus_one_edge] circuit is removed, so "no simple circuits".
    Then since vertex number doesn't change, we can use 11.1.3 THEOREM 2.
  - The main idea is to *construct one new* spanning tree from one assumed.
  - [One alternative proof][primsproof]
    - >  so let {a, b} be the first edge on this path with one endpoint (a) inside W
      this must exist because $x,y$ are one in W one not.
    - > Prim’s algorithm will select {a, b} at this step
      i.e. select one edge connecting one vertex in W to one not in.
    - [prefix](https://www.ime.usp.br/~pf/algorithms/chapters/footnotes/math.html)
      in this context it can also not "contain the first term". Then $W=\{x\}$.
    - So the book proof may should use $\{a,b\}$ here and contents before "so let {a, b}" in [primsproof] are same as the book corresponding ones (although the contents after may overlap partly).
      - > we can find an edge e *not in Sk+1* that has an endpoint that is *also an endpoint* of one of the edges e1, e2, … , ek.
        as [primsproof] shows, we can find one counterexample:
        maybe "{a, b}" is in $S_{k+1}$, then continue we may find one edge 
        $e$ has no endpoints in $W$.
        Here "maybe "{a, b}" is in $S_{k+1}$" is due to this edge weight may be the *minimal* at one stage after.
        - In [primsproof], it *only needs "also an endpoint"* instead of 2 conditions as the above shows which is one weaker condition which can be easily met based on "this must exist because $x,y$" above. <a name="Prim_find_incident_edge"></a>
        - ~~**Notice** we can modify the book proof to get the **3rd** proof which is almost same as Kruskal’s in exercise 32.~~
          ~~Here we *only* need "there must be an edge in the simple circuit that does *not belong to* Sk+1" (i.e. "an edge e not in Sk+1")~~
          then $T-\{e\}+\{e_{k+1}\}$ is still one spanning tree with ~~the~~ one ~~maybe *smaller* weight sum (case 1 in [primsproof] and excludes case 3 in [primsproof])~~ (Since Prim's only ensure the smallest weight among edges *incident* with already added vertices, we can't directly say "smaller") and including one more 
          $e_i,i=1\sim n-1$ (case 2 in [primsproof]), contradiction. <a name="MST_scratch"></a>
          - **Notice**
            > Let T be a *minimum spanning tree* of G containing the edges e1, e2, … , ek, where k is the *maximum* integer

            *doesn't need the "incident" requirement*.
            - This also *implies* we can derive Kruskal’s without the stronger conditions in Prim’s, although the [original paper](https://sci-hub.hkvisa.net/10.1090/S0002-9939-1956-0078686-7) doesn't mention it by something like "Prim" or "incident".
    - > Prim’s algorithm hasn’t selected edge {a, b} yet
      because $a\in W, b\notin W$ while selected edge $w=(u,v),\{u,v\}\subseteq W$
- ~~> Kruskal’s algorithm can be carried out using O(m log m) operations and Prim’s algorithm can be carried out using O(m log n) operations.~~
  ~~By CRLS, they are same with "O(m log n)".~~
  > it is preferable to use Kruskal’s algorithm for graphs that are sparse,
  But it is shown in CRLS both in 3rd and 4th exercise 23-2 that we can improve only for Prim’s further.
## 12
### 12.1
- > Boolean algebras may also be defined using the notion of a lattice
  1. Identity laws <a name="lattice_boolean_algebra"></a>
    here 0 may mean the *least possible* number
    This is [Bounded lattice](https://en.wikipedia.org/wiki/Boolean_algebra_(structure)#Definition)
  2. Associative laws are trivial
  3. Commutative laws are trivial
  4. distributivity *may not hold*. See [not_distributive_lattice]
  5. complements see 9-supplementary-43
  6. absorption shown in wikipedia: trivial since the upper bound of $a$ and one lower bound of $a$ is trivially $a$.
### 12.2
- > any Boolean function can be represented by a Boolean sum of Boolean products of the variables and their complements.
  This problem first occurs in COD where I said "TODO learn the boolean algebra"
- "disjunctive normal form of the Boolean function" is same as "Exercise 46 in Section 1.3".
- $\overline{x}=\overline{x\land x}=x\vert x$
  - $\overline{xy}=\overline{x}\lor \overline{y}=\overline{x\land y}=x\vert y$  
    Then use the above, we have $xy=(x\vert y)\vert(x\vert y)$
### 12.3
- FIGURE 9 A full adder
  it calculates the sum of 3 single bits $x+y+c_i$
  - $s=s_{x+y}\overline{c_i}+\overline{s_{x+y}}c_i=\ldots+(xy+\overline{x}\overline{y})c_i$
  - Here $c_{i+1}=s_{x+y}c_i+xy$
  - This is same as [wikipedia][full_adder] says which is also show in [asm_doc].
    - ~~TODO~~
      > The above expressions for ${\displaystyle S}$ and ${\displaystyle C_{in}}$ can be derived from using a *Karnaugh map to simplify* the truth table.
      maybe similar to [this](https://stackoverflow.com/questions/34687917/detecting-xor-in-karnaugh-maps#comment137461623_34687917)
      - [asm_doc] only shows examples using $+,\cdot$ without using $\oplus$
        and "Maxterm" is already said in this book.
        - But since $x\oplus y=x\overline{y}+\overline{x}y$ which is *sum-of-products*,
          we can still use the Karnaugh map
### 12.4
- heuristic (or rule-of-thumb) methods
  i.e. [based on experiences](https://www.mindtools.com/a01ufjx/heuristic-methods)
- [literal](https://en.wikipedia.org/wiki/Literal_(mathematical_logic)) i.e. $x,\neg x$ or $1,\neg 1=0$ in TABLE 3
- > we can eliminate from the table *the row for a minterm* if there is another minterm that is covered by a subset of the prime implicants that cover this minterm.
  This may means row $r_i$ has *only one* minterm $t_i$
  and there is another row $r_k$ which has $t_i$ and *other minterms*.
  TODO So same as
  > we can simplify the table by eliminating the rows for minterms *covered* by these prime implicants
  - [wikipedia examples][Quine_McCluskey_example] finds "the essential prime implicants" $BC'D'$ and adds necessary 1 or more non-essential ones without using the above *a bit complex* tricks.
    - Notice here 9,14 with `f=x` "where 'x' stands for don't care".
    - [consensus theorem](https://en.wikipedia.org/wiki/Consensus_theorem)
      here consensus $yz$ (i.e. $y=z=1$) *isn't excluded* by $xy\lor \overline{x}z$.
      e.g. if we use $xy\lor \overline{x}\overline{z}\;(*)$ then 
      $(0,1,1)$ will have $0$ for $(*)$ so we must have 
      $yz$ to make the whole expression be 1 as expected by $xy\lor \overline{x}\overline{z}\lor yz$.
- whether Karnaugh Map and Quine-McCluskey method "generate the circuit with the *minimum inputs and minimum gates*" [TODO](https://cs.stackexchange.com/q/165508/161388)
- > A K-map in *three* variables is a rectangle divided into eight cells ... This K-map can be thought of as lying on a *cylinder*
  > The K-map of a sum-of-products expansion in *four* variables can be thought of as lying on a *torus*, 
  Here "A K-map in *three* variables" doesn't need "torus" because $x,\overline{x}$ always has distance 1 either in the cylinder or the torus. See FIGURE 9-(c)
- > the rows and columns of a K-map are arranged using Gray codes
  i.e.
  > each string *differs in exactly one position* from the preceding bit string, and the last string differs from the first in exactly one position
  same as K-map
- 12.4.2
  > the goal is to identify the largest blocks of 1s in the map that correspond to the *prime implicants* and to cover all the 1s using the *fewest* blocks needed, using the *largest blocks first*.
  [comparison](https://math.stackexchange.com/questions/4458965/proof-of-karnaughk-map-method/4459351#comment10361492_4459351) between K-map and Quine-McCluskey which shows the *greatest* prime implicant may be not included in the *optimal* solution.
  > We begin by selecting the *essential* prime implicants because each of these is represented by a block that covers a cell containing a 1 that is not covered by any other prime implicant. We add *additional* prime implicants to ensure that all 1s in the K-map are covered.
  This is same as the above [Quine_McCluskey_example]
  - Notice the Quine-McCluskey may be [not optimal](https://cs.stackexchange.com/questions/165508/prove-or-disprove-that-the-quine-mccluskey-method-generates-the-circuit-with-the#comment343984_165508) in [some cases](https://cs.stackexchange.com/questions/165508/prove-or-disprove-that-the-quine-mccluskey-method-generates-the-circuit-with-the#comment344058_165508).
## 13
### TODO after formal language theory
~~- [Chomsky hierarchy](https://en.wikipedia.org/wiki/Chomsky_hierarchy#Recursively_enumerable_(Type-0)_grammars) especially type-3,0.~~
- TODO [prove](https://courses.cs.washington.edu/courses/cse322/09sp/lec16.pdf) a set is recognized by a pushdown automaton if and only if it is the language generated by a context-free grammar.
- > linear bounded automata can recognize context-sensitive languages
  proof
- > It can be shown that a set can be recognized by a Turing machine if and only if it can be generated by a type 0 grammar, or in other words, if the set is generated by a phrase-structure grammar. The proof *will not be presented here*.
- > Turing machines can model all the computations that can be performed on a computing machine
### 13.1
- here $T^{*}$ may mean "The set of all words over" T (i.e. terminals)
  based on 
  > The set of all words over V
- example 
  - 4: here only one is used in the recursive definition, so only one *new string* of terminals is generated at each iteration.
    - using one binary tree can easily see the result.
  - 5 is still based on induction.
    similar to 4
  - 6 is based on induction of $m+n=k$ (i.e. if this grammer can generate for k, then it can generate for k+1).
    This is done by $S\to 0S$ and $A\to 1A$ to add one 0/1.
    - See exercise 12
      we also need to show it can't have forms other than $0^m 1^n$.
      1. only 0,1. This is ensured by $T$
      2. all 0's are on the left of 1's
        since 0 can be only generated by $S\to 0S$. So all 0's must be at the left (same as $G_1$).
        Then 1 is done by $S\to 1A/1$ and then transform $A/1A$.
    - similar to [this](https://en.wikipedia.org/wiki/Context-free_grammar#Second_block_of_b's_of_double_size) where it is Context-free because LHS has no forms like as $BA$ example 7.
- 13.1.4 same as [this][Chomsky_hierarchy]
  - TODO
    1. why define for type-1
      > It can also have the production S → 𝜆 as long as S does not appear on the right-hand side of any other production. 
      - Notice type-3 is also as the above
        > The rule ${\displaystyle S\rightarrow \varepsilon }$ is also allowed here if ${\displaystyle S}$ does not appear on the right side of any rule
      - Based on example 8 and 6, $S\to 0S,S\to \lambda$
        "on the right side of any rule" means *alone* on the right.
  - > only when it is surrounded by the strings l and r.
    by [this][type_1_grammar], $S\to aBC$ is allowed.
    So the above should be "if sometimes it is surrounded ...".
- example 8 notice here $G_1$ is not Regular but Context-free.
- As FIGURE 1 shows,
  > A derivation in the language generated by a *context-free* grammar can be represented graphically using an *ordered rooted tree*, called a derivation, or parse tree.
  Here each $A$ in [$A\to \alpha$][Chomsky_hierarchy] can function as one internal leaf
  and each symbol $\alpha$ from left to right are its children from left to right which implies ["ordered"][ordered_rooted_tree] (i.e. children are ordered w.r.t. their [~~direct~~ immediate ~~parent~~ ancestor](https://ducmanhphan.github.io/2020-04-25-Some-common-concepts-of-tree/)).
- "[AhLaSeUl06]" may be "[AhHoUl74] A. V. Aho, J. E. Hopcroft, and J. D. Ullman, The Design and Analysis of Computer Algorithms, "
- Definition 3 also [see](https://en.wikipedia.org/wiki/Formal_grammar#Formal_definition)
- 13.1.3 A type 3 grammar is the [extended one](https://en.wikipedia.org/wiki/Regular_grammar#Extended_regular_grammars).
- phrase structure grammar is [also called formal grammar](https://en.wikipedia.org/wiki/Formal_grammar#The_syntax_of_grammars).
### 13.2
- The book definition 1 is similar to [this][13_2_definition_1] which is one specific version of [this](https://en.wikipedia.org/wiki/Finite-state_transducer#Formal_construction)
### 13.3
- Kleene closure is similar to connectivity relation where both is related with the power operation.
- [definition 3](https://en.wikipedia.org/wiki/Deterministic_finite_automaton#Formal_definition)
  - Here we have no output alphabet and output function but have the final/accepting states in [13_2_definition_1]
- Computable, i.e. [The Halting Problem in 3.1.6](https://www.geeksforgeeks.org/computable-and-non-computable-problems-in-toc/) and [Decidability](https://www.geeksforgeeks.org/decidability-and-undecidability-in-toc/) which is based on reduction.
- example 6
  - a) it trivially enumerates all possible bit strings.
  - b,c,d,e) are related.
- example 7 
  1. trivially enumerates all possible ~~cases~~ states
  2. has 2 input cases for each state.
  So it enumerates all possible cases.
- example 8
  - > We leave it to the reader to fill in the details.
    trivial listing all possible cases.
  - we can also find that $s_0\to s_2\to s_4,s_0\to s_1$ in $M_0$ can be combined into 
    $s_0\to s_1$ in $M_1$.
- > the reader should provide an inductive proof of this
  maybe based on the definition of "recognize" in THEOREM 1.
- notice in EXAMPLE 12, $\{s_0,s_2\}$ only 
  $s_0$ is the final state in Example 10.
  Although letting $\{s_0,s_2\}$ be the final state in EXAMPLE 12 may be ambiguous because it includes oen unnecessary 
  $s_2$, letting $\{s_0,s_2\}$ not be the final state will be *wrong*. 
  So we let $\{s_0,s_2\}$ be the final state.
### 13.4
- EXAMPLE 1
  "any string not ending with 0" can be manipulated from the end back
  where each 1 and the following subsequent continuous are seen as one group (i.e. $0^*1$)
  - similarly, EXAMPLE 2 b) 
    from the ending 0, we either meet the next 0 (i.e. $0^*0$)
    or 1 (i.e. $10$) from where we either meet 0 (i.e. $0^*10$) (from here we can recursively use the process just used) but not 1.
    - c)
      > split into blocks each starting with a 0 and containing one more 0
      starting with 1 is contained in the ending $1^*$ of 
      $1^* 0 1^*$
      - in summary this is based on the process of finding consecutive 0 which may meet 1 between each pair of 0's/
- THEOREM 1 if part proof 
  - $\varnothing$
    > To do this, all we need is an automaton with no final states.
    TODO Here it is still one [deterministic finite automaton](https://en.wikipedia.org/wiki/Deterministic_finite_automaton#Formal_definition).
    - But all DFAs can be [seen as NFA](https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton#Equivalence_to_DFA).
  - $\{\lambda\}$
    > The nondeterministic automaton in Figure 1(b) shows such a machine.
    here it uses one [DFA_partial_transition_function].
  - $AB$
    > Note that we can assume that SA and SB are disjoint
    if not disjoint, then still do $\cup$ where the duplicate States only exist once.
    - > Start state is sAB = sA, which is final if sA and sB are final.
      here we can see start directly go to $s_B$ which is a final state with input $\epsilon$, so the original graph still holds.
      - It means $𝜆 ∈ A \cap B$
      - > Transition from sB in MB produces a transition from sAB = sA. 
        TODO IMHO this should not be contained except when $s_A$ is final so that we can directly go into $M_B$.
        - It is same as [Elements_of_Theory_of_Computation_2ed_Lewis_Papadimitriou] ~~$s_A\xRightarrow{\epsilon}s_B\xRightarrow{i}(s_B,i)$~~
        - This is also impled in the example 3 $01$ [see][overleaf_automata].
  - $A\cup B$
    - > {sA∪B} if 𝜆 ∈ A ∪ B
      It is implied in $s\xRightarrow{e}s_{1,2}$ in [Elements_of_Theory_of_Computation_2ed_Lewis_Papadimitriou]
  - [Elements_of_Theory_of_Computation_2ed_Lewis_Papadimitriou]
    - $A\cup B$
      - here $(s,e,sl),(s,e,s2)$ are both $e$ so "nondeterministically".
      - $(s,ew)=(s,w)|-_{M}(s_1,w)$
    - $\circ$ see p56 concatenation
    - $AB$ uses $\epsilon$ which the book doesn't use.
    - $A^*$
      - > M consists of the states of M1 and all the transitions of M l ; any final state of M1 is a final state of M
        since the power operation *doesn't incur new states* and other new things.
      - > This new initial state is also final, so that e is accepted.
        implies $e=\lambda=A^0$
      - $s_1'\to s_1$ is to ensure $A^1$ can be run
        and $s_i\in F_1, s_i\to s_1$ is to ensure $A^k\to A_{k+1}$ inductive step.
- example 3 $s_{12}\to s_{17}$ is unnecessary.
  - FIGURE 3 b) removes all replaced states in a).
- [regular set](https://www.tutorialspoint.com/automata_theory/regular_sets.htm) definition
- phrase structure grammar is [related](https://en.wikipedia.org/wiki/Phrase_structure_grammar) with [constituency relation](https://en.wikipedia.org/wiki/Dependency_grammar#Dependency_vs._phrase_structure) which tries to split the component while dependency tries to concatenate.
- THEOREM 2
  - only if
    - here $a,\lambda,aB$ is included in [Elements_of_Theory_of_Computation_2ed_Lewis_Papadimitriou] p62 regular definition (1),(4),(2).
    - better see the example 4 to see how this works.
  - if
    - > The production S → 𝜆 is included in P if and only if 𝜆 ∈ L(M)
      "only if" is already proved in the above "only if" proof.
      "if" means $\lambda$ is accepted i.e. one terminal forming one accepted string. So $S\to \lambda$.
    - > Because the productions of G correspond to the transitions of M and the productions leading to terminals correspond to transitions to final states
      find the correct mapping between 
      1. "production" and "transition".
      2. "*to* terminal" and "to final state"
        notice here terminal also functions as the input while the final states don't.
    - example 5
      - here $S\to 1,A\to 1$ because $B\to \lambda$ is not allowed.
        so $01$ is not recognized by $S\to 0A,A\to 1B,B\to 1$.
        - or more specifically, we must hava $A\to \alpha$ to *make the production end* where the $\alpha$ is its *last* production implying pointing to the final state.
- EXAMPLE 6
  - > Let s0, s1, s2, … , s2N be the sequence of states that is obtained starting at s0
    here assumes states in the sequence can be same so the minimal path can be any length $\le 2N$.
  - is same as exercise 13.~~4~~3-57 where $n$ is same as here $N$ but it uses $0^{n+1}$ which will bring 
    $s_0\to s_{n+1}$ which has $n+2$ states.
- $\{0^n1^n ∣ n = 0, 1, 2, ... \}$ can be recognized by [the context-free grammar](https://stackoverflow.com/a/28721319/21294350).
  - corresponding [PDA](https://en.wikipedia.org/wiki/Pushdown_automaton#Example)
    - Here $AZ,AA$ includes the original top and the pushed symbol.
    - Here [both modes](https://en.wikipedia.org/wiki/Pushdown_automaton#Formal_definition) of accepting are met.
### 13.5
- > finite-state automata to compute relatively simple functions such as the sum of two numbers
  [see](https://cs.stackexchange.com/a/49348/161388)
- > we can include the five-tuple (s2, 0, s2, 0, R)
  Here we should also have (s2, 1, s2, 1, R) because "(s1, 0, s2, 0, R)" only implies the *old* 0 is unchanged but after R we may have the symbol *0 or 1*.
- > many possible ways to define how to recognize sets using Turing machines
  See [this](https://human.libretexts.org/Bookshelves/Philosophy/Sets_Logic_Computation_(Zach)/03%3A_Turing_Machines/12%3A_Turing_Machine_Computations/12.08%3A_Variants_of_Turing_Machines)
  > We allow the machine to write a symbol to the tape and move at the same time, other definitions allow *either writing or moving*.
- EXAMPLE 2
  - > the machine will terminate in the nonfinal state s2
    > will terminate in the final state s3
    So s2 should be similar to s3 where both has no something like $(s2, 0, s2, 0, R)$.
    - Here (s0, B, s2, 0, R) and (s1, B, s2, 0, R) may unnecessarily change tape because we only want to *recognize* strings.
    - Then the machine will *halt* at the *nonfinal* state $s_2$ due to the undefined transition rule, so the string is not recognized.
      So we *also don't need* "(s0, B, s2, 0, R) and (s1, B, s2, 0, R)" where we may halt at the *nonfinal* state $s_{0,1}$.
  - > the bit string has at least two bits and the second bit of the input string is a 1
    "at least two bits" is implied by "(s0, B, s2, 0, R) and (s1, B, s2, 0, R)".
    "the second bit of the input string is a 1" is implied by "(s1, 1, s3, 1, R)".
  - Also see this example which shows the *terminating transition rule* $(s_0, B, s_2, B, R)$ containing 
  $B$
- EXAMPLE 3
  Here "(s3, M, s5, M, R)" is used when "MMMMMM" after "(s2, 1, s3, M, L)" for the 4th symbol 1 in "MMM1MM".
  - Here "(s5, M, s6, M, R)" is to ensure $n\ge 1$ in "$\{0^n1^n ∣ n \ge 1\}$".
- Normally, "number-theoretic function" has positive integer domain instead of the tuple of integers.
- EXAMPLE 4
  Here we have $n_1+1+1+n_2+1$ characters and we want $n_1+n_2+1$ 1s left.
  so "(s0, 1, s1, B, R)" removes the *first* character
  and "(s1, ∗, s3, B, R), (s1, 1, s2, B, R)" removes the *2nd* where "(s1, ∗, s3, B, R)" already has all 1s left so we terminate and 
  after "(s1, 1, s2, B, R)" we need to ensure all left characters are 1s by "(s2, 1, s2, 1, R), and (s2, ∗, s3, 1, R)".
- TODO 
  > build up multitape Turing machines for the composition of functions
  [1](https://www.hse.ru/mirror/pubs/share/167262307) [2](https://gyires.inf.unideb.hu/GyBITT/26/ch04s05.html)
- > using (2 + 3n)-tuples to describe the Turing machine when n tapes are used
  see [this](https://en.wikipedia.org/wiki/Multitape_Turing_machine#Formal_definition) where 2 corresponds to $Q\setminus F,Q$
- > we can restrict the tape to be infinite in only one direction
  i.e. only right direction when transformed from DFA.
- > While the Church Turing Thesis is generally accepted as true, it's important to clarify that it's *not formally proven*
  [See](https://www.studysmarter.co.uk/explanations/computer-science/theory-of-computation/church-turing-thesis/#:~:text=While%20the%20Church%20Turing%20Thesis,nature%20of%20'effective%20computability'.)
- Definition 4
  here a computer program always has one [corresponding Turing machine](https://en.wikipedia.org/wiki/Turing_completeness#Non-mathematical_usage), also [this](https://cs.stackexchange.com/a/142895/161388)
  TODO proof
- > That is, no Turing machine exists that
  is based on "the Church–Turing thesis".
- > It is fairly straightforward, using a *countability* argument, to show that there are number-theoretic functions that are not computable (see Exercise 39 in Section 2.5).
  - ~~TODO~~ [Why doesn't Cantor's diagonal argument also apply to *natural numbers*?](https://math.stackexchange.com/a/35109/1059606)
    [See](https://math.stackexchange.com/questions/35107/why-doesnt-cantors-diagonal-argument-also-apply-to-natural-numbers#comment10397344_35109)
- > In a nondeterministic Turing machine, allowed steps are defined using a relation consisting of five-tuples rather than using a partial function
  here (relation,partial) may corresponds to [(multivalued,well-defined)](https://math.stackexchange.com/a/271615/1059606)
- > For a problem to be in NP, it is necessary only that there be a *nondeterministic* Turing machine that, when given a true statement from the set of statements addressed by the problem, can *verify* its truth in *polynomial* time
  "verify" should be ["solvable"](https://en.wikipedia.org/wiki/NP_(complexity))
- Although [a non-deterministic Turing machine can be converted into a deterministic Turing machine](https://cs.stackexchange.com/a/16797/161388) ([also](https://cs.stackexchange.com/a/148937/161388)), but [the running time may be not same](https://cs.stackexchange.com/a/93151/161388) for them
## Appendix
### 1
- THEOREM 7 can be also used to prove 'the identity elements axiom'
  'Consequently, −1 = 0' which is trivially wrong by Theorem 1.
- [ARCHIMEDES method](https://maa.org/press/periodicals/convergence/archimedes-method-for-computing-areas-and-volumes-introduction) for computing the area under a curve
- Archimedes [expressing large integers inexpressible by the usual Greek method](https://web.calstatela.edu/faculty/hmendel/Ancient%20Mathematics/Archimedes/SandReckoner/SandReckoner.html)
- THEOREM 8 is based on 'the completeness property'.
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
  - [product](https://tex.stackexchange.com/a/32827/308105)
- [bmod -> binary mod](https://tex.stackexchange.com/a/42872/308105)
- [big equal sign](https://tex.stackexchange.com/a/35406/308105) needs extra package or self define length `\mathrel{\mkern-3mu}`.
- [Stirling number](https://tex.stackexchange.com/a/86064/308105) or use [wikipedia one](https://en.wikipedia.org/wiki/Stirling_numbers_of_the_second_kind#Recurrence_relation)
- Roman number by [plain Tex](https://tex.stackexchange.com/a/23491/308105) `\romannumeral #1`.
## doc
- [1](https://latexref.xyz)
- font ["LaTeX Font Catalogue"](https://tug.org/FontCatalogue/mathfonts.html) from [this](https://tex.stackexchange.com/a/58124/308105)
- symbols using [deTeXify or others](https://tex.stackexchange.com/a/21/308105)
  notice [usage](https://tex.stackexchange.com/questions/14/how-to-look-up-a-symbol-or-identify-a-letter-from-a-math-alphabet-or-other-chara#comment1630644_14)
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
# miscs with sympy usage
- use `apart` for the Partial fraction decomposition
- use `rational_algorithm` for finding the coefficient for rational generating function like $\frac{p(x)}{q(x)}$
# TODO after one specific graph theory book
- [alternating_path_Hall_Marriage_Theorem]
- [this](https://math.stackexchange.com/questions/2490502/counting-techniques-to-find-all-nonisomorphic-graphs-with-six-vertices-all-havi#comment9806829_2490933)
# TODO after abstract algebra
- [this](#RSA_Cauchy_theorem)
- [this](#abstract_algebra_2)
- [equivalence_relation_definition]
  - Also questions for the partial ordering.
- dihedral group in 9.5-58
- semigroup and [Semilattice](https://proofwiki.org/wiki/Definition:Semilattice) about lattice in 9.6
- [Duality](https://en.wikipedia.org/wiki/Duality_(mathematics)) relation with [Involution](https://en.wikipedia.org/wiki/Involution_(mathematics)), i.e. [bijection](https://math.stackexchange.com/questions/4834752/provide-a-closed-formula-based-on-the-generating-function-fracx1xx2#comment10294429_4834850).
  > but also indicates that the precise meaning of duality may vary from case to case.
  so it may be difficult to give one exact definition for all cases.

  We can just think it as the meaning of *pair*.
  - By [duality_onto_with_one_to_one]
    here the 2nd $g$ *may be not same* as the 1st $f$ where it may not map the rest *all to $x_0$*
    But the proof process is very similar.
- [This](https://math.stackexchange.com/q/3383113/1059606) related with 9-supplementary-43 and isomorphic. (example from [wikipedia](https://en.wikipedia.org/wiki/Distributive_lattice))
- [chain vs cycle](https://en.wikipedia.org/wiki/Chain_(algebraic_topology)) [Also](https://math.stackexchange.com/a/3554072/1059606)
- Burnside's lemma. See 10.3-74.
- "Integers Modulo m under Addition" in mcs 9.7
- TODO relation with [p-adic valuation](https://en.wikipedia.org/wiki/P-adic_valuation)
# TODO after set theory or order theory
- [This](https://math.stackexchange.com/a/3896116/1059606) related with 9.6-38.
# TODO after mathematical analysis
- [This](#sup_Hardy_Littlewood) due to it may probably [introduce the supremum](https://math.stackexchange.com/q/4173249/1059606)
- > the completeness of ≤, i.e. the least upper bound property.
  from Appendix 1
  why they mean same?
# TODO after Computer Networking
- 6.1 -> "1111111 is not available as the netid of a Class A network"
  also "hostids consisting of all 0s and all 1s are unavailable".
- 11.4 IP Multicasting
  why it can't have the loop.
- mcs 11.2
# TODO after algorithm
- [6.2-27](https://leetcode.cn/problems/longest-increasing-subsequence/description/?utm_source=LCUS&utm_medium=ip_redirect&utm_campaign=transfer2china)
- Why is [this](#Pseudo_polynomial) based on the length of the input instead of the value?
- [This](https://stackoverflow.com/q/33590974/21294350) related with [scc]
  CRLS gives the detailed proof.
- the above [safe_edge_MST]
- The above "B-tree".
- mcs
  > In fact, the O.n2:55/-operation multiplication pro-cedure is almost never used in practice because it only becomes relatively efficient on matrices of impractical size.
# TODO after compiler
- [This](https://stackoverflow.com/a/575337/21294350) related with naming and binding in 10_5_64 code.
# TODO after complexity book
- [This](https://cs.stackexchange.com/questions/165101/how-can-the-approximation-algorithm-of-one-np-complete-problem-be-used-to-prove#comment342996_165101)
- decidable but not computable problems from [this](https://www.geeksforgeeks.org/difference-between-decidability-and-computability/)
- [recursive function](https://en.wikipedia.org/wiki/General_recursive_function)
# TODO after computablity theory
- [This](https://math.stackexchange.com/a/462795/1059606)
# TODO after logic
- 12.2-20-b)

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

<!-- csapp -->
[csapp_doc]:https://github.com/sci-42ver/csapp3e/blob/master/asm/README.md

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

[asm_doc]:https://github.com/sci-42ver/csapp3e/blob/master/asm/README.md

<!-- proofwiki -->

<!-- crypto stackexchange -->
[RSA_coprime_guarantee]:https://crypto.stackexchange.com/a/25649
[RSA_proof]:https://crypto.stackexchange.com/a/1006

<!-- Math-for-CS-solutions -->
[sol_20]:./others/mcs/sol/Math-for-CS-solutions/MIT6_042JS15_cp20_solutions.pdf