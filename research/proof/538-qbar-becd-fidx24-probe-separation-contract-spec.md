# 538 - Qbar_BECD exact-24 admissible source-square probe-separation contract

Status: construction-spec refinement anchor, 2026-06-28.
Four-hundred-first cycle of the doc-137 construction arc. This is not a
no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 537 required terminality to live in a nonvacuous admissible category. The
remaining cheap escape is probe blindness: a category can have multiple probes
while all probes fail to distinguish the source constraints, DD.4 handoff,
graph-later handoff, inhabitance, or budget closure.

This document requires a named probe-separation certificate:

```text
ProbeSep_AdmCat_TermUP_DepClosure_FinIdx24Budget_LimCut_NCoup_med_UP_Eq_NCoup_med_UP_Eq_id_id_source_square.
```

The certificate is charged to the existing finite-limit coherence cell. It
uses no extra source facet, no extra coherence cell, no control/DH/Epstein
probe, no finite sample, and no basis-dependent probe.

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_fidx24_probe_separation_contract`
(CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD10 ALL PASS).
Adjacent Qbar_BECD witnesses plus the DD.4 SCC interface: 231/231 exit 0.
Frontier-map check with current witness: current_doc=538, atoms=36, edges=60.

## 1. Purpose

The cheap repair after doc 537 is:

```text
the admissible category is nonvacuous, but its probes do not see the data
that makes the terminal source square the missing object.
```

That would reduce terminality to formal category theory with no construction
content. The probe family must be conservative on the source square: the
probes must separate the seven source constraints, the DD.4 handoff, the
graph-later handoff, the inhabitance certificate, and the exact-24 budget /
dependency / terminal / category data.

The live object narrows from:

```text
admissible-category terminal dependency-closed exact-24-budgeted inhabited
DD.4-image-handoff graph-later-realization context-separated finite-limit-
subrepresented represented coupled formation-coherent mediator
```

to:

```text
probe-separated admissible-category terminal dependency-closed exact-24-
budgeted inhabited DD.4-image-handoff graph-later-realization context-
separated finite-limit-subrepresented represented coupled formation-coherent
mediator.
```

## 2. Lemma

```text
Lemma 538.1 (admissible probes must be conservative).

The admissible source-square category is accepted only if its six probe
classes remain distinct and jointly separate:

    mediator cone data,
    all seven source constraints,
    DD.4 image handoff data,
    graph-later-realization data,
    finite-limit inhabitance data,
    and exact-24 budget/dependency/terminal/category data.

Thus merged probe classes, source-constraint-blind probes, DD.4-handoff-
blind probes, graph-handoff-blind probes, inhabitance-blind probes, budget-
blind probes, nonconservative probe families, control/DH/Epstein probe
replacements, finite-sample probes, basis-dependent probes, and missing
probe-separation certificates do not construct the current frontier.
```

## 3. Consequence

Doc 538 does not solve R1 and does not prove RH. It prevents the categorical
frontier from becoming formally terminal but observationally empty.

The next negative route is now specific: prove that any admissible probe
family separating the source constraints and both handoffs must collapse to
control/DH/Epstein probes, finite samples, basis-dependent rows, or extra
finite-index structure.

## 4. Verification Gates

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD1
    Requires the doc-538 probe-separation layer to be embedded in the current
    map.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD2
    Rejects merged probe classes.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD3
    Rejects constraint-blind probes.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD4
    Rejects DD.4-handoff-blind probes.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD5
    Rejects graph-handoff-blind probes.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD6
    Rejects inhabitance or budget-blind probes.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD7
    Rejects nonconservative probe families.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD8
    Rejects control/sample/basis probe replacements.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD9
    Rejects missing probe-separation certificates.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD10
    Confirms that only conservative source-probe separation passes.
```

## 5. Fail-Closed Note

The witness reads the current `frontier-map.yaml`. If the admissible probes
merge, go blind to any source constraint or handoff, stop detecting
inhabitance or budget closure, use control/DH/Epstein replacements, use finite
samples or basis rows, or omit the separation certificate, the refinement
fails before terminality can count as construction evidence.
