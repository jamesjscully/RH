# Hermite-junction synthesis — three angles — 2026-06-05

Ran the three fresh angles on the junction as parallel subagents. Each was disciplined and
honest; all three are committed (`totally_positive.py`/angle1, `renormalization.py`/angle2,
`lambda_height.py`/angle3, with logs). Independently re-verified the two new exact identities
(below). They **triangulate to one sharp conclusion.**

## What each angle found

- **Angle 1 — total positivity: NO-GO as a coordinate.** TP is the right *language* (the
  Pólya-frequency / Aissen–Schoenberg–Whitney Toeplitz criterion, and the dBN flow as a
  variation-diminishing TP semigroup, are genuinely one object), but **not a fresher
  coordinate**: the valid ASW minor margin decays at `−0.49`/degree, the same as the Jensen
  min-rel-gap `−0.44`; higher minors are worse. The naive Hankel/moment determinant is
  *certifiably negative* (so {γ(k)} is not a Hamburger moment sequence — moment positivity ≠
  RH). A seductive slow-decaying "condition-number" margin was caught and rejected (boundary-
  blind) by the §8 backpressure. **The slack is super-exponential in every TP coordinate.**

- **Angle 2 — renormalization: GO on structure, NO-GO on a fixed-point recursion.** Two clean
  new exact/certified identities:
  - **(A)** `disc(H_{n+1}) = 2^{3n}·(n+1)^{n+1}·disc(H_n)` (exact; follows from P1a).
  - **(B)** `e^{−tD²}H_n(x) = (1+4t)^{n/2} H_n(x/√(1+4t))` — **the dBN flow acts on the Hermite
    fixed shape as a PURE DILATION** (re-verified to machine precision). So along the fixed shape
    the flow is *exactly marginal* — a precise statement of "`Λ=0` at the fixed point."
  But there is **no** `ρ(d+1)=F(ρ(d))` fixed-point recursion: the slack obeys the marginal
  `log(1/ρ(d)) ~ ½ d log d` law (log-corrected, the textbook marginal-operator signature), the
  minimizing perturbation sits at the **outermost / spectral-edge** critical point (Airy regime),
  and the real-ζ Jensen→Hermite collapse is genuine but power-law slow (`~n^{−1/3}`).

- **Angle 3 — Λ as a height: GO on unification, NO-GO on Λ-as-height.** The dBN archimedean
  term, the Weil explicit-formula archimedean term, the BGS resultant height, and the Pardo–Pardo
  log-norm are **all one digamma object** — the archimedean `Γ_ℝ` factor. Verified exactly:
  `2 Re E_Ξ(t) = −log π + Re ψ(¼+it/2) = h₊(t)` (the dBN fixed-shape gamma-factor energy = the
  Weil archimedean term, to `1e-35`); and the Weil constant `log4π+γ` and the Burnol/BD constant
  `2+γ−log4π` are complementary halves of `2+2γ`. **But** `Λ` has no height interpretation (it is
  the marginal time of a Gaussian-kernel flow, not a digamma), and the shared digamma is the
  `Γ_ℝ` factor that **Davenport–Heilbronn shares identically** — i.e. **RH-neutral / dispersing.**

## The synthesis (the genuinely sharp part)

The three converge on one thing: **the static side of the junction — the fixed shape and its
archimedean structure — is now fully understood, and it is fully RH-neutral.**

- the dBN flow on the fixed shape is a **pure dilation = exactly marginal** (Angle 2B);
- the fixed shape's archimedean energy is the **shared digamma `Γ_ℝ` factor**, identical for ξ
  and DH ⇒ **RH-neutral** (Angle 3);
- the slack is an **intrinsic marginal height**, super-exponential in **every** coordinate,
  including total positivity (Angles 1+2), and **edge/Airy-controlled** (Angle 2).

Therefore **the RH content is not in the junction's static/archimedean structure at all** — it
is in the **deviation from the fixed shape**: *transverse* to the marginal flow, at the
**spectral edge (Tracy–Widom / Airy)**, on the **non-archimedean / dynamical / Euler-product**
side. This relocates the difficulty precisely and rules out the entire static/archimedean half
of the junction as RH-neutral.

## The one fresh thread that survived

**The transverse / spectral-edge direction.** The slack is controlled at the outermost (Airy)
critical point; the flow is marginal *along* the fixed shape (so all its action is transverse);
the RH-relevant fluctuation is the **Tracy–Widom edge** of the Jensen→Hermite deviation. The
concrete, honest question: *does the edge (Airy/Tracy–Widom) fluctuation of `J_{d,n} − H_d`
admit a one-sided (`Λ≥0`-compatible) bound under the dBN flow, uniform in `d`?* This is exactly
where the GUE universality Rodgers–Tao exploit (zero statistics) meets the slack's edge control —
the only place Angle 2's marginal flow (B) and the edge-controlled slack could connect. It is not
a proof and likely still RH-hard, but it is a *sharper* target than "uniform-in-`d` slack bound":
the action is transverse, at the edge, and on the dynamical side.

## Honest status

No proof; the §8 discipline held (Angle 1 caught a near-miss, Angle 3 flagged its own result as
RH-neutral). Net gain: the junction is mapped to the line — static/archimedean = understood and
RH-neutral; RH content = transverse, spectral-edge, dynamical. Two clean new exact identities
(2A, 2B) and one exact archimedean unification (3) are banked.
