# Angle 1 — total positivity as the common language of the Hermite junction — 2026-06-05

Tested the bet that **total-positivity coordinates** give a more *uniform* RH margin than the
super-exponential degree-by-degree Jensen slack. The setup (correct, and the genuine payoff of
this probe):

> RH ⟺ ξ ∈ Laguerre–Pólya ⟺ the Jensen sequence {γ(k)} is a Pólya-frequency (totally-positive)
> sequence ⟺ the de Bruijn–Newman flow (Gaussian = strictly-TP, variation-diminishing kernel,
> Schoenberg) realizes the zeros.

So "total positivity" names **both** the static criterion (the PF cone) and the dynamic flow (a
TP semigroup). The hypothesis: the slack measured in TP/minor coordinates is more uniform
(polynomial) than the Jensen min-rel-gap / Hermite discriminant (super-exponential).

Module: `scripts/numerics/witness/totally_positive.py`. Real-ξ certified Jensen sequence γ(k)
(`xi_jensen`); small Hankel dets certified as acb balls.

## Findings (honest, certified where it bites)

**(A) The naive Hankel/moment coordinate is CERTIFIABLY WRONG.** The first guess — "Hankel
determinants of {γ(k)}" — fails: the Hankel matrix det[γ(i+j)] of the *true* real-ξ sequence is
**not** PSD. Certified acb balls:

| n | det[γ(i+j)]_{n×n} (certified) |
|---|---|
| 1 | `+0.248560…` |
| 2 | `−1.76392…e−5  ± 5.6e−20`  ← **certifiably < 0** |
| 3 | `−1.838…e−14  ± 2.7e−28`   ← < 0 |

So {γ(k)} is **not a Hamburger moment sequence**. Hankel/moment positivity characterizes
"moments of a positive measure" — a *different* condition from real-rootedness / LP membership.
This is a real clarification: the obvious determinantal coordinate is not even a property of
RH-satisfying ξ. (The shifted Hankel det[γ(i+j+1)] is likewise sign-indefinite.)

**(B) The correct TP coordinate is Aissen–Schoenberg–Whitney (ASW).** A polynomial with positive
coefficients is hyperbolic (all roots real & negative) ⟺ the **Toeplitz matrix of its coefficient
sequence is totally nonnegative**. For each Jensen polynomial J_{d,n} (coeffs c_j = C(d,j)γ(n+j)),
hyperbolicity ⟺ coeff-Toeplitz TNN. Validated as a genuine RH margin: pushing J_{5,0} to the
discriminant variety (two closest roots merge at t=0, split complex at t<0), the smallest
strictly-positive contiguous (Fekete) minor → 0 and a **negative** minor appears *exactly* when
hyperbolicity is lost. This is the valid "distance to the PF-cone boundary."

**(C) The valid ASW margin is the SAME super-exponential slack — NO-GO.** Fair, fixed-order
comparison (no minor-order inflation), decay rate in degree at shift n=0:

| coordinate | log-slope /degree | verdict |
|---|---|---|
| 2×2 TP minor (Turán / log-concavity, lowest-order valid) | **−0.49** | = the gap |
| min-rel-gap (known Jensen slack) | **−0.44** | baseline |
| 3×3 TP minor | −3.24 (steepening) | **worse** |
| smallest positive minor over all orders | super-exp (−5.6) | worse |

The lowest-order valid TP minor (2×2 = log-concavity) decays at the **same rate** as the Jensen
root gap; every higher-order minor is **worse** (super-exponential). There is **no order of TP
minor that beats the gap**. Total positivity does not change the height of the discriminant
variety.

**(D) A seductive-but-INVALID near-miss (the §8 trap, stress-tested and rejected).** The
condition number σ_min/σ_max of the coeff-Toeplitz matrix decays only **−0.05/deg** — 10× more
uniform than the gap, the kind of "clean uniform margin" we were hunting. **Rejected** by the
validity test: as two roots merge to the discriminant boundary, σ_min/σ_max does **not** go to 0
— it stays ≈0.89 and *rises* (to 0.96) as the polynomial goes non-hyperbolic. It does **not
detect the PF-cone boundary**, so its uniform decay is irrelevant decoration. Separately, the
s-th-root normalization of any minor is a massive artificial compressor (it turns the Jensen
discriminant's true log-slope of **+61** into +0.17) — also rejected. The §8 backpressure caught
both; this is the third over-claim this discipline has stopped on this project.

**(E) Heat flow gives no cleaner handle.** Under the dBN TP semigroup H_t = e^{−tD²}, the smallest
positive Toeplitz minor of J_{6,0} moves monotonically but stays pinned at ~1e-11 (super-exp
small) for |t| up to the hyperbolicity threshold. The variation-diminishing structure controls
*sign changes* (Schoenberg) but does not lift the *minor margin* off the floor — no fresher
dynamic handle on the minors than on the Jensen polynomials themselves.

## Verdict — NO-GO

Total positivity is the **correct language** — it genuinely unifies the static PF criterion, the
ASW Toeplitz form, and the dBN TP semigroup into one object, which is conceptually satisfying and
confirms the Hermite junction. But it is **not a fresher coordinate**: the valid TP margin is the
*same* super-exponential slack the Jensen view already gave, and the only uniform-looking TP
quantity is invalid (blind to the boundary). This matches and reinforces the metric-Arakelov
finding (`metric-arakelov-probe.md`): the slack is the **height of the discriminant variety**,
super-exponentially small, and **changing coordinates (Jensen ↔ Toeplitz minors) does not change a
height**. GORZ's `n ≥ c·e^d` is not an artifact of the Jensen parametrization — it is intrinsic to
the distance-to-the-PF-cone-boundary, in whatever TP coordinate.

This is the cheap, honest outcome the brief asked for: TP was tested as a candidate coordinate and
shown to be decoration on the margin question (while being the right *language*). The RH-hard
endpoint (uniform-in-d slack / positive Green form, BGS §6.3) is unchanged.

## Honest next step (were it GO — it is not)

None toward a proof. The one residual idea, recorded and *not* pursued because the data kill it:
one might hope a *weighted* TP form (a different metric on the minors, e.g. Bombieri–Weyl-weighted
Toeplitz) flattens the 2×2 rate — but since even the σ-ratio (the most favorable reweighting)
fails the boundary-validity test, any reweighting that stays uniform will be boundary-blind by the
same mechanism (the boundary is a measure-zero algebraic set the smooth condition number does not
see). The genuine frontier remains the metric/Arakelov uniform bound, not a coordinate change.
