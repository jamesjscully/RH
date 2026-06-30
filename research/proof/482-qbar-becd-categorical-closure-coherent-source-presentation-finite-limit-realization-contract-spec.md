# 482 - Qbar_BECD categorical closure coherent source-presentation finite-limit realization contract

Status: construction-spec refinement anchor, 2026-06-23.
Three-hundred-forty-fifth cycle of the doc-137 construction arc. This is not
a no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 481 left the categorical closure branch live only if the remaining
square/cube/facet/boundary/coherence data are represented by one finite
coherent source-presentation totalizer:

```text
    Cat_CohSrcPres_BCCube_Qbar_BECD,
    Tot_CohSrcPres_BCCube_Qbar_BECD,
    eta_CohSrcPres_BCCube_Qbar_BECD.
```

This document fixes the next edge. A finite represented totalizer is still
not enough if it is only declared, freely presented, syntax-quotiented, or
realized in an external category. The totalizer must be the comparison target
of an internal finite-limit/equalizer object in the existing source category:

```text
    SrcCat_BCCube_Qbar_BECD,
    Prod_CohSrcPres_BCCube_Qbar_BECD_facets_cells,
    alpha_CohSrcPres_BCCube_Qbar_BECD_constraints,
    beta_CohSrcPres_BCCube_Qbar_BECD_constraints,
    Eq_CohSrcPres_BCCube_Qbar_BECD,
    incl_Eq_CohSrcPres_to_Tot_CohSrcPres_BCCube_Qbar_BECD,
    cmp_Eq_CohSrcPres_to_Tot_CohSrcPres_BCCube_Qbar_BECD.
```

The product must have source-native projections to the seven facets and
seventeen coherence cells. The parallel maps must encode the same constraints
as the doc-481 totalizer. The equalizer must be monic into the totalizer, and
the comparison must be an isomorphism preserving coefficients, signed support,
and source-before-points order.

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_coherent_source_presentation_finite_limit_contract`
(CATCOHSRCPRESLIMQBARBECD1-CATCOHSRCPRESLIMQBARBECD10 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
from doc 481 through the DD.4 SCC interface (175/175 exit 0).

## 1. Purpose

After doc 481, the cheap repair is:

```text
declare a finite coherent source-presentation totalizer and use its name as
the universal source-presentation object.
```

That still does not construct the missing object. The source presentation has
to be a finite limit in the existing carrier/source category, not a free
presentation category or syntax quotient built after the fact. This cycle
therefore turns the doc-481 totalizer into a finite-limit question: either the
product/projections, parallel source maps, equalizer, monic inclusion, and
comparison isomorphism exist internally, or the totalizer was only a name.

The live branch narrows from "finite represented coherent source-presentation
totalizer" to:

```text
construct SrcCat_BCCube_Qbar_BECD;
construct Prod_CohSrcPres_BCCube_Qbar_BECD_facets_cells;
construct all twenty-four source-native projections;
construct alpha_CohSrcPres_BCCube_Qbar_BECD_constraints and
beta_CohSrcPres_BCCube_Qbar_BECD_constraints;
construct Eq_CohSrcPres_BCCube_Qbar_BECD;
construct incl_Eq_CohSrcPres_to_Tot_CohSrcPres_BCCube_Qbar_BECD;
construct cmp_Eq_CohSrcPres_to_Tot_CohSrcPres_BCCube_Qbar_BECD;
prove the comparison is an isomorphism with the doc-481 totalizer; and
prove coefficient/signed-support preservation and source-before-points order.
```

## 2. Lemma

```text
Lemma 482.1 (the coherent source-presentation totalizer must be an internal
finite limit).

The original DD.4 class remains:

    c=(1+z)^-1,
    H^1(<phi>; U_1)=Z/2,
    [c] != 0,
    res_1(c)=1,

in truncations L=6,8,10,12.

The accepted finite-limit realization data are:

    SrcCat_BCCube_Qbar_BECD,
    Tot_CohSrcPres_BCCube_Qbar_BECD,
    eta_CohSrcPres_BCCube_Qbar_BECD,
    Prod_CohSrcPres_BCCube_Qbar_BECD_facets_cells,
    alpha_CohSrcPres_BCCube_Qbar_BECD_constraints,
    beta_CohSrcPres_BCCube_Qbar_BECD_constraints,
    Eq_CohSrcPres_BCCube_Qbar_BECD,
    incl_Eq_CohSrcPres_to_Tot_CohSrcPres_BCCube_Qbar_BECD,
    cmp_Eq_CohSrcPres_to_Tot_CohSrcPres_BCCube_Qbar_BECD.

The product has twenty-four source-native projections: seven to
endpoint_integrality, degree_maps, dd4_boundary, boundary_pushforward,
graph_composition, rosati_count, and control_death, and seventeen to the
source-square, Beck-Chevalley-cube, cartesian-lift, component-cone,
component/projection/pairing, globular-modification, boundary-fiber,
cartesian-boundary-fiber, boundary-fiber-coherence, fiber-coherence-
modification, source/target-boundary, multiplier-path, coefficient-
preservation, signed-support-preservation, source-before-points, and
closed-finite-coherence cells.

The live graph contains the finite-limit spine:

    SrcCat_BCCube_Qbar_BECD -> Prod_CohSrcPres_BCCube_Qbar_BECD_facets_cells,
    Prod_CohSrcPres_BCCube_Qbar_BECD_facets_cells -> source-native projections,
    source-native projections -> seven facets,
    source-native projections -> seventeen coherence cells,
    Prod_CohSrcPres_BCCube_Qbar_BECD_facets_cells -> alpha_CohSrcPres_BCCube_Qbar_BECD_constraints,
    Prod_CohSrcPres_BCCube_Qbar_BECD_facets_cells -> beta_CohSrcPres_BCCube_Qbar_BECD_constraints,
    alpha_CohSrcPres_BCCube_Qbar_BECD_constraints -> Eq_CohSrcPres_BCCube_Qbar_BECD,
    beta_CohSrcPres_BCCube_Qbar_BECD_constraints -> Eq_CohSrcPres_BCCube_Qbar_BECD,
    Eq_CohSrcPres_BCCube_Qbar_BECD -> incl_Eq_CohSrcPres_to_Tot_CohSrcPres_BCCube_Qbar_BECD,
    incl_Eq_CohSrcPres_to_Tot_CohSrcPres_BCCube_Qbar_BECD -> Tot_CohSrcPres_BCCube_Qbar_BECD,
    Eq_CohSrcPres_BCCube_Qbar_BECD -> cmp_Eq_CohSrcPres_to_Tot_CohSrcPres_BCCube_Qbar_BECD,
    cmp_Eq_CohSrcPres_to_Tot_CohSrcPres_BCCube_Qbar_BECD -> comparison isomorphism,
    comparison isomorphism -> eta_CohSrcPres_BCCube_Qbar_BECD,
    eta_CohSrcPres_BCCube_Qbar_BECD -> finite source facets,
    eta_CohSrcPres_BCCube_Qbar_BECD -> finite coherence cells,
    closed finite coherence cell -> no next coherence obligation.

The exact self-dual finite-limit rows are:

    z                         = {1:2, 2:-1},
    T_C3(z)                   = {3:2, 6:-1},
    T_C5(z)                   = {5:2, 10:-1},
    T_C3(T_C5(z))             = T_C5(T_C3(z))
                                = T_C15(z)            = {15:2, 30:-1},
    T_C3(T_C3(T_C5(z)))       = T_C45(z)              = {45:2, 90:-1},
    z*F22                     = {2:4, 4:-2},
    T_C15(z*F22)              = z*(C15*F22)           = {30:4, 60:-2},
    T_C45(z*F22)              = z*(C45*F22)           = {90:4, 180:-2}.

The mixed checks are equality of full finite-limit payloads:

    CohSrcLim(T_C3(T_C5(z)))       = CohSrcLim(T_C15(z)),
    CohSrcLim(T_C5(T_C3(z)))       = CohSrcLim(T_C15(z)),
    CohSrcLim(T_C3(T_C3(T_C5(z)))) = CohSrcLim(T_C45(z)),
    CohSrcLim(T_C15(z*F22))        = CohSrcLim(z*(C15*F22)),
    CohSrcLim(T_C45(z*F22))        = CohSrcLim(z*(C45*F22)).

The graph/Rosati/count diagnostics remain anchored:

    count defect 0,
    Rosati anti-involution defect 0.

The control warning remains:

    carrier q=7 graph signature = control q=3 graph signature,
    carrier primitive sign -13.5,
    control primitive sign +12,
    control projection defect 24,
    retuned first degree 27.

Thus declared totalizers, free presentation categories, syntax-only limits,
external limits, posthoc equalizers, graph-side or pointwise limits,
pro-limits, retuned comparisons, and control/DH/Epstein point-formability do
not construct the internal finite-limit realization.
```

## 3. Proof

`prime_int_n1b_qbar_becd_coherent_source_presentation_finite_limit_contract`
verifies ten gates.

CATCOHSRCPRESLIMQBARBECD1 records the internal equalizer realization, its
twenty-four projections, H1 profile, strict rows, mixed path equalities, and
connected finite-limit graph.

CATCOHSRCPRESLIMQBARBECD2 records again that graph identities do not supply
the finite limit.

CATCOHSRCPRESLIMQBARBECD3 rejects declared totalizers without source limits.

CATCOHSRCPRESLIMQBARBECD4 rejects free presentation categories and syntax
limits.

CATCOHSRCPRESLIMQBARBECD5 makes the product and all source-native projections
mandatory.

CATCOHSRCPRESLIMQBARBECD6 makes the equalizer, monic inclusion, comparison,
and universal property mandatory.

CATCOHSRCPRESLIMQBARBECD7 rejects external, posthoc, graph-side, pointwise,
and pro limits.

CATCOHSRCPRESLIMQBARBECD8 rejects retuned comparisons.

CATCOHSRCPRESLIMQBARBECD9 makes every finite-limit edge mandatory.

CATCOHSRCPRESLIMQBARBECD10 accepts only the internal finite-limit realization.

Therefore a candidate that satisfies doc 481 is still incomplete unless its
finite coherent source-presentation totalizer is realized by an internal
finite product, source-native projections, parallel constraints, equalizer,
monic inclusion, and comparison isomorphism in the existing source category.

## 4. Consequence

The live categorical closure branch is now:

```text
construct Prod_CohSrcPres_BCCube_Qbar_BECD_facets_cells,
alpha_CohSrcPres_BCCube_Qbar_BECD_constraints,
beta_CohSrcPres_BCCube_Qbar_BECD_constraints,
Eq_CohSrcPres_BCCube_Qbar_BECD,
incl_Eq_CohSrcPres_to_Tot_CohSrcPres_BCCube_Qbar_BECD, and
cmp_Eq_CohSrcPres_to_Tot_CohSrcPres_BCCube_Qbar_BECD inside
SrcCat_BCCube_Qbar_BECD; prove all twenty-four projections are source-native;
prove the equalizer has the universal property and compares isomorphically to
Tot_CohSrcPres_BCCube_Qbar_BECD; and prove coefficient/signed-support
preservation and source-before-points order.
```

The open construction target is no longer "name a finite coherent
source-presentation totalizer." It is "construct the internal finite-limit
realization of that totalizer in the existing source category."

## 5. Acceptance Target For Any Future Candidate

A future candidate must provide:

```text
1. SrcCat_BCCube_Qbar_BECD;
2. Prod_CohSrcPres_BCCube_Qbar_BECD_facets_cells;
3. all twenty-four source-native projections;
4. alpha_CohSrcPres_BCCube_Qbar_BECD_constraints and beta_CohSrcPres_BCCube_Qbar_BECD_constraints;
5. Eq_CohSrcPres_BCCube_Qbar_BECD;
6. incl_Eq_CohSrcPres_to_Tot_CohSrcPres_BCCube_Qbar_BECD;
7. cmp_Eq_CohSrcPres_to_Tot_CohSrcPres_BCCube_Qbar_BECD;
8. proof that the comparison is an isomorphism with the doc-481 totalizer;
9. proof of the equalizer universal property and coefficient/signed-support preservation;
10. proof that the finite limit is formed before points and graph objects with controls, DH, and Epstein non-points.
```

Until this internal finite-limit realization exists, the object remains
missing.
