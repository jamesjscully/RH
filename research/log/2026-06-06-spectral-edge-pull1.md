# Spectral-edge thread — first pull (edge vs bulk) — 2026-06-06

Resolved the edge-vs-bulk question (the subtlety flagged in research/spectral-edge.md) on the
REAL ξ data. `scripts/numerics/witness/spectral_edge.py`.

## The §8 catch

My first attempt computed the min-gap location in the *raw* (un-standardized, one-sided) Jensen
frame and had a sign bug in the verification — it nearly recorded "edge confirmed" on a wrong
frame. The high-precision (mpmath) cross-check forced the correct method: standardize the roots
(mean 0, std 1, the canonical affine normalization) so the comparison to the standardized
Hermite frame is honest. Backpressure working.

## Finding (standardized frame, high-precision roots; d=8,10,12; n=4,12,20)

- **Hermite**: closest root pair at the **center (bulk)**, loc 0 — as expected (semicircle roots
  densest at center).
- **Real ξ J_{d,n}**: the **deviation from Hermite is MAXIMAL at the far spectral edge** —
  standardized loc `+1.00` in *every* case (the `+` side = largest roots = highest zeros in the
  window). The closest root pair (the immediate hyperbolicity danger) sits at the **shoulder**,
  loc `≈ +0.5`, dragged from Hermite's center toward the edge by that deviation. The ξ min-gap is
  much smaller than Hermite's (more marginal) and grows toward Hermite as `n→∞`, but stays
  edge-pinned.

## Verdict

**Edge framing CONFIRMED on real ζ** — and it is *not* a BW-metric artifact: in the
metric-independent standardized root frame, the real-ξ deviation lives at the spectral edge (the
high-zero side, the Airy regime of the semicircle), not the bulk. The RH-relevant deviation is
edge-concentrated. Nuance: the closest pair is at the shoulder (loc ~+0.5), driven by the edge.

Why the `+`/high-zero side: the Jensen polynomial is the Gaussian/Hermite (central-limit) profile
of ξ's local data; the deviation is largest where that approximation is weakest — the edge of the
moment window — i.e. the Airy/Tracy–Widom edge.

## Step 2 — edge vs bulk convergence rate

For fixed `d`, the edge (largest-root) deviation from Hermite is consistently **~1.85× the bulk**
(central-root) deviation, and **both decay at the same slow rate** in `n` (`~n^{−0.2}` / `e^{−0.02n}`
— extremely slow, consistent with GORZ's `n ≳ e^d`; at `n=28, d=10` the edge deviation is still
0.38). So the edge is uniformly the *largest* deviation but not a separately-slower mode. ("Tracy–
Widom" per se does not apply — ξ is deterministic, so the relevant object is the deterministic
**Airy** edge, not a fluctuation distribution.)

## Step 3 — the DYNAMIC edge test (the clean result)

Under the **backward** dBN flow `H_{−s}` (the direction that destroys hyperbolicity), the root
that goes complex **first is always at the EDGE** (standardized loc `±1`, the outermost pair) — in
*every* `(d,n)` tested. So the de Bruijn–Newman hyperbolicity-loss (the `Λ` mechanism) is
**edge-localized**, and the backward margin decays fast with `d` (`1.1e-2 → 7e-4` over `d=6→12`).

## Conclusion of the first pull

**The spectral edge is the RH-critical region in BOTH senses:** the static deviation `J_{d,n}−H_d`
is edge-concentrated (steps 1–2), AND the dynamic `Λ` mechanism (backward-flow hyperbolicity loss)
is edge-localized (step 3). This **localizes the uniform-in-`d` problem to the edge root pair under
the flow** — a genuine (if modest) structural reduction on real ζ: from "control `J_{d,n}`
everywhere" to "control the outermost root pair under the dBN flow." The flow's action is
**one-sided** (forward preserves hyperbolicity = the `Λ≥0` direction; backward breaks it at the
edge). It does not prove anything — the edge backward-margin still decays fast in `d` — but it
reduces the target to a **single edge degree of freedom**.

## Next

- The exact `d`-law of the **edge backward-margin** (certify it; is it the same super-exponential
  `½ d log d` as the static slack, now edge-localized?).
- Whether the **forward** (`Λ≥0`) direction, combined with the edge localization, yields a
  *uniform one-sided edge bound* — the genuine frontier the pull has sharpened to.
