# C7: Continuous Optimization — Study Notes

> Optimization is the engine of machine learning. Every model trains by solving
> an optimization problem. This chapter gives you the vocabulary, the algorithms,
> and the geometric intuition to understand what is actually happening when you
> press "train."

**Primary source:** MML Ch 7 (pp 225–247)
**Supplementary:**
- [Stanford CS229: Convex Optimization review notes](https://cs229.stanford.edu/section/cs229-cvxopt.pdf)
- [Convex Optimization (Boyd & Vandenberghe) — free PDF](https://web.stanford.edu/~boyd/cvxbook/)
- [Distill: Why Momentum Really Works](https://distill.pub/2017/momentum/)
- [Adam paper (Kingma & Ba, 2015)](https://arxiv.org/abs/1412.6980)

---

## Chapter Structure at a Glance

C7 covers the three major pillars of continuous optimization:

1. **§7.1** — Gradient descent: vanilla, with momentum, and Adam
2. **§7.2** — Constrained optimization: Lagrange multipliers and KKT conditions
3. **§7.3** — Convex optimization: when you can trust your solution is global

The chapter's central question: given a function f(x) we want to minimize, how
do we find x* without solving analytically? And when do we know the answer is
the *globally* best one?

---

## Reading Notes

### 7.1 Optimization Using Gradient Descent

#### The Basic Setup

We want to find:
```
x* = argmin_{x} f(x)
```
where f: ℝⁿ → ℝ is differentiable. At a minimum, the gradient must be zero:
```
∇f(x*) = 0
```
But we usually cannot solve this analytically. Gradient descent is an iterative
approach: take small steps in the direction that decreases f fastest.

#### Vanilla Gradient Descent

The gradient ∇f(x) points in the direction of steepest *ascent*. So we step
in the *opposite* direction:
```
x_{t+1} = xₜ − α ∇f(xₜ)
```
where α > 0 is the **learning rate** (step size).

**Geometric picture:** Imagine a hilly landscape. Gradient descent always steps
downhill in the locally steepest direction. It will reach a valley — but not
necessarily the deepest one in the whole landscape.

**The learning rate α is critical:**
- Too large: steps overshoot and may diverge
- Too small: convergence is very slow
- Just right: converges to a local minimum

This is the classic learning rate selection problem. There is no universal answer;
in practice you use schedules, line searches, or adaptive methods (see Adam below).

**Three variants by how much data is used per step:**

| Variant | Data per step | Gradient | Use case |
|---------|--------------|----------|----------|
| Batch GD | Full dataset | Exact ∇f | Convex problems, small data |
| Stochastic GD (SGD) | 1 sample | Noisy estimate | Online learning |
| Mini-batch SGD | k samples | Estimate, less noisy | Standard DL training |

Mini-batch SGD is the standard in deep learning. The noise from using a subset
is actually beneficial: it helps escape sharp local minima (that generalize poorly)
and finds flatter minima (that tend to generalize better — see Hochreiter & Schmidhuber
1997, Keskar et al. 2017).

#### Gradient Descent with Momentum

Plain GD takes the same-sized step every iteration. **Momentum** accumulates a
velocity vector: it speeds up in consistent directions and dampens oscillations.

```
vₜ = β vₜ₋₁ + ∇f(xₜ)      (accumulate gradient, discount old directions)
x_{t+1} = xₜ − α vₜ
```

β ∈ [0, 1) is the momentum coefficient (typically 0.9).

**Intuition:** Think of a ball rolling downhill. Without momentum, it moves
only based on the current slope. With momentum, it carries velocity from previous
steps — it rolls faster in consistent directions and oscillates less in narrow
valleys ("ravines").

**Why it helps with ill-conditioned Hessians:** If the loss surface is much
steeper in one direction than another (large condition number of H), plain GD
bounces back and forth across the steep direction and barely progresses in the
flat direction. Momentum damps the oscillations and lets the ball pick up speed
along the flat direction.

#### Adam: Adaptive Moment Estimation

Adam (Kingma & Ba, 2015) is the most widely used optimizer in deep learning.
It combines momentum with **per-parameter adaptive learning rates**.

```
m_t = β₁ m_{t-1} + (1 − β₁) gₜ         (1st moment: exponential MA of gradients)
v_t = β₂ v_{t-1} + (1 − β₂) gₜ²        (2nd moment: exponential MA of squared grads)

m̂_t = m_t / (1 − β₁ᵗ)                   (bias correction — important early in training)
v̂_t = v_t / (1 − β₂ᵗ)

x_{t+1} = xₜ − α m̂_t / (√v̂_t + ε)
```

Default hyperparameters: β₁ = 0.9, β₂ = 0.999, ε = 10⁻⁸.

**What each part does:**
- m̂_t (first moment) is momentum: average direction of recent gradients
- v̂_t (second moment) is an estimate of gradient variance per parameter
- Dividing by √v̂_t scales the learning rate down for parameters with large/erratic
  gradients, and up for parameters with small/consistent gradients

**Intuition:** Adam is like a scientist who pays more attention to consistent
signals and discounts noisy ones. A parameter that always gets a large gradient
gets a smaller effective step size; one with a small gradient gets a larger step.

**Bias correction:** Early in training, m and v are initialized at zero. Without
correction, they are biased toward zero and the effective step would be tiny.
The (1 − βᵗ) denominator corrects this.

**Practical note:** Adam often works well with minimal tuning. But for convex
problems or when you need reproducibility, SGD with momentum can outperform Adam
in final accuracy (Wilson et al., 2017). Adam typically gets you *close* to
a good solution fast; fine-tuning often switches to SGD.

#### Convergence and the Loss Landscape

**Convex functions:** A single global minimum. GD always converges to it (for
appropriate α). See §7.3.

**Non-convex functions (typical neural networks):**
- Many local minima, saddle points, plateaus
- No guarantee of finding the global minimum
- Empirically, large neural networks seem to have many near-equivalent local minima
  (Goodfellow et al. 2015, Choromanska et al. 2015)
- Saddle points (not local minima) are the main obstacle in high dimensions

---

### 7.2 Constrained Optimization and Lagrange Multipliers

#### The Problem

Sometimes you need to minimize f(x) subject to constraints:
```
min  f(x)
s.t. gᵢ(x) = 0    for i = 1,...,m    (equality constraints)
     hⱼ(x) ≤ 0    for j = 1,...,k    (inequality constraints)
```

Simply doing unconstrained GD ignores the constraints — you might step outside
the feasible region. Lagrange multipliers reformulate the problem so you can
optimize without constraints while still respecting them.

#### Equality Constraints: Lagrange Multipliers

For min f(x) subject to g(x) = 0, introduce a **Lagrange multiplier** λ:

```
L(x, λ) = f(x) + λ g(x)          (the Lagrangian)
```

At the optimum, the gradient of L with respect to *both* x and λ must be zero:
```
∂L/∂x = ∇f(x) + λ ∇g(x) = 0
∂L/∂λ = g(x) = 0
```

**Geometric intuition:** The condition ∇f + λ∇g = 0 means the gradient of f
is parallel to the gradient of g at the solution. Equivalently, the level curves
of f and g are tangent at the optimum — you cannot move along the constraint
and decrease f simultaneously. λ is the "exchange rate" between f and g.

**Example:** Maximize xᵀy subject to ‖x‖ = 1. The Lagrangian is:
```
L = xᵀy − λ(‖x‖² − 1)
∂L/∂x = y − 2λx = 0  →  x = y/(2λ)
```
This shows the optimum is x = y/‖y‖ (unit vector in the direction of y).

#### Inequality Constraints: KKT Conditions

For both equality and inequality constraints, the **Karush-Kuhn-Tucker (KKT)
conditions** generalize Lagrange multipliers:

Form the Lagrangian:
```
L(x, λ, μ) = f(x) + Σᵢ λᵢgᵢ(x) + Σⱼ μⱼhⱼ(x)
```

At the optimum x*, the following must hold:

| Condition | Name | Meaning |
|-----------|------|---------|
| ∇ₓL = 0 | Stationarity | Gradient condition at optimum |
| gᵢ(x*) = 0 | Primal feasibility (eq.) | Equality constraints satisfied |
| hⱼ(x*) ≤ 0 | Primal feasibility (ineq.) | Inequality constraints satisfied |
| μⱼ ≥ 0 | Dual feasibility | Multipliers for ineq. must be non-negative |
| μⱼhⱼ(x*) = 0 | Complementary slackness | Either constraint is active OR multiplier = 0 |

**Complementary slackness explained:** If the inequality hⱼ ≤ 0 is *inactive*
at the optimum (hⱼ(x*) < 0 strictly), then the constraint is not "biting" and
its multiplier must be 0 (μⱼ = 0). If the constraint *is* active (hⱼ(x*) = 0),
then μⱼ may be nonzero. This is what "complementary" means — at least one of
{μⱼ, hⱼ(x*)} is zero.

**Connection to SVMs (Ch 12):** Support vector machines solve exactly this type
of problem. The training objective is quadratic with linear inequality constraints
(margin conditions). The KKT conditions reveal that only the support vectors
(data points where the margin constraint is active) have nonzero μⱼ — all other
training points don't affect the solution. This is why SVMs are sparse in the
"support" that defines the decision boundary.

#### Primal and Dual Problems

The Lagrangian also leads to the **dual problem**:
```
Primal: min_x max_{λ,μ} L(x, λ, μ)
Dual:   max_{λ,μ} min_x  L(x, λ, μ)
```

The dual is always concave (easy to maximize), even if the primal is non-convex.
**Strong duality** (primal = dual optimal value) holds when the problem is convex
and Slater's condition holds (there exists a strictly feasible point). Under
strong duality, solving the dual is equivalent to solving the primal — and
the dual is often easier.

---

### 7.3 Convex Optimization

#### Why Convexity Matters

**The key guarantee:** If f is convex, any local minimum is a global minimum.
Gradient descent will find it (with appropriate step size). This is the gold
standard — you know you've found the best possible solution.

Most of the "nice" ML problems are convex: linear regression, logistic regression,
SVMs with appropriate kernels. Neural networks are not convex — but the tools
from convex optimization still inform how we think about them.

#### Convex Sets

A set C ⊆ ℝⁿ is **convex** if for any two points x, y ∈ C, the line segment
between them lies entirely in C:
```
θx + (1−θ)y ∈ C    for all θ ∈ [0, 1]
```

**Examples of convex sets:**
- The empty set and any single point
- Any line, line segment, ray
- ℝⁿ itself
- Hyperplanes {x : aᵀx = b}
- Halfspaces {x : aᵀx ≤ b}
- Euclidean balls {x : ‖x − xc‖ ≤ r}
- Ellipsoids
- Polyhedra (intersection of halfspaces)
- Positive semidefinite cone {X : X = Xᵀ, xᵀXx ≥ 0 for all x}

**Examples of non-convex sets:**
- Annuli (rings)
- Non-convex polygons
- The set {0, 1}ⁿ (discrete points — this is why integer programming is hard)

**Operations that preserve convexity:**
- Intersection of convex sets is convex
- Affine images and preimages of convex sets are convex

#### Convex Functions

f: C → ℝ is **convex** if for all x, y ∈ C and θ ∈ [0, 1]:
```
f(θx + (1−θ)y) ≤ θf(x) + (1−θ)f(y)
```

**Geometric picture:** The function lies *below* any chord between two points on
its graph. Equivalently: the epigraph (set of points above the graph) is a convex set.

**Strictly convex:** strict inequality above (for x ≠ y and θ ∈ (0,1)).
Strictly convex functions have at most one global minimum.

**Common convex functions:**

| Function | Domain | Notes |
|----------|--------|-------|
| Linear f(x) = aᵀx + b | ℝⁿ | Also concave — both flat |
| Quadratic ‖x‖² | ℝⁿ | Strictly convex |
| exp(x) | ℝ | |
| max(x₁,...,xₙ) | ℝⁿ | Convex but not differentiable |
| log-sum-exp | ℝⁿ | Smooth approximation to max |
| −ln(x) | ℝ₊₊ | |
| Negative entropy x ln x | ℝ₊ | |

**Operations that preserve convexity:**
- Nonneg. linear combination: α f + β g (for α, β ≥ 0, f, g convex)
- Pointwise max of convex functions
- Composition with affine function: f(Ax + b)
- (With care) composition with convex/monotone functions

#### Second-Order Characterization

If f is twice differentiable, f is convex iff its Hessian is positive
semidefinite (PSD) everywhere:
```
H(x) = ∇²f(x) ⪰ 0    for all x in the domain
```

For strictly convex: H ≻ 0 (positive definite). This connects §5.7 directly
to convexity — the curvature must always be non-negative.

**Example:** f(x) = xᵀAx for symmetric A. H = 2A. f is convex iff A is PSD.

#### Jensen's Inequality

For a convex function f:
```
f(E[X]) ≤ E[f(X)]
```
"The function of the average is at most the average of the function."

**Why it matters in ML:**
- Derives the EM algorithm's lower bound (E-step)
- Proves the KL divergence is non-negative: KL(p‖q) ≥ 0
- Underlies the variational inference framework (ELBO)
- Used in information theory and statistical bounds throughout Ch 6

**Intuition:** The expected value of X is "inside" the distribution, and
convex functions "bowl upward," so f applied at the average is lower than the
average of f applied at each point.

#### Convexity and Optimization Algorithms

**Gradient descent on convex f:**
- Converges to the global minimum for α small enough (α < 1/L where L is the
  Lipschitz constant of ∇f)
- Convergence rate: O(1/t) for convex, O(1/t²) for strongly convex (Nesterov)

**Strongly convex:** f(y) ≥ f(x) + ∇f(x)ᵀ(y−x) + (m/2)‖y−x‖² for some m > 0.
Strongly convex functions have a unique global minimum and GD converges linearly
(exponentially fast): O(e^{-mt}) for appropriate α.

**Condition number:** κ = L/m (ratio of Lipschitz constant to strong convexity
constant) controls convergence speed. Large κ (ill-conditioned) → slow
convergence → similar to the ill-conditioned Hessian problem from §5.7.

---

## Key Formulas Quick Reference

| Concept | Formula |
|---------|---------|
| Gradient descent step | x_{t+1} = xₜ − α∇f(xₜ) |
| Momentum update | vₜ = βvₜ₋₁ + ∇f; x_{t+1} = xₜ − αvₜ |
| Adam (simplified) | x_{t+1} = xₜ − α m̂ₜ / (√v̂ₜ + ε) |
| Lagrangian (equality) | L(x,λ) = f(x) + λᵀg(x) |
| Lagrangian (ineq.) | L(x,λ,μ) = f(x) + λᵀg(x) + μᵀh(x) |
| KKT stationarity | ∇ₓL = 0 |
| KKT complementary slackness | μⱼhⱼ(x*) = 0, μⱼ ≥ 0 |
| Convexity (set) | θx + (1−θ)y ∈ C ∀ θ ∈ [0,1] |
| Convexity (function) | f(θx + (1−θ)y) ≤ θf(x) + (1−θ)f(y) |
| Convexity (2nd order) | ∇²f(x) ⪰ 0 everywhere |
| Jensen's inequality | f(E[X]) ≤ E[f(X)] |
| Newton step | x ← x − H⁻¹∇f(x) |

---

## Key Connections to Other Chapters

| Concept | Where It Shows Up |
|---------|-------------------|
| Gradients (from C5) | §7.1 — gradient descent is built directly on ∂f/∂x |
| Hessians (from C5 §5.7) | §7.1 Newton's method, §7.3 2nd-order convexity condition |
| Taylor expansion (from C5 §5.8) | §7.1 — GD step derived from 1st-order Taylor |
| Lagrange multipliers / KKT | Ch 12 (SVM dual, support vectors, kernel trick) |
| Convex sets and functions | Ch 12 (SVM objective is convex QP) |
| Jensen's inequality | Ch 6 (KL divergence, ELBO in variational inference) |
| Positive semidefinite matrices | C3 (SPD inner products), Ch 4 (eigenvalues) |
| Strong duality | Ch 12 (SVM dual is solved instead of primal) |
| Lagrangian duality | Ch 6 (EM algorithm — lower-bounding log-likelihood) |

---

## The Gradient Descent Landscape in One Picture

```
Unconstrained           Constrained              Convex
─────────────           ───────────              ──────
min f(x)                min f(x)                 min f(x)   [convex f]
                        s.t. g(x) = 0            s.t. x ∈ C  [convex C]
Solve: ∇f = 0          Solve: ∇L = 0            Guarantee: local = global
Algo: GD / Adam        Tool: Lagrangians/KKT     Algo: GD converges
Risk: local minima      Risk: dual gap (non-cvx) Benefit: global optimum
```

---

## Open Questions

- Why does SGD's gradient noise help generalization? (Flat minima hypothesis,
  relates to regularization — see Ch 8 on regularization)
- When does strong duality fail? (Slater's condition; what if it is violated?)
- Adam can diverge on some convex problems (Reddi et al. 2018). Why? What fixes
  it (AMSGrad)? Is this a theoretical or practical concern?
- The KKT conditions are necessary for optimality. Under what conditions are they
  also sufficient? (Convexity + constraint qualification — research this)
- How does the condition number κ relate to the spectrum of the Hessian, and how
  do preconditioned optimizers (AdaGrad, RMSProp) implicitly reduce κ?
