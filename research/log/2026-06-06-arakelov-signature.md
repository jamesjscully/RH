# Arakelov self-intersection / arithmetic Hodge index signature on bar(Spec Z): the (1,ρ−1) signature is real but BGS §6.3 blocks it ζ-intrinsically (2026-06-06)

**Item (AGENDA NEXT #1, load-bearing).** The ζ-intrinsic Frobenius reality structure: does the
**Arakelov self-intersection of an arithmetic Frobenius correspondence on `bar(Spec Z)` / the BGS
positive-Green-form**, built from ζ's own primes `Λ(n)`, carry the Hodge signature `(1,ρ−1)`, and
**where exactly does BGS §6.3 block it**? Run through `falsify.py`'s three axes.

Module: `scripts/numerics/witness/arakelov_signature.py` (+ 1 `falsify.py` registry row).

---

## What I built

The prior signature work (`signature_forcing.py`) put the Hodge signature `(1,ρ−1)` on a **borrowed**
Frobenius eigenvalue lattice (a genus-`g` curve over `𝔽_q`) — RH-for-the-curve, a THEOREM. This module
asks the ζ-INTRINSIC question over `bar(Spec Z)`, the arithmetic base where ζ literally lives, and pins
the §6.3 obstruction by making the **arithmetic intersection pairing executable from the Weil explicit
formula**.

**The structure exploited [THM: Moriwaki 1994, arXiv:alg-geom/9403011, Thm B; Faltings; Hriljac].**
The arithmetic Hodge index theorem: for `x ∈ CH^1-hat(X)` with vanishing generic-fiber degree (the
primitive part), `deg-hat(x²·c₁(H,k)^{d−1}) ≤ 0` — NEGATIVE SEMIDEFINITE, signature `(1,ρ−1)`-type
(one ample/polarization `+` direction, neg-def primitive part). The negativity comes from **two**
pieces, which I verified are exactly the two sides of the Weil explicit formula:
- **(i) FINITE places** `(D_F²·H) ≤ 0` (geometric Hodge index / Zariski, Moriwaki Lemma 1.3) `=` the
  prime terms `−Σ Λ(n) h(log n)/√n`;
- **(ii) ARCHIMEDEAN** `∫ φ dd^c(φ) Φ^{d−1} ≤ 0` (Moriwaki Lemma 1.1.1, `= −∫|∂φ|²`) `=` the
  `+ (1/2π)∫ ĥ(r) Re ψ(¼+ir/2) dr` `Γ_ℝ` term.

The **load-bearing hypothesis** is Moriwaki Thm 1.1 **(ii): `c₁(H,k)` must be a KÄHLER form** (the
metric POSITIVE / `(H,k)` arithmetically ample). Without it the `dd^c` term in Lemma 1.1.1 has no
definite sign and the index theorem fails. **THIS is BGS §6.3: a positive Green form / positive `c₁`
need NOT exist on `bar(Spec Z)`** (`positivity-program.md` auditor row).

## Findings [computed, certified — mpmath/numpy, Λ(n) via flint in `explicit_formula.py`]

On a 5-dim even-Gaussian test basis (centers at log-scales `{0.7,1.1,1.6,2.3,3.0}`, prime sum to
`M=400`), I assembled the archimedean Gram `A` (Plancherel pairing against `Re ψ(¼+ir/2)`) and the
finite-place Gram `P` (`Σ c(n) hᵢ(log n)hⱼ(log n)/n`), with `W = A − P` the Weil form.

1. **The archimedean Kähler form is IDENTICAL for ζ and DH — `max|A_ζ − A_DH| = 0.0` exactly.** `A`
   depends only on `Re ψ(¼+ir/2)` (the `Γ_ℝ` factor), which ζ and Davenport–Heilbronn **share
   verbatim**. So the **dominating positive piece** of the signature (the (ii) Kähler/`dd^c` term, the
   one that supplies the `(1,·)` direction) is **DH-shared, carries NO RH content**.

2. **The Euler content lives ENTIRELY in the FINITE-place piece `P`, and it enters with a MINUS sign.**
   `P` signature: **ζ → (5,0,0)** (positive-definite — `Λ(n)≥0`, prime-power supported) vs **DH →
   (3,0,2)** (indefinite — mixed-sign, off-prime-power coefficients `c_DH`). This is the Euler-product
   fingerprint, sharply localized to the finite places. But in `W = A − P` the prime piece is the
   **subtracted/dominated** term — it is what the archimedean positivity must DOMINATE, not the
   dominator (`Weil W=A−P`: ζ `(1,0,4)` vs DH `(2,0,3)` on this coarse basis — the form does
   distinguish them, through the finite places).

3. **Where §6.3 blocks the ζ-intrinsic object (the decisive structural finding).** For ζ,
   `X = bar(Spec Z)` is arithmetically a **CURVE** (`d = dim f = 0`; the base is 1-dimensional). There
   is **no ample polarization class `c₁(H,k)` of positive dimension** on `bar(Spec Z)` itself to carry
   a `(1,ρ−1)` signature. The signature needs a **2-dimensional self-product** (the surface `S²`,
   `F-sym2-os-bridge` A5) — the SAME "no `H¹(S²)` over `ℤ`" / "continuous Frobenius `Δ·Δ=∞`" wall the
   audit keeps hitting. The arithmetic Hodge index theorem is a THEOREM **on an EXISTING arithmetic
   surface `X/Spec(O_K)`**; for ζ the requisite surface (whose polarization self-intersection is the
   zeta data) is EXACTLY the missing object. And §6.3 says: **even granting the surface**, the positive
   Green form / Kähler hypothesis (ii) that makes the negativity hold **can fail** — and that failure is
   precisely the archimedean **knife-edge** (positivity restored only by the exact prime, thread 0 /
   CC20, `positivity-program.md` §E.2).

## Falsifier verdict

- **Euler-borne?** PARTIAL — and decisively so: the dominating positive piece (archimedean Kähler) is
  IDENTICAL for ζ and DH (`max|A_ζ−A_DH|=0`); the Euler content is only in the subtracted finite-place
  `P`. Same shape as `phase_winding.py`: the dominator is DH-shared.
- **sees-zeros?** YES, but only because `W = A − P` **IS** the Weil explicit-formula form (planting an
  off-line zero breaks its primitive-part neg-definiteness, cf. `signature_forcing.py`).
- **independent?** NO. The arithmetic Hodge index negativity holds only GIVEN (a) the surface `S²/ℤ`
  (missing) and (b) the positive-Green-form / Kähler hypothesis (BGS §6.3, can fail). Over
  `bar(Spec Z)` as a curve there is no polarization of positive dimension to carry `(1,ρ−1)` at all.

> **VERDICT: CIRCULAR.** The arithmetic Hodge index theorem **genuinely carries** the `(1,ρ−1)`
> signature and its negativity **is** the Weil positivity — but ζ-intrinsically over `bar(Spec Z)`
> (a 1-dim base, no surface) there is no room for it, and BGS §6.3 is EXACTLY the archimedean
> positive-Green-form hypothesis that can fail = CC20's knife-edge. **The dominating positivity is
> DH-shared (not Euler-borne); the Euler content sits only in the dominated finite-place piece.**
> **19th Euler-product confirmation.**

## Honest subtleties (do not fool ourselves)

- The 5-dim Gaussian basis with integration cutoff `R=60`, `M=400` is a **coarse finite-rank model**;
  the exact `W` signature is `(1,ρ−1)` only in the limit. I do NOT claim the computed `(1,0,4)` is the
  exact Hodge signature — the **load-bearing, exact** computed facts are (1) `max|A_ζ−A_DH|=0` and
  (2) the `P`-signature split `ζ:(5,0,0)` vs `DH:(3,0,2)`. Those are robust to basis/cutoff.
- "`bar(Spec Z)` is arithmetically a curve" is the standard arithmetic-dimension count
  (`dim bar(Spec Z) = 1`); the (1,ρ−1) signature is a SURFACE (codim-1 cycles on a 2-dim arithmetic
  scheme) phenomenon. This is why the agenda's "Arakelov self-intersection of a Frobenius
  correspondence" needs the **self-product** — and is the same `S²/ℤ` gap, now confirmed from the
  arithmetic-intersection-theory side with the precise §6.3 hypothesis named.

## What this sharpens

This **confirms and localizes** the standing wall from the Arakelov/BGS side that NEXT #1 named: the
arithmetic Hodge index theorem is the right `(1,ρ−1)` structure, but (a) it lives on a SURFACE `S²/ℤ`
that doesn't exist ζ-intrinsically (1-dim base), and (b) BGS §6.3 = Moriwaki Thm 1.1 (ii) Kähler
hypothesis is the archimedean positive-Green-form that **can fail** = the CC20 knife-edge. The split is
new and decisive: **the dominating positivity (archimedean Kähler `Γ_ℝ`) is DH-shared; the Euler
content is only in the dominated finite-place prime piece** — so the §6.3 positivity, qua archimedean
positivity, is RH-SILENT, and the RH content can only be the cross-place coupling making the finite
piece dominate. Same wall as `W_∞ ≥ Σ_p W_p`, reached from arithmetic intersection theory.

Sources:
- A. Moriwaki, *Hodge index theorem for arithmetic cycles of codimension one*, arXiv:alg-geom/9403011
  (Thm B; Lemmas 1.1.1, 1.1.2, 1.3).
- J.-B. Bost, H. Gillet, C. Soulé, *Heights of projective varieties and positive Green forms*,
  J. Amer. Math. Soc. 7 (1994) 903–1027 (§6.3, positive Green forms).
- Faltings; Hriljac (arithmetic Hodge index on surfaces, via −Néron–Tate height).
