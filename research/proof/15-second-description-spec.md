# 15 - Spec: a description of the Weil form that does not pass through the explicit formula

Status: DESIGN SPECULATION (recorded 2026-06-09), not a theorem and not a plan.
This is the answer to "what would have to sit in the place of the missing
geometry, given that our analytic substitute (docs 01-13) forked back into the
explicit formula?" It is constrained on every side by proven results: the
no-go preprint (no finite characteristic at infinity; similitude
underdetermines signature), the E1-E4 must-encodes (doc 10), the no-go map
(docs 09-12), the fork protocol (doc 14), and the margin-thinness law.

## 1. Why the substitution failed, stated structurally

Weil's function-field proof has TWO descriptions of one form:

```text
spectral:   zeros of Z(C)            <- where the difficulty reads off
geometric:  intersection numbers on   <- where the sign is PROVED, by the
            the surface C x C            Hodge index theorem (a signature
                                          statement from finite-dimensional
                                          cohomology; no point counting)
```

The proof never controls the zeros; it controls a signature on the square and
lets the comparison isomorphism do the rest. Our program built candidate
second descriptions (nested Schur cone, passive realization, edge-compliance
geometry) - but every one was DERIVED from EF-bound data (digamma + atoms +
filtration), so each was the spectral description in new clothes. The fork
test (doc 14) now detects this in an hour.

## 2. The spec (five clauses)

A genuine second description D consists of:

```text
S1 (carrier). A space / category / algebra X attached to Z (or Q), built from
   structure ORTHOGONAL to the distribution of primes. Primes may label
   generators; their POSITIONS (the content of psi(x) - x) must not enter
   X's construction. Litmus: X's definition should be writable without ever
   stating the prime number theorem or any zero-free region.

S2 (doubling). X must be square-like: two commuting copies of the arithmetic,
   so that correspondences COMPOSE. This is the role of C x C, and it is
   exactly what the no-go theorems forbid at the literal scheme level (the
   self-product of Spec Z over the absolute point, with a finite ground at
   the archimedean place). The spec therefore demands a NON-SCHEME square -
   a categorified or operator-theoretic doubling that evades the
   characteristic obstruction because it is not a geometry with an
   infinity-fiber.

S3 (native positivity axiom). X carries a sign-producing principle of the
   soft/discrete kind (margin thinness kills everything else):
   signature/index (Hodge-index type), trace positivity (tau(x* x) >= 0 in an
   operator algebra), unitarity/quantum-dimension (tensor-categorical),
   reflection positivity (transfer-matrix). The principle must be provable
   INSIDE X, without the comparison map of S4.

S4 (comparison identity). An exact identity
       D( pairing on X, graph of the scaling/Frobenius flow ) = Weil form.
   The explicit formula re-enters HERE and only here - as the comparison,
   never as the source of the sign. (In the function-field case this is the
   Lefschetz trace formula; positivity never uses it.)

S5 (fork compliance). P1: X computes strictly more than the Weil form
   (correspondence algebra, higher pairings - extra information). P2: for a
   DH-type function, X must FAIL TO EXIST (no Euler product => no
   multiplicative structure => no carrier), so RH-selectivity is by
   existence, not by computation. Any candidate whose DH kill-test requires
   computing a negative number is already in the EF orbit.
```

## 3. Candidate carriers, with their known obstructions

Recorded as a compass, not endorsements. Each line names the doubling, the
native positivity, and the wall it currently faces.

```text
(a) Lambda-ring / Witt doubling (Borger's F1). The descent datum Spec Z ->
    "Spec F1" is the family of commuting Frobenius lifts (the canonical
    Lambda-structure on Z); the self-product becomes Witt-vector geometry
    (W(Z), the big de Rham-Witt complex). Native positivity: unknown - the
    missing Hodge index for dRW arithmetic cohomology. S5-P2 is promising:
    DH has no Frobenius lifts (no multiplicativity), so the carrier
    genuinely fails to exist. Wall: nobody has an intersection theory here.

(b) Scaling-site square (Connes-Consani). They constructed the arithmetic
    site, its scaling topos, and a square with a sketched Riemann-Roch.
    Native positivity: open - this is exactly their program's missing step.
    S4 exists in trace-formula form. Wall: the positivity step keeps
    reducing to the EF (our fork phenomenon at topos level); their Sonin
    space work (CC20, our anchor) is the analytic shadow of the square's
    diagonal neighborhood - which is precisely the part we extended and
    found EF-bound.

(c) Type-II / type-III trace doubling. X = a factor M built from the adele
    class space of Q x Q (or the BC system's square) with tau the canonical
    trace; positivity = trace axiom. The known spectral realizations are
    guarded as circular (G2/AGENDA): they build M FROM the zeros or from
    EF data. The spec demands M from S1-compliant data. Worker A's finding
    (real-axis KMS is RH-silent) and the beta = 1/2 pinning say the relevant
    state is NOT a KMS state of the BC flow - it sits inside the critical
    strip's type-III region. Wall: no construction of the critical state
    that is not EF-derived.

(d) Arithmetic Hodge index (Arakelov). Arithmetic surfaces over Spec Z have
    a genuine Hodge index theorem (Faltings-Hriljac). The needed object is
    "Spec Z x Spec Z" as an arithmetic surface - forbidden literally (the
    no-go), but the Arakelov compactification idea (adding analytic data at
    infinity rather than a finite fiber) is the one systematic evasion of
    the characteristic obstruction that already has index theorems. Wall:
    the second factor; Arakelov theory doubles the GEOMETRY over Z, not Z
    itself.

(e) Reflection positivity. Realize the Weil form as the boundary two-point
    function of a transfer-matrix system in the filtration time (our edges
    ARE discrete time steps; the corner channel is boundary radiation).
    Native positivity: OS-positivity, checkable from a local transfer
    structure. Partially constrained already: S2's channel result says no
    reflection through the standard shift semigroup works (both channels
    indefinite); any RP structure must be place-global and channel-global.
    Wall: the reflection that works, if any, is not the obvious one.
```

## 4. The refined wall, one sentence

The wall is not the absence of estimates and not the choice of coordinates;
it is that the one-variable arithmetic (multiplicative semigroup of Z plus the
archimedean place) generates no positivity beyond what the explicit formula
already accounts for - so the sign must be imported through a square-like
carrier with its own discrete positivity principle, the carrier must exist
for zeta and fail to exist for DH, and the only thing the explicit formula is
allowed to do is compare.
