# Worker E — the Hecke/Euler dual certificate (the sharpened §J target) (2026-06-06)

*(§8 discipline: [THM] proven in the literature, [PROG] partial, [CONJ] conjecture, [unexplored].
Numerics in `scripts/numerics/witness/hecke_certificate.py`; run
`python3 -m scripts.numerics.witness.hecke_certificate`. Three-axis verdicts defer to the certified
`falsify.py`; the DH prime-side signature to `explicit_formula.py`.)*

**Task.** Worker D (`D-fourier-optimization.md` §4) sealed the Fourier-interpolation route with a
litmus: the Bondarenko–Radchenko–Seip modular interpolation couples primes **and** zeros as nodes but
only **records** RH, because its natural **dual certificate is Eisenstein** (archimedean — exactly
where ζ and DH agree). A **forcing** extremal must instead carry a modular form's **Euler/Hecke** data
in its dual certificate. A Hecke eigenform has an Euler product built in. So: **can a Hecke eigenform
supply the dual certificate, making the ζ-vs-DH value gap *sign*-load-bearing AND clearing the
sees-zeros axis?**

**Verdict up front.** There are exactly two Hecke positivities, and they fail on *different* axes —
neither forces:
- **Route (I), the Hecke L-function's own Li/Weil positivity** `Re λₙ(π) ≥ 0` ⟺ GRH for `L(s,π)`
  [THM, Li 2004]: **CIRCULAR** — the Euler product is present, but the positivity *is* that
  L-function's own Riemann hypothesis. Swapping ζ's unproven positivity for `L(s,f)`'s is no lever.
- **Route (II), the auxiliary Euler product** — **symmetric-square / Rankin–Selberg coefficient
  positivity**: this is the genuinely new structure a Hecke eigenform supplies (a *second* Euler
  product `L(s, f×f̄)` with **provably non-negative** Dirichlet coefficients), and it is the best
  automorphic candidate the whole audit has produced — **Euler-borne in the strongest form** (DH has
  no Euler product → no Satake `{αₚ}` → *no* sym²/Rankin–Selberg exists; DH cannot even be ingested)
  **and INDEPENDENT** (the `L(1,sym²) ≫ 1/log k` lower bound is unconditional, Hoffstein–Lockhart /
  Goldfeld–Hoffstein–Lieman). **But it is RH-SILENT on the decisive axis**: it is a **zero-free-region
  / Siegel-zero** mechanism — it excludes one **real** exceptional zero at the **edge** `s=1`, and is
  completely **blind to whether the infinitely many complex zeros sit on `Re s = ½`**.

**Net: the 8th independent Euler-product confirmation, in automorphic clothing.** The Hecke Euler
product *does* finally deliver an honest, unconditional, DH-refusing positivity — but it lands at the
**edge** `s=1`, exactly the Worker-A/QSM failure mode (Euler-borne, real-axis, blind to complex-zero
locations). It is a **half-plane** certificate, not the **line** certificate the BRS extremal needs.

---

## 1. The precise question — what a "Hecke dual certificate" would have to be

In the Cohn–Elkies / BRS framework (`D-fourier-optimization.md` §1–4) the Weil positivity is a `+1`
sign-uncertainty whose **dual certificate** is, for Viazovska's packing problem, an **Eisenstein
series** (`E₆`/`E₄`): a modular form **with no cusp/Hecke content** whose data lives at the
archimedean weight/normalisation. Worker D's diagnosis: an Eisenstein dual certifies the **archimedean
place**, where ζ and DH share the same `Γ_ℝ` — hence RH-neutral.

The sharpened target: replace the Eisenstein dual by a **Hecke-eigenform dual** — a *cusp* form whose
**Hecke eigenvalues / Euler product** enter the certificate. The hope is that the Euler product, now
*inside the certificate* rather than only in the functional values `W Uₙ = Λ(n)`, makes the
discriminator a **sign**, not just a value (worker C showed values aren't enough). Concretely a Hecke
eigenform `f` offers two distinct positivities to try:

| route | object | the positivity | what it would certify |
|---|---|---|---|
| **(I)** | `L(s,f)` itself | `Re λₙ(f) ≥ 0` (Li/Weil coefficients) | the zeros of `L(s,f)` on the **line** |
| **(II)** | `L(s, sym² f)` / `L(s, f×f̄)` | **Dirichlet coefficients `≥ 0`** (Euler norm-square) | `L(1,sym²) > 0` → a **half-plane** (no Siegel zero) |

Route (I) is the obvious "Hecke certificate"; route (II) is the *Euler-product-borne* positivity that
actually proves something unconditionally — the one the program has never tried on its Hecke side.

## 2. Literature — what is [THM] vs [unexplored]

**(a) Hecke-L-function Li positivity [THM].** Li, *Li coefficients for automorphic L-functions*
(arXiv:math/0404394; Ann. Inst. Fourier 2007), and the Rankin–Selberg extension (Ramanujan J. 2010,
*On Li's coefficients for the Rankin–Selberg L-functions*): for a principal automorphic `L(s,π)` over
`GL(N)`, **`Re λₙ(π) ≥ 0 ∀n ⟺ GRH for `L(s,π)`** — the `λₙ(π)` are values of Weil's quadratic
functional. **This is the automorphic Bombieri–Lagarias/Li criterion: circular by construction.**

**(b) Rankin–Selberg / symmetric-square coefficient positivity [THM, the load-bearing one].** The
local factor of `L(s, f×f̄) = ζ(s)·L(s, sym²f)` is `∏(1 − xᵢ p⁻ˢ)⁻¹` over a root multiset
`{α,β}⊗{ᾱ,β̄}` **closed under conjugation** ⟹ a **norm-square** Dirichlet series `Σ|dₖ|²p⁻ᵏˢ` with
**non-negative coefficients** (verified in the module: all `cₖ ≥ 0` over sampled Satake angles).
**This nonnegativity is the engine of:**
- Hoffstein–Lockhart, *Coefficients of Maass forms and the Siegel zero*, Ann. of Math. 140 (1994),
  **with the appendix by Goldfeld–Hoffstein–Lieman**: `L(1, sym² f) ≫ 1/log k`, hence **no
  Landau–Siegel (real exceptional) zero** for `L(s,f)`. [THM, unconditional]
- the broader use of "coefficients of positive type" for **zero-free regions** and pole bounds of
  Rankin–Selberg L-functions (standard; e.g. the level-aspect zero-free-region literature).

**(c) The barrier, stated in the literature.** Conrey–Li, *A note on some positivity conditions…*
(arXiv:math/9812166) already established for the **de Branges** positivity that "positivity may only
yield a weaker result, such as the non-existence of a **finite number** of zeros outside the critical
line" — *not* RH. Bombieri (*Problems of the Millennium: RH*) and the "reasons for doubting RH"
literature make the same structural point: the **Davenport–Heilbronn** function has a functional
equation and even bounded coefficients (Ramanujan) yet **off-line zeros**, *because it lacks the Euler
product* — so any positivity that is to force the **line** must consume the Euler product in a way
that an edge/half-plane positivity does not.

**Status table.**

| object | status | RH-relation |
|---|---|---|
| Hecke/automorphic Li positivity `λₙ(π) ≥ 0` | [THM] | **= GRH for `L(s,π)`** (circular) |
| sym²/Rankin–Selberg coefficient `cₙ ≥ 0` | [THM] | **edge**: `L(1,sym²) ≫ 1/log` ⟹ no Siegel zero (zero-free region) |
| GHL Siegel-zero exclusion | [THM, unconditional] | excludes **one real** zero; silent on complex off-line |
| "Hecke eigenform dual certificate forces Weil positivity" | **[unexplored / CONJ]** | the bet of §1 — assessed §3–4 below |

**No prior work uses a Hecke/Euler dual certificate for the *explicit-formula* (line) positivity** as
opposed to the central-value (period) positivity (the demoted thread 4) or the edge (Siegel)
positivity. The line-vs-edge distinction is the crux and is [unexplored] only in the trivial sense
that it is **structurally precluded** (§3).

## 3. The kill-test, sharpened — where it stalls

Run through `falsify.py`'s three axes (`hecke_certificate.py §[4]`):

**Route (I) — Hecke Li positivity.** Euler-borne **Y**, sees-zeros **Y** (it *is* the zero
functional), independent **N** (= GRH for `π`). → **CIRCULAR.** Stalls immediately: it is ζ's stone-2
wall, re-indexed by `π`.

**Route (II) — sym²/Rankin–Selberg coefficient positivity.** The interesting one.

| axis | result | mechanism (module) |
|---|---|---|
| **Euler-borne** (fails DH?) | **YES — strongest form** | `dh_has_no_sym2()`: DH's `c_DH(n)` are signed + off-prime-power (`n=6,12,14,…`), so there is **no `{αₚ}` to tensor** — the sym²/Rankin–Selberg L-function **does not exist** for DH. DH cannot even be *ingested* by the certificate. |
| **independent** (provable without RH?) | **YES** | `L(1,sym²) ≫ 1/log k` is the unconditional GHL theorem. |
| **sees-zeros** (off-line complex sensitive?) | **NO** | `edge_positivity_sees_zeros()`: the canonical Li functional flips sign under a planted off-line **complex** quadruple at `n*=12` (sees the line); the **edge surrogate** modelling the Siegel/`L(1,sym²)` mechanism is **invariant** — it controls only a (near-)**real** zero near `s=1`, never a complex zero's distance to `Re s = ½`. |

→ **RH-SILENT.** Euler-borne **and** independent — a first for the audit — but it **certifies a
half-plane, not the line**.

**Exactly where it stalls (and why it is structural, not incidental).** A coefficient/value positivity
`L(s) = Σ cₙ n⁻ˢ` with `cₙ ≥ 0` is a statement about `L` on the **edge of convergence** `Re s = 1`:
non-negative coefficients force `L` to inherit the pole's positivity at `s=1` and push real zeros away
from `s=1`. The **critical line `Re s = ½`** is the **reflected centre** of the functional equation —
the place coefficient positivity **cannot reach**, because reflecting `s=1 ↦ s=0` lands on the *other*
edge, never on the centre. So sym²-positivity is intrinsically a **zero-free-region engine**, not a
critical-line engine. This is the **same shape Worker C found** at `{∞,2}`: the Euler product enters
the **values** (here, makes `L(1,sym²)` positive) but the **sign that would force the line never
appears**.

## 4. Honest verdict — new lever, or the wall in automorphic clothing?

**The wall in automorphic clothing — but it moved the certificate one place in the right direction.**
The audit's progression of dual certificates is now:

```
   Eisenstein certificate   ->  the ARCHIMEDEAN place   (ζ = DH)            [worker D]
   Hecke/Euler certificate  ->  the EDGE  s = 1         (Siegel/zero-free)  [worker E, here]
   a FORCING certificate     ->  the LINE  Re s = ½                          [STILL EMPTY]
```

The Hecke Euler product is a **genuine improvement over Eisenstein**: it is finally **Euler-borne AND
independent** (Eisenstein was neither — it was archimedean and RH-neutral). The certificate has moved
from the archimedean place to the **prime/edge**. But it **stops at the edge**. The gap **edge → line**
is precisely the program's standing object — the cross-place coupling `W_∞ ≥ Σ_p W_p` — **unmoved**.
So the Hecke/Euler dual certificate is **not** a new forcing lever; it is the **8th independent
confirmation** that the Euler product discriminates ζ from DH but does not, by itself, force the zeros
onto the **line** — now demonstrated in the sharpest possible automorphic form (a positivity that is
*both* Euler-borne *and* unconditional, yet still RH-silent because it is edge-type).

**The single most concrete next probe (if pursued).** The *one* place a sym² positivity could touch
the **line** is a **Rankin–Selberg unfolding that is a genuine `L²`-norm** (Petersson/Plancherel
inner product) continued to the central line — the de-Branges-killed direction, but now with the Hecke
**Euler product** (not the archimedean kernel) supplying the reproducing kernel. Probe: does
`⟨f, f⟩_s`, analytically continued to `Re s = ½`, carry a **sign** that flips when a zero of `L(s,f)`
goes off-line? **Prediction (from this audit):** **NO** — the Rankin–Selberg `L²` norm is positive
from `Σ|coeff|²` alone (the *same* norm-square that made the coefficients non-negative), independent of
zero locations → **RH-SILENT**, the QSM pattern once more. It is falsifiable and expected to wall at
the same place; that is the honest next step, not an afternoon's win.

---

## 5. Auditor deltas (to fold into `positivity-program.md`)

- **§C tracker — new row:**
  | positivity mechanism | kill-test | verdict |
  |---|---|---|
  | Hecke/Euler dual certificate (sym²/Rankin–Selberg coeff positivity; GHL Siegel-zero) | *worker E* | **RH-SILENT (route II) / CIRCULAR (route I).** Route I `λₙ(π)≥0 ⟺` GRH for `π` (circular). Route II: sym²/Rankin–Selberg coeffs `≥0` (Euler norm-square) is **Euler-borne in the strongest form** (DH has *no* sym² — can't be ingested) **AND independent** (`L(1,sym²)≫1/log` unconditional) — a first — but **edge-type**: it excludes a **real** Siegel zero at `s=1`, blind to **complex** off-line zeros. Certifies a **half-plane**, not the **line**. |

- **§B auditor — new row:**
  | function-field structure | over ℤ | status / breakpoint |
  |---|---|---|
  | tensor/symmetric-power of Frobenius (Rankin–Selberg, sym²) with positive trace | sym²/Rankin–Selberg L-function `L(s,f×f̄)` with `cₙ ≥ 0` (Euler norm-square) | **transfers as an Euler-borne, unconditional positivity** (DH-refusing in the strongest form: no Satake ⟹ no sym²). **breaks at the LINE**: coefficient positivity certifies the **edge** `s=1` (zero-free region / no Siegel zero); the critical line `Re s=½` is the reflected centre no edge-positivity reaches. Edge → line = the cross-place coupling, unmoved |

- **§E durable lessons — addendum (8th confirmation):** a Hecke eigenform supplies the first
  automorphic positivity that is **both Euler-borne and unconditional** (sym²/Rankin–Selberg
  coefficient non-negativity ⟹ GHL `L(1,sym²)≫1/log`, no Siegel zero). It is nonetheless **RH-silent**
  because it is **edge-type** (real zero near `s=1`), not **line-type**. The wall sharpens to a
  one-line dichotomy: **coefficient/value positivity of an Euler product is a half-plane (`Re s=1`)
  certificate; the only line (`Re s=½`) automorphic positivity is GRH itself (circular).** The
  edge→line gap is the cross-place coupling `W_∞ ≥ Σ_p W_p`.

- **§J addendum:** the Hecke/Euler side of thread 4, opened by worker D, is now **closed negatively** —
  route I circular, route II RH-silent (edge). The BRS dual certificate cannot be made forcing by a
  Hecke eigenform: its Euler product lands at the edge, not the line.

---

### Module
`scripts/numerics/witness/hecke_certificate.py` — `rankin_selberg_local_coeffs` /
`symmetric_square_local_coeffs` (the Euler norm-square coefficients, `≥0`), `rankin_coeffs_nonnegative`
(axis 1 content), `dh_has_no_sym2` (axis 1 strongest form — DH has no sym²), `li_coeff_sym2_edge` +
`edge_positivity_sees_zeros` (axis 2 — edge positivity is blind to complex off-line zeros),
`hecke_certificate_falsified` (the two-route three-axis verdict), `SUMMARY_NOTE`. Run
`python3 -m scripts.numerics.witness.hecke_certificate`.

### Sources
- Li, *Li coefficients for automorphic L-functions*, arXiv:math/0404394, Ann. Inst. Fourier 57 (2007)
  — `Re λₙ(π) ≥ 0 ⟺` GRH for `L(s,π)` (the automorphic Li criterion; route I = circular).
- *On Li's coefficients for the Rankin–Selberg L-functions*, Ramanujan J. (2010) — Li coefficients for
  `L(s, π×π̃)` under GRH.
- Hoffstein, Lockhart, *Coefficients of Maass forms and the Siegel zero*, Ann. of Math. 140 (1994),
  **appendix by Goldfeld, Hoffstein, Lieman** — `L(1, sym² f) ≫ 1/log k`, no Siegel zero (the
  load-bearing Euler-norm-square positivity; route II, edge/unconditional).
- Conrey, Li, *A note on some positivity conditions related to zeta- and L-functions*,
  arXiv:math/9812166, IMRN (2000) — positivity (de Branges) yields at most *finitely many* off-line
  zeros, not RH; the barrier already on record.
- Bombieri, *Problems of the Millennium: the Riemann Hypothesis* (Clay); Sarnak, *Problems of the
  Millennium: RH* — the Euler product as the discriminator; Davenport–Heilbronn (functional equation,
  no Euler product) has off-line zeros.
- Internal: `research/positivity-program.md` (§E–K), `research/work/D-fourier-optimization.md` (§4 —
  the Eisenstein-vs-Hecke litmus that opened this worker), `A-qsm-free-energy.md` (the RH-silent
  edge/real-axis pattern), `C-semilocal-2.md` (Euler product in values, not sign); scaffold
  `falsify.py`, `explicit_formula.py`.
