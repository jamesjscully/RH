# 64 - Epstein carrier-guard lemma

Status: proof lemma for docs 49, 53, 54, and 60, 2026-06-11. This
isolates the concrete Epstein obstruction used throughout the gate
stack. It proves a carrier-address failure, not a sign failure.

## 1. Statement

Let:

```text
Q(x,y) = x^2 + 5y^2
```

and let `R_Q` be the set of positive integers represented by `Q`.
Then:

```text
1, 4, 6, 9, 36 in R_Q;
2, 3 notin R_Q.
```

Moreover, at the first visible multiplicative level:

```text
4, 6, 9
```

are irreducible with respect to factorization by represented integers
greater than `1`, while:

```text
36 = 4*9 = 6*6.
```

Therefore the represented-norm data of `Q` has a theta/count shadow,
but it does not supply the free prime-power valuation/tower address
needed by the doc-45 Euler-product carrier.

## 2. Proof Of The Representations

The represented values are explicit:

```text
1  = Q(1,0);
4  = Q(2,0);
6  = Q(1,1);
9  = Q(3,0);
36 = Q(6,0) = Q(4,2).
```

For `2`, if `y = 0` then `x^2 = 2`, impossible in integers. If
`|y| >= 1`, then `5y^2 >= 5 > 2`, impossible. Thus `2` is not
represented.

For `3`, if `y = 0` then `x^2 = 3`, impossible in integers. If
`|y| >= 1`, then `5y^2 >= 5 > 3`, impossible. Thus `3` is not
represented.

## 3. First Irreducibles

Irreducible here means:

```text
n in R_Q, n > 1, and there is no factorization n = ab
with a,b in R_Q and a,b > 1.
```

For `4`, the only nontrivial integer factorization is:

```text
4 = 2*2.
```

Since `2 notin R_Q`, this is not a represented-norm factorization.
Thus `4` is irreducible.

For `6`, the only nontrivial integer factorizations are:

```text
6 = 2*3 = 3*2.
```

Since `2,3 notin R_Q`, `6` is irreducible.

For `9`, the only nontrivial integer factorization is:

```text
9 = 3*3.
```

Since `3 notin R_Q`, `9` is irreducible.

But `36` has two represented-norm factorizations:

```text
36 = 4*9 = 6*6.
```

The two factorizations use different represented irreducible multisets.
Thus any multiplicative carrier that treats represented irreducibles as
prime-power atoms lacks a unique factorization address already at `36`.

## 4. What Survives

The theta/count layer survives:

```text
theta_Q(t) = sum_{(x,y) in Z^2} exp(-pi t Q(x,y))
```

is a perfectly valid positive theta series, and Poisson/theta
formalism for the lattice still exists.

This is why the Epstein guard is not:

```text
the count layer is undefined.
```

The guard is:

```text
the count/theta shadow is defined, but the Euler-product carrier
address is not.
```

## 5. What Dies

A prime-power carrier has structural data of the form:

```text
1, p, p^2, p^3, ...
```

with a distinguished atom `p`, a canonical tower coordinate `k`, and a
well-defined valuation/depth function.

The represented-norm data above has no analogous distinguished atom or
free tower coordinate. At the first obstruction:

```text
36 = 4*9 = 6*6
```

so the atom multiset attached to `36` is not unique. In particular,
there is no candidate-native way to assign prime-power graph depth or
Lambda(p^k)-style address from this represented-norm data alone.

Thus an LS4-like coupling that requires a prime-power comb, valuation
tower, or graph-depth carrier must be undefined for this Epstein
replacement. If it still computes after replacing the carrier by
`R_Q`, it is carrier-blind.

## 6. Relation To Witnesses

This lemma is the proof-level version of the integer checks in:

```text
scripts/numerics/witness/prime_b0_tate_rr_calibration.py
scripts/numerics/witness/prime_int_jj_archimedean_unit.py
scripts/numerics/witness/prime_xx_b1_liquid.py
scripts/numerics/witness/prime_yy_second_evaluation_audit.py
```

The B0 witness uses only the finite part needed here:

```text
Q=x^2+5y^2 represents 1,4,6,9,36;
2,3 are absent;
4,6,9 are irreducible;
36=4*9=6*6.
```

The witness is a deterministic guard. This document records the
mathematical proof.

## 7. Program Consequence

The Epstein guard can now be stated without re-running examples:

```text
Any proposed carrier whose LS4-like coupling is still defined after
replacing prime-power valuation towers by the represented-norm data of
x^2+5y^2 fails doc-45 B2/B3.
```

The required death profile remains:

```text
theta/count/Poisson shadow: alive;
Euler-product carrier/coupling: undefined;
failure point: carrier/effectivity before signs.
```
