Recently, when I self-learnt Discrete Mathematics and Its Applications 8th by Kenneth Rosen, I did only the even-numbered exercises which the author offers the detailed description instead of the odd ones because the odd ones and the corresponding even ones are very similar. 

I has some questions about exercise 10-supplementary-32. The problem is
> How many nonisomorphic simple connected graphs with five vertices are there
> 
> a) with no vertex of degree more than two?

The answer says:
> If no degree is greater than 2 , then the graph must consist either of the 5-cycle or a walk with no vertices repeated. Therefore there are just two graphs.

Since for paths, it must have degree 2 for interior vertices and degree 1 for end vertices.
Based on the above, maybe we have the following generalized statement for all numbers of vertices $k\ge 3$ "simple connected graphs with no vertex of degree more than two **if and only if** it is one walk connecting all vertices" (Here I dropped $k=2$ because the cycle $C_2$ will cause one multigraph.)

The "if" part is already proved.

For "only if" part, I tried induction (The following uses $n$ as the number of vertices and $G_n$ the corresponding graph).

- Basis step $n=3$: This can be checked by enumeration because only 2 connected graph with $3$ vertices.

- Induction step:

  If $n=k$ holds, then for $n=k+1$. Since graphs is connected, we remove one arbitrary vertex $v$ with degree $m\le 2$ and incident edges and get $H_k=G_{k+1}-\{v\}$. 

  Since $H_k$ is still connected, by *hypothesis* it is one cycle with one edge removed $C_k-\{vw\}$ or $C_{k}$. 
  If $C_k$, then adding one edge it must have one vertex with degree greater than 2.
  If $C_k-\{vw\}$, then we can add one edge or 2 edges to the vertices of degree 1 (degree 0 is impossible because the graph is connected). Both cases imply one "walk connecting all vertices".

Q:

Is the "only if" part right? If right, is the above proof right? If the proof is wrong, could you give one correct proof?