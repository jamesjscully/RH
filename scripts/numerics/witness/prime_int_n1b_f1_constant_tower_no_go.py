"""Named F1 constant-field tower no-go.

Doc 202 narrowed the family route to a carrier-native finite
constant/residue-field marker at the archimedean special fiber.  The direct
repair is to use one of the named F1 constant-field objects: the cyclotomic
tower mu_infinity / F_{1^n}, Borger's Lambda-ring / big-Witt ghost
constants, or the Connes-Consani/Arakelov archimedean component.

The older constant-field tower probe shows the obstruction recurs.  Each
finite-field anchor has a finite field F_q and finite roots of unity, and q
marks q^{w/2}.  The named F1 objects are not finite fields: mu_infinity is
the countable colimit Q/Z, Witt ghosts form an infinite indexed product
with one Frobenius per prime, and the Arakelov component has residue field
R or C.  None supplies a single finite base size q.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_f1_constant_tower_no_go
"""

from scripts.numerics.witness.constant_field_tower import (
    candidate_arakelov_archimedean,
    candidate_cyclotomic_tower,
    candidate_witt_ghosts,
    constant_field_roots_of_unity_FF,
    decide,
    dh_vacuous,
)
from scripts.numerics.witness.residue_field_cardinality import (
    decide as residue_field_decide,
)


failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


ff_rows = [constant_field_roots_of_unity_FF(q) for q in (4, 9, 25)]
gate(
    "CFT1 finite-field anchors have finite constant fields and marked radii",
    all(row["constant_field_finite"] and row["radius_marked"] for row in ff_rows)
    and [row["|constant field|"] for row in ff_rows] == [4, 9, 25]
    and [row["|roots of unity|"] for row in ff_rows] == [3, 8, 24],
    "F_q finite, mu_{q-1} finite, q marks q^{1/2}",
)


mu = candidate_cyclotomic_tower()
gate(
    "CFT2 cyclotomic F1 tower has finite levels but infinite colimit",
    mu["all_levels_finite"]
    and not mu["colimit_finite"]
    and not mu["type_match_to_finite_cardinality"]
    and mu["|colimit|"].startswith("aleph_0"),
    f"colimit={mu['colimit']}, |colimit|={mu['|colimit|']}",
)


witt = candidate_witt_ghosts()
gate(
    "CFT3 Witt ghosts are an infinite product, not one finite field",
    not witt["single_constant_field_with_one_Frobenius"]
    and not witt["type_match_to_finite_cardinality"]
    and "INFINITE" in witt["ghost_ring_index"],
    witt["number_of_frobenii"],
)


arak = candidate_arakelov_archimedean()
gate(
    "CFT4 Arakelov archimedean component is continuum/metric data",
    arak["archimedean_structure_is_metric"]
    and not arak["is_finite_constant_field"]
    and not arak["type_match_to_finite_cardinality"]
    and "R or C" in arak["residue_field_at_infinity"],
    arak["size_type"],
)


tower_decision = decide()
residue_decision = residue_field_decide()
gate(
    "CFT5 named F1 towers do not furnish finite constant-field q",
    not tower_decision["any_named_F1_tower_furnishes_finite_constant_field"]
    and not residue_decision["any_F1_supplier_furnishes_finite_kappa"],
    tower_decision["verdict"],
)


dh_msg = dh_vacuous()
gate(
    "CFT6 DH control has no constant-field slot",
    "NO closed point" in dh_msg and "NO 'constant field' slot" in dh_msg,
    "control dies before any finite-q question",
)


carrier_native_finite_constant_field_constructed = False
carrier_native_finite_residue_field_constructed = False
single_frobenius_base_size_constructed = False
finite_q_truncation_constructed = False
archimedean_radius_marker_constructed = False
family_carrier_with_finite_special_fiber_constructed = False
square_side_iota_constructed = False
properness_duality_constructed = False
square_h2_defined = False
square_intersection_form_defined = False
square_correspondence_algebra_defined = False
frobenius_graph_defined = False
positive_rosati_defined = False
laurent_axis_defined = False
boundary_map_defined = False
torsor_splitter_defined = False
dd4_weight_ge_1_datum_defined = False

gate(
    "CFT7 no End(S^2/Z) square/Rosati/R1 data is constructed",
    not carrier_native_finite_constant_field_constructed
    and not carrier_native_finite_residue_field_constructed
    and not single_frobenius_base_size_constructed
    and not finite_q_truncation_constructed
    and not archimedean_radius_marker_constructed
    and not family_carrier_with_finite_special_fiber_constructed
    and not square_side_iota_constructed
    and not properness_duality_constructed
    and not square_h2_defined
    and not square_intersection_form_defined
    and not square_correspondence_algebra_defined
    and not frobenius_graph_defined
    and not positive_rosati_defined
    and not laurent_axis_defined
    and not boundary_map_defined
    and not torsor_splitter_defined
    and not dd4_weight_ge_1_datum_defined,
    "named F1 constants are infinite objects, not the finite q or square correspondences",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (CFT1-CFT7)")
print(
    "VERDICT: the named F1 constant-field towers do not supply the finite "
    "base size required after doc 202.  mu_infinity is countably infinite, "
    "Witt ghosts are an infinite product with one Frobenius per prime, and "
    "the Arakelov archimedean component is R/C continuum metric data.  No "
    "finite q, square correspondence, DD.4 weight>=1 datum, or positive "
    "Rosati is built."
)
