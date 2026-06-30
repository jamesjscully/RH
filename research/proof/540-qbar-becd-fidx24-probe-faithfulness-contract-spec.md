# 540 - Qbar_BECD exact-24 admissible source-square probe-faithfulness contract

Status: construction-spec refinement anchor, 2026-06-28.
Four-hundred-third cycle of the doc-137 construction arc. This is not a
no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 539 required the separated probes to be natural source-defined probe
functors. The remaining cheap escape is faithful collapse: the functors can be
natural because they quotient the admissible morphism category, mask
automorphisms, identify isomorphic-but-distinct source-square morphisms, or
forget identities, composition, terminal arrows, and handoff/dependency
morphism classes.

This document requires a named probe-faithfulness certificate:

```text
FaithProbe_NatProbe_ProbeSep_AdmCat_TermUP_DepClosure_FinIdx24Budget_LimCut_NCoup_med_UP_Eq_NCoup_med_UP_Eq_id_id_source_square.
```

The certificate is charged to the existing finite-limit coherence cell. It
uses no new source facet, no new coherence cell, no morphism quotient, no
automorphism mask, no point/graph morphism shadow, no finite morphism sample,
and no basis-row morphism test.

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_fidx24_probe_faithfulness_contract`
(CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPFAITHPROBENATPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPFAITHPROBENATPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD10 ALL PASS).
Adjacent Qbar_BECD witnesses plus the DD.4 SCC interface: 233/233 exit 0.
Frontier-map check with current witness: current_doc=540, atoms=38, edges=76.

## 1. Purpose

The cheap repair after doc 539 is:

```text
the probes are natural, but their functors identify the source-square
morphisms that carry the actual construction content.
```

That would make naturality commute by erasing the difference between source
morphisms. The probe family must be jointly faithful: the product of the six
probe functors must reflect distinct admissible morphisms, identity arrows,
composition, the terminal arrow, dependency closure, DD.4 image handoff,
graph-later realization, finite-limit inhabitance, and exact-24 budget
morphisms.

The live object narrows from:

```text
probe-natural probe-separated admissible-category terminal dependency-closed
exact-24-budgeted inhabited DD.4-image-handoff graph-later-realization
context-separated finite-limit-subrepresented represented coupled
formation-coherent mediator
```

to:

```text
probe-faithful probe-natural probe-separated admissible-category terminal
dependency-closed exact-24-budgeted inhabited DD.4-image-handoff
graph-later-realization context-separated finite-limit-subrepresented
represented coupled formation-coherent mediator.
```

## 2. Lemma

```text
Lemma 540.1 (natural probes must be jointly faithful on morphisms).

The admissible source-square category is accepted only if the six natural
probe functors of doc 539 are jointly faithful on the morphism skeleton:

    identities,
    composition,
    the terminal arrow,
    dependency-closure morphisms,
    DD.4 image-handoff morphisms,
    graph-later-realization morphisms,
    finite-limit inhabitance morphisms,
    and exact-24 budget-closure morphisms.

Thus nonfaithful probe families, morphism quotients, automorphism masks,
isomorphism collapses, identity-blind probes, composition-blind probes,
terminal-arrow-blind probes, dependency- or handoff-morphism-blind probes,
point/graph morphism shadows, finite morphism samples, basis-row morphism
tests, and missing probe-faithfulness certificates do not construct the
current frontier.
```

## 3. Consequence

Doc 540 does not solve R1 and does not prove RH. It prevents the natural
probe layer from becoming a quotient diagram where every square commutes
after the morphisms that matter have been identified away.

The next negative route is now sharper: prove that any source-defined natural
separating probe family necessarily loses joint faithfulness on admissible
source-square morphisms, or that joint faithfulness forces an automorphism
mask, an isomorphism quotient, point/graph morphism semantics, finite samples,
basis rows, or extra finite-index structure.

## 4. Verification Gates

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPFAITHPROBENATPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD1
    Requires the doc-540 probe-faithfulness layer to be embedded in the
    current map.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPFAITHPROBENATPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD2
    Rejects nonfaithful probe families.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPFAITHPROBENATPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD3
    Rejects morphism quotients and automorphism masks.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPFAITHPROBENATPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD4
    Rejects isomorphism collapses.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPFAITHPROBENATPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD5
    Rejects identity- or composition-blind probes.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPFAITHPROBENATPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD6
    Rejects terminal-arrow-blind probes.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPFAITHPROBENATPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD7
    Rejects dependency- or handoff-morphism-blind probes.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPFAITHPROBENATPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD8
    Rejects point/graph morphism shadows, finite morphism samples, or
    basis-row morphism probes.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPFAITHPROBENATPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD9
    Rejects missing probe-faithfulness certificates.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPFAITHPROBENATPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD10
    Confirms that only jointly faithful natural source-probe functors pass.
```

## 5. Fail-Closed Note

The witness reads the current `frontier-map.yaml`. If the natural probes
identify distinct source morphisms, quotient by automorphisms or isomorphisms,
ignore identity/composition/terminal/dependency/handoff morphisms, move to
point or graph morphism shadows, use finite morphism samples, use basis-row
morphism tests, or omit the faithfulness certificate, the refinement fails
before probe naturality can count as construction evidence.
