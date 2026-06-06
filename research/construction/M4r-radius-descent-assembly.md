# M4r — the radius-descent assembly: is the global even split a RIGIDITY or a CONJUNCTION? [coherence-checked · anchored vs 𝔽_q / Δ]

**Charter:** `construction-program.md` §0 (polarization = duality pairing, not a metric), Pillar B
(the object by descent / cross-place coupling), §1 clause C3b. **Mandate (AGENDA M4r / K2r-fix — the
SOLE LIVE KEYSTONE):** K2r-fix resolved the reality/radius fork — the conjugation `κ=c_0` (the FE /
phase) is FREE over `ℤ` and **radius-silent by a theorem** (every conjugation `|μ|=1` carries only a
phase), while the radius `|α|=√d` is `σ_d`'s **scale** `d`, an Euler datum orthogonal to every
conjugation that must be **Euler-assembled in the descent**, not supplied by a real structure. M4r
SPECIFIES that assembly and **bounds what it can deliver**. **Built on:** K2r (the per-prime
edge/split factorization), M2d (purity is **intrinsically GLOBAL** for `ζ` — no single prime carries
`gr^W_1`). **Module:** `scripts/numerics/witness/radius_descent_assembly.py`
(run: `python3 -m scripts.numerics.witness.radius_descent_assembly`). **Falsifier row added** (→ 34th wall confirmation).

---

## The gap M4r closes (the wrong altitude of K2r, named by M2d)

K2r / K2r-split / K2r-fix all worked **prime by prime**: each prime's even split
`|α(p)|=|β(p)|=p^{(k−1)/2}` is, in isolation, exactly Ramanujan/RH for that prime — hence "CIRCULAR
per prime". **But M2d proved purity is intrinsically GLOBAL for `ζ`:** no single prime carries a
weight-1 `gr^W_1` (numerator degree `0`, *identical* in FF and `ℤ`); the weight-1 carrier exists only
GLOBALLY (the FF curve's `H^1` of rank `2g`, assembled from all its points by Lefschetz). So the
per-prime framing was the wrong altitude for the descent question. M4r asks it at the right altitude:

> **[The descent question, sharp].** When the even split is imposed **GLOBALLY** — across ALL
> places at once, as a property of the single glued weight-1 carrier — is it
> **(a) a RIGIDITY** (one cross-place constraint, where the radii at different places are *linked* by
> the Euler product / FE, so the global even split is forced by a coupling no single place sees — the
> descent ADDS content over the per-place conjunction), or
> **(b) a CONJUNCTION** (the global condition factors as `⋀_v` (per-place even split), the radii are
> *independent*, the Euler product imposes NO cross-place link, and the descent gluing adds NOTHING)?

This is the decisive Pillar-B question: does cross-place coupling **exist** as a radius constraint?

---

## The deliverable — the descent assembly map, and the rigidity test

> **[DEF · the radius-descent map].** The glued weight-1 carrier `gr^W_1` (FF: `H^1(C)`, rank `2g`;
> `ζ`: the assembled Satake data) carries two Euler-borne / FE data, both FREE:
> - the **global determinant** `det(F | gr^W_1) = ∏_i α_i = q^g` (FF) / `∏_p |α(p)β(p)| = ∏_p p^{k−1}`
>   (`ζ`) — the global EDGE (M2d's abscissa, the Petersson `‖f‖²` pole at `Re s=1`);
> - the **Poincaré pairing** `α_i α_{g+i} = q` per dual pair (the FE on `H^1`).
>
> The radius residue is the **global even split**: every modulus `|α_i| = √q` (resp. `√(p^{k−1})`).
> **The RIGIDITY TEST:** is the global even split FORCED by (determinant + pairing), or can the moduli
> redistribute across places while preserving every datum the Euler/FE data supply?

---

## The decisive computation — it is a CONJUNCTION, not a rigidity (exact mpmath 40 dps)

**FF anchor, genus 2 / `q=9`, eigenvalues in 2 conjugate-dual pairs (all load-bearing facts exact):**

A **determinant-neutral, pairing-neutral modulus redistribution** moves two pairs off the even split:
`|α_1| = r√q, |α_3| = √q/r` (pairing `α_1α_3=q` preserved); `|α_2| = √q/r, |α_4| = r√q` (pairing
preserved). Net effect on `∏|α_i|`: `(r)(1/r)(1/r)(r) = 1` — the **global determinant `q^g=81` is
PRESERVED**.

| config | moduli | `∏α_i` (det) | pairings `α_iα_{g+i}` | even split |
|---|---|---|---|---|
| genuine (on line) | `{3,3,3,3}` | `81` ✓ | `{9,9}` ✓ | **True** |
| redistributed (`r=e^{0.4}`) | `{4.475, 2.011, 2.011, 4.475}` | `81` ✓ | `{9,9}` ✓ | **False** (off at 2 places) |

So **(det PRESERVED) ∧ (pairing PRESERVED) ∧ (even split BROKEN)** — the global even split is **NOT
forced** by (determinant + pairing). The FE fixes the **product** of moduli (`=q^g`, the global edge,
FREE) but **not the individual moduli**; a balanced cross-place redistribution is invisible to it.

**`ζ` side (`f=Δ`, primes 5 and 7, `δ=0.3`):** plant off-even at `p_1` AND `p_2` independently, each
preserving its own determinant `p^{k−1}`. The **global determinant product is untouched**
(`9.6549…e16` before = after), yet `|α(5)|≠5^{(k−1)/2}` and `|α(7)|≠7^{(k−1)/2}`. The global FE of
`L(s,f)` is the single relation `s↔k−1−s` — it couples **no two primes' moduli**. The primes are
modulus-**independent**: the global mirror of the FF redistribution.

---

## The result (sharper than the agenda hoped — and a genuine BOUND)

| descent datum | status |
|---|---|
| global determinant `∏α_i = q^g` / `∏_p p^{k−1}` (the EDGE, `Re s=1`, `‖f‖²` pole) | **Euler-assembled, RH-FREE** |
| each Poincaré pairing `α_iα_{g+i}=q` (the FE on `H^1`) | **FE-free** |
| global even split `|α_i|=√q` for ALL `i` (the centre `Re s=½`) | **CONJUNCTION, NO cross-place rigidity** |

> **[coherence-checked].** The descent gluing **assembles the global determinant** (the product of
> moduli) — the global edge, free — but the radius RESIDUE (the global even split) is a **conjunction
> of per-place conditions with NO cross-place rigidity**: a determinant-neutral, pairing-neutral
> modulus redistribution moves eigenvalues off the even split at several places while preserving EVERY
> datum the Euler product / FE supplies. **So the descent adds no global lever over the per-prime K2r
> finding — the FE/Euler data couple the PRODUCT of radii, never the individual radii.**

This is K2r-fix's "the radius must be Euler-assembled" made **precise and then BOUNDED**: the assembly
delivers the **product** (the edge `Re s=1`), never the **split** (the centre `Re s=½`). The
agenda-level hope of M4r — "per-prime `√d` data assemble the global centre against the radius-silent
`(P_∞,D,c)`" — is **half achievable** (the product/edge assembles) and **half impossible by a
theorem** (no determinant/FE quantity is a function of the individual radii).

### Where this sends the keystone (the structural payoff)

The *only* structure that distinguishes the redistributed (off-even) configuration from the genuine
(even) one — both having identical determinant and pairings — is a **POSITIVITY on the global `gr^W_1`
that FAILS under redistribution**. That is exactly the Weil/Hodge index `P_∞ ⪰ 0` (the archimedean
keystone, M3/K1), which is **not a function of the determinant**: redistributing moduli off `√q` makes
the Hodge–Riemann form indefinite precisely because `C_W`'s radius is no longer uniform. **M4r thus
PROVES the descent cannot read `Re s=½` off the Euler/FE data (no rigidity exists) and relocates the
centre entirely onto the archimedean positivity `P_∞ ⪰ 0`.** The cross-place coupling K2r searched for
— a *link* between different places' radii — does not exist at the level of the FE; the link is the
positivity, and the positivity is the keystone.

---

## DH falsifier (type-level)

No Euler product ⟹ no Satake ⟹ no per-place determinant ⟹ **no edge to assemble AND no carrier to
glue.** The descent map has **empty domain at step 0**, strictly before the rigidity-vs-conjunction
question. Carrier ladder (M2d) `DH < ζ < FF`: DH lacks the edge; `ζ` has the edge (determinant, free)
+ the open global even split; FF has both, but its global even split is **also a conjunction**, forced
by **Deligne** (a positivity theorem on `H^1`), **not by the FE**.

## Falsifier verdict (M4r — a descent/coherence check; the residue is bounded away from the descent)

- **EULER-ASSEMBLED — the PRODUCT only.** The global determinant edge IS Euler-assembled and RH-free;
  the even split is **provably not** a function of the assembled determinant/pairing data (the
  redistribution is invisible to them). DH fails at step 0 (no edge).
- **SEES-ZEROS — YES**, but only through the positivity that fails under redistribution (the
  determinant/pairing data are blind to the redistribution).
- **INDEPENDENT — NO.** The discriminating structure is `P_∞ ⪰ 0` = Weil/Hodge index = RH.

Tabled **CIRCULAR** (`euler_borne=Y / sees_zeros=Y / independent=N`), with the NEW content being a
**no-go on the descent**: the radius is not a descent constraint at all — it is the archimedean
positivity. (This is the load-bearing negative — the loop working: a constructive bound that names the
next move.)

---

## Verdict

`[coherence-checked · anchored vs 𝔽_q / Δ]` — M4r executed the radius-descent assembly on the GLOBAL
weight-1 carrier (the altitude M2d proved is the right one) and found a **theorem-grade bound**: the
descent gluing **assembles the global determinant** (the product of moduli = the edge `Re s=1`,
Euler-borne, RH-free) but the **global even split** (the centre `Re s=½`) is a **CONJUNCTION of
per-place conditions with NO cross-place rigidity** — a determinant-neutral, pairing-neutral
redistribution breaks the even split at several places while preserving every datum the Euler/FE data
supply (exact: `∏α_i=81` and pairings `{9,9}` preserved, even split broken). **The FE couples the
PRODUCT of radii, never the individual radii.** So the descent adds NO global lever over K2r — and,
more sharply, it **CANNOT**: no determinant/FE quantity is a function of the individual radii. **Not
overclaimed:** M4r does not build the centre; it **proves the descent cannot** and relocates the
centre entirely onto the archimedean positivity `P_∞ ⪰ 0` (the keystone, M3/K1), which is the unique
structure that fails under the redistribution. **Successors named:** K7 [the redistribution as the
falsifier — make "Hodge–Riemann form indefinite under modulus redistribution" the executable test that
`P_∞⪰0` is the ONLY discriminator, on the FF anchor]; K3 sharpened (the forcing lemma's hypothesis
"`C_W` has uniform radius" is exactly "no redistribution" — the keystone is forcing uniformity of the
`C_W` radius, the one thing the descent provably cannot supply).
