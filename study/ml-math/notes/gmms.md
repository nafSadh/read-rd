# C11: Density Estimation with Gaussian Mixture Models — Study Notes

> A single Gaussian is rarely rich enough to describe real data.
> GMMs solve this by superimposing K Gaussians, each with its own mean and covariance,
> weighted so they sum to a valid probability density. The chapter shows how to fit those
> weights from data — which forces us to confront the EM algorithm, the latent-variable
> perspective, and the principled trade-off between model complexity and fit.

**Primary source:** MML Ch 11 (pp 348–368)
**Supplementary:**
- [3Blue1Brown: But what is a neural network? (intuition for mixture models)](https://www.youtube.com/watch?v=aircAruvnKk)
- [Stanford CS229 EM Algorithm notes (Andrew Ng)](http://cs229.stanford.edu/notes2021fall/cs229-notes7b.pdf)
- [Bishop PRML §9.2–9.3](https://www.microsoft.com/en-us/research/uploads/prod/2006/01/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf)
- [Scikit-learn GaussianMixture docs (with visual examples)](https://scikit-learn.org/stable/modules/mixture.html)

---

## Chapter Structure at a Glance

C11 motivates, defines, and fits Gaussian Mixture Models through four tightly coupled sections:

1. **§11.1** — Gaussian Mixture Model: the generative recipe (weighted sum of Gaussians)
2. **§11.2** — Maximum Likelihood: why naive gradient ascent breaks, and why EM is needed
3. **§11.3** — EM Algorithm ⭐: the alternating E/M-step procedure and its convergence guarantee
4. **§11.4** — Latent Variable Perspective: ELBO, Jensen's inequality, EM as coordinate ascent
5. **§11.5** — Density Estimation: GMMs as universal density approximators, model selection via BIC

The conceptual thread: the latent variable z (§11.4) is the key that unlocks EM (§11.3) —
once you accept that each data point secretly "belongs" to one component, the M-step
update equations follow directly from weighted Gaussian MLE.

---

## Reading Notes

### 11.1 Gaussian Mixture Model

**The core idea:** model a complex, multi-modal distribution p(x) as a weighted sum of
K simple Gaussian distributions. Each Gaussian component k has its own mean μₖ, covariance
Σₖ, and mixture weight πₖ.

**Mixture density:**
```
p(x) = Σₖ₌₁ᴷ πₖ N(x | μₖ, Σₖ)
```
where N(x | μₖ, Σₖ) is the multivariate Gaussian density.

**Constraints on mixture weights:**
```
πₖ ≥ 0   for all k = 1, ..., K
Σₖ πₖ = 1
```
These constraints ensure p(x) integrates to 1 and is a valid probability density.

**Parameters:** A GMM with K components in D dimensions has:
- K means μₖ ∈ ℝᴰ
- K covariance matrices Σₖ ∈ ℝᴰˣᴰ (symmetric positive definite)
- K-1 free mixture weights (the K-th is determined by the sum-to-one constraint)

**The latent variable z:** The GMM has an elegant generative story involving a discrete
latent variable z ∈ {1, ..., K} that encodes which component generated a data point:

```
p(z = k) = πₖ                         (prior over components)
p(x | z = k) = N(x | μₖ, Σₖ)          (component likelihood)
```

The observed density is recovered by marginalizing out z:
```
p(x) = Σₖ p(x | z=k) p(z=k) = Σₖ πₖ N(x | μₖ, Σₖ)
```

**Generative sampling procedure:**
1. Draw a component index: z ~ Categorical(π₁, ..., πₖ)
2. Draw the data point from that component: x | z=k ~ N(μₖ, Σₖ)

This generative view is what makes EM work — z is unobserved but we can reason about
its posterior given x.

**Why K > 1 is needed:** A single Gaussian is unimodal and symmetric. Real data is often
multi-modal (e.g., heights of men and women), skewed, or cluster-structured. K = 2 GMM
already captures bimodal structure; larger K can approximate any smooth density.

**Special cases:**
- K = 1: reduces to a single Gaussian N(x | μ, Σ)
- Equal covariances Σₖ = σ²I: spherical, isotropic clusters (like soft K-means)
- Diagonal Σₖ: axis-aligned ellipsoids, fewer parameters than full covariance

---

### 11.2 Parameter Learning via Maximum Likelihood

**Given:** a dataset X = {x₁, ..., xₙ} of N i.i.d. observations from an unknown density.
**Goal:** find θ = {μₖ, Σₖ, πₖ}ₖ₌₁ᴷ that maximizes the likelihood of the data.

**Log-likelihood:**
```
ℓ(θ) = Σₙ₌₁ᴺ log p(xₙ | θ)
      = Σₙ₌₁ᴺ log [ Σₖ₌₁ᴷ πₖ N(xₙ | μₖ, Σₖ) ]
```

**The fundamental difficulty: log of a sum.** For a single Gaussian, the log-likelihood
is concave and setting the gradient to zero gives closed-form MLE. But here the log sits
outside a sum over K terms. Setting ∂ℓ/∂μₖ = 0 gives:
```
∂ℓ/∂μₖ = Σₙ [ πₖ N(xₙ|μₖ,Σₖ) / Σⱼ πⱼ N(xₙ|μⱼ,Σⱼ) ] Σₖ⁻¹(xₙ - μₖ) = 0
```
The term in brackets appears in the update for μₖ but depends on μₖ itself — the
equations are coupled and have no closed-form solution.

**Why not gradient ascent directly?**
- The log-likelihood is non-convex with many local maxima
- Covariance matrices must remain positive definite (a constrained optimization)
- The mixture weights must satisfy the simplex constraint Σπₖ = 1
- EM provides a structured, constraint-respecting iterative scheme that is simpler
  and more numerically stable than projected gradient methods

**Singularity / degeneracy issue:** If one component collapses onto a single data point,
the likelihood blows up to infinity (the Gaussian becomes a delta function). This is a
pathological maximum that EM avoids in practice through careful initialization, but it
is a theoretical limitation of pure MLE for GMMs.

---

### 11.3 EM Algorithm for GMMs ⭐

The EM (Expectation-Maximization) algorithm alternates between two steps, guaranteed
to increase (or maintain) the log-likelihood at every iteration.

**Key quantity: responsibility.** The responsibility rₙₖ is the posterior probability
that component k "generated" data point xₙ:

```
rₙₖ = p(z=k | xₙ) = πₖ N(xₙ|μₖ,Σₖ) / Σⱼ πⱼ N(xₙ|μⱼ,Σⱼ)
```

By Bayes' theorem: prior πₖ times likelihood N(xₙ|μₖ,Σₖ), normalized over all K
components. The responsibilities form a soft assignment: rₙₖ ∈ [0,1], Σₖ rₙₖ = 1.

**Effective count:**
```
Nₖ = Σₙ₌₁ᴺ rₙₖ
```
Nₖ is the "effective number of data points assigned to component k". Note Σₖ Nₖ = N.

---

**E-step (Expectation):** Given current parameters θᵒˡᵈ = {μₖ, Σₖ, πₖ}, compute
the responsibilities for every (n, k) pair:

```
rₙₖ ← πₖ N(xₙ | μₖ, Σₖ) / Σⱼ₌₁ᴷ πⱼ N(xₙ | μⱼ, Σⱼ)
```

This step computes the posterior distribution over the latent variables z given the
observed data and current parameters. No parameters are updated here.

---

**M-step (Maximization):** Given the responsibilities {rₙₖ}, update parameters to
maximize the expected complete-data log-likelihood:

```
μₖ  ← (1/Nₖ) Σₙ₌₁ᴺ rₙₖ xₙ                               (weighted mean)

Σₖ  ← (1/Nₖ) Σₙ₌₁ᴺ rₙₖ (xₙ - μₖ)(xₙ - μₖ)ᵀ              (weighted covariance)

πₖ  ← Nₖ / N                                               (weight = fraction of data)
```

Each formula is the standard Gaussian MLE formula but with data points weighted by
their responsibility rₙₖ. Data points closer to component k's mean get higher weight.

---

**Full EM procedure:**

```
1. Initialize: choose K, set initial {μₖ, Σₖ, πₖ} (e.g., random or from K-means)
2. Repeat until convergence:
   a. E-step: compute rₙₖ for all n, k using current parameters
   b. M-step: update μₖ, Σₖ, πₖ using rₙₖ
   c. Evaluate log-likelihood ℓ(θ); check for convergence
3. Return final parameters
```

**Convergence guarantee:** The log-likelihood ℓ(θ) is non-decreasing at every EM iteration.
It converges to a local maximum (or saddle point). Global maximum is not guaranteed —
multiple random restarts are used in practice to find a good solution.

---

**Connection to K-means (hard vs. soft assignment):**

K-means can be seen as the limiting case of EM for GMMs with:
- All covariances equal and spherical: Σₖ = σ²I (same for all k)
- Taking the limit σ² → 0

In this limit, responsibilities become "hard" assignments:
```
rₙₖ → 1  if k = argmin‖xₙ - μₖ‖²    (the nearest cluster)
rₙₖ → 0  otherwise
```
The M-step mean update becomes the ordinary cluster mean (unweighted). EM for GMMs is
"soft K-means" — every point contributes to every cluster, just with fractional weight.

| Property | K-means | EM for GMMs |
|---|---|---|
| Assignment | Hard (0 or 1) | Soft (rₙₖ ∈ [0,1]) |
| Cluster shape | Spherical | Arbitrary ellipsoid |
| Covariance | Implicit, σ²I | Learned per cluster |
| Uncertainty | None | Posterior probabilities |
| Objective | Sum of squared distances | Log-likelihood |

---

### 11.4 Latent Variable Perspective

This section gives the theoretical foundation for why EM works and generalizes it
beyond GMMs.

**Why marginalizing z causes the problem:** The log-likelihood involves
log Σₖ p(x,z=k | θ), a log of a sum. If z were observed, the "complete-data"
log-likelihood would be log Σₖ [zₙ=k] log N(xₙ|μₖ,Σₖ) — separable over k, with
closed-form solutions.

**Jensen's inequality:** For any concave function f (log is concave) and any
distribution q(z):
```
log Σₖ q(z=k) [p(x,z=k)/q(z=k)] ≥ Σₖ q(z=k) log [p(x,z=k)/q(z=k)]
```
That is: log E_q[g(z)] ≥ E_q[log g(z)].

**The ELBO (Evidence Lower BOund):** Applying Jensen's inequality to the log-likelihood:
```
log p(x | θ) ≥ Σₖ q(z=k) log [p(x, z=k | θ) / q(z=k)]   =: ELBO(q, θ)
```
The ELBO is a lower bound on the log-likelihood for any choice of variational distribution q.
The gap between the ELBO and log p(x|θ) equals the KL divergence KL(q ‖ p(z|x,θ)).

**EM as coordinate ascent on the ELBO:**
- **E-step:** maximize ELBO over q (holding θ fixed). The optimal q is the posterior:
  q*(z=k) = p(z=k | x, θ) — which makes the KL divergence zero, so ELBO = log-likelihood.
  For GMMs, this is exactly the responsibility computation.
- **M-step:** maximize ELBO over θ (holding q fixed). For GMMs this yields the weighted
  mean/covariance/weight updates in closed form.

Each full iteration (E then M) increases the ELBO, hence the log-likelihood is non-decreasing.

**Decomposition:**
```
log p(x | θ) = ELBO(q, θ) + KL(q(z) ‖ p(z|x, θ))
```
Since KL ≥ 0, ELBO ≤ log-likelihood always. The E-step tightens the bound (KL→0);
the M-step increases the bound itself.

**Generality:** The ELBO / EM framework extends to any latent variable model: hidden
Markov models, probabilistic PCA, variational autoencoders, etc. The GMM case is the
cleanest worked example because the posterior p(z|x) is tractable.

---

### 11.5 GMMs for Density Estimation

**Universal approximation of densities:** Any smooth probability density on ℝᴰ
can be approximated arbitrarily well by a GMM with enough components K. The smoothness
of the individual Gaussians is inherited by the mixture.

**Choosing K in practice:** K is a hyperparameter that controls model complexity.
- Too small: underfitting — the model misses structure in the data
- Too large: overfitting — spurious clusters, degenerate solutions, long training time

**Bayesian Information Criterion (BIC) for model selection:**
```
BIC(K) = -2 ℓ(θ̂) + p(K) log N
```
where:
- ℓ(θ̂) is the maximized log-likelihood (using EM)
- p(K) is the number of free parameters for a K-component model
- N is the number of data points

The BIC penalizes model complexity. Choose K that minimizes BIC.

**Number of free parameters for a GMM in D dimensions:**
```
p(K) = K · D         (means)
     + K · D(D+1)/2  (covariance matrices, symmetric)
     + (K-1)         (mixture weights, one is determined)
```
For full covariances. Diagonal covariances reduce the middle term to K·D.

**Why not AIC?** AIC uses a penalty of 2p(K) rather than p(K) log N. For large N,
BIC penalizes complexity more strongly and tends to select simpler models. Both
criteria are used; BIC is more common for density estimation.

**Practical workflow for density estimation with GMMs:**
```
For K in {1, 2, 3, ..., Kmax}:
  1. Run EM (multiple restarts) to get θ̂_K
  2. Compute BIC(K)
Select K* = argmin BIC(K)
Use the GMM with K* components as the density estimate
```

**Limitations of GMM density estimation:**
- Requires choosing K (cross-validation or BIC help but don't eliminate the ambiguity)
- All components are Gaussian — cannot capture heavy-tailed or skewed sub-populations well
  without many components
- EM finds local optima; results depend on initialization
- Curse of dimensionality: in high D, covariance estimation requires many data points
  (diagonal or tied covariances help)

---

## Key Formulas Quick Reference

| Concept | Formula | Note |
|---------|---------|------|
| Mixture density | p(x) = Σₖ πₖ N(x\|μₖ,Σₖ) | K components |
| Weight constraints | πₖ ≥ 0, Σₖ πₖ = 1 | Simplex constraint |
| Component prior | p(z=k) = πₖ | Discrete distribution |
| Component likelihood | p(x\|z=k) = N(x\|μₖ,Σₖ) | |
| Marginal (generative) | p(x) = Σₖ p(x\|z=k)p(z=k) | Marginalizes out z |
| Log-likelihood | ℓ(θ) = Σₙ log Σₖ πₖ N(xₙ\|μₖ,Σₖ) | No closed form |
| Responsibility (E-step) | rₙₖ = πₖN(xₙ\|μₖ,Σₖ) / Σⱼ πⱼN(xₙ\|μⱼ,Σⱼ) | Posterior p(z=k\|xₙ) |
| Effective count | Nₖ = Σₙ rₙₖ | "Soft" cluster size |
| Mean update (M-step) | μₖ = (1/Nₖ) Σₙ rₙₖ xₙ | Weighted mean |
| Covariance update (M-step) | Σₖ = (1/Nₖ) Σₙ rₙₖ (xₙ-μₖ)(xₙ-μₖ)ᵀ | Weighted cov |
| Weight update (M-step) | πₖ = Nₖ/N | Fraction of data |
| ELBO | Σₖ q(z=k) log[p(x,z=k\|θ)/q(z=k)] | Lower bound on log p(x) |
| BIC | -2ℓ(θ̂) + p(K) log N | Model selection |
| Parameters per GMM | K·D + K·D(D+1)/2 + (K-1) | Full covariances |

---

## Key Connections to Other Chapters

| Concept in C11 | Relevant chapter |
|----------------|-----------------|
| Multivariate Gaussian N(x\|μ,Σ) | C6 §6.5 — definition, properties, marginals, conditionals |
| Conjugate priors (Bayesian GMM) | C6 §6.6 — Dirichlet prior on π, Normal-Wishart on (μₖ,Σₖ) |
| MLE derivations, information criteria | C8 §8.3 — MLE principle; model selection trade-offs |
| Cholesky for Σₖ | C4 §4.3 — numerically stable covariance representation; sampling |
| Eigendecomposition of Σₖ | C4 §4.4 — ellipsoid axes; checking SPD; visualizing clusters |
| EM as coordinate ascent | C7 §7.1 — optimization by alternating over parameter subsets |
| Jensen's inequality (ELBO) | C6 (Jensen appears in information-theoretic derivations) |
| Low-rank Σₖ | C4 §4.6 — factor analysis / probabilistic PCA uses rank-r covariances |
| Variational inference (ELBO) | C9 (Bayesian linear regression hints at variational methods) |
| Latent variables, marginalization | C8 §8.4 — Bayesian inference marginalizes over parameters |
| K-means as limit of GMM-EM | C12 — classification / clustering chapter builds on GMM intuition |

**From C4 feeding in:**
Fitting a GMM requires repeatedly computing and inverting D×D covariance matrices Σₖ.
In practice: represent Σₖ = LₖLₖᵀ (Cholesky) for stable inversion; use the spectral
decomposition Σₖ = QₖΛₖQₖᵀ to visualize cluster ellipsoids.

**From C6 feeding in:**
The multivariate Gaussian N(x|μ,Σ) is the building block. All properties needed —
normalization, the exponent form, marginals — come directly from C6.

**From C8 feeding in:**
MLE (C8 §8.3) sets up the optimization objective. BIC (§11.5) is a direct consequence
of the Bayesian model evidence approximation (C8). The tension between fit and complexity
is the core of Bayesian model selection.

---

## Open Questions

- Why does EM guarantee non-decreasing likelihood but not find the global maximum?
  (Each step increases the ELBO which is a lower bound on the likelihood. But the
   likelihood is non-convex with multiple peaks — EM finds the nearest local maximum
   from the initialization. Multiple restarts explore different basins.)

- When do GMM covariances become degenerate during EM, and how is it prevented?
  (If a component absorbs very few points, Σₖ → 0 and the likelihood blows up.
   Fixes include: adding a regularization λI to Σₖ, enforcing a minimum covariance,
   or using a Bayesian prior (Normal-Wishart) that prevents collapse.)

- What is the relationship between the ELBO in §11.4 and variational inference in
  deep generative models like VAEs?
  (VAEs generalize the ELBO to non-Gaussian likelihoods and amortize the E-step with
   a neural encoder q_φ(z|x) instead of computing the exact posterior. Same Jensen
   lower bound, different parameterization of q.)

- Why does BIC outperform AIC for GMM model selection in the large-N regime?
  (BIC's penalty p(K) log N grows with N, matching the Bayesian evidence approximation.
   AIC's constant penalty 2p(K) overfits as N grows — it doesn't "know" more data means
   complexity is riskier. BIC is asymptotically consistent for model selection; AIC is not.)

- Can we choose K without any held-out data?
  (Yes: BIC uses only the training data. But cross-validation log-likelihood is more
   reliable in practice. Nonparametric Bayesian methods — Dirichlet process GMMs — let
   K grow with the data, avoiding the choice entirely.)
