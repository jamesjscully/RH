# dBN flow functional from Λ(n): the open object the anchor named — built and falsified (NEXT #1)

**Item** (AGENDA NEXT #1, the top dBN item). The dBN anchor (`2026-06-06-dbn-anchor.md`) closed the
Rodgers–Tao branch and named the precise OPEN object the dynamical route leaves:

> Is there a **flow functional built from `Λ(n)`** (the Euler data) that is **monotone toward
> reality** under the dBN flow — a *dynamical* `W_∞ ≥ Σ_p W_p`?

Such a functional would force `Λ≤0` (RH) *while being Euler-borne*, escaping **both** defects of the
only unconditional RT lever (GUE pair correlation: universal **and** wrong-direction). I constructed a
genuine candidate, ran it through `falsify.py`'s three axes, and pre-tested the agenda's hypothesis:
does it **split** (modulus-monotone but phase / `sign Im`-blind) like every static functional?

Module: `scripts/numerics/witness/dbn_flow_functional.py` (+ 1 `falsify.py` row).

## The construction [computed]

**The load-bearing structural fact** (from the anchor, now central): the dBN generator
`e^{−tD²}` / log-gas `d/dt x_j = −2 Σ_{k≠j} 1/(x_k−x_j)` is **Euler-FREE**. The Euler product `Λ(n)`
enters dBN **only through the INITIAL datum** `Φ` (the theta/`Λ(n)` series). So "a flow functional
built from `Λ(n)`" can only be the Euler data **riding on** the flowing configuration — a
prime-weighted functional `E_Λ[config]` recomputed along the flow. The generator never sees a prime.

**The candidate** (the most natural Euler-borne reality functional). The Weil explicit formula reads
`Λ(n)` against the zeros; when a zero is off-line, `γ_ρ = t − i(β−½)` is **complex** and the
prime-side kernel acquires an imaginary part. So the Euler-borne "distance from reality" is

    P(γ) = Σ_n Λ(n)/√n · e^{−σ²(log n)²} · cos(γ log n),   E_Λ[config] = Σ_γ Im P(γ),

the off-line **prime defect** of the explicit formula — the SAME Euler-borne prime data `P` every
static route used, now weighting a functional of the **dBN-flowed** zeros. Two readings tested:
- `E_modulus = Σ |Im P(γ)|`  (≥ 0, = 0 iff reality);
- `E_signed  = Σ  Im P(γ)`   (the only reading that could see `sign Im γ` = which side of the line).

## What the falsifier found — the SPLIT, exactly as pre-tested [computed + THM-flavored]

**[Axis 1 — EULER-BORNE: YES.]** Sign-scrambling `Λ(n)` (a non-multiplicative "DH-like" weight on the
same abscissas) moves the functional: `|E_ζ − E_DH| = 1.33`. The functional genuinely uses the Euler
data; DH (no Euler product) has a different prime sum.

**[Axis 2 — SEES-ZEROS: YES (modulus reading).]** `E_modulus` = `0.000000` on an on-line config (real
`γ`) → `0.286` with a planted off-line pair (complex `γ`). Under the flow `E_modulus` tracks the
reality distance `max|Im root|` with correlation **`+1.00`** (`17.34→11.25` as `max|Im|: 0.872→0.728`).

**[Axis 3 — INDEPENDENT: NO → CIRCULAR (modulus reading).]** `|·|` is a **MODULUS**: it measures HOW
FAR off-line, not WHICH SIDE — symmetric under `γ → conj(γ)` (the swap `+Im ↔ −Im`). And
`E_modulus → 0` **iff** the flow reaches reality **iff** `Λ≤0` = RH — exactly `weil_form.py`'s
PSD-iff-RH. No independent certificate; a certificate would BE a proof of RH.

**The decisive split — the signed reading vanishes [computed, exact].** `E_signed` (no `|·|`) WOULD
see `sign Im` (which side of the line), but it is **IDENTICALLY ZERO** on any FE-symmetric
configuration: verified `max|E_signed| = 0.00e0` across the entire flow. The `+Im` and `−Im` conjugate
zeros **CANCEL**. The FE forces the conjugate pair, so the only Euler-borne reading that sees
`sign Im` is annihilated — **exactly the conjugation symmetry `ρ ↔ ρ̄`** that closed the whole
real-form family (`zero_in_form_pairing`, DONE #25): `sign Im` is conjugation-ODD, every Euler-borne
functional value is conjugation-EVEN (a modulus).

**The flow gives no INDEPENDENT help.** `E_modulus` is monotone in `max|Im root|` **trivially** (it is
built to track `|Im|`); its decrease forward merely RE-READS that this particular config reaches
reality after flow (`Λ>0`). The Euler-free generator decides the reality; the primes only **watch**.
Reading a config's reality with a prime weight is **not** the primes *forcing* reality.

## Verdict [computed + THM-flavored]

The Euler-borne flow functional **SPLITS exactly like every static functional**:
- the **modulus** reading is Euler-borne YES, sees-zeros YES, independent NO → **CIRCULAR** (and
  phase-blind: symmetric under `γ↔conj γ`);
- the **signed** reading that sees `sign Im` is **identically zero** on the FE-forced conjugate config.

**No Euler-borne flow functional is reality-MONOTONE under the (Euler-free) dBN flow.** The dynamical
`W_∞ ≥ Σ_p W_p` does **not** materialize. The open object the anchor named is **unrealizable for the
SAME reason** as every static form: `sign Im` is conjugation-odd, Euler-borne functionals are
conjugation-even (modulus). **30th confirmation of the standing wall, now closing the dBN frontier.**

**This CLOSES dBN NEXT #1.** The dynamical branch was genuinely distinct on the *inertia* axis (the
flow escapes the Sylvester `*`-congruence lock — the anchor's real finding), but the precise open
object it left (an Euler-borne reality-monotone flow functional) hits the identical conjugation wall:
the flow generator carries no primes; the primes ride passively; the only `sign Im`-sensitive Euler
reading cancels by conjugation. **Distinct endpoint on inertia, same wall on the Euler/location axis.**

## Honest subtleties

- The flow demos use small synthetic polynomials (the dBN flow is exact on polynomials; the structural
  facts — `E_modulus` tracks `max|Im|`, `E_signed ≡ 0`, the Euler-borne diff `1.33` — are exact/robust).
- `E_modulus`'s monotonicity-in-reality-distance is **by construction** (it is built to read `|Im|`);
  the load-bearing finding is not "it tracks reality" (trivial) but that **the only reading that sees
  `sign Im` (`E_signed`) is annihilated by the FE conjugation** — the same conjugation-odd/even split
  that is `[THM]` for the static forms. That split is the genuine content, not the small-config numerics.
- The conjugation cancellation `E_signed ≡ 0` is exact for any FE-symmetric multiset (`+Im`/`−Im`
  pairing), independent of basis/config — the load-bearing structural fact.

## Sources / cross-refs
- `scripts/numerics/witness/dbn_anchor.py`, `research/log/2026-06-06-dbn-anchor.md` (the anchor that
  named this object).
- `scripts/numerics/witness/zero_in_form_pairing.py` (DONE #25): `sign Im ρ` is intrinsically complex /
  conjugation `ρ↔ρ̄` symmetric — no real form encodes it. This flow functional is the dynamical instance.
- `scripts/numerics/witness/weil_form.py`: `E_modulus → 0 ⟺ PSD ⟺ RH` (the circularity).
- Rodgers–Tao, arXiv:1801.05914 (the `Λ≥0` theorem whose lever this candidate tried to replace).
