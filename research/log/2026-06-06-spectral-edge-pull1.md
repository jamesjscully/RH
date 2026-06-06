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

## Next (steps 2–3 of the pull)

2. The edge-deviation SCALING in `(d,n)`: is `|J_{d,n}−H_d|` at the edge governed by the Airy
   function / Tracy–Widom edge scaling (`~ d^{−1/6}` fluctuation scale)? If yes, the Tracy–Widom
   framing is real and we have a universal handle; if not, it's decoration.
3. The dBN flow's TRANSVERSE action on the edge deviation: does the flow (a pure dilation along
   the fixed shape) suppress the edge deviation one-sidedly (`Λ≥0`-compatibly)?
