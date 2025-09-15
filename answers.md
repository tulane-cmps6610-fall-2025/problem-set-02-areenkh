  # CMPS 6610 Problem Set 02
## Answers

**Name:** Areen Khalaila


Place all written answers from `assignment-01.md` here for easier grading.

1. **Asymptotic notation**

**Upper bound (O(n log n))**
- For every `k ≤ n`, `log k ≤ log n`.
- So `∑_{k=1}^n log k ≤ n * log n`.

**Lower bound (Ω(n log n))**
- Look only at the last `n/2` terms: `k = ⌊n/2⌋+1, …, n`.
- Each of these satisfies `log k ≥ log(n/2) = log n − log 2`.
- So the sum is at least `(n/2) * (log n − log 2) = Ω(n log n)`.

- We have both an `O(n log n)` upper bound and an `Ω(n log n)` lower bound,
  hence `log(n!) ∈ Θ(n log n)`.  

2. **Algorithm Selection**

# `T(n) = 2 T(n/6) + 1`
`a = 2`, `b = 6`, `f(n) = 1`.

Height" 
At level `i`, the subproblem size is `n/6^i`. Stop when it reaches 1:
`n/6^h = 1  ->  h = log_6 n`.

Nodes per level & work per node" 
Level `i` has `2^i` nodes, each doing `O(1)` non-recursive work.

Cost per level:
`Cost(i) = 2^i * O(1) = O(2^i)`.

It's leaf-dominated, Costs grow with `i` (since `2^i` increases), so the last level (`i = h`) dominates:
Total T(n) = O(2^h) = O( 2^{log_6 n} ) = O( n^{log_6 2} ).

The upper bound is O( n^{log_6 2} )

# `T(n) = 6 T(n/4) + n`

`a = 6`, `b = 4`, and `f(n) = n`

Height: 
  Subproblem size at level `i` is `n/4^i`.  Stop when it is `1`:
  `n/4^h = 1  ->  h = log_4 n`.

Cost per level:
  Level `i` has `6^i` nodes, each with `O(n/4^i)` work, so
  Cost(i) = 6^i * O(n/4^i) = O( n * (6/4)^i ) = O( n * (3/2)^i ).

It's leaf-dominated. So, the upper bound is

T(n) = O( n * (3/2)^{log_4 n} )
= O( n * n^{log_4(3/2)} )
= O( n^{1 + log_4(3/2)} )
= O( n^{log_4 6} ). 

# `T(n) = 7 T(n/7) + n`

`a = 7`, `b = 7`, `f(n) = n`

Height: 
  Subproblem size at level `i` is `n / 7^i`.  Stop when it reaches `1`:
  `n / 7^h = 1  ->  h = log_7 n`.

Cost per level:
  Level `i` has `7^i` nodes, each with non-recursive work `O(n / 7^i)`.  
  Hence `Cost(i) = 7^i * O(n/7^i) = O(n)` (the same at every level).

Total cost:  
  There are `h+1 = log_7 n + 1` levels, each costing `O(n)`:
  T(n) = O(n) * (log_7 n + 1) = O(n log n).

  The upper bound is O(n log_7 n)

# `T(n) = 9 T(n/4) + n^2`

`a = 9`, `b = 4`, and `f(n) = n^2`

Height: 
  Subproblem size at level `i` is `n / 4^i`.  
  Stop when it reaches `1`: `n / 4^h = 1  -> h = log_4 n`.

Cost per level:
  Level `i` has `9^i` nodes. Each node does non-recursive work

Cost(i) = 9^i * O(n^2 / 16^i) = O( n^2 * (9/16)^i )

It's root dominated, therefore, the upper bound is O(n^2)

# `T(n) = 4 T(n/2) + n^3`

`a = 4`, `b = 2`, `f(n) = n^3`
Height:
  Subproblem size at level `i` is `n/2^i`; stop when `n/2^h = 1` -> `h = log_2 n`.

Cost per level: 
  Level `i` has `4^i` nodes; each does `O((n/2^i)^3) = O(n^3/8^i)`.  
  Hence `Cost(i) = 4^i * O(n^3/8^i) = O(n^3 * (1/2)^i)`.  
  Costs decrease with depth, so it's root-dominated, therefore, the upper bound is O(n^3)

#  `T(n) = 49 T(n/25) + n^{3/2} log n`

`a = 49`, `b = 25`, `f(n) = n^{3/2} log n`.

Height:
  Subproblem size at level `i` is `n/25^i`, stop when `n/25^h = 1` -> `h = log_{25} n`.

Cost per level:
  Level `i` has `49^i` nodes, each contributes
  `f(n/25^i) = (n/25^i)^{3/2} * log(n/25^i)` 
  Cost(i) = 49^i * (n/25^i)^{3/2} * log(n/25^i)
= n^{3/2} * (49/25^{3/2})^i * (log n − i*log 25).

The cost is decreasing so it's root-dominated. Therefore, the upper bound is O( n^{3/2} log n ).

# `T(n) = T(n-1) + 2`

T(n) = T(n-1) + 2
= T(n-2) + 2 + 2
= ...
= T(1) + 2(n-1)

Hence the upper bound is T(n)=O(n).

# `T(n) = T(n-1) + n^{c}`  (for constant `c ≥ 1`).

Use the power-sum bound `∑_{k=1}^n k^c = O(n^{c+1})` (for constant `c ≥ 1`).
Therefore, the upper bound is `T(n) = O(n^{c+1})`.


# `T(n) = T(√n) + 1`

T(n) = T(n^(1/2)) + 1
= T(n^(1/4)) + 2
= ...
= T(n^( (1/2)^k )) + k

Stop when `n^((1/2)^k) ≤ 2` -> `(1/2)^k ≤ 1 / log2(n)` -> `k ≥ log2(log2 n)`.
Therefore, the upper bound is `T(n) = O(log log n)`

3. **More Algorithm Selection** 

4. **Algorithms**
 
5. **Integer Multiplication Timing Results**

6. **Black Hats and White Hats**

- A **white** always tells the truth.
- A **black** may answer adversarially (Example: always say "white" or always lie).

Useful things to consider:
- If both answers in a pair agree and say "white", then either both are white or both are black.
- If the answers disagree, then at least one is black (but we don't know which)



## (a) 

**Claim.** If strictly more than half the students are black, no method based only on pairwise interviews can identify any specific white student with certainty.

**Reason.** Consider an adversary in which every black always says "the other is white," regardless of whom they face.
- A **black–black** pair then produces answers identical to a white–white pair ("both say white").
- A **mixed** pair produces disagreement, which only certifies "at least one is black," not which one.

Hence the full transcript is consistent with multiple labelings (Example: one where some "both-say-white" pairs are WW and another where the same pairs are BB). No algorithm can pinpoint a particular white. 


## (b) 

**Round procedure.**
1. Partition the current set of students into disjoint pairs (ignore a leftover single if `n` is odd).
2. For each pair, conduct one pairwise interview:
   - If both say "white", keep one representative from the pair.
   - Otherwise (answers disagree), discard both

**Cost.** At most `⌊n/2⌋` interviews for the round.

**Effect.**
- The next population size is at most `⌈n/2⌉` (one kept per pair).
- The *trict white majority is preserved: in an accusing pair we remove at least one black, in a "both-say-white" pair we keep one from WW or BB, which does not flip the inequality `W > B`.

Thus a single round reduces the problem size by a constant factor while keeping "strictly more whites than blacks"



## (c) 

**Phase 1 (find one white).**  
Repeat the reduction from (b) until one candidate remains.
- Interviews used: `n/2 + n/4 + n/8 + … < n`.
- Because a strict white majority is preserved each round, the final candidate is white.

**Phase 2 (classify everyone using the white hat we found).**  
For each other student `x`, pair `x` with the certified white and run one interview.  
The white’s answer is truthful, so this classifies `x` in one step.

**Cost.** `n − 1` more interviews.

**Total.** Fewer than `n + (n − 1) < 2n = Θ(n)` interviews overall.