# 483 - Qbar_BECD categorical closure coherent source-presentation eta-factorization contract

Status: construction-spec refinement anchor, 2026-06-23.
Three-hundred-forty-sixth cycle of the doc-137 construction arc. This is not
a no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 482 left the categorical closure branch live only if the doc-481 finite
coherent source-presentation totalizer is realized by an internal source
finite limit:

```text
    SrcCat_BCCube_Qbar_BECD,
    Prod_CohSrcPres_BCCube_Qbar_BECD_facets_cells,
    alpha_CohSrcPres_BCCube_Qbar_BECD_constraints,
    beta_CohSrcPres_BCCube_Qbar_BECD_constraints,
    Eq_CohSrcPres_BCCube_Qbar_BECD,
    incl_Eq_CohSrcPres_to_Tot_CohSrcPres_BCCube_Qbar_BECD,
    cmp_Eq_CohSrcPres_to_Tot_CohSrcPres_BCCube_Qbar_BECD.
```

This document fixes the next edge. An internal equalizer object is still not
the missing object if the existing source universal arrow does not factor
through it. Object-only equalizers, empty equalizers, product-only
factorizations, chosen sections, posthoc point maps, or graph-side sections
can name the right finite-limit object without constructing the sourced
presentation. The source arrow must factor to the product, equalize the
parallel constraints, lift through the equalizer, and compare isomorphically
to the doc-481 totalizer arrow:

```text
    eta_BCCube_Qbar_BECD_source,
    fact_eta_BCCube_to_Prod_CohSrcPres_BCCube_Qbar_BECD,
    lift_eta_BCCube_to_Eq_CohSrcPres_BCCube_Qbar_BECD,
    cmp_lift_eta_BCCube_to_eta_CohSrcPres_BCCube_Qbar_BECD.
```

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_coherent_source_presentation_eta_factorization_contract`
(CATCOHSRCPRESETAQBARBECD1-CATCOHSRCPRESETAQBARBECD10 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
from doc 482 through the DD.4 SCC interface (176/176 exit 0).

## 1. Purpose

After doc 482, the cheap repair is:

```text
construct the internal product/equalizer object and then choose a section or
point of it after the fact.
```

That still does not construct the missing object. The existing source
universal arrow has to land in the finite-limit object. It must first factor
through the product projections to the seven facets and seventeen coherence
cells, then satisfy the alpha/beta constraints, then lift through the
equalizer monic, and finally compare to the doc-481 totalizer arrow. Without
this factorization, the equalizer can be correct as an object while remaining
empty, unsourced, or graph-side.

The live branch narrows from "internal finite-limit realization" to:

```text
construct fact_eta_BCCube_to_Prod_CohSrcPres_BCCube_Qbar_BECD;
prove eta_BCCube_Qbar_BECD_source generates all twenty-four projections;
prove alpha_CohSrcPres_BCCube_Qbar_BECD_constraints and
beta_CohSrcPres_BCCube_Qbar_BECD_constraints agree on that factorization;
construct lift_eta_BCCube_to_Eq_CohSrcPres_BCCube_Qbar_BECD;
prove the lift is through incl_Eq_CohSrcPres_to_Tot_CohSrcPres_BCCube_Qbar_BECD;
construct cmp_lift_eta_BCCube_to_eta_CohSrcPres_BCCube_Qbar_BECD;
prove that comparison is an isomorphism; and
prove coefficient/signed-support preservation and source-before-points order.
```

## 2. Lemma

```text
Lemma 483.1 (the internal finite limit must be sourced by eta).

The original DD.4 class remains:

    c=(1+z)^-1,
    H^1(<phi>; U_1)=Z/2,
    [c] != 0,
    res_1(c)=1,

in truncations L=6,8,10,12.

The accepted eta-factorization data are:

    eta_BCCube_Qbar_BECD_source,
    Prod_CohSrcPres_BCCube_Qbar_BECD_facets_cells,
    Eq_CohSrcPres_BCCube_Qbar_BECD,
    eta_CohSrcPres_BCCube_Qbar_BECD,
    fact_eta_BCCube_to_Prod_CohSrcPres_BCCube_Qbar_BECD,
    lift_eta_BCCube_to_Eq_CohSrcPres_BCCube_Qbar_BECD,
    cmp_lift_eta_BCCube_to_eta_CohSrcPres_BCCube_Qbar_BECD,
    incl_Eq_CohSrcPres_to_Tot_CohSrcPres_BCCube_Qbar_BECD,
    cmp_Eq_CohSrcPres_to_Tot_CohSrcPres_BCCube_Qbar_BECD.

The factorization has twenty-four source-native projections, generates the
seven source facets and seventeen coherence cells, equalizes
alpha_CohSrcPres_BCCube_Qbar_BECD_constraints and
beta_CohSrcPres_BCCube_Qbar_BECD_constraints, and lifts through the equalizer
monic before points and graph objects.

The live graph contains the eta-factorization spine:

    eta_BCCube_Qbar_BECD_source -> fact_eta_BCCube_to_Prod_CohSrcPres_BCCube_Qbar_BECD,
    fact_eta_BCCube_to_Prod_CohSrcPres_BCCube_Qbar_BECD -> Prod_CohSrcPres_BCCube_Qbar_BECD_facets_cells,
    fact_eta_BCCube_to_Prod_CohSrcPres_BCCube_Qbar_BECD -> source-native projections,
    source-native projections -> seven facets,
    source-native projections -> seventeen coherence cells,
    fact_eta_BCCube_to_Prod_CohSrcPres_BCCube_Qbar_BECD -> alpha_CohSrcPres_BCCube_Qbar_BECD_constraints,
    fact_eta_BCCube_to_Prod_CohSrcPres_BCCube_Qbar_BECD -> beta_CohSrcPres_BCCube_Qbar_BECD_constraints,
    alpha_CohSrcPres_BCCube_Qbar_BECD_constraints -> eta equalizes parallel pair,
    beta_CohSrcPres_BCCube_Qbar_BECD_constraints -> eta equalizes parallel pair,
    eta equalizes parallel pair -> lift_eta_BCCube_to_Eq_CohSrcPres_BCCube_Qbar_BECD,
    lift_eta_BCCube_to_Eq_CohSrcPres_BCCube_Qbar_BECD -> Eq_CohSrcPres_BCCube_Qbar_BECD,
    lift_eta_BCCube_to_Eq_CohSrcPres_BCCube_Qbar_BECD -> incl_Eq_CohSrcPres_to_Tot_CohSrcPres_BCCube_Qbar_BECD,
    lift_eta_BCCube_to_Eq_CohSrcPres_BCCube_Qbar_BECD -> cmp_lift_eta_BCCube_to_eta_CohSrcPres_BCCube_Qbar_BECD,
    cmp_lift_eta_BCCube_to_eta_CohSrcPres_BCCube_Qbar_BECD -> eta_CohSrcPres_BCCube_Qbar_BECD,
    cmp_lift_eta_BCCube_to_eta_CohSrcPres_BCCube_Qbar_BECD -> comparison isomorphism,
    lift_eta_BCCube_to_Eq_CohSrcPres_BCCube_Qbar_BECD -> coefficient preservation,
    lift_eta_BCCube_to_Eq_CohSrcPres_BCCube_Qbar_BECD -> signed-support preservation,
    lift_eta_BCCube_to_Eq_CohSrcPres_BCCube_Qbar_BECD -> source before points.

The exact self-dual eta-factorization rows are:

    z                         = {1:2, 2:-1},
    T_C3(z)                   = {3:2, 6:-1},
    T_C5(z)                   = {5:2, 10:-1},
    T_C3(T_C5(z))             = T_C5(T_C3(z))
                                = T_C15(z)            = {15:2, 30:-1},
    T_C3(T_C3(T_C5(z)))       = T_C45(z)              = {45:2, 90:-1},
    z*F22                     = {2:4, 4:-2},
    T_C15(z*F22)              = z*(C15*F22)           = {30:4, 60:-2},
    T_C45(z*F22)              = z*(C45*F22)           = {90:4, 180:-2}.

The mixed checks are equality of full eta-factorization payloads:

    EtaFact(T_C3(T_C5(z)))       = EtaFact(T_C15(z)),
    EtaFact(T_C5(T_C3(z)))       = EtaFact(T_C15(z)),
    EtaFact(T_C3(T_C3(T_C5(z)))) = EtaFact(T_C45(z)),
    EtaFact(T_C15(z*F22))        = EtaFact(z*(C15*F22)),
    EtaFact(T_C45(z*F22))        = EtaFact(z*(C45*F22)).

Thus object-only equalizers, empty equalizers, unsourced lifts, product-only
factorizations, chosen sections, posthoc point maps, graph-side sections,
nonmonic lifts, retuned eta comparisons, and control/DH/Epstein
point-formability do not construct the sourced finite-limit object.
```

## 3. Proof

`prime_int_n1b_qbar_becd_coherent_source_presentation_eta_factorization_contract`
verifies ten gates.

CATCOHSRCPRESETAQBARBECD1 records the source eta factorization through the
product and equalizer, the H1 profile, strict rows, mixed path equalities,
and connected eta-factorization graph.

CATCOHSRCPRESETAQBARBECD2 rejects object-only equalizers.

CATCOHSRCPRESETAQBARBECD3 rejects empty equalizers and unsourced lifts.

CATCOHSRCPRESETAQBARBECD4 rejects chosen sections and posthoc point maps.

CATCOHSRCPRESETAQBARBECD5 rejects product-only factorizations that do not
lift through the equalizer.

CATCOHSRCPRESETAQBARBECD6 rejects nonmonic or retuned eta comparisons.

CATCOHSRCPRESETAQBARBECD7 makes eta generate every projection, facet, and
coherence cell.

CATCOHSRCPRESETAQBARBECD8 makes every eta-factorization edge mandatory.

CATCOHSRCPRESETAQBARBECD9 records that graph-side eta sections still leave
controls, DH, and Epstein formable.

CATCOHSRCPRESETAQBARBECD10 accepts only the sourced eta equalizer lift.

Therefore a candidate that satisfies doc 482 is still incomplete unless the
actual source universal arrow factors through the product, equalizes the
parallel constraints, lifts through the equalizer, and compares isomorphically
to eta_CohSrcPres_BCCube_Qbar_BECD.

## 4. Consequence

The live categorical closure branch is now:

```text
construct fact_eta_BCCube_to_Prod_CohSrcPres_BCCube_Qbar_BECD,
lift_eta_BCCube_to_Eq_CohSrcPres_BCCube_Qbar_BECD, and
cmp_lift_eta_BCCube_to_eta_CohSrcPres_BCCube_Qbar_BECD; prove the source
eta generates all projections/facets/coherence cells; prove it equalizes
alpha/beta; prove the equalizer lift is monic and source-native; and prove
the comparison with eta_CohSrcPres_BCCube_Qbar_BECD is an isomorphism.
```

The open construction target is no longer "construct the internal equalizer
object." It is "show that the existing source universal arrow actually lands
in that equalizer and is the doc-481 source-presentation arrow."

## 5. Acceptance Target For Any Future Candidate

A future candidate must provide:

```text
1. eta_BCCube_Qbar_BECD_source;
2. fact_eta_BCCube_to_Prod_CohSrcPres_BCCube_Qbar_BECD;
3. proof that this factorization generates all twenty-four projections;
4. proof that alpha and beta agree on the factorization;
5. lift_eta_BCCube_to_Eq_CohSrcPres_BCCube_Qbar_BECD;
6. proof that the lift is through incl_Eq_CohSrcPres_to_Tot_CohSrcPres_BCCube_Qbar_BECD;
7. cmp_lift_eta_BCCube_to_eta_CohSrcPres_BCCube_Qbar_BECD;
8. proof that the comparison is an isomorphism;
9. proof of coefficient and signed-support preservation;
10. proof that the eta factorization is formed before points and graph objects with controls, DH, and Epstein non-points.
```

Until this sourced eta factorization exists, the object remains missing.
