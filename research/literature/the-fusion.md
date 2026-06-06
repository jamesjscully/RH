# The tropical↔spectral fusion — both paths, synthesized (2026-06-06)

The user's thread: *"corner compact and spectrum self-adjoint — tropical and spectral fusion."* We
explored both the **characterization** side (Path 1, `corner_defect.py`) and the **geometry** side
(Path 2, `geometry-of-the-square.md`). This is the honest synthesis — including the §8 correction the
geometry side forced on the characterization side. Tags **[THM]/[PROG]/[CONJ]/[AN]** as before.

## What the two paths found

**Path 1 — the corner, computed (`corner_defect.py`).** The corner is the archimedean fixed point
`u=0` (`ρ=1`). Two computed facts: (1) the archimedean Weil functional **diverges** as a test
function localizes there and **converges** off it (at primes) — the RH trouble is the corner, not the
primes; (2) the corner kernel is **`K_∞(u) ~ −1/(2|u|)`** (verified `K_∞·|u| → −½`), a conformal
Coulomb singularity, so `Δ·Δ ~ −log ε` is log-divergent. This **matches** the Connes–Consani analytic
form **[THM, CC20]**: the trace-remainder `δ(ρ)` has a first-derivative jump at `ρ=1` (`−1 → +1`)
generating a `−2δ'_1` distribution; `W_ℝ → +∞` at `ρ=1`. Same corner, two parametrizations.

**Path 2 — the geometry, current (`geometry-of-the-square.md`).** Headline: **the curve moved, the
square did not.** On the 1-dimensional `\overline{Spec ℤ}`, Connes–Consani now **prove** [THM, RR-Z
2023] an integer-dimensional `H⁰, H¹`, **Serre duality**, and **Riemann–Roch** (over the sphere
spectrum, solving Bost's real-dimension obstruction), and the **Jacobian** [THM, 2026]; Deninger
**constructs** primes-as-periodic-orbits [THM, 2024, via rational Witt vectors]. **But every advance
is on the curve; the square — `H¹(S²)`, the corner compactification, the intersection positivity —
did not move.**

## The §8 correction (geometry corrected characterization)

Path 1, as I first framed it, said: the `−1/(2|u|)` conformal corner is where the scaling Hamiltonian
**gets a self-adjoint extension**, so *compactify the corner ⟺ choose that extension* — "one object
seen twice." **This is wrong, and the geometry side shows exactly why** [THM, CC20, verbatim]:

- the cutoff that compactifies the corner (the `Λ=1` prolate/Sonin projection) *"lack[s] invariance
  under the scaling action ϑ … makes problematic restricting the Hamiltonian"*;
- *"the scaling action ϑ does not restrict to [Sonin's] space"* — so the self-adjoint generator is
  **obstructed, not chosen**;
- Connes–Consani therefore **avoid self-adjointness**, using a **positive projection `S`**: the
  realized statement is the *weaker* `Tr(ϑ(g)Sϑ(g)*) ≥ 0` **[THM, one place `∞`, conditional on the
  `\hat g(±i/2)=0` `H¹`-conditions, support `(½,2)`, no primes]** — a positive operator, **not** a
  self-adjoint one with spectrum = the zeros.

So **"corner-compact ⟺ self-adjoint" is false** in the only construction that realizes any of it.

## The corrected fusion — a tension, not an identity

The honest picture is sharper and more interesting than "one object seen twice":

> The corner-compactness and the self-adjointness are **in tension**. The cutoff that tames the
> `−1/(2|u|)` corner (`Λ=1` Sonin projection) **breaks the scaling invariance** that a self-adjoint
> Hilbert–Pólya generator needs. You can have a **compact corner with a positive projection** (CC20,
> the RH-neutral functional-equation facet, one place), or a **scaling-invariant generator with a
> divergent corner** — *not yet both*. That tension **is** the difficulty, and the user's instinct
> named exactly the two horns that do not yet meet.

The reverse force — the missing object — is precisely a construction that holds **both at once**:
a corner-compact, scaling-equivariant `H¹(S²)` with Serre duality whose self-adjoint generator (or
RH-signed `Δ·Δ`) has spectrum = the zeros.

## The single sharpest blocker (both paths agree)

The **canonical characteristic-1 Frobenius correspondences `Ψ_λ` do not lift from the curve to two
variables** ("the most problematic step"), and characteristic-1 homological algebra yields `H⁰, H²`
but **not `H¹` on a surface**. Equivalently, on the operator side: the corner cutoff yields a
**positive projection, not a self-adjoint operator**. The 1-variable Riemann–Roch/Serre-duality is now
a **theorem**; the 2-variable lift is the wall. There is **no no-go** — three precise obstructions
(BGS §6.3 positivity can genuinely fail; the corner is a divergent analytic boundary, not a projective
closed point; self-adjointness is avoided, not forced) explain why corner-compactification **cannot
automatically** force RH, but none forbids the object.

## Did the characterization reveal a path? (the honest answer)

Partly — by *killing* the easy version and sharpening the real one. The fusion is **not** "regularize
the corner and self-adjointness falls out" (that's the obstructed naive hope). The genuine, precisely-
located target is now:

1. **Lift the `Ψ_λ` / the 2023 curve Riemann–Roch to the square** — the one-variable theorem exists;
   the two-variable `H¹(S²)` with Serre duality is the missing piece, and it is the *active* frontier
   on the geometry side (sphere-spectrum / Segal Γ-ring; possibly condensed/analytic duality for the
   archimedean factor).
2. **Or** resolve the tension directly: find a scaling-equivariant compactification of the corner
   (one that does *not* break invariance the way the `Λ=1` cutoff does) — equivalently a self-adjoint
   generator whose corner is finite. CC20's "move `Δ` into `Σ`" gets the sign but sacrifices
   equivariance and the primes; the open problem is doing it equivariantly and globally.

Neither is a finite handle we can compute our way through — both are the research frontier — but the
thread did real work: it converted "tropical–spectral fusion" from a hope into a **precisely located
tension** with a named blocker (`Ψ_λ` won't lift; the cutoff isn't equivariant), and it tied our
*computed* corner kernel `−1/(2|u|)` directly to the [THM] `δ'`-jump that the geometry must absorb.
