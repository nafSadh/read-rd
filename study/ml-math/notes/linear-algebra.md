# C2: Linear Algebra — Study Notes

> The algebraic backbone of ML. Everything from PCA to neural network training
> traces back to vectors, matrices, and the maps between them.

**Primary source:** MML Ch 2 (pp 23–75)
**Supplementary:**
- [3Blue1Brown: Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
- [MIT 18.06 (Strang)](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/)
- [Immersive Linear Algebra](http://immersivemath.com/ila/)
- [Khan Academy: Linear Algebra](https://www.khanacademy.org/math/linear-algebra)

---

## Reading Notes

### From MML Ch 2

**What IS a vector?** Not just arrows. MML opens with four examples:
1. Geometric vectors (arrows in space)
2. Polynomials (yes, really — add them, scale them, still a polynomial)
3. Audio signals
4. Tuples in R^n (what computers actually use)

Key insight: anything you can add together and scale is a vector. This is the
abstract view that makes linear algebra so powerful — the *same* math works on
all of these.

**Systems of linear equations** — the motivating problem. Given Ax = b:
- No solution (lines don't intersect)
- Exactly one solution (lines cross at a point)
- Infinitely many solutions (lines overlap)

Three outcomes, no fourth option. This is fundamental.

**Matrices** — not just grids of numbers, but:
- Compact notation for systems of linear equations
- Representations of linear mappings (transformations)
- Collections of column vectors

Key operations:
- Addition (elementwise, same dimensions required)
- Multiplication (row-by-column dot products; NOT elementwise!)
  - AB ≠ BA in general (not commutative)
  - (AB)C = A(BC) (associative)
  - Neighboring dimensions must match: (n×k)(k×m) = (n×m)
- Hadamard product = elementwise multiply (common in code, not standard math)

**Inverse A⁻¹:**
- Only for square matrices, and only when det ≠ 0
- For 2×2: A⁻¹ = (1/det) × [swap diag, negate off-diag]
- (AB)⁻¹ = B⁻¹A⁻¹ (note: reversed order!)
- (A+B)⁻¹ ≠ A⁻¹ + B⁻¹ (common trap)

**Transpose A⊤:**
- Flip rows and columns
- (AB)⊤ = B⊤A⊤ (reversed again!)
- Symmetric matrix: A = A⊤ (only square matrices)

**Gaussian elimination** — the workhorse algorithm:
- Elementary transformations: swap rows, scale rows, add rows
- Brings system to row-echelon form (REF) — staircase shape
- Further to reduced REF (RREF) — pivots are 1, only nonzero in column
- Pivot columns = basic variables; non-pivot = free variables
- General solution = particular solution + null space

**The minus-1 trick:** Extend RREF matrix to n×n by adding −1 on diagonal
where pivots are missing. The −1 columns give you the null space basis directly.

**Computing A⁻¹ via Gaussian elimination:**
- Augment [A | I], row-reduce to [I | A⁻¹]
- Same complexity as solving n systems of equations

**Vector spaces** — the formal framework:
- A set V with two operations (+, ·) satisfying closure, associativity,
  distributivity, neutral elements, inverse elements
- Built on *groups*: (G, ⊗) with closure, associativity, neutral element,
  inverse element. Abelian = commutative.
- General linear group GL(n,R) = all invertible n×n matrices under multiplication

**Vector subspaces:**
- A subset U ⊆ V that is itself a vector space (with the same operations)
- Must contain 0, be closed under + and scalar ·
- Solution set of Ax = 0 is always a subspace
- Solution set of Ax = b (b≠0) is NOT a subspace (no zero vector)

**Linear independence:**
- Vectors are linearly dependent if one can be written as a combination of others
- MML's geographic example: Nairobi→Kampala→Kigali uses 2 independent direction
  vectors; the direct Nairobi→Kigali vector is dependent (redundant info)
- Test: write vectors as columns, row-reduce. Non-pivot columns = dependent ones.
- In n dimensions, at most n vectors can be linearly independent

**Basis and rank:**
- Basis = minimal generating set = maximal linearly independent set
- Every vector in the space has a UNIQUE representation as a linear combination
  of basis vectors
- Dimension = number of basis vectors (not the size of the vectors!)
  - span{[0,1]⊤} is 1-dimensional, even though the vector has 2 components
- Standard basis of R³: e₁=[1,0,0], e₂=[0,1,0], e₃=[0,0,1]
- Rank of a matrix = number of linearly independent columns (= rows)
  - rk(A) = rk(A⊤)
  - Full rank: rk(A) = min(m,n) — all columns (or rows) independent

**Linear mappings** — the heart of it:
- Φ: V → W such that Φ(λx + ψy) = λΦ(x) + ψΦ(y)
- Preserves vector space structure (addition and scaling)
- Every linear mapping can be represented as a matrix (and vice versa)
- Special cases:
  - Injective (one-to-one): different inputs → different outputs
  - Surjective (onto): every output is reachable
  - Bijective = both → invertible
  - Isomorphism (bijective linear), endomorphism (V→V), automorphism (V→V bijective)
- Transformation matrix: columns are the images of the basis vectors
  - AΦ = [Φ(b₁) | Φ(b₂) | ... | Φ(bₙ)]

**Image and kernel:**
- Image (range): im(Φ) = {Φ(x) : x ∈ V} — what the mapping can produce
- Kernel (null space): ker(Φ) = {x ∈ V : Φ(x) = 0} — what gets squished to zero
- rk(A) + dim(ker(A)) = n (rank-nullity theorem!)
  - This is HUGE: rank tells you the dimension of the output, kernel tells you
    what info is lost, and they always add up to the input dimension

**Change of basis:**
- Same linear mapping, different matrix representation depending on basis choice
- If B and B' are two bases, the transformation matrix changes via:
  AΦ' = T⁻¹ AΦ S (where S, T are basis change matrices)
- This is why eigendecomposition matters (Ch 4) — find the basis that makes
  the matrix simple

**Affine spaces:**
- Like vector subspaces but shifted away from origin
- L = x₀ + U where U is a subspace and x₀ is the offset
- Important for: hyperplanes, solution sets of Ax = b (b≠0)
- Every affine subspace is the solution of an inhomogeneous linear system

---

### From 3Blue1Brown (Essence of Linear Algebra)

Key geometric intuitions the book doesn't emphasize enough:

- **Vectors as arrows vs. points:** The arrow picture is great for transformation
  intuition; the point picture is better for data (each data point = a vector in R^n)

- **Linear transformations = "grid stays parallel and evenly spaced":**
  3B1B's visual test: if gridlines stay parallel and evenly spaced, it's linear.
  This is more intuitive than checking Φ(λx + ψy) = λΦ(x) + ψΦ(y).

- **Matrix multiplication is composition of transformations:**
  AB means "first apply B, then apply A." Reading right to left, like function
  composition. This explains why AB ≠ BA — rotating then shearing differs
  from shearing then rotating.

- **Determinant = scaling factor of area/volume:**
  det(A) tells you how much the transformation stretches/squishes space.
  det = 0 means the transformation collapses a dimension (not invertible).
  Negative det means orientation flips.

- **Column space = range = what outputs are reachable:**
  The columns of A span the output space. Rank = dimension of column space.

- **Null space = what gets sent to zero:**
  If a 3×3 matrix has rank 2, it squishes 3D space onto a 2D plane.
  The null space (1D line) is what gets flattened.

- **Dot product and duality:** Every 1×n matrix (linear functional) corresponds
  to a vector via the dot product. This duality shows up everywhere in ML.

---

### From MIT 18.06 (Strang)

Strang's "four fundamental subspaces" framework — a beautiful big picture:

For any m×n matrix A:
1. **Column space** C(A) ⊆ R^m — what Ax can produce
2. **Null space** N(A) ⊆ R^n — what Ax = 0
3. **Row space** C(A⊤) ⊆ R^n — span of the rows
4. **Left null space** N(A⊤) ⊆ R^m — what A⊤y = 0

Key relationships:
- C(A) ⊥ N(A⊤) and dim(C(A)) + dim(N(A⊤)) = m
- C(A⊤) ⊥ N(A) and dim(C(A⊤)) + dim(N(A)) = n
- This is the rank-nullity theorem from TWO perspectives

Strang's mantra: "The row space and null space split R^n into two orthogonal
parts." This directly connects to PCA (Ch 10) and least-squares (Ch 9).

---

### From Immersive Linear Algebra

Interactive explorations worth noting:
- Dragging basis vectors in 2D and watching the entire grid deform — visceral
  understanding of linear transformations
- Seeing how changing one basis vector affects the coordinate representation
  of every other point in the space
- The "breakout game" analogy for understanding direction vectors

---

## Key Connections to Later Chapters

| Concept | Where It Shows Up |
|---------|-------------------|
| Matrix multiplication | Ch 5 (Jacobians), Ch 9 (normal equations) |
| Inverse & pseudo-inverse | Ch 9 (linear regression: (A⊤A)⁻¹A⊤b) |
| Rank | Ch 4 (SVD), Ch 10 (PCA low-rank approximation) |
| Null space / kernel | Ch 10 (PCA — what variance is lost) |
| Change of basis | Ch 4 (eigendecomposition), Ch 10 (PCA coordinates) |
| Linear mappings | Ch 5 (vector calculus — derivatives ARE linear maps) |
| Affine spaces | Ch 9 (regression with intercept), Ch 12 (SVM hyperplanes) |

## Open Questions
- How does the choice of basis affect numerical stability? (likely Ch 4)
- When is the pseudo-inverse preferred over the true inverse? (Ch 9)
- How do linear mappings generalize to nonlinear ones? (Ch 5 — via linearization)
