# C8: When Models Meet Data — Study Notes

> Data is observed; models are assumed; parameters are learned.
> This chapter builds the complete pipeline from raw observations to principled
> decisions: how to write down a model, how to fit it to data, how to reason
> about uncertainty, and how to choose between competing model structures.
> The unifying thread is probability: every step — fitting, inference, selection —
> is an act of probabilistic reasoning.

**Primary source:** MML Ch 8 (pp 251–288)
**Supplementary:**
- [3Blue1Brown: Bayes theorem](https://www.youtube.com/watch?v=HZGCoVF3YvM)
- [Seeing Theory — Bayesian Inference (Brown Univ.)](https://seeing-theory.brown.edu/bayesian-inference/)
- [Bishop PRML Ch 1 & 3](https://www.microsoft.com/en-us/research/people/cmbishop/) — deeper treatment of generalization and Bayesian model comparison
- [Jake VanderPlas: Frequentism and Bayesianism (blog series)](https://jakevdp.github.io/blog/2014/03/11/frequentism-and-bayesianism-a-practical-intro/)

---

## Chapter Structure at a Glance

C8 is the conceptual hub of Part II — it introduces the vocabulary that all of
Chapters 9–12 will use in specific settings:

1. **§8.1** — Data, Models, Learning: the three-way vocabulary
2. **§8.2** — Empirical Risk Minimization (ERM): the optimization view of learning
3. **§8.3** — Parameter Estimation: MLE — the frequentist workhorse
4. **§8.4** — Probabilistic Modeling and Inference: the Bayesian view, MAP, and predictive distributions
5. **§8.5** — Directed Graphical Models: Bayesian networks and conditional independence
6. **§8.6** — Model Selection: how to compare models using marginal likelihood and BIC

The conceptual arc: §8.2 sets up learning as minimizing a loss over observed data;
§8.3 shows MLE is a special case of that; §8.4 adds a prior to MLE to get MAP and
full Bayesian inference; §8.5 gives notation for complex joint distributions; §8.6
uses all of the above to choose between model families.

---

## Reading Notes

### 8.1 Data, Models, and Learning

The chapter opens by defining the three pillars that every ML problem rests on:

**Data:** A training set of N pairs
```
D = {(x_1, y_1), ..., (x_N, y_N)}
```
where x_i ∈ R^D is the input (feature vector) and y_i is the target (label or
real value). The core assumption is that D is drawn i.i.d. from some true but
unknown joint distribution p*(x, y).

**Models:** A parameterized family of functions or distributions indexed by θ:
```
f: R^D × Θ → Y      (discriminative / predictor view)
p(y | x, θ)         (probabilistic view)
```
The model is our hypothesis about the mechanism that generated y given x. Different
model families (linear, neural network, GP) impose different structural assumptions.

**Learning:** Finding the θ that makes the model "fit" the data as well as possible,
according to some criterion. The criterion is the loss function.

**Loss function** ℓ(y_hat, y): measures how wrong a single prediction y_hat is
relative to the true target y. Common examples:
```
Squared loss:        ℓ(y_hat, y) = (y_hat - y)^2
Absolute loss:       ℓ(y_hat, y) = |y_hat - y|
Binary cross-entropy: ℓ(y_hat, y) = -[y log y_hat + (1-y) log(1-y_hat)]
0-1 loss:            ℓ(y_hat, y) = 1[y_hat ≠ y]
```

**Cost / Risk:** The aggregate performance over all data. Two versions:
```
Expected risk (true risk):   R(θ) = E_{(x,y)~p*}[ℓ(f(x,θ), y)]
Empirical risk:              R_emp(θ) = (1/N) Σ_{i=1}^{N} ℓ(f(x_i,θ), y_i)
```
We cannot compute R(θ) because p* is unknown. We minimize R_emp(θ) instead.

**Key intuition:** The model is not the truth — it is a useful fiction that compresses
data into parameters. All of statistics and ML is about navigating the gap between
the fiction (model) and the real world (p*).

---

### 8.2 Empirical Risk Minimization (ERM)

**Empirical Risk Minimization (ERM)** is the formal statement of "fit the model to the data":
```
θ* = argmin_θ R_emp(θ) = argmin_θ (1/N) Σ_{i=1}^{N} ℓ(f(x_i, θ), y_i)
```
This is the defining equation of supervised learning. Most learning algorithms are
special cases of ERM with different choices of f, ℓ, and possibly a regularizer.

**Regularized ERM:**
```
θ* = argmin_θ [ (1/N) Σ_{i=1}^{N} ℓ(f(x_i, θ), y_i)  +  λ R(θ) ]
```
where R(θ) is a regularizer (e.g., ‖θ‖^2 for ridge, ‖θ‖_1 for lasso) and λ ≥ 0
controls the strength. Regularization corresponds, in the Bayesian view, to a prior on θ
(see §8.4).

**Generalization gap:**
```
generalization gap = R(θ) - R_emp(θ)
```
Because we minimize R_emp rather than R, the gap measures how much better we look
on training data than on new data. Large generalization gap = overfitting.

**Overfitting:** The model captures noise in D rather than the true signal. Symptoms:
- Very low training loss, high test loss
- High model complexity (too many parameters relative to N)
- Large generalization gap

**Underfitting:** The model is not expressive enough to capture the true signal.
Symptoms:
- High training loss, high test loss
- Low model complexity (too few parameters)

**Bias-variance tradeoff:** For squared loss, the expected test error of a predictor f_hat
trained on a random training set D can be decomposed as:
```
E_D[(y - f_hat(x))^2] = Bias(f_hat(x))^2  +  Var(f_hat(x))  +  noise^2
```
where:
```
Bias(f_hat(x))  = E_D[f_hat(x)] - f*(x)      (systematic error — underfitting)
Var(f_hat(x))   = E_D[(f_hat(x) - E_D[f_hat(x)])^2]   (sensitivity to D — overfitting)
noise^2         = Var_{p*}[y | x]              (irreducible, from data stochasticity)
```

Three observations:
1. Increasing model complexity typically decreases bias but increases variance.
2. The optimal complexity minimizes bias² + variance; this is not achieved by
   always choosing the most or least complex model.
3. The noise² term is a floor — no model can do better than Bayes error.

**Worked example — polynomial regression:**
Fit degree-d polynomials to N = 10 points from y = sin(x) + ε:
- d = 1 (linear): high bias, low variance — underfits the curve
- d = 9 (degree-9 poly): zero training error, wild oscillations on test set — overfits
- d = 3 (cubic): reasonable fit — balances bias and variance

**How to control the tradeoff:**
1. Regularization (penalize large θ)
2. Cross-validation to choose hyperparameters (e.g., λ, d)
3. Early stopping (for gradient-descent-based methods)
4. Data augmentation (increases effective N)
5. Ensemble methods (bagging reduces variance)

**Note on ERM and model selection:** ERM, as stated, minimizes over θ within a fixed
model family. Choosing between families (linear vs. neural network) is **model
selection**, handled in §8.6.

---

### 8.3 Parameter Estimation — Maximum Likelihood

**The setup:** Assume data D = {x_1, ..., x_N} are i.i.d. draws from p(x | θ_true).
Given observed D, what θ best explains it?

**Likelihood function:**
```
L(θ | D) = p(D | θ) = Π_{i=1}^{N} p(x_i | θ)
```
The likelihood is a function of θ for fixed D. It is NOT a probability distribution
over θ (in the frequentist view θ is a fixed unknown, not a random variable).

**Maximum Likelihood Estimator (MLE):**
```
θ_MLE = argmax_θ L(θ | D) = argmax_θ Π_{i=1}^{N} p(x_i | θ)
```

**Log-likelihood trick:** Products of probabilities underflow numerically; the log
is monotone so maximizing L is equivalent to maximizing log L:
```
θ_MLE = argmax_θ Σ_{i=1}^{N} log p(x_i | θ)
```
This converts a product over N terms into a sum — much more numerically stable
and mathematically convenient (gradients of sums are sums of gradients).

**Connection to ERM with negative log-likelihood loss:**
```
θ_MLE = argmin_θ [ -(1/N) Σ_{i=1}^{N} log p(x_i | θ) ]
```
So MLE is exactly ERM when the loss function is the negative log-likelihood (NLL).
This is the bridge between the optimization and probabilistic views of learning.

**MLE for a univariate Gaussian:**

Assume x_i ~ N(μ, σ²). The log-likelihood is:
```
log L(μ, σ² | D) = -(N/2) log(2πσ²)  -  (1 / 2σ²) Σ_{i=1}^{N} (x_i - μ)^2
```
Setting ∂/∂μ = 0 and ∂/∂σ² = 0:
```
μ_MLE    = (1/N) Σ_{i=1}^{N} x_i         (sample mean)
σ²_MLE   = (1/N) Σ_{i=1}^{N} (x_i - μ_MLE)^2   (biased sample variance, divides by N)
```

Note: σ²_MLE is biased — it systematically underestimates the true variance.
The unbiased estimator divides by (N-1) (Bessel's correction), but MLE does not
automatically produce unbiased estimators.

**MLE for a multivariate Gaussian:**

Assume x_i ~ N(μ, Σ) with x_i ∈ R^D. Log-likelihood:
```
log L(μ, Σ | D) = -(N/2) log det(2πΣ)  -  (1/2) Σ_{i=1}^{N} (x_i - μ)^T Σ^{-1} (x_i - μ)
```
MLE estimates:
```
μ_MLE   = (1/N) Σ_{i=1}^{N} x_i                                    (sample mean vector)
Σ_MLE   = (1/N) Σ_{i=1}^{N} (x_i - μ_MLE)(x_i - μ_MLE)^T         (sample covariance)
```

**Properties of MLE:**
- **Consistency:** θ_MLE → θ_true as N → ∞ (under regularity conditions)
- **Asymptotic normality:** √N (θ_MLE - θ_true) → N(0, I(θ_true)^{-1}) where I is
  the Fisher information matrix
- **Efficiency:** Achieves the Cramér-Rao lower bound asymptotically — no unbiased
  estimator has lower variance in the limit
- **Invariance:** If θ_MLE maximizes L(θ), then g(θ_MLE) maximizes L(g^{-1}(·))
  for any invertible transformation g
- **Bias:** MLE is generally biased for finite N (as seen with σ²)

**MLE for linear regression (supervised case):**

For D = {(x_i, y_i)}, assume y_i = θ^T x_i + ε_i, ε_i ~ N(0, σ²). Then:
```
p(y_i | x_i, θ) = N(θ^T x_i, σ²)
```
The MLE for θ is:
```
θ_MLE = argmin_θ Σ_{i=1}^{N} (y_i - θ^T x_i)^2
```
This is exactly **ordinary least squares** — minimizing squared residuals.
Under the Gaussian noise assumption, MLE = least squares. This is why
Chapter 9 (linear regression) begins where this chapter ends.

---

### 8.4 Probabilistic Modeling and Inference

MLE treats θ as a fixed unknown. The Bayesian view treats θ as a **random variable**,
encoding uncertainty about parameters via a probability distribution.

**Prior:** p(θ) — our belief about θ before seeing data. Encodes domain knowledge or
structural assumptions (e.g., "weights are small" → Gaussian prior).

**Likelihood:** p(y | X, θ) — probability of the data given parameters. Same object
as in MLE, but now paired with a prior.

**Posterior (via Bayes' theorem):**
```
p(θ | y, X) = p(y | X, θ) p(θ) / p(y | X)
```
In words: posterior ∝ likelihood × prior. The denominator p(y|X) is a normalizing
constant (the marginal likelihood or evidence), which does not depend on θ:
```
p(y | X) = ∫ p(y | X, θ) p(θ) dθ       (marginal likelihood)
```
This integral is usually intractable — it requires integrating over all possible θ
weighted by the prior. Approximations (Laplace, variational inference, MCMC) are needed.

**Maximum a Posteriori (MAP) estimate:**
```
θ_MAP = argmax_θ p(θ | y, X)
       = argmax_θ [ log p(y | X, θ) + log p(θ) ]
```
MAP maximizes the posterior (instead of just the likelihood). Because the evidence
p(y|X) is constant in θ, it drops out. MAP = MLE + log-prior regularization.

**Connection between MAP and regularized ERM:**

If the prior is Gaussian: p(θ) = N(0, σ_0² I), then:
```
log p(θ) = -(1/2σ_0²) ‖θ‖^2 + const
```
So MAP optimization becomes:
```
θ_MAP = argmin_θ [ -Σ log p(y_i|x_i,θ)  +  (1/2σ_0²) ‖θ‖^2 ]
```
This is exactly **ridge regression** (L2 regularization). The regularization strength
λ = 1/σ_0² is controlled by the prior variance: a tighter prior (small σ_0²) means
more regularization. The Bayesian and optimization views are formally equivalent for MAP.

Similarly, a Laplace prior p(θ) ∝ exp(-|θ|/b) gives L1 regularization (lasso).

**Predictive distribution (full Bayesian):**

Once we have the posterior p(θ|y,X), the prediction for a new input x* is:
```
p(y* | x*, X, y) = ∫ p(y* | x*, θ) p(θ | y, X) dθ
```
This marginalizes over all possible θ, weighting each model by how consistent it
is with the data. The result is a distribution over y*, not a point estimate.
This is the full Bayesian prediction — it properly accounts for **parameter uncertainty**.

Compare to MAP and MLE predictions, which plug in a single θ and produce a point
estimate (or at best a conditional Gaussian for fixed θ):
```
MLE prediction:  p(y* | x*, θ_MLE)       (ignores all parameter uncertainty)
MAP prediction:  p(y* | x*, θ_MAP)        (uses the single best θ under posterior)
Bayes prediction: ∫ p(y*|x*,θ) p(θ|y,X) dθ   (averages over all θ, most principled)
```

**Conjugate priors:** When the prior and likelihood are chosen so that the posterior
has the same distributional family as the prior, computation is tractable. Examples:
```
Likelihood         Prior              Posterior
Gaussian (μ)       Gaussian (μ)       Gaussian (μ)
Binomial (p)       Beta (p)           Beta (p)
Poisson (λ)        Gamma (λ)          Gamma (λ)
Multinomial (π)    Dirichlet (π)      Dirichlet (π)
Gaussian (Σ)       Inverse-Wishart    Inverse-Wishart
```
Conjugacy makes the posterior update a closed-form formula — no integral required.

**Bayesian updating as sequential learning:**

The posterior after seeing N data points becomes the prior when N+1 data arrive:
```
p(θ | x_1,...,x_N, x_{N+1}) ∝ p(x_{N+1} | θ) p(θ | x_1,...,x_N)
```
This is Bayesian learning — the model continuously updates as data arrive, without
ever storing the raw data. The posterior is a sufficient summary.

---

### 8.5 Directed Graphical Models (Bayesian Networks)

As models grow complex (latent variables, hierarchical priors, multivariate outputs),
writing out the full joint distribution p(x_1, ..., x_K) becomes unwieldy. Directed
graphical models (DGMs), also called **Bayesian networks**, provide a language for
expressing and reasoning about these distributions compactly.

**Graph structure:**
- **Nodes:** random variables x_1, ..., x_K (observed or latent)
- **Directed edges:** x_i → x_j means "x_i directly influences x_j"
- **Directed Acyclic Graph (DAG):** no cycles — enforced to ensure the distribution
  factors consistently

**Factorization theorem:**
```
p(x_1, ..., x_K) = Π_{k=1}^{K} p(x_k | pa(x_k))
```
where pa(x_k) is the set of **parents** of node x_k in the DAG.
Each node's distribution depends only on its parents — not on the entire history.

This is the central equation of graphical models: a complicated joint over K variables
factorizes into K local conditional distributions, one per node.

**Worked example — a 3-node chain A → B → C:**
```
p(A, B, C) = p(A) p(B | A) p(C | B)
```
Note: C and A are NOT conditionally independent unconditionally, but:
```
p(C | A, B) = p(C | B)      (C is independent of A given B)
```
B "blocks" the path from A to C when B is observed. This is the chain rule at work.

**Worked example — a naive Bayes classifier:**

Class label Y and D features x_1, ..., x_D:
```
p(Y, x_1, ..., x_D) = p(Y) Π_{d=1}^{D} p(x_d | Y)
```
The graph has Y as parent of all x_d. Given Y, all features are conditionally
independent. The "naive" in Naive Bayes is this conditional independence assumption.

**d-Separation (directional separation):**

d-Separation is the graphical criterion for reading off conditional independence
statements from the DAG, without computing distributions.

Three basic structures to know:

**Chain:** A → B → C
- A ⊥⊥ C | B (B observed blocks information flow)
- A and C are NOT independent marginally

**Fork (common cause):** A ← B → C
- A ⊥⊥ C | B (conditioning on common cause blocks correlation)
- A and C are correlated marginally (through B)

**Collider:** A → B ← C
- A and C ARE independent marginally
- A and C are NOT independent given B (conditioning on a collider OPENS a path —
  "explaining away" or Berkson's paradox)

**d-Separation rule:** Two nodes X and Y are conditionally independent given set Z
(written X ⊥⊥ Y | Z) if every path between X and Y is **blocked** given Z.
A path is blocked if it contains:
- A chain or fork where the middle node is in Z, OR
- A collider where neither the collider nor any of its descendants are in Z.

**Plate notation:** Repeated structure (e.g., N i.i.d. observations) is represented
by enclosing nodes in a rectangle (plate) with a count. Avoids drawing the same
sub-graph N times.

**Latent variable models in graph notation:**

Hidden Markov Model (HMM):
```
z_1 → z_2 → ... → z_T      (hidden states, Markov chain)
 ↓     ↓             ↓
x_1   x_2    ...   x_T     (observed emissions)
```
Factorization:
```
p(z_1,...,z_T, x_1,...,x_T) = p(z_1) Π_{t=2}^{T} p(z_t | z_{t-1}) Π_{t=1}^{T} p(x_t | z_t)
```

**Why graphical models matter:**
1. Compact specification of complex joint distributions
2. Systematic inference algorithms (belief propagation, variational inference)
3. Explicit encoding of independence assumptions — model assumptions become visible
4. Modular: can swap components (e.g., change emission model) without redesigning
   inference from scratch

---

### 8.6 Model Selection

So far we have assumed a fixed model family (e.g., degree-d polynomial) and estimated
θ within it. **Model selection** is the problem of choosing among families.

**Why standard train/test splits are not enough:**
Repeatedly choosing the model with the best test error will eventually overfit to the
test set. Proper model selection requires either a held-out validation set, cross-
validation, or an information-theoretic criterion that penalizes complexity.

**Bayesian model comparison:**

Model M_k is a choice of likelihood p(y|X,θ,M_k) and prior p(θ|M_k).
The **marginal likelihood** (or **model evidence**) of M_k is:
```
p(y | X, M_k) = ∫ p(y | X, θ, M_k) p(θ | M_k) dθ
```
This is the probability of observing the data y under model M_k, averaged over all
possible parameter values θ under the prior. It is a single number per model.

**Model posterior:**
```
p(M_k | y, X) ∝ p(y | X, M_k) p(M_k)
```
With uniform model prior p(M_k) = const, model comparison reduces to comparing
marginal likelihoods. The model with the highest evidence "wins."

**Occam's razor built-in:** The marginal likelihood automatically penalizes overly
complex models. A complex model (many parameters, weak prior) spreads its probability
mass thinly across many possible datasets — it assigns low probability to any specific
observed dataset unless the parameters fit very well. A simple model concentrates its
mass on fewer datasets. The marginal likelihood balances fit and complexity without
requiring an explicit penalty term.

**Bayesian model averaging (BMA):**
Rather than choosing a single model, average predictions over all models:
```
p(y* | x*, X, y) = Σ_k p(y* | x*, X, y, M_k) p(M_k | y, X)
```
This is the most principled approach but requires tractable marginal likelihoods
for each M_k — computationally expensive.

**Bayesian Information Criterion (BIC):**

The marginal likelihood integral is usually intractable. BIC approximates
log p(y|X,M_k) using a Laplace approximation around θ_MAP:
```
BIC(M_k) = log p(y | X, θ_MAP, M_k)  -  (d_k / 2) log N
```
where d_k = number of parameters in M_k, N = number of data points.

Select the model with the **highest** BIC (least negative). The penalty term
-(d_k/2) log N penalizes model complexity, analogous to AIC but with a stronger
penalty that scales with log N rather than a constant 2.

**BIC vs AIC:**
```
AIC(M_k) = 2 log p(y | X, θ_MLE, M_k)  -  2 d_k
BIC(M_k) = 2 log p(y | X, θ_MLE, M_k)  -  d_k log N
```
(Some texts write AIC/BIC with signs flipped — minimize instead of maximize.)

- **AIC** is derived from information theory (Kullback-Leibler divergence to true model)
  and is better for prediction tasks
- **BIC** approximates the Bayesian marginal likelihood and is better for model
  identification / structure selection
- For large N: BIC penalizes complexity more aggressively (log N grows without bound,
  whereas AIC's constant 2 stays fixed)

**Cross-validation as an alternative:**

K-fold cross-validation approximates the expected test error without a held-out set:
1. Split D into K roughly equal folds
2. For each fold k: train on D \ fold_k, evaluate on fold_k
3. Average the K test errors

Leave-one-out CV (K=N) is the most thorough but expensive. For linear models, LOO-CV
has a closed-form solution (the "hat matrix trick") so it costs no more than a single fit.

**Summary of model selection methods:**

| Method | What it measures | Computationally |
|--------|-----------------|-----------------|
| Train/val/test split | Generalization on a single holdout | Cheap, low variance if N large |
| K-fold CV | Avg generalization over K holdouts | Moderate (K fits) |
| AIC | Estimated KL to true model | One MLE fit |
| BIC | Approx log marginal likelihood | One MAP fit |
| Marginal likelihood | Exact Bayesian model score | Expensive (requires integration) |

---

## Key Formulas Quick Reference

| Concept | Formula | Notes |
|---------|---------|-------|
| Empirical risk | R_emp(θ) = (1/N) Σ ℓ(f(x_i,θ), y_i) | Objective of ERM |
| ERM solution | θ* = argmin_θ R_emp(θ) | Core learning equation |
| Regularized ERM | θ* = argmin_θ [R_emp(θ) + λ R(θ)] | λ controls regularization strength |
| Likelihood | L(θ\|D) = Π p(x_i\|θ) | Product over i.i.d. data |
| Log-likelihood | ℓ(θ) = Σ log p(x_i\|θ) | Numerically stable, sum not product |
| MLE | θ_MLE = argmax_θ Σ log p(x_i\|θ) | Maximizes log-likelihood |
| Gaussian MLE (mean) | μ_MLE = (1/N) Σ x_i | Sample mean |
| Gaussian MLE (var) | σ²_MLE = (1/N) Σ (x_i-μ)² | Biased by factor (N-1)/N |
| Bayes' theorem | p(θ\|y,X) ∝ p(y\|X,θ) p(θ) | Posterior ∝ likelihood × prior |
| MAP estimate | θ_MAP = argmax_θ [log p(y\|X,θ) + log p(θ)] | MLE + log-prior |
| Predictive dist. | p(y*\|x*,X,y) = ∫ p(y*\|x*,θ) p(θ\|y,X) dθ | Marginalizes θ |
| Marginal likelihood | p(y\|X,M) = ∫ p(y\|X,θ,M) p(θ\|M) dθ | Model evidence |
| DGM factorization | p(x_1,...,x_K) = Π p(x_k\|pa(x_k)) | One factor per node |
| BIC | log p(y\|X,θ_MAP,M) - (d/2) log N | Penalizes complexity by log N |
| Bias-variance | E[(y-f_hat)²] = Bias² + Var + noise² | Test error decomposition |

---

## Key Connections to Other Chapters

| Concept | Where It Shows Up |
|---------|-------------------|
| MLE with Gaussian noise = least squares | C9 (linear regression derives from this equivalence) |
| MAP with Gaussian prior = ridge regression | C9 (Bayesian linear regression, §9.3) |
| Predictive distribution for linear model | C9 (§9.3.3 gives the closed-form Gaussian predictive) |
| PCA as MLE for probabilistic latent model | C10 (probabilistic PCA = Gaussian latent variable model, §10.7) |
| Gradients of log-likelihood | C5 (matrix calculus; ∂/∂μ and ∂/∂Σ of Gaussian log-likelihood) |
| Gaussian distribution formulas | C6 (multivariate normal, §6.5; Cholesky for sampling) |
| Eigendecomposition of covariance | C4 (SVD/eigendecomp), C6 (Gaussian geometry), C10 (PCA) |
| Bayesian networks for density models | C11 (density estimation with GMMs uses latent variable graphs) |
| Marginal likelihood of GP | C12 (Gaussian processes select kernel hyperparameters via evidence) |
| d-Separation for checking model assumptions | C6 (conditional independence in multivariate Gaussians, §6.4) |

**From earlier chapters feeding in:**
- C5 (matrix calculus) provides the machinery to take derivatives of log-likelihood
  with respect to μ and Σ — this is how MLE solutions are derived
- C6 (probability) provides the Gaussian, conditional distributions, and change-of-
  variables formula needed for likelihood calculations
- C2/C4 (linear algebra): solving normal equations X^T X θ = X^T y uses least squares
  and rank conditions on the design matrix

---

## Open Questions

- Why does MLE underestimate variance (σ²_MLE biased)? Intuition: MLE uses the sample
  mean μ_MLE, which already "absorbs" some variance in the data. The true residuals
  (x_i - μ_true) would be larger on average. The fix is to divide by (N-1) not N.

- When does MAP collapse to MLE? When the prior is flat (uniform over θ), the log-
  prior term is constant, and MAP = MLE. A flat prior encodes "no prior knowledge."

- Why does the marginal likelihood penalize complex models (Occam's razor)?
  A flexible model can fit many datasets, so it spreads probability mass thinly.
  The marginal likelihood averages likelihood over the prior: complex models assign
  lower probability to any specific observed dataset unless the parameters fit well —
  exactly the penalty needed for principled model comparison.

- What happens to d-separation when a collider is conditioned on?
  Conditioning on a collider B in A → B ← C opens the path: A and C become correlated.
  This is "explaining away" — if B is observed and we learn A caused it, then C is
  less likely. Classic example: bright students and family legacy admissions —
  given admission (collider), high GPA and legacy status become negatively correlated.

- Full Bayesian prediction vs. MAP prediction: when does the difference matter?
  When the posterior is broad (few data, high uncertainty), integrating over θ gives
  substantially wider predictive intervals than plugging in θ_MAP. As N → ∞, the
  posterior concentrates at θ_MLE/MAP and the difference vanishes.

- Why is BIC derived from a Laplace approximation? The Laplace method approximates
  ∫ exp(g(θ)) dθ ≈ exp(g(θ*)) × (2π/N)^{d/2} / √det(-∇²g(θ*)) where θ* is the
  maximum of g. Taking logs and dropping constants yields the -(d/2) log N term in BIC.
