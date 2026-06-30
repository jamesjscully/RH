# 235 - CM Shimura data does not construct the square

Status: no-go + CM/Shimura-Taniyama carrier boundary, 2026-06-20.
Ninety-eighth cycle of the doc-137 construction arc. Doc 234 killed
Tate/Hodge fixed subspaces as square construction. This document tests a
stronger positivity repair: put the would-be Frobenius inside a CM
endomorphism field, use Shimura-Taniyama / CM theory to identify Rosati with
complex conjugation, and read the radius from the norm identity.

```text
CM abelian carrier + CM type + pi*pi_bar=q
  -> Rosati = complex conjugation
  -> radius forced for that CM object
  -> End(S^2/Z).
```

Witness, lead-reran this cycle:
`prime_int_n1b_cm_shimura_carrier_no_go` (CMST1-CMST7 ALL PASS) -- the CM
norm identity genuinely forces the radius for actual CM objects; the same
abstract CM type profile does not determine a count anchor; an off-radius
fake CM adjoint `q/pi` is not complex conjugation; a CM endomorphism does not
construct NS degree slots; formal CM labels are formable on controls without
a CM carrier; the CM theorem applies only after a CM carrier exists; and no
square package over `Z` is built.

Adjacent witnesses, lead-reran this cycle:
`cm_shimura_taniyama` (exit 0), `prime_int_n1b_rosati_self_degree_no_go`
(RSD1-RSD6 ALL PASS), and
`prime_int_n1b_tate_cycle_fixed_subspace_no_go` (TCF1-TCF7 ALL PASS).

## 1. Purpose

Doc 210 already killed the abstract Rosati self-degree shortcut: positive
Rosati forces a radius only relative to the endomorphism's own degree, not an
externally prescribed zeta base size. Doc 234 killed the fixed-cycle repair:
Tate/Hodge fixed classes are downstream of a carrier and do not construct
`rep_NS`.

The CM repair is different enough to test separately. For a CM abelian
variety, Shimura-Taniyama / CM theory is a real theorem: a Frobenius element
`pi` in a CM field satisfies

```text
    pi * pi_bar = q,
```

and because the CM involution is complex conjugation, `|pi|=sqrt(q)` follows
without a separate RH input for that CM object.

That is a genuine theorem, not circularity. The failed step is promotion:

```text
because CM objects have automatic positivity, the zeta square carrier has
been constructed.
```

This document rejects only that promotion. It does not reject a future
zeta-native square which first constructs a CM endomorphism carrier, its
degree map, proper correspondences, projection formula, Frobenius graph, and
Rosati relation.

## 2. Lemma

```text
Lemma 235.1 (CM positivity is not the zeta square carrier).

For the genuine CM element pi=1+2i, the norm identity is exact:

    N(pi)=5,        5/pi = 1-2i = pi_bar.

Thus the CM mechanism really forces the radius for the CM object.

However, the abstract CM type profile

    imaginary quadratic field,
    conjugation,
    CM type,
    norm-degree identity,
    Rosati = complex conjugation

does not determine the finite-field count anchor. The profile is the same
for pi=1+2i and pi=2+3i, while the count windows differ:

    N(1+2i)=5:   4, 32, 148, 640
    N(2+3i)=13: 10, 180, 2290, 28800.

If an external q is fixed and pi is off that radius, the algebraic adjoint
`q/pi` is not complex conjugation. With q=9 and `|pi|=1.4 sqrt(q)`, the
defect

    |q/pi - pi_bar| = 2.057

is nonzero. Equality is exactly the radius condition.

Nor does a CM endomorphism construct the NS degree slots. Keeping the same
CM z-operator while changing only the formal degree slot changes

    Delta . Gamma  from 4 to 7.

The endomorphism field is not the diagonal, graph, degree maps, projection
formula, or square correspondence category.

Formal CM labels are also unsafe as carrier substitutes: one can declare a
quadratic field and involution around control data while no actual CM
abelian carrier, CM endomorphism ring, square, or positive Rosati on the
square exists.

Finally, the zeta object and Davenport-Heilbronn controls do not acquire a
CM abelian carrier merely because CM theory exists. The theorem applies only
after a CM carrier and Frobenius element in its endomorphism field have
already been constructed.

Consequently a CM/Shimura-Taniyama package constructs no CM carrier over the
zeta square, CM type, CM endomorphism field, `rep_NS`, actual square, proper
correspondence category, fiber-product composition, carrier-native degree
maps, carrier-native pairing, projection formula, Frobenius graph, positive
Rosati, DH/Epstein death, DD.4 weight>=1 datum, or End(S^2/Z).
```

Verdict label:

```text
N1B_CM_SHIMURA_CARRIER__CM_THEOREM_NEEDS_CARRIER__NO_GO.
```

## 3. Proof

`prime_int_n1b_cm_shimura_carrier_no_go` verifies the seven gates.

CMST1 records the positive anchor. For `pi=1+2i`, `N(pi)=5`,
`5/pi=1-2i`, and this equals complex conjugation. The radius is genuinely
forced for that CM object.

CMST2 records profile non-determination. The same toy CM type profile
supports `1+2i` and `2+3i`, but their count windows differ:

```text
4, 32, 148, 640
10, 180, 2290, 28800.
```

The type profile is not the square carrier or count anchor.

CMST3 records the off-radius adjoint failure. For q=9 and an off-radius
`pi`, `q/pi` differs from `pi_bar` by `2.057`. Therefore the CM shortcut
forces the radius only after one has the CM field/involution package whose
conjugation is already the correct positive Rosati.

CMST4 records the NS-degree-slot failure. The same CM z-operator gives
different `Delta.Gamma` values after changing only the formal `d1` slot:

```text
4 -> 7.
```

The CM endomorphism has not constructed the two degree maps.

CMST5 records control formability. Formal quadratic-field and involution
labels can be declared on control data, with the same adjoint defect and no
actual CM abelian carrier, endomorphism ring, square, or Rosati.

CMST6 records applicability. A CM elliptic anchor has a carrier; the zeta
candidate and DH controls do not have a CM abelian carrier, CM endomorphism
field, or CM Frobenius element.

CMST7 records the construction failure: no CM carrier/type/endomorphism
field, `rep_NS`, actual square, proper correspondence category,
fiber-product composition, carrier-native degree maps, carrier-native
pairing, projection formula, Frobenius graph, positive Rosati, control
death, or DD.4 weight>=1 datum is constructed.

## 4. Impact on R1

```text
R1 after docs 138-235:
  NEWLY CLOSED THIS CYCLE:
    - CM/Shimura-Taniyama theorem as global square carrier, CM type as
      rep_NS construction, CM endomorphism field as degree-slot
      construction, norm identity as external zeta q, formal CM involution
      as positive Rosati on End(S^2/Z), and CM-applicability as DH/Epstein
      carrier death (doc 235).

  STILL ADMISSIBLE:
    - a carrier-native global square over Z which constructs a CM
      endomorphism algebra before using a CM theorem;
    - a theorem proving the zeta square is an actual CM object with proper
      correspondences, degree maps, projection formula, Frobenius graph, and
      positive Rosati;
    - a non-CM zeta-native positivity theorem whose hypotheses are built by
      the square carrier and which kills controls at carrier formation.

  STILL OPEN:
    - construct rep_NS over Z with an actual square carrier, proper
      correspondence category or carrier-native proper dg enhancement,
      fiber-product composition, carrier-native degree maps, canonical
      pairing and projection formula, off-diagonal intersection form,
      preserved trace/count anchor, positive Rosati, DD.4 weight>=1 data, and
      square-side properness.
```

R1 remains open. This cycle closes the CM shortcut without discarding the
CM theorem: the theorem is useful only downstream of the missing carrier.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-CMST.1 CM theorem as square construction
  A proposal invokes Shimura-Taniyama or CM purity and calls it the square.
  Kill it unless the CM abelian carrier and square correspondence category
  have already been constructed.

KILL-CMST.2 CM type as count anchor
  A proposal reads the zeta count anchor from an abstract CM type. Kill it:
  the same type profile supports different norm/count windows.

KILL-CMST.3 q/pi as complex conjugation
  A proposal declares the algebraic adjoint `q/pi` to be complex conjugation.
  Kill it unless the CM field embedding and positive Rosati relation are
  constructed; equality is the radius condition.

KILL-CMST.4 CM endomorphism as rep_NS
  A proposal treats a CM endomorphism field as the NS correspondence carrier.
  Kill it unless the two degree slots, diagonal, Frobenius graph,
  off-diagonal intersections, and projection formula are constructed.

KILL-CMST.5 formal CM labels
  A proposal adds a quadratic field/involution label to arbitrary control
  data. Kill it unless an actual CM abelian carrier and endomorphism ring are
  built.

KILL-CMST.6 CM applicability as control death
  A proposal says DH lacks CM, hence zeta wins. Kill it unless zeta has the
  CM carrier that DH lacks. Otherwise both fail the carrier hypothesis.

KILL-CMST.7 CM package as End(S^2/Z)
  A proposal promotes CM theory directly to End(S^2/Z). Kill it unless it
  constructs square H2, intersection form, correspondences, Frobenius graph,
  Laurent boundary data, DD.4 weight>=1 datum, and positive Rosati.
```

## 6. Board

```text
doc-137 R1, cycle 98 = doc 235:
  N1B_CM_SHIMURA_CARRIER__CM_THEOREM_NEEDS_CARRIER__NO_GO.

What got built: no End object. The value is a sharper applicability theorem:
CM forces radius for actual CM objects, but the CM hypothesis is itself a
carrier theorem and does not construct the zeta square.

What remains: construct the global square carrier; construct degree maps,
diagonal, Frobenius graph, correspondence composition, projection formula,
and positive Rosati; or prove a zeta-native CM carrier theorem that supplies
those data before invoking Shimura-Taniyama.
```
