# C5: Vector Calculus — Study Notes

> Differentiation is just asking "what is the best linear approximation here?"
> Everything in this chapter — partial derivatives, Jacobians, backprop — is
> that one idea applied at different scales.

**Primary source:** MML Ch 5 (pp 139–170)
**Supplementary:**
- [3Blue1Brown: Essence of Calculus](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr)
- [Khan Academy: Multivariable Calculus](https://www.khanacademy.org/math/multivariable-calculus)
- [The Matrix Calculus You Need for Deep Learning (Parr & Howard)](https://explained.ai/matrix-calculus/)
- [CS231n: Backpropagation Notes (Karpathy)](https://cs231n.github.io/optimization-2/)

---

## Chapter Structure at a Glance

C5 builds differentiation from the ground up and then connects it directly to ML:

1. **§5.1** — Univariate derivatives: the foundation
2. **§5.2** — Partial derivatives and gradients: extend to multiple inputs
3. **§5.3** — Jacobians: gradients of vector-valued functions (the key for backprop)
4. **§5.4** — Gradients of matrices: chain rule meets linear algebra
5. **§5.5** — Useful identities: a reference table for practical computations
6. **§5.6** — Backpropagation and automatic differentiation: the ML payoff
7. **§5.7** — Hessians: second derivatives capture curvature
8. **§5.8** — Taylor series: linearization and higher-order local approximation

The thread connecting everything: **a derivative is a linear map** that locally
approximates a nonlinear function. Jacobians are matrices of those linear maps.
Backprop is just the chain rule applied to Jacobians, traversed in reverse.

---

## Reading Notes

### 5.1 Differentiation of Univariate Functions

**The basic idea:**
```
f'(x) = lim_{h→0} [f(x+h) - f(x)] / h
```
This is the slope of the tangent line at x — equivalently, the best linear
approximation to f near x. If f'(x) > 0, f is increasing; if f'(x) < 0, decreasing.

**Differentiation rules** (the toolkit):

| Rule | Formula |
|------|---------|
| Sum | (f + g)' = f' + g' |
| Product | (fg)' = f'g + fg' |
| Quotient | (f/g)' = (f'g - fg') / g² |
| Chain rule | (g∘f)'(x) = g'(f(x)) · f'(x) |

The chain rule is the most important one. In the multivariate setting it becomes
a product of Jacobian matrices — and that's what backpropagation computes.

**Standard derivatives to know:**

| Function f(x) | Derivative f'(x) |
|----------------|-----------------|
| xⁿ | nxⁿ⁻¹ |
| exp(x) | exp(x) |
| ln(x) | 1/x |
| sin(x) | cos(x) |
| cos(x) | -sin(x) |

**Taylor series preview:** f'(x) is the coefficient of the linear term when f
is expanded around a point. The full Taylor expansion (§5.8) generalizes this.

---

### 5.2 Partial Differentiation and Gradients

**Multiple inputs, one output.**

For f: ℝⁿ → ℝ, the **partial derivative** ∂f/∂xᵢ holds all other inputs fixed
and differentiates only with respect to xᵢ:
```
∂f/∂xᵢ = lim_{h→0} [f(x₁,...,xᵢ+h,...,xₙ) - f(x₁,...,xᵢ,...,xₙ)] / h
```

**The gradient** collects all partial derivatives into one row vector:
```
∇ₓf = [∂f/∂x₁, ∂f/∂x₂, ..., ∂f/∂xₙ] ∈ ℝ¹ˣⁿ
```

Critical point: MML defines the gradient as a **row vector**, not a column
vector. This matters for matrix shapes when composing Jacobians. (Many other
books use column vectors — be careful about which convention a source uses.)

**Intuition:** The gradient points in the direction of steepest ascent. Its
magnitude ‖∇f‖ tells you how fast f is changing in that direction. This is
exactly what gradient descent uses — step opposite to the gradient.

**Partial derivatives can be taken in any order** (Schwarz's theorem):
```
∂²f / ∂xᵢ∂xⱼ = ∂²f / ∂xⱼ∂xᵢ
```
as long as f is twice continuously differentiable. This symmetry will reappear
in the Hessian (§5.7).

**Rules carry over from univariate:**

| Rule | Multivariate form |
|------|-------------------|
| Sum | ∇(f + g) = ∇f + ∇g |
| Product | ∇(fg) = g∇f + f∇g |
| Chain rule | See §5.3 / §5.4 |

**Example — squared Euclidean norm:**
```
f(x) = ‖x‖² = xᵀx = Σᵢ xᵢ²
∇f = 2xᵀ   (a row vector)
```
You'll compute this all the time in regression and optimization.

---

### 5.3 Gradients of Vector-Valued Functions (Jacobians)

**Multiple inputs, multiple outputs.**

For f: ℝⁿ → ℝᵐ (i.e., f outputs a vector, not just a scalar), the derivative
is no longer a simple row vector. It is the **Jacobian matrix**:
```
J = ∂f/∂x ∈ ℝᵐˣⁿ

      [∂f₁/∂x₁  ∂f₁/∂x₂  ...  ∂f₁/∂xₙ]
J =   [∂f₂/∂x₁  ∂f₂/∂x₂  ...  ∂f₂/∂xₙ]
      [    ⋮                         ⋮  ]
      [∂fₘ/∂x₁  ∂fₘ/∂x₂  ...  ∂fₘ/∂xₙ]
```
- Each row i is the gradient of the i-th output fᵢ with respect to all inputs.
- Each column j shows how all outputs change when input xⱼ changes.

**The Jacobian is the linear map that best approximates f near a point.**
This is the geometric heart of the chapter: just as f'(x) tells you the slope
of a line (1D linear map), J(x) is the matrix of a linear transformation (nD
linear map) that locally approximates f.

**Chain rule for vector functions:**
If y = f(x) and z = g(y), then:
```
dz/dx = (dz/dy)(dy/dx) = J_g · J_f
```
where J_g ∈ ℝᵖˣᵐ and J_f ∈ ℝᵐˣⁿ, so dz/dx ∈ ℝᵖˣⁿ.

This is just matrix multiplication of Jacobians. Backpropagation is
this formula, applied layer by layer from output to input (§5.6).

**Dimension tracking is everything.** If you lose track of whether a quantity
is (1×n) or (n×1), the Jacobians won't multiply correctly. Always check shapes.

**Example:** For a neural network layer y = σ(Wx + b):
- dy/dx = J_σ(Wx+b) · W
- J_σ is diagonal (σ acts elementwise) so this simplifies
- But the shapes must match: if y ∈ ℝᵐ and x ∈ ℝⁿ, then dy/dx ∈ ℝᵐˣⁿ

---

### 5.4 Gradients of Matrices

**Differentiating with respect to matrices.**

When either the input or output is a matrix (not just a vector), we need to be
even more careful. For f: ℝᵐˣⁿ → ℝ (a scalar function of a matrix), the
gradient is a matrix of the same shape:
```
∂f/∂A ∈ ℝᵐˣⁿ    where (∂f/∂A)ᵢⱼ = ∂f/∂Aᵢⱼ
```

This comes up constantly in ML:
- Loss as a function of weight matrix W
- Derivatives of trace, determinant, matrix norms

**Vectorization approach:** Sometimes it is cleaner to flatten (vectorize)
matrices into vectors and work with standard Jacobians. MML introduces the
**vec** operator:
```
vec(A) stacks columns of A into a single column vector
```
The resulting Jacobians can be very large, but they are notationally consistent
with the vector case. In practice, libraries handle the bookkeeping.

**Key identity often needed:**
```
d/dX [aᵀXb] = abᵀ
d/dX [aᵀXᵀb] = baᵀ
d/dX [tr(AXB)] = AᵀBᵀ  (for appropriate dimensions)
```
See §5.5 for a fuller list.

---

### 5.5 Useful Identities for Computing Gradients

This section is a reference table — a lookup for when you need specific
matrix-calculus results. Do not memorize these; learn where to look them up
and how to verify them from first principles if needed.

**Most frequently used:**

| Expression | Gradient (w.r.t. x or X) |
|------------|--------------------------|
| ∂(xᵀa)/∂x | a (column) |
| ∂(aᵀx)/∂x | aᵀ (row) |
| ∂(xᵀBx)/∂x | xᵀ(B+Bᵀ) |
| ∂(xᵀBx)/∂x (B symmetric) | 2xᵀ |
| ∂‖x‖²/∂x | 2xᵀ |
| ∂(tr(AB))/∂A | Bᵀ |
| ∂(det(A))/∂A | det(A) · A⁻ᵀ |
| ∂(ln det A)/∂A | A⁻ᵀ |

**Why det(A) gradient is det(A)·A⁻ᵀ:** Jacobi's formula. The log-determinant
gradient A⁻ᵀ appears in the derivation of maximum-likelihood for Gaussian
models (Ch 6) — log|Σ| is differentiated w.r.t. Σ.

**Strategy for deriving an unfamiliar gradient:**
1. Write out the expression element-by-element
2. Take partial derivative w.r.t. one element
3. Read off the pattern and pack it back into matrix form
4. Check dimensions — if a scalar is differentiated by an (m×n) matrix,
   the result must be (m×n)

---

### 5.6 Backpropagation and Automatic Differentiation ⭐

This is the most important section for ML practitioners.

#### Why It Exists

Neural networks are compositions of many functions:
```
y = fₖ(fₖ₋₁(...f₂(f₁(x))))
```
We need ∂L/∂θ for every parameter θ in every layer. Computing each derivative
independently is prohibitively expensive (O(N) passes for N parameters).
Backpropagation reduces this to **two passes** (one forward, one backward).

#### The Chain Rule, Again

For a composition of K functions with intermediate values y₀ = x, y₁, ..., yₖ = L:
```
∂L/∂yᵢ = (∂L/∂yᵢ₊₁) · (∂yᵢ₊₁/∂yᵢ)
```
Each step multiplies a Jacobian. Going from output to input is the **reverse
accumulation** — and this is all backprop is.

#### Forward vs. Reverse Mode

Two ways to apply the chain rule to a composition:

| Mode | Direction | Cost | Best when |
|------|-----------|------|-----------|
| Forward (forward-mode AD) | Left to right (input → output) | O(n) per output | Many outputs, few inputs |
| Reverse (reverse-mode AD = backprop) | Right to left (output → input) | O(m) per input | Few outputs, many inputs |

Neural network training: 1 scalar loss output, millions of parameters (inputs).
Reverse mode wins overwhelmingly. This is why backprop is used everywhere.

#### The Computation Graph

Any computation can be represented as a directed acyclic graph (DAG):
- **Nodes:** intermediate values (scalars, vectors, matrices)
- **Edges:** operations (addition, multiplication, nonlinear activations, etc.)

Forward pass: compute all node values, store them.
Backward pass: traverse the graph in reverse, accumulate **gradients** using
the chain rule at each edge.

**The key insight:** Each operation only needs to implement two things:
1. Forward computation (produce its output from its inputs)
2. Local gradient (the Jacobian of its output w.r.t. each input)

The chain rule handles the rest automatically.

#### Example: One Layer

For y = Wx + b, with scalar loss L = ½‖y − t‖²:
```
Forward:  y = Wx + b
          L = ½‖y − t‖²

Backward: ∂L/∂y = (y − t)ᵀ              [1×m]
          ∂L/∂W = ∂L/∂y · ∂y/∂W = (y−t)xᵀ   [m×n]
          ∂L/∂b = ∂L/∂y · ∂y/∂b = (y−t)      [m×1]
          ∂L/∂x = Wᵀ(y−t)                     [n×1]
```

Note: ∂L/∂x is needed to pass the gradient back to the previous layer.
∂L/∂W and ∂L/∂b are the parameter updates.

#### Automatic Differentiation (AD) vs. Alternatives

| Method | What it does | Problem |
|--------|-------------|---------|
| Symbolic differentiation | Algebraically differentiates expressions | Explosion in expression size |
| Numerical differentiation | Finite differences: [f(x+h) - f(x)]/h | Truncation error + slow |
| Automatic differentiation | Tracks derivatives through actual computation | Exact + efficient |

Modern deep learning frameworks (PyTorch, JAX, TensorFlow) implement **reverse-mode AD**.
The user writes the forward computation; the framework constructs the backward pass
automatically using the computation graph.

#### Key Concepts in AD Systems

- **Tape / Wengert list:** a record of all operations in order (forward pass builds it)
- **vjp (vector-Jacobian product):** the primitive that reverse mode actually computes
  (gradient vector times Jacobian); avoids materializing the full Jacobian matrix
- **jvp (Jacobian-vector product):** the forward-mode primitive

For large n (many parameters), vjp/reverse mode does one sweep; jvp/forward mode
would need n sweeps. This cost difference is why ML uses reverse mode.

---

### 5.7 Higher-Order Derivatives (Hessians)

**Second derivatives capture curvature.**

For f: ℝⁿ → ℝ, the **Hessian** H (or ∇²f) is the matrix of second-order
partial derivatives:
```
H ∈ ℝⁿˣⁿ,    Hᵢⱼ = ∂²f / ∂xᵢ∂xⱼ
```

Since ∂²f/∂xᵢ∂xⱼ = ∂²f/∂xⱼ∂xᵢ (Schwarz's theorem), the Hessian is **symmetric**.

**Interpretation:**
- H tells you the curvature of f in every direction.
- If H is positive definite (all eigenvalues > 0) at a critical point, that
  point is a local minimum.
- If H is negative definite, it's a local maximum.
- If H has mixed-sign eigenvalues, it's a saddle point.

**Newton's method** uses the Hessian to find optima:
```
x_{t+1} = xₜ − H⁻¹∇f(xₜ)
```
This converges much faster than gradient descent (quadratic vs. linear
convergence) — but computing and inverting H is O(n³), which is prohibitive
for n = millions of parameters. Quasi-Newton methods (L-BFGS, etc.) approximate
H⁻¹ cheaply without forming the full matrix.

**The Hessian's eigenvalues** describe the loss landscape. Very large eigenvalue
ratio (ill-conditioned H) means the landscape is steep in some directions and
flat in others — this causes gradient descent to oscillate and slow down.
This is part of why learning rate tuning matters.

---

### 5.8 Linearization and Multivariate Taylor Series

**Local approximation by polynomials.**

The **Taylor expansion** of f around a point x₀ gives a polynomial approximation:

**Univariate:**
```
f(x) ≈ f(x₀) + f'(x₀)(x−x₀) + ½f''(x₀)(x−x₀)² + ...
     = Σₖ₌₀ᴷ [f⁽ᵏ⁾(x₀)/k!](x−x₀)ᵏ  +  remainder
```

**Multivariate (f: ℝⁿ → ℝ):**
```
f(x) ≈ f(x₀) + (∇f(x₀))(x−x₀) + ½(x−x₀)ᵀH(x₀)(x−x₀) + ...
```

- Zeroth-order term: f(x₀) — constant approximation
- First-order term: ∇f(x₀)·(x−x₀) — linear (plane) approximation
- Second-order term: ½(x−x₀)ᵀH(x₀)(x−x₀) — quadratic (bowl) approximation

**Why this matters for optimization:**
- Gradient descent uses only the first-order (linear) term.
- Newton's method uses first + second-order (quadratic) terms — much better model
  of the loss surface, hence faster convergence.
- Momentum and Adam approximate second-order information cheaply.

**Linearization = first-order Taylor = Jacobian:**
```
f(x₀ + Δx) ≈ f(x₀) + J(x₀) Δx
```
This is exactly the definition of the derivative as a linear map. The Jacobian
*is* the linearization operator.

---

## Key Formulas Quick Reference

| Concept | Formula |
|---------|---------|
| Univariate chain rule | (g∘f)'(x) = g'(f(x)) · f'(x) |
| Gradient (f: ℝⁿ→ℝ) | ∇ₓf = [∂f/∂x₁, ..., ∂f/∂xₙ] ∈ ℝ¹ˣⁿ |
| Jacobian (f: ℝⁿ→ℝᵐ) | J = ∂f/∂x ∈ ℝᵐˣⁿ, Jᵢⱼ = ∂fᵢ/∂xⱼ |
| Vector chain rule | ∂z/∂x = (∂z/∂y)(∂y/∂x) = J_g · J_f |
| Gradient of ‖x‖² | 2xᵀ |
| Gradient of xᵀBx (B symm.) | 2xᵀB |
| Gradient of tr(AB) w.r.t. A | Bᵀ |
| Gradient of ln det A | A⁻ᵀ |
| Hessian | Hᵢⱼ = ∂²f/∂xᵢ∂xⱼ, H symmetric |
| Newton step | x ← x − H⁻¹∇f |
| Multivariate Taylor (2nd order) | f(x₀) + ∇f(x₀)(x−x₀) + ½(x−x₀)ᵀH(x₀)(x−x₀) |

---

## Key Connections to Other Chapters

| Concept | Where It Shows Up |
|---------|-------------------|
| Gradients / ∇f | Ch 7 (gradient descent), Ch 9 (MLE / MAP optimization) |
| Jacobians as linear maps | C2 (linear mappings) — the derivative IS a linear map |
| Chain rule / backprop | Ch 6 (gradient of log-likelihoods), every ML model training |
| Hessian + convexity | Ch 7 (§7.3 convex functions, second-order condition) |
| Taylor series / linearization | Ch 7 (gradient descent step derivation), Ch 9 (Laplace approx.) |
| Matrix gradients | Ch 9 (differentiating least-squares loss w.r.t. W) |
| log det A gradient | Ch 6 (MLE for Gaussians, differentiating log-likelihood w.r.t. Σ) |

## Open Questions

- Why does reverse-mode AD have cost O(m) in the number of outputs? Work through
  a concrete example with different m and n to see when forward mode wins.
- What happens to the Jacobian at a point where f is not differentiable
  (e.g., ReLU at 0)? Why does subgradient/supergradient still work in practice?
- How do second-order optimizers (L-BFGS) approximate H⁻¹ without forming it?
  (connects to quasi-Newton methods)
- The Jacobian is a linear map. What is the geometric meaning of its singular
  values? (connects back to SVD in Ch 4)
