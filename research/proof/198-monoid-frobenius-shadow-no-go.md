# 198 - Monoid Frobenius shadow does not construct End(S^2/Z)

Status: no-go + monoid/cyclotomic Frobenius boundary, 2026-06-20.
Sixty-first cycle of the doc-137 construction arc. Doc 197 killed
promoting the connective `ku` square / Adams HH0 graph shadow itself to
End(S^2/Z). This document tests the stronger repair isolated in the
W-record: use the monoid/cyclotomic Frobenius shadow, which restores
degree growth and the Lorentzian index shape missing from the invertible
Adams family, as the missing square carrier.

Witness, lead-reran this cycle:
`prime_int_n1b_monoid_frobenius_shadow_no_go` (MFS1-MFS10 ALL PASS) --
exact fixed-point tower `q^w-1`, branch-(i) HH0 collapse, adelic
tame/LTE assembly, p-complete cyclotomic blindness, bidegree degree-zeta
factor, Lorentzian max-Gram shape, missing bimodule graph for cyclotomic
Frobenius, missing integral non-invertible `psi^p`, missing global
TP/iota/properness assembly, missing compactified square
cohomology/intersection/correspondence/Frobenius/Rosati data, missing
Laurent boundary/torsor/DD.4 data, and residual R1 carrier-guard checks.

Adjacent witness, lead-reran this cycle:
`prime_monoid_frobenius_shadow` (ALL PASS) -- the positive W-record that
the monoid-level fixed-point object gives growth `q^w-1`, bidegree `d_2=q`,
and a certified Lorentzian max-Gram index shape on the geometric family.

## 1. Purpose

Doc 197 left a precise gap: p-complete Adams operations are group-like and
therefore have bidegree `(1,1)`, while the function-field Frobenius graph
needs degree growth. The W-record repairs that at the monoid level:

```text
|pi_{2w-1} K(F_q)| = q^w - 1,
d_2 = q on the Bott/ruling line,
log |q^{iw} - q^{jw}| = w log q max(i,j) + lower terms.
```

The last line gives the Lorentzian max-Gram shape the index mechanism
needs. This is a real improvement over the Adams HH0 shadow.

It is still not End(S^2/Z). The cyclotomic Frobenius `phi_p` lives in
cyclotomic spectra and TP/TC, not as a bimodule graph correspondence.
Non-invertible `psi^p` is impossible on periodic KU and unconstructed on
connective `ku` as an integral structured map. The local finite-field TP
theorem remains p-complete and semilinear, and its determinant extraction
uses a finite-field `W(F_q) -> C` embedding; the square-side analogue of
that archimedean `iota` is precisely part of the properness/Poisson wall.

This document is local. It does not reject a future spherical delta-ring,
cyclotomic, or PFD construction that uses the monoid Frobenius shadow as an
associated graded. It rejects only the shortcut:

```text
monoid/cyclotomic Frobenius shadow = End(S^2/Z).
```

## 2. Lemma

```text
Lemma 198.1 (The monoid Frobenius shadow is not the compactified square).

The monoid/cyclotomic Frobenius record supplies genuine positive shadow
data:

  q^w - 1 fixed-point growth,
  adelic tame/LTE assembly of q^w - 1,
  bidegree d_2=q and local zeta(s-1) degree factor,
  and Lorentzian max-Gram index shape for the geometric family.

However, the cyclotomic Frobenius has no bimodule graph, the corresponding
Lefschetz object is TC/TP rather than a square correspondence algebra, and
the local finite-field determinant theorem relies on finite-field
linearization and an archimedean embedding not available for the
compactified arithmetic square over S.

Moreover, no connective integral non-invertible psi^p correspondence, no
global TP square linearization, no square-side iota, no compactified
arithmetic square, no square H2, no intersection form, no correspondence
algebra, no Frobenius graph, no positive Rosati, no Laurent boundary map,
no torsor splitter, and no DD.4 weight>=1 datum is constructed.

Therefore the banked monoid/cyclotomic Frobenius shadow cannot itself be
promoted to End(S^2/Z).
```

Verdict label:

```text
N1B_MONOID_FROBENIUS_SHADOW__INDEX_SHADOW_NOT_END_S2Z__NO_GO.
```

## 3. Proof

`prime_int_n1b_monoid_frobenius_shadow_no_go` verifies the R1 gate, with
`prime_monoid_frobenius_shadow` rerun as the adjacent positive witness.

MFS1 records the positive fixed-point tower:

```text
|K_{2w-1}(F_q)| = q^w - 1 = 1/|zeta(F_q,-w)|.
```

The witness checks the exact recursion `q^{w+1}-1=q(q^w-1)+(q-1)` and
linear log-growth on a finite grid.

MFS2 records the fork boundary: the bimodule HH0 branch still collapses to
the tame constant `Z/(k-l)` because
`gcd_{j<=w}(k^j-l^j)=k-l`. The growing tower lives in the fixed-point
carrier, not in the naive HH0 graph quotient.

MFS3 records adelic assembly: `q^w-1` factors as the product of the
tame/LTE towers at all other primes, equivalently as
`prod_{d|w} Phi_d(q)`.

MFS4 records the p-complete blindness: if `q=p^r`, then
`v_p(q^w-1)=0` for `w>=1`, and Hesselholt's finite-field weight formula
cancels exactly at the p-complete TP level. The degree growth is recovered
only after the finite-field archimedean embedding.

MFS5 records the bidegree degree factor:

```text
sum_{w>=1} q^w q^{-ws} = q^{1-s}/(1-q^{1-s}).
```

This is the local `zeta(s-1)` surface factor shadow, not a square
correspondence algebra.

MFS6 records the positive index shape: max-Grams on the geometric family
have Lorentzian signature `(1,n)` in the checked range, matching the
W-record's exact/certified max-Gram lemma.

MFS7 records the first categorical obstruction: the cyclotomic Frobenius
is a map in cyclotomic spectra and TP/TC, not a bimodule correspondence
graph of the square.

MFS8 records the second categorical obstruction: periodic non-invertible
`psi^p` is impossible by the Bott-unit argument, while connective integral
`psi^p` is not constructed.

MFS9 records the global assembly obstruction: the finite-field TP theorem
does not provide a global linearized square over `S`, nor a square-side
embedding replacing `W(F_q) -> C`.

MFS10 records the carrier failure: no compactified square H2,
intersection form, correspondence algebra, Frobenius graph, positive
Rosati, Laurent boundary, torsor splitter, or DD.4 weight>=1 datum is
constructed.

## 4. Impact on R1

```text
R1 after docs 138-198:
  NEWLY CLOSED THIS CYCLE:
    - monoid/cyclotomic Frobenius fixed-point tower, bidegree growth,
      degree-zeta factor, and Lorentzian max-Gram index shadow, as
      End(S^2/Z), square H2, intersection form, correspondence algebra,
      Frobenius graph, Laurent boundary data, torsor splitter, DD.4
      weight>=1 datum, or positive Rosati (doc 198).

  STILL ADMISSIBLE:
    - a spherical delta-ring / cyclotomic / PFD construction that turns the
      monoid Frobenius shadow into an actual compactified square
      correspondence;
    - a connective integral non-invertible psi^p construction with full
      twisted THH, off-diagonal correspondences, and properness/duality;
    - a square-side iota/properness theorem replacing the finite-field
      W(F_q)->C step carrier-natively;
    - a genuinely different carrier whose correspondence algebra is built
      internally.

  STILL OPEN:
    - a genuinely different carrier whose first
      correspondence/multiplication constructs the square data internally
      and finishes DD.4 weights>=1.
```

R1 is still open. The monoid Frobenius shadow is the best current index
shape, but it is not the target object. R2 remains locked.

## 5. Kill Conditions

```text
KILL-MFS.1 monoid fixed-point tower as End(S^2/Z)
  A proposal identifies q^w-1 fixed-point growth with the compactified
  arithmetic square. Kill it unless it constructs square H2, intersection,
  and correspondences.

KILL-MFS.2 cyclotomic Frobenius as bimodule graph
  A proposal treats phi_p: THH -> THH^{tC_p} as a square bimodule graph.
  Kill it: phi_p lives in cyclotomic spectra/TP, not as a bimodule
  correspondence.

KILL-MFS.3 non-invertible psi^p as available correspondence
  A proposal uses psi^p as an integral structured ku correspondence. Kill it
  unless it constructs connective psi^p; periodic KU is impossible by the
  Bott-unit obstruction.

KILL-MFS.4 finite-field TP theorem as global S^2/Z properness
  A proposal imports Hesselholt's finite-field determinant theorem without a
  square-side global linearization and iota. Kill it: those are the
  archimedean/properness steps.

KILL-MFS.5 Lorentzian max-Gram as positive Rosati
  A proposal treats the max-Gram index shape as the positive Rosati. Kill it
  unless the Lorentzian form is realized as an involution on a
  correspondence algebra.

KILL-MFS.6 carrier-specific DH/Epstein death as S^2/Z construction
  A proposal says DH/Epstein die because they lack ring/cyclotomic
  structure, then promotes that to End(S^2/Z). Kill it unless the actual
  square map and its carrier-native control death are constructed.
```

## 6. Board

```text
doc-137 R1, cycle 61 = doc 198:
  N1B_MONOID_FROBENIUS_SHADOW__INDEX_SHADOW_NOT_END_S2Z__NO_GO.

What got built: no End object. The value is a sharper boundary theorem:
the monoid/cyclotomic Frobenius shadow gives real degree growth and the
right Lorentzian index shape, but without a bimodule/correspondence
realization, square-side iota/properness, and positive Rosati, it is not
End(S^2/Z).

What remains: construct the spherical-delta/cyclotomic/PFD square that
turns this shadow into correspondences; construct connective integral
psi^p plus full twisted THH; solve the square-side iota/properness problem;
or return to the in-house PFD/Xbar DD.4 weight>=1 obstruction.
```
