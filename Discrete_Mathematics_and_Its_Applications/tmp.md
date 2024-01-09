One [comment][1] has answered the OP's question. Here I add something related with Manmohan Khandelwal's answer.

---

Here I give one strict proof that $\text{Reflexive closure} \rightarrow \text{Symmetric Closure} \rightarrow \text{Transitivity Closure}$ will must construct relation $T$ which is one equivalence closure [$C(P)$](https://en.wikipedia.org/wiki/Closure_(mathematics)#Closure_operator) of $P$.

1. closure: since each step is one closure operation, $T$ must be one closure of $P$.
2. reflexive: Trivially at each step, it only adds some pairs, so $T$ is reflexive.
3. symmetric: After the Symmetric Closure, we do Transitivity Closure.
  Then $\forall (a,b),(b,c)\in T,(b,a),(c,b)\in T\Rightarrow (a,c),(c,a)\in T$,
  so we must add one set of pairs which always have the symmetric property at the Transitivity Closure step.
  So $T$ is symmetric.
4. transitive: since the last step is the Transitivity Closure, so $T$ is transitive.

Based on the above 4 conditions met, $T\subseteq C(P)$

---

It can be also shown that the above $T$ is the [smallest equivalence relation](https://en.wikipedia.org/wiki/Closure_(mathematics)#Binary_relations) that contains $P$. Here I quote the answer to section 9 supplementary-exercise 24 in Discrete Mathematics and Its Applications 8th by Kenneth Rosen
> Let S be the transitive closure of the symmetric closure of the reflexive closure of R. ... Furthermore, every element added to R to produce S was **forced** to be added in order to **insure** reflexivity, symmetry, or transitivity; therefore S is the smallest equivalence relation containing R

It means that we can remove one element from $T$ to construct one new equivalence closure. Here the closure at each step implies the [smallest](https://en.wikipedia.org/wiki/Reflexive_closure) property.

---

This question has also one similar answer in this [QA](https://math.stackexchange.com/a/566545/1059606)


  [1]: https://math.stackexchange.com/questions/1552485/symmetric-closure-of-the-reflexive-closure-of-the-transitive-closure-of-a-relati/4840776#comment3164656_1552485