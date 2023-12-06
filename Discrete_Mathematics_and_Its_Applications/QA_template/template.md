Recently, when I self-learned Discrete Mathematics and Its Applications 8th by Kenneth Rosen, I did only the even-numbered exercises which the author offers the detailed description than the odd ones because the odd ones and the corresponding even ones are very similar. 

I was stuck at exercise 5-Supplementary-36 which is related with induction. The problem is
> Use mathematical induction to prove that if $x_1, x_2, \ldots , x_n$ are positive real numbers with $n\ge 2$, then $$
(x_1+\frac{1}{x_1})(x_2+\frac{1}{x_2})\cdots(x_n+\frac{1}{x_n})\ge (x_1+\frac{1}{x_2})(x_2+\frac{1}{x_3})\cdots(x_n+\frac{1}{x_{n-1}})(x_1+\frac{1}{x_n})
$$

The answer says
> It will be convenient to clear fractions by multiplying both sides by the product of all the $x_s$’s ; this makes the desired inequality 
$$
(x_1^2 + 1)(x_2^2 + 1)\cdots(x_n^2 + 1) \ge (x_1 x_2 + 1)(x_2 x_3 + 1) ···(x_{n−1}x_n + 1)(x_n x_1 + 1).
$$ ...
> 
> Because of the *cyclic* form of this inequality, we can *without loss of generality* assume that $x_{n+1}$ is the largest (or tied for the largest) of all the given numbers

Q:

However, when I swap between arbitrary $x_i,x_j$ where $1\le i,j\le n$, then $(x_1 x_2 + 1)(x_2 x_3 + 1) ···(x_{n−1}x_n + 1)(x_n x_1 + 1)$ will *change* value. Then how does the above the WLOG(without loss of generality) assumption work? If the assumption has some problems, how to prove the above theorem?