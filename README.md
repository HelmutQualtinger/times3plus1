This is a playground for playing with the infamous times 3 plus 1 algorithm. Arguably the simples chaotic algorithm known.

Consider the following operation on an arbitrary positive integer:

If the number is even, divide it by two.
If the number is odd, triple it and add one.
In modular arithmetic notation, define the function f as follows:

{\displaystyle f(n)={\begin{cases}{\frac {n}{2}}&{\text{if }}n\equiv 0{\pmod {2}}\\[4px]3n+1&{\text{if }}n\equiv 1{\pmod {2}}.\end{cases}}}{\displaystyle f(n)={\begin{cases}{\frac {n}{2}}&{\text{if }}n\equiv 0{\pmod {2}}\\[4px]3n+1&{\text{if }}n\equiv 1{\pmod {2}}.\end{cases}}}
Now form a sequence by performing this operation repeatedly, beginning with any positive integer, and taking the result at each step as the input at the next.