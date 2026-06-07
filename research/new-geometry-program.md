# The new-geometry program — constructing the geometry that forces the radius (2026-06-06)

The seven-instrument map (`research/the-complete-account.md`) proved that **every known geometry forces
purity only by importing a finite ground `𝔽_q`, which `ℤ` provably lacks at `∞`.** The residue — the
reality condition `F†=F̄` / the proper boundary / the archimedean Weil-II monodromy — is therefore not a
gap in our search of *existing* geometries; it is a demand for a **new** one. This is now the target.

## The goal, stated as a falsifiable spec

> **Construct a geometry that forces Step B — the radius `|α|=√q` = `F†=F̄` = purity — *archimedean-
> natively, without a finite ground*.** Step A (the functional equation / Poincaré duality / the trace)
> is free and supplied by many known geometries; it is not the target. Step B is.

**The novelty test (what makes a geometry genuinely new, not a re-skin of a tested one):** it must
**pass the radius-forcing test all seven known instruments FAIL** — force `|α|=√q` on the anchor without
assuming the zeros, and *fail to exist* for Davenport–Heilbronn (`falsify.py`). Equivalence to a known
geometry ⟺ it reads the same value (Step A only). So "new" is sharp and falsifiable: **clears Step B.**

## The abstracted axiom `P*` (reverse-engineered from purity)

Over `𝔽_q`, purity is forced because the eigenvalues are **Weil numbers** (algebraic, all Galois
conjugates one modulus), pinned by **finite-dimensional cohomology with a bounded weight filtration**.
The finite ground enters *only* to make the cohomology finite-dimensional and the Frobenius algebraic.
Abstract that away:

> **`P*`:** the archimedean fibre has a **finite / dualizable** cohomology carrying a self-map whose
> spectrum is **rigid (all conjugates one modulus) by a structural symmetry** — not a metric, not a
> finite field. A new geometry = any honest realization of `P*` that is `ζ`-satisfiable.

## Method (per candidate)

1. **Mechanism:** how does the candidate geometry properize / finitize an archimedean transcendental
   object, and is "infinite product → finite/algebraic" genuinely what it does?
2. **Anchor:** does it recover `|α|=√q` over `𝔽_q` (or for finite primes) without assuming the zeros?
3. **`ζ`-model:** is the archimedean fibre of `\overline{Spec ℤ}` an object of this geometry?
4. **Force B or only A:** does it force the radius, or reproduce only the FE/edge (the universal failure)?
5. **Falsify:** fails for DH? Distinguish `[BUILT]/[computed]/[circular]/[aspirational]`.

## The candidates (untested, each attacks the right half)

- **(1) Tame / o-minimal geometry [FIRST].** A genuinely different geometry of the reals — a finiteness
  theory for archimedean/transcendental objects. Bakker–Klingler–Tsimerman use o-minimal GAGA to force
  **period maps to be algebraic** — i.e. o-minimality *properizes transcendental archimedean objects*.
  Bet: the archimedean fibre's proper boundary is a **tame-finiteness**, the radius forced by o-minimal
  algebraicity. Archimedean-native, not finite-prime-indexed, not a metric. The crux: is the archimedean
  fibre **tame** (properizable, a lead) or **wild** (non-o-minimal — the no-go locating itself)?
- **(2) Frobenius-first / dynamical geometry.** Invert the foundation: take the **Frobenius as primitive**
  (an abstract self-map with the explicit-formula Lefschetz trace and `F·F†=[q]` scalar) and *define* the
  space as what it coherently acts on (Tannaka for a dynamical datum); the radius forced by reconstruction-
  coherence, not imposed.
- **(3) A symmetric-monoidal category of archimedean motives** where the archimedean fibre is dualizable
  *and canonically polarizable* — the polarization positivity a **coherence theorem of the category**,
  not an axiom.

## Candidate 1 (o-minimal) — RESULT: NOGO_BLUEPRINT (`research/construction/NG-omin-*.md`)

All three angles agree by independent routes. The BKT o-minimal-GAGA mechanism is REAL (transcendental
archimedean → algebraic/finite) **but PROPERNESS IS AN INPUT, not an output** — the o-minimal analogue
of the imported finite ground. The archimedean fibre is **provably WILD**: `Γ_ℝ` has an infinite-discrete
pole spectrum `{0,−2,−4,…}`, non-definable in *any* o-minimal structure (van den Dries finiteness — a
type-obstruction). The tame/wild line is exactly **proper↔open = polynomial↔infinite-product =
finite-prime↔archimedean**, and the fibre is wild *exactly where RH lives*.

**The blueprint (the no-go crystallizing):** across every instrument, **Step B is never *created* by a
geometry — always *imported* via a finite ground / properness.** Emerging theorem-shaped claim:

> **The geometric no-go (conjecture): every purity-forcing geometry imports a finite ground; none
> manufactures properness from a wild archimedean fibre.**

So **candidate 2 (Frobenius-first) is precisely the test of whether this conjecture is FALSE** — the one
approach that tries to *create* the finite spectrum (posit the Frobenius, reconstruct the space) rather
than import it. Binary: does it FORCE `F·F†=[q]` from consistency (gap non-empty, new geometry), or does
positing the Frobenius *import* the finite ground (second instance of the no-go theorem)?

## The honest fork (both outcomes are real results)

Building the geometry and proving it cannot be built are the **same investigation**. Either **(a)** the
gap `P*` is non-empty — a new geometry realizes "force purity with no finite ground," and RH falls to it;
or **(b)** the gap is provably empty — *every* purity-forcing geometry must import a finite ground `ℤ`
lacks at `∞` — a **no-go theorem: RH is not provable by geometry** (a geometric independence statement).
Grothendieck's move: **try to prove the gap empty, and watch where the proof fails — the failure is the
blueprint for the new geometry.**
