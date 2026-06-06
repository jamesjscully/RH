# RF — CM / Shimura-Taniyama: is the radius FORCED by an archimedean infinity-type, w/o RH? [PARTIAL_LEAD · forced-for-CM, empty-for-zeta]

`[BUILT + computed · anchored vs 𝔽_q]` — 2026-06-06
Module: `scripts/numerics/witness/cm_shimura_taniyama.py`
(run: `python3 -m scripts.numerics.witness.cm_shimura_taniyama`, EXIT 0).

## The angle (the Rosati-reflection RF mandate)

The radius `|α|=√q` is the Rosati equality clause `F F†=q·Id` = Weil positivity, confirmed circular at
every prior level (PA-synthesis, PA2-equality-clause, M2/M3/M4A). **The CM / Shimura-Taniyama escape:**
for a CM abelian variety, purity `|α|=q^{1/2}` is a **THEOREM** (Shimura-Taniyama), with the radius
**forced by the CM TYPE** — a purely **archimedean** datum (a set of archimedean embeddings Φ / a Hodge
structure / an *infinity-type*). If the radius drops out of an archimedean infinity-type *without RH*,
and zeta's carrier (the weight-2 NS / Rankin-Selberg piece) carries such a type, that is a genuine escape.

## What got BUILT / computed (3 anchors, exact)

**[1] ANCHOR — the radius drops out of an EXACT integer norm identity, no zeros.** For CM elliptic curves
`E/𝔽_p` with CM by `O_K`, `K=ℚ(√−d)`, the Frobenius `π=(a+b√−d)/2` satisfies `N(π)=π·π̄=(a²+d b²)/4 = p`,
the **exact factorization** `a²+d b² = 4p`. Computed over **9 (d,p) pairs** (`d∈{1,2,3,7}`,
`p∈{5,7,11,13,17,23,31}`): `|α|²=p` to machine zero, every root. **`|α|=√p` is read off the norm — an
algebraic-integer identity — with NO zero-location input.**

**[2] THE CIRCULARITY PROBE — Rosati `q/π` = complex conjugation `π̄`.** Computed: the **algebraic** (Galois/
Rosati) involution `π↦q/π` and the **archimedean** (complex) conjugation `π↦π̄` **COINCIDE** for every CM `π`
(residual `<1e-9`). This coincidence is the whole mechanism, and it is a **structural fact of CM (imaginary-
quadratic) fields**, FREE of RH: the unique nontrivial automorphism of `K` *is* complex conjugation.

**[3] THE DECISIVE FORCING — `a²<4q` is FORCED by `N(π)=q`, not assumed.** The roots of `T²−aT+q` are
genuine complex conjugates (⟹ `|α|²=αᾱ=q`) **iff `a²<4q`** (else real, off-circle). Computed: for ordinary
CM (`π` irrational, `b≠0`), `a² = 4q − d b² < 4q` is **FORCED** the instant `b≠0`. And `b≠0` is the
*ordinary/split* condition (`p` splits in `K`), a property of the CM type / reduction — **not** a
zero-location assumption. A hypothetical off-line `π` (`a²>4q`) would need `d b²<0`, i.e. a **real**
quadratic End-field, where Galois-conj `≠` complex-conj — **not a CM/purity structure at all.**

> **The chain, all one structural fact:** CM (imaginary quadratic) ⟺ Galois-conjugation = complex-
> conjugation ⟺ `N(π)=|π|²` ⟺ `a²<4q` ⟺ on-line. The radius is the v=∞ shadow of the `N(π)=q` norm
> identity, and the identification `N=|·|²` is the **CM-field structure**, not a positivity one assumes.

## Where RH enters (the audit) — and where it does NOT

- **It does NOT enter for CM.** `|α|²=q=N(π)` is the constant term of the Frobenius char poly = the
  **degree** (free). `N(π)=π·σ(π)` with `σ`=Galois; the CM condition makes `σ` = complex conjugation, so
  `N(π)=|π|²`. **Shimura-Taniyama is a theorem; the radius is GENUINELY FORCED, zero-input from the zeros.**
- **It WOULD enter for a general (non-CM) AV.** There `σ` is not complex conjugation on one eigenvalue;
  `|α|=√q` then needs the **Rosati positivity** (Weil) = RH-for-the-AV. **CM is special: a large, archimedean-
  typed (CM) endomorphism algebra makes `Rosati = complex-conjugation` AUTOMATIC, hence positive, hence the
  radius — with no separate positivity input.** This is the exact place the radius is normally `F F†=q·Id`
  (PA2): for CM it is supplied *for free by the endomorphism field*.

## The archimedean analogue for zeta — and why it is EMPTY

The CM type Φ is the **infinity-type** (the set of archimedean embeddings / the Hodge structure) the
mandate hoped would force the zero-modulus archimedean-only. The test (part 2/3):

- **zeta is GL(1).** Its motive is `ℚ(0)`, Hodge type `(0,0)`, weight 0 — **no Frobenius `π`, no
  endomorphism field `K`, no Rosati involution** for an infinity-type to act on. The zeta "infinity-type" is
  the `Γ_ℝ` factor (the `(0,0)`-Hodge type at ∞), which is **DH-SHARED**.
- **The weight-2 NS / Rankin-Selberg carrier (M4A) is NON-CM.** A CM structure there would require the cusp
  form `f` (eigenvalues `α_i`) to be **CM** — a Hecke character of an imaginary-quadratic field, where
  `|α_i|=√p` IS forced (a theorem). But that is the **measure-zero CM subfamily**, not zeta and not the
  generic Rankin-Selberg piece. **zeta's zeros are not the L-function of a CM object.**
- So the archimedean infinity-type that forces purity needs a **Frobenius eigenvalue carried by a CM
  endomorphism field** to act on. **zeta supplies none.** The forcing is real; the carrier is **absent**.

## DH / falsify

- **DH a CM structure?** **NO** — no Euler product ⟹ no Frobenius/Satake ⟹ no End-field ⟹ no CM type. The
  CM angle is **unposable** for DH (Euler-borne, DH-failing by design). But this discriminates DH from a CM
  *elliptic curve*, **not** DH from zeta: zeta is on the DH side of THIS discriminator (neither has a CM AV
  with a Frobenius `π`).
- **falsify three axes:** EULER-BORNE **YES** (needs `π`/Satake in a CM field). SEES-ZEROS **YES**
  (`a²<4q` ⟺ on-line, CM forces it). RADIUS **FORCED** (not assumed — the new content). APPLIES-TO-ZETA
  **NO** (no CM carrier).

## Verdict

`[PARTIAL_LEAD]` — **the radius IS genuinely forced (non-circular) for CM objects via Shimura-Taniyama, but
the route is EMPTY for zeta.** This is *not* the usual circular terminus: the CM mechanism really does force
`|α|=√q` **without RH** — the `N(π)=q` norm identity (the degree, free) is identified with `|π|²` by the
**structural fact that a CM (imaginary-quadratic) endomorphism field makes the Rosati involution = complex
conjugation**. That is exactly the `F F†=q·Id` positivity PA2 named the radius — supplied here **for free by
a large archimedean-typed endomorphism algebra**, not assumed. **The escape is real; the catch is the
carrier.** zeta (GL(1)) has no Frobenius/endomorphism-field for an infinity-type to act on, and the relevant
weight-2 Rankin-Selberg piece is **non-CM**. The very feature that forces the radius (a CM endomorphism
field) is precisely **what zeta lacks** — which is *why* the CM case is easy and zeta is hard.

**The sharpened next step (the residue):** the radius is forced exactly when the endomorphism algebra is big
enough (CM) to identify `N(π)` with `|π|²`. The open question is therefore **not** "find an archimedean
positivity" (PA2 closed that as circular) but: **can zeta's carrier be given an enlarged, archimedean-typed
endomorphism algebra in which the Rosati involution is forced = complex conjugation?** This is the
*motivic-CM-lift* question — manufacture, for the weight-2 NS lattice, a CM-by-an-archimedean-field structure
making purity automatic. Predicted **hard/likely-impossible** for a non-CM carrier (CM is measure-zero, and a
generic motive has End = ℤ), but it relocates the wall to a *concrete, decidable* place: **the absence of a
CM endomorphism algebra on zeta's carrier**, not a missing positivity — a strictly sharper terminus than
"the radius is `F F†=q·Id`."
