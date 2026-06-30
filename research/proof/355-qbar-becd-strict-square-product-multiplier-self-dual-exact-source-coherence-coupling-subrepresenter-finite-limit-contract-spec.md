# 355 - Qbar_BECD strict-square product multiplier self-dual exact-source coherence-coupling subrepresenter finite-limit contract

Status: construction-spec refinement anchor, 2026-06-23.
Two-hundred-eighteenth cycle of the doc-137 construction arc. This is not a
no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 354 left the strict-square branch live only if the source-coupling
representer is an actual subrepresenter/fiber of the represented source
fiber:

```text
    SubRep_NCoup_Qbar_BECD_source_fiber,
    incl_NCoup_to_Rep_Qbar_BECD_source_fiber.
```

This document fixes the next edge. A source subrepresenter is still not the
missing object if it is certified only by a pointwise exact-image predicate,
a characteristic map into a subobject classifier, a sequential intersection
of filters, a local row table, or a late pullback after graph objects exist.
The subrepresenter must be produced internally by one finite-limit/equalizer
fork in the represented source fiber:

```text
    LimCut_NCoup_Qbar_BECD_source_fiber,
    Fork_endpoint_dd4_rosati_control_NCoup,
    eq_NCoup_constraints_to_SubRep_Qbar_BECD_source_fiber.
```

That fork must impose endpoint integrality, degree maps, the original DD.4
boundary, boundary pushforward, graph composition, Rosati/count, and control
death simultaneously, before points and graph objects exist.

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_self_dual_exact_source_coherence_coupling_subrepresenter_finite_limit_contract`
(SCFL1-SCFL10 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_self_dual_exact_source_coherence_coupling_subrepresenter_contract`,
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_self_dual_exact_source_coherence_coupling_representability_contract`,
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_self_dual_exact_source_coherence_coupling_contract`,
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_self_dual_exact_source_formation_coherence_contract`,
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_self_dual_exact_source_formation_gate_contract`,
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_represented_source_fiber_contract`,
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_cartesian_coherence_contract`,
`prime_int_n1b_qbar_becd_joint_formation_coupling_contract`,
`prime_int_n1b_qbar_becd_control_formation_death_contract`,
`prime_int_n1b_qbar_becd_boundary_pushforward_compat_contract`, and
`prime_int_n1b_dd4_scc_interface`.

## 1. Purpose

After doc 354, the cheap repair is:

```text
name a subrepresenter whose points are exactly the coupled sources,
prove the pointwise image has the desired finite rows,
then use graph/Rosati/DD.4 filters to remove controls after the fact.
```

That still does not construct the missing object. The square must make the
source fiber cut out the subrepresenter internally. The cut must be a single
finite-limit/equalizer fork, not an intersection of separately checked
predicates. The fork must carry the endpoint, degree, DD.4, pushforward,
graph, Rosati/count, and control-death constraints together. If any one of
those constraints is added later, controls can be formed before the square
kills them.

The live branch therefore narrows from "actual source subrepresenter" to:

```text
construct LimCut_NCoup_Qbar_BECD_source_fiber,
Fork_endpoint_dd4_rosati_control_NCoup, and
eq_NCoup_constraints_to_SubRep_Qbar_BECD_source_fiber; prove this is a
carrier-native finite-limit/equalizer fork in Rep_Qbar_BECD_source_fiber;
prove its equalizer arrow is monic; prove its image is the doc-354
subrepresenter; prove the fork imposes all endpoint/DD.4/pushforward/
graph/Rosati/count/control-death constraints simultaneously before points and
graph objects exist.
```

## 2. Lemma

```text
Lemma 355.1 (the source subrepresenter must be an internal finite-limit cut).

The original DD.4 class remains:

    c=(1+z)^-1,
    H^1(<phi>; U_1)=Z/2,
    [c] != 0,
    res_1(c)=1,

in truncations L=6,8,10,12.

The accepted finite-limit subrepresenter data are:

    Rep_Qbar_BECD_source_fiber,
    SubRep_NCoup_Qbar_BECD_source_fiber,
    incl_NCoup_to_Rep_Qbar_BECD_source_fiber,
    LimCut_NCoup_Qbar_BECD_source_fiber,
    Fork_endpoint_dd4_rosati_control_NCoup,
    eq_NCoup_constraints_to_SubRep_Qbar_BECD_source_fiber,
    NCoup_Qbar_BECD_BCF_self_dual_exact_source,
    Delta_Qbar_BECD_BCF_to_dQ_boundary,
    dd4_c_original_res1,
    NR_Qbar_BECD_ordered_p1_p2,
    PF_Qbar_BECD_p1p2,
    G_Qbar_BECD_prop,
    R_Qbar_BECD_pos,
    CD_Qbar_BECD,
    CTRL_Qbar_BECD_coherent_death.

The finite-limit dependency graph contains the live edges:

    Rep_Qbar_BECD_source_fiber -> LimCut_NCoup,
    LimCut_NCoup -> Fork_endpoint_dd4_rosati_control_NCoup,
    Fork_endpoint_dd4_rosati_control_NCoup -> endpoint integrality,
    Fork_endpoint_dd4_rosati_control_NCoup -> degree maps,
    Fork_endpoint_dd4_rosati_control_NCoup -> DD.4 boundary,
    Fork_endpoint_dd4_rosati_control_NCoup -> boundary pushforward,
    Fork_endpoint_dd4_rosati_control_NCoup -> graph composition,
    Fork_endpoint_dd4_rosati_control_NCoup -> Rosati/count,
    Fork_endpoint_dd4_rosati_control_NCoup -> control death,
    LimCut_NCoup -> eq_NCoup_constraints_to_SubRep,
    eq_NCoup_constraints_to_SubRep -> SubRep_NCoup,
    eq_NCoup_constraints_to_SubRep -> incl_NCoup_to_Rep_Qbar_BECD_source_fiber,
    eq_NCoup_constraints_to_SubRep -> monic equalizer arrow,
    monic equalizer arrow -> exact subrepresenter image,
    exact subrepresenter image -> coupled self-dual exact sources,
    coupled self-dual exact sources -> NCoup,
    NCoup -> exact boundary delta,
    exact boundary delta -> original DD.4 boundary,
    original DD.4 boundary -> normal ratio,
    normal ratio -> endpoint pushforward,
    endpoint pushforward -> graph composition,
    graph composition -> Rosati/count,
    Rosati/count -> control death,
    LimCut_NCoup -> universal property,
    universal property -> same cut on all paths,
    same cut on all paths -> C3*C5=C15,
    same cut on all paths -> C5*C3=C15,
    same cut on all paths -> C3*C3*C5=C45,
    same cut on all paths -> F22 product,
    LimCut_NCoup -> source before points and graph objects,
    source before points and graph objects -> controls not points,
    source before points and graph objects -> DH not points,
    source before points and graph objects -> Epstein not points.

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

The mixed finite-limit checks are equality of full finite-limit cut payloads:

    LimCut(T_C3(T_C5(z)))       = LimCut(T_C15(z)),
    LimCut(T_C5(T_C3(z)))       = LimCut(T_C15(z)),
    LimCut(T_C3(T_C3(T_C5(z)))) = LimCut(T_C45(z)),
    LimCut(T_C15(z*F22))        = LimCut(z*(C15*F22)),
    LimCut(T_C45(z*F22))        = LimCut(z*(C45*F22)).

The graph/Rosati/count diagnostics remain anchored:

    count defect 0,
    Rosati anti-involution defect 0.

The control warning remains:

    carrier q=7 graph signature = control q=3 graph signature,
    carrier primitive sign -13.5,
    control primitive sign +12,
    control projection defect 24,
    retuned first degree 27.

Thus pointwise image certificates, predicate subobject selections, subobject
classifiers, characteristic-map-only repairs, sequential intersections,
iterated filters, post-hoc image factorizations, external finite-limit
completions, pullbacks after graph objects, local row tables, finite-sample
cuts, basis-dependent cuts, retuned/projected constraints, graph-invariant
classifiers, declared equalizers, and control/DH/Epstein point-formability do
not construct the finite-limit source cut.

The accepted datum is exactly:

    carrier-native,
    represented source fiber,
    actual coupling subrepresenter,
    actual finite-limit cut,
    actual joint constraint fork,
    actual equalizer arrow,
    monic equalizer arrow,
    commuting fork,
    actual universal property,
    cut before points,
    cut before graph objects,
    image is the doc-354 subrepresenter,
    constraints in one fork,
    endpoint integrality in the fork,
    degree maps in the fork,
    DD.4 boundary in the fork,
    boundary pushforward in the fork,
    graph composition in the fork,
    Rosati/count in the fork,
    control death in the fork,
    same cut on all paths,
    actual C3*C5=C15 source coherence,
    actual C5*C3=C15 source coherence,
    actual C3*C3*C5=C45 source coherence,
    actual F22 product source coherence,
    finite anchors generated,
    controls not points,
    DH not points,
    Epstein not points,
    required finite-limit edges present,
    no pointwise image certificate,
    no predicate subobject selection,
    no subobject classifier,
    no characteristic map only,
    no sequential intersection,
    no iterated filters,
    no post-hoc image factorization,
    no external finite-limit completion,
    no pullback after graph objects,
    no local row table,
    no finite-sample cut,
    no basis-dependent cut,
    no retuned/projected constraint,
    no graph-invariant classifier,
    no declared equalizer,
    no control/DH/Epstein point-formability.
```

Verdict label:

```text
N1B_QBAR_BECD_STRICT_SQUARE_PRODUCT_MULTIPLIER_SELF_DUAL_EXACT_SOURCE_COHERENCE_COUPLING_SUBREPRESENTER_FINITE_LIMIT__SIMULTANEOUS_SOURCE_EQUALIZER_CUT__SPEC.
```

## 3. Proof

`prime_int_n1b_qbar_becd_strict_square_product_multiplier_self_dual_exact_source_coherence_coupling_subrepresenter_finite_limit_contract`
verifies ten gates.

SCFL1 records the source finite-limit/equalizer fork, H1 profile, strict
rows, finite-limit-payload equalities, and connected cut graph.

SCFL2 records again that graph identities do not supply the finite-limit cut.

SCFL3 rejects pointwise exact-image predicates, predicate subobject
selection, subobject classifiers, and characteristic-map-only repairs.

SCFL4 rejects sequential intersections, iterated filters, and post-hoc image
factorizations.

SCFL5 rejects external finite-limit completions and pullbacks after graph
objects.

SCFL6 rejects local row tables, finite-sample cuts, basis-dependent cuts, and
retuned/projected constraints.

SCFL7 rejects graph/Rosati/DD.4 after-filters that leave controls, DH, and
Epstein formable.

SCFL8 proves every finite-limit cut edge is mandatory.

SCFL9 proves only simultaneous source finite-limit cuts pass.

SCFL10 records the live predicate. The live cut is internal, not a predicate
shell.

## 4. Effect on R1

This cycle fixes one more interface in the categorical square:

```text
SubRep_NCoup is acceptable only if it is produced by a carrier-native
finite-limit/equalizer fork inside Rep_Qbar_BECD_source_fiber, imposing the
endpoint, degree, DD.4, pushforward, graph, Rosati/count, and control-death
constraints simultaneously before points and graph objects exist.
```

The open construction target is now:

```text
construct LimCut_NCoup_Qbar_BECD_source_fiber,
Fork_endpoint_dd4_rosati_control_NCoup, and
eq_NCoup_constraints_to_SubRep_Qbar_BECD_source_fiber, or kill the
strict-square branch at the finite-limit source-cut interface.
```

No claim here proves R1 or RH. The document only prevents the next
categorical shortcut: certifying the source subrepresenter by pointwise
image, predicate selection, sequential filters, local tables, late pullbacks,
retunings, or graph/Rosati/DD.4 after-filters.

## 5. Acceptance and kill conditions

ACCEPT-SCFL.1 Exhibit `LimCut_NCoup_Qbar_BECD_source_fiber`.

ACCEPT-SCFL.2 Exhibit `Fork_endpoint_dd4_rosati_control_NCoup`.

ACCEPT-SCFL.3 Exhibit
`eq_NCoup_constraints_to_SubRep_Qbar_BECD_source_fiber`.

ACCEPT-SCFL.4 Prove the fork commutes in `Rep_Qbar_BECD_source_fiber`.

ACCEPT-SCFL.5 Prove the equalizer arrow is monic and has image exactly the
doc-354 subrepresenter.

ACCEPT-SCFL.6 Prove endpoint integrality, degree maps, DD.4 boundary,
boundary pushforward, graph composition, Rosati/count, and control death are
all constraints of the same fork.

ACCEPT-SCFL.7 Prove the same finite-limit cut transports all C3/C5/C15/C45/F22
paths.

ACCEPT-SCFL.8 Prove controls/DH/Epstein are non-points before points and graph
objects exist.

KILL-SCFL.1 Kill any pointwise image certificate, predicate subobject
selection, subobject classifier, characteristic-map-only repair, sequential
intersection, iterated filter, post-hoc image factorization, external
finite-limit completion, late pullback, local row table, finite-sample cut,
basis-dependent cut, retuned/projected constraint, graph-invariant
classifier, declared equalizer, or point-formable control/DH/Epstein repair.
