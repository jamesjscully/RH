# 214 - Isospectral graph data does not construct the square carrier

Status: no-go + isospectral carrier boundary, 2026-06-20. Seventy-seventh
cycle of the doc-137 construction arc. Doc 213 killed finite trace
realization as a graph carrier. This document tests the stronger repair: use
the full spectrum or conjugacy class, so all power traces and graph
composition are preserved.

```text
full spectrum / all power traces
  -> graph law up to conjugacy
  -> Frobenius/Hecke graph carrier
  -> End(S^2/Z).
```

Witness, lead-reran this cycle:
`prime_int_n1b_isospectral_graph_carrier_no_go` (ISG1-ISG6 ALL PASS) --
the genuine finite-field block has an integral graph, `q`-similitude, and the
right Hodge sign; noncanonical similarities preserve all sampled power traces,
characteristic polynomial, and graph law; the same similarities move the
integral lattice and cup form; Rosati can be transported only after choosing
the similarity; isospectral conjugacy is formable on controls; and no square
package over `Z` is built.

Adjacent witness, lead-reran this cycle:
`prime_int_n1b_finite_trace_realization_no_go` (FTR1-FTR6 ALL PASS).

## 1. Purpose

Doc 213 says finitely fitting an operator to traces is not a carrier. The
stronger repair is to use the whole spectral package:

```text
power traces for all n,
the characteristic polynomial,
and the semigroup law A^m A^n = A^{m+n}.
```

This fixes the conjugacy class of a finite semisimple operator, but the
finite-field square needs more than a conjugacy class. It needs an integral
lattice, a cup/Rosati pairing, an `NS` square, off-diagonal intersections,
and a carrier-native reason controls cannot form the same package.

This document rejects only the shortcut:

```text
full isospectral graph data constructs the Frobenius/Hecke graph carrier
required by End(S^2/Z).
```

## 2. Lemma

```text
Lemma 214.1 (Isospectral graph data is not square-carrier data).

Let F be a finite-field Frobenius block preserving an integral lattice and
a cup form E:

    F^T E F = q E.

For any invertible P, the conjugate A=P F P^{-1} has the same characteristic
polynomial, the same power traces, and the same graph law:

    A^m A^n = A^{m+n}.

Thus full spectral data and graph composition do not determine the lattice or
the pairing.

For a nonintegral non-symplectic P, A no longer preserves the original
integral lattice and does not satisfy the q-similitude relation with the
original cup form. One can transport the cup form to

    E_P = P^{-T} E P^{-1},

and then A becomes a q-similitude again. But this shows the missing choice:
the Rosati/cup pairing has moved with P. The spectrum did not choose it.

The same isospectral conjugacy operation is formable on arbitrary control
operators. It consumes no Euler product, Satake parameters, `rep_NS`,
intersection form, or Rosati duality.

Consequently isospectral graph data constructs no `rep_NS`, integral
lattice, canonical pairing, off-diagonal intersections, positive Rosati,
DH/Epstein death, DD.4 weight>=1 datum, or End(S^2/Z).

Therefore full spectral/conjugacy data cannot itself be promoted to the
square Frobenius graph carrier.
```

Verdict label:

```text
N1B_ISOSPECTRAL_GRAPH_CARRIER__CONJUGACY_NOT_LATTICE_NOT_ROSATI__NO_GO.
```

## 3. Proof

`prime_int_n1b_isospectral_graph_carrier_no_go` verifies the six gates.

ISG1 records the genuine finite-field block. For two genus-1 blocks at
`q=7`, the graph matrix is integral, the `q`-similitude defect is zero, and
the primitive Hodge index is negative:

```text
H = -24.000.
```

ISG2 records the isospectral similarity test. A noncanonical similarity
preserves the sampled power traces, the characteristic polynomial, and graph
law. The sampled graph-law defect is `7.9e-15`.

ISG3 records the carrier failure relative to the original square data. The
isospectral graph has nonintegral entries and fails the original cup form:

```text
integral_defect = 0.440,
qsim_original   = 13.567.
```

ISG4 records the transported-Rosati ambiguity. Transporting the cup form
along the chosen similarity restores `q`-similitude with defect `9.9e-16`,
but the transported pairing differs from the original, and different
similarities give different transported pairings:

```text
|E1 - E|  = 0.620,
|E1 - E2| = 1.168.
```

Thus the spectrum did not construct the Rosati pairing; it moved with an
external choice of similarity.

ISG5 records control formability. The same isospectral conjugacy operation
preserves power traces for arbitrary control operators without Euler product,
Satake parameters, `rep_NS`, or Rosati.

ISG6 records the construction failure: no `rep_NS`, integral lattice,
canonical pairing, off-diagonal intersections, positive Rosati, control
death, or DD.4 weight>=1 datum is constructed.

## 4. Impact on R1

```text
R1 after docs 138-214:
  NEWLY CLOSED THIS CYCLE:
    - full spectrum/all power traces as Frobenius graph carrier,
      characteristic polynomial/conjugacy class as End(S^2/Z), transported
      Rosati by similarity as carrier-native pairing, and isospectral
      conjugacy as DH/Epstein carrier guard (doc 214).

  STILL ADMISSIBLE:
    - a zeta-native graph whose lattice and pairing are constructed by the
      carrier, not transported by a chosen similarity;
    - a square correspondence algebra with off-diagonal pairings;
    - a carrier-native Rosati/cup pairing and positivity theorem;
    - a construction that kills DH/Epstein before spectral conjugacy.

  STILL OPEN:
    - construct `rep_NS` over Z with an integral graph carrier, canonical
      pairing, off-diagonal intersection form, positive Rosati, DD.4
      weight>=1 data, and square-side properness.
```

R1 remains open. This cycle closes the full-spectrum version of the graph
shortcut: spectra and graph laws are still not a square correspondence
object.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-ISG.1 spectrum as square carrier
  A proposal promotes the full spectrum or all power traces to Gamma. Kill it
  unless it also constructs the lattice, pairing, and off-diagonal
  correspondences.

KILL-ISG.2 conjugacy class as End(S^2/Z)
  A proposal says the characteristic polynomial/conjugacy class is the graph
  carrier. Kill it: noncanonical similarities preserve it while moving the
  lattice and cup form.

KILL-ISG.3 transported Rosati as construction
  A proposal transports a pairing along a chosen similarity. Kill it unless
  the similarity and pairing are carrier-native; otherwise Rosati is being
  chosen, not constructed.

KILL-ISG.4 isospectral control guard
  A proposal uses isospectrality to distinguish zeta from controls. Kill it:
  arbitrary control operators have the same conjugacy operation.

KILL-ISG.5 isospectral graph as square package
  A proposal promotes spectral graph data to End(S^2/Z). Kill it unless it
  constructs rep_NS, integral lattice, canonical pairing, off-diagonal
  intersections, positive Rosati, square-side properness, Laurent boundary
  data, and DD.4 weight>=1.
```

## 6. Board

```text
doc-137 R1, cycle 77 = doc 214:
  N1B_ISOSPECTRAL_GRAPH_CARRIER__CONJUGACY_NOT_LATTICE_NOT_ROSATI__NO_GO.

What got built: no End object. The value is a sharper graph boundary:
full spectral graph data is only conjugacy data; the square lattice and
Rosati pairing are not constructed by it.

What remains: construct the zeta-side rep_NS carrier; construct the integral
graph lattice; construct the canonical cup/Rosati pairing; construct the
off-diagonal intersection form and positivity; construct DH/Epstein death at
carrier formation; solve DD.4 weights>=1 and square-side iota/properness.
```
