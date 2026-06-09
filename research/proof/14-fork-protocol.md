# 14 - The fork protocol (standing discipline)

Status: STANDING RULE as of 2026-06-09, distilled from the R-TRACK terminal
result (doc 13). Applies to every future proposed mechanism, object, or
decomposition in this program. Infrastructure:
`scripts/numerics/witness/fork_lib.py`.

## 1. The conservation law it enforces

Every quantity constructed from the program's ingredients - the digamma
density, the prime-power atoms, the support filtration - is transported
LOSSLESSLY to a zero-side functional by the explicit formula. This is exact,
not asymptotic (doc 13: the tracking residual equals its zero cross-correlation
to truncation; doc 09 6''': every finite margin is the minimal spectral side).
Consequence: a construction from EF-bound data can relocate the difficulty of
RH but cannot dilute it. The difficulty is invariant under realization changes.

The R-TRACK rung cost one full working day between "exact per-edge structure
discovered" and "structure shown to be a coordinate change". The fork protocol
exists so the next candidate costs one hour instead.

## 2. The protocol

Given a proposed object Q (a decomposition, a target vector, a storage
function, a "geometric" center, a candidate positivity mechanism):

```text
F1 (value fork). Express Q's key quantity in witness coordinates and compute
   its zero-side image via fork_lib.zero_gram. If candidate ~ image (rel at
   truncation scale, cos ~ 1): Q is EF-DERIVED - a coordinate change of the
   explicit formula. Keep it if the coordinates are useful; abandon it as an
   attack surface. No exceptions: tightness of the match is not "structure",
   it is the conservation law.
F2 (deformation kill). Run Q's claimed SIGN MECHANISM on data where the
   spectral side is known to go negative: DH coefficients, beta != 1/2
   weights, smooth surrogates. If the mechanism still "proves" positivity
   there, it over-proves and is wrong (guard G5). If it fails exactly where
   the spectral side fails, combine with F1: it is tracking the explicit
   formula.
F3 (slack audit). If any inequality in the mechanism carries slack (loses a
   constant, an epsilon, a log), it is dead a priori: margins sit e^{-1.5R}
   below the natural scale of every constituent term (doc 09 Finding 1).
   Surviving sign mechanisms must be exact identities plus a soft discrete
   step (signature, index, dimension count, existence).
```

## 3. The positive criterion (what passing would look like)

A candidate that survives F1-F3 must, by elimination, have BOTH properties:

```text
P1 (extra information). It computes invariants the EF data cannot - strictly
   more than the Weil form. (Weil's function-field proof: intersection theory
   on C x C computes all correspondences, not just the diagonal pairing.)
P2 (existence-selectivity). Its kill-test against DH should be satisfied by
   NON-EXISTENCE of the carrier object, not by a computation on it. DH has no
   Euler product, hence no multiplicative/Frobenius structure, hence the
   carrier (whatever plays the role of the surface C x C) should simply fail
   to exist for DH. A mechanism that has to COMPUTE its way to failing DH is
   in the EF orbit; a mechanism whose applicability is conditioned on the
   arithmetic structure existing is the genuine article. This is the shadow
   of finding E1 (the full semigroup is load-bearing) at the level of
   foundations.
```

See doc 15 for the spec of what such a second description would have to be.
