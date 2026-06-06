# Angle 2 — Renormalization / marginal fixed point at the Hermite junction — 2026-06-05

Tested the RG hypothesis on the Hermite junction: is the slack `ρ(d)` a *marginal observable*
at a renormalization fixed point (Hermite/semicircle), with an EXACT self-consistency recursion
`ρ(d+1)=F(ρ(d))` that would turn "uniform in d" into a fixed-point statement rather than a ∀d
estimate? Module: `scripts/numerics/witness/renormalization.py` (reproduces every number against
the existing certified data — `jensen_p1` discriminant, `jensen_p1b.deterministic_slack`,
`xi_jensen` real-ζ sequence).

## What is real (GO on exact structure)

**(A) Certified discriminant RG recursion.** Exact integer equality, verified `n=2..11`:
```
disc(H_{n+1}) = 2^{3n} · (n+1)^{n+1} · disc(H_n)
=> log disc(H_{n+1}) − log disc(H_n) = 3n·ln2 + (n+1)·ln(n+1)   (exact)
```
This is a clean RG recursion *on the energy/height*. But the increment GROWS like `n log n` —
the energy is a **RELEVANT** direction; there is no fixed point on the energy.

**(B) Exact "flow = rescale" identity at the fixed point** (machine precision, dev `≈3e-11`):
```
D² H_n = 4 n(n−1) H_{n−2}                         (exact lowering operator)
e^{−tD²} H_n(x) = (1+4t)^{n/2} · H_n( x / sqrt(1+4t) )    (pure dilation)
```
The de Bruijn–Newman heat flow acts on the Hermite fixed shape as a **pure dilation**. Dilation
preserves hyperbolicity and stays in-degree, so *along the fixed shape the dBN flow is EXACTLY
MARGINAL* — it neither creates nor destroys reality of roots. This is the precise content of
"Λ=0 at the fixed point": the flow direction tangent to Hermite is the null/marginal direction.
(This is a genuinely clean way to *say* Λ=0; it does not bound the off-fixed-shape flow.)

## What is NOT there (NO-GO on the load-bearing object)

**(C) No clean fixed-point recursion for the slack.** The ratio `ρ(d+1)/ρ(d)` does **not** tend
to a finite constant — it falls monotonically (`d8:0.41 → d48:0.15 → 0`). The per-step increment
`Δ log(1/ρ)(d)` **diverges** like `+log d` (`d8:0.90 → d48:1.91`). Asymptotic fit (d=12..50,
4-param, max resid 0.076):
```
log(1/ρ(d)) ≈ 0.546·d log d − 0.745·d + 0.276·log d − 0.296,   leading coeff → ~1/2
```
So the slack obeys the **marginal d·log d law** `log(1/ρ(d)) ~ (1/2) d log d` — a
super-exponential decay with a *logarithmic correction*, the textbook signature of a marginal
operator. It is **not** a self-similar geometric recursion `ρ(d+1)=c·ρ(d)`.

**The slack is the energy per degree.** Both share the semicircle/GUE log-energy:
`log disc(H_d) ~ (1/2) d² log d` (certified, P1a) and `log(1/ρ(d)) ~ (1/2) d log d`, i.e.
`log(1/ρ(d)) ~ (1/d) log disc(H_d)`. The ratio `log(1/ρ)/(logdisc/d)` climbs 0.40→0.51 over
d=20..50 (slow, consistent with →1). The minimizing perturbation sits at the **outermost**
critical point (|s|~edge of the semicircle), so the slack is **edge/Airy-controlled**, not bulk.

**(D) Scaling collapse is real but slow.** On real ζ, the normalized roots of `J_{4,n}` converge
to the `H_4` roots as the shift grows, with a **power-law** tail `dev ~ n^{−0.32}` (the GORZ 1/n
correction). The fixed point is genuine and confirmed on real data, but there is no clean
finite-n universal scaling function — the approach is power-law-slow (which is *why* the matching
threshold needs `n ≳ e^d`).

## Verdict

The RG framing supplies a **correct taxonomy** of the junction — *relevant* energy (A),
*marginal* flow along the fixed shape (B), *marginal* slack with a d·log d law (C), and a real
but slow scaling collapse (D). Two of these are exact/certified and were not previously written
down (the discriminant recursion and the flow=rescale dilation identity).

But the go/no-go question is **NO-GO on the load-bearing object**: there is *no* clean
`ρ(d+1)=F(ρ(d))` with a finite marginal fixed-point ratio that would let "uniform in d" become a
self-consistency statement. The slack's marginality is a *logarithmic-correction / super-exp* law
governed by the spectral **edge**, not a self-similar recursion. "Uniform in d" remains a ∀d
estimate against a super-exponentially shrinking, edge-controlled margin — exactly the RH-hard
endpoint (`error-height ≤ slack-height uniformly in d`, BGS §6.3). The RG language **sharpens** the
diagnosis (it pins the marginality as a d·log d edge law and identifies the flow's marginal
direction exactly) but does **not** ease the endpoint.

## Honest next step (if pursued)

The one non-decorative thread the RG view opens: the slack is **edge-controlled** (outermost
critical point, Airy regime), and the dBN flow is a pure dilation *only on the exact fixed shape*.
A real next move would be to compute the flow's action **transverse** to the fixed shape (the
*irrelevant/relevant* directions of the Jensen → Hermite deviation `~n^{−1/3}`) and ask whether
the *edge* fluctuation (Tracy–Widom / Airy) of the deviation can be controlled by the flow — i.e.
whether the marginal-flow identity (B) extends to a one-sided bound on the edge slack. This is the
only place (B) and (C) might connect; absent that, it is the same RH-hard uniform bound. No claim
of proof progress — this is a sharpened map, not a summit.
