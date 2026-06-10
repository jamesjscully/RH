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

## 4. Prior-art audit (added same day, after a repo + literature sweep)

Section 3 was written before re-reading the program's pre-proof-track phases.
Almost every candidate WAS examined there, with verdicts; the corrected map:

```text
(a) Borger/Witt/F1: KILLED in f1-construction.md - but against a DIFFERENT
    criterion than this spec's. All six F1 grounds (sphere spectrum, tropical,
    Borger Lambda, monoid, period, global) were tested for "supplies the
    arithmetic scale q at the archimedean place" and all six are scale-free
    (the count/radius decoupling; the no-go preprint's criterion). This spec
    deliberately DROPS the scale demand (the no-go proves scale is impossible)
    and asks for a square with native signature positivity instead. The repo
    kill does not close that question; nobody has the intersection theory.
(b) Scaling-site square: literature/connes-consani-scaling-site.md - OPEN,
    with Connes' own boxed statement of the missing object: "an intersection
    theory and a Riemann-Roch theorem on the square of the arithmetic site...
    no Serre duality or good cohomological H^j for j != 0." RR proven on
    periodic orbits (curves) only; the square is missing. Matches this spec.
(c) Type II/III trace: work/A-qsm-free-energy.md - AUDITED, RH-SILENT, and
    this is the most instructive prior result for the spec (see section 5).
    The BC system already exhibits P2 (DH has no Euler product => no BC
    partition function => carrier fails to exist) AND its native positivity
    is certified real - yet it is RH-silent: the genuine OS-positive object
    (the KMS correlator) is positive BECAUSE a_n >= 0, independent of zero
    locations, and no FE-reflection continuation stays positive.
(d) Arakelov index: log/2026-06-06-arakelov-signature.md - AUDITED. The
    arithmetic Hodge index (Faltings-Hriljac-Moriwaki) genuinely carries the
    signature, and its negativity IS the Weil positivity decomposed into
    finite + archimedean pieces. Two measured blocks: Spec Z is 1-dim (no
    surface to carry (1, rho-1)); and the archimedean Gram is IDENTICAL for
    zeta and DH (max difference 0.0 exactly) - the geometric/archimedean part
    of any such pairing is DH-shared, hence RH-silent on its own; the Euler
    content sits entirely in the finite-place part, which is the SUBTRACTED
    term. Sign must be carried where the discrimination is.
(e) Reflection positivity: CLOSED NEGATIVELY at the test-class level
    (correcting an earlier draft of this section that called it live, based
    on a stale summary). The full record: thread-1 surveyed four families
    (Hamiltonian/Berry-Keating/BBM, determinantal/GUE, lattice gas, generic
    OS) - all RH-neutral or circular - and identified the prime-place
    reflection theta as the only possible new lever. Worker B
    (work/B-prime-reflection.md, 2026-06-06) then EXHAUSTED the reflection
    inventory over the EF-bound test class: (i) multiplicative inversion =
    identity on even tests (archimedean, neutral); (ii) FE reflection =
    trivial on even tests; (iii) the Gram doubling W_p = P_p P_p^T, whose
    OS-positivity IS Lambda >= 0 - the Euler product re-skinned, circular as
    forcing (it does discriminate DH: prime block min eig -0.66 vs +5.2e-3,
    but the discriminator is sign(Lambda)). Verdict verbatim: "no prime-place
    reflection theta exists beyond the Euler product itself"; the live edge
    was redirected to the cross-place margin W_inf >= sum_p W_p - WHICH IS
    EXACTLY THE PROGRAM DOCS 01-13 THEN EXECUTED TO TERMINATION. RP's residue
    was metabolized into the margin program and died in the fork (doc 13).
    Our S2 channel kill is the same closure one level up. Any RP revival
    must place theta on an S1-carrier (a new space), not on the EF-bound
    test class - RP does not bypass the carrier problem; it is an S3 option
    once a carrier exists.

(e') Worker F's sharpening (work/F-sym2-os-bridge.md), which belongs in this
    spec: the constructive RP route through sym^2/Rankin-Selberg reduces RH
    to the reflection-positivity of one form (A4) and then to the SAME
    missing square - but with the spec sharpened by one number: the
    self-product surface must have self-intersection equal to the Petersson
    norm ||f||^2 (an unconditional positivity), and DH-refusal is structural
    (no Satake parameters => no sym^2 => no Petersson norm => the surface
    cannot be formed - the strongest known instance of P2). This names the
    target self-intersection that candidates (a), (b), (d) must hit.
(f) Deninger (omitted from section 3, already fully audited):
    literature/deninger-spectral-cohomology.md - the most precise existing
    specification of the carrier: a laminated 3-dim space with conformal
    weight alpha = 1 whose closed orbits are primes and fixed points are the
    archimedean places; manifolds PROVEN excluded (alpha = 0 forced);
    laminated trace formula with fixed points unproven. Deninger's spec and
    this spec are the same demand in different categories (his: dynamical/
    cohomological; ours: pairing/signature + fork compliance).
```

## 5. The new clause the audit forces: S4 is where carriers die quietly

The BC/KMS result (worker A) is a COUNTEREXAMPLE TO THE SUFFICIENCY of
S1+S2+S3+S5: a carrier can be prime-position-orthogonal, multiplicative,
natively positive, and existence-selective against DH - and still be
RH-silent, because its comparison map lands on the wrong locus (the real
axis / high-temperature region) and no positivity-preserving continuation
reaches the critical strip (worker A tested all three continuations; all
fail). Therefore sharpen S4:

```text
S4' (full-locus comparison). The comparison identity must equate the carrier
    pairing with the Weil form ON THE FULL CRITICAL-STRIP TEST CLASS (the
    pole-killed compactly-supported class of doc 00), not with a real-axis,
    high-temperature, or small-support shadow of it. Positivity that holds
    on a shadow and must be analytically continued to reach the strip will
    lose positivity in the continuation (worker A: FE reflection flips the
    variance sign; naive susceptibility is OS-indefinite). The continuation
    IS the wall in thermal clothing.
```

Status ledger for the spec, after the audit: (a) reopened-but-unbuilt (the
repo kill was against the scale criterion, not the signature criterion);
(b) open, blocked at the square (Connes' own missing object); (c) killed by
S4' (the instructive failure); (d) blocked at the missing second factor, with
the archimedean part proven DH-shared; (e) LIVE (prime reflection theta,
sym^2 bridge); (f) open, blocked at the laminated construction. Nothing in
the audit contradicts the spec; (c) sharpens it.

## 4'. The refined wall, one sentence

The wall is not the absence of estimates and not the choice of coordinates;
it is that the one-variable arithmetic (multiplicative semigroup of Z plus the
archimedean place) generates no positivity beyond what the explicit formula
already accounts for - so the sign must be imported through a square-like
carrier with its own discrete positivity principle, the carrier must exist
for zeta and fail to exist for DH, and the only thing the explicit formula is
allowed to do is compare.
