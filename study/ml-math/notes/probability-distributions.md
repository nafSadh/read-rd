# C6: Probability and Distributions — Study Notes

> Probability is the language of uncertainty. This chapter builds the grammar:
> from sample spaces to the multivariate Gaussian — the distribution that shows
> up in every corner of Part II.

**Primary source:** MML Ch 6 (pp 172–222, PDF pp 178–228)
**Supplementary:**
- [3Blue1Brown: Bayes theorem](https://www.youtube.com/watch?v=HZGCoVF3YvM)
- [Seeing Theory (Brown Univ.)](https://seeing-theory.brown.edu/) — interactive probability visuals
- [Michael Jordan: An Introduction to Probabilistic Graphical Models](https://people.eecs.berkeley.edu/~jordan/prelims/)
- [Chris Bishop: Pattern Recognition and Machine Learning, Ch 2](https://www.microsoft.com/en-us/research/uploads/prod/2006/01/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf)
- [StatQuest: Probability is not Likelihood](https://www.youtube.com/watch?v=pYxNSUDSFH4)

---

## Chapter Structure at a Glance

C6 builds a probability toolkit in seven stages:

1. **6.1** — Foundations: sample space, events, probability axioms
2. **6.2** — Discrete vs. continuous: PMF, PDF, CDF
3. **6.3** — Sum rule, product rule, Bayes' theorem
4. **6.4** — Summary statistics: mean, variance, covariance, independence
5. **6.5** — The Gaussian distribution ← the workhorse of Part II
6. **6.6** — Conjugate priors and the exponential family
7. **6.7** — Change of variables / inverse transform sampling

The logical arc: build a rigorous framework (6.1–6.3), add summary tools (6.4),
master the Gaussian (6.5), then understand *why* certain distributions pair
nicely in Bayesian inference (6.6), and finally learn how to transform
distributions (6.7).

---

## 6.1 Construction of a Probability Space

### The three ingredients

Probability theory rests on a triple (Ω, A, P):

| Component | Name | What it is |
|-----------|------|------------|
| Ω | Sample space | All possible outcomes of an experiment |
| A | Event space (σ-algebra) | Collection of subsets of Ω we can assign probabilities to |
| P | Probability measure | A function A → [0,1] satisfying the Kolmogorov axioms |

**Sample space Ω:**
- Discrete (finite or countably infinite): coin flips, dice rolls, word counts
- Continuous: real-valued measurements (temperatures, heights, model parameters)

**Event space A:**
- A subset E ⊆ Ω is an *event* — a set of outcomes
- A must be a σ-algebra: closed under complements and countable unions
- We need this formality because on continuous Ω, not every subset can be
  assigned a sensible probability (measure-theoretic technicality)

**Probability measure P:**
Three Kolmogorov axioms:
1. P(A) ≥ 0 for all A ∈ A (non-negativity)
2. P(Ω) = 1 (total probability = 1)
3. P(A₁ ∪ A₂ ∪ ...) = Σᵢ P(Aᵢ) for pairwise disjoint events (countable additivity)

From just these three axioms, everything else follows:
- P(∅) = 0
- P(Aᶜ) = 1 − P(A)
- P(A ∪ B) = P(A) + P(B) − P(A ∩ B)

### Why the formality?

For this book's purposes, you mostly just need the intuition: probabilities are
non-negative and sum/integrate to 1. But the formal setup matters because in
Part II (Bayesian models), the "experiment" is often the choice of model parameters,
and the sample space is continuous (e.g., Ω = ℝᵈ for a d-dimensional parameter vector).

---

## 6.2 Discrete and Continuous Probabilities

### Target space and random variables

A **random variable** X: Ω → T maps outcomes to a *target space* T (often T = ℝ).
- X induces a distribution on T
- We write P(X = x) or P(X ≤ x) as shorthand for probabilities of preimages

### Discrete: Probability Mass Function (PMF)

If T is discrete, X has a **PMF** p(x) = P(X = x).

Requirements:
- p(x) ≥ 0 for all x
- Σₓ p(x) = 1

Example: Bernoulli(μ): p(x=1) = μ, p(x=0) = 1−μ. Models a biased coin.

### Continuous: Probability Density Function (PDF)

If T is continuous, X has a **PDF** p(x) such that:

```
P(a ≤ X ≤ b) = ∫ₐᵇ p(x) dx
```

Requirements:
- p(x) ≥ 0 for all x
- ∫ p(x) dx = 1

**Critical distinction:** p(x) is NOT a probability. It's a *density* —
it can exceed 1. P(X = x) = 0 for any specific x in a continuous distribution.
Only intervals have nonzero probability.

### Cumulative Distribution Function (CDF)

```
F_X(x) = P(X ≤ x) = ∫₋∞ˣ p(t) dt
```

The CDF unifies discrete and continuous: it always maps ℝ → [0,1], is monotone
non-decreasing, right-continuous, and:
- lim_{x→−∞} F(x) = 0
- lim_{x→+∞} F(x) = 1

For continuous X: p(x) = dF/dx (density = derivative of CDF).

### Multivariate case

For a random vector **X** = (X₁, ..., Xₙ)ᵀ, the **joint distribution** p(**x**)
captures the full dependence structure.

**Marginal distribution** (sum/integrate out the other variable):

```
Discrete:   p(x) = Σ_y p(x, y)
Continuous: p(x) = ∫ p(x, y) dy
```

This is the **sum rule** (also called marginalization). You recover p(x) by
"summing over all the ways y could have been."

---

## 6.3 Sum Rule, Product Rule, Bayes' Theorem

These three rules are the entire engine of probabilistic reasoning.

### Conditional probability

```
P(A | B) = P(A ∩ B) / P(B)    for P(B) > 0
```

Read: "probability of A, given that B occurred."
Intuitively: restrict your universe to the event B, then renormalize.

### Product rule (chain rule)

Rearranging the conditional:

```
P(A ∩ B) = P(A | B) · P(B) = P(B | A) · P(A)
```

In joint distribution form: **p(x, y) = p(y | x) · p(x)**

This chains: **p(x₁, ..., xₙ) = p(x₁) · p(x₂|x₁) · p(x₃|x₁,x₂) · ... · p(xₙ|x₁,...,xₙ₋₁)**

### Sum rule (marginalizing)

```
p(x) = ∫ p(x, y) dy = ∫ p(x | y) p(y) dy
```

Also written as: **p(x) = E_y[p(x | y)]** — marginalizing = averaging over y.

### Bayes' theorem ⭐

Combining sum rule + product rule:

```
p(x | y) = p(y | x) p(x) / p(y)
```

where **p(y) = ∫ p(y | x) p(x) dx** (the normalizing constant, also called "evidence").

**The Bayesian interpretation:**
- **p(x)** — prior: what we believe about x before seeing data
- **p(y | x)** — likelihood: how probable is observation y if x is true
- **p(x | y)** — posterior: updated belief after seeing y
- **p(y)** — evidence: total probability of observation (normalizing constant)

```
posterior ∝ likelihood × prior
```

The ∝ matters in practice: computing p(y) often requires a difficult integral,
so many algorithms work with unnormalized posteriors and handle the constant separately.

**Why Bayes' theorem is central to ML:**
In supervised learning, x often plays the role of model parameters θ and y the role
of observed data D. Bayes' theorem is the mechanism for Bayesian inference:
p(θ | D) ∝ p(D | θ) p(θ). All of Ch 9 (Bayesian linear regression) uses this directly.

---

## 6.4 Summary Statistics and Independence

Rather than working with full distributions, we often need compact descriptions.

### Expected value (mean)

```
Discrete:   E_X[g(X)] = Σₓ g(x) p(x)
Continuous: E_X[g(X)] = ∫ g(x) p(x) dx
```

The mean of X is μ = E[X]. Linearity of expectation always holds:
- E[αX + βY] = α E[X] + β E[Y]   (no independence required)

For a random vector **X**: μ = E[**X**] = (E[X₁], ..., E[Xₙ])ᵀ (applied componentwise).

### Variance

For scalar X with mean μ:
```
Var[X] = E[(X − μ)²] = E[X²] − (E[X])²
```

Standard deviation σ = √Var[X]. Units match those of X.

Useful identity (often easier to compute):
```
Var[X] = E[X²] − μ²
```

Variance of affine transformation:
```
Var[aX + b] = a² Var[X]    (constant shifts don't affect spread)
```

### Covariance

For two scalars X, Y:
```
Cov[X, Y] = E[(X − E[X])(Y − E[Y])] = E[XY] − E[X]E[Y]
```

- Cov[X, X] = Var[X]
- Positive: X and Y tend to move together
- Negative: X and Y tend to move in opposite directions
- Zero: no *linear* relationship (but nonlinear dependence may still exist)

### Covariance matrix Σ

For a random vector **X** ∈ ℝᵈ with mean **μ**:
```
Σ = Cov[X] = E[(X − μ)(X − μ)ᵀ] ∈ ℝᵈˣᵈ
```

Entry Σᵢⱼ = Cov[Xᵢ, Xⱼ]. The diagonal entries are the individual variances.

**Properties of Σ:**
- Symmetric: Σ = Σᵀ
- Positive semi-definite: xᵀΣx ≥ 0 for all x (≥ 0 because variance is non-negative)
- Strictly positive definite (non-singular) iff no component is a deterministic
  linear function of the others

This is why SPD matrices (from C3, C4) matter so much in ML — covariance matrices
ARE SPD matrices.

**Transformation rule:**
If **Y** = A**X** + **b** for a deterministic matrix A and vector b:
```
E[Y] = A E[X] + b = Aμ + b
Cov[Y] = A Cov[X] Aᵀ = AΣAᵀ
```

This formula appears constantly: every linear layer in a neural network transforms
the covariance of its input by AΣAᵀ.

### Correlation

Normalized covariance:
```
corr(X, Y) = Cov[X, Y] / (√Var[X] √Var[Y]) ∈ [−1, 1]
```

(The bound follows from Cauchy-Schwarz — see C3.)

Correlation = 1 means perfect positive linear relationship; −1 means perfectly
negative linear; 0 means uncorrelated (not necessarily independent).

### Independence

**X and Y are independent** iff:
```
p(x, y) = p(x) · p(y)    for all x, y
```

Equivalently: p(x | y) = p(x) — knowing Y tells you nothing about X.

**Key implications of independence:**
- E[XY] = E[X]E[Y]
- Cov[X, Y] = 0
- Var[X + Y] = Var[X] + Var[Y]

**Warning:** Cov[X,Y] = 0 does NOT imply independence (uncorrelated ≠ independent).
Independence is a much stronger condition — it eliminates ALL statistical dependence,
not just linear dependence. Exception: for joint Gaussians, zero correlation
*does* imply independence.

**Conditional independence:** X ⊥⊥ Y | Z iff p(x, y | z) = p(x | z) p(y | z).
This is the building block of graphical models (Ch 8).

---

## 6.5 Gaussian Distribution ⭐

The Gaussian is the single most important distribution in ML. It shows up because:
1. Central Limit Theorem: averages of any distribution converge to Gaussian
2. Maximum entropy: Gaussian has maximum entropy for a given mean and variance
3. Tractability: sums, marginals, conditionals of Gaussians are all Gaussian
4. Conjugacy: Gaussian prior × Gaussian likelihood = Gaussian posterior

### Univariate Gaussian

```
p(x | μ, σ²) = (1 / √(2πσ²)) exp(−(x − μ)² / (2σ²))
```

Notation: X ~ N(μ, σ²). Parameters:
- μ = mean (location of the peak)
- σ² = variance (width of the bell)
- σ = standard deviation

**Standard normal:** Z ~ N(0, 1). Any X ~ N(μ, σ²) can be standardized:
Z = (X − μ)/σ ~ N(0,1).

**68-95-99.7 rule:** approximately 68%/95%/99.7% of probability mass lies
within ±1/±2/±3 standard deviations of the mean.

### Multivariate Gaussian ⭐⭐

For **X** ∈ ℝᵈ:
```
p(x | μ, Σ) = (2π)^(−d/2) |Σ|^(−1/2) exp(−½ (x−μ)ᵀ Σ⁻¹ (x−μ))
```

Notation: **X** ~ N(**μ**, **Σ**) where:
- **μ** ∈ ℝᵈ — mean vector (center)
- **Σ** ∈ ℝᵈˣᵈ — covariance matrix (shape and orientation), must be SPD

**Geometric interpretation:**
The exponent (x−μ)ᵀΣ⁻¹(x−μ) is a squared *Mahalanobis distance* from x to μ.
The contours of constant density are ellipsoids in ℝᵈ. The eigenvectors of Σ
give the axes of the ellipsoid; the eigenvalues give the squared lengths.

**The normalizing constant** (2π)^(−d/2)|Σ|^(−1/2) ensures the density integrates to 1.
It involves |Σ|^(1/2) because larger Σ means the Gaussian is more spread out,
so the peak must be lower to normalize.

### Key properties of the multivariate Gaussian

#### 1. Marginals are Gaussian

Partition **X** = (**X**_a, **X**_b)ᵀ with:
```
μ = [μ_a]     Σ = [Σ_aa  Σ_ab]
    [μ_b]         [Σ_ba  Σ_bb]
```

The marginal distributions are:
```
p(x_a) = N(x_a | μ_a, Σ_aa)
p(x_b) = N(x_b | μ_b, Σ_bb)
```

Just read off the relevant block of the mean and the diagonal block of the covariance.
Marginalizing a multivariate Gaussian just means dropping the unwanted dimensions.

#### 2. Conditionals are Gaussian ⭐

This is the key result used in Bayesian linear regression (Ch 9) and Gaussian
processes (Ch 9, and implicitly in Ch 8):

```
p(x_a | x_b) = N(x_a | μ_{a|b}, Σ_{a|b})
```

where:
```
μ_{a|b} = μ_a + Σ_ab Σ_bb⁻¹ (x_b − μ_b)
Σ_{a|b} = Σ_aa − Σ_ab Σ_bb⁻¹ Σ_ba
```

**Intuition for μ_{a|b}:**
Start at μ_a, then correct by Σ_ab Σ_bb⁻¹(x_b − μ_b).
The term Σ_ab Σ_bb⁻¹ is a regression coefficient — it's how much we expect a_a
to shift per unit shift in x_b. The correction is proportional to how far x_b
is from its mean.

**Intuition for Σ_{a|b}:**
The conditional variance is the prior variance Σ_aa minus a non-negative term
Σ_ab Σ_bb⁻¹ Σ_ba. Conditioning always *reduces* variance — observing x_b
gives us information about x_a. The reduction is larger when the cross-covariance
Σ_ab is large (variables are more correlated).

The quantity Σ_aa − Σ_ab Σ_bb⁻¹ Σ_ba is the **Schur complement** of Σ_bb in Σ.

#### 3. Affine transformations are Gaussian

If **X** ~ N(**μ**, **Σ**) and **Y** = A**X** + **b**, then:
```
Y ~ N(Aμ + b, AΣAᵀ)
```

This is powerful: linear operations (projection, rotation, scaling, shifting)
preserve the Gaussian family. Combined with the sum and conditional rules, it
means we can do exact Bayesian inference in linear Gaussian models.

#### 4. Sums of independent Gaussians are Gaussian

If X ~ N(μ_x, σ_x²) and Y ~ N(μ_y, σ_y²) independently, then:
```
X + Y ~ N(μ_x + μ_y, σ_x² + σ_y²)
```

In the multivariate case: **X** ~ N(**μ_x**, **Σ_x**), **Y** ~ N(**μ_y**, **Σ_y**),
then **X** + **Y** ~ N(**μ_x** + **μ_y**, **Σ_x** + **Σ_y**).

#### 5. For Gaussians: uncorrelated = independent

This is the exception to the general rule. If **X** is jointly Gaussian and
Cov[Xᵢ, Xⱼ] = 0, then Xᵢ and Xⱼ are independent. This only works because
the Gaussian is fully characterized by first and second moments.

### The product of two Gaussians

This arises in Bayes' theorem when both likelihood and prior are Gaussian.
The product of two Gaussian densities is itself (proportional to) a Gaussian:

If p₁(x) = N(x | μ₁, σ₁²) and p₂(x) = N(x | μ₂, σ₂²), their product is:

```
p₁(x) · p₂(x) ∝ N(x | μ, σ²)
```

where:
```
1/σ² = 1/σ₁² + 1/σ₂²                 (precisions add)
μ = σ² (μ₁/σ₁² + μ₂/σ₂²)             (precision-weighted average of means)
```

Written with precisions τᵢ = 1/σᵢ²:
```
τ = τ₁ + τ₂                           (total precision = sum of precisions)
μ = (τ₁μ₁ + τ₂μ₂) / (τ₁ + τ₂)        (precision-weighted mean)
```

Intuition: if you have two independent Gaussian "measurements" of the same
quantity, your combined estimate has higher precision (narrower distribution)
than either alone, and the combined mean lies between the two, pulled toward
the more precise measurement.

### Why the Gaussian is so central to Part II

| Application | Where the Gaussian appears |
|-------------|---------------------------|
| Ch 8 — Probabilistic modeling | Joint distributions over latent + observed |
| Ch 9 — Bayesian linear regression | Gaussian prior on weights, Gaussian noise, Gaussian posterior |
| Ch 10 — PCA | Gaussian assumption justifies ML in PCA derivation |
| Ch 11 — Density estimation | Gaussian mixture models (GMMs) |
| Ch 12 — Classification | Gaussian class-conditional densities in LDA |

---

## 6.6 Conjugate Priors and the Exponential Family

### Why conjugacy matters

In Bayesian inference, we want to compute the posterior p(θ | x) ∝ p(x | θ) p(θ).
In general, this requires a difficult integral to normalize. However, if the prior
and likelihood are chosen from a compatible pair, the posterior has the **same
functional form** as the prior — just with updated parameters.

This is called a **conjugate prior**. The payoff: exact, closed-form posterior
updates. No sampling, no approximation.

The exponential family provides the systematic framework for identifying conjugate pairs.

### The exponential family

A distribution belongs to the exponential family if its density can be written as:

```
p(x | η) = h(x) exp(ηᵀ φ(x) − A(η))
```

where:
- **η** — natural parameters (the "canonical" parameterization)
- **φ(x)** — sufficient statistics (the features of x that matter for inference)
- **h(x)** — base measure (does not depend on η)
- **A(η)** — log-partition function (log of the normalizing constant)

The name "sufficient statistics" comes from the Fisher-Neyman factorization theorem:
φ(x) contains ALL the information in x relevant to estimating η. Once you know
φ(x), the raw data x adds nothing.

**Why A(η) is important:**
A(η) = log ∫ h(x) exp(ηᵀφ(x)) dx
- Ensures the distribution normalizes to 1
- Its gradient gives the mean of the sufficient statistics: ∇_η A(η) = E[φ(X)]
- Its Hessian gives the covariance: ∇²_η A(η) = Cov[φ(X)]
- A(η) is always convex (since its Hessian is a covariance matrix, hence PSD)

**Members of the exponential family:**
- Bernoulli / Binomial
- Multinomial
- Poisson
- Gaussian (both mean and variance parameterized; or just mean with known variance)
- Gamma, Beta, Dirichlet
- Laplace (with known mean)
- Wishart / inverse-Wishart

Many common distributions are in this family — which is one reason the exponential
family is so tractable.

### Beta-Binomial conjugacy

**Binomial likelihood:** X ~ Bin(n, μ) — number of successes in n coin flips.
Natural parameter η = log(μ/(1−μ)) (log-odds). In standard form:
```
p(x | μ) ∝ μˣ (1−μ)ⁿ⁻ˣ
```

**Beta prior:** μ ~ Beta(α, β):
```
p(μ | α, β) ∝ μ^(α−1) (1−μ)^(β−1)
```

Hyperparameters α, β > 0 control shape:
- α = β = 1: uniform over [0,1]
- α > β: prior mass above 0.5 (biased toward heads)
- Large α, β: strongly concentrated (confident prior)
- Think of α−1 as "prior successes" and β−1 as "prior failures"

**Posterior update:** After observing x successes in n trials:
```
p(μ | x) ∝ μˣ(1−μ)ⁿ⁻ˣ · μ^(α−1)(1−μ)^(β−1) = μ^(α+x−1)(1−μ)^(β+n−x−1)
```

This is Beta(α + x, β + n − x). The update rule:
```
α_new = α + x          (prior successes + observed successes)
β_new = β + (n − x)    (prior failures + observed failures)
```

**Intuition:** The Beta distribution acts as a "pseudo-count" prior. Each observation
just increments the appropriate count. As n grows, the data overwhelms the prior.

**Posterior predictive:** The probability of heads in the next flip:
```
E[μ | x] = (α + x) / (α + β + n)
```

This is a weighted average between the prior mean α/(α+β) and the MLE x/n.

### Gaussian-Gaussian conjugacy

**Gaussian likelihood with known variance:** X | μ ~ N(μ, σ²), σ² known.
**Gaussian prior:** μ ~ N(μ₀, σ₀²).

After observing x:
```
p(μ | x) ∝ N(x | μ, σ²) · N(μ | μ₀, σ₀²)
```

Using the product-of-Gaussians formula from §6.5:
```
posterior: μ | x ~ N(μ_n, σ_n²)

where:
  1/σ_n² = 1/σ₀² + 1/σ²           (precisions add)
  μ_n = σ_n² (μ₀/σ₀² + x/σ²)      (precision-weighted mean)
```

For n iid observations x₁,...,xₙ with sample mean x̄:
```
  1/σ_n² = 1/σ₀² + n/σ²
  μ_n = σ_n² (μ₀/σ₀² + nx̄/σ²)
```

As n → ∞: posterior mean → x̄ (MLE), posterior variance → 0 (certainty).

**Intuition:** Posterior precision = prior precision + data precision.
More data → tighter posterior. The posterior mean is a weighted compromise
between prior belief and data, with weights proportional to precision (1/variance).

### Sufficient statistics and the link to ML

In the exponential family, the MLE of η is found by solving:
```
∇_η A(η) = (1/n) Σᵢ φ(xᵢ)
```

Meaning: fit the model so that the expected sufficient statistics match the
empirical sufficient statistics. For a Gaussian, this gives the sample mean and
covariance. For logistic regression (Bernoulli), the sufficient statistic is
the feature vector x, and this equation gives the moment-matching condition.

---

## 6.7 Change of Variables / Inverse Transform

### The change-of-variables formula

If X has density p_X(x) and Y = g(X) is a monotone transformation, then Y has density:

```
p_Y(y) = p_X(g⁻¹(y)) · |d/dy g⁻¹(y)|
```

Or equivalently: p_Y(y) = p_X(x) · |dx/dy|.

The factor |dx/dy| is the **Jacobian correction** — it accounts for the stretching
or squishing of probability mass under the transformation.

**Intuition:** probability mass is conserved. If the transformation stretches a region
by a factor of 2, the density must halve (same mass, twice the area).

### Multivariate change of variables

For a bijective transformation **y** = g(**x**) from ℝᵈ → ℝᵈ:

```
p_Y(y) = p_X(g⁻¹(y)) · |det J_{g⁻¹}(y)|
```

where J_{g⁻¹} is the Jacobian matrix of the inverse transformation:
(J_{g⁻¹})ᵢⱼ = ∂[g⁻¹(y)]ᵢ / ∂yⱼ.

Equivalently: p_X(x) = p_Y(g(x)) · |det J_g(x)|.

**Why the determinant?** In d dimensions, the Jacobian determinant measures how
much the transformation stretches/squishes d-dimensional volume — the d-dimensional
analogue of |dx/dy|. This is directly related to det(A) from C2.

### Inverse transform sampling

A key application: how to draw samples from any CDF F_X.

**Algorithm:**
1. Draw U ~ Uniform[0,1]
2. Return X = F_X⁻¹(U)

**Why it works:** P(F_X⁻¹(U) ≤ x) = P(U ≤ F_X(x)) = F_X(x). ✓

**Limitation:** Requires computing F_X⁻¹ analytically, which is not always possible.
For the Gaussian, this requires numerical methods (the error function erf is not
analytically invertible). Box-Muller and reparameterization tricks (important in
VAEs) are alternatives.

### Connection to normalizing flows

This section is the foundation for **normalizing flows** — a class of deep generative
models that chain together invertible transformations to transform a simple base
distribution (usually Gaussian) into a complex distribution. Each step uses the
change-of-variables formula to track the density through the transformation.
Though not covered in MML, this is a direct application of §6.7.

---

## Key Formulas Quick Reference

| Concept | Formula |
|---------|---------|
| Conditional probability | P(A\|B) = P(A∩B)/P(B) |
| Product rule | p(x,y) = p(y\|x)p(x) |
| Sum rule (marginalization) | p(x) = ∫ p(x,y) dy |
| Bayes' theorem | p(x\|y) = p(y\|x)p(x) / p(y) |
| Expected value | E[g(X)] = ∫ g(x)p(x) dx |
| Variance | Var[X] = E[X²] − (E[X])² |
| Covariance | Cov[X,Y] = E[XY] − E[X]E[Y] |
| Covariance matrix | Σ = E[(X−μ)(X−μ)ᵀ] |
| Affine transform mean | E[AX+b] = Aμ+b |
| Affine transform cov | Cov[AX+b] = AΣAᵀ |
| Univariate Gaussian | N(x\|μ,σ²) = (2πσ²)^(−½) exp(−(x−μ)²/2σ²) |
| Multivariate Gaussian | N(x\|μ,Σ) = (2π)^(−d/2)\|Σ\|^(−½) exp(−½(x−μ)ᵀΣ⁻¹(x−μ)) |
| Gaussian marginal | X_a ~ N(μ_a, Σ_aa) |
| Gaussian conditional mean | μ_{a\|b} = μ_a + Σ_ab Σ_bb⁻¹(x_b − μ_b) |
| Gaussian conditional cov | Σ_{a\|b} = Σ_aa − Σ_ab Σ_bb⁻¹ Σ_ba |
| Exponential family | p(x\|η) = h(x) exp(ηᵀφ(x) − A(η)) |
| Beta-Binomial update | Beta(α,β) + x successes/n trials → Beta(α+x, β+n−x) |
| Gaussian precision update | 1/σ_n² = 1/σ₀² + n/σ² |
| Change of variables | p_Y(y) = p_X(g⁻¹(y)) \|det J_{g⁻¹}(y)\| |

---

## Connections to Other Chapters

| Concept from C6 | Where it shows up |
|-----------------|-------------------|
| Bayes' theorem | C8 (probabilistic generative models), C9 (Bayesian regression), C11 (EM algorithm for GMMs) |
| Multivariate Gaussian | C9 (Gaussian process regression), C10 (probabilistic PCA), C11 (GMMs), C12 (LDA) |
| Gaussian conditionals | C9 (Bayesian linear regression posterior), predictive distributions everywhere in Part II |
| Gaussian marginals | C11 (marginalization in mixture models), any latent variable model |
| Covariance matrix Σ | C4 (eigendecomposition of Σ = PCA), C10 (principal components) |
| AΣAᵀ transform rule | C9 (propagating uncertainty through linear models) |
| Independence | C8 (conditional independence = graphical model structure) |
| Exponential family | C9 (generalized linear models), Bayesian statistics broadly |
| Conjugate priors | C9 (Bayesian linear regression with Gaussian-Gaussian conjugacy), C11 (Dirichlet-Multinomial for GMMs) |
| Change of variables | C11 (reparameterization trick used in variational inference), normalizing flows |
| Sufficient statistics | Maximum likelihood estimation throughout Part II |
| Mahalanobis distance | C12 (distance-based classifiers, anomaly detection) |

**From earlier chapters feeding in:**
- C2: Matrix operations (ΣAᵀ, Σ⁻¹), rank, SPD matrices
- C3: SPD matrices (covariance must be PSD), Cauchy-Schwarz (bounds correlation)
- C4: Eigendecomposition of Σ reveals geometry of the Gaussian ellipsoids
- C5: Jacobian (appears explicitly in change of variables)

---

## Open Questions

- How does the Mahalanobis distance (x−μ)ᵀΣ⁻¹(x−μ) connect to the notion of
  distance from C3? (It is the distance induced by the inner product ⟨a,b⟩ = aᵀΣ⁻¹b.)
- What happens to the Gaussian conditional formula when Σ_bb is singular?
  (The Moore-Penrose pseudoinverse replaces Σ_bb⁻¹ — see C4.)
- The exponential family log-partition function A(η) is convex — does this connect
  to convex optimization (C7)? (Yes: maximum likelihood in the exponential family
  is always a convex problem.)
- Why does the posterior variance Σ_{a|b} not depend on the observed value x_b?
  (Specific to the Gaussian: variance is a global property, not affected by where
  you condition. Non-Gaussian conditionals do not have this property.)
- Normalizing flows chain change-of-variables steps — how do you ensure each
  transformation is invertible and has a tractable Jacobian determinant?
  (Autoregressive and coupling-layer architectures; beyond MML scope.)
- How is the Wishart distribution (the matrix generalization of the Gamma) a
  conjugate prior for the Gaussian precision matrix Σ⁻¹? (Used in full Bayesian
  Gaussian models where both μ and Σ are unknown.)
