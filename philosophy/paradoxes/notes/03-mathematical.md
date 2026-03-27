# S3: Mathematical Paradoxes

> Mathematics is the domain of certainty. These theorems prove that certainty and intuition are not the same thing.

**Sources:** 7 (Quanta Magazine, Cambridge UP, arXiv, Wikipedia Hilbert/Monty Hall, Harvard Stats 110, Math in the Spotlight)
**Adequacy:** Adequate.

---

## 1. Banach-Tarski (1924)

A solid sphere can be decomposed into finitely many pieces (5 suffice), reassembled via rotations and translations into two identical spheres. Not a physical paradox — the pieces are non-measurable sets, impossible to physically construct. Depends on the Axiom of Choice. Constructivists reject the theorem as a reductio of that axiom. Most mathematicians accept it as a surprising but valid consequence.

Key insight: the sphere contains uncountably many points, and the Axiom of Choice allows selecting from uncountably many non-empty sets simultaneously. The resulting pieces have no well-defined volume.

## 2. Gabriel's Horn (1643)

Torricelli discovered that the surface of revolution of y = 1/x from x = 1 to infinity has infinite surface area but finite volume (pi cubic units). You can fill it with paint but never paint its surface. Resolution: "filling" and "painting" involve different measures. Volume is the integral of pi/x^2, which converges. Surface area involves 2*pi/x * sqrt(1 + 1/x^4), which diverges.

## 3. Hilbert's Hotel (1924)

A hotel with infinitely many rooms, all occupied. A new guest arrives: move each guest from room n to room n+1. Countably many new guests: move each from n to 2n, freeing all odd rooms. Demonstrates that a countably infinite set has the same cardinality as one of its proper subsets — the defining property of Dedekind-infinite sets.

## 4. The Birthday Paradox

In a room of 23 people, there's a >50% chance two share a birthday. At 70 people, it's 99.9%. Counterintuitive because we conflate "any match" with "a match with a specific person." The number of pairs grows quadratically: C(23,2) = 253 pairs, each with a 364/365 chance of NOT matching. 0.9973^253 = 0.4927, so P(match) > 50%.

## 5. Monty Hall (1975/1990)

Three doors, one car, two goats. You pick door 1. Host opens door 3 (goat). Should you switch? Yes: switching wins 2/3 of the time. Your initial pick was right 1/3 of the time; the host's action concentrates the remaining 2/3 probability on the other unopened door.

The 1990 Marilyn vos Savant column provoked thousands of angry letters from PhD mathematicians. Erdos himself was reportedly unconvinced until shown a computer simulation. The key: the host's action is not random; he always reveals a goat, which is informative.

## 6. Simpson's Paradox

A trend in subgroups reverses when combined. Berkeley 1973: overall admissions favored men, but every department favored women (or was neutral). Women applied disproportionately to competitive departments. The paradox is not mathematical but statistical: aggregation across a confounding variable can reverse trends. Practically dangerous in medicine, law, and policy.
