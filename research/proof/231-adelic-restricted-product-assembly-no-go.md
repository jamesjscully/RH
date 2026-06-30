# 231 - Adelic restricted products do not construct the square

Status: no-go + adelic/restricted-product/all-place-assembly boundary,
2026-06-20. Ninety-fourth cycle of the doc-137 construction arc. Doc 230
killed prismatic/syntomic/p-adic comparison packages as square construction.
This document tests the next repair: assemble the local p-adic/prismatic
packages over all primes by a restricted product, add the archimedean place,
and promote that all-place package to the missing global square carrier.

```text
local p-adic/prismatic packages at every prime
  -> restricted product / product formula / archimedean component
  -> global square correspondence carrier
  -> End(S^2/Z).
```

Witness, lead-reran this cycle:
`prime_int_n1b_adelic_restricted_product_assembly_no_go` (ARP1-ARP7 ALL
PASS) -- identical restricted-product profiles do not determine finite-field
count anchors; restricted-product data does not construct NS degree slots;
finite all-prime windows do not pin the global over-`Z` degree character;
product-formula/determinant data does not impose individual radius split or
Rosati; finite adelic windows admit ghost summands; the same package is
formable on controls; and no square package over `Z` is built.

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_prismatic_syntomic_package_no_go` (PSP1-PSP7 ALL PASS) and
`prime_int_n1b_radius_descent_assembly_no_go` (RDA1-RDA6 ALL PASS).

## 1. Purpose

Doc 230 says p-adic/prismatic comparison data is local downstream data. The
obvious repair is to remove the local defect:

```text
take every p-adic/prismatic local package;
impose a restricted-product condition;
add the archimedean place;
use the product formula as the global glue.
```

This is still not construction of `End(S^2/Z)`. Restricted products,
idele-style bookkeeping, and product-formula compatibility can organize local
realizations after a global object exists. They do not by themselves
construct the global over-`Z` square, `rep_NS`, carrier-native degree maps,
proper correspondence category, fiber-product composition, Frobenius graph,
projection formula, or positive Rosati relation.

This document rejects only the shortcut:

```text
an all-place restricted product of local comparison packages constructs the
square correspondence carrier required by End(S^2/Z).
```

It does not reject a future zeta-native square whose actual proper
correspondence category first constructs the global carrier and whose local
and archimedean realizations then assemble as a restricted product.

## 2. Lemma

```text
Lemma 231.1 (Restricted products are not global square carriers).

For the finite-field q=7, Tr(F)=1 anchor and the q=5, Tr(F)=2 anchor, take
the same toy all-place profile:

    displayed local packages = 3,
    restricted product        = yes,
    product formula           = yes,
    archimedean component     = yes,
    local trace factors       = yes,
    comparison maps           = yes.

The profiles are identical, but the count windows differ:

    q=7: 7, 63, 364, 2331
    q=5: 4, 32, 148, 640.

Therefore the abstract restricted-product profile does not determine the
finite-field count anchor.

Nor does restricted-product data construct the NS degree slots. Keeping the
same all-place profile and z-action while changing the formal triple from
(7,F,1) to (10,F,1) changes

    Delta . Gamma  from 7 to 10.

Finite all-prime windows cannot pin the global over-Z degree character.
Degrees 7 and 37 agree at the displayed primes 2, 3, and 5, hence modulo
30, but

    Delta . Gamma  changes from 7 to 37.

Product-formula and determinant/pairing data also do not force the individual
radius split or Rosati compatibility. With q=9, the moduli

    e^0.4 * 3, e^-0.4 * 3, e^-0.4 * 3, e^0.4 * 3

have pair-products 9 and determinant 81, but they are not all equal to 3.
Separately, the off-circle integral q-similitude control

    F = [[0,-2],[1,3]], q=2

has normalized metric defect 5.916 for the positive identity metric.

Finite adelic windows remain unsafe. A 5-cycle ghost summand preserves
traces in powers 1,2,3,4 and changes count 5 by 5.

The same abstract restricted-product package is formable on arbitrary control
companion data with no carrier-produced local factors, archimedean square
component, rep_NS, square carrier, or positive Rosati.

Consequently an adelic restricted-product assembly constructs no
restricted-product square, rational diagonal quotient, archimedean-compatible
carrier, rep_NS, actual square, proper correspondence category,
fiber-product composition, carrier-native degree maps, carrier-native
pairing, projection formula, Frobenius graph, positive Rosati, DH/Epstein
death, DD.4 weight>=1 datum, or End(S^2/Z).
```

Verdict label:

```text
N1B_ADELIC_RESTRICTED_PRODUCT_ASSEMBLY__LOCAL_PRODUCTS_NOT_GLOBAL_SQUARE__NO_GO.
```

## 3. Proof

`prime_int_n1b_adelic_restricted_product_assembly_no_go` verifies the seven
gates.

ARP1 records profile non-determination. The q=7 and q=5 anchors have the same
restricted-product profile but different count windows.

ARP2 records the NS-degree-slot failure. With the same all-place profile and
z-action, changing only the formal degree slot changes `Delta.Gamma` from
`7` to `10`.

ARP3 records finite local-window degree ambiguity. Degrees `7` and `37`
agree at primes `2,3,5`, hence modulo `30`, but the diagonal/graph
intersection changes from `7` to `37`.

ARP4 records product formula versus Rosati separation. Balanced local radius
redistribution preserves pair-products and determinant while breaking the
individual even split, and an off-circle q-similitude still has positive
metric defect `5.916`. The missing datum is global carrier-native Rosati,
not another product identity.

ARP5 records finite-window ghost survival. A 5-cycle ghost preserves the
first four traces and changes count 5 by `5`.

ARP6 records control formability. A control companion with the same abstract
restricted-product profile has count window `8,112,1064` and metric defect
`9.950`, with no carrier-produced local factors, archimedean square
component, `rep_NS`, square, or Rosati input.

ARP7 records the construction failure: no restricted-product square, rational
diagonal quotient, archimedean-compatible carrier, `rep_NS`, actual square,
proper correspondence category, fiber-product composition, carrier-native
degree maps, carrier-native pairing, projection formula, Frobenius graph,
positive Rosati, control death, or DD.4 weight>=1 datum is constructed.

## 4. Impact on R1

```text
R1 after docs 138-231:
  NEWLY CLOSED THIS CYCLE:
    - adelic restricted product as global square carrier, product formula as
      rep_NS construction, finite all-prime window as degree-character
      construction, archimedean appendage as Rosati, local-product trace
      factors as count determination, and restricted-product packages as
      DH/Epstein carrier guards (doc 231).

  STILL ADMISSIBLE:
    - a carrier-native global square over Z whose proper correspondence
      category is constructed before local completions are assembled;
    - all-prime plus archimedean compatibility as a theorem downstream of an
      actual square carrier;
    - a theorem excluding ghost local factors from the actual carrier;
    - controls killed at carrier formation, not after local/product assembly.

  STILL OPEN:
    - construct rep_NS over Z with an actual square carrier, proper
      correspondence category or carrier-native proper dg enhancement,
      fiber-product composition, carrier-native degree maps, canonical
      pairing and projection formula, off-diagonal intersection form,
      preserved trace/count anchor, positive Rosati, DD.4 weight>=1 data, and
      square-side properness.
```

R1 remains open. This cycle closes the all-place restricted-product shortcut:
local products plus the archimedean place are not construction of the global
square carrier.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-ARP.1 restricted product as square construction
  A proposal supplies a restricted product of local comparison packages and
  calls it the square. Kill it unless the global over-Z square carrier was
  already constructed carrier-natively.

KILL-ARP.2 product formula as rep_NS
  A proposal treats product-formula or idele-style compatibility as the NS
  triple. Kill it unless the degree slots, off-diagonal intersections, and
  projection formula are constructed.

KILL-ARP.3 finite all-prime window
  A proposal verifies finitely many local factors or congruences and reads a
  global degree character from them. Kill it unless the over-Z degree maps
  are constructed by the carrier.

KILL-ARP.4 archimedean appendage as Rosati
  A proposal adds an archimedean component to local p-adic packages and reads
  positive Rosati from the product. Kill it unless Frobenius/Rosati
  compatibility is constructed globally.

KILL-ARP.5 local ghost survival
  A proposal verifies finitely many local trace or comparison identities.
  Kill it unless ghost local factors are excluded carrier-natively.

KILL-ARP.6 control survival
  A proposal's restricted-product package can be formed on arbitrary control
  companion data. Kill it unless controls die at carrier formation.
```
