# How long I have taken to read the book
- From May 26 to Jun 2 (7 days), I 
  read the preface of some books
  check the book list and course list
  and decided to learn sicp and other related books.
# course
1. ~~all~~ most of them are based on lectures and use *multiple* textbooks as the reference
2. CS 161 recommend [Tim Roughgarden](https://www.youtube.com/channel/UCcH4Ga14Y4ELFKrEYM1vXCg/playlists)
3. I mainly cares about books and Prerequisites.
4. course list about algorithm rank from high to low based on the numbers of *general* courses (the latter 2 don't have corresponding graduate general courses for algorithm)
  list
  - mit
  - UIUC
  - cmu
  - stanford
  - ucb
  summary
  - cmu has 2 specific algorithm courses for graduate but has less general algorithm courses.
    stanford has *no* specific algorithm courses for graduate but has *more* general algorithm courses.
    So their order may exchange.
    mit has all the above 2 advantages while ucb has none.
    UIUC is similar to cmu but has *very useful* reference list.
  - These 4 universities [may be enough](https://www.usnews.com/best-graduate-schools/top-science-schools/computer-science-rankings)
    although [scientist rank](https://research.com/scientists-rankings/computer-science) which is [not h-index](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8238192/) doesn't follow that
    - The best is [unknown](https://careervillage.org/questions/767986/answers/769058)
    - TODO also [see](https://qr.ae/psSRT3)
5. algorithm book order based on university reference count (mainly based on *general* algorithm courses)
  data structure see uiuc
  - CRLS (s,m,c,u) with high proportional mathematics proof
    it is highly used in cmu 2020 and mit
  - DPV (s,c,ucb,u)
    recommended in "Useful Resources" in uiuc
  - Kleinberg (s,c,u)
  - JeffE (c,u)
    *highly recommended* by cmu and uiuc (the latter is trivially due to it is written by one uiuc professor)
  - Algorithms Illuminated (s,c->15750)
    It is preferable than the following 2 because s->CS369B is taught by the author.
  - kozen (s->CS369B,c->15750)
    Aho, Hopcroft & Ullman (s->CS369B,[c->15-451/651~2020](https://www.cs.cmu.edu/~15451-f20/resources.html) which has one more full list than 2024 / 15750,)
  - The following searches have no valuable results about the related university
    stanford algorithm Jeff Erickson
    mit Dasgupta, Papadimitriou, and Vazirani
    uc berkeley "CRLS" algorithm
    Algorithms Illuminated uiuc
    "Design and Analysis of Algorithms" uiuc (no related books)
  - ~~The above "Aho, Hopcroft & Ullman" are skipped since 2024 15-451/651 has dropped this book.~~
6. prerequisites of UG and G general courses (1. stanford have no general courses, so I checked its all related algorithm graduate courses 2. ucb has only 270 general course 3.) are mainly maths and basic programming (mostly use *object-oriented programming* with abstraction)
  except for
  - stanford -> Computer Organization & Systems
  - cmu -> *functional programming*
  - ucb -> *sicp*, Data Structures
  - uiuc -> Data structures, Computer Systems, hardware
In summary, I read CRLS. 
I use those general books in *shared* by *general* algorithm courses of different universities as the *main* reference and other specific books when studying related topics. (They are pdfs directly in CRLS/others dir and CRLS/others/Algorithms_Illuminated dir)
## stanford
### undergraduate
[CS 161](https://stanford-cs161.github.io/winter2024/resources/#textbook-information)
textbook list shares 3 with cmu 15-451/651 with "Algorithms by Jeff Erikson" -> "Algorithms Illuminated" (Notice cmu 15750 uses "Tim Roughgarden's lectures on Algorithms." as the reference).
See [Algorithms Problem-Solving Guide](https://stanford-cs161.github.io/winter2024/assets/files/algorithms-problem-solving-guide-.pdf) and [Algorithm Design Robot](https://stanford-cs161.github.io/winter2024/assets/files/robot.jpg)
- Prerequisites based on order 
  needs programming experience and related maths
  - [CS106A Programming Methodology](https://cs106a.stanford.edu/syllabus) with [no prerequisite](https://web.stanford.edu/class/archive/cs/cs106a/cs106a.1216/handouts/coursePlacement.html#) (also [see](https://bulletin.stanford.edu/courses/1056441) which has no "Prerequisite: ...") ([book](https://compedu.stanford.edu/karel-reader/docs/python/en/intro.html)) 
    [->](https://web.stanford.edu/class/cs106b/#prerequisites) [CS106B Programming Abstractions](https://web.stanford.edu/class/cs106b/#course-resources) [book](https://web.stanford.edu/class/cs106b/index.html#textbook)
  - [cs103 Mathematical Foundations of Computing textbook](https://web.stanford.edu/class/archive/cs/cs103/cs103.1246/syllabus#readings) [Prerequisites](https://web.stanford.edu/class/archive/cs/cs103/cs103.1246/syllabus#prerequisites)
    also uses "Introduction to the Theory of Computation"
  - [cs109 Probability for Computer Scientists](https://chrispiech.github.io/probabilityForComputerScientists/en/examples/mixture_models/) TODO with Machine Learning (Also see [its used Textbook "First Course in Probability"](https://web.stanford.edu/class/cs109/)) [Prerequisites](https://web.stanford.edu/class/cs109/handouts/FAQ.html)
    Math51
    > calculus (integration/differentiation) and linear algebra (basic operations on vectors and matrices)
### [graduate from stanford *online*](https://online.stanford.edu/courses/cs265-randomized-algorithms-and-probabilistic-analysis) no coursesite
a bit general courses like 261,168 has no textbooks.
- [2024 course list](https://explorecourses.stanford.edu/print?q=algorithm&descriptions=on&academicYear=&catalog=&page=0&filter-coursestatus-Active=on&collapse=&catalog=)
  [This search about "Algorithm"](https://explorecourses.stanford.edu/print?q=Algorithm&descriptions=on&academicYear=&catalog=&page=0&filter-coursestatus-Active=on&collapse=&catalog=) is weird since it doesn't have [CS 369O: Optimization Algorithms](https://explorecourses.stanford.edu/search?view=catalog&filter-coursestatus-Active=on&page=0&catalog=&q=CS+369O%3A+Optimization+Algorithms&collapse=).
  - I skipped due to they are specific
    1. CS 227A: *Robot* Perception: Hardware, Algorithm, and Application (EE 227)
      EE 227: Robot Perception: Hardware, Algorithm, and Application (CS 227A)
    2. MS&E 238: Computational and Algorithmic Aspects of *Fairness*
    3. CS 354: Topics in *Intractability*: Unfulfilled Algorithmic Fantasies
- [all CS algorithm](https://bulletin.stanford.edu/courses?cq=algorithm&subjectCode=CS&page=2) course list
  - I skipped
    - Algorithms for Interactive *Robotics*
    - Topics in *Geometric* Algorithms: Non-Euclidean Methods in Machine Learning
    - CS207 Antidiscrimination *Law* and Algorithmic Bias
      CS369O Optimization Algorithms no website
    - ~~CS125~~ [cancelled](https://law.stanford.edu/courses/data-algorithms-tools-policy-and-society/)
    - the following 2 are too specific
      - [cs256 algorithmic-fairness](https://omereingold.wordpress.com/cs-256-algorithmic-fairness/) ~~no course website~~
        based on CS 161 and [221 Artificial Intelligence](https://stanford-cs221.github.io/spring2024/)
        - cs 154 [(1) Introduction to the Theory of Computation](https://omereingold.wordpress.com/cs-154-introduction-to-automata-and-complexity-theory/) / [(2)](https://explorecourses.stanford.edu/search?view=catalog&filter-coursestatus-Active=on&q=CS%20154:%20Introduction%20to%20Automata%20and%20Complexity%20Theory&academicYear=20182019)
          they may be same due to the same Prerequisites
          uses book "Introduction to the Theory of Computation"
      - [cs368 Algorithmic Techniques for Big Data](https://cs368-stanford.github.io/spring2022/) maybe [no textbook](https://cs368-stanford.github.io/spring2022/lectures.html)
        TODO prerequisite
  - The following 3 *prerequisites* are 
    basic algorithm course
    maths like probability
    and programming experience
  - [CS 261 Optimization and Algorithmic Paradigms](https://web.stanford.edu/~ashishg/cs261/) [part book](https://drive.google.com/file/d/1-4cBBLszFzjN79AylvGDJa4sFYNRawG-/view)
    Prerequisite: 161
  - [cs265 Randomized Algorithms and Probabilistic Analysis](https://web.stanford.edu/class/cs265/index.html#classes) mainly based on lectures and papers
    - prerequisite
      CS 161
      - [STAT 116](https://web.stanford.edu/class/stats116/texts.html) which is [substituted into 117,118](https://mcs.stanford.edu/news/stats-116-will-be-replaced-stats-117-and-stats-118)
        uses "First Course in Probability" and "Introduction to Probability, Joe Blitztein and Jessica Hwang" which are known when I prepared for Chinese graduate entrance exam.
  - [CS 168 The Modern Algorithmic Toolbox](https://web.stanford.edu/class/cs168/) maybe no textbook use
    - prerequisite
      CS161
      [CS107 Computer Organization & Systems](https://web.stanford.edu/class/archive/cs/cs107/cs107.1246/syllabus.html#course-overview) -> Prerequisites CS106
      > translating C to/from *assembly*
      > a working understanding of the basics of *computer architecture*
      > understanding *compilers and disassemblers*
### Algorithms Illuminated (I didn't give one summary about their prerequisites because they are old courses)
See [notes](https://github.com/claytonjwong/Algorithms-Illuminated)
- See [author page](https://timroughgarden.org/videos.html)
  -  364a Algorithmic Game Theory seems to be removed in 2024.
    similarly for 364b which is [now](https://stanford.edu/class/ee364b/index.html) and 264 [now](https://web.stanford.edu/class/cs246/)
    - see 364a,b [booklist](https://timroughgarden.org/f13/f13.html)
      - 364a prerequisite
        154N [maybe](http://kilby.stanford.edu/~rvg/154/)
    - 264 seems *no book*
  - CS261 [old](https://www.youtube.com/playlist?list=PLEGCF-WLh2RJh2yDxlJJjnKswWdoO8gAc) *no textbook*
- full [list](https://timroughgarden.org/teaching.html) (only read Stanford Courses)
  - CS167 *skipped*
  - CS364B only the latter kept is checked (i.e. Frontiers in Mechanism Design. See above)
  - [CS369B](https://timroughgarden.org/w08b/w08b.html) with comprehensive booklist -> 261
    with "Kozen, Design and Analysis of Algorithms." shared with cmu 15750
    "Tarjan, Data Structures and Network Algorithms."
  - CS369C is one old course including [old 15-859](https://cstheory.stackexchange.com/questions/9901/an-intuitive-justification-metric-embedding-based-approximation-algorithms) [highly dependent on papers](https://www.cs.cmu.edu/~anupamg/metrics/)
    mainly about Discrete *Geometry*.
  - CS369E with no textbook
## mit
1. check [prerequisite](https://catalog.mit.edu/subjects/6/)
2. graduate course updates are more frequent then undergraduate.
It only uses CRLS for undergraduate courses and other *more specific* books for 6.5210.
### undergraduate
prerequisite maths & programming experience
- 6.1210 Introduction To Algorithms [using CRLS in 6.006][mit_6_006_2020]
  - prerequisite
    - [6.100A Introduction to Computer Science Programming in Python](https://introcomp.mit.edu/fall23?course=0001) (2024 ~~probability change name because they share the same textbook ->~~ uses 6.100B name [Introduction to Computational Thinking and Data Science](https://introcomp.mit.edu/spring24/information) for the website)
      - [old book](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/pages/readings/)
      - goal
        > Together, these classes provide an introduction to the role that computation can play in solving problems.
      - [python book](https://introcomp.mit.edu/spring24/additional_resources)
      - TODO read [this guide](https://introcomp.mit.edu/spring24/styleguide) to avoid some mistakes
    - 6.120A or 6.1200[J] Mathematics for Computer Science which I have read its mcs 2018.
- [6.1220 Design And Analysis Of Algorithms](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/pages/syllabus/) using CRLS
  - prerequisite
    ~~6.1200[J]~~ (duplicate with the above)
    6.1210
### graduate
prerequisite maths & basic algorithm
- 6.5210 [book](https://6.5210.csail.mit.edu/info.html)
  prerequisite 6.1220[J] and 
  ~~(6.1200[J] or ...)~~ (duplicate with the above)
  - [lec](https://6.5210.csail.mit.edu/materials.html)
### course [list](https://catalog.mit.edu/degree-charts/master-computer-science-economics-data-science-course-6-14-p/) ([This](https://catalog.mit.edu/degree-charts/master-electrical-engineering-computer-science-course-6-p/) has no definite list)
Here I *didn't care about prerequisite* because they are for graduate and it seems impossible to learn all required prerequisites by self.
- 6.5220[J]	Randomized Algorithms -> [6.856J](https://ocw.mit.edu/courses/6-856j-randomized-algorithms-fall-2002/pages/syllabus/) uses the [same book](https://web.archive.org/web/20000622110130/http://www.cup.org/Reviews&blurbs/RanAlg/RanAlg.html) as 15852
- 6.5250[J]	Distributed Algorithms [book](https://people.csail.mit.edu/ghaffari/DA22/) uses "5.-NancyA.Lynch.DistributedAlgorithms.pdf".
- 6.7810 -> 6.438 Algorithms For Inference uses "Information Theory, Inference, and Learning Algorithms.pdf".
- doesn't contain (I skip "Common Ground for Computing Education" because they are too specific) the following in the catalog
  [6.5240 Sublinear Time Algorithms](https://people.csail.mit.edu/ronitt/COURSE/F22/index.html#:~:text=The%20study%20of%20sublinear%20time,applied%20to%20analyzing%20such%20algorithms.) cares about Property Testing
  6.5350 Matrix Multiplication and Graph Algorithms -> [6.890](https://people.csail.mit.edu/virgi/6.890/)
#### *full* [list](https://student.mit.edu/catalog/index.cgi) -> [this catalog](https://catalog.mit.edu/subjects/6/)
- TODO
  6.5060 Algorithm Engineering [cares too much about papers](https://people.csail.mit.edu/jshun/6506-s23/)
  > For each lecture we will study several research papers; for each paper one student will give a presentation, which will be followed by a discussion.
## [cmu](https://csd.cmu.edu/sites/default/files/2023-08/MSCS%20Handbook%202023-2024.pdf) (from google or [this](https://csd.cmu.edu/academics/masters/ms-in-computer-science))
[B.S. IN COMPUTER SCIENCE CURRICULUM](https://csd.cmu.edu/bs-in-computer-science-curriculum) or [this](http://coursecatalog.web.cmu.edu/schools-colleges/schoolofcomputerscience/undergraduatecomputerscience/#bscurriculumtextcontainer)
[course search (TODO why 15750 can't be searched but it can be searched in enr-apps)](https://csd.cmu.edu/academics/courses)
[TODO](https://csd.cmu.edu/academics/undergraduate/requirements)
> Computer Science Undergraduate curriculum information for prior years is available on the Current Student Resources page.
- *book* recommendation
  it doesn't include skiena manual and Sedgewick Algorithms book in 15-451/651
  15750/850 contains 4 in 15-451/651 with others added.
- TODO check [objective](http://coursecatalog.web.cmu.edu/schools-colleges/schoolofcomputerscience/scsconcentrations/#algorithmsandcomplexitytextcontainer)
  > Relating algorithms and/or complexity of computation to a variety of complexity measures such as time, space, *communication, or information* content.
  > The understanding of several advanced algorithms *beyond what is covered* in the core.
  **especially**
  > The ability to understand and apply a variety of advanced algorithmic techniques and proof techniques, such as Lovasz Local Lemma, Johnson Lindenstrauss, Chernoff Bounds, sparsification, expanders, probabilistic method, regret bounds, spectral graph theory, fixed parameter tractability and semi-indefinite programming.
### undergraduate 15-451/651 [book](https://www.cs.cmu.edu/~15451-s24/FAQ.html)
[Prerequisites](http://coursecatalog.web.cmu.edu/schools-colleges/schoolofcomputerscience/undergraduatecomputerscience/#coursestextcontainer) are
maths
programming including functional programming
- TODO [15210 Parallel and Sequential Data Structures and Algorithms](https://www.cs.cmu.edu/~15210/)
  > this course puts an emphasis on parallel thinking
  - [textbook no use](https://www.diderot.one/courses/44/books/260/chapter/3075) ~~because it is [not intended](https://www.cs.cmu.edu/afs/cs/academic/class/15210-f12/www/lectures/all.pdf)~~
    [old](https://sites.google.com/view/algorithms-book/home) or [this](https://www.cs.cmu.edu/afs/cs/academic/class/15210-s14/www/lectures/)
    [newer in Diderot](https://www.cs.cmu.edu/afs/cs/academic/class/15210-s21/www/syllabus.html) needs account.
  - [Prerequisites](http://coursecatalog.web.cmu.edu/schools-colleges/schoolofcomputerscience/undergraduatecomputerscience/#coursestextcontainer)
    - [15-122 imperative programming](https://www.cs.cmu.edu/~15122/about.shtml) no textbook
      Prerequisites
      - [15-112 Fundamentals of Programming and Computer Science](https://www.cs.cmu.edu/~112/) no textbook & Prerequisites
      - [15-151 Mathematical Foundations for Computer Science](https://www.math.cmu.edu/~jmackey/151_128/welcome.html) [no Pre-required](https://csd.cmu.edu/course/15151/s24)
    - 15-150 **functional programming** [no textbook](https://www.cs.cmu.edu/~15150/resources.html)
      Prerequisites 15-151 15-122
- [21-241 Matrix Algebra](https://www.math.cmu.edu/~handron/21_241/info.html)
  I didn't check prerequisite and books because I have learnt linear algebra.
- 15-251 Great Ideas in Theoretical Computer Science [book](https://www.cs.cmu.edu/~15251/course-info.html)
  - 15-122
  - 15-151
### [graduate](https://aco.math.cmu.edu/reqs.html) (Also [see](https://fanpu.io/cmu-online/))
with *no Prerequisites courses* but [just description of knowledge assumed](https://csd.cmu.edu/course/15850/s24).
> algorithms, probability, and linear algebra
> mathematical maturity/curiosity and problem-solving skills are a must
textbook add 3 based on 15-451/651 where 1 is specific and 2 are general (~~TODO~~ "Aho, Hopcroft, and Ullman" book ~~seems to be shared with another course~~ is different from "Hopcroft, Motwani, and Ullman" (JEFFREY D. ULLMAN) in UIUC cs374al1).
- maybe [15-850 (same book as 15750)](https://www.cs.cmu.edu/~15850/policies.html#:~:text=Prerequisites%3A) (*no Textbook*) is better by [FAQs](https://www.cs.cmu.edu/~15750/policies.html)
  451/651 may already contain 50% os 750
  > If you still feel you want to take 15-750, please talk to us first.
- 15750 [book](https://www.cs.cmu.edu/~15750/policies.html)
### [list](https://enr-apps.as.cmu.edu/open/SOC/SOCServlet/search) about "algorithm" in 2024 with "Course Titles and Descriptions".
- [11601](https://www.cs.cmu.edu/~ralf/11-601_F22_Syllabus.pdf) is skipped due to its textbook.more about *interview*
- [95771](https://www.andrew.cmu.edu/user/mm6/95-771/syllabus.html) is skipped due to textbook based on *Java*.
- [04630](https://enr-apps.as.cmu.edu/assets/SOC/ICT_FALL.htm) is skipped due to it is in *Africa*.
- 18667 is skipped because it is more about *Machine Learning*.
- 15495 Topics of Algorithmic Problem Solving seems to be one new course *with no website* (similar for 15795).
- others not in the above curriculum but in the list
  - [15-351](https://www.csd.cs.cmu.edu/15351-algorithms-and-advanced-data-structures) is *skipped* due to (graduate [15650](https://www.cs.cmu.edu/~ckingsf/class/15351-f15/))
    > This course is not open to Computer Science Majors or Minors.
    ~~maybe~~ it is for [~~B.S in Music and Technology~~](https://www.cs.cmu.edu/~music/mat/bachelor-curriculum.html) [CB and STAMACH](https://www.stat.cmu.edu/~hseltman/files/CMUCodes.pdf) as the list course description says.
  - 15859 Randomized Algorithms -> old [15852](https://www.cs.cmu.edu/~avrim/Randalgs97/course_info.html) (TODO prerequisite)
## uc berkeley
- textbook
  Sedgewick, DPV
### graduate [no corresponding good one](https://www.ischool.berkeley.edu/courses/info/231)
- Also [see](https://www2.eecs.berkeley.edu/Courses/CS/)
  - I *skipped* 
    CS C177. Algorithmic *Economics*
    CS 284B. Advanced Computer *Graphics* Algorithms and Techniques 
    because they are too specific.
  - [CS 270. *Combinatorial* Algorithms and Data Structures (*no book*)](https://cs270.org/spring23/syllabus/)
    [Prerequisites](https://www2.eecs.berkeley.edu/Courses/CS270/): COMPSCI 170
  - TODO CS 287H. Algorithmic Human-*Robot* Interaction
### undergraduate [list](https://guide.berkeley.edu/courses/compsci/)
See [map](https://hkn.eecs.berkeley.edu/courseguides) from PKUFlyingPig/Self-learning-Computer-Science
- [cs170 / COMPSCI 170](https://cs170.org/)
  [textbook DPV](https://cs170.org/syllabus/) (This may already contain [*advanced* algorithms](https://buffy.eecs.berkeley.edu/legacy/Anydb/genreport.php?pubinfo=&format=abstract&minihead=&pubid=11179&f_gotparams=1&f_repname=pubs&f_database=pubinfo&f_formid=0) so no one graduate sourse)
  - prerequisite (Also see the above list)
    - [math 1a Calculus](https://math.berkeley.edu/~ogus/Math_1A/index.html) using
      > Single Variable Calculus, by Stewart, (Early Transcendentals for UC Berkeley). We will cover most of chapters 1--6
      cs10 [*online book*](https://cs10.org/bjc-r/llab/html/topic.html?topic=berkeley_bjc%2Fpython%2Fbesides-blocks-oop-joshhug-edition.topic&course&novideo&noreading&noassignment) whic can be skipped probably it is [AP using Snap!](https://bjc.berkeley.edu/)
    - cs61A Structure and Interpretation of Computer Programs
      book which uses [*scip* python customized version](https://cs61a.org/articles/about/#textbook)
      TODO [debugging](https://cs61a.org/articles/debugging/) and [tips](https://cs61a.org/articles/composition/)
      - notice its book may [differ from sicp][reddit_SICP_vs_HtDP] since they use totally different languages (See "why it is discontinued")
      - CS 61B [Data Structures](https://www2.eecs.berkeley.edu/Courses/CS61B/) based on Java
        [book](https://sp24.datastructur.es/policies/#reading) -> Algorithms, 4th Edition by Wayne and *Sedgewick*
    - cs70 [sp21 with *no textbooks*](https://inst.eecs.berkeley.edu/~cs70/archives.html)
- [~~COMPSCI X404.1~~](https://extension.berkeley.edu/search/publicCourseSearchDetails.do?method=load&courseId=31082496)
  [list](https://extension.berkeley.edu/public/category/courseCategoryCertificateProfile.do?method=load&certificateId=21942844#collapse_1)
  - Notice this is extension course which is for those [On-the-job education](https://qr.ae/psczn0)
    > I started searching for a program wherein I *don’t have to sacrifice my day job* and i could get quality education.
    > While some articles challenged extension school’s prestige there were couple that hit the bulls eye.
    It is [accredited](https://en.wikipedia.org/wiki/UC_Berkeley_Extension#:~:text=The%20University%20of%20California%2C%20Berkeley,through%20self%2Dsupporting%20academic%20programs.)
    Also [implied](https://www.reddit.com/r/OMSCS/comments/huyd5z/comment/fyqbimz/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button) by [CPE](https://www.techtarget.com/whatis/definition/CPE-credit)
  Its used books "A Common-Sense Guide to Data Structures and Algorithms" and "Grokking Algorithms: An Illustrated Guide for Programmers and Other Curious People" imply they are not as useful as the above ones.
  - [stanford online](https://online.stanford.edu/), [continuingstudies](https://continuingstudies.stanford.edu/courses/courses-by-category), [summer session](https://summer.stanford.edu/course-list) may be similar
## UIUC due to [Jeff Erikson book](https://jeffe.cs.illinois.edu/teaching/algorithms/#blah)
prerequisite list in [course list](https://cs.illinois.edu/academics/courses)
- Also see "More Algorithms Lecture Notes"
- TODO
  > Nothing will be more blasphemous than writing a textbook that anyone can go out and buy.
- textbook 
  - based on the "Useful Resources" from 374,473
    1. Jeff's Algorithms
    2. DPV
    3. CRLS
  - It also has 2 *Data Structures* book recommendations in Jeff Erikson's link.
  - cs374 course page
    the above 3 plus Kleinberg
  - CS 473 course page
    the above 3 *without CRLS* plus preparata1985 (Computational Geometry) and Raghavan (randomized-algorithms-motwani-and-raghavan.pdf).
### author opinions
- [1](https://news.ycombinator.com/item?id=32131585)
  > My students are almost exclusively juniors and seniors. ...
  - > For getting me through the tests, I did end up using *more traditional* books. However, now, several years past academia, I find this *style* very engaging and delightful to read.
  - > On top of that, 374 only uses about *half* this textbook in conjunction with other notes about topics *not covered in this book* (mostly models of computation). The rest of the material in this textbook is used in 473, the elective advanced algorithms course.
  - > There really needs to be a text that captures the middle ground *between* CLRS and Grokking Algorithms and I guess this *isn’t it.*
### undergraduate
CS [374 Introduction to Algorithms & Models of Computation](https://courses.grainger.illinois.edu/cs374al1/sp2024/) I [choose](https://jeffe.cs.illinois.edu/374-questions.html) [AL1](https://courses.grainger.illinois.edu/CS374AL1/su2024/)
- prerequisite on the course page or [this which only needs "one of"](https://cs.illinois.edu/academics/courses/cs374)
  - [CS173 Discrete Structures](https://courses.engr.illinois.edu/cs173/su2024/ALL-lectures/) [book](https://mfleck.cs.illinois.edu/building-blocks/index-sp2020.html)
    - [goals](https://cs.illinois.edu/academics/courses/cs173) due to "Theory / Math"
      TODO
      > Classify examples the complexity of very simple examples in terms of countable versus uncountable, polynomial versus exponential, decidable versus undecidable
    - [prerequisite](https://courses.engr.illinois.edu/cs173/su2024/ALL-lectures/registration.html)
      - [cs125 Intro to Computer Science](https://cs.illinois.edu/academics/courses/cs125)
        teaches programming, Data structures and basic algorithms
        - [old book](https://math.hws.edu/eck/cs124/downloads/javanotes9-linked.pdf) from [this](https://courses.physics.illinois.edu/cs125/su2017/index.php)
          [new](https://cs.illinois.edu/academics/courses/cs125)
  - [Stuff You Already Know](https://courses.engr.illinois.edu/cs374/sp2019/standards.html) about maths, basic data structures and algorithms.
    - Open *Data Structures* with link list "related projects"
  - CS 225 Introduction to Data Structures and Algorithms with *C++*
    with cpp *reference book* recommendation
    - prerequisite [on the course page](https://courses.engr.illinois.edu/cs225/sp2024/policy/syllabus/) is different from that in the course list (but similar to that in the [course info page](https://cs.illinois.edu/academics/courses/CS225)).
      - [CS 128 Intro to Computer Science II](https://cs128.org/)
        prerequisite CS 125 (see above)
        maybe [*no book*](https://www.reddit.com/r/UIUC/comments/w4tusv/cs128_lectures/)
        - [goal](https://cs.illinois.edu/academics/courses/cs128) *maybe* programming
          > More advanced concepts in computing and techniques and approaches for *solving computational problems*
      - ece220 Computer Systems & Programming
        [textbook](https://courses.grainger.illinois.edu/ece220/sp2024/#textbook) *has been* learnt (briefly due to it is similar to csapp) when learning ostep
        - [Detailed Description and Outline (I only read this)](https://ece.illinois.edu/academics/courses/ece220)
          > Simple data structures such as linked lists and trees
          > Basic sorting algorithms
          > Assembly language programming
          > object-oriented programming
        - [prerequisite](https://courses.illinois.edu/schedule/DEFAULT/DEFAULT/ECE/220) -> [ECE 120 - Introduction to Computing](https://ece.illinois.edu/academics/courses/ece120) (no public course website).
          > understand the connections between hardware and software when developing computing systems
          > Computer organization and machine-level programming
          > Combinational network analysis and design
          objective 
          > recognize that self-motivation and lifelong learning are necessary to success in engineering
          - TODO
            > be able to design and implement *a simple FSM using assembly language*
            > understand the *principles* of computer organization
          - I skipped reading 
            Detailed Description and Outline
- [very useful resourse list Useful Resources](https://courses.engr.illinois.edu/cs374al1/fa2023/resources.html) including textbooks from "see also here"
  - I only read OP in "Tips to thrive in CS 374"
  - [Sariel Har-Peled's *algorithms notes*](https://web.archive.org/web/20091227021139/http://valis.cs.uiuc.edu/~sariel/teach/courses/473/) I directly choose the biggest circle.
  - Algorithm is not a four-letter word (Also [see](https://professor-l.github.io/mazes/))
    my understanding is ["exercise consistently and frequently"](https://www.jamisbuck.org/presentations/rubyconf2011/index.html#slide-10) which is different from [play](https://www.jamisbuck.org/presentations/rubyconf2011/index.html#play).
    We [ought to understand some of the theory](https://www.jamisbuck.org/presentations/rubyconf2011/index.html#chin-up)
    - TODO about maze
      [uniform spanning tree](https://www.jamisbuck.org/presentations/rubyconf2011/index.html#spanning-forest) 
      - [proof](https://www.jamisbuck.org/presentations/rubyconf2011/index.html#aldous-broder-snail) of [Aldous and Broder's method](https://www.jamisbuck.org/presentations/rubyconf2011/index.html#aldous-broder)
      - What does Wilson mean by [feelers](https://www.jamisbuck.org/presentations/rubyconf2011/index.html#wilsons-feelers) and [this](https://www.jamisbuck.org/presentations/rubyconf2011/index.html#wilsons-trailblaze)
        > Except each time around, any point already in the tree is a valid "point B"
      - [non-uniform maze and "Winding corridors, abundant dead-ends, and trivial solutions"](https://www.jamisbuck.org/presentations/rubyconf2011/index.html#bias)
      - how binary tree [works](https://www.jamisbuck.org/presentations/rubyconf2011/index.html#binary-tree-demo) by proof
      - [Sidewinder](https://www.jamisbuck.org/presentations/rubyconf2011/index.html#sidewinder)
    I skipped all algorithms from [Eller's](https://www.jamisbuck.org/presentations/rubyconf2011/index.html#ellers) to [this](https://www.jamisbuck.org/presentations/rubyconf2011/index.html#just-for-grins) because I *didn't care about algorithms for maze*
    - generate new algorithm by [combination](https://www.jamisbuck.org/presentations/rubyconf2011/index.html#the-point)
      implementing them in an [unfamiliar environment](https://www.jamisbuck.org/presentations/rubyconf2011/index.html#exercise-with-algorithms) for [resistance](https://www.jamisbuck.org/presentations/rubyconf2011/index.html#resistance)
  - How to rock an algorithms interview
    - TODO
      Bloom filter
    - key
      > Looking at the corner cases is a good way to bound the complexity and scope of the problem
### [CS 473](https://cs.illinois.edu/academics/courses/cs473) Algorithms which is a bit like [one graduate course](https://publish.illinois.edu/theory-cs/theory-courses/) with [*graduate* hours](https://cs.illinois.edu/academics/courses/CS473)
- [Stuff You *Already* Know](https://courses.engr.illinois.edu/cs473/fa2022/prereqs.html) almost same as the above
- [prerequisite](https://cs.illinois.edu/academics/courses/cs473#:~:text=CS%20473%20%2D%20Algorithms&text=Course%20Information%3A%20Same%20as%20CSE,MATH%20463%20or%20STAT%20400.)
  CS 374
  CS 361 - Prob & Stat for Computer Sci
- Useful Resources again similar to the above except for the last 2 links.
- [link](https://courses.grainger.illinois.edu/cs473/sp2023/)
  Preparata and Shamos's book -> preparata1985.pdf
### prerequisite booklist
- [datastructures](https://donsheehy.github.io/datastructures/fullbook.pdf) by Don Sheehy
- opendatastructures
### [courselist](https://cs.illinois.edu/academics/courses)
- ~~CS 573~~ - Algorithms is *old*
- [CS 554 - Parallel Numerical Algorithms](https://relate.cs.illinois.edu/course/cs554-f23/) ~~is skipped due to its prerequisite~~ (seems no textbooks)
  prerequisite
  [CS 450](https://cs.illinois.edu/academics/courses/cs450) - Numerical Analysis is skipped
- ~~CS 491~~ CAP - Adv Competitive Algorithm Prog recommended by google 
  with *no website*
- CS 574 Randomized Algorithms with [useful book list](https://courses.grainger.illinois.edu/cs574/sp2021/)
  [Mitzenmacher and Upfal 1st old version](https://www.cs.purdue.edu/homes/spa/courses/pg17/mu-book.pdf)
  prerequisite CS374
- [CS 583 Approximation Algorithms with booklist](https://courses.engr.illinois.edu/cs583/fa2021/)
  prerequisite CS 473
# CRLS 4th (2022)
2nd -> 2001
[mit_6_006_2020], [mit_6_006_2011] and [mit_6_006_2005] needs [*A strong understanding*](https://www.reddit.com/r/learnprogramming/comments/1di8dbn/comment/l925w5r/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button) (see 2005) of programming prerequisite.
> You are expected to have taken 6.001 Structure and Interpretation of Computer Programs
> So instead of the *project (a deep understanding* of software) start with your first small task (the basics)

notice to follow the [style](https://github.com/wojtask/clrs4e-solutions/blob/main/CONVENTIONS.md) when writing the solution
- useful quotes
  2020
  > Written course material will be distributed via notes from lectures and recitations. ... though this text is *not required* for the course.
  2011
  > When you are called upon to “give an algorithm,” you must provide (1) a textual description of the algorithm, and, if helpful, pseudocode; (2) at least one worked example or diagram to illustrate how your algorithm works; (3) a proof (or other indication) of the correctness of the algorithm; and (4) an analysis of the time complexity (and, if relevant, the space complexity) of the algorithm.
## programming prerequisite
beginning from [2008](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2008/pages/syllabus/) it uses python. For [mit_6_006_2005] it uses sicp. But by "mit Structure And Interpretation Of Computer Programs site:ocw.mit.edu" mit seems to discontinue teaching sicp since 2005.
- See [this tutorial](https://ocw.mit.edu/courses/6-01sc-introduction-to-electrical-engineering-and-computer-science-i-spring-2011/pages/python-tutorial/)
### sicp
- Hacker News comments
  - [1](https://news.ycombinator.com/item?id=36803119)
    > If you aspire to understand computing systems from first-principles, there's no better resource that SICP.
  - [2](https://news.ycombinator.com/item?id=28280226)
    > For what it’s worth, I disagree with you and I think there are good CS books that* don’t really talk about bits or technical details* of computers (SICP is a famous example).
    - If "Sorry." when visiting this page
      then [that means](https://news.ycombinator.com/item?id=38958700)
      > It turns out my IP was blocked.
  - [3](https://news.ycombinator.com/item?id=1485366)
    - it is not easy to solve all exercises shortly
#### why it is discontinued
Also see "why switch"
- [1](https://www.wisdomandwonder.com/link/2110/why-mit-switched-from-scheme-to-python)
  > He said that the reason that happened was because engineering in 1980 was not what it was in the mid-90s or in 2000.
  scheme
  > had been conceived to teach engineers how to *take small parts* that they understood entirely and use simple techniques to compose them into larger things that do what you want.
  python
  > You have to do basic science on your *libraries* to see how they work, *trying out different inputs* and seeing how the code reacts. This is a fundamentally different job, and it needed a different course.
  > And why Python, then? Well, said Sussman, it probably just had a library *already implemented for the robotics interface*, that was all.
- [2](https://mitadmissions.org/blogs/entry/the_end_of_an_era_1/) which *doesn't* say about the *inherent* reasons
  > It’s an unusual language with a syntax that’s *radically different from most* other programming languages
  [6.02](https://web.mit.edu/6.02/www/currentsemester/index.shtml)
  - Also [see](https://mitadmissions.org/blogs/entry/the_end_of_an_era_1/#comment-31965)
    > The head of our CS department started studying in the early 60’s and he says that the concepts he learned then are the *same* as the ones people need today.
  - DONALDGUY
    > he told me that he thought I was *placing to high an emphasis* on the specific language.
    maybe too high
    > Understanding the principles is *not essential* for an introduction to the subject matter anymore, it matters more that you can develop a *mental map* of systems and make things work for you which is what dealing with the *robots* in 6.01 will make you do.
    [6.01 2008](https://courses.csail.mit.edu/6.01/spring08/resource.html)
    > He sees 6.001 as obsolete. Personally, I wish it was possible to *understand all the principles*, but I guess its simply a reality that I must deal with.
    :)
    > Also, I’d like to say that the simple fact that Professor Sussman didn’t mind taking the time to talk to me really shows how *truly accessible the amazing staff* at MIT are.
  - others
    > And even though languages aren’t supposed to be important, I think learning Python makes up for the loss of Scheme in many ways.
    also see HAWKINS's archive link.
- [3](https://irreal.org/blog/?p=11127)
  - [video](https://www.youtube.com/watch?v=OgRFOjVzvm0) almost same as link 1
    See 2:22, 2:33~3:09, 3:19~4:11, 4:21~37
  - > I’m *less convinced* by his rational for what replaced it. He describes the poking at “batteries included” libraries to figure out what they do as *a sort of science*. To me, it seems more like casting magic spells. ... I think *a lot is lost* with this approach but folks smarter than me—like Sussman—*disagree*.
    > Sussman is clearly a very smart guy but that *doesn't mean he's knowledgeable* about what's best in terms of *education*.
    > None of that changes the fact there's value in SICP and general Computer Science nonetheless.
- [4](https://qr.ae/psSS4I)
  > Count me in the number of those who think it was a *short-sighted decision*. If a university isn’t somewhere to be *challenged* about the way you think and be confronted with the *complex* foundations of subjects you had thought you understood, what is it for?
  - [blog](https://web.archive.org/web/20181229054611/https://cemerick.com/2009/03/24/why-mit-now-uses-python-instead-of-scheme-for-its-undergraduate-cs-program/)
    > This change is something that was widely *panned* when it was announced by many people
    scheme
    > Then, what generaly happened was a programmer would think for a really long time, and then write just a little bit of code, and in practical terms, programming involved *assembling many very small pieces* into a larger whole that had aggregate (did he say ‘emergent’?) behaviour.
    > Building larger programs out of a group of very small, understandable pieces is what things like recursion and functional programming are built for
    today programming
    > it was *impossible* for any one programmer to be *aware of all of the individual pieces*, never mind understand them
    > programming today is all about doing science *on the parts you have to work with*
    scheme disadvantage compared with python (maybe without library)
    > the kinds of problems that we’re trying to solve are much sloppier, and the solutions a lot less discrete than they used to be.
    > Why did they choose python?  Who knows, it’s probably because python has a *good standard library* for interacting with the robot.
    addendum
    > His response was an emphatic ‘no’; in the general case, those core ideas and principles that scheme and SICP have helped to spread for so many years are just *as important as they ever were*.
    So it is fine to continue learning it.
    > However, he did say that starting off with python makes an undergraduate’s initial experiences *maximally productive* in the current environment.
  - comment -> [this](https://jaortega.wordpress.com/2009/03/29/sussmaniana/)
    > I must say, however, that the ideas SICP grew upon, that simple world where you built up complexity out of small pieces and system that you understood *completely*, have much to offer to new generations.
    wingolog
    > you have to build in robustness to the system, in a different way than the one SICP discusses.
- [5](https://qr.ae/psSSHf)
  - one [**useful amazon Customer Review**](https://www.amazon.com/review/R403HR4VL71K8/ref=cm_cr_srp_d_rdp_perm?ie=UTF8) by [Peter Norvig](https://www.norvig.com/)
    > I think it is because SICP is a very personal message that works only if the reader is *at heart* a computer scientist (or willing to become one).
    > The people who *hate* SICP are the ones who *just* want to know how to drive their car on the highway, just like everyone else.
    > rather you're looking for a way of *synthesizing* what you already know, and building a rich framework onto which you can *add new learning* over a career.
    > Some of the reviewers complain that SICP *doesn't teach the basics of OO design*, and so on. In a sense they are right.
    > Rather, the book tells you what those principles are, *how* they came to *be selected* as worthwhile, how they can be implemented *from the ground up*, and how a *different combination* of principles might be more appropriate for some particular problems. This approach requires you to understand the range of possibilities, and to *think about trade-offs* as you go through the design process. ... many projects are started and abandoned because the designers do *not have the flexibility*, experience and understanding to come up with a suitable design and implementation. SICP gives you an approach that will succeed, but it is an approach based on *principles* and wisdom, *not on a checklist*. If you don't understand the principles, or if you are the kind of person who wants to be given a *cookbook* of what to do *rather than* to think *creatively*, or if you only want to work on problems that are pretty much like the problem you worked on last time, then this approach will *not work* for you. There are other approaches that will be more reproducible for a limited range of simple problems, but there is *no better way* than SICP to learn how to address the *truly hard* problems.
    > Now, a big part of the explanation is that the audience is self-selected, and is *not a representative sample*.
    weird this is [not listed in the comments](https://www.amazon.com/Structure-Interpretation-Computer-Programs-Engineering/dp/0262510871/ref=sr_1_1?crid=1TS4ZG1RBUU4E&dib=eyJ2IjoiMSJ9.yvDe9vTEM9IbNsPJnH-SMQRsOaw-1QQ6wrB__8naI73XqwT_VQ07_YdAzJIVPqS3LeodN8mllIAx32Yac5NtftAXWbPK1BBSVqlM7oyvJ0sxOV4TjcDHwE77estvjB_x7ez0UZ22aC5989LAlbD1l_S4W88u596yg0zVQgCtobvUfACoWIBRsDp50dEi8s0BTbx2UQ5-CHkSLNZMZXyfGqkWLzXsuj0sbQ0vuEqvRqo.ufVk-TJ7WiNL6FnzHTPXjejs0WPO-yUuKtS91JfDPTg&dib_tag=se&keywords=Structure+and+Interpretation+of+Computer+Programs&qid=1717230154&s=books&sprefix=structure+and+interpretation+of+computer+programs%2Cstripbooks%2C349&sr=1-1)
  - Also see [paul graham's review](https://www.amazon.com/review/R3G05B1TQ5XGZP/) by [this](https://www.amazon.com/gp/customer-reviews/R243UIFT3VJLYI/ref=cm_cr_dp_d_rvw_ttl?ie=UTF8&ASIN=0262510871)
    > I still don't feel I have learned everything the book has to teach.
    > Yet SICP, which is pretty much the bible of our world, has only three?
    > An optimistic professor somewhere has been feeding SICP to undergrads who are *not ready for it*.
    [related Hacker News](https://news.ycombinator.com/item?id=29929420) doesn't say about the problem set.
- I skipped [this lone comment list](https://news.ycombinator.com/item?id=11628080) because cemerick has given what the author thought.
  I only read the specific reference comment by [this](http://lambda-the-ultimate.org/node/5335#:~:text=So%20in%201997%2C%20they%20walked,what%20engineering%20is%20like%20today.)
  - > You can cover all the set theory and graph theory you need *in a day*. Most people get this in high school. The stuff you need is just not that complicated. You can safely skip category theory.
    crazy "a day"?
    > What you do need is some amount of time spent on the idea that *computer programs* are *mathematical objects* which can be reasoned about mathematically. This is the part that the vast majority of people are *missing nowadays*, and it can be a little tricky to wrap your brain around at first. You need to understand what a fixed point is and why it matters.
    TODO what is "a fixed point"
    > You need automata theory, but again, the basics are really *not that complicated.*
    - TODO
      > You need some programming language theory. You need to know what a binding is, and that there are two types of bindings that matter: *lexical and dynamic*. ...
      environments, RTL, associative maps, dealing with the architectural differences between RAM and non-volatile storage.
    - Why it says "For operating systems, you need to know what a process is ..."
  - blog post (I only read the context of "SICP")
    > they felt that the SICP curriculum *no longer prepared engineers* for what engineering is like today. Sussman said that in the 80s and 90s, engineers built complex systems by *combining simple and well-understood parts*.
    > The “analysis-by-synthesis” view of SICP — where you build a larger system out of smaller, simple parts — *became irrelevant.*
#### useless forum
- [this](https://scsynth.org/t/structure-and-interpretation-of-computer-programs-supercollider-edition/8792) doesn't say something much valuable.
#### why It is still useful (Also see why it is discontinued)
- [1](https://www.reddit.com/r/programming/comments/4hu9e4/comment/d2seb0t/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)
  > If you don't have that understanding, then it becomes an exercise in the *futile art*
- [this](https://www.joelonsoftware.com/2005/12/29/the-perils-of-javaschools-2/)
  referred to in [this](https://softwareengineering.stackexchange.com/a/165247) and many others.
- [uc berkeley review][ucb_sicp_review] **very helpful** showing the **details** why this book is useful
  > Most importantly, it dramatically *raised the bar* for the intellectual content of introductory computer science. Before SICP, the first CS course was almost always entirely filled with learning the *details of some programming language*. SICP is about standing back from the details to *learn big-picture ways* to think about the programming process. It focused attention on the central idea of abstraction -- finding *general patterns* from specific problems and building software tools that embody each pattern. It made heavy use of the idea of *functions as data*, an idea that's hard to learn initially, but immensely powerful once learned. (This is the same idea, in a different form, that makes freshman calculus so notoriously hard even for students who've done well in earlier math classes.) It fit into the first CS course *three different programming paradigms* (functional, object oriented, and declarative), when most other courses didn't even really discuss even one paradigm.
  > To this day, most introductions to computer science use whatever is the *"hot" language* of the moment: from Pascal to C to C++ to Java to Python. Scheme has never been widely used in industry, but it's the perfect language for an *introduction to CS*. For one thing, it has a very *simple*, uniform notation for everything. Other languages have one notation for variable assignment, another notation for conditional execution, two or three more for looping, and yet another for function calls. Courses that teach those languages spend *at least half their time just on learning the notation*. In my SICP-based course at Berkeley, we spend *the first hour* on notation and that's all we need; for the rest of the semester we're learning ideas, *not syntax.*
  > in particular, letting us see *how object oriented programming is implemented*, so OOP languages don't seem like magic to our students. Scheme is a dialect of Lisp, so it's great at handling functions as data, but it's a *stripped-down version* ... It was *very brave* of Abelson and Sussman to teach their introductory course in the best possible language for teaching, paying *no attention to complaints* that all the jobs were in some other language. Once you learned the big ideas, they thought, and this is my experience also, *learning another programming language isn't a big deal*; it's a chore for a weekend. ... Instead we have to give you *the skills you need to learn new languages* as they appear.
  - the book is not easy
    > Finally, SICP was *firmly optimistic* about what a college freshman can be expected to accomplish. SICP students write *interpreters for programming languages*, ordinarily considered more appropriate for *juniors or seniors*. The text itself isn't easy reading; it has none of the sidebars and colored boxes and interesting pictures that typify the modern textbook aimed at students with low attention spans. There are *no redundant exercises*; each exercise teaches an important new idea. It uses big words. But it *repays a close reading; every sentence matters*.
  - maybe not minority as [sicp_computationalculture] says in [reference 11](https://mitp-content-server.mit.edu/books/content/sectbyfn/books_pres_0/6515/sicp.zip/adopt-list.html)
    > Statistically, SICP-based courses have been a small minority. But the book has had an influence beyond that minority.
  - > The use of Scheme as a language for learners has been extended by others over a range *from middle school* to graduate school. ... The idea that computer science *should be about ideas*, not entirely about programming practice, has since widened to include non-technical ideas about the context and social implications of computing.
    > SICP itself has had *a longevity that's very unusual* for introductory CS textbooks. Usually, a book lasts only as long as the language fad to which it is attached. SICP has been going strong for over 25 years and shows *no sign of going out of print.* Computing has changed enormously over that time, from giant mainframe computers to personal computers to the Internet on cell phones. And yet the big ideas behind these changes *remain the same*, and they are *well captured by SICP.*
  - better **read more after reading sicp**
    like courses
    > we've added sections on parallelism, concurrency control, user interface design, and the *client/server paradigm*.
    > We'll find out pretty soon whether the course can survive my own retirement. (Footnote: Nope. Berkeley's new first course for majors uses Python, with lecture notes that try to *keep the ideas (and some of the text)* of SICP.)
  - why switch
    > What MIT decided was to move from a curriculum organized around *topics* (programming paradigms, then circuits, then signal processing, then architecture) to a curriculum organized around applications (let's build and program a robot; let's build and program a cell phone). ... the choice of programming language was *the least of those decisions*.
  - > Perhaps in time the applications-first approach will spark a revolution as profound as the one that followed SICP, but it *hasn't happened yet.*
    > I regularly get visits and emails from long-gone students to tell me about how they're *using in their work* ideas that they thought *were impractical ivory-tower notions as students*. The invention of the *MapReduce* software for data parallelism at Google, based on *functional programming* ideas, has helped eliminate that ivory-tower reputation.
#### comparison with other books
scheme is used [generally for CS books](https://discuss.ocaml.org/t/why-most-books-on-computer-science-use-scheme-and-not-ocaml/11398)
[scheme booklist](https://jaortega.wordpress.com/2007/01/31/a-scheme-bookshelf/) (also [see](https://racket.discourse.group/t/sicp-in-racket-documentation/2037/4))
I will probably read only the top comment in reddit because these users have too different backgrounds.
- [htdp & DCIC (no pdf) & ~~CTMCP~~](https://news.ycombinator.com/item?id=36802579)
  - [htdp How to Design Programs 2018](https://edu.anarcho-copy.org/Programming%20Languages/Racket/How%20to%20design%20program%20se.pdf) (This is [up-to-date for printed version](https://www.amazon.com/How-Design-Programs-Introduction-Programming-dp-0262534800/dp/0262534800/ref=dp_ob_title_bk) but maybe not for [the online version](https://htdp.org/2023-8-14/Book/index.html))
    based on [this][softwareengineering_sicp_vs_HtDP], we seems to be able to safely ignore htdp.
    > it covers much the same ground as SICP, but it only assumes average high-school level domain knowledge
    - But by [reference 4.2 paragraph 1][sicp_htdp_paper] which is almost same as [this](https://www2.ccs.neu.edu/racket/pubs/fdpe2002-fffk.pdf) got from google "htdp vs sicp"
      > *explicitly* how programs should be constructed
      > represent five distinct knowledge levels
      > few, if any, exercises are designed for the sake of domain knowledge
      > more accessible forms of domain knowledge than sicp
      point 1 is  same as [this](https://www.reddit.com/r/Racket/comments/xib8at/comment/ip2r57j/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button) says
  - [DCIC](https://dcic-world.org/2023-02-21/index.html) 
    see why this book is [written][DCIC_author_comment] by one author of htdp and also DCIC who is ["a member of the *core* development group for the Racket programming languages"](https://en.wikipedia.org/wiki/Shriram_Krishnamurthi).
    recommended by [reddit_SICP_vs_HtDP] and as author says
    > increasingly, DCIC
    - [reddit_SICP_vs_HtDP]
      - not use OSSU
      - HtDP is rejected by Georgia Tech same as [this](https://computinged.wordpress.com/2010/05/11/playing-the-cards-youre-dealt-a-story-of-gt-and-htdp/)
        > We moved away from HtDP for two reasons mostly: (1) Some majors (like all of the Colleges of Liberal Arts, Architecture, and Management) were *failing* the course at *higher* than 50% rates. (2) Engineering faculty, particularly, wanted us to teach something that could be used in their classes, and they *weren’t willing to learn Scheme*.
        these reasons can be ignored based on "why It is still useful"
    - [structure](https://spreadsheets-to-programs.github.io/pyret-data-cs1.pdf)
    - [pdf of the 1st version](https://www.davidjoyner.net/b/wp-content/uploads/2017/03/Joyner_IntroductiontoComputing_1stEdition.pdf)
  - [~~Concepts, Techniques, and Models of Computer Programming / CTMCP~~](https://news.ycombinator.com/item?id=36803081)
    *not recommended* by [softwareengineering_sicp_vs_HtDP]
    although it is recommended by [Stewart Mackenzie](https://github.com/sjmackenzie) in [mail_archive_after_sicp_eopl]
- ~~Also try [PAPL (no pdf)](https://papl.cs.brown.edu/2020/) in [Shriram Krishnamurthi page](https://cs.brown.edu/~sk/)~~ (See [this](https://www.reddit.com/r/BrownU/comments/1d67rf1/comment/l6vz9yo/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button) for why I skipped this book)
  > Therefore, this book is no longer maintained (for now)
  > For the material in the first half (programming), go to the DCIC book. That material is *now substantially bigger*, deeper, and richer than in PAPL.
  > For the material in the second half (programming languages), go to the PLAI book (which PAPL grew out of, and which will *eventually incorporate the material that PAPL added*).
- [PLAI Programming Languages: Application and Interpretation](https://www.plai.org/)
  referred to in [this post](https://www.reddit.com/r/Racket/comments/xib8at/comment/ip29d4g/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)
  > The Racket community recognises the value SICP
  at least listed in Shriram Krishnamurthi page
  - referred to by the Racket documentation as [racket_discourse_SICP] says
    > PLAI is designed for *upper-level courses* that introduce the main ideas of programming languages.
    TODO read full of [racket_discourse_SICP]
  - ~~Directly read PAPL~~ (See the above)
    > The second half of PAPL is a further revision of PLAI’s second edition.
    [Also see](https://news.ycombinator.com/item?id=8750689) although it is old.
    > PLAI is *almost completely subsumed* into PAPL. ... The first edition of PLAI tried one way to achieve this synthesis (but didn't really succeed as much as I'd have liked); PAPL *is a fresh attempt* at getting there.
    - Notice here both [shriramkmurthi](https://news.ycombinator.com/item?id=11671745) and [DCIC_author_comment] are Shriram Krishnamurthi's account since Hacker News doesn't restrict the registration which is different from [lobste](https://lobste.rs/about#invitations).
  - recommended by [this](https://cseducators.stackexchange.com/a/7481)
    > If you want to explore the *foundations* of programming languages using a Lisp as a vehicle, then I recommend Programming Languages: Application and Interpretation by Shriram Krishnamurthi.
- [~~How to Design Components~~](https://stackoverflow.com/a/56571940/21294350)
  referred to in [softwareengineering_sicp_vs_HtDP]
  > The material about *imperative* programming has been removed, and is going to be covered in the as-of-yet unwritten second volume *How to Design Components*, but you can take those either from the *first* edition or *from SICP* or both.
  - Also see [DCIC_htdp_comparison]
    > HtDP has a (not formally published) follow-up that teaches program design *in Java*
- ~~EOPL Essentials of Programming Languages~~ (reference of [racket_discourse_SICP]) [influenced][SICP_influence] by SICP (why it is skipped. See below.)
  maybe more [advanced](https://www.reddit.com/r/compsci/comments/lea3qj/comment/gms40tq/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)
- The Little Typer [after SICP and EOPL][mail_archive_after_sicp_eopl]
  > but it covers the subject really well
  - TODO [review](https://nickdrozd.github.io/2019/08/01/little-typer.html)
  [See](https://www.amazon.com/Little-Typer-MIT-Press/dp/0262536439)
  > The first five chapters of The Little Typer provide the needed tools to understand *dependent types*; the remaining chapters use these tools to build a bridge *between mathematics and programming.*
- ~~Coq’Art~~ recommended by [mail_archive_after_sicp_eopl]
  - [review](https://www.reddit.com/r/Coq/comments/p2of9e/comment/h8nvzqo/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)
  - [outline](https://www.amazon.com/Interactive-Theorem-Proving-Program-Development-ebook/dp/B000QCUCZU) So I will skip reading this book now since it is not one necessary prerequisite for the algorithm.
    > This book provides a pragmatic introduction to the *development of proofs and certified programs* using Coq.
- [Software Design for Flexibility](https://groups.csail.mit.edu/mac/users/gjs/6.945/) referred to in [sicp_computationalculture]
  One course with both undergraduate and *graduate* version
  ~~TODO~~ ~~both 6.945 and~~ 6.5150/1 ~~are not listed in [2024 spring](https://student.mit.edu/catalog/archive/spring/m6a.html)~~ are listed as "Officially: Large-scale Symbolic Systems" in course list.
  - prerequisite (I don't have that time to learn all of these courses since my main goal is to learn SICP and it doesn't have prerequisites)
    [old 6.009 Fundamentals of Programming](https://py.mit.edu/spring19) [new](https://py.mit.edu/spring24)
    - This is not targeted for teaching "data structure" by searching 'MIT Fundamentals of Programming data structure'.
    - [6.100A](https://introcomp.mit.edu/spring24)
  - sicp as [the background](https://groups.csail.mit.edu/mac/users/gjs/6.945/overview.pdf)
  - review
    [1](https://www.reddit.com/r/mit/comments/kv031p/comment/giw84j7/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)
    > Most people who take it seem to be interested in functional programming for their graduate research.
    [2](https://wozniak.ca/blog/2022/03/01/1/index.html) I only read the context of "software" up to "The point, then, is that your software should be extensible."
    > *Unless you share the same vision for software* that the authors put forth, the explanations will ring hollow because they *do not match up with the realities* developers are confronted with on a regular basis.
- https://www.composingprograms.com/ from cs61a and [ucb_sicp_review]
  It seems to have [*official* lab solutions](https://cs61a.org/lab/sol-lab09/)
  TODO [to pdf](https://github.com/daxwann/ComposingPrograms-to-PDF)
##### reading order
Notice the following 2~4 are highly related because they are written by almost same people

Read SDF and SICP at the same time as 6.5151 (6.905) does.
- sicp since all other books are [derived from it][SICP_influence].
- Software Design for Flexibility
  This is the last because it may cover some knowledge for the graduate students.
  [code](https://www.reddit.com/r/lisp/comments/mp00sy/comment/gu6tgjo/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)
  - This is like [the expansion of SICP](https://www.reddit.com/r/lisp/comments/mp00sy/comment/gu76il9/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button).
See https://cs.brown.edu/courses/cs019/2023/ (one course using HtDP and DCIC)
- HtDP based on [sicp_htdp_paper]
  [placement exercises](https://cs.brown.edu/courses/cs019/2021/placement-self-test.html)
- DCIC since it has ["a lot algorithmic content" compared with HtDP][DCIC_htdp_comparison] and use python (As "why It is still useful" says language doesn't matter).
  > HtDP is built around a beautiful idea: the data structures shown *grow in complexity in set-theoretic terms.*
  > However, this has a downside. You *have to imagine what the data represent* (this number is an age, that string is a name, that list is of GDPs), but they’re idealized
  > Buut there’s a big catch! A key feature of HtDP is that for every level of datatype, it provides a Design Recipe for programming over that datatype. Lists-of-structs are *complex. So is their programming recipe*.
  > *So* over the past few years, we’ve been working on different program design methods that address the same ends through different means. A lot of our recent education research has been putting new foundations in place. It’s very much work in progress. And DCIC is *the distillation of those efforts*. As we have new results, we’ll be weaving them into DCIC (and probably HtDP too). Stay tuned!
- ~~EOPL probably sharing similar contents as PLAI by their names. Also [see](https://en.wikipedia.org/wiki/Essentials_of_Programming_Languages)~~
  > EOPL has spawned at least two other related texts: Queinnec's[2] Lisp in Small Pieces[3] and Krishnamurthi's Programming Languages: Application and Interpretation.
  > Its first part now *incorporates ideas on programming from HtDP*, another unconventional textbook, which uses Scheme to teach the principles of program design.
  Same as what [ucb_sicp_review] says
  > Like SICP, EOPL represents a significant departure from the prevailing textbook approach in the 1980s.
  - ~~PLAI should [be read first](https://racket.discourse.group/t/which-to-read-first-plai-or-eopl/2087)~~
    As [the author of PLAI says](https://cs.brown.edu/~sk/Publications/Books/ProgLangs/2007-04-26/FAQ/)
    > Otherwise, reading this book is like learning how to build a car *without ever having seen one!*
    > That could almost be *a plug for PLAI.*
    PLAI is based on EOPL, so we can skip EOPL.
- https://www.composingprograms.com/ & sicpjs
- [~~PAPL/~~PLAI](https://www.reddit.com/r/BrownU/comments/1d67rf1/which_of_plai_and_papl_should_i_choose_to_learn/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button) See [this](https://www.reddit.com/r/BrownU/comments/1d67rf1/comment/l6vz9yo/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button) for why PAPL is dropped.
  This needs to be read [after SICP](https://web.archive.org/web/20231130001301/https://conservatory.scheme.org/schemers/Documents/)
- The Little Typer (check whether it is related with sicp. If not, skip it.)
  after already understanding sicp based on the help of related similar books
#### racket
- TODO [mentor help](https://exercism.org/tracks/racket) from [this](https://www.reddit.com/r/Racket/comments/sd3nc9/comment/huckkxb/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)
#### compared with JavaScript version
better read [this diff between these 2 books](https://sicp.sourceacademy.org/chapters/making-of.html) from [sicp_computationalculture]
[course](https://en.wikipedia.org/wiki/Structure_and_Interpretation_of_Computer_Programs#cite_note-8)
- From [amazon](https://www.amazon.com/Structure-Interpretation-Computer-Programs-Engineering/dp/0262543230/ref=pd_lpo_sccl_1/141-2303586-3076928?pd_rd_w=QeIrK&content-id=amzn1.sym.1ad2066f-97d2-4731-9356-36b3edf1ae04&pf_rd_p=1ad2066f-97d2-4731-9356-36b3edf1ae04&pf_rd_r=BGR477QKVA0XXBF7MFG7&pd_rd_wg=z4mEP&pd_rd_r=6ce014d7-3955-43cf-9297-f4c642205e98&pd_rd_i=0262543230&psc=1)
  > Chapter four offers new material, in particular an introduction to the notion of program parsing.
  TODO
  > The evaluator and compiler in chapter five introduce a subtle stack discipline to support return statements (a prominent feature of statement-oriented languages) without sacrificing *tail recursion*.
- Also [see][sicp_computationalculture]
  - HtDP
  - better learn SICP first before SICPJS.
    > JavaScript’s semantics are not so simple. Consequently, SICP’s implementation of a meta-circular evaluator for JavaScript occupies 36 pages of the text (pp. 319-355). For comparison, in the first edition of SICP, the meta-circular evaluator for Scheme took only 20 pages of the textbook to define.
    > Nevertheless, there are *deep connections* between Scheme and JavaScript which makes the JavaScript edition of SICP feasible.
    > was also the editor of the first edition of the standard for JavaScript — called ECMAScript
    > What do Lisp [including the Lisp dialect Scheme] and JavaScript have in common? The ability to abstract a computation … for *later execution as a function*; the ability to embed references to such functions *within data structures*; the ability to invoke functions on arguments; the ability to draw a distinction (conditional execution); a convenient *universal data structure*; completely *automatic storage management* for that data …; a large set of useful functions for operating on that universal data structure; and *standard strategies* for using the universal data structure to represent *more specialized* data structures (xv).
  - > the technology for coping with *large-scale computer systems* merges with the technology for building *new computer languages*, and computer science itself becomes *no more (and no less)* than the discipline of *constructing appropriate descriptive languages*
    > be one that is not idiosyncratic to Abelson and Sussman but *representative of a widely-supported* approach to computing, a language designers’ approach.
    > After the implementation of the meta-circular evaluator in section 4.1, SICP continues like this: “ ... writing an evaluator that *embeds the new language* within an existing high-level language” (360).
    > The first edition of SICP introduced *more than one* approach to time (e.g., the use of lazy evaluation for the implementation of infinite streams), the second and subsequent editions provide an introduction to *multiple* approaches to time
    > principles of programming introduced through the implementation of *a series of programming language interpreters*
    - reasons are same as the above
      > Sussman’s answer was that … they felt that the SICP curriculum no longer prepared engineers for what engineering is like today.
    - > Second, the textbook for 6.945, the 2022 book cited above, by Sussman and Hansen, is essentially SICP taken to the next level. 
      TODO
      > Nevertheless, even if Sussman himself did not make the statement, the statement cited by *McDirmid* is representative of a broad and growing consensus
      > *automation is not the primary purpose* of programming
- [compared with python](https://lobste.rs/s/x1tnlj/new_edition_structure_interpretation#c_cku4t7)
- [wikipedia](https://en.wikipedia.org/wiki/Structure_and_Interpretation_of_Computer_Programs,_JavaScript_Edition#Differences_from_the_original_textbook)
  > Since JavaScript shares its functional core with Scheme ... Chapter four offers new material ... The evaluator and compiler ...
- https://functionalcs.github.io/curriculum/sicp.html
  > the authors have had to make significant changes in chapter 4 because of the limitations of JavaScript.
## 3rd (2009)
- it removes [Binomial Heaps](http://mitp-content-server.mit.edu:18180/books/content/sectbyfn?collid=books_pres_0&id=8030&fn=Chapter%2019.pdf) and [Sorting Networks](http://mitp-content-server.mit.edu:18180/books/content/sectbyfn?collid=books_pres_0&id=8030&fn=Chapter%2027.pdf)
- [No official public](https://qr.ae/psSZmb) Java solution referred to in the transition guide
  but there is one [user-maintained repo](https://github.com/Robertboy18/Theoretical-Algorithms-Implementation) of Python/C++/Java Implementation
## [online resources](https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/)
- Pseudocode and Figures as PDFs is *already contained* in the book
- "Materials Removed from 3e" are ~~*skipped*~~ partly dropped See page xvii
  - I *may* check
    1. implementing pointers and objects
    2. perfect hashing
    3. push-relabel  algorithms  for  maximum  üow
    4. iterative fast Fourier transform method
    5. the details of the simplex algorithm for linear  programming
    6. integer  factorization
- "Khan Academy Course" is *skipped* because they are much incomplete.
- "CLRS code.pdf" is for latex package.
- *TODO
  - ~~I didn't~~ read ["Professor Jokes Explained"](https://mitp-content-server.mit.edu/books/content/sectbyfn/books_pres_0/11599/4e-professor-jokes.html)
  - see [Introduction to Algorithms OpenCourseWare](https://ocw.mit.edu/courses/6-046j-introduction-to-algorithms-sma-5503-fall-2005/) although they are for the 2nd version book
    - see [latest](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) and [this](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/pages/syllabus/) based on mit Computer Science and Engineering (Course 6-3).
  - ~~use "Python Code".~~
    > If you wish to implement any of the algorithms, you should ûnd the transla-tion of our pseudocode into your favorite programming language to be a *fairly straightforward* task. 
  - See 3e to 4e Transition Guide when reading chapters
  - [errata](https://mitp-content-server.mit.edu/books/content/sectbyfn/books_pres_0/11599/e4-bugs.html)
  - > as well as other content, which we may add to
    maybe in the future.
- All solutions [may be impossible for one person to do](https://www.cs.dartmouth.edu/~thc/#solutions)
## preface
- > The chapter notes, bibliography, and index were updated, reüecting  the  dra-matic growth of the ûeld of algorithms since the third edition.
  from 2009 to 2022
- > Those that were reported while we were in full swing preparing this edition were not posted, but were corrected in this edition.
  i.e. in errata TODO
- > Chapter 4 underwent substantial  changes to improve its mathematical founda-tion and make it more robust and intuitive
  TODO how "robust"? and other page xvii~xix list.
## transition-guide
- "Global Changes" point 1~3, 3 New Chapters, Moved Online are said in preface. (Content Changes temporarily is not read)
## 1
- > An incorrect algorithm might not halt at all on some input instances, or it might halt with an incorrect answer.
  corresponds to mcs "6.3 Partial Correctness & Termin"
- [gene relation](https://medlineplus.gov/genetics/understanding/basics/gene/) with DNA.
# The Algorithm Design Manual
[errata](https://www3.cs.stonybrook.edu/~skiena/algorist/book/errata-adm3)
- from [course page](https://www3.cs.stonybrook.edu/~skiena/373/)
  - maybe part 1 is [enough](https://www3.cs.stonybrook.edu/~skiena/373/syllabus.pdf)
    - It is for the undergraduate course
      > There should not be any CS graduate students taking this course, and likely none from any department
  - [hard problem](https://www3.cs.stonybrook.edu/~skiena/373/hard.txt)
  - [notes](https://www.adamconrad.dev/tag/algorithms/)
- [exercise source](https://www.algorist.com/credit.html)
## preface
- TODO
  - How to access "Thomson Reuters Book Citation Index" [1](https://en.wikipedia.org/wiki/Book_Citation_Index#References) [2](https://www.igi-global.com/newsroom/archive/thomson-reuters-indexes-igi-global/1536/)
- > require only black and white, and are under 275 pages, Springer offers the flexibly designed Undergraduate Topics in Computer Science series,
  [see](https://dblp.org/db/series/utcs/index.html) 
  they are not all under 275 like [1](https://sci-hub.se/10.1007/978-3-319-09888-3) [2](https://sci-hub.se/10.1007/978-3-030-39357-1)

[mit_6_006_2020]:https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/pages/syllabus/
[mit_6_006_2011]:https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/pages/syllabus/
[mit_6_006_2005]: https://ocw.mit.edu/courses/6-046j-introduction-to-algorithms-sma-5503-fall-2005/pages/syllabus/

<!-- reddit -->
[reddit_SICP_vs_HtDP]:https://www.reddit.com/r/learnprogramming/comments/13qldro/comment/jlfrov7/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button

[racket_discourse_SICP]:https://racket.discourse.group/t/sicp-in-racket-documentation/2037

<!-- softwareengineering Stack Exchange -->
[softwareengineering_sicp_vs_HtDP]:https://softwareengineering.stackexchange.com/a/165277

[sicp_computationalculture]:http://computationalculture.net/a-matter-of-interpretation-a-review-of-structure-and-interpretation-of-computer-programs-javascript-edition/

[ucb_sicp_review]:https://people.eecs.berkeley.edu/~bh/sicp.html

[SICP_influence]:https://en.wikipedia.org/wiki/Structure_and_Interpretation_of_Computer_Programs#Influence

[sicp_htdp_paper]:https://www2.ccs.neu.edu/racket/pubs/jfp2004-fffk.pdf

[DCIC_htdp_comparison]:https://dcic-world.org/2023-02-21/part_appendix.html#%28part._htdp-vs-dcic%29

[DCIC_author_comment]:https://news.ycombinator.com/item?id=33932462

[mail_archive_after_sicp_eopl]:https://www.mail-archive.com/racket-users@googlegroups.com/msg39234.html