# C9: Linear Regression — Study Notes

> Linear regression is the proving ground for probabilistic machine learning.
> Starting from a simple noise model, the chapter builds from MLE (least squares)
> to MAP (ridge) to full Bayesian inference — each adding one more ingredient
> of uncertainty. The Bayesian treatment culminates in a predictive distribution
> over outputs, not just a point estimate, and connects cleanly to Gaussian processes.

**Primary source:** MML Ch 9 (pp 289–315, PDF pp 295–321)
**Supplementary:**
- [3Blue1Brown: But what is a neural network?](https://www.youtube.com/watch?v=aircAruvnKk) (regression intuition)
- [Bishop PRML Ch 3](https://www.microsoft.com/en-us/research/publication/pattern-recognition-machine-learning/) — companion treatment of Bayesian linear regression
- [Gaussian Processes for Machine Learning (Rasmussen & Williams)](http://www.gaussianprocess.org/gpml/) — Ch 2 extends §9.5
- [David MacKay: Information Theory, Inference, and Learning Algorithms](http://www.inference.org.uk/mackay/itila/) — Ch 43 on evidence maximization

---

## Chapter Structure at a Glance

C9 assembles a ladder of regression estimators, each step adding a richer treatment of uncertainty:

1. **§9.1** — Problem Formulation: noise model, design matrix, assumptions
2. **§9.2** — Maximum Likelihood Estimation: likelihood → log-likelihood → normal equations (least squares)
3. **§9.3** — MAP Estimation: add a Gaussian prior → ridge regression
4. **§9.4** — Bayesian Linear Regression: treat θ as a random variable → posterior + predictive distribution
5. **§9.5** — Features and the Kernel Trick: lift inputs via φ; predictive equations in kernel form; GP connection
6. **§9.6** — Evidence Maximization (Type II MLE): optimize the marginal likelihood over hyperparameters α, σ²

The conceptual thread: each section relaxes one more rigid assumption. MLE assumes fixed noise and no prior. MAP adds a prior but still collapses the posterior to a point. Bayesian regression keeps the full posterior distribution. Evidence maximization removes the need to hand-tune hyperparameters.

---

## Reading Notes

### 9.1 Problem Formulation

**The generative model.** We observe scalar outputs yₙ ∈ ℝ paired with input vectors
xₙ ∈ ℝᴰ. The assumed relationship is:

```
yₙ = xₙᵀθ + εₙ
```

where:
- **θ ∈ ℝᴰ** — parameter vector (weights)
- **εₙ ~ N(0, σ²)** — independent Gaussian noise with known variance σ²

This means each observation is a noisy linear function of its input:
```
p(yₙ | xₙ, θ) = N(yₙ | xₙᵀθ, σ²)
```

The mean is the linear predictor xₙᵀθ; the variance σ² is the irreducible noise.

**Dataset and design matrix.** We collect N observations into:
```
D = {(x₁, y₁), ..., (xₙ, yₙ)}
```

Stack them into matrix/vector form:
```
X ∈ ℝᴺˣᴰ   (design matrix: row n = xₙᵀ)
y ∈ ℝᴺ      (target vector: entry n = yₙ)
```

So the full likelihood factorizes as a product of Gaussians over N observations.

**Assumptions to keep in mind:**
- Linearity: the signal is truly xᵀθ (no interaction terms unless features are expanded)
- Homoscedastic noise: σ² is the same for all n
- Independent observations: the εₙ are i.i.d.
- Noise is Gaussian (not Student-t, not Laplace)

When these assumptions hold, the MLE is optimal. When they fail, the estimates can be biased or inefficient.

**Scalar vs. vector form.** The full dataset in matrix notation:
```
y = Xθ + ε,     ε ~ N(0, σ²I)
```
where 0 is the N-vector of zeros and I is the N×N identity. This gives:
```
p(y | X, θ) = N(y | Xθ, σ²I)
```
— a multivariate Gaussian with mean vector Xθ and diagonal covariance σ²I.

---

### 9.2 Maximum Likelihood Estimation

**The likelihood.** Since the observations are independent:
```
p(y | X, θ) = ∏ₙ N(yₙ | xₙᵀθ, σ²)
             = ∏ₙ (1/√(2πσ²)) exp(-(yₙ - xₙᵀθ)² / (2σ²))
```

**Log-likelihood.** Taking the log (monotone transformation, doesn't change the argmax):
```
log p(y | X, θ) = -N/2 log(2πσ²) - 1/(2σ²) Σₙ (yₙ - xₙᵀθ)²
                = -N/2 log(2πσ²) - 1/(2σ²) ‖y - Xθ‖²
```

The first term is a constant w.r.t. θ. Maximizing the log-likelihood over θ is therefore
equivalent to **minimizing the residual sum of squares**:
```
L(θ) = ‖y - Xθ‖²   =   (y - Xθ)ᵀ(y - Xθ)
```

**Connection to least squares.** MLE under Gaussian noise = ordinary least squares (OLS).
The probabilistic model gives a clean justification for a classic algorithm.

**Deriving the normal equations.** Expand and differentiate with respect to θ:
```
L(θ) = yᵀy - 2θᵀXᵀy + θᵀXᵀXθ

∂L/∂θ = -2Xᵀy + 2XᵀXθ = 0

XᵀXθ = Xᵀy          ← the normal equations
```

**MLE solution.** When XᵀX is invertible (X has full column rank, i.e., rank D):
```
θ_ML = (XᵀX)⁻¹ Xᵀy
```

This is the **pseudoinverse** (Moore-Penrose) of X applied to y:
```
θ_ML = X⁺ y,     where X⁺ = (XᵀX)⁻¹Xᵀ
```

**Conditions for uniqueness.** XᵀX is invertible iff X has full column rank D.
If N < D (fewer samples than features), or if columns of X are linearly dependent,
XᵀX is singular and there is no unique MLE — infinitely many θ minimize L(θ).
This is the underdetermined or collinear regime; MAP/Bayesian methods regularize it.

**Geometric interpretation.** The predicted values ŷ = Xθ_ML are the orthogonal
projection of y onto the column space of X:
```
ŷ = X(XᵀX)⁻¹Xᵀ y   =   P_X y
```
where P_X = X(XᵀX)⁻¹Xᵀ is the **hat matrix** (projection matrix).

Properties of P_X:
- Symmetric: P_Xᵀ = P_X
- Idempotent: P_X² = P_X
- P_X y = ŷ (projects onto col(X)); (I - P_X)y = residuals ⊥ col(X)

The residuals y - ŷ are orthogonal to every column of X. This is why the normal
equations are called "normal" — the residual vector is normal (perpendicular) to
the column space.

**MLE for σ².** Plugging θ_ML back in and optimizing over σ²:
```
σ²_ML = (1/N) ‖y - Xθ_ML‖²
```
This is the average squared residual. (Note: biased estimator; unbiased is 1/(N-D).)

---

### 9.3 MAP Estimation

**Motivation.** When XᵀX is singular or nearly singular, the MLE is unstable.
Introducing a prior on θ regularizes the problem by shrinking estimates toward zero.

**The prior.** Place a zero-mean isotropic Gaussian prior on θ:
```
p(θ) = N(θ | 0, b²I)
```
The hyperparameter b² controls how "spread out" we expect θ to be.
Larger b² → weaker regularization; as b² → ∞, MAP → MLE.

**Posterior (unnormalized).** By Bayes' theorem:
```
p(θ | X, y) ∝ p(y | X, θ) p(θ)
```

Taking logs (since we maximize):
```
log p(θ | X, y) ∝ -1/(2σ²) ‖y - Xθ‖² - 1/(2b²) ‖θ‖²
```

Maximizing this is equivalent to minimizing:
```
L_MAP(θ) = ‖y - Xθ‖² + (σ²/b²) ‖θ‖²
```

**Connection to ridge regression.** Setting λ = σ²/b², this is exactly the **ridge
regression** (L2-regularized least squares) objective:
```
L_MAP(θ) = ‖y - Xθ‖² + λ‖θ‖²
```

Ridge regression was originally proposed as a computational trick to stabilize
ill-conditioned systems; MAP gives it a principled probabilistic justification.
The regularization strength λ is the noise-to-prior-variance ratio.

**MAP solution.** Differentiating and setting to zero:
```
∂L_MAP/∂θ = -2Xᵀ(y - Xθ) + 2(σ²/b²)θ = 0

(XᵀX + σ²/b² I) θ = Xᵀy
```

```
θ_MAP = (XᵀX + σ²/b² I)⁻¹ Xᵀy
```

**Why this always exists.** The matrix XᵀX + λI (λ > 0) is always **positive definite**:
- XᵀX is positive semidefinite (xᵀXᵀXx = ‖Xx‖² ≥ 0)
- Adding λI shifts all eigenvalues up by λ, making them all strictly positive
- Therefore (XᵀX + λI) is always invertible — no rank assumption needed

This is the key practical advantage of MAP over MLE: it works even when N < D.

**Bias-variance tradeoff.**
- MLE: unbiased, but high variance when XᵀX is ill-conditioned
- MAP/ridge: introduces bias (estimates shrink toward 0), but variance is reduced
- The optimal λ minimizes the total prediction error (bias² + variance)
- Cross-validation or evidence maximization (§9.6) can select λ

---

### 9.4 Bayesian Linear Regression

**Motivation.** MAP gives a point estimate of θ — the posterior mode.
But the full posterior p(θ | X, y) carries more information: which θ values are plausible,
how uncertain we are, and how that uncertainty propagates to predictions.
Bayesian linear regression keeps the full posterior.

**Conjugate prior.** When the likelihood is Gaussian and the prior is Gaussian,
the posterior is also Gaussian (conjugate pair). This makes everything tractable.

**Setup.** Prior:
```
p(θ) = N(θ | m₀, S₀)
```
Likelihood:
```
p(y | X, θ) = N(y | Xθ, σ²I)
```

**Posterior derivation.** The key identity: product of two Gaussians in θ is Gaussian.
Completing the square in the exponent of p(y|X,θ)p(θ) w.r.t. θ:

**Posterior:**
```
p(θ | X, y) = N(θ | m_N, S_N)
```

**Posterior precision (inverse covariance):**
```
S_N⁻¹ = S₀⁻¹ + σ⁻² XᵀX
```

**Posterior mean:**
```
m_N = S_N (S₀⁻¹ m₀ + σ⁻² Xᵀy)
```

**Intuition behind the formulas:**
- S_N⁻¹ is a sum of prior precision (S₀⁻¹) and data precision (σ⁻²XᵀX).
  More data → larger data precision term → tighter posterior (smaller S_N).
- m_N is a precision-weighted average of prior information (S₀⁻¹m₀)
  and data information (σ⁻²Xᵀy). As N→∞, data overwhelms the prior.
- When m₀ = 0 and S₀ = b²I (isotropic prior), the posterior mean reduces to θ_MAP:
  ```
  m_N = (XᵀX + σ²/b² I)⁻¹ Xᵀy = θ_MAP
  ```
  MAP is the mode AND mean of the posterior (since Gaussian is symmetric).

**Sequential / online updating.** Bayesian linear regression can be updated
incrementally: process data in batches, using the current posterior as the next prior.
After seeing batch 1 → posterior (m₁, S₁); use (m₁, S₁) as prior for batch 2 → (m₂, S₂).
The final posterior is the same regardless of how the data is split.

**Predictive distribution.** Given a new test input x*, we want to predict y*.
Marginalizing over the posterior on θ:
```
p(y* | x*, X, y) = ∫ p(y* | x*, θ) p(θ | X, y) dθ
```

Both factors under the integral are Gaussian in θ. The result is:
```
p(y* | x*, X, y) = N(y* | m_Nᵀ x*, x*ᵀ S_N x* + σ²)
```

**Predictive mean:** m_Nᵀ x* — posterior mean prediction (same as MAP prediction)

**Predictive variance:** x*ᵀ S_N x* + σ²
- x*ᵀ S_N x*: **epistemic uncertainty** — uncertainty in θ (shrinks with more data)
- σ²: **aleatoric uncertainty** — irreducible observation noise (constant)

This decomposition is one of the key payoffs of Bayesian inference.
The predictive variance is not constant — it depends on x*. Predictions far from
the training data have higher epistemic uncertainty (S_N inflates variance for
out-of-distribution x*).

**Comparison with MAP:**
- MAP: point prediction m_Nᵀ x*, no uncertainty quantification
- Bayesian: full predictive distribution with calibrated confidence intervals

---

### 9.5 Bayesian Linear Regression with Features

**Motivation.** Raw inputs x ∈ ℝᴰ may not be linearly related to y.
By mapping x through a **feature map** φ, we can fit non-linear relationships
while keeping all the Bayesian machinery.

**Feature map:**
```
φ: ℝᴰ → ℝᴷ
x ↦ φ(x)
```
Examples:
- Polynomial: φ(x) = [1, x, x², ..., xᴷ⁻¹]
- Radial basis functions (RBFs): φ(x) = [exp(-‖x-c₁‖²/(2l²)), ...]
- Fourier features, Legendre polynomials, etc.

**Feature design matrix:**
```
Φ ∈ ℝᴺˣᴷ,    Φₙₖ = φₖ(xₙ)
```

All formulas from §9.4 carry over with X → Φ, D → K:
```
S_N⁻¹ = S₀⁻¹ + σ⁻² ΦᵀΦ
m_N   = S_N (S₀⁻¹ m₀ + σ⁻² Φᵀy)

Predictive mean:     φ(x*)ᵀ m_N
Predictive variance: φ(x*)ᵀ S_N φ(x*) + σ²
```

**The kernel trick.** For large K (or K = ∞), computing with Φ explicitly is expensive.
The predictive distribution depends on Φ only through inner products φ(x)ᵀφ(x').
Define the **kernel function**:
```
k(x, x') = φ(x)ᵀ φ(x')
```

The **kernel matrix** (Gram matrix):
```
K ∈ ℝᴺˣᴺ,    Kₙₘ = k(xₙ, xₘ) = φ(xₙ)ᵀ φ(xₘ)
```

With the prior S₀⁻¹ = α I (isotropic, precision α), the predictive mean becomes:
```
E[y* | x*, X, y] = φ(x*)ᵀ m_N
                 = σ⁻² φ(x*)ᵀ S_N Φᵀ y
                 = k*ᵀ (K + σ²I)⁻¹ y
```
where k* ∈ ℝᴺ is the vector with entries k*ₙ = k(x*, xₙ).

**Predictive variance in kernel form:**
```
Var[y* | x*, X, y] = k(x*, x*) - k*ᵀ (K + σ²I)⁻¹ k* + σ²
```

These are exactly the **Gaussian process regression** equations. The Bayesian linear
regression with feature map φ is equivalent to a GP with kernel k(x, x') = φ(x)ᵀφ(x').

**Gaussian Process connection.** A GP defines a distribution over functions directly
via the kernel, without specifying φ explicitly. Mercer's theorem guarantees that any
valid (positive definite) kernel corresponds to some (possibly infinite-dimensional) feature
map. So GP regression is the limiting case of Bayesian linear regression as K → ∞.

**Why the kernel form is useful:**
- The N×N kernel matrix K replaces the K×K matrix ΦᵀΦ
- When K << N (few features, many data), the feature form (§9.4) is cheaper
- When K >> N (many features, few data), the kernel form is cheaper (N×N inversion)
- For infinite-dimensional φ (e.g., RBF kernel), only the kernel form is tractable

**The duality.** There are two equivalent ways to write the same predictor:
```
Primal (feature) form:    f(x) = φ(x)ᵀ θ,    θ learned in K-dim space
Dual (kernel) form:       f(x) = k*ᵀ (K+σ²I)⁻¹ y,    directly from data
```

---

### 9.6 Evidence Maximization (Type II MLE)

**The hyperparameter problem.** Bayesian linear regression still has hyperparameters:
- α: prior precision (= 1/b²)
- σ²: noise variance

These are often hand-tuned, but we can instead learn them from data by maximizing
the **marginal likelihood** (also called the **evidence**):
```
p(y | X, α, σ²) = ∫ p(y | X, θ, σ²) p(θ | α) dθ
```

This is called **Type II MLE** or **empirical Bayes** — we treat hyperparameters as
parameters to be optimized, but via the marginal (not the full joint) likelihood.

**Why the marginal likelihood?** By integrating out θ, the marginal likelihood
automatically balances model fit vs. complexity (Occam's razor):
- High α (tight prior): θ forced near 0, poor fit, low evidence
- Low α (loose prior): θ free to fit, but large model space, lower evidence
- Optimal α: best fit achievable by the typical θ under the prior

**Computing the evidence.** Since both p(y|X,θ,σ²) and p(θ|α) are Gaussian, the
integral is tractable. The result is:
```
log p(y | X, α, σ²) = -N/2 log(2π)
                     - 1/2 log|S_N⁻¹/α|
                     - N/2 log(σ²)
                     - 1/(2σ²) ‖y - Xm_N‖²
                     - α/2 m_Nᵀ m_N
```

(Exact form varies by notation convention; the key point is that it is computable.)

Equivalently, using the eigendecomposition of XᵀX:
```
log p(y | X, α, σ²) = N/2 log α - 1/2 Σᵢ log(α + σ⁻² λᵢ)
                     - 1/(2σ²) ‖y - Xm_N‖² - α/2 m_Nᵀm_N
                     + const
```
where λ₁,...,λ_D are the eigenvalues of XᵀX.

**Effective number of parameters.** Define:
```
γ = Σᵢ λᵢ / (α σ² + λᵢ)     (sum over D eigenvalues)
```
γ ∈ [0, D] measures how many parameters are "determined by the data" (as opposed to
being pinned by the prior). When all λᵢ >> ασ², all D parameters are data-determined (γ≈D).
When λᵢ << ασ², the prior dominates and γ≈0.

**Optimality conditions.** Taking derivatives and setting to zero:
```
α* = γ / (m_Nᵀ m_N)       (optimal prior precision)
σ²* = ‖y - Xm_N‖² / (N - γ)    (optimal noise variance)
```

These are implicit equations (m_N depends on α and σ²), so we iterate:
1. Initialize α, σ²
2. Compute m_N, S_N (posterior update, §9.4)
3. Compute γ
4. Update α* and σ²*
5. Repeat until convergence

**Connection to EM.** Evidence maximization is a special case of the EM algorithm
where θ is the "latent variable" and (α, σ²) are the parameters.
The E-step computes the posterior over θ; the M-step maximizes the expected
complete-data log-likelihood w.r.t. (α, σ²) — which yields the update formulas above.

**Evidence lower bound (ELBO).** By Jensen's inequality:
```
log p(y | X) ≥ E_q[log p(y | X, θ)] - KL(q(θ) ‖ p(θ))
```
for any approximate posterior q(θ). When q is chosen to be the exact posterior
(as in §9.4), the ELBO equals the log evidence exactly. This is the foundation of
variational inference — when exact posteriors are intractable, we optimize the ELBO
over a family of approximate distributions q.

---

## Key Formulas Quick Reference

| Concept | Formula | Note |
|---------|---------|------|
| Noise model | yₙ = xₙᵀθ + εₙ, εₙ ~ N(0,σ²) | i.i.d. Gaussian noise |
| Design matrix | X ∈ ℝᴺˣᴰ, row n = xₙᵀ | Stacks all inputs |
| Likelihood | p(y|X,θ) = N(y | Xθ, σ²I) | Product of N Gaussians |
| Log-likelihood | -N/2 log(2πσ²) - 1/(2σ²)‖y-Xθ‖² | Maximized by MLE |
| Normal equations | XᵀXθ = Xᵀy | Set ∂L/∂θ = 0 |
| MLE solution | θ_ML = (XᵀX)⁻¹Xᵀy = X⁺y | Least squares |
| Hat matrix | P_X = X(XᵀX)⁻¹Xᵀ | Projection onto col(X) |
| Ridge / L2 objective | ‖y-Xθ‖² + λ‖θ‖² | λ = σ²/b² |
| MAP solution | θ_MAP = (XᵀX + σ²/b² I)⁻¹Xᵀy | Always exists (λ>0) |
| Prior | p(θ) = N(θ | m₀, S₀) | Conjugate to Gaussian likelihood |
| Posterior precision | S_N⁻¹ = S₀⁻¹ + σ⁻²XᵀX | Prior + data precision |
| Posterior mean | m_N = S_N(S₀⁻¹m₀ + σ⁻²Xᵀy) | Precision-weighted average |
| Predictive mean | m_Nᵀ x* | Posterior mean prediction |
| Predictive variance | x*ᵀS_Nx* + σ² | Epistemic + aleatoric |
| Kernel | k(x,x') = φ(x)ᵀφ(x') | Inner product in feature space |
| GP predictive mean | k*ᵀ(K+σ²I)⁻¹y | Kernel form |
| GP predictive var | k(x*,x*) - k*ᵀ(K+σ²I)⁻¹k* + σ² | Kernel form |
| Evidence | p(y|X,α,σ²) = ∫ p(y|X,θ)p(θ|α) dθ | Marginal likelihood |
| Effective params | γ = Σᵢ λᵢ/(ασ²+λᵢ) | ∈ [0, D] |
| Optimal α | α* = γ/(m_Nᵀm_N) | Evidence maximization |
| Optimal σ² | σ²* = ‖y-Xm_N‖²/(N-γ) | Evidence maximization |

---

## Key Connections to Other Chapters

| Concept in C9 | Where It Comes From / Goes |
|---------------|---------------------------|
| Gaussian distribution | C6 (definition, conditioning, marginalization) |
| Product of Gaussians is Gaussian | C6 §6.5 (Gaussian conditioning formulas) |
| Completing the square in θ | C6 (deriving Gaussian posteriors) |
| Matrix calculus (∂L/∂θ) | C5 (vector/matrix gradients, chain rule) |
| Pseudoinverse X⁺ = (XᵀX)⁻¹Xᵀ | C4 §4.6 (SVD-based pseudoinverse) |
| Orthogonal projection P_X | C3 §3.8 (projection formula, geometric interpretation) |
| Eigenvalues of XᵀX | C4 §4.2 (eigenvalues, spectral properties) |
| Cholesky for solving S_N | C4 §4.3 (stable linear system solver) |
| Conjugate prior | C9 = first detailed worked example; generalized in C11 (GMMs) |
| KL divergence (ELBO) | C6 §6.7 (KL divergence between Gaussians) |
| Evidence ↔ ELBO ↔ EM | Foundational for C11 (EM algorithm for GMMs) |
| Kernel trick / GP | C12 (Gaussian processes as infinite-dimensional BLR) |
| Bayesian model comparison | C9 §9.6 provides the concrete example; general theory in C8 |
| Feature maps φ | Connects to neural networks (Part III), where φ is learned |
| Bias-variance decomposition | C8 §8.2 (bias-variance tradeoff in generalization) |

**Downstream dependencies:**
- C10 (PCA) uses eigendecomposition of data covariance — same XᵀX structure as C9
- C11 (Gaussian Mixture Models) uses EM — the same algorithmic pattern as §9.6
- C12 (Gaussian Processes) is Bayesian linear regression in the kernel dual form,
  taken to the limit K → ∞

---

## Open Questions

- Why does maximizing the marginal likelihood avoid overfitting even though we're still
  doing MLE (just on hyperparameters)?
  (Because the marginal likelihood integrates out θ. Hyperparameters that allow
   a "too flexible" model are penalized by the volume of function space — the model
   can fit the data, but so can many other θ values, diluting the likelihood.)

- What happens to the posterior when N → ∞?
  (The data precision term σ⁻²XᵀX dominates S₀⁻¹. The posterior concentrates
   around the MLE: m_N → θ_ML and S_N → 0. Bayesian and frequentist solutions agree.)

- Why does ridge regression shrink coefficients toward zero but not select variables?
  (L2 penalty ‖θ‖² shrinks all coefficients proportionally but never makes them
   exactly zero. L1 (Lasso) creates sparsity because its gradient has a discontinuity
   at zero. This connects to Laplace prior vs. Gaussian prior in the MAP framework.)

- How does the predictive variance x*ᵀS_Nx* behave far from the training data?
  (For test points x* far from the training distribution, the term x*ᵀS_Nx* is large
   because S_N has not been "shrunk" in directions not covered by training data.
   This is epistemic uncertainty growing appropriately for out-of-distribution inputs.)

- In evidence maximization, what goes wrong if we just maximize p(y|X,θ) over θ AND
  (α, σ²) jointly?
  (Setting α=0 (infinite prior width) and σ²→0 gives infinite likelihood for any N≥D —
   the degenerate solution. Marginalizing out θ avoids this by penalizing complexity
   through the prior volume.)

- How is C9's Bayesian linear regression different from a Gaussian process?
  (They are mathematically equivalent when the kernel is k(x,x')=φ(x)ᵀφ(x').
   GPs are more general: any positive definite k is valid, not just those arising from
   finite-dimensional φ. The RBF kernel corresponds to an infinite-dimensional φ.)
