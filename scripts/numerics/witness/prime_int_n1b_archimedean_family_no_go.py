"""Archimedean degenerating family / finite-residue-field no-go.

After doc 201, the surviving surface-shaped route is no longer the static
product surface.  It is the family carrier: a degenerating family with a
special fiber, nearby-cycle monodromy N, and monodromy filtration M(N)=W.

The older archimedean-family probes show the subtle point.  The family and
nearby-cycle data exist at infinity: Schmid supplies N and M(N)=W for a
degeneration over a complex disk.  What does not exist there is a finite
residue field at the closed point t=0.  Over F_q, the finite cardinality
|kappa(t=0)|=q supplies the base size that marks radii q^{w/2}.  At
infinity, kappa(t=0)=C, so there is no finite q, no Frobenius base size,
and no carrier-native radius marker.  The scaling-site, length-edge, and
Bost-Connes suppliers give continuum/length/discrete-index data, not a
finite residue-field cardinality.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_archimedean_family_no_go
"""

from scripts.numerics.witness.archimedean_degenerating_family import (
    check_A_nearby_cycle_exists,
    check_B_fq_finite_residue_field,
    check_C_archimedean_continuum_residue_field,
    check_D_dh_vacuous as archimedean_dh_vacuous,
)
from scripts.numerics.witness.residue_field_cardinality import (
    decide,
    dh_vacuous as cardinality_dh_vacuous,
    residue_field_cardinality_FF,
    supplier_bost_connes,
    supplier_length_edge,
    supplier_scaling_site,
)


failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


nearby = check_A_nearby_cycle_exists(w=2)
gate(
    "ADF1 nearby-cycle N and M(N)=W exist at infinity",
    nearby["M(N)=W_symmetric_split"] and nearby["base_field_free"],
    f"split={nearby['M(N)_graded (centre w)']}",
)


finite_rows = check_B_fq_finite_residue_field()
finite_qs = [row["q = |kappa(t=0)|"] for row in finite_rows]
finite_radii = [
    row["radius |alpha| on gr^W_w = q^{w/2}"] for row in finite_rows
]
gate(
    "ADF2 finite-field special fibers mark radii by finite kappa",
    finite_qs == [4, 9, 25]
    and all(row["radius_marked"] for row in finite_rows)
    and finite_radii == [2.0, 3.0, 5.0],
    f"q={finite_qs}, radii={finite_radii}",
)


arch = check_C_archimedean_continuum_residue_field()
gate(
    "ADF3 archimedean special fiber has continuum residue field",
    arch["N_present (Schmid)"]
    and arch["M(N)=W_present (integer weight grading)"]
    and not arch["residue_field_finite"]
    and not arch["has_Frobenius"]
    and not arch["radius_marked"],
    f"kappa={arch['kappa(t=0)']}, q={arch['q = |kappa(t=0)|']}",
)


constant_field_rows = [residue_field_cardinality_FF(q, deg_point=1) for q in (4, 9, 25)]
gate(
    "ADF4 finite kappa is supplied by a finite constant field",
    all(row["kappa_finite"] and row["radius_marked"] for row in constant_field_rows)
    and [row["|kappa(t=0)| = q^deg"] for row in constant_field_rows] == [4, 9, 25],
    "finite closed-point cardinality is a constant-field datum",
)


sca = supplier_scaling_site()
length = supplier_length_edge()
bc = supplier_bost_connes()
residue_decision = decide()
gate(
    "ADF5 F1 suppliers fail the finite-kappa type check",
    not sca["type_match_to_constant_field_cardinality"]
    and not length["type_match_to_constant_field_cardinality"]
    and not bc["type_match_to_constant_field_cardinality"]
    and not residue_decision["any_F1_supplier_furnishes_finite_kappa"],
    residue_decision["verdict"],
)


arch_dh = archimedean_dh_vacuous()
card_dh = cardinality_dh_vacuous()
gate(
    "ADF6 DH control dies before the family/special-fiber question",
    "NO surface S^2/Z" in arch_dh
    and "NO family-of-surfaces" in arch_dh
    and "no special fiber" in card_dh,
    "control has no H1, no surface, no family, no closed point cardinality",
)


family_carrier_with_finite_special_fiber_constructed = False
carrier_native_constant_field_constructed = False
closed_point_finite_residue_cardinality_constructed = False
frobenius_base_size_constructed = False
archimedean_radius_marker_constructed = False
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
    "ADF7 no End(S^2/Z) square/Rosati/R1 data is constructed",
    not family_carrier_with_finite_special_fiber_constructed
    and not carrier_native_constant_field_constructed
    and not closed_point_finite_residue_cardinality_constructed
    and not frobenius_base_size_constructed
    and not archimedean_radius_marker_constructed
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
    "family/N/M(N)=W is real, but finite q and square correspondence data are absent",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (ADF1-ADF7)")
print(
    "VERDICT: the archimedean degenerating family supplies nearby-cycle "
    "N and M(N)=W, but its closed point has residue field C rather than "
    "a finite F_q.  Without a carrier-native finite |kappa|=q, there is "
    "no Frobenius/base-size marker for q^{w/2}, and no square-side "
    "correspondence, DD.4 weight>=1 datum, or positive Rosati is built."
)
