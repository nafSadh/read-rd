# C12: Classification with Support Vector Machines — Study Notes

> SVMs distill classification down to a single geometric question: where is the widest
> "street" you can draw between two classes? The algorithm finds that street by solving
> a quadratic program, and the kernel trick lets it do so in arbitrarily high-dimensional
> feature spaces while working entirely in the original input space.

**Primary source:** MML Ch 12 (pp 370–392)
**Supplementary:**
- [3Blue1Brown: Support Vector Machines](https://www.youtube.com/watch?v=efR1C6CvhmE)
- [MIT 6.034 (Winston): Support Vector Machines](https://www.youtube.com/watch?v=_PwhiWxHK8o)
- [CS229 (Ng) SVM notes](https://cs229.stanford.edu/notes2022fall/cs229-notes3.pdf)
- [Understanding the Bias-Variance Tradeoff (scikit-learn docs)](https://scikit-learn.org/stable/auto_examples/svm/plot_rbf_parameters.html)

---

## Chapter Structure at a Glance

C12 builds the SVM in four conceptual moves:

1. **§12.1** — Separating Hyperplanes: what it means to linearly separate two classes
2. **§12.2** — Hard-Margin SVM: maximize the geometric margin (the "widest street") when data is perfectly separable
3. **§12.3** — Dual Formulation: rewrite the primal as a dual QP over Lagrange multipliers; prediction depends only on inner products
4. **§12.4** — Soft-Margin SVM: allow misclassifications via slack variables; trade margin width against violations with regularization constant C
5. **§12.5** — Kernelization: replace inner products with kernel functions to classify in implicit high-dimensional feature spaces
6. **§12.6** — Numerical Solution: quadratic programming; SMO algorithm; sparsity of support vectors

The conceptual thread: the dual formulation (§12.3) is the pivot. It reveals that
both the solution and prediction depend only on pairwise inner products xₙᵀxₘ —
which is exactly what the kernel replaces in §12.5.

---

## Reading Notes

### 12.1 Separating Hyperplanes

**Setup — binary classification:**
```
Training set: {(xₙ, yₙ) : n = 1,...,N},  xₙ ∈ ℝᴰ,  yₙ ∈ {+1, −1}
```
Goal: find a linear decision boundary that correctly separates the two classes.

**The hyperplane:**
```
{x ∈ ℝᴰ : wᵀx + b = 0}
```
where **w** ∈ ℝᴰ is the **weight vector** (normal to the hyperplane) and **b** ∈ ℝ is
the **bias** (offset from the origin). The hyperplane has dimension D−1 and divides ℝᴰ
into two half-spaces: {x : wᵀx + b > 0} and {x : wᵀx + b < 0}.

**Prediction rule:** classify a test point x* as
```
ŷ = sign(wᵀx* + b)
```
If wᵀx* + b > 0 → class +1; if < 0 → class −1.

**Signed distance from a point xₙ to the hyperplane:**
```
dₙ = (wᵀxₙ + b) / ‖w‖
```
Positive if xₙ is on the +1 side, negative on the −1 side.

**Correct classification condition:** for a correctly classified point,
the sign of yₙ matches the sign of (wᵀxₙ + b), so
```
yₙ(wᵀxₙ + b) > 0   ↔   xₙ is on the correct side
```
The magnitude yₙ(wᵀxₙ + b) / ‖w‖ is the (always positive) distance to the hyperplane
for a correctly classified point.

**Functional margin vs. geometric margin:**
- **Functional margin** of point n: ŷₙ = yₙ(wᵀxₙ + b) — unnormalized, depends on ‖w‖
- **Geometric margin** of point n: yₙ(wᵀxₙ + b) / ‖w‖ — actual Euclidean distance
- **Margin of the classifier:** min over all n of the geometric margin

The hyperplane is not unique — scaling (w, b) by any constant α > 0 gives the same
geometric separator but different functional margins. We will exploit this freedom
in §12.2 by fixing the functional margin of the closest point to be exactly 1.

**Non-uniqueness of separating hyperplanes:** if the data is linearly separable, there
are infinitely many hyperplanes that separate the classes. The SVM selects the one
with the maximum margin — the "widest street" between the two classes.

---

### 12.2 Hard-Margin SVM

**Setup:** assume the data is linearly separable. We want the hyperplane that maximizes
the width of the "margin" — the symmetric band around the boundary that contains no
training points.

**Margin geometry:**
```
Margin boundary for class +1:  wᵀx + b = +1
Decision boundary:              wᵀx + b =  0
Margin boundary for class −1:  wᵀx + b = −1
```
The width of the margin (the "street") is the distance between the two margin boundaries:
```
Margin width = 2 / ‖w‖
```
(Computed as the projection of the vector between a +1 support vector and a −1 support
vector onto the unit normal w/‖w‖.)

**Canonical form of constraints:** by the scale-freedom argument, we can choose ‖w‖ and b
such that the closest point(s) from each class lie exactly on the margin boundaries:
```
yₙ(wᵀxₙ + b) ≥ 1   for all n = 1,...,N
```
This is the **functional margin = 1** convention.

**Primal optimization problem (hard-margin SVM):**
```
min_{w, b}   ½ ‖w‖²
subject to   yₙ(wᵀxₙ + b) ≥ 1   for all n
```
The ½ and the square are for mathematical convenience (gives clean gradients).
Maximizing 2/‖w‖ is equivalent to minimizing ½‖w‖².

This is a **convex quadratic program** with N linear inequality constraints.
It has a unique global minimum.

**Support vectors:** the training points for which yₙ(wᵀxₙ + b) = 1 exactly — i.e.,
the points that lie exactly on the margin boundaries. These are the "support" of the
solution; all other points are strictly inside and irrelevant. If you removed a
non-support-vector training point, the solution would not change.

**Solution:** the optimal weight vector lies in the span of the support vectors:
```
w* = Σₙ αₙ yₙ xₙ   (summed over support vectors only)
```
This foreshadows the dual formulation.

---

### 12.3 Dual Formulation

The dual is constructed by introducing Lagrange multipliers and applying the KKT conditions.
This is where C7 (constrained optimization) feeds directly into C12.

**Lagrangian:**
```
L(w, b, α) = ½ ‖w‖² − Σₙ αₙ [yₙ(wᵀxₙ + b) − 1]
```
where αₙ ≥ 0 are the Lagrange multipliers (one per training point).

**KKT stationarity conditions:** set partial derivatives to zero.
```
∂L/∂w = 0:    w = Σₙ αₙ yₙ xₙ
∂L/∂b = 0:    Σₙ αₙ yₙ = 0
```
The first condition gives us w in terms of the multipliers.
The second gives the constraint Σₙ αₙ yₙ = 0 on the multipliers.

**KKT complementary slackness:**
```
αₙ [yₙ(wᵀxₙ + b) − 1] = 0   for all n
```
This means: either αₙ = 0 (point is not a support vector, constraint is slack)
or yₙ(wᵀxₙ + b) = 1 (point is a support vector, sits on the margin).
Most points have αₙ = 0 — the solution is sparse.

**Dual problem:** substitute the stationarity conditions back into L to eliminate w and b:
```
max_{α}   Σₙ αₙ − ½ ΣₙΣₘ αₙ αₘ yₙ yₘ xₙᵀxₘ
subject to  αₙ ≥ 0   for all n
            Σₙ αₙ yₙ = 0
```
This is also a convex QP (the Hessian of the objective is positive semidefinite).
Key structural feature: the data only appears through **pairwise inner products** xₙᵀxₘ.

**Recovering the primal solution from the dual:**
```
w* = Σₙ αₙ yₙ xₙ           (sum over all n, but most αₙ = 0)
b* = yₛ − w*ᵀxₛ            (computed from any support vector xₛ where αₛ > 0)
```
In practice b* is averaged over all support vectors for numerical stability.

**Prediction on a test point x*:**
```
ŷ = sign(w*ᵀx* + b*)
  = sign(Σₙ αₙ yₙ xₙᵀx* + b*)
```
Again, only inner products appear. Support vectors with αₙ > 0 contribute to the sum;
the rest drop out. Prediction is a weighted vote of the support vectors.

**Why strong duality holds:** the primal is convex and the constraints are affine
(Slater's condition is satisfied when data is separable), so the duality gap is zero
and the dual optimal = primal optimal.

---

### 12.4 Soft-Margin SVM

**Problem with hard-margin:** if the data is not linearly separable (overlapping classes,
outliers), no feasible solution exists. The hard-margin SVM fails.

**Idea:** allow some training points to be on the wrong side of the margin or even
misclassified, but penalize such violations.

**Slack variables:** introduce ξₙ ≥ 0 for each training point:
```
yₙ(wᵀxₙ + b) ≥ 1 − ξₙ   for all n,    ξₙ ≥ 0
```
- ξₙ = 0: point is correctly classified, outside or on the margin (no violation)
- 0 < ξₙ ≤ 1: point is inside the margin but still correctly classified
- ξₙ > 1: point is misclassified

**Soft-margin SVM primal:**
```
min_{w, b, ξ}   ½ ‖w‖² + C Σₙ ξₙ
subject to       yₙ(wᵀxₙ + b) ≥ 1 − ξₙ   for all n
                 ξₙ ≥ 0                    for all n
```
**C > 0** is the **regularization hyperparameter**:
- Large C → heavy penalty on violations → narrow margin, fewer misclassifications,
  risk of overfitting to outliers
- Small C → slack allowed → wider margin, more misclassifications tolerated,
  better generalization on noisy data

The two terms trade off: ½‖w‖² maximizes the margin (small ‖w‖), while C Σₙ ξₙ
penalizes constraint violations.

**Dual of the soft-margin SVM:**
```
max_{α}   Σₙ αₙ − ½ ΣₙΣₘ αₙ αₘ yₙ yₘ xₙᵀxₘ
subject to  0 ≤ αₙ ≤ C   for all n
            Σₙ αₙ yₙ = 0
```
The only difference from the hard-margin dual is the box constraint 0 ≤ αₙ ≤ C
(replacing αₙ ≥ 0). C now acts as an upper bound on each multiplier.

**Connection to hinge loss (C8 link):**
The soft-margin SVM objective can be rewritten (after eliminating the slack) as:
```
min_{w, b}   ½‖w‖² + C Σₙ max(0, 1 − yₙ(wᵀxₙ + b))
```
The function max(0, 1 − yₙ(wᵀxₙ + b)) is the **hinge loss** for point n.
It is zero when the point is correctly classified outside the margin, and grows
linearly with the violation. So the soft-margin SVM = L2-regularized ERM with hinge loss.

```
Hinge loss:   ℓ_hinge(y, f(x)) = max(0, 1 − y·f(x))
```

This connects to C8's empirical risk minimization framework. The ½‖w‖² term is the
regularizer (weight decay / L2); C is the inverse of the regularization strength λ.

**Support vectors in the soft-margin case (KKT analysis):**
- αₙ = 0: point is outside the margin, correctly classified, no contribution to w
- 0 < αₙ < C: point lies on the margin (yₙ(wᵀxₙ+b) = 1, ξₙ = 0) — margin support vector
- αₙ = C: point is inside the margin or misclassified (ξₙ > 0) — bound support vector

---

### 12.5 Kernelization

**Key observation from the dual:** both the dual objective and the prediction rule depend
on the training data only through **inner products** xₙᵀxₘ.

**Feature map idea:** suppose we apply a nonlinear feature map φ: ℝᴰ → ℝᴹ (M >> D),
mapping inputs to a higher-dimensional feature space. The dual then depends only on
φ(xₙ)ᵀφ(xₘ) — inner products in the high-dimensional space.

**Kernel function:** instead of computing φ(x) and then the inner product, define
```
k(xₙ, xₘ) = φ(xₙ)ᵀφ(xₘ)
```
If we can evaluate k directly in the original input space, we never need to compute φ
explicitly. This is the **kernel trick** — we work in a potentially infinite-dimensional
feature space without paying the computational cost.

**Kernelized dual:**
```
max_{α}   Σₙ αₙ − ½ ΣₙΣₘ αₙ αₘ yₙ yₘ k(xₙ, xₘ)
subject to  0 ≤ αₙ ≤ C   for all n
            Σₙ αₙ yₙ = 0
```

**Kernelized prediction:**
```
ŷ = sign(Σₙ αₙ yₙ k(xₙ, x*) + b*)
```

**Common kernels:**

Linear kernel (recovers the standard SVM):
```
k(x, x') = xᵀx'
```

Polynomial kernel:
```
k(x, x') = (xᵀx' + c)^p     (c ≥ 0, p ∈ ℕ)
```
Corresponds to features that are all monomials of degree ≤ p.

Gaussian / RBF (radial basis function) kernel:
```
k(x, x') = exp(−‖x − x'‖² / 2σ²)
```
σ is the **bandwidth** hyperparameter. The implied feature space is infinite-dimensional.
As σ → 0 the kernel becomes very local (high complexity); as σ → ∞ it approaches a
constant (underfitting). The Gaussian kernel corresponds to an infinite-dimensional
dot product via the Taylor expansion of the exponential.

**Mercer's theorem:** a symmetric, positive semidefinite function k: ℝᴰ × ℝᴰ → ℝ
is a valid kernel — i.e., there exists a feature map φ such that k(x, x') = φ(x)ᵀφ(x').
Validity is checked by confirming the kernel (Gram) matrix K ∈ ℝᴺˣᴺ with Kₙₘ = k(xₙ, xₘ)
is positive semidefinite for any set of inputs.

**Gram matrix:** the N×N matrix of all pairwise kernel evaluations on the training set:
```
K = [k(xₙ, xₘ)]_{n,m}
```
The dual QP can be expressed entirely in terms of K — no explicit feature vectors needed.

**Practical note:** kernel choice encodes assumptions about the structure of the data.
Linear kernel → linear boundaries. Polynomial → polynomial boundaries. RBF → smooth
local boundaries. The bandwidth σ (RBF) and degree p (polynomial) are tuned by
cross-validation alongside C.

**Connection to C4 (kernel PCA):** PCA on the Gram matrix K = φ(X)φ(X)ᵀ gives
**kernel PCA** — principal components in the implicit feature space. This is how
SVD (C4) and kernels (C12) intersect.

---

### 12.6 Numerical Solution

**Form of the problem:** the SVM dual is a **quadratic program (QP)**:
```
min_{α}   ½ αᵀ Q α − 1ᵀα
subject to  0 ≤ αₙ ≤ C   for all n
            yᵀα = 0
```
where Q ∈ ℝᴺˣᴺ with Qₙₘ = yₙ yₘ k(xₙ, xₘ). Q is PSD (valid kernel), so the QP
is convex with a unique global minimum.

**Challenge at scale:** Q is dense and N×N. For N = 10⁶, storing Q requires ~10¹²
entries — infeasible. Direct QP solvers do not scale.

**Sequential Minimal Optimization (SMO):** Platt (1998). The standard algorithm.
Instead of optimizing all N multipliers at once, SMO analytically solves the minimal
subproblem of **two variables** at a time (the smallest subproblem that respects the
equality constraint Σₙ αₙ yₙ = 0). The two-variable subproblem has a closed-form
solution, so no inner numerical solver is needed.

**SMO heuristics:**
1. Select one αₙ that violates the KKT conditions (most violated)
2. Select a second αₘ by a heuristic (e.g., maximize |Eₙ − Eₘ| where Eₙ = f(xₙ) − yₙ
   is the prediction error on point n)
3. Clip the updated αₙ, αₘ to the box [0, C] and rescale to satisfy the equality constraint
4. Update the bias b and the error cache

SMO has O(N) memory (stores only the N multipliers and errors) and converges superlinearly
in practice despite formally quadratic worst-case behavior.

**Sparsity of the solution:**
```
αₙ = 0    →  not a support vector; irrelevant to prediction
αₙ > 0    →  support vector; contributes to w* and prediction
```
Typically only a small fraction of training points are support vectors. This sparsity
makes prediction fast and the model interpretable: the classifier is fully described
by a small set of support vectors and their weights αₙ yₙ.

**Computing b*:** once the α are found, b is recovered from any support vector xₛ with
0 < αₛ < C (which lies exactly on the margin, yₛ(w*ᵀxₛ + b*) = 1):
```
b* = yₛ − Σₙ αₙ yₙ k(xₙ, xₛ)
```
Averaged over all such support vectors for numerical stability.

---

## Key Formulas Quick Reference

| Concept | Formula | Note |
|---------|---------|------|
| Decision boundary | wᵀx + b = 0 | D−1 dimensional hyperplane |
| Prediction rule | ŷ = sign(wᵀx* + b) | |
| Signed distance | yₙ(wᵀxₙ + b) / ‖w‖ | Positive ↔ correct side |
| Correct classification | yₙ(wᵀxₙ + b) > 0 | |
| Margin width | 2 / ‖w‖ | Between the two margin hyperplanes |
| Hard-margin primal | min ½‖w‖² s.t. yₙ(wᵀxₙ+b) ≥ 1 | Equivalent to max margin |
| Soft-margin primal | min ½‖w‖² + C Σξₙ s.t. yₙ(wᵀxₙ+b) ≥ 1−ξₙ, ξₙ≥0 | C controls tradeoff |
| Hinge loss | max(0, 1 − yₙ(wᵀxₙ+b)) | L2-reg ERM connection |
| Lagrangian | L = ½‖w‖² − Σαₙ[yₙ(wᵀxₙ+b)−1] | Hard-margin |
| KKT: ∂L/∂w = 0 | w = Σₙ αₙ yₙ xₙ | w in span of training pts |
| KKT: ∂L/∂b = 0 | Σₙ αₙ yₙ = 0 | Equality constraint in dual |
| Hard-margin dual | max Σαₙ − ½ΣΣαₙαₘyₙyₘxₙᵀxₘ s.t. αₙ≥0, Σαₙyₙ=0 | Inner-product form |
| Soft-margin dual | same but 0 ≤ αₙ ≤ C | Box constraint |
| Kernel trick | k(xₙ,xₘ) = φ(xₙ)ᵀφ(xₘ) | Replace inner products |
| RBF/Gaussian kernel | k(x,x') = exp(−‖x−x'‖²/2σ²) | Infinite-dim feature space |
| Polynomial kernel | k(x,x') = (xᵀx' + c)^p | Degree-p features |
| Kernelized prediction | ŷ = sign(Σαₙyₙk(xₙ,x*) + b*) | No explicit w needed |
| Primal from dual | w* = Σαₙyₙxₙ, b* = yₛ − w*ᵀxₛ | xₛ = any support vector |
| Complementary slackness | αₙ[yₙ(wᵀxₙ+b)−1] = 0 | αₙ=0 or on margin |

---

## Key Connections to Other Chapters

| Concept in C12 | Connection |
|----------------|------------|
| Lagrangian and dual formulation | **C7** — Lagrange multipliers, KKT conditions, strong duality (Slater's condition). The dual SVM is a direct application of C7 §7.2–7.3. |
| Inner products in the dual | **C3** — inner products, norms, and projections. The margin width = 2/‖w‖ is a C3 norm; signed distance is a C3 projection formula. |
| Kernel PCA | **C4** — SVD of the Gram matrix K = φ(X)φ(X)ᵀ gives principal components in the feature space. Kernel methods and SVD share the same Gram-matrix structure. |
| Hinge loss = ERM + L2 reg | **C8** — empirical risk minimization. The soft-margin SVM is ERM with hinge loss and L2 regularizer. C8 §8.2 covers ERM and the bias–variance tradeoff that C controls. |
| Positive semidefinite kernels | **C3** — inner product requires a PSD bilinear form (§3.2). Mercer's theorem reuses this: a valid kernel is exactly a PSD function (valid "inner product" in feature space). |
| Feature maps φ(x) | **C2** — basis change and linear maps. The feature map φ is a (nonlinear) change of representation; linear classification in feature space ↔ nonlinear boundary in input space. |
| Covariance / Gram matrix K | **C6** — K = φ(X)φ(X)ᵀ has the same structure as sample covariance matrices. Eigenvalues of K appear in kernel PCA (C10). |

**From C7 feeding in (most direct):**
- Lagrangian construction → dual of the hard-margin SVM (§12.2 → §12.3)
- KKT stationarity conditions → recover w* = Σαₙyₙxₙ
- KKT complementary slackness → sparsity (most αₙ = 0)
- KKT primal feasibility → constraint yₙ(wᵀxₙ+b) ≥ 1
- Slater's condition → strong duality holds (zero duality gap)

**The C → λ correspondence:**
```
Soft-margin SVM:   min_{w,b} ½‖w‖² + C Σ max(0, 1−yₙ(wᵀxₙ+b))
L2-reg ERM (C8):  min_{w,b} λ‖w‖² + Σ ℓ(yₙ, w,b)
```
Setting λ = 1/(2C) shows they are the same problem. Large C = small λ = little
regularization = complex model.

---

## Open Questions

- Why does the hard-margin SVM dual have no duality gap?
  (The primal is convex, constraints are affine, and the feasible set is non-empty when
  data is separable. Slater's condition (C7) guarantees strong duality.)

- How does the Gaussian kernel correspond to an infinite-dimensional feature space?
  (Via the Taylor expansion of exp(·): exp(−‖x−x'‖²/2σ²) = exp(−‖x‖²/2σ²)·exp(xᵀx'/σ²)·exp(−‖x'‖²/2σ²),
  and exp(xᵀx'/σ²) = Σₖ (xᵀx')ᵏ/(k! σ²ᵏ) — an infinite sum of polynomial kernels.)

- What happens when C → ∞ in the soft-margin SVM?
  (No slack is tolerated. If the data is separable, the soft-margin solution converges to
  the hard-margin solution. If not, the problem becomes infeasible.)

- Why are support vectors sufficient to define the decision boundary?
  (Complementary slackness: all non-support vectors have αₙ = 0, so they contribute nothing
  to w* = Σαₙyₙxₙ. Moving non-support vectors does not change w* or b*, as long as they
  remain outside the margin.)

- How do you choose σ (RBF bandwidth) and C in practice?
  (Cross-validation on a grid. Typical starting grid: C ∈ {10⁻², 10⁻¹, 1, 10, 100},
  σ ∈ {10⁻², 10⁻¹, 1, 10, 100}. Larger σ = smoother decision boundary.)

- What is the relationship between the SVM margin and the VC dimension?
  (The VC dimension of a linear classifier in ℝᴰ is D+1. But for the maximum-margin
  classifier, the effective complexity is bounded by the margin, not D — this is why SVMs
  can generalize even in very high dimensions, as in kernel feature spaces.)
