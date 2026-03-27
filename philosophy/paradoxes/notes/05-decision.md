# S5: Decision & Game Theory Paradoxes

> Rationality, it turns out, is not a coherent concept. Or at least it's not the simple concept we thought it was.

**Sources:** 7 (Wikipedia Newcomb/Arrow/St. Petersburg, SEP St. Petersburg, Brilliant, MIRI TDT, Wiris)
**Adequacy:** Adequate.

---

## 1. The Prisoner's Dilemma (1950)

Flood and Dresher (RAND) formalized it; Tucker named it. Two prisoners, each choosing cooperate or defect. Defection dominates (always better individually), but mutual defection is worse than mutual cooperation. Nash equilibrium is suboptimal. Extends to arms races, climate change, tragedy of the commons. Iterated PD allows cooperation (Axelrod's tournaments: tit-for-tat wins).

## 2. Newcomb's Problem (1969)

Nozick published it from physicist William Newcomb. A predictor places $1M in Box B if it predicts you'll take only B; $0 if it predicts you'll take both A+B. Box A always has $1,000. Predictor is 99% accurate.

Two-boxers (causal decision theory): money is already placed; taking both dominates. One-boxers (evidential decision theory): one-boxers almost always get $1M; two-boxers almost always get $1,000. After 50+ years, no consensus. Some argue the problem is genuinely ambiguous — "rationality" means different things in causal vs. evidential frameworks.

## 3. The Trolley Problem (1967)

Philippa Foot's original: divert trolley to kill 1 instead of 5? Most say yes. Thomson's footbridge variant: push a large man off a bridge to stop the trolley? Most say no. Same outcome (1 dies to save 5), different moral intuitions. Reveals that moral reasoning is not purely consequentialist — means matter, not just outcomes. Extensive variants (surgeon, loop, etc.) have mapped the boundaries of moral intuition.

## 4. Arrow's Impossibility Theorem (1951)

No ranked voting system for 3+ candidates can satisfy: (1) non-dictatorship, (2) Pareto efficiency, (3) independence of irrelevant alternatives. This is a mathematical theorem, not an empirical observation. It means perfect ranked voting is provably impossible. Practical implications: all voting systems have known failure modes. The Gibbard-Satterthwaite theorem extends this: all non-trivial voting systems are manipulable.

## 5. The St. Petersburg Paradox (1713)

Flip a coin until heads. Pay 2^n dollars for first heads on flip n. Expected value: 1 + 1 + 1 + ... = infinity. But nobody would pay $1000 to play. Bernoulli's solution: people maximize expected utility, not expected value, and utility has diminishing returns (log utility). Challenges: the paradox can be reconstructed with any unbounded utility function (superSt. Petersburg).

## 6. Braess's Paradox (1968)

Adding a road to a network can increase everyone's travel time. Each driver optimizes individually, but the new route creates congestion patterns that make the whole network worse. Observed in real networks. Seoul removed a highway in 2005 and traffic improved. The paradox extends beyond traffic: adding options to any network with selfish agents can decrease global efficiency.

## 7. The Common Thread

These paradoxes share a theme: individual rationality does not aggregate into collective rationality. The Prisoner's Dilemma shows this for strategic interaction. Arrow shows it for voting. Braess shows it for networks. Newcomb shows that even *individual* rationality may be incoherent, splitting into competing definitions that give opposite answers.
