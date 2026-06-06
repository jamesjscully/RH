# Thread 6 — the two-worlds merger: function fields ⊕ Selberg (2026-06-06)

**The bet (from `positivity-program.md` §A.6):** RH is *proven* in two worlds —
**function fields** (geometric: Frobenius eigenvalues + Hodge index on `C×C`, Weil/Deligne **[THM]**)
and **hyperbolic surfaces** (spectral: self-adjoint Laplacian, zeros = eigenvalues, Selberg **[THM]**).
The missing arithmetic object is their **fusion**, and the merger is supposed to force the positivity
that neither world has alone: function fields have **Hodge-index positivity** but a *discrete* Frobenius;
Selberg has a *self-adjoint* Laplacian but **no Euler product / no arithmetic**. Our stone-1 work
(`2026-06-06-scattering-stone1.md`) found the two worlds *meet* at the archimedean conformal boundary —
the cusp of `PSL(2,ℤ)\ℍ`, where the scattering matrix `S(s)=Λ(2s−1)/Λ(2s)` literally **is** the
completed ζ. This thread asks precisely: what object is genuinely both at once, where do the two
positivities have to become one statement, and is the merger a path to the positivity or does it
inherit both worlds' obstructions.

Tags **[THM] / [PROG] / [CONJ] / [AN]**, §8 throughout: theorems quoted, programs marked, analogies
flagged. No fabrication.

---

## 0. The two worlds, stated as positivities (so we can ask if they're the same)

**World A — function fields (geometric / Hodge).** For a smooth projective curve `C/𝔽_q`, RH for
`ζ_C` is Weil's theorem **[THM]**. The load-bearing positivity is the **Hodge index theorem** on the
surface `C×C`: on the primitive part of the Néron–Severi group the intersection pairing is
**negative-definite**, `(D·D) ≤ 0` for `D` orthogonal to the polarization. Applied to the
correspondence `D = Frob − (deg)·Δ` (Frobenius graph minus a multiple of the diagonal), negative-
definiteness of `(D·D)` forces `|α_i| = q^{1/2}` for the Frobenius eigenvalues — i.e. the zeros on the
critical line. **[THM]** (Weil; modern: the same positivity is Faltings–Hriljac over Arakelov bases —
see `curvature-spectral-lead.md`, where we noted the *generic* Arakelov sign is already this negative
sign with **no RH input**.)

**World B — Selberg / hyperbolic (spectral).** For a **compact** hyperbolic surface `Γ\ℍ` the Selberg
zeta `Z(s)` satisfies RH **[THM]**: its nontrivial zeros sit at `s = ½ ± i r_n` with `λ_n = ¼ + r_n²`
the eigenvalues of the Laplacian `Δ_hyp`. The load-bearing positivity is **self-adjointness**:
`Δ_hyp ⪰ 0` is self-adjoint, so `λ_n ≥ 0` are real, so `r_n` real (for `λ ≥ ¼`), so `Re s = ½`.
**[THM]** (the chain we recorded in `curvature-spectral-lead.md`: negative curvature ⟹ self-adjoint
positive Laplacian ⟹ real spectrum ⟹ zeros on the line).

So the two positivities are, literally:

| world | positivity | what it pins |
|---|---|---|
| A (Hodge) | `(D·D) ≤ 0` on primitive `NS(C×C)` | Frobenius eigenvalues on `|α|=q^{1/2}` |
| B (spectral) | `Δ ⪰ 0` self-adjoint, `λ_n ≥ ¼` | Laplace eigenvalues real, zeros on `Re s = ½` |

**The thread's question is whether these are two faces of one positivity.**

---

## 1. The most concrete object that is genuinely BOTH worlds at once

The single most concrete both-worlds object is **Connes–Consani's Arithmetic Site together with its
Scaling Site** (`arXiv:1405.4527` *The Arithmetic Site*; `arXiv:1502.05580` *Geometry of the Arithmetic
Site*; Bristol-2018 *Riemann–Roch strategy* slides). It is explicitly engineered to be both:

- **Geometric / function-field side (world A).** The Arithmetic Site is a **semiringed topos**
  (the topos `[0,∞)⋊ℕ^×` dual to the multiplicative monoid of positive integers, with the **tropical /
  min-plus semiring** as structure sheaf) built to be the **analogue of a curve over 𝔽_q**. Its
  **square** carries a *one-parameter semigroup of Frobenius correspondences* `Frob_λ` (`λ ∈ ℝ_+^×`),
  realized as sub-objects (Newton polygons) of the square — the explicit analogue of the
  Frobenius graph on `C×C` **[PROG]**. Connes–Consani develop **Cartier divisors, theta functions, and
  a Riemann–Roch formula** on the (quasi-tropical) Scaling Site, with **real-valued dimensions** (type-II
  index theory), paralleling Weil's adelic proof of Riemann–Roch for function fields. **[THM for the
  RR formula itself; PROG for its use toward RH.]**

- **Spectral / scaling-flow side (world B).** The **Scaling Site** carries the **scaling action of
  `ℝ_+^×`** — the continuous analogue of the discrete Frobenius. The set of geometric points of the
  Arithmetic Site over the tropical reals is exactly **Connes' adèle class space**
  `𝔸_ℚ/ℚ^× mod \hat{ℤ}^×`, on which the scaling flow's periodic orbits are the **primes** and whose
  semilocal trace formula reproduces the **Weil explicit formula** as a Lefschetz trace **[PROG]**.
  This is the spectral/dynamical face: ζ-zeros appear as an **absorption spectrum** of the scaling
  action (Connes 1999), i.e. as **resonances**, not as a manifest self-adjoint eigenvalue list.

What it provides that neither world alone does: **a single space where the Frobenius-correspondence
language (Hodge side) and the scaling-flow/trace-formula language (spectral side) live on the same
object**, with a Riemann–Roch theorem already proven on it, and with the Weil explicit formula already
recovered as a Lefschetz trace. It is the closest existing realization of "be both at once."

**The honest caveat (and the reason this is `[PROG]` not `[THM]` for RH).** The Connes–Consani
program **stalls at exactly the place this thread is about**: to run Weil's proof they need the
**positivity** of the trace-formula / Weil functional — equivalently, the Hodge-index inequality on
the *square* of the Scaling Site — and **that positivity is unproven**. Their `arXiv:2006.13771`
*Weil positivity and trace formula, the archimedean place* (Selecta 2021) proves the positivity at the
**single archimedean place** (via prolate-spheroidal wave functions and Hermitian Toeplitz matrices),
and states that "all the concepts and tools make sense in the general semilocal case, **where Weil
positivity implies RH**" — i.e. **the global / equivariant extension to the primes is exactly what is
missing.** This is *precisely* thread-0's "CC20 global/equivariant extension" wall, reached from the
two-worlds side. **[THM: archimedean positivity. PROG/open: the global extension = RH.]**

**Runner-up both-worlds object: Deninger's foliated dynamical systems** (`empslocal.ex.ac.uk/.../
deninger.htm`; recent `arXiv:2410.20758`, `arXiv:2508.15971`). Deninger posits a **foliated laminated
space with an `ℝ`-flow** whose **primitive compact orbits are the primes** (geometry: leafwise
cohomology `H^i`, a Lefschetz trace; spectral: the flow generator's infinitesimal action on reduced
leafwise cohomology gives the zeros as its **spectrum**). `arXiv:2410.20758` **proves Deninger's
conjectured regularized-determinant formula** for 3-dimensional Riemannian foliated systems via a
distributional dynamical Lefschetz trace **[THM]**, and `arXiv:2508.15971` connects Deninger's systems
to Connes–Consani's adelic spaces **[THM]**. But Deninger's RH step **explicitly requires an analogue
of "Weil's RH (= Hodge index positivity) for singular foliations,"** which is **unproven** — the same
wall, in foliation language. **[PROG/open.]**

So: the most concrete both-worlds object is **Arithmetic Site ⊕ Scaling Site**; what it *provides* is a
proven Riemann–Roch and a recovered explicit formula on one space; what it *lacks* is the positivity —
and the lack is identical to thread-0's wall.

---

## 2. Where Hodge-positivity and spectral-positivity WOULD unify — and why they don't yet

The two positivities are supposed to unify at **one identity**, the **trace-formula = intersection
pairing** identity:

> **(Lefschetz/Weil bridge).** The Weil explicit formula is simultaneously
> **(A)** a **Lefschetz trace** `∑_i (−1)^i Tr(Frob | H^i)` (Hodge world, an intersection number on the
>   square), and
> **(B)** a **trace formula** `∑_n h(r_n)` over the spectrum of a flow generator / Laplacian (spectral
>   world). Setting `(A) = (B)` is the place the two positivities have to become the same statement.

Concretely the unification point is: **the quadratic form `Q(f) = ⟨f, f⟩_Weil`** (the Weil pairing /
explicit-formula functional, our `weil_form.py`) must equal **both**

- `−(D_f · D_f)` for the correspondence `D_f` attached to test function `f` on the square `S²`
  (so `Q ⪰ 0` ⟺ Hodge index `(D·D) ≤ 0`), **and**
- `‖P f‖²` / `Tr(ϑ S ϑ^*)` ≥ 0 for the compression of the scaling action to a Hilbert subspace
  (so `Q ⪰ 0` ⟺ self-adjoint positivity of a generator) — this is exactly the CC20 archimedean
  identity `W_∞ ≥ Tr(ϑSϑ^*) ≥ 0`.

**If both hold, they coincide:** `−(D·D) = Q = ‖Pf‖² ≥ 0`. The Hodge-index negativity and the
operator-positivity are then **the same number**, and RH follows. This is the merger's whole point, and
it is *real*: CC20 proves exactly this coincidence **at the archimedean place** (Tr of compression =
Weil distribution up to a controlled prolate-spheroidal defect, which is ≥ 0).

**Why they don't unify yet — three precise failures, one per structural gap:**

1. **No `H¹` on the square (the geometric leg fails first).** The whole `(D·D)` language needs the
   **surface** `C×C` and its `H²`/`NS`. Over ℤ there is **no `H¹(S²)`**: our analogy auditor already
   records "`C×C` → the square `S²` **breaks**: no `H¹(S²)`; `Ψ_λ` don't lift to two variables"
   (`positivity-program.md` §B). Connes–Consani build a Scaling **Site** and its square, but the
   cohomology that would carry `(D·D)` with the right finiteness is **not yet constructed** with a
   provable Hodge index. So leg (A) of the bridge has no object to be a number on. **[open]**

2. **The Frobenius is continuous, not discrete (the merger's defining tension).** This is the *exact*
   mismatch the thread names. Function-field Hodge positivity uses a **discrete** `Frob` whose graph is
   a genuine divisor with a finite self-intersection. The spectral world's generator is the
   **continuous** scaling `ℝ_+^×`, which **contains the identity**, so the diagonal's self-intersection
   **diverges**: `Δ·Δ = ∞` (`lift_obstruction.py`; auditor row 1: "Frobenius `Fr` (discrete) → scaling
   `ℝ_+^×` (continuous) **breaks**"). The merger requires fusing a discrete `Frob` (so `(D·D)` is
   finite) with a self-adjoint flow (so the spectrum is real). **These two demands pull opposite ways:
   discretizing kills self-adjointness of the flow; keeping the flow self-adjoint kills the finite
   intersection.** This is `curvature-spectral-lead.md`'s **Janus** observation promoted to the merger
   level: the `−1/(2|u|)` corner is *both* the negative (Hodge) sign *and* the failure of essential
   self-adjointness of the scaling generator. The two positivities want the **same** object to be
   *both* a finite-intersection divisor *and* a self-adjoint flow, and the corner says it can't be
   both at the identity. **[the structural obstruction]**

3. **Spectral side is RESONANCES, not self-adjoint eigenvalues (stone 1).** Even granting the spectral
   leg, the modular/scaling spectral object that carries ζ is **non-compact** (it has a **cusp /
   continuous spectrum**). On `PSL(2,ℤ)\ℍ` the ζ-zeros are **scattering resonances** — poles of
   `S(s) = Λ(2s−1)/Λ(2s)` (continuous-spectrum data) — **not** discrete `L²` eigenvalues of a
   self-adjoint Laplacian. The Selberg-RH **[THM]** is a theorem only for **compact** surfaces (pure
   point spectrum); the modular surface is non-compact, and its resonances are **not** governed by
   self-adjointness. Our stone-1 kill-test made this exact and load-bearing: `|S(½+it)| = 1`
   (unitarity / self-adjoint structure) **is RH-NEUTRAL** — it holds verbatim for an off-line-zero
   (DH-type) function, which then has an **off-line resonance**. So the spectral world's
   self-adjointness/unitarity **does not transport** to the ζ object: it *reflects* the zeros as
   resonances but does **not force** them onto the line. **[THM/verified, stone 1]**

**Net:** the unification point (trace = intersection, `Q = −(D·D) = ‖Pf‖²`) is correctly identified and
is *literally proven at the archimedean place*. It fails to globalize because (1) the square has no
cohomology carrying `(D·D)`, (2) continuous-Frobenius vs discrete-Frobenius is a genuine contradiction
at the diagonal, and (3) the only spectral realization that *has* the arithmetic (the cusp / scaling)
delivers **resonances**, whose self-adjointness is RH-neutral.

---

## 3. Is the merger a genuine path to the POSITIVITY, or does it inherit both worlds' obstructions?

**Verdict: it inherits both worlds' obstructions — but it also localizes the *one* missing ingredient
more sharply than either world alone, which is its real (limited) value.**

- **It does NOT inherit a contradiction-free shortcut.** The merger's hope was that *combining* a
  defect-free Hodge positivity (world A) with a defect-free self-adjointness (world B) cancels each
  world's weakness. But the auditor + stone-1 show the two weaknesses are **the same weakness wearing
  two masks**: world A's missing object over ℤ is precisely the *non-compact/continuous* corner that
  world B has to confront as the cusp, and world B's self-adjointness is precisely the structure that
  (stone 1) is RH-neutral on the corner that world A needs to make finite. The merger therefore
  **inherits both** the missing-`H¹(S²)` obstruction (A) **and** the resonances-not-eigenvalues
  obstruction (B); they do not cancel, they **coincide** (the `−1/(2|u|)` Janus corner).

- **What is genuinely gained.** The merger is not a path *through* the wall, but it is the **sharpest
  available statement of what the wall is**: the missing positivity is *exactly one functional* —
  `Q(f) = −(D_f·D_f) = ‖Pf‖²` — which must be **Euler-product-borne** (the only thing ζ has that DH
  lacks; stone 1, kill-test) and which **CC20 already proved at one place**. The merger says the global
  RH = *globalizing one already-proven local positivity equivariantly past one place*. That is
  thread-0's wall, now **triangulated from three independent directions** (Hodge square, Selberg
  spectral, scattering resonances) that all land on the same functional. Triangulation is real progress
  of *localization*; it is **not** new forcing.

- **Kill-test compliance.** Self-adjointness/unitarity already **failed** the standing kill-test
  (auditor §C: "self-adjointness — reflects not forces — **RH-neutral**, stone 1"). The merger does not
  rescue it: adding the Hodge side does not make the *spectral* positivity Euler-borne, and the Hodge
  side has no object to be positive on. **The merger as such has no Euler-product-borne lever that
  survives the kill-test** — it relabels the wall, it does not pass it.

So: **genuine path? No — it inherits both obstructions, which are one obstruction.** Genuine *value*?
Yes, but only as the tightest localization: RH ⟺ globalize the CC20 archimedean Weil positivity
equivariantly to the primes, and the merger proves this is simultaneously the Hodge index on the
Scaling Site's square. The forcing itself remains absent.

---

## 4. The single most concrete next step

**Make the trace = intersection bridge of §2 falsifiable on the off-line control — i.e. extend the
stone-1 / `weil_form.py` scaffold to test whether the Hodge-index quadratic form `−(D_f·D_f)` on the
Scaling-Site square is Euler-product-borne, by checking it FAILS for the DH / off-line-zero function.**

Concretely (one script, reusing existing scaffold):

1. Take the Weil functional `Q(f)` already implemented in `weil_form.py` (demonstrated RH-detector) and
   the off-line-zero control `S_offline` already in `scattering.py`.
2. Express `Q(f)` in the **two** §2 forms on the *same* test functions: (A) as the scaling-action
   compression trace `Tr(ϑ S ϑ^*)` (CC20 archimedean side), (B) as the resonance-sum / scattering-phase
   derivative `d/dt arg S(½+it)` (Birman–Krein, stone-1 "Weil bridge").
3. **Kill-test the equality `(A) = (B)` against `S_offline`.** The honest, decisive question: at the
   archimedean place CC20 proves `(A) ⪰ 0`; does the *off-line* function break (A)=(B), or does it (like
   unitarity in stone 1) pass both verbatim? If the off-line control **passes** both `(A)` and `(B)`,
   then the trace=intersection bridge is **also RH-neutral** at one place — confirming that the *only*
   place positivity can become Euler-borne is the **global/semilocal** coupling across places, and
   pinning down *which cross-place term* DH must violate. If it **fails**, that term is the first
   Euler-product-borne forcing object found — feed it straight into the kill-test scaffold.

This is immediately falsifiable (the `S_offline` control already exists), it does not require building
`H¹(S²)` (it works on the test-function functional, not the unconstructed cohomology), and its outcome
either (i) localizes the missing forcing to a *specific cross-place term* of the semilocal trace
formula — the exact gap CC20 leaves open — or (ii) surfaces the first non-RH-neutral functional. Either
way it advances thread-0's "state-of-art global extension" question with a concrete numerical witness.

**One-line bottom line.** The best both-worlds object is **Connes–Consani's Arithmetic ⊕ Scaling
Site** (proven Riemann–Roch + recovered explicit formula on one space; CC20 archimedean Weil positivity
proven); the two positivities would unify at **`Q(f) = −(D·D) = ‖Pf‖² ≥ 0`** (trace = intersection),
which holds at one place but fails to globalize because the square has **no `H¹`**, the Frobenius is
**continuous not discrete** (`Δ·Δ=∞`), and the ζ-spectrum is **resonances not self-adjoint eigenvalues**
(RH-neutral, stone 1); the merger therefore **inherits both obstructions as one** and is **not** a new
forcing — but it is the tightest localization of the wall; next step is to **kill-test the
trace=intersection bridge against the off-line control** to find which cross-place term DH must violate.

---

## Auditor deltas (to fold back into `positivity-program.md`)

New §B rows:
- `Frob graph on C×C (one divisor, finite (D·D))` over ℤ → `Scaling-Site square Frob_λ, λ∈ℝ_+^×` —
  **breaks**: continuous semigroup ⟹ no single finite-self-intersection divisor (same `Δ·Δ=∞` corner).
- `Selberg-RH (compact surface, pure point spectrum)` over ℤ → `modular/scaling object (cusp,
  continuous spectrum)` — **breaks**: ζ-zeros are scattering **resonances**, not self-adjoint
  eigenvalues; Selberg's self-adjoint forcing is **not available** (stone 1, RH-neutral).
- `trace = Lefschetz intersection (function field)` over ℤ → `Weil explicit formula = CC20 semilocal
  trace` — **transfers as identity**; the attached positivity `Q=−(D·D)=‖Pf‖²` **proven at the
  archimedean place (CC20)**, **open globally/equivariantly** (= thread-0 wall).

New §C tracker row:
- two-worlds merger (Arithmetic⊕Scaling Site) — kill-test: *inherits* both obstructions; no
  Euler-borne lever beyond CC20's open global extension — **relabels the wall, does not pass it**
  (RH-neutral as a merger; the live edge is the CC20 global extension, thread 0).

---

### Sources
- A. Connes, C. Consani, *The Arithmetic Site*, arXiv:1405.4527.
- A. Connes, C. Consani, *Geometry of the Arithmetic Site*, arXiv:1502.05580.
- A. Connes, *The Riemann–Roch strategy* (Bristol 2018 slides), aimath.org.
- A. Connes, C. Consani, *Weil positivity and trace formula, the archimedean place*,
  arXiv:2006.13771 (Selecta Math. 2021).
- C. Deninger, *Some ideas on dynamical systems and the Riemann zeta function*,
  empslocal.ex.ac.uk/people/staff/mrwatkin/zeta/deninger.htm.
- *Regularized determinant formulas for the zeta functions of 3-dimensional Riemannian foliated
  dynamical systems*, arXiv:2410.20758.
- *On a relation between Deninger's foliated dynamical systems and Connes–Consani's adelic spaces*,
  arXiv:2508.15971.
- Lax–Phillips, *Scattering Theory for Automorphic Functions* (AM-87); Friedman–Jorgenson,
  *The determinant of the Lax–Phillips scattering operator*, arXiv:1603.07613.
- Internal: `research/the-lift-program.md`, `research/positivity-program.md`,
  `research/literature/curvature-spectral-lead.md`,
  `research/log/2026-06-06-scattering-stone1.md`; scaffold `scattering.py`, `weil_form.py`,
  `lift_obstruction.py`, `harness.py`.
