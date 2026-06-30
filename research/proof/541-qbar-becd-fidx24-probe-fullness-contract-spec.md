# 541 - Qbar_BECD exact-24 admissible source-square probe-fullness contract

Status: construction-spec refinement anchor, 2026-06-28.
Four-hundred-fourth cycle of the doc-137 construction arc. This is not a
no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 540 required the natural probe functors to be jointly faithful on the
source-square morphism skeleton. The remaining cheap escape is non-fullness:
there may be compatible probe-level morphism tuples that do not lift to an
actual admissible source-square morphism. Faithfulness prevents collapse, but
without fullness the probe diagram can still contain extra observer-side maps.

This document requires a named probe-fullness certificate:

```text
FullProbe_FaithProbe_NatProbe_ProbeSep_AdmCat_TermUP_DepClosure_FinIdx24Budget_LimCut_NCoup_med_UP_Eq_NCoup_med_UP_Eq_id_id_source_square.
```

The certificate is charged to the existing finite-limit coherence cell. It
uses no new source facet, no new coherence cell, no declared fullness axiom,
no arbitrary lift selector, no posthoc lift, no point/graph fullness, no
finite tuple sample, and no basis-row fullness test.

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_fidx24_probe_fullness_contract`
(CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPFULLPROBEFAITHPROBENATPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPFULLPROBEFAITHPROBENATPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD10 ALL PASS).
Adjacent Qbar_BECD witnesses plus the DD.4 SCC interface: 234/234 exit 0.
Frontier-map check with current witness: current_doc=541, atoms=39, edges=84.

## 1. Purpose

The cheap repair after doc 540 is:

```text
the probes are faithful on source morphisms, but their compatible probe-level
maps do not all come from source-square morphisms.
```

That would keep the construction outside the source square: the probes would
observe a larger morphism category than the one constructed. The product of
the six probe functors must be full on the live morphism skeleton, so every
compatible tuple of probe morphisms lifts to a source morphism, and doc 540
faithfulness makes that lift unique.

The live object narrows from:

```text
probe-faithful probe-natural probe-separated admissible-category terminal
dependency-closed exact-24-budgeted inhabited DD.4-image-handoff
graph-later-realization context-separated finite-limit-subrepresented
represented coupled formation-coherent mediator
```

to:

```text
probe-full probe-faithful probe-natural probe-separated admissible-category
terminal dependency-closed exact-24-budgeted inhabited DD.4-image-handoff
graph-later-realization context-separated finite-limit-subrepresented
represented coupled formation-coherent mediator.
```

## 2. Lemma

```text
Lemma 541.1 (natural faithful probes must be full on live morphisms).

The admissible source-square category is accepted only if every compatible
tuple of morphisms in the six probe images lifts to a source-square morphism
for the live classes:

    identities,
    composition,
    the terminal arrow,
    dependency-closure morphisms,
    DD.4 image-handoff morphisms,
    graph-later-realization morphisms,
    finite-limit inhabitance morphisms,
    and exact-24 budget-closure morphisms.

Thus non-full probe families, extra probe-image morphisms, compatible probe
tuples without source lifts, fullness by declaration, arbitrary or nonunique
lift selectors, posthoc or retuned fullness lifts, lax fullness, point/graph
fullness, finite tuple samples, basis-row fullness tests, and missing
probe-fullness certificates do not construct the current frontier.
```

## 3. Consequence

Doc 541 does not solve R1 and does not prove RH. It prevents the probe layer
from being a faithful embedding whose image is too small or whose ambient
probe category contains morphisms not constructed by the source square.

The next negative route is now sharper: prove that any jointly faithful
natural separated probe family is not full on compatible probe morphism
tuples, or that fullness requires declared/external lift selection, posthoc
retuning, point/graph semantics, finite tuple samples, basis rows, or extra
finite-index structure.

## 4. Verification Gates

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPFULLPROBEFAITHPROBENATPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD1
    Requires the doc-541 probe-fullness layer to be embedded in the current
    map.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPFULLPROBEFAITHPROBENATPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD2
    Rejects non-full probe families.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPFULLPROBEFAITHPROBENATPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD3
    Rejects extra probe-image morphisms.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPFULLPROBEFAITHPROBENATPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD4
    Rejects fullness by declaration or arbitrary lift selectors.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPFULLPROBEFAITHPROBENATPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD5
    Rejects nonunique lifts.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPFULLPROBEFAITHPROBENATPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD6
    Rejects posthoc or retuned fullness lifts.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPFULLPROBEFAITHPROBENATPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD7
    Rejects lax fullness.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPFULLPROBEFAITHPROBENATPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD8
    Rejects point/graph fullness, finite tuple samples, or basis-row
    fullness.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPFULLPROBEFAITHPROBENATPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD9
    Rejects missing probe-fullness certificates.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPFULLPROBEFAITHPROBENATPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD10
    Confirms that only full faithful natural source-probe functors pass.
```

## 5. Fail-Closed Note

The witness reads the current `frontier-map.yaml`. If a compatible probe
morphism tuple has no source lift, if the probe image contains extra
morphisms, if the lift is selected by declaration, is arbitrary, nonunique,
posthoc, retuned, lax, point/graph-side, finite-sampled, basis-row-dependent,
or if the fullness certificate is missing, the refinement fails before probe
faithfulness can count as construction evidence.
