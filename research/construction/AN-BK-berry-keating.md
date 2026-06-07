# AN-BK — Berry–Keating / quantum chaos (the xp Hamiltonian). Verdict: OPEN_ROAD (but a degenerate, RH-silent one)

*Analytic-side map. 2026-06-06. Discipline: rigorous; [established]/[partial]/[heuristic] tagged.*

## The strategy

Hilbert–Pólya made physical: the zeros `γ` (with `ζ(½+iγ)=0`) are the eigenvalues of the quantization
of a classical Hamiltonian. The candidate is `H = xp` (Berry–Keating 1999; Connes 1999), whose
classical phase-space `xp = E` hyperbolas give, semiclassically, the **smooth (average) counting
function** of the zeros `N̄(E) = (E/2π)log(E/2π) − E/2π + 7/8`. The dream: the **primes are the
periodic orbits** of a chaotic flow, and the Montgomery–Odlyzko law (zero statistics = GUE) is the
fingerprint of a time-reversal-broken chaotic quantum system whose spectrum is the zeros.

Prerequisite (precise): **a genuine self-adjoint operator `H` on a Hilbert space, with discrete
spectrum `= {γ}`, carrying the functional-equation symmetry**, such that self-adjointness is provable
*without* assuming the zeros are real.

## (1) Prerequisite status — UNCONSTRUCTED, and the constructed pieces hit a hard wall

`xp` is **not essentially self-adjoint** as written: on the half-line it is the generator of dilations
`A = ½(xp+px)`, whose spectrum is the *whole real line* (continuous), and on a domain it requires a
choice of boundary condition / self-adjoint extension. The literature splits cleanly:

- **Berry–Keating / Sierra regularization** [partial, established as stated]: regularizing `xp` (a
  hyperbola cutoff `x≥l_x, p≥l_p`, or the closed-orbit variants `x(p+1/p)`, `(x+1/x)(p+1/p)`) yields
  semiclassical energies whose **average** density is `N̄(E)` — the *smooth part only*. This is a
  **theorem about the smooth counting function, not about the zeros.** Sierra–Townsend, Sierra: the
  boundary wave functions make the average zeros appear as **resonances** (poles of a scattering matrix
  on the second sheet), *converging asymptotically toward the average positions* — never the exact
  individual `γ`. (arXiv:1102.5356, 0712.0705, math-ph/0702034.) [established for the *average*;
  the *exact* spectrum is not produced.]

- **Connes (1999)** [established, and decisive on direction]: the adelic/scaling realization gives the
  zeros as an **absorption spectrum** — *missing* lines in a continuum, not eigenvalues of a
  self-adjoint operator. The "minus sign" in the fluctuation term is, in Connes's own framing, the
  structural signature that this is **not** an emission (discrete-eigenvalue) spectrum. This is the
  same phenomenon as the program's stone 1: **resonances ≠ self-adjoint eigenvalues** (the object is
  non-compact; the zeros are scattering data, not a point spectrum). (math/9811068, scalingH.pdf.)

- **Bender–Brody–Müller (2017, PRL 118.130201)** [the strongest modern claim — and it fails its own
  test]: an operator `H ∝ (1−e^{−ip})(xp+px)(1−e^{−ip})^{−1}`, *non-Hermitian*, with `iH`
  PT-symmetric, whose eigenvalues (under a boundary condition tied to `ζ`) are formally the `γ`. BBM
  state explicitly: **"the operator is not self-adjoint, so the reality of its eigenvalues is not
  guaranteed"** — RH would follow *only if* one independently proves `H` is self-adjoint. **Bellissard
  (arXiv:1704.02644) [established critique]**: `H` is obtained from the dilation generator `A` by a
  **non-unitary similarity transform**; a non-unitary change of basis does **not** preserve
  self-adjointness or the reality of the spectrum, so the construction "does not actually work" as a
  proof. The boundary condition that pins the eigenvalues to the zeros is precisely the input that
  would have to encode `ζ(½+iγ)=0` — i.e. it **smuggles in the zeros**, it does not derive them.

**Is the quantization contradictory?** No — unlike de Branges (Conrey–Li: a *specific* positivity
provably incompatible with `ζ`) there is **no theorem forbidding** a self-adjoint `H` with `spec=
{γ}`. The functional equation provides the `t↦1−t` symmetry; GUE statistics are *consistent* with a
genuine chaotic quantizable system. So the prerequisite is **not CONTRADICTORY**. It is
**UNCONSTRUCTED**: every actual construction produces either (a) the *smooth/average* part (BK–Sierra),
(b) a *resonance/absorption* spectrum (Connes), or (c) a *non-self-adjoint* operator whose reality is
exactly the unproven assertion (BBM). The exact discrete self-adjoint realization remains unbuilt.

## (2) Positivity source — the decisive axis: it is NONE / circular, not a new analytic source

Self-adjointness *is* the would-be positivity mechanism (real spectrum = "`F†=F̄`", the §4.1 Step-B
positive-definiteness). But Theorem B′ (`WRITEUP-geometric-obstruction.md` §4.1) already settled the
**generic** structural fact, and BK is an *instance* of it on the analytic side:

> **Self-adjointness reflects RH; it does not force it.** Bare self-adjointness of an operator with the
> right *trace/symmetry* data (Step A, the functional equation) is free; whether the invariant form is
> positive-definite (Step B = real spectrum = RH) is an **independent** condition. A construction that
> derives `H` from its symmetry/trace data alone (as `xp` does) forces only Step A.

Concretely, in the kill-test language (`positivity-program.md` row "self-adjointness (Hilbert–Pólya):
reflects not forces → **RH-neutral** (stone 1)"): the *only* way BK supplies the RH-positivity is to
**impose** self-adjointness/real-spectrum as the boundary condition — which is BBM's move, and which
Bellissard shows is the unproven assumption itself. So:

- It does **not** supply a new analytic source (no estimate, no constructed *self-adjoint* operator
  with provable real spectrum, no positive measure independent of the zeros).
- It **reduces to** the circular positivity: "prove `H` self-adjoint" = "prove the spectrum real" =
  "`F†=F̄`" = the Weil/Hilbert–Pólya positivity restated as an operator condition. The trace of `H`
  reproduces the **explicit formula** (smooth `N̄` + an oscillatory prime/periodic-orbit sum) — i.e.
  the *same* Weil explicit-formula data, in which the positivity *is* RH.

Verdict on the discriminator: **NONE** (it does not address the positivity from a genuinely analytic
source) shading to **REDUCES_TO_WEIL** (the only positivity on offer is the circular self-adjointness).
I record it as **NONE** because BK's actual output (smooth density / resonances / a non-s.a. operator)
does not even reach a positivity *statement*; the moment it tries (BBM's boundary condition) it is the
circular self-adjointness.

## (3) The known obstruction (sharp)

`xp` is the **dilation generator** `A` (continuous spectrum `= ℝ`). Every regularization that makes the
spectrum discrete recovers the **smooth counting function `N̄(E)`** — which is **archimedean data**
(`N̄` is `arg Γ_ℝ` + `arg ζ`-mean), **shared verbatim by Davenport–Heilbronn** and every L-function
with the same `Γ_ℝ`. The *individual* zeros (the Euler-product content) appear only as the
**fluctuation/oscillatory term** = the periodic-orbit (prime) sum, and there they appear as
**resonances / absorption lines**, not eigenvalues. The gap *smooth → exact* and *resonance →
eigenvalue* is exactly the gap *Step A → Step B*. **No regularization has closed it**, and Bellissard
shows the one claimed closure (BBM) is a non-unitary sleight that does not preserve reality.

## (4) Anchor (function field) and DH

- **Function-field anchor** [established]: over `𝔽_q(C)` the Hilbert–Pólya/spectral realization is a
  **theorem** — the zeros are the *eigenvalues of Frobenius* on `H¹_ét`, a genuine finite-dimensional
  operator whose "self-adjointness" (purity `|α|=√q`) is forced by the **Hodge index theorem** on
  `C×C`. So BK's prerequisite *exists and is non-vacuous* in the FF world — but its positivity there
  comes from the **finite ground `q`** (Theorem A: forbidden at `∞`), *not* from a physical Hamiltonian.
  The FF analogue confirms BK is an *open road* (the object exists in the model) while pinpointing that
  what makes it work there (the geometric Hodge positivity over a finite field) is precisely what is
  absent at the archimedean place. The "quantum chaos / periodic orbits = primes" picture is the
  *Selberg/dynamical-zeta* shadow of the Lefschetz–Frobenius trace; analytic content there is the
  trace formula (real), **but the positivity is geometric, not spectral-self-adjointness**.

- **DH kill-test: FAIL [established].** Berry–Keating–Sierra produce **`N̄(E)`**, the smooth density,
  which depends only on `Γ_ℝ` (the gamma factor / functional equation) and **not** on the Euler
  product. Davenport–Heilbronn has the *same* `Γ_ℝ` and *same* `N̄`, yet has off-line zeros. So the
  BK Hamiltonian's principal, provable output is **identical for ζ and DH** — it is **RH-silent /
  Euler-blind** on its self-adjoint (smooth) part. The discrimination would have to live in the
  fluctuation term (the prime/periodic-orbit sum), exactly where BK has only resonances, not a forced
  real spectrum. This is the program's standing pattern (positivity-program.md §E.1): self-adjoint /
  archimedean / GUE data are all DH-shared. **GUE statistics are universal (random-matrix), carry no
  Euler product** — evidence, not proof; the Montgomery–Odlyzko match holds for the *bulk statistics*,
  which DH-type surrogates can mimic.

## Verdict

**OPEN_ROAD** on the prerequisite axis (the self-adjoint quantization is *unconstructed*, **not**
contradictory — no Conrey–Li-type no-go exists), but it is a **degenerate / RH-silent** open road on
the decisive axis: its only positivity mechanism is **self-adjointness, which reflects rather than
forces RH** (Theorem B′ / stone 1) and is therefore **REDUCES_TO_WEIL when pushed to a positivity
claim, NONE as actually delivered**. The DH kill-test **FAILS** (the constructed output is the
DH-shared smooth density). GUE is heuristic evidence, not a construction.

**The precise missing object** (if one insists on the open road): *a self-adjoint operator `H` on a
Hilbert space whose **discrete** spectrum is exactly `{γ : ζ(½+iγ)=0}`, with self-adjointness provable
from the prime/periodic-orbit (Euler-product) data alone — i.e. a quantization whose **positivity comes
from the dynamics (a genuine compact/trace-class resolvent), not from imposing real eigenvalues as a
boundary condition.* No such `H` exists; every candidate delivers the smooth part (BK–Sierra), an
absorption spectrum (Connes), or a non-self-adjoint operator (BBM, refuted by Bellissard). Until the
positivity is supplied by the dynamics rather than assumed, BK is Hilbert–Pólya in physical costume:
the same wall, restated as "prove `H = H*`".

## Sources
- Berry–Keating / Sierra: arXiv:1102.5356, 0712.0705, math-ph/0702034 (H=xp revisited; resonances → average zeros).
- Connes spectral realization (absorption spectrum): arXiv:math/9811068; alainconnes.org/.../scalingH.pdf.
- Bender–Brody–Müller, PRL 118, 130201 (2017), arXiv:1608.03679 (non-Hermitian, PT, "not self-adjoint").
- Bellissard, Comment, arXiv:1704.02644 ("the strategy does not actually work"; non-unitary change of basis from the dilation generator).
- Sierra, "The Riemann zeros as spectrum and the Riemann hypothesis", Symmetry 11(4) 494 (2019).
- Program internal: WRITEUP-geometric-obstruction.md §4.1 (Theorem B′), positivity-program.md §C (HP row), §E.1 (DH-shared archimedean/self-adjoint/GUE data).
