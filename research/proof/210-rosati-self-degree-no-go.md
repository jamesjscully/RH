# 210 - Rosati self-degree does not construct End(S^2/Z)

Status: no-go + Rosati self-degree circularity boundary, 2026-06-20.
Seventy-third cycle of the doc-137 construction arc. Doc 209 killed the
determinant-descent shortcut: product/FE data gives the edge, not the split.
This document tests the next repair: use abstract positive Rosati on an
archimedean polarized abelian variety to force the split.

```text
polarized AV + endomorphism F
  -> positive Rosati and F F^dag = deg(F)
  -> |alpha| = sqrt(deg(F))
  -> prescribed zeta center
  -> End(S^2/Z).
```

Witness, lead-reran this cycle:
`prime_int_n1b_rosati_self_degree_no_go` (RSD1-RSD6 ALL PASS) -- the
on-prescribed-radius model has positive Rosati and self-degree `q`;
off-prescribed-radius endomorphisms still have positive Rosati but with
`F F^dag=r^2`, not the external `q`; integrality gives an endomorphism's
own norm; the Rosati positivity condition is exactly the line-forcing
content; over `Z`, the edge diagonal and FE reflection transfer but the
off-diagonal Rosati coupling does not; and no square/Rosati/R1 data is built.

Adjacent witnesses, lead-reran this cycle:
`rosati_circularity_skeptic` (exit 0) and `rosati_reflection` (exit 0).

## 1. Purpose

After doc 209, the missing datum is positive Rosati on a constructed global
carrier. The tempting shortcut is to move to a polarized abelian variety,
where Rosati positivity is automatic, and then read the radius from
`F F^dag=deg(F)`.

The issue is that the degree is not an external base size unless the carrier
constructs it. It is the endomorphism's own norm. An off-prescribed-radius
endomorphism can still admit a positive polarization; its self-degree simply
changes.

This document rejects only the shortcut:

```text
abstract polarized-AV Rosati positivity itself supplies the zeta base size
and therefore constructs End(S^2/Z).
```

## 2. Lemma

```text
Lemma 210.1 (Rosati self-degree is not the prescribed zeta radius).

On a polarized abelian variety, Rosati positivity and the self-degree identity
force an endomorphism F to satisfy

    F F^dag = deg(F),
    |alpha| = sqrt(deg(F))

relative to F's own degree.

This does not force |alpha|=sqrt(q) for an externally prescribed q. A planted
complex conjugate pair with modulus r != sqrt(q) admits a positive
polarization and positive Rosati form, but its Rosati scalar is r^2, not q.

Integrality does not repair this. For an imaginary quadratic integer alpha,
the corresponding CM torus has alpha as an endomorphism and the degree is
N(alpha)=alpha alpha-bar=|alpha|^2. The radius is again forced only relative
to the endomorphism's own norm.

In the function-field anchor, Rosati positivity of the full trace form is
exactly the line-forcing theorem. The edge identity and FE/Rosati reflection
transfer as shadows over Z, but the positive full Rosati Gram needs the
off-diagonal Frobenius/correspondence coupling. That is the missing
Hodge-index/RH content, not a consequence of the edge diagonal or reflection.

Consequently abstract Rosati self-degree constructs no global gr^W_1 carrier
over Z, no externally prescribed base size q, no carrier-native
self-degree relation, no off-diagonal Rosati coupling, no q-power map, no
uniform modulus bound, no DH-killing carrier, no finite constant field, no
square-side iota/properness theorem, no square H2, intersection form,
correspondence algebra, Frobenius graph, Laurent boundary data, torsor
splitter, DD.4 weight>=1 datum, or positive Rosati on End(S^2/Z).

Therefore Rosati self-degree cannot itself be promoted to End(S^2/Z).
```

Verdict label:

```text
N1B_ROSATI_SELF_DEGREE__OWN_NORM_NOT_EXTERNAL_Q__NO_GO.
```

## 3. Proof

`prime_int_n1b_rosati_self_degree_no_go` verifies the R1 gate, with
`rosati_circularity_skeptic` and `rosati_reflection` rerun as adjacent
witnesses.

RSD1 records the on-prescribed-radius anchor. For `q=7`, the model has a
positive polarization, positive Rosati form, and `F F^dag=7=|alpha|^2`.

RSD2 records the decisive off-prescribed-radius test. With
`|alpha|=1.3 sqrt(7)`, a positive polarization and positive Rosati form still
exist, but

```text
F F^dag = 11.83 = |alpha|^2 != 7.
```

Thus positive Rosati does not obstruct the off-prescribed-radius
endomorphism; it only changes the self-degree.

RSD3 records the integrality check. Gaussian integer examples have degrees

```text
1+i:2, 2+i:5, 1+2i:5, 3+i:10.
```

Each degree is the endomorphism's own norm. Integrality gives
`|alpha|=sqrt(N(alpha))`, not `|alpha|=sqrt(q)` for an independently
specified `q`.

RSD4 records the function-field Rosati anchor. The trace-form determinant
`4q-a^2` tracks the line exactly: positivity is the line-forcing theorem.

RSD5 records the Z-audit. The edge diagonal and FE reflection transfer as
shadows, but not as a constructed algebraic involution on `End(S^2/Z)`, and
the full Rosati positivity is exactly the missing off-diagonal
Frobenius/correspondence coupling.

RSD6 records the construction failure: no global `gr^W_1` carrier over `Z`,
carrier-native purity theorem, external `q`/base-size datum,
carrier-native self-degree relation, positive Rosati, off-diagonal Rosati
coupling, q-power map, uniform modulus bound, DH-killing carrier, finite
constant field, square-side `iota`/properness, square H2, intersection form,
correspondence algebra, Frobenius graph, Laurent boundary, torsor splitter,
or DD.4 weight>=1 datum is constructed.

## 4. Impact on R1

```text
R1 after docs 138-210:
  NEWLY CLOSED THIS CYCLE:
    - abstract polarized-AV Rosati as End(S^2/Z), Rosati self-degree as an
      external zeta base size, integrality as prescribed q, FE reflection as
      algebraic Rosati on End(S^2/Z), edge diagonal as full Rosati
      positivity, determinant/Rosati trace diagonal as off-diagonal coupling,
      finite constant field, Frobenius/base size, square-side
      iota/properness, square H2/intersection form, Laurent boundary data,
      torsor splitter, DD.4 weight>=1 datum, or positive Rosati (doc 210).

  STILL ADMISSIBLE:
    - a global glued carrier that constructs `gr^W_1` and the external base
      size before applying Rosati;
    - a non-product compactified square whose correspondence algebra supplies
      the off-diagonal Rosati coupling;
    - a zeta-native positivity theorem whose hypotheses are built by the
      carrier and which kills DH/Epstein at carrier formation.

  STILL OPEN:
    - a genuinely different carrier whose first
      correspondence/multiplication constructs the square data internally
      and finishes DD.4 weights>=1.
```

R1 is still open. This cycle prevents a subtle promotion error: Rosati
positivity is not enough unless the construction also supplies the correct
external base-size/Frobenius graph and the off-diagonal correspondence
coupling. R2 remains locked.

## 5. Kill Conditions

```text
KILL-RSD.1 self-degree as external q
  A proposal reads the zeta base size from `deg(F)` after choosing F. Kill it:
  `deg(F)` is F's own norm unless q is constructed independently.

KILL-RSD.2 abstract AV positivity as radius theorem
  A proposal says positive Rosati forbids off-radius endomorphisms. Kill it:
  off-prescribed-radius endomorphisms still have positive Rosati, with a
  different self-degree.

KILL-RSD.3 integrality as prescribed radius
  A proposal says integrality forces the critical radius. Kill it unless it
  also constructs the external q: integrality gives the algebraic norm.

KILL-RSD.4 FE reflection as algebraic Rosati
  A proposal uses the functional equation reflection as Rosati on
  `End(S^2/Z)`. Kill it unless the correspondence algebra is constructed.

KILL-RSD.5 edge diagonal as full positivity
  A proposal promotes the edge norm-square diagonal to the full Rosati Gram.
  Kill it unless it supplies the off-diagonal Frobenius/correspondence
  coupling.

KILL-RSD.6 Rosati self-degree as End(S^2/Z)
  A proposal promotes abstract self-degree directly to the square
  correspondence algebra. Kill it unless it constructs square H2,
  intersection form, correspondences, Frobenius graph, Laurent boundary data,
  DD.4 weight>=1 datum, and positive Rosati.
```

## 6. Board

```text
doc-137 R1, cycle 73 = doc 210:
  N1B_ROSATI_SELF_DEGREE__OWN_NORM_NOT_EXTERNAL_Q__NO_GO.

What got built: no End object. The value is a sharper Rosati theorem:
positive Rosati forces radius relative to a self-degree; the construction
still must supply the external zeta base size and off-diagonal correspondence
coupling.

What remains: construct the global `gr^W_1` carrier; construct the external
base-size/q-power/Frobenius graph on it; construct positive Rosati with the
off-diagonal correspondence coupling; construct an indecomposable
compactified square correspondence; solve square-side iota/properness; or
return to the in-house PFD/Xbar DD.4 weight>=1 obstruction.
```
