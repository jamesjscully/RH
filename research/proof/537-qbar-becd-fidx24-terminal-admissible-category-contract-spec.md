# 537 - Qbar_BECD exact-24 terminal source-square admissible-category contract

Status: construction-spec refinement anchor, 2026-06-28.
Four-hundredth cycle of the doc-137 construction arc. This is not a no-go
theorem, not an RH proof, and not added to the no-go bank.

Doc 536 required the dependency-closed exact-24 source square to be terminal.
The remaining cheap escape is vacuity: terminality can be manufactured if the
category of admissible source squares is a singleton, is defined by the
terminal object itself, admits graph-first probes, or is retuned after the
fact.

This document requires a named admissible-category certificate:

```text
AdmCat_TermUP_DepClosure_FinIdx24Budget_LimCut_NCoup_med_UP_Eq_NCoup_med_UP_Eq_id_id_source_square.
```

The category is charged to the existing finite-limit coherence cell. It is
preterminally specified by source-before-points order, the seven source
constraints, the finite-limit equalizer, directed DD.4 and graph-later
handoffs, exact-24 budget, dependency closure, and source-fiber inhabitance.
It is not defined by the terminal object.

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_fidx24_terminal_admcat_contract`
(CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD10 ALL PASS).
Adjacent Qbar_BECD witnesses plus the DD.4 SCC interface:
230/230 exit 0. Frontier-map check with current witness:
current_doc=537, atoms=35, edges=54.

## 1. Purpose

The cheap repair after doc 536 is:

```text
the terminal object exists because the admissible category was made too small
or defined after seeing the terminal object.
```

That is not construction evidence. The admissible category must be wide
enough to contain independent source-side probes and narrow enough to exclude
control/DH/Epstein point formability, graph-first probes, H^1 quotient
collapse, and posthoc universal-arrow probes.

The live object narrows from:

```text
terminal dependency-closed exact-24-budgeted inhabited DD.4-image-handoff
graph-later-realization context-separated finite-limit-subrepresented
represented coupled formation-coherent mediator
```

to:

```text
admissible-category terminal dependency-closed exact-24-budgeted inhabited
DD.4-image-handoff graph-later-realization context-separated finite-limit-
subrepresented represented coupled formation-coherent mediator.
```

## 2. Lemma

```text
Lemma 537.1 (terminality must be nonvacuous).

The current frontier is admissible only if the category of admissible
budgeted dependency-closed source squares is specified before terminality by:

    source_before_points,
    the seven source constraints,
    finite_limit_equalizer,
    directed DD.4 image handoff,
    directed graph-later-realization handoff,
    exact_24_budget,
    dependency_closure,
    and source_fiber_inhabitance.

The category must contain independent probe classes for mediator cones,
constraint forks, DD.4 handoff, graph-later realization, inhabitance, and
budget closure. Membership may not be defined by the terminal object.

Thus singleton admissible categories, retuned categories, terminal-defined
categories, posthoc probe classes, graph-first probe categories, control/DH/
Epstein probe admission, H^1 quotient probe categories, missing admissible-
category certificates, expanded finite index, and one-more-layer towers do
not construct the current frontier.
```

## 3. Consequence

Doc 537 does not solve R1 and does not prove RH. It makes the categorical
approach honest: the terminal source square is meaningful only in a fixed,
nonvacuous, probe-full source category.

The next negative route is now specific. Kill the branch by proving that any
such admissible category is necessarily singleton, terminal-defined,
graph-first, control-admitting, H^1-quotienting, or finite-index expanding.

## 4. Verification Gates

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD1
    Requires the doc-537 admissible-category layer to be embedded in the
    current map.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD2
    Rejects singleton admissible categories.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD3
    Rejects terminal-defined or retuned categories.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD4
    Rejects posthoc probe classes.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD5
    Rejects graph-first probe categories.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD6
    Rejects control/DH/Epstein probe admission.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD7
    Rejects H^1 quotient probe categories.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD8
    Rejects missing admissible-category certificates.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD9
    Rejects expanded finite-index admissible categories.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD10
    Confirms that only the nonvacuous preterminal admissible category passes.
```

## 5. Fail-Closed Note

The witness reads the current `frontier-map.yaml`. If the admissible category
is absent, singleton, terminal-defined, posthoc, graph-first, control-
admitting, H^1-quotienting, or finite-index expanding, the refinement fails
before terminality can count as construction evidence.
