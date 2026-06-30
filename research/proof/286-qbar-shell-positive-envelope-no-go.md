# 286 - Qbar shell positive envelope is not the square carrier

Status: no-go + Qbar-shell-positive-envelope deletion, 2026-06-21.
One-hundred-forty-ninth cycle of the doc-137 construction arc. Doc 285
killed freely adjoining formal fiber-product objects and projection cells to
the positive `U+End` envelope. This document tests the next stronger repair:

```text
add a named Qbar shell with p1,p2,dQ,Corr^prop, boundary localization,
Rosati, projection, and control-death labels, but do not construct the
carrier geometry.
```

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_shell_positive_envelope_no_go` (QBS1-QBS8 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_fiber_product_saturated_positive_envelope_no_go`,
`prime_int_n1b_carrier_first_categorical_square_contract`,
`prime_int_n1b_dd4_scc_interface`, and
`prime_int_n1b_square_carrier_contract`.

## 1. Purpose

Doc 276 made the carrier-first categorical contract explicit. Docs 284 and
285 then killed forcing projection by relation repair and by formal
fiber-product cells. The remaining shortcut is more subtle:

```text
declare all carrier-first names at once.
```

This can pass a naive checklist. The package can say `Qbar`, `p1,p2`, `dQ`,
`Corr^prop`, fiber products, localization, Rosati, projection formula, and
control death. But unless those names are represented by an actual
compactified square and proper correspondence geometry, they import the
contract instead of constructing it.

This document rejects only the shell. It does not reject a real `Qbar`.

## 2. Lemma

```text
Lemma 286.1 (Qbar names are not Qbar construction).

Let U_1=1+z F_2[[z]], phi(z)=z/(1+z), and c=(1+z)^-1. In U_1, for
truncations L=6,8,10,12:

    H^1(<phi>; U_1) = Z/2,
    [c] != 0,
    res_1(c)=1.

For the q=7, Tr(F)=1 finite-field anchor, the positive `U+End` data before
Qbar-shell naming has:

    Delta.Gamma_1 = 7,
    Gamma_1.Gamma_2 = 76,
    Gamma_1 o Gamma_2 = Gamma_3,
    F^T E F = qE,
    primitive Hodge/Rosati sign < 0.

A shell with the declared generators

    Qbar, Q, dQ, p1,p2, Corr^prop, fiber products, integral cycles,
    proper pushforward, intersection pairing, Frobenius graph,
    localization sequence, boundary self-duality, duality functor,
    primitive Hodge index, and control-death guard

passes a name-level carrier-first dependency graph: it names all eleven SCC
slots. But it represents zero slots unless the generators are actual
geometric objects and maps.

The shell can declare projection formula, but the componentwise positive
`U+End` semantics still has projection defect 27. No geometric proof from
proper pullback and pushforward is supplied.

The shell can declare a boundary localization killing DD.4, but the base
class `[c]` remains non-boundary with `res_1(c)=1`. The same endpoint DD.4
split works with labels `qbar_shell_boundary`, `declared_localization`, and
`control_shell`, so the killing is declaration or free splitting, not a
carrier boundary map.

The shell can name `p1,p2`, but labels do not force carrier-native endpoint
maps. In the finite-field SCC anchor, `(10,F,1)` and `(7,F,4)` have the same
total degree 11 and the same diagonal pairing 10, while left and right
endpoint probes differ.

Positive controls admit the same Qbar shell and name-level SCC slots while
retaining semantic projection defect 11. Therefore the shell supplies no
control death.

Consequently Qbar-shell positive-envelope data constructs no actual `Qbar`,
no actual `p1,p2`, no proper pullbacks, no carrier-produced integral
`rep_NS`, no projection formula from geometry, no carrier boundary
localization, no carrier Rosati, and no control death.
```

Verdict label:

```text
N1B_QBAR_SHELL_POSITIVE_ENVELOPE__NAME_LEVEL_CONTRACT_NOT_CARRIER__NO_GO.
```

## 3. Proof

`prime_int_n1b_qbar_shell_positive_envelope_no_go` verifies eight gates.

QBS1 recomputes the base DD.4 obstruction:

```text
L6:  |B|=2^3, |Z1|=2^4, |H1|=2
L8:  |B|=2^4, |Z1|=2^5, |H1|=2
L10: |B|=2^5, |Z1|=2^6, |H1|=2
L12: |B|=2^6, |Z1|=2^7, |H1|=2
```

QBS2 checks that the positive finite-field anchor is intact before shelling:
diagonal count, off-diagonal pairing, graph law, q-similitude, and negative
primitive sign all hold.

QBS3 checks checklist failure: a Qbar shell names all eleven carrier-first
slots, while representing none of them.

QBS4 checks projection by name: the shell declares projection, but the
semantic defect remains 27 and no geometric proof is supplied.

QBS5 checks DD.4 by name: `[c]` remains non-boundary in the base coefficient
system, and the endpoint split is label-independent.

QBS6 checks endpoint-map ambiguity: shell labels `p1,p2` do not recover two
carrier-native endpoint maps from total degree or diagonal pairings.

QBS7 checks positive control formability: controls admit the same name-level
shell and still have semantic projection defect.

QBS8 applies the construction-grade carrier contract: names are not actual
`Qbar`, actual `p1,p2`, proper pullbacks, geometric projection formula,
carrier boundary, carrier Rosati, or control death.

## 4. Impact on R1

```text
R1 after docs 138-286:
  NEWLY CLOSED THIS CYCLE:
    - Qbar by name;
    - p1,p2 by label;
    - dQ/localization by declaration;
    - Corr^prop/fiber products/projection formula by shell syntax;
    - control death as a named guard rather than a formation failure.

  POSITIVE INFORMATION RETAINED:
    - the CFC/SCC slot list is still the right dependency graph;
    - the proof process must distinguish name-level satisfaction from
      represented construction;
    - any surviving route must show the slots are forced by one object, not
      listed as its desired output.

  STILL ADMISSIBLE:
    - a compactified zeta square whose maps, boundary, proper pullbacks,
      integral pushforwards, projection formula, Rosati, and control death
      are actual theorems of the carrier.

  STILL OPEN:
    - construct the carrier geometry rather than a shell satisfying the
      carrier checklist.
```

## 5. Kill conditions

```text
KILL-QBS.1 Qbar by name
  Kill any proposal that names Qbar without constructing the object and its
  structural maps.

KILL-QBS.2 carrier-first checklist by labels
  Kill a candidate that satisfies CFC/SCC by listing slot names rather than
  representing the slots.

KILL-QBS.3 projection theorem by shell
  Kill declared projection formulas while the semantic projection defect
  remains or no proper push-pull proof is given.

KILL-QBS.4 boundary localization by declaration
  Kill DD.4 boundary claims where `[c]` dies only in a declared localization
  or free split unrelated to carrier geometry.

KILL-QBS.5 p1,p2 by endpoint labels
  Kill endpoint maps that are labels or decoders rather than carrier-native
  pushforwards.

KILL-QBS.6 control death by named guard
  Kill control-death guards unless controls fail to instantiate the carrier
  before positivity, quotienting, projection cells, or trace filters.
```
