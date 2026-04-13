# C4: Matrix Decompositions — Study Notes

> Decompositions break matrices into structured factors — diagonal, orthogonal, triangular.
> Each factorization reveals a different layer of meaning: geometry of the transformation,
> energy distribution, compressed rank. This chapter synthesizes C2 (linear algebra)
> and C3 (geometry) into the tools that make all of Part II computable.

**Primary source:** MML Ch 4 (pp 98–137, PDF pp 104–143)
**Supplementary:**
- [3Blue1Brown: Eigenvectors and eigenvalues](https://www.youtube.com/watch?v=PFDu9oVAE-g)
- [3Blue1Brown: Singular Value Decomposition](https://www.youtube.com/watch?v=Cx5Z-OslNWE)
- [Gilbert Strang: MIT 18.06 Lecture 21 — Eigenvalues](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/)
- [Interactive SVD demo (explained.ai)](https://explained.ai/matrix-calculus/)

---

## Chapter Structure at a Glance

C4 builds three "lenses" for understanding matrices:

1. **§4.1** — Determinant & Trace: two numbers that summarize a matrix
2. **§4.2** — Eigenvalues & Eigenvectors: special directions a matrix preserves
3. **§4.3** — Cholesky: square root for SPD matrices
4. **§4.4** — Eigendecomposition: factorize via eigenvectors (square matrices only)
5. **§4.5** — SVD ⭐: the universal factorization (any matrix, any shape)
6. **§4.6** — Matrix Approximation: optimal low-rank compression via SVD
7. **§4.7** — Matrix Phylogeny: the family tree of matrix types

The conceptual thread: the SVD (§4.5) is the "fundamental theorem of linear algebra" —
it generalizes and subsumes everything else in the chapter.

---

## Reading Notes

### 4.1 Determinant and Trace

**Determinant = signed volume.** For a matrix A, |det(A)| is the volume of the
parallelepiped formed by its columns. det > 0 means orientation is preserved;
det < 0 means it flips; det = 0 means the matrix collapses a dimension (not invertible).

**Key 2×2 formula:**
```
det([[a, b], [c, d]]) = ad - bc
```

**Properties of det:**
- det(AB) = det(A) det(B)
- det(Aᵀ) = det(A)
- det(A⁻¹) = 1/det(A)
- det(αA) = αⁿ det(A) for A ∈ ℝⁿˣⁿ
- Adding a multiple of one row/column to another does NOT change det
- Swapping two rows changes the sign of det
- Triangular matrix: det = product of diagonal entries

**Laplace expansion (cofactor expansion):** For any row or column j:
```
det(A) = Σₖ (-1)^(k+j) aₖⱼ det(Aₖⱼ)
```
where Aₖⱼ is the (n-1)×(n-1) submatrix obtained by removing row k and column j.
Recursive — reduces n×n det to (n-1)×(n-1) dets.

**Characteristic polynomial:** The polynomial
```
pₐ(λ) = det(A - λI)
```
has degree n, leading coefficient (-1)ⁿ, and the roots are the eigenvalues of A.
The constant term = det(A); the (n-1) coefficient encodes tr(A).

**Trace = sum of diagonals:**
```
tr(A) = Σᵢ aᵢᵢ
```
Properties: tr(A+B) = tr(A)+tr(B); tr(αA) = α tr(A); tr(AB) = tr(BA).
**Cyclic invariance:** tr(ABC) = tr(BCA) = tr(CAB) — order within a cycle doesn't matter.
For vectors: tr(xyᵀ) = yᵀx (scalar). This identity is used constantly in gradient derivations.

**Connection to eigenvalues:**
- det(A) = product of all eigenvalues λ₁···λₙ
- tr(A) = sum of all eigenvalues λ₁+···+λₙ

---

### 4.2 Eigenvalues and Eigenvectors

**The eigenvector equation:**
```
Ax = λx      (x ≠ 0)
```
x is an **eigenvector** of A, λ is the corresponding **eigenvalue**.
Geometric meaning: the transformation A maps x to a scaled version of itself.
The direction of x is preserved (or flipped if λ < 0); only the length changes by λ.

**How to find eigenvalues:**
1. Solve det(A - λI) = 0 → the characteristic polynomial pₐ(λ)
2. The roots λ₁,...,λₙ are the eigenvalues (possibly complex, possibly repeated)

**How to find eigenvectors for eigenvalue λᵢ:**
1. Solve (A - λᵢI)x = 0 (homogeneous system)
2. The solution space = eigenspace Eλᵢ = ker(A - λᵢI)

**Algebraic vs. geometric multiplicity:**
- **Algebraic multiplicity:** how many times λᵢ appears as a root of pₐ
- **Geometric multiplicity:** dim(Eλᵢ) = dim(ker(A - λᵢI))
- Always: geometric ≤ algebraic
- **Defective matrix:** geometric < algebraic for some eigenvalue → cannot diagonalize

**Key properties of eigenvalues:**
- det(A) = λ₁···λₙ (product of all eigenvalues)
- tr(A) = λ₁+···+λₙ (sum)
- If A is invertible, eigenvalues of A⁻¹ are 1/λᵢ
- Eigenvectors for distinct eigenvalues are linearly independent

**Spectral theorem (for symmetric matrices):**
> If A = Aᵀ, then:
> 1. All eigenvalues are real
> 2. Eigenvectors for distinct eigenvalues are orthogonal
> 3. A has an orthonormal basis of eigenvectors (always diagonalizable)

This is why symmetric matrices (and covariance matrices in ML) are so tractable.

**PageRank connection:** Google's PageRank is the eigenvector of the link-matrix A
corresponding to eigenvalue 1. The power method (repeatedly multiply Ax, Ax², ...)
converges to the dominant eigenvector. This is why eigenvalues matter in practice.

---

### 4.3 Cholesky Decomposition

For a **symmetric positive definite (SPD)** matrix A, the Cholesky decomposition is:
```
A = LLᵀ
```
where L is a lower triangular matrix with positive diagonal entries. The decomposition
is unique and always exists for SPD matrices.

**Algorithm:** Compute L column by column:
- lᵢᵢ = √(aᵢᵢ - Σₖ<ᵢ lᵢₖ²)
- lᵢⱼ = (1/lⱼⱼ)(aᵢⱼ - Σₖ<ⱼ lᵢₖlⱼₖ)  for i > j

**Why it matters for ML:**
1. **Solving Ax = b:** factor A = LLᵀ, then solve Ly = b (forward substitution),
   then Lᵀx = y (back substitution). Numerically stable and efficient.
2. **Sampling from a multivariate Gaussian:** if X ~ N(0, Σ), and Σ = LLᵀ,
   then X = Lz where z ~ N(0, I). This is how you draw samples in practice.
3. **Checking SPD:** if Cholesky succeeds, the matrix is SPD.

---

### 4.4 Eigendecomposition and Diagonalization

**Diagonalization:** A square matrix A ∈ ℝⁿˣⁿ is **diagonalizable** if there exists
an invertible P such that:
```
A = P D P⁻¹     ↔     D = P⁻¹ A P
```
where D = diag(λ₁,...,λₙ) and P = [x₁|···|xₙ] (columns = eigenvectors).

**Existence:** A is diagonalizable iff it has n linearly independent eigenvectors
(i.e., it is **non-defective**). Sufficient condition: n distinct eigenvalues.

**For symmetric matrices:** even stronger — P can be chosen to be orthogonal (Pᵀ = P⁻¹):
```
A = P D Pᵀ     (spectral decomposition)
```
Columns of P are orthonormal eigenvectors. This always exists for symmetric A.

**Geometric picture** (from Figure 4.7 in MML):
A = P D P⁻¹ means: (1) P⁻¹ changes basis to the eigenvector coordinate system,
(2) D scales along the eigenvector directions, (3) P changes back to the original basis.
The "natural" coordinate system for A is its eigenvector basis.

**Powers of A:**
```
Aᵏ = P Dᵏ P⁻¹
```
Easy because Dᵏ = diag(λ₁ᵏ,...,λₙᵏ). Used for Markov chains, PageRank, etc.

**Determinant and trace via eigendecomposition:**
```
det(A) = det(P D P⁻¹) = det(P) det(D) det(P⁻¹) = det(D) = λ₁···λₙ
tr(A)  = tr(P D P⁻¹) = tr(D P⁻¹ P) = tr(D) = λ₁+···+λₙ
```
(Cyclic invariance of trace in the middle step.)

---

### 4.5 Singular Value Decomposition (SVD) ⭐

The SVD is the most important decomposition in the book. It exists for **any** matrix
(not just square, not just symmetric) and always has real, non-negative singular values.

**Definition:** For A ∈ ℝᵐˣⁿ:
```
A = U Σ Vᵀ
```
where:
- **U** ∈ ℝᵐˣᵐ: orthogonal matrix (columns = **left singular vectors** u₁,...,uₘ)
- **Σ** ∈ ℝᵐˣⁿ: "diagonal" matrix (entries σ₁ ≥ σ₂ ≥ ··· ≥ 0, **singular values**)
- **V** ∈ ℝⁿˣⁿ: orthogonal matrix (columns = **right singular vectors** v₁,...,vₙ)

**Number of nonzero singular values = rank(A).**

**Geometric picture** (Figure 4.8):
1. Vᵀ: change basis in domain ℝⁿ to the right-singular-vector frame
2. Σ: scale each dimension by σᵢ (some may be 0, squishing those dimensions)
3. U: change basis in codomain ℝᵐ to the left-singular-vector frame

Every linear map = rotate → scale → rotate. The SVD makes this explicit.

**How to construct the SVD:**
- Right singular vectors V = eigenvectors of **AᵀA**
- Left singular vectors U = eigenvectors of **AAᵀ**
- Singular values σᵢ = √(eigenvalues of AᵀA) = √(eigenvalues of AAᵀ)
- AᵀA and AAᵀ have the same nonzero eigenvalues

**Connection to eigendecomposition:**
- For SPD matrices A: SVD = eigendecomposition (U=V=P, Σ=D)
- For symmetric matrices: σᵢ = |λᵢ| (singular values are absolute eigenvalues)
- SVD generalizes eigendecomp to non-square and asymmetric matrices

**Thin/reduced SVD:** Only keep the first r = rank(A) columns of U and V, and the
r×r top-left block of Σ. This is the "compact" form and most software returns it.

---

### 4.6 Matrix Approximation (Truncated SVD / Eckart-Young Theorem)

**Rank-1 decomposition:** Any matrix A of rank r can be written as:
```
A = Σᵢ₌₁ʳ σᵢ uᵢ vᵢᵀ
```
Each term σᵢuᵢvᵢᵀ is a **rank-1 matrix** (outer product of two vectors).
The singular values σᵢ give the "importance" weight of each rank-1 component.

**Low-rank approximation:**
```
Â(k) = Σᵢ₌₁ᵏ σᵢ uᵢ vᵢᵀ    (k ≤ r)
```
This is the best rank-k approximation to A in both spectral and Frobenius norms
(Eckart-Young theorem, 1936). The approximation error is exactly:
```
‖A - Â(k)‖₂ = σₖ₊₁     (spectral norm)
‖A - Â(k)‖_F = √(σₖ₊₁² + ··· + σᵣ²)   (Frobenius norm)
```

**Applications:**
- **Image compression:** Store only the top-k singular vectors/values instead of
  full pixel matrix. Rank-5 often gives visually acceptable results for typical images.
- **Collaborative filtering (recommender systems):** Movie rating matrix A → SVD →
  left singular vectors = "movie concepts", right = "user concepts", σᵢ = importance.
- **PCA (Ch 10):** PCA of centered data = truncated SVD of the data matrix.
- **Pseudoinverse:** A⁺ = V Σ⁺ Uᵀ (Σ⁺ = reciprocals of nonzero singular values).
  Solves Ax = b in the least-squares sense.

---

### 4.7 Matrix Phylogeny

The hierarchy of matrix types (Figure 4.13 in MML):

```
All matrices ℝᵐˣⁿ
  └── Square (m=n)
       ├── Regular (invertible, det≠0)
       │    ├── Symmetric (A=Aᵀ) — real eigenvalues
       │    │    ├── SPD (xᵀAx>0) — positive eigenvalues, Cholesky exists
       │    │    │    └── Diagonal
       │    │    │         └── Identity
       │    └── Orthogonal (AᵀA=I) — det=±1, eigenvalues on unit circle
       └── Singular (det=0)
            ├── Defective — no full eigenvector basis
            └── Non-defective — eigenvectors span ℝⁿ, diagonalizable

SVD exists for ALL matrices (top of tree).
Eigendecomp exists only for square non-defective matrices.
Cholesky only for SPD.
```

---

## Key Formulas Quick Reference

| Concept | Formula | Note |
|---------|---------|------|
| Determinant (2×2) | ad - bc | Signed area of parallelepiped |
| det(AB) | det(A) det(B) | Multiplicative |
| det(Aᵀ) | det(A) | Transpose invariant |
| Eigenvalue equation | Ax = λx | x ≠ 0 |
| Find eigenvalues | det(A - λI) = 0 | Roots of char. polynomial |
| det(A) | λ₁···λₙ | Product of eigenvalues |
| tr(A) | λ₁+···+λₙ | Sum of eigenvalues |
| tr(AB) | tr(BA) | Cyclic invariance |
| Cholesky | A = LLᵀ | SPD only, L lower triangular |
| Eigendecomp | A = PDP⁻¹ | Non-defective square matrices |
| Spectral (symmetric) | A = PDPᵀ | P orthogonal |
| SVD | A = UΣVᵀ | Any A ∈ ℝᵐˣⁿ |
| Singular values | σᵢ = √λᵢ(AᵀA) | Always real, ≥ 0 |
| Low-rank approx | Â(k) = Σᵢ≤ₖ σᵢuᵢvᵢᵀ | Best rank-k (Eckart-Young) |
| Approx error | ‖A-Â(k)‖₂ = σₖ₊₁ | |

---

## Key Connections to Other Chapters

| Concept | Where It Shows Up |
|---------|-------------------|
| Eigendecomposition of Σ | C6 (Gaussian ellipsoids = eigenvectors of covariance matrix) |
| SVD | C10 (PCA = truncated SVD of data matrix X) |
| Eigenvalues of SPD matrix | C3 (inner product with A: ⟨x,y⟩=xᵀAy requires A SPD) |
| Spectral theorem | C10 (maximizing variance → eigenvalue problem) |
| Low-rank approximation | C10 (PCA dimension reduction), C11 (GMM fitting with few components) |
| Cholesky | C6 (sampling from multivariate Gaussian), C9 (numerical stability of regression) |
| Trace of matrix product | C5 (gradient of tr(AB) w.r.t. A = Bᵀ; used in Gaussian MLE) |
| Determinant gradient | C5 (∂ ln det A/∂A = A⁻ᵀ), C6 (MLE for Gaussian covariance) |
| Pseudoinverse | C9 (least-squares: X⁺ = (XᵀX)⁻¹Xᵀ when XᵀX is invertible) |
| Rank of A | C2 (rank = dim of column space = number of nonzero singular values) |

**From C2/C3 feeding in:**
- Basis change (C2 §2.7.2) → eigendecomposition as basis change to eigenvector frame
- Orthogonal matrices (C3 §3.4) → U and V in SVD are orthogonal → preserve distances
- Projections (C3 §3.8) → Gram-Schmidt builds orthonormal columns → constructs U, V

---

## Open Questions

- Why do AᵀA and AAᵀ always have the same nonzero eigenvalues?
  (If Av = σu, then AᵀAv = σAᵀu = σ²v — they share the σ² eigenvalues.)
- When is the pseudoinverse A⁺ = V Σ⁺ Uᵀ the right tool vs. the true inverse?
  (Use A⁺ when A is non-square or rank-deficient; it gives the min-norm least-squares solution.)
- Why does eigendecomposition need square matrices but SVD works for any shape?
  (The eigenvalue equation Ax = λx requires A to map a vector to a scalar multiple of itself,
   impossible if domain and codomain have different dimensions.)
- How does the condition number κ(A) = σ₁/σₙ relate to numerical stability?
  (Large κ means the matrix nearly collapses a direction; solving Ax=b amplifies errors by κ.)
- SVD and PCA: if X is the data matrix (centered), why is PCA = SVD?
  (Covariance matrix Σ = XᵀX/n; its eigenvectors = right singular vectors of X.)
