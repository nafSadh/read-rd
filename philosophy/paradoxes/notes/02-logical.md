# S2: Logical Paradoxes

> Russell's letter to Frege destroyed the foundations of mathematics. Godel's theorem showed they could never be fully rebuilt.

**Sources:** 9 (SEP Russell, Wikipedia Russell, SEP Contemporary Logic, IEP Logical Paradoxes, SEP Curry, Wikipedia Grelling-Nelson, Paulson 2024, Tom Rocks Maths, Number Analytics)
**Adequacy:** Strong.

---

## 1. The Liar Paradox

"This sentence is false." If true, it's false. If false, it's true. No consistent truth assignment possible. Attributed to Eubulides (~400 BCE). Simple but devastating: shows that self-reference + negation = contradiction in any language that can talk about its own truth.

## 2. Russell's Paradox (1901)

Consider the set R = {x : x is not a member of x}. Is R a member of R? If yes, then by definition no. If no, then by definition yes. Frege's Grundgesetze allowed unrestricted set comprehension, which permitted R. Russell's letter to Frege (1902) destroyed Frege's life work. Response: Zermelo-Fraenkel set theory restricts set formation; Russell's type theory stratifies language into levels.

## 3. The Foundational Crisis (1900-1930)

Russell + Whitehead spent 10 years on Principia Mathematica (1910-1913), attempting to derive all of mathematics from logic. 362 pages to prove 1+1=2. But Godel (1931) showed any consistent system powerful enough for arithmetic is incomplete (contains true but unprovable statements) and cannot prove its own consistency. Method: construct a formal sentence that says "I am not provable" — a Liar Paradox for formal systems.

## 4. Curry's Paradox

"If this sentence is true, then Santa Claus exists." Formally: if we have a self-referential conditional X where X = (X → Y), we can prove Y for any Y. Unlike the Liar, Curry's doesn't require negation — just a self-referential conditional. This matters because some "solutions" to the Liar restrict negation; Curry shows the problem is deeper.

## 5. Grelling-Nelson Paradox (1908)

"Autological" describes words that describe themselves ("short" is short, "English" is English). "Heterological" describes words that don't describe themselves ("long" is not long). Is "heterological" heterological? If yes, it describes itself, so it's autological. If no, it doesn't describe itself, so it IS heterological. Same structure as Russell's, applied to adjectives.

## 6. Berry's Paradox

"The smallest positive integer not definable in fewer than sixty letters." This sentence defines that number in fewer than sixty letters — contradiction. Reveals that "definability" is a treacherous concept when applied self-referentially.

## 7. The Diagonal Pattern

All these paradoxes share Cantor's diagonal structure: construct an object that differs from every item in a list by differing from the nth item in its nth position. Godel and Turing formalized this pattern, showing it generates fundamental impossibility results, not just puzzles.
