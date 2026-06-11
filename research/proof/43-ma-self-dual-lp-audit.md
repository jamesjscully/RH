# 43 - M-A self-dual LP audit

Status: 2026-06-11. First-pass execution of doc 40/41 move M-A from
banked RR/AB evidence, with current-worktree witness reruns. This
decides the fork at the level it was posed: whether a deep-cell
per-place obstruction is unit-independent enough to join OC2.

Witnesses rerun in this session:

```text
python3 -m scripts.numerics.witness.prime_rr_face_cycle
python3 -m scripts.numerics.witness.prime_ab_nongaussian_stress
```

Both exited 0. RR reproduces freeze
`f036d4b6aff1087023d96a77a7388a6b8602c500d7279c8c04183daf09596266`;
AB reports `ALL PASS (AB1-AB9)`.

## 1. The M-A fork

Doc 40 posed:

```text
M-A deep-cell self-dual LP
  feasible   => per-place obstruction is pure k=1 threading;
  infeasible => a unit-independent deep obstruction joins OC2.
```

The relevant "deep" family is the `(p;k>=2)` slot family. The banked
Gaussian decision cell was `(11;2)@4.96`, certified negative in NN/RR:

```text
m+_gauss((11;2), 4.96) = -2.214249e-3.
```

The decisive self-dual comparison is AB's Hermite unit

```text
f_C(x) = e^{-pi x^2}(1 + eps H4(sqrt(2pi)x))/(1+12eps),
eps = 1/100,
```

with `fhat_C = f_C` certified by the Poisson checks in AB2.

## 2. Evidence

RR, with the Gaussian unit and GG repair, says the banked decision cell
is per-place infeasible:

```text
decision cell under chi_GG:
  (11;2)@4.96 = -2.214249e-3, unchanged.

per-place p=11 LP:
  variant v: infeasible, both slot margins < 0.
  variant g: w_(11,2) <= 5e-48 of k=1 mass; effectively no measure
             charging the breaking class.

global GG-repaired aggregate:
  A_g(4.96) = +3.027393e-2.
```

AB reruns the same row after changing the unit. The self-dual Hermite
unit flips the banked deep cell:

```text
Hermite unit:
  m+(d=1, 4.96)       = -3.5126e-3  [negative]
  m+((11;2), 4.96)   = +2.0913e-4  [positive]
  A_11 variant v      = -2.0802e-3  [negative]
  A_11 variant g      = +3.8023e-5  [positive]
```

So the deep-cell LP at the banked cell is feasible under an admissible
self-dual non-Gaussian unit. The Gaussian cell obstruction is therefore
not unit-independent object data.

AB also records that deep breakage does not disappear; its phase set
shifts:

```text
(11;2) signs over [2log11, 2log11 + (1/2)log121]:
  Gaussian: -------
  Hermite:  +------
```

and later points in the half-period turn positive in both records. The
lesson is not "Hermite proves all deep cells positive"; it is sharper:
which deep cell breaks, and at which phase, belongs to the unit slot.

Finally, AB's depth-wall gate remains invariant:

```text
needed / available at a = 8:
  Gaussian q=3      155.7
  Hermite q=3       155.7
  Gaussian q=121   3514.4
  Hermite q=121    3514.4

needed e^{-8} / (rho~ Lambda^2) = 0.998..1.000 for every unit.
```

The wall is object data; the named deep breaking cell is not.

## 3. Verdict

M-A first pass returns the FEASIBLE branch:

```text
The banked deep-cell obstruction does not join OC2.
```

The OC2 statement should remain exactly the AB/doc-41 form:

```text
OC2 threading
  The Lambda(p)-class deficit is per-place unpayable under every
  admissible unit, while the KMS-beta=1/2 global aggregate pays the
  scanned deficit. The object moves surplus across places.

Demoted from OC2
  A specific `(p;k>=2)` cell or phase being negative. Deep-cell
  breakage is slot-parametric; AB's self-dual Hermite unit already
  flips the banked decision cell.
```

OC3 receives the positive invariant from M-A:

```text
OC3 depth wall
  The exponential Frobenius-depth demand versus linear window supply is
  unit-free in covariant units, with law constant 1. This survives the
  self-dual unit swap.
```

## 4. Consequences

```text
1. Do not add "deep-cell per-place negativity" to the object
   conditions. It is slot data.

2. Future LP work should not ask whether a Gaussian deep cell is
   negative. It should ask whether a candidate's own unit makes the
   k=1 per-place deficit globally payable by an intrinsic cross-place
   comparison.

3. The missing structure must explain the invariant threading pattern:
   local k=1 deficit + global KMS-1/2 payability + unit-free depth
   wall. It need not preserve the Gaussian `(11;2)@4.96` failure.

4. M-B should inherit this scoping: BC13 exhaustion must be tested with
   the candidate's own unit and on the full Frobenius-graph cone, not
   by reusing a Gaussian deep-cell phase. Doc 44 applies this: the
   strict proxy is killed, and live M-B awaits a candidate-native unit.
```

## 5. Updated Characterization

After M-A, the missing structure is not required to carry a
unit-independent negative deep cell. It is required to carry:

```text
liquid/metrized address
+ Euler-product carrier
+ k=1 continuum-unit charge and local deficit
+ cross-place KMS-1/2 threading
+ unit-free depth wall
+ forced-nonnegative index/Gram over the full graph cone
+ independent count comparison with unforced odd-slot eigenvalues.
```

This narrows OC2 and strengthens OC3. It does not construct the
missing carrier.
