```python
chapters=[2,3,3,7,4,5,4,4,3,3,5,3,4,5,4,4,3,3,4,5,2,5,3,3,3,3,3,3,3,3,8,5,3,5,5,2,5,5,2]
sum(chapters)/12
Out[11]: 12.416666666666666
```
# course
1. ~~all~~ most of them are based on lectures and use *multiple* textbooks as the reference
2. CS 161 recommend [Tim Roughgarden](https://www.youtube.com/channel/UCcH4Ga14Y4ELFKrEYM1vXCg/playlists)
3. I mainly cares about books and Prerequisites.
4. course list about algorithm rank from high to low based on the numbers of *general* courses (the latter 2 don't have corresponding graduate general courses for algorithm)
  list
  - mit
  - cmu
  - stanford
  - ucb
  summary
  - cmu has 2 specific algorithm courses for graduate but has less general algorithm courses.
    stanford has *no* specific algorithm courses for graduate but has *more* general algorithm courses.
    So their order may exchange.
    mit has all the above 2 advantages while ucb has none.
  - These 4 universities [may be enough](https://www.usnews.com/best-graduate-schools/top-science-schools/computer-science-rankings)
    although [scientist rank](https://research.com/scientists-rankings/computer-science) which is [not h-index](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8238192/) doesn't follow that
    - The best is [unknown](https://careervillage.org/questions/767986/answers/769058)
    - TODO also [see](https://qr.ae/psSRT3)
## stanford
### undergraduate
[CS 161](https://stanford-cs161.github.io/winter2024/resources/#textbook-information)
textbook list shares 3 with cmu 15-451/651 with "Algorithms by Jeff Erikson" -> "Algorithms Illuminated".
- Prerequisites based on order
  - [CS106A Programming Methodology](https://cs106a.stanford.edu/syllabus) with [no prerequisite](https://web.stanford.edu/class/archive/cs/cs106a/cs106a.1216/handouts/coursePlacement.html#) (also [see](https://bulletin.stanford.edu/courses/1056441) which has no "Prerequisite: ...") ([book](https://compedu.stanford.edu/karel-reader/docs/python/en/intro.html)) [->](https://web.stanford.edu/class/cs106b/#prerequisites) [CS106B](https://web.stanford.edu/class/cs106b/#course-resources) [book](https://web.stanford.edu/class/cs106b/index.html#textbook)
  - [cs103 Mathematical Foundations of Computing textbook](https://web.stanford.edu/class/archive/cs/cs103/cs103.1246/syllabus#readings) [Prerequisites](https://web.stanford.edu/class/archive/cs/cs103/cs103.1246/syllabus#prerequisites)
    also uses "Introduction to the Theory of Computation"
  - [cs109](https://chrispiech.github.io/probabilityForComputerScientists/en/examples/mixture_models/) TODO with Machine Learning (Also see [its used Textbook "First Course in Probability"](https://web.stanford.edu/class/cs109/)) [Prerequisites](https://web.stanford.edu/class/cs109/handouts/FAQ.html)
    Math51
### [graduate from stanford *online*](https://online.stanford.edu/courses/cs265-randomized-algorithms-and-probabilistic-analysis) no coursesite
- [2024 course list](https://explorecourses.stanford.edu/print?q=algorithm&descriptions=on&academicYear=&catalog=&page=0&filter-coursestatus-Active=on&collapse=&catalog=)
  [This search about "Algorithm"](https://explorecourses.stanford.edu/print?q=Algorithm&descriptions=on&academicYear=&catalog=&page=0&filter-coursestatus-Active=on&collapse=&catalog=) is weird since it doesn't have [CS 369O: Optimization Algorithms](https://explorecourses.stanford.edu/search?view=catalog&filter-coursestatus-Active=on&page=0&catalog=&q=CS+369O%3A+Optimization+Algorithms&collapse=).
  - I skipped due to they are specific
    1. CS 227A: *Robot* Perception: Hardware, Algorithm, and Application (EE 227)
      EE 227: Robot Perception: Hardware, Algorithm, and Application (CS 227A)
    2. MS&E 238: Computational and Algorithmic Aspects of *Fairness*
    3. CS 354: Topics in *Intractability*: Unfulfilled Algorithmic Fantasies
- [all CS algorithm](https://bulletin.stanford.edu/courses?cq=algorithm&subjectCode=CS&page=2) course list
  - [cs256](https://omereingold.wordpress.com/cs-256-algorithmic-fairness/) ~~no course website~~
    based on CS 161 and [221 Artificial Intelligence](https://stanford-cs221.github.io/spring2024/)
    - cs 154 [(1) Introduction to the Theory of Computation](https://omereingold.wordpress.com/cs-154-introduction-to-automata-and-complexity-theory/) / [(2)](https://explorecourses.stanford.edu/search?view=catalog&filter-coursestatus-Active=on&q=CS%20154:%20Introduction%20to%20Automata%20and%20Complexity%20Theory&academicYear=20182019)
      they may be same due to the same Prerequisites
      uses book "Introduction to the Theory of Computation"
  - [cs368 Algorithmic Techniques for Big Data](https://cs368-stanford.github.io/spring2022/) maybe [no textbook](https://cs368-stanford.github.io/spring2022/lectures.html)
    TODO prerequisite
  - CS207 Antidiscrimination Law and Algorithmic Bias
    CS369O Optimization Algorithms no website
  - CS125 [cancelled](https://law.stanford.edu/courses/data-algorithms-tools-policy-and-society/)
  - I skipped
    - Algorithms for Interactive *Robotics*
    - Topics in *Geometric* Algorithms: Non-Euclidean Methods in Machine Learning
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
      [CS107](https://web.stanford.edu/class/archive/cs/cs107/cs107.1246/syllabus.html#course-overview) -> Prerequisites CS106
      > translating C to/from *assembly*
      > a working understanding of the basics of *computer architecture*
      > understanding *compilers and disassemblers*
## mit
1. check [prerequisite](https://catalog.mit.edu/subjects/6/)
2. graduate course updates are more frequent then undergraduate.
It only uses CRLS for undergraduate courses.
### undergraduate
- [6.1220 Design And Analysis Of Algorithms](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/pages/syllabus/) using CRLS
 - prerequisite
   6.1200[J] Mathematics for Computer Science which I have read its mcs 2018.
   6.1210
- 6.1210 Introduction To Algorithms [using CRLS in 6.006](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/pages/syllabus/)
 - prerequisite
   6.100A Introduction to Computer Science Programming in Python [book](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/pages/readings/)
   6.120A or 6.1200[J]
### gradute 
- [list](https://catalog.mit.edu/degree-charts/master-computer-science-economics-data-science-course-6-14-p/) ([This](https://catalog.mit.edu/degree-charts/master-electrical-engineering-computer-science-course-6-p/) has no definite list)
  Here I *didn't care about prerequisite* because they are for graduate and it seems impossible to learn all required prerequisites by self.
  - 6.5220[J]	Randomized Algorithms -> [6.856J](https://ocw.mit.edu/courses/6-856j-randomized-algorithms-fall-2002/pages/syllabus/) uses the [same book](https://web.archive.org/web/20000622110130/http://www.cup.org/Reviews&blurbs/RanAlg/RanAlg.html) as 15852
  - 6.5250[J]	Distributed Algorithms [book](https://people.csail.mit.edu/ghaffari/DA22/) uses "5.-NancyA.Lynch.DistributedAlgorithms.pdf".
  - 6.7810 -> 6.438 Algorithms For Inference uses "Information Theory, Inference, and Learning Algorithms.pdf".
  - doesn't contain (I skip "Common Ground for Computing Education" because they are too specific) the following in the catalog
    [6.5240 Sublinear Time Algorithms](https://people.csail.mit.edu/ronitt/COURSE/F22/index.html#:~:text=The%20study%20of%20sublinear%20time,applied%20to%20analyzing%20such%20algorithms.) cares about Property Testing
    6.5350 Matrix Multiplication and Graph Algorithms -> [6.890](https://people.csail.mit.edu/virgi/6.890/)
- 6.5210 [book](https://6.5210.csail.mit.edu/info.html)
  prerequisite 6.1220[J] and (6.1200[J] or ...)
  - [lec](https://6.5210.csail.mit.edu/materials.html)
- full [list](https://student.mit.edu/catalog/index.cgi) -> [this catalog](https://catalog.mit.edu/subjects/6/)
  - TODO
    6.5060 Algorithm Engineering [cares too much about papers](https://people.csail.mit.edu/jshun/6506-s23/)
    > For each lecture we will study several research papers; for each paper one student will give a presentation, which will be followed by a discussion.
## [cmu](https://csd.cmu.edu/sites/default/files/2023-08/MSCS%20Handbook%202023-2024.pdf) (from google or [this](https://csd.cmu.edu/academics/masters/ms-in-computer-science))
[B.S. IN COMPUTER SCIENCE CURRICULUM](https://csd.cmu.edu/bs-in-computer-science-curriculum) or [this](http://coursecatalog.web.cmu.edu/schools-colleges/schoolofcomputerscience/undergraduatecomputerscience/#bscurriculumtextcontainer)
[course search (TODO why 15750 can't be searched but it can be searched in enr-apps)](https://csd.cmu.edu/academics/courses)
[TODO](https://csd.cmu.edu/academics/undergraduate/requirements)
> Computer Science Undergraduate curriculum information for prior years is available on the Current Student Resources page.
- *book* recommendation
  it doesn't include skiena manual and Sedgewick Algorithms book
- TODO check [objective](http://coursecatalog.web.cmu.edu/schools-colleges/schoolofcomputerscience/scsconcentrations/#algorithmsandcomplexitytextcontainer)
  > Relating algorithms and/or complexity of computation to a variety of complexity measures such as time, space, *communication, or information* content.
  > The understanding of several advanced algorithms *beyond what is covered* in the core.
  **especially**
  > The ability to understand and apply a variety of advanced algorithmic techniques and proof techniques, such as Lovasz Local Lemma, Johnson Lindenstrauss, Chernoff Bounds, sparsification, expanders, probabilistic method, regret bounds, spectral graph theory, fixed parameter tractability and semi-indefinite programming.
### undergraduate 15-451/651 [book](https://www.cs.cmu.edu/~15451-s24/FAQ.html)
[Prerequisites](http://coursecatalog.web.cmu.edu/schools-colleges/schoolofcomputerscience/undergraduatecomputerscience/#coursestextcontainer)
- TODO [15210](https://www.cs.cmu.edu/~15210/)
  [textbook no use](https://www.diderot.one/courses/44/books/260/chapter/3075) ~~because it is [not intended](https://www.cs.cmu.edu/afs/cs/academic/class/15210-f12/www/lectures/all.pdf)~~
  [old](https://sites.google.com/view/algorithms-book/home) or [this](https://www.cs.cmu.edu/afs/cs/academic/class/15210-s14/www/lectures/)
  [newer in Diderot](https://www.cs.cmu.edu/afs/cs/academic/class/15210-s21/www/syllabus.html) needs account.
  > this course puts an emphasis on parallel thinking
  - [Prerequisites](http://coursecatalog.web.cmu.edu/schools-colleges/schoolofcomputerscience/undergraduatecomputerscience/#coursestextcontainer)
    - [15-122 imperative programming](https://www.cs.cmu.edu/~15122/about.shtml) no textbook
      Prerequisites
      - [15-112 Fundamentals of Programming and Computer Science](https://www.cs.cmu.edu/~112/) no textbook & Prerequisites
      - [15-151](https://www.math.cmu.edu/~jmackey/151_128/welcome.html) [no Pre-required](https://csd.cmu.edu/course/15151/s24)
    - 15-150 **functional programming** [no textbook](https://www.cs.cmu.edu/~15150/resources.html)
      Prerequisites 15-151 15-122
- others not in the curriculum but in the following search list
  - [15-351](https://www.csd.cs.cmu.edu/15351-algorithms-and-advanced-data-structures) is *skipped* due to (graduate [15650](https://www.cs.cmu.edu/~ckingsf/class/15351-f15/))
    > This course is not open to Computer Science Majors or Minors.
    ~~maybe~~ it is for [~~B.S in Music and Technology~~](https://www.cs.cmu.edu/~music/mat/bachelor-curriculum.html) [CB and STAMACH](https://www.stat.cmu.edu/~hseltman/files/CMUCodes.pdf) as the list course description says.
  - 15859 Randomized Algorithms -> old [15852](https://www.cs.cmu.edu/~avrim/Randalgs97/course_info.html) (TODO prerequisite)
### [graduate](https://aco.math.cmu.edu/reqs.html) (Also [see](https://fanpu.io/cmu-online/))
with *no Prerequisites courses* but [just description of knowledge assumed](https://csd.cmu.edu/course/15850/s24).
- maybe [15-850 (same book as 15750)](https://www.cs.cmu.edu/~15850/policies.html#:~:text=Prerequisites%3A) (no Textbook) is better by [FAQs](https://www.cs.cmu.edu/~15750/policies.html)
  451/651 may already contain 50% os 750
  > If you still feel you want to take 15-750, please talk to us first.
- 15750 [book](https://www.cs.cmu.edu/~15750/policies.html)
### [list](https://enr-apps.as.cmu.edu/open/SOC/SOCServlet/search) about "algorithm" in 2024 with "Course Titles and Descriptions".
- [11601](https://www.cs.cmu.edu/~ralf/11-601_F22_Syllabus.pdf) is skipped due to its textbook.more about *interview*
- [95771](https://www.andrew.cmu.edu/user/mm6/95-771/syllabus.html) is skipped due to textbook based on *Java*.
- [04630](https://enr-apps.as.cmu.edu/assets/SOC/ICT_FALL.htm) is skipped due to it is in *Africa*.
- 18667 is skipped because it is more about *Machine Learning*.
- 15495 Topics of Algorithmic Problem Solving seems to be one new course *with no website* (similar for 15795).
## uc berkeley
- textbook
  Sedgewick, DPV
### graduate [no corresponding good one](https://www.ischool.berkeley.edu/courses/info/231)
- Also [see](https://www2.eecs.berkeley.edu/Courses/CS/)
  - I *skipped* CS C177. Algorithmic *Economics*, CS 284B. Advanced Computer *Graphics* Algorithms and Techniques because they are too specific.
  - [CS 270. Combinatorial Algorithms and Data Structures (no book)](https://cs270.org/spring23/syllabus/)
    [Prerequisites](https://www2.eecs.berkeley.edu/Courses/CS270/): COMPSCI 170
  - TODO CS 287H. Algorithmic Human-Robot Interaction
### undergraduate [list](https://guide.berkeley.edu/courses/compsci/)
See [map](https://hkn.eecs.berkeley.edu/courseguides) from PKUFlyingPig/Self-learning-Computer-Science
- [cs170 / COMPSCI 170](https://cs170.org/)
  [textbook DPV](https://cs170.org/syllabus/) (This may already contain [*advanced* algorithms](https://buffy.eecs.berkeley.edu/legacy/Anydb/genreport.php?pubinfo=&format=abstract&minihead=&pubid=11179&f_gotparams=1&f_repname=pubs&f_database=pubinfo&f_formid=0) so no one graduate sourse)
  - prerequisite (Also see the above list)
    - [math 1a](https://math.berkeley.edu/~ogus/Math_1A/index.html) using
      > Single Variable Calculus, by Stewart, (Early Transcendentals for UC Berkeley). We will cover most of chapters 1--6
      cs10 [*online book*](https://cs10.org/bjc-r/llab/html/topic.html?topic=berkeley_bjc%2Fpython%2Fbesides-blocks-oop-joshhug-edition.topic&course&novideo&noreading&noassignment)
    - cs61A
      book which uses [*scip* python customized version](https://cs61a.org/articles/about/#textbook)
      TODO [debugging](https://cs61a.org/articles/debugging/) and [tips](https://cs61a.org/articles/composition/)
      - CS 61B [Data Structures](https://www2.eecs.berkeley.edu/Courses/CS61B/) based on Java
        [book](https://sp24.datastructur.es/policies/#reading) -> Algorithms, 4th Edition by Wayne and *Sedgewick*
    - cs70 [sp21 with *no textbooks*](https://inst.eecs.berkeley.edu/~cs70/archives.html)
- [COMPSCI X404.1](https://extension.berkeley.edu/search/publicCourseSearchDetails.do?method=load&courseId=31082496)
  [list](https://extension.berkeley.edu/public/category/courseCategoryCertificateProfile.do?method=load&certificateId=21942844#collapse_1)
  - Notice this is extension course which is for those [On-the-job education](https://qr.ae/psczn0)
    > I started searching for a program wherein I *don’t have to sacrifice my day job* and i could get quality education.
    > While some articles challenged extension school’s prestige there were couple that hit the bulls eye.
    It is [accredited](https://en.wikipedia.org/wiki/UC_Berkeley_Extension#:~:text=The%20University%20of%20California%2C%20Berkeley,through%20self%2Dsupporting%20academic%20programs.)
    Also [implied](https://www.reddit.com/r/OMSCS/comments/huyd5z/comment/fyqbimz/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button) by [CPE](https://www.techtarget.com/whatis/definition/CPE-credit)
  Its used books "A Common-Sense Guide to Data Structures and Algorithms" and "Grokking Algorithms: An Illustrated Guide for Programmers and Other Curious People" imply they are not as useful as the above ones.
  - [stanford online](https://online.stanford.edu/), [continuingstudies](https://continuingstudies.stanford.edu/courses/courses-by-category), [summer session](https://summer.stanford.edu/course-list) may be similar
# CRLS
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