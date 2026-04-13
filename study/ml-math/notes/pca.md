# C10: Dimensionality Reduction with PCA — Study Notes

> PCA asks: given high-dimensional data, what lower-dimensional representation
> loses as little information as possible? The answer is always the same —
> project onto the eigenvectors of the data covariance matrix. This chapter
> shows why that answer is correct from two complementary angles (maximize
> variance; minimize reconstruction error) and how the SVD from C4 makes
> everything computable.

**Primary source:** MML Ch 10 (pp 317–343, PDF pp 323–349)
**Supplementary:**
- [3Blue1Brown: Essence of linear algebra — Eigenvectors](https://www.youtube.com/watch?v=PFDu9oVAE-g)
- [StatQuest: PCA Step-by-Step](https://www.youtube.com/watch?v=FgakZw6K1QQ)
- [Jake VanderPlas: In-Depth PCA (Python Data Science Handbook)](https://jakevdp.github.io/PythonDataScienceHandbook/05.09-principal-component-analysis.html)
- [CS229 Notes on Factor Analysis](https://cs229.stanford.edu/notes2020fall/notes2020fall/fa.pdf)

---

## Chapter Structure at a Glance

C10 develops PCA through four successive perspectives, then extends it:

1. **§10.1** — Problem Formulation: what "dimensionality reduction" means precisely
2. **§10.2** — Maximum Variance Perspective: find directions of greatest spread
3. **§10.3** — Projection Perspective: find directions of smallest reconstruction error
4. **§10.4** — Eigendecomposition of the Covariance Matrix: the standard algorithm
5. **§10.5** — PCA in High Dimensions: when N < D, work with a smaller matrix
6. **§10.6** — PCA as Data Compression: explained variance, scree plots, model selection
7. **§10.7** — Probabilistic PCA: a generative model that subsumes classical PCA

The conceptual thread: §10.2 and §10.3 give two routes to the same answer —
the principal components are the eigenvectors of the data covariance matrix S.
§10.5 shows that the SVD of X is the computationally efficient path to both.

---

## Reading Notes

### 10.1 Problem Formulation

**The setup:**
```
X ∈ ℝᴺˣᴰ     N data points, D features (columns)
xₙ ∈ ℝᴰ      the n-th data point (row n of X)
```

**Centering — always do this first:**
```
μ = (1/N) Σₙ xₙ          (sample mean, a vector in ℝᴰ)
x̃ₙ = xₙ - μ              (centered data point)
```
After centering the data matrix is written X̃ (rows x̃ₙᵀ) with the property
that its columns each have mean zero. All subsequent analysis assumes centered data.

**The goal:** Find a linear subspace U ⊂ ℝᴰ of dimension M < D such that
projecting the data onto U loses as little information as possible. We represent
U by an orthonormal basis B = [b₁ | b₂ | ··· | bₘ] ∈ ℝᴰˣᴹ (bᵢᵀbⱼ = δᵢⱼ).

**What "lose as little information" means** will be made precise in two ways:
- §10.2: maximize the variance of the projected data
- §10.3: minimize the squared reconstruction error

Both give the same answer — this is a theorem, not a coincidence.

**Notation note:** M is the target dimension (number of components to keep),
D is the original dimension, N is the number of data points.

---

### 10.2 Maximum Variance Perspective

**Variance of projections onto direction b:**

For a single unit vector b ∈ ℝᴰ (‖b‖ = 1), the projection of a centered
point x̃ₙ onto b is the scalar zₙ = bᵀx̃ₙ. The variance of these scalars is:
```
Var(z) = (1/N) Σₙ zₙ²
        = (1/N) Σₙ (bᵀx̃ₙ)²
        = bᵀ [ (1/N) Σₙ x̃ₙx̃ₙᵀ ] b
        = bᵀ S b
```
where
```
S = (1/N) X̃ᵀX̃     (D×D data covariance matrix)
```
S is symmetric and positive semidefinite. Its (i,j) entry is the sample
covariance of features i and j.

**Constrained optimization — first principal component:**
```
maximize   bᵀSb
subject to bᵀb = 1
```
Form the Lagrangian:
```
L(b, λ) = bᵀSb - λ(bᵀb - 1)
```
Set the gradient to zero:
```
∂L/∂b = 2Sb - 2λb = 0
    →   Sb = λb
```
So b must be an **eigenvector** of S, and the objective value at the optimum
is bᵀSb = bᵀλb = λ. Maximizing bᵀSb subject to ‖b‖=1 means choosing the
eigenvector with the **largest eigenvalue**.

> **First principal component b₁** = eigenvector of S corresponding to λ₁ (largest eigenvalue).
> The variance captured along b₁ is exactly λ₁.

**Subsequent principal components:**

The m-th principal component bₘ = eigenvector of S corresponding to the m-th
largest eigenvalue λₘ, subject to being orthogonal to b₁,...,bₘ₋₁.
The Lagrangian approach generalizes: the orthogonality constraint is already
satisfied because eigenvectors of a symmetric matrix for distinct eigenvalues
are orthogonal (spectral theorem, C4 §4.2).

**Total variance — a key identity:**
```
tr(S) = λ₁ + λ₂ + ··· + λ_D = total variance of the data
```
This is because tr(S) = sum of diagonal entries = sum of individual feature
variances, and also equals the sum of all eigenvalues (C4 §4.1). Keeping the
top M components captures variance λ₁+···+λ_M out of a total of tr(S).

---

### 10.3 Projection Perspective

**Projection of a point onto the subspace spanned by B = [b₁|···|bₘ]:**

The coordinates of x̃ₙ in the reduced space are:
```
zₙ = Bᵀx̃ₙ ∈ ℝᴹ          (projection coefficients / "scores")
```
The reconstruction (back in ℝᴰ) is:
```
x̃̂ₙ = Bzₙ = BBᵀx̃ₙ ∈ ℝᴰ
```
BBᵀ is the orthogonal projection matrix onto the column space of B.

**Reconstruction error (average squared):**
```
J = (1/N) Σₙ ‖x̃ₙ - x̃̂ₙ‖²
  = (1/N) Σₙ ‖x̃ₙ - BBᵀx̃ₙ‖²
```

**Minimizing J gives the same eigenvectors:**

After algebraic manipulation (using the constraint BᵀB = I and the spectral
decomposition of S), the reconstruction error can be written as:
```
J = Σᵢ₌ₘ₊₁ᴰ λᵢ
  = tr(S) - Σᵢ₌₁ᴹ λᵢ
```
This is exactly the sum of the **discarded** eigenvalues. Minimizing J means
maximizing the sum of kept eigenvalues λ₁+···+λ_M — the same problem as §10.2.

**Equivalence theorem:** The projection that minimizes reconstruction error
is the same as the projection that maximizes captured variance. Both solutions
are the top-M eigenvectors of S.

**Intuition:** The eigenvalue λᵢ measures how much variance the data has in
direction bᵢ. Variance = spread = information. Discarding a direction with
eigenvalue λᵢ loses exactly λᵢ worth of variance (reconstruction error term).
Keeping the large-λ directions and discarding the small-λ directions is
simultaneously maximum-variance and minimum-error.

---

### 10.4 Eigenvalue Decomposition of the Data Covariance Matrix

**The covariance matrix S:**
```
S = (1/N) X̃ᵀX̃     ∈ ℝᴰˣᴰ
```
S is symmetric positive semidefinite (SPD if the data has full rank D in ℝᴰ,
positive semidefinite in general). By the spectral theorem (C4 §4.2):
```
S = U Λ Uᵀ
```
where:
- **U** = [u₁ | u₂ | ··· | u_D] ∈ ℝᴰˣᴰ: orthogonal matrix of eigenvectors
- **Λ** = diag(λ₁, λ₂, ..., λ_D): diagonal matrix of eigenvalues, λ₁ ≥ λ₂ ≥ ··· ≥ λ_D ≥ 0

**Principal components** = columns of U = eigenvectors of S.

**The PCA algorithm (eigendecomp route):**
```
1. Center the data:   X̃ = X - 1μᵀ    (subtract mean from each row)
2. Compute covariance:  S = (1/N) X̃ᵀX̃
3. Eigen-decompose:     S = UΛUᵀ
4. Choose top M:        U_M = U[:, 1:M]   (D×M matrix)
5. Project:             Z = X̃ U_M         (N×M score matrix)
6. Reconstruct:         X̃̂ = Z U_Mᵀ       (N×D matrix)
```

**Score matrix Z = X̃U_M:**
- Row n of Z = coordinates of data point n in the new M-dimensional space
- Z has shape N×M; each column is one "principal component score"
- The scores for different principal components are uncorrelated (by construction)

**Why scores are uncorrelated:**
```
Cov(Z) = (1/N) Zᵀ Z
        = (1/N) (X̃U_M)ᵀ(X̃U_M)
        = U_Mᵀ S U_M
        = U_Mᵀ (UΛUᵀ) U_M
        = Λ_M         (M×M diagonal, eigenvalues λ₁,...,λ_M)
```
The covariance of the projected scores is diagonal — PCA decorrelates the data.

---

### 10.5 PCA in High Dimensions

**The problem when N < D:**

When the number of data points N is smaller than the dimension D (e.g.,
N=100 medical patients, D=20000 gene expression features), computing and
storing S ∈ ℝᴰˣᴰ is infeasible. (S would be 20000×20000.)

**The key insight:**

Instead, compute the N×N matrix:
```
C = (1/N) X̃X̃ᵀ     ∈ ℝᴺˣᴺ
```
C and S share the same nonzero eigenvalues (same argument as AᵀA and AAᵀ
having the same nonzero eigenvalues — see C4 §4.5).

**Recovering principal components from eigenvectors of C:**

If Cv = λv (v ∈ ℝᴺ, ‖v‖=1) with λ ≠ 0, then:
```
(1/N) X̃X̃ᵀ v = λv
  →  (1/N) X̃ᵀX̃ (X̃ᵀv) = λ (X̃ᵀv)
  →  S (X̃ᵀv) = λ (X̃ᵀv)
```
So u = X̃ᵀv / ‖X̃ᵀv‖ is the corresponding eigenvector of S.
Normalizing: since ‖X̃ᵀv‖ = √(Nλ):
```
u = (1/√(Nλ)) X̃ᵀv
```

**Connection to SVD — the elegant unified view:**

Apply SVD to the centered data matrix:
```
X̃ = U Σ Vᵀ
```
where U ∈ ℝᴺˣᴺ, Σ ∈ ℝᴺˣᴰ (diagonal, σ₁ ≥ σ₂ ≥ ···), V ∈ ℝᴰˣᴰ.

Then:
```
S = (1/N) X̃ᵀX̃ = (1/N) V Σᵀ Uᵀ U Σ Vᵀ = V (Σᵀ Σ/N) Vᵀ
```
The columns of **V** are the eigenvectors of S (the principal components),
and the singular values relate to eigenvalues by:
```
λᵢ = σᵢ²/N
```

**Summary of the three equivalent views:**

| Approach | Matrix computed | Eigenvectors / output |
|----------|----------------|----------------------|
| Standard (D ≤ N) | S = X̃ᵀX̃/N ∈ ℝᴰˣᴰ | U = principal components |
| High-dim (N < D) | C = X̃X̃ᵀ/N ∈ ℝᴺˣᴺ | V via X̃ᵀv/‖X̃ᵀv‖ |
| SVD (always) | SVD of X̃ ∈ ℝᴺˣᴰ | Vᵀ = principal components |

The SVD route is the most general and numerically preferred in practice.

---

### 10.6 PCA as Data Compression / Reconstruction

**Explained variance ratio:**

The fraction of total variance captured by the first M components:
```
explained variance ratio (M) = (λ₁ + λ₂ + ··· + λ_M) / (λ₁ + λ₂ + ··· + λ_D)
                              = (σ₁² + ··· + σ_M²) / Σᵢ σᵢ²
```
(Using σᵢ² = Nλᵢ, the N cancels, and Frobenius norm ‖X̃‖_F² = Σᵢ σᵢ².)

**Choosing M — the scree plot:**

Plot eigenvalues λ₁ ≥ λ₂ ≥ ··· ≥ λ_D. Look for:
- The "elbow": the point where the curve flattens out
- A threshold: keep enough components to explain e.g. 95% of total variance

```
[Example scree plot shape]
λᵢ
|*
|  *
|    *
|      * *
|           * * * * * * *
+--------------------------> i
     ^
     elbow: keep components to the left
```

**Compression perspective:**

Original data: N × D floats. After PCA to M components:
- Store: principal components U_M (D×M) + scores Z (N×M) + mean μ (D)
- Total: D·M + N·M + D floats instead of N·D
- Compression ratio: N·D / (M·(N+D) + D)

When N and D are both large and M is small, this is a significant saving.

**Reconstruction quality:**
```
‖X̃ - X̃̂‖_F² = Σᵢ₌ₘ₊₁ᴰ σᵢ²   (sum of discarded squared singular values)
```
This is the exact formula for the Frobenius norm of the reconstruction error —
the same quantity appears in the Eckart-Young theorem (C4 §4.6).

**Practical note on centering and scaling:**

- Always center (subtract mean). Without centering, the first PC often just
  points toward the data centroid rather than capturing variance structure.
- Optionally standardize (divide each feature by its standard deviation)
  before computing S. This gives the PCA on the correlation matrix instead
  of the covariance matrix. Use standardization when features have very
  different scales or units.

---

### 10.7 Probabilistic PCA

**Motivation:** Classical PCA is a computational recipe. Probabilistic PCA
(PPCA) provides a generative model, enabling:
- Missing data handling (impute via the posterior)
- Proper likelihood for model comparison (how many components M?)
- A bridge to Bayesian methods and variational autoencoders

**Latent variable model:**
```
z ~ N(0, Iₘ)                   (latent code, M-dimensional)
x | z ~ N(Wz + μ, σ²I_D)       (observed data, D-dimensional)
```
where:
- W ∈ ℝᴰˣᴹ: the **loading matrix** (maps latent to observed)
- μ ∈ ℝᴰ: the mean of the observed data
- σ² > 0: isotropic noise variance in observation space

**Marginal distribution of x:**
```
x ~ N(μ, WW ᵀ + σ²I_D)
```
The covariance of x is WW ᵀ + σ²I_D — a low-rank matrix plus a scaled identity.

**Posterior of z given x:**
```
z | x ~ N(Mˉ¹Wᵀ(x - μ), σ²Mˉ¹)    where M = WᵀW + σ²I_M
```
This is a Gaussian — the model is entirely tractable. Mˉ¹Wᵀ(x-μ) is the
posterior mean (the "encoded" representation of x).

**MLE solution — connection to classical PCA:**

Maximizing the marginal log-likelihood over W and σ² yields:
```
W_ML = U_M (Λ_M - σ²I)^(1/2) R
```
where U_M = top-M eigenvectors of S, Λ_M = diag(λ₁,...,λ_M),
and R is any orthogonal rotation matrix (a free parameter — PPCA is
rotation-invariant in the latent space). In the limit σ² → 0:
```
W_ML → U_M Λ_M^(1/2)     (principal components × square root eigenvalues)
```
Classical PCA is the noiseless limit of PPCA.

**MLE for σ²:**
```
σ²_ML = (1/(D-M)) Σᵢ₌ₘ₊₁ᴰ λᵢ
```
This is the average of the discarded eigenvalues — the average variance in
the directions PCA ignores. A large σ² means the dropped directions have
significant variance (a warning that M is too small).

**EM algorithm for PPCA:**

Useful when data is incomplete. The E-step computes the posterior mean and
covariance of z given observed x; the M-step updates W and σ². Converges
to the same MLE solution as the eigendecomposition route.

**Connection to Factor Analysis:**

Factor analysis relaxes σ²I_D to a full diagonal matrix Ψ = diag(ψ₁,...,ψ_D),
allowing different noise levels per feature. This breaks the clean eigenvector
solution — Factor Analysis must be solved by EM and does not have a closed form.

---

## Key Formulas Quick Reference

| Concept | Formula | Note |
|---------|---------|------|
| Centered data | x̃ₙ = xₙ - μ | Always center first |
| Sample mean | μ = (1/N) Σₙ xₙ | |
| Covariance matrix | S = (1/N) X̃ᵀX̃ | D×D, symmetric PSD |
| Variance along b | Var = bᵀSb | b unit vector |
| Lagrangian | L = bᵀSb - λ(bᵀb-1) | constrained max variance |
| Eigenvector condition | Sb = λb | from ∂L/∂b = 0 |
| Total variance | tr(S) = Σᵢ λᵢ | sum of all eigenvalues |
| Projection scores | zₙ = Bᵀx̃ₙ | N×M score matrix Z = X̃B |
| Reconstruction | x̃̂ₙ = BBᵀx̃ₙ | BBᵀ = projection matrix |
| Reconstruction error | J = Σᵢ₌ₘ₊₁ᴰ λᵢ | sum of discarded eigenvalues |
| Covariance of scores | Cov(Z) = Λ_M | diagonal — PCA decorrelates |
| SVD of data | X̃ = UΣVᵀ | Vᵀ = principal components |
| Eigenvalue from SVD | λᵢ = σᵢ²/N | |
| High-dim matrix | C = (1/N) X̃X̃ᵀ | N×N, use when N < D |
| Explained variance | (Σᵢ≤ₘ σᵢ²) / ‖X̃‖_F² | fraction of total variance |
| Frobenius error | ‖X̃-X̃̂‖_F² = Σᵢ>ₘ σᵢ² | discarded singular values |
| PPCA marginal | x ~ N(μ, WWᵀ + σ²I) | generative model |
| PPCA noise MLE | σ²_ML = (1/(D-M)) Σᵢ>ₘ λᵢ | avg discarded variance |

---

## Key Connections to Other Chapters

| Concept | How it connects | Where |
|---------|----------------|-------|
| SVD of X̃ = UΣVᵀ | V = principal components; σᵢ²/N = eigenvalues of S | C4 §4.5 |
| Eckart-Young theorem | PCA is the optimal low-rank approx of X̃ (Frobenius sense) | C4 §4.6 |
| Spectral theorem | S symmetric → real eigenvalues, orthogonal eigenvectors | C4 §4.2 |
| Orthogonal projection | x̃̂ = BBᵀx̃ is a projection (C3 definition) | C2/C3 §3.8 |
| Gram-Schmidt | Building orthonormal basis B = [b₁|···|bₘ] | C3 §3.8 |
| Covariance matrix | S = (1/N)X̃ᵀX̃ is the sample covariance introduced for Gaussians | C6 §6.5 |
| Multivariate Gaussian | PPCA uses N(Wz+μ, σ²I); marginal/posterior both Gaussian | C6 §6.5 |
| Chain rule / gradients | Lagrangian ∂L/∂b = 0 uses matrix gradients from C5 | C5 §5.2 |
| tr(AB) gradient | Deriving covariance of projected scores uses tr(UΛUᵀ) = tr(Λ) | C5 §5.4 |
| Basis change | PCA changes basis from standard features to eigenvectors | C2 §2.7 |
| Rank and null space | Discarded components span the null space of the projection BBᵀ | C2 §2.7 |

**Cross-chapter summary:**

C2 and C3 provide the language (subspaces, projections, orthonormal bases).
C4 provides the machinery (eigendecomposition, SVD, Eckart-Young).
C5 provides the calculus (Lagrangian stationarity conditions).
C6 provides the probabilistic interpretation (covariance, Gaussians).
C10 is where all of these threads converge into a single, coherent algorithm.

---

## Open Questions

- Why do §10.2 (max variance) and §10.3 (min reconstruction error) give the
  same answer — is there an intuitive proof without algebra?
  (Yes: variance captured + variance discarded = total variance = tr(S).
   Maximizing one is identically minimizing the other.)

- Why is the PCA solution not unique when there are repeated eigenvalues?
  (If λᵢ = λⱼ, any orthonormal basis of the corresponding eigenspace is
   equally valid — there is no unique "direction of maximum variance" within
   a degenerate eigenspace.)

- How does PPCA handle missing data?
  (At the E-step, compute the posterior of z using only the observed features;
   the model can still infer the likely latent code and thereby impute missing
   entries from the posterior mean of x given z.)

- What is the difference between PCA and whitening?
  (PCA projects onto eigenvectors and keeps the scale (variance λᵢ in each
   direction). Whitening additionally divides each component by √λᵢ, making
   the projected data isotropic: Cov = I. Useful as a preprocessing step
   for algorithms that assume zero-mean unit-variance features.)

- When should you use factor analysis instead of PCA?
  (When features have genuinely different noise levels — FA models per-feature
   noise Ψ = diag(ψ₁,...,ψ_D) and is more appropriate for questionnaire data
   or heterogeneous sensor arrays. PCA assumes isotropic noise σ²I.)

- What is the computational cost of each approach?
  (Standard: eigendecomp of S costs O(D³). High-dim: eigendecomp of C costs
   O(N³). SVD of X̃ costs O(min(N,D)·ND) — usually the cheapest route.
   Randomized SVD algorithms (e.g. Halko et al. 2011) reduce this further to
   O(NDM) for the top-M components.)
