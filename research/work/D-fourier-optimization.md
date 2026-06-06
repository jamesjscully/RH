# Worker D — Fourier-optimization / sign-uncertainty / exact-interpolation vs. the explicit-formula positivity (2026-06-06)

*(§8 discipline: [THM] proven in the literature, [PROG] partial, [CONJ] conjecture, [AN] analogy.
Numerics in `scripts/numerics/witness/fourier_optimization.py`; run
`python3 -m scripts.numerics.witness.fourier_optimization`. Cross-checks defer to the certified
`weil_form.py` (spectral side) and `explicit_formula.py` (prime-side Euler signature).)*

**Task.** Investigate whether the modern Fourier-optimization machinery — Beurling–Selberg extremal
functions in the explicit formula (Carneiro–Chandee–Littmann–Milinovich), the Cohn–Elkies LP and the
Bourgain–Clozel–Kahane sign uncertainty, Radchenko–Viazovska Fourier interpolation and Viazovska's
modular magic functions — is the right tool to **force** the explicit-formula positivity, or whether
it hits the program's standing wall (the archimedean↔prime place-crossing).

**Verdict up front.** The Fourier-optimization machinery is a **majorant machine**: it turns the
explicit formula into a Cohn–Elkies-type linear program and produces sharp *conditional-on-RH*
bounds (prime gaps, `S(t)`, pair correlation). It is genuinely **Euler-borne** (the prime weights
`Λ(n)` are the discriminator; the DH analogue with signed weights breaks the majorant). But on the
decisive axis it is **RH-SILENT as a bound / CIRCULAR as a positivity**: the extremal problem is a
`sup` over the cone `{ĝ ≥ 0}`, which is RH-agnostic; the extremal *constant* never moves when a zero
goes off-line. The **exact-interpolation** branch (Bondarenko–Radchenko–Seip, zeta-zeros-as-nodes) is
the deepest and freshest connection — modular forms make the primes *and* the zeros simultaneously
interpolation nodes — **but the interpolation basis exists unconditionally**; RH is equivalent only
to its *non-redundancy*, so the modular object **records** RH, it does not produce it. **The
modular-magic-function bet is FRESH IN STRUCTURE but WALLED IN POSITIVITY**: its dual (Eisenstein)
certificate certifies the **archimedean** place, where ζ and DH agree — the same place-crossing wall.

---

## 1. The precise reduction — the explicit formula AS a sign-uncertainty / Cohn–Elkies problem

Write the Guinand–Weil explicit formula on an even test `g = φ∗φ̃` so that `ĝ = |φ̂|² ≥ 0` is a
Fourier square (the natural Weil-positivity cone). In the program's normalisation:

```
   Σ_ρ ĝ(γ_ρ)   =   W_arch(g)   −   Σ_{n≥2} (Λ(n)/√n) g(log n)            (EF)
   └ ZEROS ┘         └ ∞-place ┘     └────────── PRIMES (Euler) ──────────┘
```

- **Spectral (zeros) side** `Σ_ρ ĝ(γ_ρ)`. With `ĝ ≥ 0`, this is `≥ 0` **iff every `γ_ρ` is real**,
  i.e. **iff RH** (each `|φ̂(γ)|² ≥ 0`; a complex `γ` from an off-line zero is what breaks it —
  certified in `weil_form.py`).
- **Archimedean side** `W_arch(g) = [pole terms g(±i/2)] + (1/2π)∫ ĝ(t)·(Re ψ(¼+it/2) − log π) dt`.
  The integral runs `ĝ` against the **digamma/Plancherel density `Re ψ(¼+it/2)`** — the ∞-place's
  spectral measure. This density is **SHARED by ζ and DH** (same `Γ_ℝ`) ⟹ **RH-neutral**.
- **Prime side** `Σ Λ(n)/√n · g(log n)`: samples `g` on the **log-prime-power lattice `{log pᵏ}`**
  with the von Mangoldt weights — the Euler-product content.

**Weil positivity** (necessary for RH) is then exactly the **sign-uncertainty inequality**:

> for every even `g` with `ĝ ≥ 0`,  `W_arch(g) ≥ Σ_{n≥2}(Λ(n)/√n) g(log n)`.   **(WP)**

This is **Cohn–Elkies-shaped**: maximise the prime/archimedean ratio `R(g) = P[g]/W_arch[g]` over the
**cone `{ĝ ≥ 0}`**; `R(g) < 1` for all admissible `g` is `(WP)`. The roles:

| Cohn–Elkies LP / BCK sign-uncertainty | explicit-formula positivity |
|---|---|
| sign constraint `f̂ ≥ 0` outside a ball | `ĝ ≥ 0` everywhere — a **`+1`-type** (Fourier-square) constraint |
| forbidden region / "ball" `|x| ≤ r` | the **archimedean density** `Re ψ(¼+it/2)` (RH-neutral) |
| lattice of vectors | the **log-prime-power lattice `{log pᵏ}`** with weights `Λ(n)` |
| dual certificate (sphere-packing optimality) | the **Weil positivity** itself |

**It is a `+1` (Fourier-square) sign-uncertainty, not the `−1` (packing) one.** The `−1` Cohn–Elkies
sign-uncertainty has a genuine forbidden region with a *sharp modular obstruction* (the `E₆`/`E₄`
Eisenstein certificates in `d=8,24`); the `+1` explicit-formula version has its "forbidden region" at
the **archimedean place**, which is exactly where ζ and DH agree. That mismatch is the whole story
(§4).

**Numerics (`weil_pairing`, module §[1]).** On a narrow Gaussian (`σ=0.5`, `ĝ ≥ 0`):
`W_arch = +1.224`, `P_ζ = +0.256` (Euler, `Λ ≥ 0`), Weil margin `= +0.967 > 0` (positive — the
expected Weil-positivity behaviour); the DH prime side `P_DH = +0.023` is structurally different
(signed log-derivative weights `c_DH(n)`). The archimedean side is shared; the **prime side is the
discriminator** — the reduction's central claim, made executable.

---

## 2. State of the art (literature), precise

**(a) Beurling–Selberg majorants in the explicit formula [THM, conditional].** Carneiro–Chandee–
Littmann–Milinovich and collaborators replace the indicator/test in the explicit formula by **optimal
bandlimited majorants/minorants** of exponential type (the Gaussian-subordination framework of
Carneiro–Littmann–Vaaler), then apply the explicit formula to bound:
- the argument function `S(t)`, `S₁(t)` — best known constants, *under RH* (Carneiro–Chandee–
  Milinovich, *On the argument of L-functions*, arXiv:1504.01833) [THM, cond. RH];
- the **largest prime gap under RH** (Carneiro–Milinovich–Soundararajan, *Fourier optimization and
  prime gaps*, arXiv:1708.04122): improved constant in `pₙ₊₁−pₙ ≪ √pₙ log pₙ` [THM, cond. RH];
- **Montgomery pair correlation** (Carneiro et al., arXiv:2310.01913) and **consequences of GRH**
  (arXiv:2411.05095): the explicit formula over Dirichlet characters is reduced to a **semidefinite /
  convex program** solved numerically [THM, cond. GRH].
- Survey: Carneiro–Milinovich–Soundararajan, *Bounds for Zeta and Primes via Fourier Analysis*
  (arXiv:2005.02393).

**The barrier (stated by the authors themselves).** These are **majorant inequalities**, all
**conditional on RH/GRH** — they *consume* RH (real zeros ⟹ `ĝ` is sampled on the real axis) to
*produce* bounds. In the least-quadratic-nonresidue problem the authors note they have matched upper
and lower bounds and have "**essentially arrived at the limit of this method**" (2411.05095). The
archimedean `Γ′/Γ` term is an inherent "forbidden region" no test function removes. **None of this
machinery is claimed to prove RH** — it is a one-sided extremal bound, never the positivity from
below. [BARRIER]

**(b) Cohn–Elkies LP + Bourgain–Clozel–Kahane sign uncertainty [THM].** BCK introduced the `±1`
sign-uncertainty (control the sign of `f` and `f̂`); Cohn–Gonçalves (arXiv:1712.04438) showed the
`+1` sign-uncertainty *is* the LP bound and solved it **optimally in `d=12`** via modular eigenfunction
construction; the `d=8,24` Cohn–Elkies LP is solved by Viazovska's magic functions. New sign-
uncertainty principles (Gonçalves–Oliveira–Steinerberger; Cohn–Gonçalves, arXiv:2003.10771; and the
2025 *Fourier inequalities and sign uncertainty*, arXiv:2505.15994) generalise widely. **No claimed
connection to RH** beyond structural analogy.

**(c) Radchenko–Viazovska Fourier interpolation + Viazovska's modular magic functions [THM].** RV
(*Fourier interpolation on the real line*, IHÉS 2019) reconstruct an even Schwartz `f` from
`{f(√n), f̂(√n)}` via modular-form-built basis functions `aₙ` (eigenfunctions of the Fourier
transform with prescribed nodes); at `x=0` this *is* Poisson summation. Viazovska's `d=8,24` magic
functions are `±1` Fourier eigenfunctions with prescribed sign and prescribed double roots at the
lattice radii — the **only known machine producing an EXACT extremal** (not a bound) for a sign-
uncertainty LP.

**(d) THE key connection — exact interpolation with ZETA ZEROS as nodes [THM, unconditional].**
Bondarenko–Radchenko–Seip, *Fourier interpolation with zeros of zeta and L-functions*
(arXiv:2005.02996, Constr. Approx. 2023). **Theorem 1.1 [THM]:** there exist entire `Uₙ`, `V_{ρ,j}`
such that every even `f ∈ H₁` satisfies

```
   f(z) = Σ_n f̂(log n / 4π) Uₙ(z)  +  Σ_{ρ, j} f^{(j)}((ρ−½)/i) V_{ρ,j}(z)          (1.2 BRS)
```

with time-nodes `{log n/4π}` (**primes via `Λ(n)`**) and frequency-nodes the **zeta zeros
`(ρ−½)/i`**. The basis is built from **weakly holomorphic modular forms for the theta group**. And
their §4.4: the **Riemann–Weil functional `W`** (the LHS of the explicit formula) is *exactly* the
evaluation of `(EF)` in this basis: `W Uₙ = π⁻¹Λ(n)/√n` (`n` a square), `W V_{ρ,0} = 2`. So **the
modular interpolation machine already couples primes (nodes) and zeros (nodes) for ζ.**

**The crucial structural facts [THM, from BRS]:**
1. **The interpolation basis (Thm 1.1) is constructed UNCONDITIONALLY** — the nodes are the zeros
   *wherever they sit*; **RH is never used** in the construction.
2. RH (+ simplicity) is invoked only to *interpret* (1.2) as a **non-redundant** recovery: "Assuming
   for a moment the truth of RH and that all zeta zeros are simple, we may think of (1.2) as a
   confirmative answer to … recover `f` in a non-redundant way." RH ⟺ the basis is a **frame**
   (neither over- nor under-complete) — a **density/completeness** statement (it matches the
   Riemann–von Mangoldt zero-counting density).
3. BRS themselves note the explicit formula `(EF)` "starts from the **Euler product**", whereas the
   interpolation `(1.2)` "is tied to the **Dirichlet series**" — *multiplicative* vs *additive*
   duality. The Euler product enters their picture **only through `W Uₙ = Λ(n)`** — i.e. through the
   explicit formula laid on top of the (RH-free) interpolation skeleton.

**Status table.**

| object | status | RH-relation |
|---|---|---|
| Beurling–Selberg majorants in EF (CCLM) | [THM] | bounds **conditional on RH**; "limit of method" reached |
| Cohn–Elkies LP / BCK `±1` sign-uncertainty | [THM] | structural analogy only; no RH link claimed |
| RV interpolation, Viazovska magic functions | [THM] | exact extremal for *packing*; no RH link |
| BRS interpolation, **zeta zeros as nodes** | [THM, **unconditional**] | basis exists ∀ zeros; **RH ⟺ non-redundancy** (records, not forces) |
| "modular extremal forces the Weil positivity" | **[unexplored / CONJ]** | the bet of §4 — assessed below |

---

## 3. Compute — the LP / extremal problem and the falsifier verdict

**The extremal ratio (`beurling_selberg_ratio`, module §[2]).** Over the admissible cone `{ĝ ≥ 0}`
(narrow Gaussians, where the bare test is a faithful Weil test), the Fourier-optimization ratio
`R(g) = P[g]/W_arch[g]` is positive and `< 1`:

```
 sigma   W_arch     P_zeta      R = P/W_arch   Weil margin > 0
 0.15   516.7      1.13e-5      2.2e-8         True
 0.20    44.5      1.21e-3      2.7e-5         True
 0.30     6.57     3.48e-2      5.3e-3         True
 0.40     2.57     1.25e-1      4.9e-2         True
 0.50     1.22     2.56e-1      2.1e-1         True
 sup R over the family = 0.209 < 1   ⟹ Weil margin positive (the conditional-on-RH bound)
```

This is exactly a **one-sided bound — a `sup` over a cone** — *not* an identity that forces RH. (The
sharp Beurling–Selberg extremals have compactly supported `ĝ` and keep `R<1` across all scales; the
point demonstrated is the **cone structure**, not the optimal constant.)

**The three-axis falsifier (`extremal_candidate_falsified`, module §[3]).** Candidate: a
Beurling–Selberg / Viazovska-style **Euler-borne modular extremal majorant** `g_*` for `(EF)`.

| axis | result | mechanism |
|---|---|---|
| **Euler-borne** (fails DH?) | **YES** | prime weights `Λ(n) ≥ 0` (Euler product); DH's signed `c_DH(n)` break the majorant (verified: `cz` nonneg+prime-power-supported, `cdh` signed) |
| **sees-zeros** (off-line sensitive?) | **NO** as a *bound*; **YES** only as the *positivity* | the Fourier-optimization **bound is a `sup` over `{ĝ≥0}`** — an extremal **constant** that does **not move** when a zero goes off-line (RH-agnostic). It "sees zeros" only when *read as the Weil positivity itself* (the Li functional flips sign at `n*=12` for a planted off-line zero — but that is the spectral side, already RH) |
| **independent** (provable without RH?) | **NO** | the sharp inequality **is** the Weil positivity (= RH, Bombieri–Lagarias/Li) |

**Falsifier verdict (`falsify.py` classifier):**
- read as the **Fourier-optimization bound** → **RH-SILENT** (Euler-borne, but blind to zero
  *locations* — the new category that catches QSM and the prime Gram);
- read as the **sharp inequality** → **CIRCULAR** (= the Weil/Li positivity).

Either way it **does not independently force the zeros on-line**. This is the **same wall** as
stones 1–2 (`scattering_forcing.py`): a correct, Euler-borne forcing functional whose positivity for
ζ is RH itself.

---

## 4. The fresh bet — a Viazovska-style modular magic function as the exact extremal (honest assessment)

**The hope.** Modular forms carry the primes (Hecke eigenvalues / Euler product) ⟹ Euler-borne;
interpolation nodes = the zeros (BRS) ⟹ sees-zeros; so a `+1` modular eigenfunction with roots at the
zeros could be the **exact extremal** that forces `(WP)` — closing the gap the way `E₆` closed
Cohn–Elkies in `d=8`.

**Why it is genuinely fresh [the real novelty].**
- Viazovska's magic functions are the **only** machine that yields an *exact* sign-uncertainty
  extremal (not a bound), via Laplace transforms of weakly holomorphic modular forms with **prescribed
  sign and prescribed roots**. That is precisely the structure `(WP)` would need: a `+1` eigenfunction
  whose roots sit at the zeros.
- BRS make this concrete *for ζ*: their modular (theta-group) interpolation basis has **primes as
  time-nodes and zeta zeros as frequency-nodes simultaneously**, and the Riemann–Weil functional is
  its evaluation. **No other construction couples the two node-sets through a single modular object.**
  This is the freshest lead the whole audit has surfaced for "sees-zeros AND Euler-borne in one
  structure."

**Where it hits the wall [the honest negative].**
1. **The BRS basis exists unconditionally.** The interpolation nodes are the zeros *wherever they
   are*; the construction never uses RH. RH (+ simplicity) ⟺ the basis is **non-redundant** (a frame).
   So the modular object **records RH as a completeness/density fact** — it does not *produce* the
   positivity. Pushing a zero off-line does not break the interpolation; it breaks the
   non-redundancy. **RH is read off, not forced.** (This is the exact analogue, in the interpolation
   language, of stone 1's "reflects not forces.")
2. **The dual certificate sits at the wrong place.** Viazovska's `d=8,24` extremals force a bound
   because the `−1` sign-uncertainty there has a **sharp modular dual certificate** (`E₆`/`E₄`
   Eisenstein series) matching the primal. The explicit-formula sign-uncertainty is `+1` type and its
   "forbidden region" is the **archimedean density `Re ψ(¼+it/2)`**, which is **RH-neutral (shared
   with DH)**. A modular dual certificate built from Eisenstein data would certify the **archimedean**
   place — exactly where ζ and DH **agree**. There is no Eisenstein-type certificate that
   distinguishes on-line from off-line zeros, because the distinguishing data (the Euler product /
   Hecke side) lives at the **primes**, not the modular weight/archimedean normalisation.
3. **Net: FRESH IN STRUCTURE, WALLED IN POSITIVITY.** The modular machine supplies the *exact
   interpolation/extremal structure* (genuinely new — one object, both node-sets). But the positivity
   it must certify is still the Weil positivity, and the modular dual it naturally produces certifies
   the archimedean place. **It would force RH only if a modular form's Euler product (the Hecke side)
   entered the dual certificate** — i.e. only if the modular construction's *primes* (Hecke
   eigenvalues), not its *archimedean weight*, carried the positivity across to the zeros. **That is
   exactly the open cross-place coupling `W_∞ ≥ Σ_p W_p` the whole program is pinned to** (thread 0 /
   workers A, B, C). The modular-magic bet does not dodge the wall — it **re-expresses** it in the
   cleanest available language: *the dual certificate must be Euler-borne (Hecke), not archimedean
   (Eisenstein).*

**Concrete falsifiable next probe (if pursued).** In BRS's basis, the Euler product enters *only*
through `W Uₙ = Λ(n)/√n`. The litmus test: build the **DH** interpolation basis (BRS extends verbatim
to any Dirichlet series with a functional equation — §5 of their paper — and DH *has* one). The basis
will still exist (DH has zeros, a functional equation, a theta-group-type kernel). If the DH basis is
*structurally indistinguishable* from ζ's except in the values `W Uₙ` (which become the **signed**
`c_DH(n)`), that confirms mechanically that **the modular interpolation skeleton is RH-neutral and the
only discriminator is the Euler product in the functional values** — i.e. the modular magic is
RH-silent and the content is `sign Λ`, the program's standing finding. (`fourier_optimization.py`
already exhibits the functional-value split `P_ζ` vs `P_DH`; the full DH-basis construction is the
deeper check, queued — it is a genuine computation, not an afternoon's work.)

---

## 5. Honest framing + auditor deltas

The Fourier-optimization / sign-uncertainty / exact-interpolation approach is **the right modern
language** for the explicit-formula positivity and produces the **best known conditional bounds** — and
the BRS zeta-zeros-as-nodes interpolation is the **freshest single object** coupling primes and zeros.
But measured on the decisive **sees-zeros / independent** axes it lands where every Euler-borne lever
has landed: **RH-SILENT as a bound, CIRCULAR as a positivity**, with the wall **re-expressed** (not
crossed) as "the modular dual certificate must be Euler-borne (Hecke), not archimedean (Eisenstein)."
This is the **7th independent confirmation** that *only the Euler product discriminates, and a
positivity/extremal built on it for ζ that fails for DH does not by itself force the zeros on-line.*

**Deltas to fold into `positivity-program.md`:**

- **§C tracker — new row:**
  | positivity mechanism | kill-test | verdict |
  |---|---|---|
  | Fourier-optimization / Beurling–Selberg–Cohn–Elkies LP + modular (Viazovska/BRS) interpolation | *worker D* | **RH-SILENT (bound) / CIRCULAR (sharp).** The EF positivity *is* a `+1` sign-uncertainty LP over `{ĝ≥0}`; Euler-borne (DH's signed prime weights break the majorant) but the extremal *constant* is RH-agnostic. BRS's modular interpolation has **primes & zeta-zeros as simultaneous nodes** (genuinely fresh) yet the basis **exists unconditionally — RH ⟺ non-redundancy**; its dual (Eisenstein) certificate sits at the **archimedean** place where ζ=DH. Forces RH only if a **Hecke/Euler dual certificate** replaces the Eisenstein one — = the open cross-place coupling. |

- **§B auditor — new row:**
  | function-field structure | over ℤ | status / breakpoint |
  |---|---|---|
  | exact Fourier interpolation (Viazovska modular magic; nodes ↔ a discrete spectrum) | BRS interpolation: time-nodes `{log n}` (primes via `Λ`), freq-nodes the **zeta zeros** | **transfers as STRUCTURE** (one modular object couples primes & zeros; Riemann–Weil functional = its evaluation). **breaks at positivity**: basis exists ∀ zero-locations (RH never used); RH ⟺ non-redundancy/frame property (density), not a forced positivity. The extremal/dual is archimedean (Eisenstein), RH-neutral; the discriminator stays the Euler-product functional values `W Uₙ = Λ(n)` |

- **§E durable lessons — addendum (7th confirmation):** the Fourier-optimization/sign-uncertainty
  language reduces `(WP)` to a Cohn–Elkies LP whose forbidden region is the **archimedean** density —
  RH-neutral by construction. Even the modular *exact-extremal* machine (the one thing that turns a
  sign-uncertainty bound into an *identity* for packing) cannot transfer the trick to RH, because its
  dual certificate certifies the archimedean place. **The exact-interpolation insight sharpens the
  wall to a one-line litmus: a forcing extremal must carry an Euler/Hecke dual certificate, not an
  Eisenstein one.**

---

### Module
`scripts/numerics/witness/fourier_optimization.py` — `archimedean_density` (the `Re ψ(¼+it/2)`
forbidden region), `weil_pairing` (the three pieces of `(EF)` for ζ and DH; Weil margin), `_gaussian_pair`
(the `+1` Fourier-square cone), `beurling_selberg_ratio` (the extremal ratio `R=P/W_arch`),
`extremal_candidate_falsified` (the three-axis verdict), `MODULAR_BET` (the assessment). Run
`python3 -m scripts.numerics.witness.fourier_optimization`.

### Sources
- Carneiro, Milinovich, Soundararajan, *Fourier optimization and prime gaps*, arXiv:1708.04122 (the
  extremal problems; "limit of this method").
- Carneiro, Chandee, Milinovich, *On the argument of L-functions*, arXiv:1504.01833 (Beurling–Selberg
  bounds for `S(t)`, cond. RH).
- Carneiro, Milinovich, Soundararajan, *Bounds for Zeta and Primes via Fourier Analysis*,
  arXiv:2005.02393 (survey).
- *Fourier optimization and consequences of the GRH*, arXiv:2411.05095 (EF → SDP; archimedean
  forbidden region; barrier).
- Carneiro et al., *Fourier optimization and Montgomery's pair correlation*, arXiv:2310.01913.
- Carneiro, Ismoilov, Ramos, *Sign uncertainty and de Branges spaces*, arXiv:2408.01186 (sign
  uncertainty ↔ de Branges ↔ L-function zero bounds).
- Cohn, Gonçalves, *An optimal uncertainty principle in twelve dimensions via modular forms*,
  arXiv:1712.04438 (`+1` sign-uncertainty = LP; modular eigenfunction).
- Gonçalves, Oliveira e Silva, Steinerberger / Cohn–Gonçalves, *New sign uncertainty principles*,
  arXiv:2003.10771; *Fourier inequalities and sign uncertainty*, arXiv:2505.15994.
- Radchenko, Viazovska, *Fourier interpolation on the real line*, Publ. IHÉS 129 (2019).
- **Bondarenko, Radchenko, Seip, *Fourier interpolation with zeros of zeta and L-functions*,
  arXiv:2005.02996, Constr. Approx. (2023)** — the key object: modular interpolation with zeta zeros
  as nodes; Thm 1.1 (unconditional); §4.4 (Riemann–Weil functional = basis evaluation).
- Cohn, *From sphere packing to Fourier interpolation*, Bull. AMS 61 (2024), arXiv:2407.14999 (survey).
- Internal: `research/positivity-program.md` (§E–H), `research/work/A-qsm-free-energy.md`,
  `research/work/B-prime-reflection.md`; scaffold `weil_form.py`, `explicit_formula.py`,
  `scattering_forcing.py`, `falsify.py`.
