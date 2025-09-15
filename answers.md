  # CMPS 6610 Problem Set 02
## Answers

**Name:** Areen Khalaila


Place all written answers from `assignment-01.md` here for easier grading.

1. **Asymptotic notation**

2. **Algorithm Selection**

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