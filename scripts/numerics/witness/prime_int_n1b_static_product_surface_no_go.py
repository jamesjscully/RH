"""Static product surface / Kunneth factorization witness.

After doc 200, a tempting carrier-native repair is to take the second
dimension literally: use the static product surface S x S, read the
middle Kunneth slot H^1(S) x H^1(S), and promote that product slot to the
missing square correspondence object.

This witness records why that is not construction-grade.  The product
surface Kunneth cross slot is exactly A tensor P + P tensor A, so the
archimedean factor is the same DH-shared one-place form and the Euler
variation is inherited from the base prime form.  The smooth product
surface also has N=0: it has rank room for monodromy but no degeneration.
The nonzero N lives on an external degenerating family with a special
fiber, not on the static surface.  No indecomposable correspondence,
square-side iota/properness, positive Rosati, or R1 boundary data is built.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_static_product_surface_no_go
"""

import numpy as np

from scripts.numerics.witness.square_representability import (
    base_grams,
    kunneth_cross_slot,
    plant_offline_in_prime_form,
    regularized_self_intersection,
    signature,
)
from scripts.numerics.witness.surface_archimedean_N import (
    check_A_smooth_surface_pure,
    check_B_room_vs_usage,
    check_C_family_supplies,
    check_D_dh_vacuous,
)


failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


centers = [0.0, np.log(2), np.log(3), np.log(5), np.log(7)]
width = 0.5

A_z, P_z = base_grams("zeta", centers, width)
A_d, P_d = base_grams("dh", centers, width)

C_z = kunneth_cross_slot(A_z, P_z)
C_d = kunneth_cross_slot(A_d, P_d)

explicit_C_z = np.kron(A_z, P_z) + np.kron(P_z, A_z)
explicit_C_d = np.kron(A_d, P_d) + np.kron(P_d, A_d)

gate(
    "SPS1 product Kunneth cross slot is a tensor expression",
    np.max(np.abs(C_z - explicit_C_z)) < 1e-12
    and np.max(np.abs(C_d - explicit_C_d)) < 1e-12,
    "C = A tensor P + P tensor A; no extra square datum enters",
)


arch_shared = float(np.max(np.abs(A_z - A_d)))
gate(
    "SPS2 archimedean factor is DH-shared",
    arch_shared == 0.0,
    f"max|A_zeta-A_DH|={arch_shared}",
)


cross_diff = float(np.max(np.abs(C_z - C_d)))
P_diff = float(np.max(np.abs(P_z - P_d)))
A_norm = float(np.linalg.norm(A_z, 2))
factorizes = cross_diff <= 2 * A_norm * P_diff + 1e-9
gate(
    "SPS3 Euler variation is inherited from the base prime form",
    factorizes and cross_diff > 0 and P_diff > 0,
    f"cross_diff={cross_diff:.6g}, bound={2 * A_norm * P_diff:.6g}",
)


sig_Cz, _ = signature(C_z)
P_off = plant_offline_in_prime_form(P_z, centers, width, rho0=(0.6, 14.0))
P_on = plant_offline_in_prime_form(P_z, centers, width, rho0=(0.5, 14.0))
sig_off, _ = signature(kunneth_cross_slot(A_z, P_off))
sig_on, _ = signature(kunneth_cross_slot(A_z, P_on))
gate(
    "SPS4 product slot does not distinguish on-line from off-line input",
    sig_off == sig_on and sig_off != sig_Cz,
    f"base perturbation moves signature to {sig_off}, same for on/off line",
)


reg1 = regularized_self_intersection(width=1.0, eps=1e-3)
reg2 = regularized_self_intersection(width=1.0, eps=1e-4)
gate(
    "SPS5 Delta self-intersection has only universal corner regularization",
    abs(reg1["finite_part"] - reg2["finite_part"]) < 2e-4
    and reg2["coulomb_tail"] > reg1["coulomb_tail"],
    f"finite parts {reg1['finite_part']:.6f}, {reg2['finite_part']:.6f}; "
    f"tails {reg1['coulomb_tail']:.3f}, {reg2['coulomb_tail']:.3f}",
)


smooth = check_A_smooth_surface_pure(q=4.0)
gate(
    "SPS6 smooth product surface is pure with N=0",
    smooth["kunneth"]["pure_weight2"]
    and smooth["kunneth"]["all_modulus_q"]
    and smooth["monodromy"]["single_weight"]
    and not smooth["monodromy"]["admits_symmetric_split"],
    f"M(N)={smooth['monodromy']['M(N)_graded']}",
)


room_rows = check_B_room_vs_usage()
gate(
    "SPS7 rank room exists but is unused on the smooth surface",
    all(row["room_for_Jordan2 (>=2)"] for row in room_rows)
    and all(not row["split_realized_on_smooth_fiber"] for row in room_rows),
    "room is a rank fact; usage needs a degeneration",
)


family = check_C_family_supplies()
gate(
    "SPS8 nonzero N belongs to a degenerating family, not the static surface",
    family["admits_symmetric_split"] and family["requires_special_fiber"],
    f"family M(N)={family['M(N)_graded (centre w=2)']}",
)


dh_msg = check_D_dh_vacuous()
gate(
    "SPS9 DH has no product-surface carrier to degenerate",
    "NO surface S^2/Z" in dh_msg,
    "control dies before the surface, but this does not construct zeta correspondences",
)


indecomposable_correspondence_defined = False
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
    "SPS10 no indecomposable square correspondence or R1 boundary data is built",
    not indecomposable_correspondence_defined
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
    "static S x S is product Kunneth data, not End(S^2/Z)",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (SPS1-SPS10)")
print(
    "VERDICT: the static product surface supplies the second dimension only "
    "as product Kunneth data.  Its cross slot factors through the one-place "
    "archimedean and prime forms, the smooth surface has N=0, and the "
    "nonzero N lives on an external degeneration.  A surviving route must "
    "construct an indecomposable square correspondence/family carrier."
)
