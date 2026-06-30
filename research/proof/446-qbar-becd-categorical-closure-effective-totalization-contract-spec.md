# 446 - Qbar_BECD categorical closure effective-totalization contract

Status: construction-spec refinement anchor, 2026-06-23.
Three-hundred-ninth cycle of the doc-137 construction arc. This is not
a no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 445 left the strict-square branch live only if the emitted endpoint,
degree, DD.4, graph, Rosati, and control-death facets form one source-native
compatibility cube with one totalization and jointly monic facet projections.
This document fixes the next edge. A totalized cube is still insufficient if
it exists only formally, at finite anchors, in truncations, or over an
external effectivity address. The totalization must be effective inside the
internal Qbar_BECD effectivity stratum.

```text
CatSq_Qbar_BECD_closes_doc443_boundary_cycle
  -> BCCube_CatSq_Qbar_BECD_facets
  -> Tot_BCCube_CatSq_Qbar_BECD
  -> EffTot_BCCube_Qbar_BECD_internal_stratum
```

The effective-totalization datum fixed by this cycle is:

```text
categorical source square: CatSq_Qbar_BECD_closes_doc443_boundary_cycle
universal source arrow: eta_CatSq_Qbar_BECD_source_closure
doc-443 boundary fiber: Fib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartCone_NCoup_eta_source_components
endpoint integrality: EndInt_CatSq_Qbar_BECD
degree maps: Deg_CatSq_Qbar_BECD_p1_p2
DD.4 boundary: DD4Bd_CatSq_Qbar_BECD
graph composition: GraphComp_CatSq_Qbar_BECD
Rosati positivity: Rosati_CatSq_Qbar_BECD_positive
control death: ControlDeath_CatSq_Qbar_BECD_formation
closure idempotence: IdemClosure_CatSq_Qbar_BECD
facet cube: BCCube_CatSq_Qbar_BECD_facets
cube totalization: Tot_BCCube_CatSq_Qbar_BECD
jointly monic facets: JMonic_BCCube_CatSq_Qbar_BECD_facets
cube exactness: BCExact_CatSq_Qbar_BECD_boundary_graph_rosati_control
internal effectivity domain: D_Qbar_BECD_eff
effective totalization: EffTot_BCCube_Qbar_BECD_internal_stratum
algebraization over Z: Alg_BCCube_Qbar_BECD_over_Z
domain-typed cube: Typed_BCCube_Qbar_BECD_by_D_eff
```

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_categorical_closure_effective_totalization_contract`
(CATEFFTOTQBARBECD1-CATEFFTOTQBARBECD10 ALL PASS).

Adjacent witnesses, lead-reran this cycle: from doc 445 through the DD.4 SCC
interface, all exit 0.

## 1. Purpose

Doc 445 stopped the independent-facet bundle. The remaining cheap repair is:

```text
construct a compatible source cube at every finite anchor or truncation,
declare the inverse-compatible family to be the totalized source square,
then use effectivity language as a label.
```

That still does not construct the missing object. The totalization has to be
effective in the internal Qbar_BECD effectivity stratum from docs 323 and
324. Its cube faces must be typed by that stratum, the prime-power valuation
tower must be native there, the totalization must algebraize over Z, and
controls/Epstein must be undefined at that internal domain while theta/count
shadows remain downstream.

The live branch narrows from:

```text
one totalized Beck-Chevalley source cube with jointly monic facets
```

to:

```text
one internally effective totalization of that source cube inside D_Qbar_BECD_eff.
```

This is compatible with doc 276's carrier-first categorical route and with
docs 301 and 302, which killed universal-property and equivalence shortcuts.
The cube is allowed only as source-native compatibility data. Effectivity is
allowed only as represented internal-stratum data, not as finite-anchor
compatibility or an external Euler address.

## 2. Lemma

```text
Lemma 446.1 (categorical closure effective-totalization contract).

The original DD.4 class remains:

    c=(1+z)^-1,
    H^1(<phi>; U_1)=Z/2,
    [c] != 0,
    res_1(c)=1,

in truncations L=6,8,10,12.

The square closure must preserve the represented endpoint rows:

    T_C3(T_C5(z))             = T_C5(T_C3(z))
                                = T_C15(z)            = {15:2, 30:-1},
    T_C3(T_C3(T_C5(z)))       = T_C45(z)              = {45:2, 90:-1},
    T_C15(z*F22)              = z*(C15*F22)           = {30:4, 60:-2},
    T_C45(z*F22)              = z*(C45*F22)           = {90:4, 180:-2}.

The cube must contain the faces:

    endpoint/degree,
    degree/DD.4,
    degree/graph,
    graph/Rosati,
    DD.4/control,
    Rosati/control.

The totalization must be typed by the internal effectivity stratum

    D_Qbar_BECD_eff

and must carry:

    native prime-power tower      1,2,4,8,16,32,64,
    native valuation depths       0,1,2,3,4,5,6,
    algebraization over Z,
    all cube faces typed by the same internal stratum,
    controls undefined at that stratum,
    Epstein undefined at that stratum.

The Epstein represented-norm shadow remains downstream: for Q=x^2+5y^2,
1,4,6,9,36 are represented and 36 has two irreducible factorizations,
4*9 and 6*6. Thus theta/count data can survive without being the internal
effectivity totalization.

Applying the boundary/cartesian/coherence/globular closure operator to the
doc-443 boundary fiber must return the same represented source square. If it
creates a new layer, the candidate is only a tower extension.

Formal totalizations, finite-anchor cubes, truncationwise descent, external
effectivity domains, declared internal-domain IDs, external prime monoids,
valuation registers, degree-pair codecs, theta-kernel promotion,
Epstein-norm shadow promotion, and control-formable totalizations do not
construct the missing object.
```

## 3. Proof

`prime_int_n1b_qbar_becd_categorical_closure_effective_totalization_contract` verifies ten
gates.

CATEFFTOTQBARBECD1 records the represented categorical source square, the
doc-443 boundary fiber, the facet cube, cube totalization, internal
effectivity domain, effective totalization, algebraization, native
prime-power tower, H1 profile, finite-field count anchors, endpoint balance,
graph composition, and Rosati sign.

CATEFFTOTQBARBECD2 rejects recognition and equivalence wrappers as effective
totalization construction.

CATEFFTOTQBARBECD3 rejects finite-anchor towers: compatible finite layers do
not algebraize the totalization over Z.

CATEFFTOTQBARBECD4 requires endpoint and degree faces to be typed by the
internal effectivity domain.

CATEFFTOTQBARBECD5 requires DD.4 exactness to be internal-effective, not a
free splitter, valuation register, or local table.

CATEFFTOTQBARBECD6 requires graph and Rosati faces to be internally typed,
not post-product graph patches or degree-pair codecs.

CATEFFTOTQBARBECD7 requires controls and Epstein to be undefined at the
internal domain while theta/count shadows stay downstream.

CATEFFTOTQBARBECD8 makes every effective-totalization face mandatory.

CATEFFTOTQBARBECD9 records that facet products after points leave controls,
DH, and Epstein formable.

CATEFFTOTQBARBECD10 accepts only one internal-effective source totalization.

Therefore the doc-445 totalized source cube is still incomplete unless its
totalization is effective inside the internal Qbar_BECD effectivity stratum.

## 4. Consequence

The live strict-square branch is now:

```text
construct CatSq_Qbar_BECD_closes_doc443_boundary_cycle;
construct BCCube_CatSq_Qbar_BECD_facets;
construct Tot_BCCube_CatSq_Qbar_BECD;
construct JMonic_BCCube_CatSq_Qbar_BECD_facets;
construct EffTot_BCCube_Qbar_BECD_internal_stratum;
construct Alg_BCCube_Qbar_BECD_over_Z;
prove the totalization is typed by D_Qbar_BECD_eff;
prove native prime-power tower and valuation depth live in that stratum;
prove every cube face is typed by that stratum;
prove controls and Epstein are undefined at that internal domain while
theta/count shadows remain downstream.
```

The open construction target is no longer "totalize the cube formally." It
is "construct the internally effective totalization of the source cube."

## 5. Acceptance Target For Any Future Candidate

A future candidate must provide:

```text
1. the represented categorical source square;
2. its universal source arrow;
3. the doc-443 represented boundary fiber as a cube face;
4. endpoint/degree, degree/DD.4, degree/graph, graph/Rosati,
   DD.4/control, and Rosati/control commutative faces;
5. exactness for the boundary, graph, Rosati, and control faces;
6. cube totalization;
7. internal-effectivity-domain typing of that totalization;
8. algebraization over Z and native prime-power valuation tower;
9. controls and Epstein undefined at the internal domain;
10. idempotent closure of the boundary/cartesian/coherence/globular cycle.
```

Until this internally effective source totalization exists, the object
remains missing.
