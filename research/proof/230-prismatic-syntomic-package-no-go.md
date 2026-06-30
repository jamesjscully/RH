# 230 - Prismatic/syntomic packages do not construct the square

Status: no-go + prismatic/syntomic/p-adic-comparison boundary, 2026-06-20.
Ninety-third cycle of the doc-137 construction arc. Doc 229 killed
six-functor/Lefschetz-Verdier trace formalism as square construction. This
document tests the next p-adic repair: use BMS/prismatic/syntomic comparison
data, p-complete `TC^-`/`TP`, Nygaard filtration, Frobenius, and comparison
maps as the missing global square carrier.

```text
six-functor trace formalism is downstream
  -> prismatic / syntomic / p-adic comparison package
  -> Nygaard filtration + Frobenius + TC^-/TP comparison
  -> global square correspondence carrier
  -> End(S^2/Z).
```

Witness, lead-reran this cycle:
`prime_int_n1b_prismatic_syntomic_package_no_go` (PSP1-PSP7 ALL PASS) --
identical prismatic/syntomic profiles do not determine finite-field count
anchors; p-adic comparison data does not construct NS degree slots; finite
p-adic truncations do not pin the global over-`Z` degree character; p-adic
filtration/Frobenius data does not impose Frobenius/Rosati compatibility;
finite prismatic windows admit ghost summands; the same package is formable
on controls; and no square package over `Z` is built.

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_six_functor_trace_no_go` (SFT1-SFT7 ALL PASS) and
`prime_int_n1b_monoid_frobenius_shadow_no_go` (MFS1-MFS10 ALL PASS).

## 1. Purpose

Doc 229 says trace formalism is downstream of the square. A serious p-adic
repair is:

```text
use prismatic cohomology / syntomic cohomology / BMS comparison;
use Nygaard filtration and Frobenius as the integral carrier;
assemble TC^- and TP to get the square.
```

This is still not construction of `End(S^2/Z)`. Prismatic and syntomic
packages are local and p-complete. They are powerful comparison tools after
one has a geometric or categorical object whose p-adic realizations are being
compared. They do not by themselves construct the global over-`Z` square,
the all-prime plus archimedean assembly, `rep_NS`, fiber degree maps, proper
correspondence category, Frobenius graph, projection formula, or positive
Rosati relation.

This document rejects only the shortcut:

```text
a prismatic / syntomic / p-adic comparison package constructs the square
correspondence carrier required by End(S^2/Z).
```

It does not reject a future zeta-native square whose actual proper
correspondence category first constructs the global object and then admits
compatible p-adic/prismatic/syntomic realizations at each prime.

## 2. Lemma

```text
Lemma 230.1 (P-adic comparison packages are local downstream data).

For the finite-field q=7, Tr(F)=1 anchor and the q=5, Tr(F)=2 anchor, take
the same toy p-adic comparison profile:

    rank                  = 2,
    p-complete             = yes,
    Nygaard/Hodge weights  = (0,1),
    Frobenius              = present,
    syntomic fiber         = present,
    comparison maps        = present.

The profiles are identical, but the count windows differ:

    q=7: 7, 63, 364, 2331
    q=5: 4, 32, 148, 640.

Therefore the abstract prismatic/syntomic profile does not determine the
finite-field count anchor.

Nor does p-adic comparison data construct the NS degree slots. Keeping the
same prismatic profile and z-action while changing the formal triple from
(7,F,1) to (10,F,1) changes

    Delta . Gamma  from 7 to 10.

Finite p-adic truncation cannot pin the global over-Z degree character. At
p=3 and precision 3^2=9, degrees 7 and 16 agree modulo 9, but

    Delta . Gamma  changes from 7 to 16.

Nygaard/Hodge-Tate weights and p-adic Frobenius also do not impose the
complex/archimedean Rosati relation. For the off-circle integral
q-similitude control

    F = [[0,-2],[1,3]], q=2,

the same profile exists, but

    ||(F/sqrt(q))^T H (F/sqrt(q)) - H|| = 5.916.

Finite p-adic/prismatic windows remain unsafe. A 5-cycle ghost summand
preserves traces in powers 1,2,3,4 and changes count 5 by 5.

The same abstract p-adic comparison package is formable on arbitrary control
companion data with no Euler product, all-prime assembly, archimedean
component, rep_NS, square carrier, or positive Rosati.

Consequently a prismatic/syntomic/p-adic comparison package constructs no
global prism or over-Z square, all-prime assembly, archimedean component,
rep_NS, actual square, proper correspondence category, fiber-product
composition, carrier-native degree maps, carrier-native pairing, projection
formula, Frobenius graph, positive Rosati, DH/Epstein death, DD.4 weight>=1
datum, or End(S^2/Z).
```

Verdict label:

```text
N1B_PRISMATIC_SYNTOMIC_PACKAGE__P_COMPLETE_COMPARISON_NOT_GLOBAL_SQUARE__NO_GO.
```

## 3. Proof

`prime_int_n1b_prismatic_syntomic_package_no_go` verifies the seven gates.

PSP1 records profile non-determination. The q=7 and q=5 anchors have the same
p-adic/prismatic profile but different count windows.

PSP2 records the NS-degree-slot failure. With the same prismatic profile and
z-action, changing only the formal degree slot changes `Delta.Gamma` from `7`
to `10`.

PSP3 records p-adic degree ambiguity at finite precision. At `p=3`,
degrees `7` and `16` agree modulo `9`, but the diagonal/graph intersection
changes from `7` to `16`.

PSP4 records p-adic filtration versus Rosati separation. A positive form
exists on the off-circle q-similitude control, but the normalized Frobenius
metric compatibility defect is `5.916`. The missing datum is the global
carrier-native Rosati relation.

PSP5 records finite-window ghost survival. A 5-cycle ghost preserves the
first four traces and changes count 5 by `5`.

PSP6 records control formability. A control companion with the same abstract
prismatic profile has count window `8,112,1064` and metric defect `9.950`,
with no Euler/all-prime/archimedean/`rep_NS`/square/Rosati input.

PSP7 records the construction failure: no global prism or over-`Z` square,
all-prime assembly, archimedean component, `rep_NS`, actual square, proper
correspondence category, fiber-product composition, carrier-native degree
maps, carrier-native pairing, projection formula, Frobenius graph, positive
Rosati, control death, or DD.4 weight>=1 datum is constructed.

## 4. Impact on R1

```text
R1 after docs 138-230:
  NEWLY CLOSED THIS CYCLE:
    - prismatic cohomology as global square carrier, syntomic fiber as
      rep_NS construction, Nygaard filtration as degree-character
      construction, p-adic Frobenius as global Frobenius graph, finite
      p-adic comparison windows as carrier determination, and p-complete
      comparison packages as DH/Epstein carrier guards (doc 230).

  STILL ADMISSIBLE:
    - a carrier-native global square over Z whose proper correspondence
      category is constructed before taking p-adic realizations;
    - all-prime plus archimedean assembly constructed before prismatic or
      syntomic comparison is invoked;
    - a theorem excluding ghost p-adic summands from the actual carrier;
    - controls killed at carrier formation, not after p-completion.

  STILL OPEN:
    - construct rep_NS over Z with an actual square carrier, proper
      correspondence category or carrier-native proper dg enhancement,
      fiber-product composition, carrier-native degree maps, canonical
      pairing and projection formula, off-diagonal intersection form,
      preserved trace/count anchor, positive Rosati, DD.4 weight>=1 data, and
      square-side properness.
```

R1 remains open. This cycle closes the prismatic/syntomic shortcut:
p-complete comparison data is not construction of the global square carrier.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-PSP.1 prismatic package as square construction
  A proposal supplies prismatic, syntomic, TC^-, or TP comparison data and
  calls it the square. Kill it unless the global over-Z square carrier was
  already constructed carrier-natively.

KILL-PSP.2 syntomic fiber as rep_NS
  A proposal treats syntomic/prismatic fibers or Nygaard pieces as the NS
  triple. Kill it unless the degree slots, off-diagonal intersections, and
  projection formula are constructed.

KILL-PSP.3 p-adic Frobenius as global graph
  A proposal reads the global Frobenius graph from local p-adic Frobenius.
  Kill it unless all-prime plus archimedean assembly and graph composition
  are constructed by the carrier.

KILL-PSP.4 Nygaard/Hodge-Tate data as Rosati
  A proposal reads positive Rosati from Nygaard or Hodge-Tate filtration data.
  Kill it unless Frobenius/Rosati compatibility is constructed globally.

KILL-PSP.5 finite p-adic window
  A proposal verifies finitely many p-adic comparison or trace identities.
  Kill it unless ghost p-adic summands are excluded carrier-natively.

KILL-PSP.6 control survival
  A proposal's p-adic comparison package can be formed on arbitrary control
  companion data. Kill it unless controls die at carrier formation.
```
