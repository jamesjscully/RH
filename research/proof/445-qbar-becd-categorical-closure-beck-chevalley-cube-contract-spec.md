# 445 - Qbar_BECD categorical closure Beck-Chevalley cube contract

Status: construction-spec refinement anchor, 2026-06-23.
Three-hundred-eighth cycle of the doc-137 construction arc. This is not
a no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 444 left the strict-square branch live only if one represented source
square closes the boundary/cartesian/coherence/globular cycle idempotently
and emits endpoint integrality, degree maps, the DD.4 boundary, graph
composition, Rosati sign, and formation-level control death from one
universal source map. This document fixes the next edge. Those facets are
still insufficient if they are only independent edge witnesses or a bundled
tuple of correct-looking values. They must form one source-native
Beck-Chevalley compatibility cube.

```text
CatSq_Qbar_BECD_closes_doc443_boundary_cycle
  -> BCCube_CatSq_Qbar_BECD_facets
  -> Tot_BCCube_CatSq_Qbar_BECD
```

The cube datum fixed by this cycle is:

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
Beck-Chevalley exactness: BCExact_CatSq_Qbar_BECD_boundary_graph_rosati_control
```

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_categorical_closure_beck_chevalley_cube_contract`
(CATBCCUBEQBARBECD1-CATBCCUBEQBARBECD10 ALL PASS).

Adjacent witnesses, lead-reran this cycle: from doc 444 through the DD.4 SCC
interface, all exit 0.

## 1. Purpose

Doc 444 stopped the mechanical tower. The remaining cheap repair is subtler:

```text
construct edge witnesses for endpoint integrality, degree maps, DD.4,
graph composition, Rosati, and control death,
bundle those witnesses beside the doc-443 boundary fiber,
then call the bundle the represented categorical source square.
```

That still does not construct the missing object. The facets have to commute
inside one source-native compatibility cube. Endpoint/degree, degree/DD.4,
degree/graph, graph/Rosati, DD.4/control, and Rosati/control faces must be
the faces of one totalization. The facet projections must be jointly monic,
so two proposed source squares with the same facet payload are the same
source square.

The live branch narrows from:

```text
one represented source square whose universal map emits all closure facets
```

to:

```text
one represented source square whose emitted facets form a totalized
Beck-Chevalley source cube with jointly monic facet projections.
```

This is compatible with doc 276's carrier-first categorical route and with
docs 301 and 302, which killed universal-property and equivalence shortcuts.
The universal property is allowed only as the universal map of the represented
source square. The cube is allowed only as source-native compatibility data,
not as a posthoc diagram of external facets.

## 2. Lemma

```text
Lemma 445.1 (categorical closure Beck-Chevalley cube contract).

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

Applying the boundary/cartesian/coherence/globular closure operator to the
doc-443 boundary fiber must return the same represented source square. If it
creates a new layer, the candidate is only a tower extension.

Independent facet bundles, edgewise-only witnesses, declared commutative
cubes, posthoc naturality, external totalizations, non-jointly-monic facet
families, facet products after points, cube-by-equivalence wrappers, and
one-more-layer cube towers do not construct the missing object.
```

## 3. Proof

`prime_int_n1b_qbar_becd_categorical_closure_beck_chevalley_cube_contract` verifies ten
gates.

CATBCCUBEQBARBECD1 records the represented categorical source square, the
doc-443 boundary fiber, the Beck-Chevalley facet cube, cube totalization,
jointly monic facets, idempotent closure layer, H1 profile, finite-field
count anchors, endpoint balance, graph composition, and Rosati sign.

CATBCCUBEQBARBECD2 rejects recognition and equivalence wrappers as cube
construction.

CATBCCUBEQBARBECD3 rejects one-more-layer tower extension: the cube
totalization must return the same source square, not create a new boundary
layer.

CATBCCUBEQBARBECD4 requires the endpoint and degree faces to commute in the
cube with jointly monic facet projections.

CATBCCUBEQBARBECD5 requires DD.4 death to be an exact cube face, not a free
splitter or local boundary table.

CATBCCUBEQBARBECD6 requires graph and Rosati faces to commute in the cube,
not as graph-side or post-product patching.

CATBCCUBEQBARBECD7 requires Rosati and control faces to share one cube
totalization.

CATBCCUBEQBARBECD8 makes every Beck-Chevalley cube face mandatory.

CATBCCUBEQBARBECD9 records that facet products after points leave controls,
DH, and Epstein formable.

CATBCCUBEQBARBECD10 accepts only one totalized source cube.

Therefore the doc-444 represented categorical closure square is still
incomplete unless its emitted endpoint, boundary, graph, Rosati, and
control-death facets form one totalized Beck-Chevalley source cube.

## 4. Consequence

The live strict-square branch is now:

```text
construct CatSq_Qbar_BECD_closes_doc443_boundary_cycle;
construct BCCube_CatSq_Qbar_BECD_facets;
construct Tot_BCCube_CatSq_Qbar_BECD;
construct JMonic_BCCube_CatSq_Qbar_BECD_facets;
prove endpoint/degree, degree/DD.4, degree/graph, graph/Rosati,
DD.4/control, and Rosati/control faces commute source-natively;
prove the cube totalizes the doc-444 square and returns the same represented
source square under closure;
prove the facet projections are jointly monic before points and graph objects.
```

The open construction target is no longer "bundle all facets." It is
"construct the represented source cube whose totalization is the missing
source square."

## 5. Acceptance Target For Any Future Candidate

A future candidate must provide:

```text
1. the represented categorical source square;
2. its universal source arrow;
3. the doc-443 represented boundary fiber as a cube face;
4. endpoint/degree, degree/DD.4, degree/graph, graph/Rosati,
   DD.4/control, and Rosati/control commutative faces;
5. Beck-Chevalley exactness for the boundary, graph, Rosati, and control
   faces;
6. cube totalization;
7. jointly monic facet projections;
8. the same cube on all finite-anchor paths;
9. coefficient and signed-support preservation;
10. idempotent closure of the boundary/cartesian/coherence/globular cycle.
```

Until this totalized Beck-Chevalley source cube exists, the object remains
missing.
