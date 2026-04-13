# C3: Analytic Geometry — Study Notes

> Geometry on top of algebra. Once you have a vector space, you add structure
> to measure lengths, angles, and distances — and use that structure to project,
> orthogonalize, and rotate.

**Primary source:** MML Ch 3 (pp 71–95)
**Key connection forward:** Everything here — especially projections and orthogonality —
is what makes PCA (Ch 10), linear regression (Ch 9), and SVMs (Ch 12) work.

---

## Reading Notes

### The Chapter's Structure at a Glance

C3 adds geometric structure to C2's algebra in three stages:

1. **Measure length** → norms
2. **Measure angles and distances** → inner products
3. **Use those measurements** → projections, Gram-Schmidt, rotations

---

### 3.1 Norms

A **norm** assigns a length ‖x‖ ≥ 0 to every vector. Three requirements:

| Property | Meaning |
|----------|---------|
| Absolutely homogeneous | ‖λx‖ = \|λ\| ‖x‖ — scaling a vector scales its length |
| Triangle inequality | ‖x + y‖ ≤ ‖x‖ + ‖y‖ — direct path ≤ detour |
| Positive definite | ‖x‖ ≥ 0, and ‖x‖ = 0 iff x = 0 |

Two important norms:

- **Manhattan (L1):** ‖x‖₁ = Σ|xᵢ| — sum of absolute values; "taxi cab" distance
- **Euclidean (L2):** ‖x‖₂ = √(xᵀx) — the usual geometric distance; **default in this book**

The "unit ball" (set of all vectors with norm = 1) looks like a square for L1,
a circle for L2. Different norms give different geometry.

---

### 3.2 Inner Products

An **inner product** ⟨x, y⟩ is a bilinear map V × V → ℝ that is:
- **Symmetric:** ⟨x, y⟩ = ⟨y, x⟩
- **Positive definite:** ⟨x, x⟩ > 0 for x ≠ 0, and ⟨0, 0⟩ = 0

The **dot product** xᵀy = Σᵢ xᵢyᵢ is the standard inner product on ℝⁿ.
(V, ⟨·,·⟩) with the dot product = **Euclidean vector space**.

**General inner products via SPD matrices:**
Any symmetric positive definite (SPD) matrix A defines an inner product:
```
⟨x, y⟩ = xᵀAy
```
A matrix A is SPD if: A = Aᵀ and xᵀAx > 0 for all x ≠ 0.

Example: A₁ = [[9,6],[6,5]] is SPD (xᵀA₁x = (3x₁+2x₂)² + x₂² > 0 always).
A₂ = [[9,6],[6,3]] is NOT (can go negative).

**Why does this matter?** Different inner products give different notions of angle and
distance. The "natural" geometry of your data may not be the standard Euclidean one.
In kernel methods (Ch 12), you work with high-dimensional or even infinite-dimensional
inner products without explicitly knowing the space.

---

### 3.3 Lengths and Distances

**Key link:** Every inner product induces a norm: ‖x‖ = √⟨x, x⟩.
But NOT every norm comes from an inner product (e.g., Manhattan norm does not).

**Cauchy-Schwarz inequality:**
```
|⟨x, y⟩| ≤ ‖x‖ ‖y‖
```
This is what makes the angle formula well-defined (the ratio never exceeds 1).

**Distance (metric):** d(x, y) = ‖x − y‖. A metric satisfies:
- Positive definite: d(x,y) ≥ 0; d(x,y) = 0 iff x = y
- Symmetric: d(x,y) = d(y,x)
- Triangle inequality: d(x,z) ≤ d(x,y) + d(y,z)

Note the duality: inner product is *large* when vectors are similar;
distance is *small* when vectors are similar. Opposite directions.

---

### 3.4 Angles and Orthogonality

**Angle formula** (from Cauchy-Schwarz):
```
cos ω = ⟨x, y⟩ / (‖x‖ ‖y‖)
```

**Orthogonality:** x ⊥ y iff ⟨x, y⟩ = 0.
If additionally ‖x‖ = ‖y‖ = 1, they're **orthonormal**.
The 0-vector is orthogonal to *everything*.

Key point: orthogonality depends on the inner product. Two vectors orthogonal
under the dot product may not be orthogonal under xᵀAy for some other A.

**Orthogonal matrices:** A square matrix A is orthogonal if AAᵀ = I = AᵀA.
- Columns are orthonormal
- A⁻¹ = Aᵀ (inverse = transpose — cheap to compute!)
- Transformations by orthogonal matrices **preserve distances and angles**

The name "orthogonal matrix" is conventional but imprecise —
"orthonormal matrix" would be more accurate.

**Orthonormal basis (ONB):** A basis {b₁,...,bₙ} where:
- ⟨bᵢ, bⱼ⟩ = 0 for i ≠ j (orthogonal)
- ⟨bᵢ, bᵢ⟩ = 1 (unit length)

---

### 3.5–3.6 Orthogonal Complement

The **orthogonal complement** U⊥ of a subspace U is all vectors orthogonal to U:
```
U⊥ = {v ∈ V : ⟨v, u⟩ = 0 for all u ∈ U}
```
- dim(U) + dim(U⊥) = dim(V)
- Every vector in V decomposes uniquely as x = u + u⊥ where u ∈ U, u⊥ ∈ U⊥

**Normal vector:** If U is a plane (2D subspace) in 3D space, U⊥ is 1D —
spanned by a single unit vector w called the **normal vector** of U.
Generalizes to hyperplanes in n dimensions. This is exactly what SVMs use (Ch 12).

---

### 3.7 Inner Product of Functions

Inner products aren't just for finite-dimensional vectors. For functions on [a,b]:
```
⟨u, v⟩ = ∫ₐᵇ u(x)v(x) dx
```
If this integral = 0, the functions are orthogonal. Example: sin(x) ⊥ cos(x) on [-π, π]
because sin(x)cos(x) is odd and integrates to zero.

This leads to **Hilbert spaces** — infinite-dimensional inner product spaces.
Fourier series are essentially projections onto orthogonal function bases.
Not needed for most of this book, but good to know it generalizes this far.

---

### 3.8 Orthogonal Projections ⭐

This is the most important section for ML applications.

**Core idea:** Given a subspace U, the projection πᵤ(x) is the closest point in U to x.
"Closest" means ‖x − πᵤ(x)‖ is minimized.

The displacement vector x − πᵤ(x) must be **orthogonal to U**.

#### Projection onto 1D (a line through origin, spanned by b):

Step by step:
1. Find coordinate: λ = ⟨x, b⟩ / ‖b‖²  = bᵀx / ‖b‖²
2. Projection point: πᵤ(x) = λb = (bᵀx / ‖b‖²) b
3. Projection matrix: **Pπ = bbᵀ / bᵀb**

Note: ‖πᵤ(x)‖ = |cos ω| ‖x‖ (if b is a unit vector). This recovers the
trigonometric projection you know from physics.

#### Projection onto m-dimensional subspace (columns of B = [b₁,...,bₘ]):

1. Orthogonality condition: Bᵀ(x − Bλ) = 0 → normal equations: **BᵀBλ = Bᵀx**
2. Solution: λ = (BᵀB)⁻¹Bᵀx (requires BᵀB invertible, i.e., B has full column rank)
3. Projection point: **πᵤ(x) = B(BᵀB)⁻¹Bᵀx**
4. Projection matrix: **Pπ = B(BᵀB)⁻¹Bᵀ**

Properties of Pπ:
- Pπ² = Pπ (idempotent — projecting twice = projecting once)
- Pπ is symmetric
- Pπx = x for any x already in U (projection is identity on its image)

**The ridge connection:** Adding λI to BᵀB → (BᵀB + λI)⁻¹ improves numerical
stability and positive definiteness. This is exactly ridge regression (Ch 9).

**Projection error** = ‖x − πᵤ(x)‖ = the reconstruction error (also called in Ch 10/PCA).

#### Gram-Schmidt Orthogonalization

Given any basis {b₁,...,bₙ}, construct an ONB {u₁,...,uₙ}:
```
u₁ = b₁
uₖ = bₖ − πspan[u₁,...,uₖ₋₁](bₖ)    for k = 2,...,n
```
Each step: subtract the projection of bₖ onto the already-orthogonalized vectors.
The result is orthogonal; normalize by ‖uₖ‖ to get ONB.

This always works and span{b₁,...,bₙ} = span{u₁,...,uₙ}.

#### Projection onto Affine Subspaces

Affine subspace L = x₀ + U (a "shifted" subspace). To project x onto L:
1. Translate: work with x − x₀ and project onto U (the direction space)
2. πᵤ(x − x₀) = B(BᵀB)⁻¹Bᵀ(x − x₀)
3. Translate back: πₗ(x) = x₀ + πᵤ(x − x₀)

---

### 3.9 Rotations

A rotation is a linear mapping (automorphism of Euclidean space) that rotates a plane
by angle θ about the origin. Positive θ = counterclockwise.

**Rotation in R²:**
```
R(θ) = [[cos θ, -sin θ],
         [sin θ,  cos θ]]
```
Columns = images of the standard basis vectors e₁, e₂.

**Rotations in R³ about each axis:**
```
R₁(θ) = [[1,    0,     0  ],    (rotate in e₂e₃-plane, e₁ fixed)
          [0, cos θ, -sin θ],
          [0, sin θ,  cos θ]]

R₂(θ) = [[cos θ,  0, sin θ],    (rotate in e₁e₃-plane, e₂ fixed)
          [0,      1,    0  ],
          [-sin θ, 0, cos θ]]

R₃(θ) = [[cos θ, -sin θ, 0],    (rotate in e₁e₂-plane, e₃ fixed)
          [sin θ,  cos θ, 0],
          [0,      0,     1]]
```

**Givens rotation in ℝⁿ:** Rᵢⱼ(θ) rotates in the (i,j)-plane, keeps all other
dimensions fixed. A generalization of 2D rotation to any pair of axes.

**Properties of rotations:**
- Preserve distances: ‖x − y‖ = ‖R(x) − R(y)‖
- Preserve angles between vectors
- In 3D+: rotations about different axes do NOT generally commute (order matters!)
- In 2D: rotations always commute (R(α)R(β) = R(β)R(α) = R(α+β))
- Rotation matrices are orthogonal: Rᵀ = R⁻¹

---

## Key Formulas Quick Reference

| Concept | Formula |
|---------|---------|
| Norm from inner product | ‖x‖ = √⟨x,x⟩ |
| Cauchy-Schwarz | \|⟨x,y⟩\| ≤ ‖x‖‖y‖ |
| Angle | cos ω = ⟨x,y⟩ / (‖x‖‖y‖) |
| Orthogonality | ⟨x,y⟩ = 0 |
| Projection (1D) | πᵤ(x) = (bᵀx/bᵀb)b, Pπ = bbᵀ/bᵀb |
| Projection (mD) | πᵤ(x) = B(BᵀB)⁻¹Bᵀx, Pπ = B(BᵀB)⁻¹Bᵀ |
| Gram-Schmidt | u₁=b₁; uₖ=bₖ−Σᵢ<ₖ(uᵢᵀbₖ/‖uᵢ‖²)uᵢ |
| Rotation R2 | [[cos,-sin],[sin,cos]] |

---

## Key Connections to Other Chapters

| Concept | Where It Shows Up |
|---------|-------------------|
| Projections | Ch 9 (linear regression = projection onto column space) |
| Pπ = B(BᵀB)⁻¹Bᵀ | Ch 9 (normal equations), Ch 10 (PCA projection matrix) |
| Gram-Schmidt / ONB | Ch 4 (QR decomposition, orthogonal eigenvectors) |
| Orthogonal complement | Ch 10 (PCA — projection onto principal subspace) |
| Normal vectors | Ch 12 (SVM decision hyperplane defined by normal vector) |
| Cauchy-Schwarz | Ch 6 (covariance and correlation bounds) |
| Rotations (orthogonal maps) | Ch 4 (orthogonal matrices in SVD, eigendecomposition) |
| Inner product of functions | Ch 6 (Gaussian process kernels), Ch 12 (kernel trick) |
| SPD matrices | Ch 4 (all symmetric matrices have real eigenvalues) |

## Open Questions
- How does the choice of inner product (i.e., the matrix A) affect PCA results? (Ch 10)
- What makes BᵀB singular? (when columns of B are linearly dependent — connects to rank from Ch 2)
- In kernel methods, what *is* the implicit inner product? (Ch 12)
