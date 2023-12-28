Recently, when I self-learnt Discrete Mathematics and Its Applications 8th by Kenneth Rosen, I did only the even-numbered exercises which the author offers the detailed description instead of the odd ones because the odd ones and the corresponding even ones are very similar. 

I has some questions about exercise 8.4-8-g) which is related with the generating function for the recurrence relation. The problem is
> For each of these generating functions, provide a closed
formula for the sequence it determines.
>
> ...
>
> g) $x/(1+x+x^2)$

The answer says
> The key here is to recall the algebraic identity $1 − x^3 = (1 − x)(1 + x + x^2)$. Therefore the given function
can be rewritten as $x(1 − x)/(1 − x^3)$, which can then be split into $x/(1 − x^3)$ plus $−x^2/(1 − x^3)$. From
Table 1 we know that $1/(1 − x^3) = 1 + x^3 + x^6 + x^9 + \cdots$ . Therefore $x/(1 − x^3) = x + x^4 + x^7 + x^{10} + \cdots$ ,
and $-x^2/(1 − x^3) = -x^2 - x^5 - x^8 - x^{11} - \cdots$ . Thus we see that **$a_n$ is 0 when $n$ is a multiple of 3, it is 1
when $n$ is 1 greater than a multiple of 3, and it is −1 when $n$ is 2 greater than a multiple of 3**. One can
check this answer with *Maple*.

I tried first by myself when doing this exercise without reading the answer:
$$
\begin{align*}
      \frac{x}{1+x+x^2}&=x\cdot \sum_{n=0}^{\infty}(-x-x^2)^n\\
      &=x\cdot \sum_{n=0}^{\infty}(-1)^n\cdot x^n\cdot (1+x)^n\\
      &=x\cdot \sum_{n=0}^{\infty}(-1)^n\cdot x^n\cdot \sum_{k=0}^n\binom{n}{k}x^k\\
      &=\sum_{n=0}^{\infty}\sum_{k=0}^n\binom{n}{k}\cdot (-1)^n\cdot x^{n+k+1}\\
    \end{align*}\\
$$
Then
$$
    \begin{align*}
      a_m&=\sum_{\substack{0\le k\le n\\n+k+1=m}}\binom{n}{k}\cdot (-1)^n\\
      &=\sum_{n=\lceil\frac{m-1}{2}\rceil}^{m-1}\binom{n}{m-n-1}(-1)^n
    \end{align*}
$$

I checked some terms for $m=3k$, $a_3=\binom{1}{1}\cdot (-1)+\binom{2}{0}\cdot 1=0$ and $a_6=\binom{5}{0}\cdot (-1)+\binom{4}{1}\cdot (1)+\binom{3}{2}\cdot (-1)=0$. Then it seems that my equation $a_m=\sum_{n=\lceil\frac{m-1}{2}\rceil}^{m-1}\binom{n}{m-n-1}(-1)^n$ is true.

Q:

Then how to prove without using the relation of my try with the book answer?
$$
a_m=\sum_{n=\lceil\frac{m-1}{2}\rceil}^{m-1}\binom{n}{m-n-1}(-1)^n
    =\begin{cases}
      0,m\equiv 0\pmod 3\\
      1,m\equiv 1\pmod 3\\
      -1,m\equiv 2\pmod 3
    \end{cases}
$$