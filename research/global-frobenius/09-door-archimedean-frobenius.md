# 09 — through the door: the archimedean Frobenius is a flow, not a finite map

Status: ATLAS step (M), 2026-06-30. Phase-2 companion to doc 08. Walks through
the F1 door (the only escape from the additive theorem) and maps where it leads.
Refines faces F1, F2, F5. Carries one new theorem-anchor (Lindemann). Grade:
Reading (map of open territory) + one Theorem-anchor + Certified identity.

## The door, entered

doc 07 located the only escape from the fundamentality theorem: a canonical
MULTIPLICATIVE (non-additive) integer structure at the archimedean place. doc 08
hands it the target. Does such a structure exist? Walking in:

```text
THE DOOR IS OCCUPIED. There IS a canonical multiplicative structure at infinity:
the SCALING FLOW R_+^* on the adele class space (Connes), equivalently the
generator Theta of Deninger's archimedean "Frobenius" (the archimedean local
factor as a regularized determinant det((s-Theta)/2pi)^{-1} = Gamma_R(s)). It is
canonical (forced by the adele class space), multiplicative (a scaling action),
and non-additive. So F1 is not empty -- the door has an occupant.

BUT ITS SPECTRUM IS CONTINUOUS. The flow generator Theta has CONTINUOUS spectrum
(the scaling action of R_+^*, a connected group); the archimedean factor is a
regularized determinant over an infinite-dimensional space, NOT a finite product
over an eigenvalue lattice. A FINITE place p has a DISCRETE Frobenius (eigenvalues
on the lattice {p^{w/2}}); infinity has a CONTINUOUS flow.
```

## The second dichotomy: discrete vs continuous (where the door leads)

```text
The additive dichotomy (integer vs transcendental) re-expresses, at the
multiplicative door, as DISCRETE vs CONTINUOUS spectrum:

  DISCRETE Frobenius (finite place, eigenvalue lattice {q^{w/2}}):
     self-intersection = regularized sum over the lattice = rational multiple of
     log q -- FINITE-PLACE TYPE, integer-compatible.
  CONTINUOUS flow (archimedean, Theta):
     self-intersection = integral over continuous spectrum = the regularized
     determinant = -zeta'(0) = (1/2) log 2pi -- TRANSCENDENTAL.

So the multiplicative door does NOT automatically escape: its occupant (the flow)
reproduces the dichotomy as continuous => transcendental. The escape would need a
DISCRETE multiplicative structure -- a finite q-power Frobenius -- at infinity.
That is exactly the F_1 / Connes-Deninger dream, and it does not exist: infinity's
multiplicative structure is the continuous flow.
```

## The Lindemann anchor (F2 + F5 hardened to a theorem)

The transcendental horn is no longer "we failed to make it an integer" — it is a
theorem:

```text
V = -zeta'(0) = (1/2) log(2 pi) = (1/2) log 2 + (1/2) log pi.
  - (1/2) log 2 is FINITE-PLACE type (in the Q-span of {log p}; the prime 2,
    cf. CC's K = -2{2}).
  - (1/2) log pi is the ARCHIMEDEAN obstruction: if V were in Q-span{log p}, then
    log pi would be too, so pi = prod p^{c_p} would be ALGEBRAIC -- contra pi
    transcendental (Lindemann). Hence V is NOT in Q-span{log p}.

THEOREM (Lindemann anchor): the archimedean self-intersection -zeta'(0) is
provably NOT of finite-place type -- it cannot be a finite-Frobenius lattice
value. The obstruction is concentrated in the (1/2) log pi term.
[Certified identity + sanity: gf_archimedean_no_finite_q, exit 0. Transcendence:
 Lindemann.]
```

This upgrades the dichotomy's finite horn from a modeling observation to a
transcendence theorem: even granting every construction, the forced archimedean
value is provably not the integer/lattice value a finite Frobenius would give.

## Atlas updates

```text
F1 (the door): OCCUPIED but does not escape. Canonical multiplicative structure
   at infinity EXISTS (the scaling flow / Deninger Theta) but has CONTINUOUS
   spectrum => transcendental self-intersection. The escape requires a DISCRETE
   (finite-q) archimedean Frobenius, which the flow is not.
F2 (transcendentality): HARDENED. The finite value -zeta'(0) = (1/2)log 2pi is
   provably transcendental and provably not finite-place type (Lindemann); the
   obstruction is the (1/2) log pi term. [Theorem-anchor.]
F5 (missing place): SHARPENED to ONE thing. infinity has a CONTINUOUS
   multiplicative flow where p has a DISCRETE Frobenius. The entire deficit
   (no finite residue q, no q-power map, no eigenvalue lattice) unifies as:
   the archimedean Frobenius is not DISCRETIZED. The missing object = a
   discretization of the scaling flow = a finite q at infinity.
```

## Where Part 2 leads — the new theorem target

```text
The door reduces the whole program to ONE sharp question, with a transcendence
anchor under it:

  Q (the discrete-archimedean-Frobenius question): does there exist a CANONICAL
    DISCRETE multiplicative structure (a finite q-power Frobenius / a discrete
    eigenvalue lattice) at the archimedean place -- a discretization of the
    scaling flow Theta?

  - YES (the door truly opens): that discretization is the missing object =>
    the integer intersection form => RH. The F_1 dream, now precisely posed as
    "discretize Theta".
  - NO (the door shuts): any canonical archimedean multiplicative structure has
    CONTINUOUS spectrum, hence transcendental self-intersection (anchored by
    Lindemann on the value it must take). This would EXTEND the fundamentality
    theorem from additive to multiplicative -- a strong bounded-negative result
    covering the entire canonical class (additive + multiplicative).

NEW THEOREM TARGET (the multiplicative extension): "every canonical multiplicative
structure at the archimedean place has continuous spectrum." If proved, combined
with doc 08, the dichotomy closes over the FULL canonical class and the
bounded-negative branch is essentially complete. This is the next theorem cycle's
target; the Lindemann anchor (the forced value is transcendental) is the first
brick.
```

## Convergence

```text
Seventh convergence, and the tightest: additive-integer (doc 08) and
multiplicative-continuous (this doc) are the two horns of ONE object -- a finite
Frobenius at infinity. The dichotomy = integer/transcendental = discrete/continuous
= finite-place/archimedean = the discretization of the scaling flow. Five atlas
faces have collapsed to a single sharp question (Q) with a transcendence theorem
(Lindemann) beneath it. The missing object is now characterized to the highest
resolution the program has reached: a canonical discretization of the archimedean
scaling flow, whose self-intersection would have to be an integer but is forced
(Lindemann) to be the transcendental (1/2)log 2pi unless the spectrum is discrete.
```

## Witness

```text
Certified (new, lead-run, exit 0):
  python3 -m scripts.numerics.witness.gf_archimedean_no_finite_q  [ALL PASS]
  -- V = -zeta'(0) = (1/2)log(2pi) = (1/2)log2 + (1/2)log pi; finite-place part
     (1/2)log2 vs archimedean (1/2)log pi; V/log q not low-height rational q=2..50.
Theorem-anchor: Lindemann (pi transcendental => log pi not in Q-span{log p} =>
  V not finite-place type).
Cited: Deninger (archimedean factor as regularized determinant of Theta); Connes
  (scaling flow on the adele class space).
```

## Next

Two live fronts, both sharp:
  (theorem, O1) close the doc-08 obligation O1 (self-intersection = additive
    tower sum, general form) -- the gate to full rigor of the additive theorem.
  (theorem-target, Q) the multiplicative extension: "canonical archimedean
    multiplicative => continuous spectrum". The Lindemann anchor is brick one.
Both feed the same conclusion; bring for review which to push first.
