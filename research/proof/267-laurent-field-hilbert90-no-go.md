# 267 - Laurent-field Hilbert 90 is not the carrier boundary

Status: no-go + Laurent-field/Hilbert-90 deletion, 2026-06-20.
One-hundred-thirtieth cycle of the doc-137 construction arc. Docs 264-266
closed Frobenius-root, perfection-colimit, and root-shift telescope repairs.
This document tests the strongest remaining Laurent repair:

```text
pass from U_1 = 1 + z F_2[[z]] to the full Laurent field K^*
and use Hilbert 90.
```

Witness, lead-reran this cycle:
`prime_int_n1b_laurent_field_hilbert90_no_go` (LFH1-LFH6 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_root_shift_telescope_no_go`,
`prime_int_n1b_prime_line_no_go`,
`prime_int_n1b_dd4_scc_interface`, and
`prime_int_n1b_square_carrier_contract`.

## 1. Purpose

Doc 263 killed the weak slogan:

```text
c * phi(c) = 1, therefore c is harmless.
```

That slogan is false inside the 1-unit coefficient system. But the full
Laurent field contains an actual Hilbert-90 splitter:

```text
phi(z) = z/(1+z).
```

So one might try to repair DD.4/SCC by saying that the missing carrier is
just the Laurent field, where the obstruction is a coboundary.

This document rejects only that shortcut. The coboundary identity is real,
but it uses the valuation/uniformizer axis outside `U_1`. It does not
construct the square carrier.

## 2. Lemma

```text
Lemma 267.1 (Laurent-field Hilbert 90 uses valuation, not carrier boundary).

Let

    U_1 = 1 + z F_2[[z]],
    K = F_2((z)),
    phi(z) = z/(1+z),
    c = (1+z)^-1.

In U_1, for truncations L=6,8,10,12:

    H^1(<phi>; U_1) = Z/2,
    [c] != 0,
    res_1(c)=1.

In K^*, however,

    b = phi(z) = z/(1+z)
    phi(b) = z
    b / phi(b) = c.

Thus the obstruction dies in the full Laurent field. Equivalently, in the
decomposition K^* = z^Z x U_1, the boundary of a valuation-m element has
unit class

    m * [c]  in H^1(<phi>; U_1).

The witness checks m=-3,...,3: odd valuation kills [c], even valuation
does not. The killing is exactly the parity of the valuation axis.

That valuation axis is not the TCR/DMP carrier line: DMP support for
`TCR(F_2;2)^{phi Z/2}` has no classes in degrees <= -2, while a Laurent
line has one class in every degree. The same uniformizer-splitting recipe
is formable on controls. No actual square, integral rep_NS, two degree maps,
indecomposable diagonal, Frobenius graph, proper correspondence category,
fiber-product composition, projection formula, canonical Rosati, positive
primitive sign, carrier boundary, or control death is constructed.
```

Verdict label:

```text
N1B_LAURENT_FIELD_HILBERT90__VALUATION_SPLITTER_NOT_CARRIER__NO_GO.
```

## 3. Proof

`prime_int_n1b_laurent_field_hilbert90_no_go` verifies six gates.

LFH1 recomputes the base 1-unit obstruction:

```text
L6:  |B|=2^3, |Z1|=2^4, |H1|=2
L8:  |B|=2^4, |Z1|=2^5, |H1|=2
L10: |B|=2^5, |Z1|=2^6, |H1|=2
L12: |B|=2^6, |Z1|=2^7, |H1|=2
```

and checks `c` is non-boundary with `res_1(c)=1`.

LFH2 checks the Laurent-field identity:

```text
b = phi(z) = z/(1+z),
phi(b) = z,
b / phi(b) = c.
```

Adding `c` to the 1-unit boundary subgroup collapses the tested H1 quotient
to the trivial group. This records the positive Hilbert-90 fact.

LFH3 records what the identity costs. A valuation-m element has boundary
class `m[c]` modulo 2. Thus the splitter exists only after leaving the
valuation-zero 1-unit sector.

LFH4 reruns the DMP/TCR support guard from doc 139:

```text
missing Laurent degrees: -6,-5,-4,-3,-2.
```

So the full Laurent valuation line is not present in the geometric
`TCR(F_2;2)^{phi Z/2}` support.

LFH5 repeats the same uniformizer-splitting recipe on exact `F_2` controls
in dimensions `1,2,4,8`. No square-carrier data is used.

LFH6 applies the SCC contract: Laurent-field Hilbert 90 supplies no
square-carrier slot.

## 4. Impact on R1

```text
R1 after docs 138-267:
  NEWLY CLOSED THIS CYCLE:
    - promoting full Laurent-field Hilbert 90, or the identity
      phi(z)/z=(1+z)^-1, to the DD.4/SCC carrier boundary.

  POSITIVE INFORMATION RETAINED:
    - the DD.4 obstruction is exactly the missing odd valuation axis;
    - any real carrier that kills [c] must explain why that valuation axis
      is carrier-native and why DMP/TCR support and controls do not get it
      for free.

  STILL ADMISSIBLE:
    - a carrier-native valuation/uniformizer axis produced by the actual
      square carrier, with properness, projection, Rosati, and control death
      built at the same step;
    - a carrier-native boundary/properness/self-duality map killing [c]
      without importing the full Laurent line as external data;
    - a proof that no such carrier-native valuation/boundary extension can
      exist, with a named mechanism and witness.

  STILL OPEN:
    - construct the actual carrier-native DD.4 extension;
    - then construct the zeta-side square carrier over Z.
```

This closes only the bare Laurent-field/Hilbert-90 promotion. It does not
close a future carrier where the square itself constructs the valuation
axis and the SCC slots.

## 5. Kill conditions

```text
KILL-LFH.1 Laurent-field Hilbert 90 promoted to carrier
  A proposal says K^* has H^1=0, so DD.4 is solved. Kill it unless the
  Laurent field and valuation axis are produced by the actual square carrier.

KILL-LFH.2 uniformizer splitter promoted to properness
  The identity b=phi(z), b/phi(b)=c is an odd-valuation boundary. It is not
  the carrier's boundary/properness/self-duality map.

KILL-LFH.3 valuation axis imported
  The class dies precisely because the coefficient system left U_1 and
  allowed valuation one. A carrier must construct that axis natively.

KILL-LFH.4 DMP support ignored
  DMP/TCR support bottoms at degree -1 and lacks the full Laurent line. Do
  not read the whole valuation axis into the geometric fiber.

KILL-LFH.5 control formability ignored
  The same valuation-axis splitting can be declared on controls. If the move
  exists before carrier formation, DH/Epstein have not died.

KILL-LFH.6 SCC slots bypassed
  Laurent-field Hilbert 90 without the square, integral rep_NS, degree maps,
  diagonal, graph, proper correspondences, projection formula, Rosati,
  positive primitive sign, and control death is not End(S^2/Z).
```
