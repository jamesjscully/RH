# 204 - Regularized determinant compactness does not construct End(S^2/Z)

Status: no-go + trace/radius split boundary, 2026-06-20. Sixty-seventh
cycle of the doc-137 construction arc. Doc 203 killed using named F1
constant-field towers as the finite base size `q`. This document tests the
next repair: replace finite cardinality by compactness, nuclearity, or a
regularized determinant.

```text
regularized determinant / trace-class compactness
  = finite radius marker
  = End(S^2/Z).
```

Witness, lead-reran this cycle:
`prime_int_n1b_regularized_determinant_no_go` (RDR1-RDR6 ALL PASS) --
finite-field Frobenius determinants are finite-rank and pure examples mark
the expected radius; off-circle perturbations keep finite rank and finite
determinants while breaking purity; Connes' archimedean regularized
determinant supplies the explicit-formula trace but does not mark
`Re(s)=1/2`; compactness supplies count/location, not independent purity;
DH has no Frobenius determinant analogue; and no square/Rosati/R1 data is
built.

Adjacent witness, lead-reran this cycle:
`regularized_determinant_radius` (exit 0) -- the older R10 probe:
compactness gives a genuine finiteness, but the radius is a separate
purity input.

## 1. Purpose

Docs 202-203 closed the finite-cardinality repair: no archimedean special
fiber or named F1 constant object supplies a finite `q`. The natural next
move is to change the type of finiteness. Over finite fields, the zeta
factor is

```text
det(1 - Fr*T | H1),
```

a finite-rank determinant. Perhaps the archimedean regularized determinant
or trace-class compactness supplies the missing finite datum without a
finite constant field.

This is a serious repair because it contains a real positive fact:
Connes' trace formula supplies a regularized trace/count at infinity. The
failure is narrower. Compactness gives discreteness and trace data; it
does not force the radius/purity. Over finite fields, finite rank does not
by itself imply `|alpha|=sqrt(q)`. At infinity, the regularized determinant
is functional-equation symmetric; pinning the spectrum to `Re(s)=1/2` is
Weil positivity/RH, not an independent construction of `End(S^2/Z)`.

This document is local. It rejects only the shortcut:

```text
trace-class / regularized determinant data itself supplies the radius and
constructs End(S^2/Z).
```

## 2. Lemma

```text
Lemma 204.1 (Trace-class finiteness is radius-silent).

Over F_q, H1(C) is finite-dimensional, so Frobenius is finite-rank and
det(1 - Fr*T | H1) is a finite polynomial. This determinant carries
trace/count data. When Frobenius is pure, its roots also lie on the radius
q^{1/2}.

However, finite rank does not force purity: one can perturb a conjugate
pair off the circle while preserving the finite-rank determinant type. The
determinant remains finite; the radius condition fails.

At infinity, Connes' regularized determinant supplies the trace-formula
side: the explicit-formula count/location datum. But the determinant is
functional-equation symmetric, so `Re(s)=1/2` is the FE-fixed locus. Pinning
the spectrum to that locus is Weil positivity/RH, not an independent
radius marker.

Consequently compactness, nuclearity, or regularized determinant data
constructs no square-side iota/properness theorem, square H2, intersection
form, correspondence algebra, Frobenius graph, Laurent boundary data,
torsor splitter, DD.4 weight>=1 datum, or positive Rosati involution.

Therefore regularized determinant compactness cannot itself be promoted to
End(S^2/Z).
```

Verdict label:

```text
N1B_REGULARIZED_DETERMINANT__TRACE_NOT_RADIUS_NOT_END_S2Z__NO_GO.
```

## 3. Proof

`prime_int_n1b_regularized_determinant_no_go` verifies the R1 gate, with
`regularized_determinant_radius` rerun as the adjacent witness.

RDR1 records the finite-field anchor. For the tested examples, `H1` has
finite dimension and the pure examples have zero radius deviation.

RDR2 records the key separation. Off-circle perturbations preserve the
finite determinant type but break the radius:

```text
E_ordinary_q5: radius deviation 0.671
genus2_q2:    radius deviation 0.424
```

Thus finite rank and trace-class compactness do not force purity.

RDR3 records the archimedean determinant type check. The regularized trace
exists and supplies a finiteness that cardinality could not; nevertheless
the determinant does not mark `Re(s)=1/2`. The line is the FE-fixed locus,
and pinning the spectrum there is Weil positivity/RH.

RDR4 records the combined decision: compactness supplies count/location,
not independent purity.

RDR5 records DH-vacuity: DH has no Frobenius and no
`det(1 - Fr*T | H1)` analogue, so the determinant/radius question is
unposable for the control.

RDR6 records the carrier failure: no carrier-native purity on the spectrum,
archimedean monodromy `N`, Weil positivity theorem, independent radius
marker, finite constant field, square-side `iota`/properness, square H2,
intersection form, correspondence algebra, Frobenius graph, positive
Rosati, Laurent boundary, torsor splitter, or DD.4 weight>=1 datum is
constructed.

## 4. Impact on R1

```text
R1 after docs 138-204:
  NEWLY CLOSED THIS CYCLE:
    - regularized determinant / trace-class compactness / finite-rank
      determinant as End(S^2/Z), independent radius marker, carrier-native
      purity on the spectrum, archimedean monodromy N on the spectrum,
      finite constant field, Frobenius/base size, square-side
      iota/properness, square H2/intersection form, Laurent boundary data,
      torsor splitter, DD.4 weight>=1 datum, or positive Rosati (doc 204).

  STILL ADMISSIBLE:
    - a nuclear/trace-class construction that also constructs purity or the
      archimedean monodromy/Rosati datum carrier-natively, rather than only
      the trace/count;
    - a future F1 or family construction that manufactures a finite
      constant/residue-field cardinality at the archimedean place without
      selecting a finite level externally;
    - a non-product compactified square whose middle correspondence is
      indecomposable rather than Kunneth-factored;
    - a square-side iota/properness theorem that makes the correspondence
      algebra global rather than one-place-tensored.

  STILL OPEN:
    - a genuinely different carrier whose first
      correspondence/multiplication constructs the square data internally
      and finishes DD.4 weights>=1.
```

R1 is still open. Compactness is a real positive datum, but only on the
trace/count axis. The radius/purity axis is still the missing square/Rosati
datum. R2 remains locked.

## 5. Kill Conditions

```text
KILL-RDR.1 finite rank as purity
  A proposal says finite rank or trace-class status forces the radius. Kill
  it: off-circle finite-rank determinants remain finite but fail purity.

KILL-RDR.2 regularized trace as radius
  A proposal identifies the explicit-formula trace/count with the
  radius-line bound. Kill it unless it constructs an independent positivity
  or purity datum.

KILL-RDR.3 FE symmetry as radius marker
  A proposal uses det(s)=det(1-s) as the radius. Kill it: the FE-fixed line
  is DH-shared; pinning zeros there is Weil positivity/RH.

KILL-RDR.4 Connes determinant as End(S^2/Z)
  A proposal promotes the archimedean regularized determinant directly to
  the square correspondence algebra. Kill it unless it also constructs the
  compactified square, correspondences, and Rosati.

KILL-RDR.5 compactness as DD.4 weight>=1
  A proposal treats nuclearity/discreteness as the DD.4 weight datum. Kill
  it unless the carrier constructs the Laurent boundary and weight>=1
  self-duality datum.

KILL-RDR.6 DH-vacuity as zeta correspondence construction
  A proposal notes DH has no Frobenius determinant and promotes that to
  End(S^2/Z). Kill it unless the zeta-side square maps, correspondences,
  purity, and Rosati are actually constructed.
```

## 6. Board

```text
doc-137 R1, cycle 67 = doc 204:
  N1B_REGULARIZED_DETERMINANT__TRACE_NOT_RADIUS_NOT_END_S2Z__NO_GO.

What got built: no End object. The value is a sharper boundary theorem:
compactness supplies trace/count finiteness but not the radius/purity datum.

What remains: construct purity/Rosati on the discrete spectrum
carrier-natively; construct a finite base-size marker carrier-natively;
construct an indecomposable compactified square correspondence; solve
square-side iota/properness; or return to the in-house PFD/Xbar DD.4
weight>=1 obstruction.
```
