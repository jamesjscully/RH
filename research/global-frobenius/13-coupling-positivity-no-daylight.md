# 13 — the coupling form is the right object; its positivity is RH (no daylight)

Status: 2026-06-30. Runs the test posed in doc 12: is the Frobenius-cone coupling
form W_inf constructible / forceable non-circularly, or does its content route
back to RH? Outcome-D kill condition pre-registered BEFORE the run. Result: KILL
(no daylight). Deliverable type: fail-closed test, decisive.

## Pre-registered Outcome-D guard (fixed before the run)

```text
DAYLIGHT exists only if the coupling form is (a) carrier-native (Euler-specific,
DH-unformable -- not the trivial FE-layer) AND (b) its positivity has a structural
source NOT identical to the RH-equivalence.
KILL (no daylight) if the coupling's only non-FE content is its positivity, and
that positivity is the tracking equivalence (M_R(zeta) >= 0 but M_R(DH) < 0 = RH).
```

## (a) carrier-native: YES (the right object)

```text
HH H6 (prime_hh_weil_index_factorization, reran exit 0): the Frobenius-cone
lattice form is DH-UNFORMABLE -- DH has 42 negative-weight atoms (Lambda =
-<d,d> >= 0 violated) and 45 non-prime-power atoms (no tower address). So the
coupling form is genuinely EULER-NATIVE, not the FE-layer. It PASSES the carrier
guard. This is the RIGHT object -- the correct face (contrast doc 12: the strict
family was the WRONG face).
```

## (b) positivity: it is the tracking equivalence = RH (KILL)

```text
prime_edge_tracking (reran exit 0), the doc-13 margin form M_R = W_inf - P_R
(HH.1: "the Weil side IS the doc-13 margin form"):
   zeta, edge 1.60->1.88:  tau = 0.714 < 1,  eigmin(SN) = +0.078 > 0  [M_R >= 0]
   DH,   edge 1.60->1.88:  tau = 1.554 > 1,  eigmin(SN) = -0.282 < 0  [M_R < 0]
   DH, all higher edges: OLD BLOCK DEAD -- never reaches the tracking regime.
The coupling form's positivity HOLDS for zeta and FAILS for Davenport-Heilbronn
(which has off-line zeros). So the positivity is EULER-SPECIFIC = exactly Weil
positivity = RH. There is no structural source for it that is not RH itself
(doc 13: "no admissible attack surface from this structure").
```

## Verdict: KILL -- no daylight; the threads merge

```text
The coupling form is the RIGHT object (carrier-native, the correct face), and the
construction program built it. But its ONLY remaining content is its positivity,
which is the tracking equivalence (RH). The construction thread and the analytic
equivalence (doc 13) MERGE here, at the positivity = RH. There is no non-circular
construction of the positivity -- the Outcome-D kill condition fired exactly as
pre-registered.
```

## What following the thread actually established (this session, honestly)

```text
GENUINELY NEW (non-circular, on-thread):
  doc 12: the STRICT FAMILY is the WRONG FACE -- its unit is a vanishing pad,
    while the RH-relevant Frobenius cone needs an O(1) sign-indefinite coupling.
    This corrects where the construction program (docs 17-34, the doc-45 spec,
    the index-attack) thought it was making progress: it was on the wrong face.
  doc 13 (this): the RIGHT FACE (the Frobenius-cone coupling form) is carrier-
    native and built, but its content is the tracking equivalence = RH. No
    daylight.

NOT NEW (the wall the thread merges into):
  the tracking equivalence (research/proof/13, 2026-06-09): M_R(zeta) >= 0 <=> RH,
    DH fails -- "no admissible attack surface". The construction thread reaches
    THIS, from the construction side, with the right face now identified.

NET: the construction program's honest position is that it has built the right
Euler-native object and localized RH to its positivity (= the tracking
equivalence), having now also ruled out the strict-family face. The non-circular
work this session was the FACE correction (doc 12) and the decisive merge test
(doc 13); both fail-closed, both RH-neutral in what they assert.
```

## Anti-trap audit (honest)

```text
This test did NOT prove RH and did not assume it. It ran a pre-registered
fail-closed control (DH) and the kill fired. The result is a statement about the
construction (its content = RH-equivalent positivity), not a new RH-equivalence
manufactured for its own sake -- it is the DETECTION that the construction's
remainder is the already-known equivalence. That detection is the correct,
honest output: it tells us the construction sub-thread has merged with the wall,
so further work HERE is circular.
```

## Where the thread goes (honest, not a declared terminus)

```text
The construction-of-the-Weil-positivity-object sub-thread merges with the
tracking equivalence (RH) here. Per the repeated lesson (the thread keeps
continuing past where I call it done), I will NOT declare the program over.
What I can say honestly:
  - On THIS sub-thread (build the coupling form, force its positivity), there is
    no daylight: it is RH.
  - The face correction (doc 12) is the session's real yield: the strict-family
    construction was misdirected.
If the thread continues, it is NOT through forcing this form's positivity (that
is RH). It would have to be a genuinely different object or a different question
-- which is the user's call, since the thread has continued past every terminus
I have named so far.
```
