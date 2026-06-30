# 12 — executing the deferred test: the strict family is the wrong face

Status: 2026-06-30. This RESETS the arc off the circular track (docs 01-11
re-derived the month-old f1-construction terminus, user-caught) and onto the
GENUINE live thread: the test posed in research/proof/34-duality-cycle.md sec 3
on 2026-06-11 and never run -- "test the inequality's extension to the
Frobenius-graph classes with the hand-inserted unit (cheap, fail-closed)."
Deliverable type: fail-closed test, executed. Anti-trap: RH-neutral (a statement
about which construction face is correct, NOT about RH).

## The test (from doc 34 sec 3, deferred since 2026-06-11)

```text
The index inequality  h^0(D) + h^0_ren(K_sq - D) >= chi_sq(D)  (== h^0_ren >= 0)
holds on the STRICT FAMILY D_T with the hand-inserted unit (LL, zero slack).
The zeros live not on the strict family but on the FROBENIUS-GRAPH cone (HH's
classes, Lambda(p^k) = -<d_k,d_k>, where the explicit formula lives). doc 34
sec 3, never executed: does the inequality extend there with the SAME unit?
  FAIL-CLOSED: "if it fails THERE even with the unit, the strict-family success
  is not the right face."
```

## The two certified facts (both witnesses reran this session, exit 0)

```text
STRICT FAMILY -- the unit is a VANISHING PAD (prime_int_ll_square_dual, LL5/LL6):
  the index margin nearly holds on its own at deep effectivity; the inserted
  unit's required magnitude m+(a) -> 0:
      m+(1) = 0.154,  m+(2) = 0.073,  m+(5) = 0.0041,  m+(8) = 0.0002.
  The unit is an asymptotically NEGLIGIBLE correction (zero slack = the pad
  shrinks to nothing as effectivity deepens).

FROBENIUS CONE -- the archimedean form is O(1) sign-indefinite, ESSENTIAL
(prime_hh_weil_index_factorization, H4):
      M_R = W_inf - P_R,   eigmin(W_inf) = -0.073 at R=2.30, min over rungs
      = -0.91;  eigmin(P_R) = -1.65;  eigmin(M_R) = +0.023.
  W_inf GOES NEGATIVE and STAYS O(1) across rungs; positivity is a JOINT
  CANCELLATION with the prime side. The archimedean object is ESSENTIAL, not a
  vanishing pad ("the unit must couple, not patch", HH).
```

## The result (fail-closed: WRONG FACE)

```text
The archimedean unit plays OPPOSITE asymptotic roles on the two faces:
  - strict family:   VANISHING (m+ -> 0; the inequality self-satisfies),
  - Frobenius cone:  ESSENTIAL, O(1), SIGN-INDEFINITE (W_inf goes negative,
                     must joint-cancel).
This is unit-normalization-independent: it is the asymptotic ROLE that differs
(negligible vs essential), not a magnitude in one chart. The object that
satisfies the strict-family inequality (a vanishing pad) is therefore NOT the
object the Frobenius cone requires (an O(1) sign-indefinite coupling). The
strict-family success does NOT extend to where the zeros live.

VERDICT (the doc-34 fail-closed branch fires): THE STRICT FAMILY IS NOT THE
RIGHT FACE. The recent construction "progress" concentrated on the strict family
(the doc-45 spec, the index-attack docs) was building the wrong unit -- a
vanishing pad -- while the RH-relevant cone needs the coupling unit (the
joint-cancellation object). This is why that progress felt real but never reached
RH: wrong face.
```

## Why this is genuine (not the docs-01-11 circle)

```text
- It is a statement about CONSTRUCTION (which face), not an RH-equivalence. It
  does not claim, assume, or reduce RH. Anti-trap (Outcome D) passed.
- It is the step the program DEFERRED on 2026-06-11 and never took -- executed
  here from two certified witnesses, both reran exit 0.
- It KILLS a path (the strict-family face) fail-closed -- the program's
  highest-value move type -- rather than re-deriving a known equivalence.
- It is NOT the f1-construction terminus (the F_1 scale): it is about the
  index-inequality construction's face. Different content, genuinely on-thread.
```

## Grade + scope

```text
GRADE: the two underlying facts are Certified (LL, HH; both reran exit 0); the
contrast (vanishing vs essential asymptotic role) is a synthesis reading built
on them; the test verdict is fail-closed. The "wrong face" conclusion is solid
because it rests on the asymptotic role (unit-independent), not a cross-chart
magnitude.
SCOPE: redirects construction effort; RH-neutral. Does NOT construct the coupling
unit (the hard object) -- it shows the easy object (the pad) is the wrong target.
```

## Where the thread goes now (the real target, restated correctly)

```text
The genuine construction target is the COUPLING UNIT on the Frobenius cone -- the
object that supplies W_inf's O(1) sign-indefinite archimedean form so that
M_R = W_inf - P_R >= 0 by joint cancellation. That IS the Weil-positivity
mechanism HH measured, and it is the hard object (not the strict-family pad).
  THE LIVE QUESTION: is the coupling unit constructible non-circularly, or does
  its construction route back through the archimedean-Frobenius wall
  (f1-construction)? This is the next test -- and it must be guarded HARD against
  the Outcome-D trap (the coupling unit's positivity = Weil positivity = RH, so
  any "construction" that assumes the coupling is positive is circular). The
  honest sub-question: can W_inf's sign-indefinite coupling form be built from
  the prime data ALONE (the EF lattice coordinates HH established) without a
  positivity input?
```

## Next

Test whether the Frobenius-cone coupling form W_inf is constructible from the
prime/EF lattice data alone (HH's coordinates) -- a definite, fail-closed
question -- with the Outcome-D guard explicit (positivity-in => RH => circular).
If it routes back to f1-construction's wall, the construction thread and the
geometric thread have genuinely merged at one object and the program's negative
localization is complete; if there is daylight, it is here, on the coupling
unit's constructibility, that the only non-circular progress remains.
