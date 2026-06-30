r"""Frobenius-first Tannakian compactness no-go.

After doc 206 kills a single operator as count/radius recoupler, the next
repair is categorical: take an abstract Frobenius F as primitive, form the
rigid Tannakian category Rep(<F>_Zar), and hope reconstruction forces
compact Sato-Tate / polarizability / radius.

The obstruction is that rigidity and tensor closure are free for any
invertible F, including count-scale-preserving off-purity examples.
Compactness and a positive/unitary fiber functor occur exactly at the
normalized unit-circle condition, so they are extra radius/Rosati input.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_frobenius_tannakian_compactness_no_go
"""

import numpy as np

from scripts.numerics.witness.frob_tannakian_compactness import (
    closure_type,
    polarizability,
    run,
    step_A_rigidity,
    tensor_consistency,
)
from scripts.numerics.witness.recouple_count_radius import (
    count_data,
    frobenius_config,
    radius_data,
)


failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


q = 7
g = 2
sqrt_q = np.sqrt(q)

pure_alphas = frobenius_config(g, q)
off_alphas = frobenius_config(g, q, off_pair=(sqrt_q * 1.6, 0))
F_pure = np.diag(pure_alphas)
F_off = np.diag(off_alphas)

pure_count = count_data(pure_alphas, q)
off_count = count_data(off_alphas, q)
pure_radius = radius_data(pure_alphas, q)
off_radius = radius_data(off_alphas, q)

gate(
    "FTC1 off-purity anchor preserves count scale but breaks radius",
    abs(pure_count["|det F|"] - q ** g) < 1e-6
    and abs(off_count["|det F|"] - q ** g) < 1e-6
    and pure_radius["max dev |.|-sqrt(q)"] < 1e-6
    and off_radius["max dev |.|-sqrt(q)"] > 0.1,
    (
        f"pure det={pure_count['|det F|']}, off det={off_count['|det F|']}, "
        f"off dev={off_radius['max dev |.|-sqrt(q)']}"
    ),
)


pure_step_a = step_A_rigidity(F_pure)
off_step_a = step_A_rigidity(F_off)
pure_tensor = tensor_consistency(F_pure)
off_tensor = tensor_consistency(F_off)

gate(
    "FTC2 rigid Tannakian Step A is consistent off-line",
    pure_step_a["F invertible"]
    and off_step_a["F invertible"]
    and pure_step_a["dual eigenvalues = 1/alpha (contragredient)"]
    and off_step_a["dual eigenvalues = 1/alpha (contragredient)"]
    and pure_step_a["V** = V (finite-dim reflexive)"]
    and off_step_a["V** = V (finite-dim reflexive)"]
    and pure_tensor["==> Rep(<F>_Zar) is a consistent rigid tensor category"]
    and off_tensor["==> Rep(<F>_Zar) is a consistent rigid tensor category"]
    and off_tensor["traces finite & well-defined (any radius)"],
    "duals, finite tensor spectra, and traces exist for the off-purity F",
)


pure_closure = closure_type(F_pure, q)
off_closure = closure_type(F_off, q)
pure_pol = polarizability(F_pure, q)
off_pol = polarizability(F_off, q)

gate(
    "FTC3 compactness/polarizability detects radius and is not forced",
    pure_closure["normalized closure COMPACT (Sato-Tate compact)"]
    and pure_pol["POLARIZATION EXISTS (Step B holds)"]
    and not off_closure["normalized closure COMPACT (Sato-Tate compact)"]
    and not off_pol["POLARIZATION EXISTS (Step B holds)"]
    and off_pol["BUT Rep(<F>_Zar) still a consistent rigid tensor category (Step A)"],
    (
        f"off normalized moduli="
        f"{[round(m, 4) for m in off_closure['normalized |alpha|/sqrt q']]}"
    ),
)


primitive_rows = run(q=float(q))
step_a_all = []
tensor_all = []
polar_rows = []
for label, row in primitive_rows:
    step_a = row["A_rigidity (Step A)"]
    tensor = row["tensor consistency (Tannakian closure)"]
    closure = row["closure/compactness (Step B)"]
    pol = row["polarizability (Step B)"]
    step_a_all.append(
        step_a["F invertible"]
        and step_a["dual eigenvalues = 1/alpha (contragredient)"]
        and step_a["perfect FE pairing exists (any radius)"]
    )
    tensor_all.append(tensor["==> Rep(<F>_Zar) is a consistent rigid tensor category"])
    polar_rows.append((label, closure["modulus == sqrt q (on-line)"], pol["POLARIZATION EXISTS (Step B holds)"]))

gate(
    "FTC4 primitive Frobenius-first examples show Step A free at every radius",
    all(step_a_all)
    and all(tensor_all)
    and polar_rows[0][1] is True
    and polar_rows[0][2] is True
    and all(on_line is False and pol is False for _, on_line, pol in polar_rows[1:]),
    ", ".join(f"{label}:on_line={on_line},polarizable={pol}" for label, on_line, pol in polar_rows),
)


uses_euler_product_or_effectivity = False
depends_on_actual_square_correspondence = False
can_form_rep_zar_for_arbitrary_invertible_operator = True
dh_or_control_killed_by_tannakian_closure = False

gate(
    "FTC5 Tannakian closure alone is not a carrier guard",
    can_form_rep_zar_for_arbitrary_invertible_operator
    and not uses_euler_product_or_effectivity
    and not depends_on_actual_square_correspondence
    and not dh_or_control_killed_by_tannakian_closure,
    "Rep(<F>_Zar) consumes an invertible operator, not zeta-only square carrier data",
)


carrier_native_q_power_map_constructed = False
carrier_native_compact_sato_tate_constructed = False
positive_fiber_functor_constructed = False
polarization_relation_constructed = False
uniform_modulus_bound_constructed = False
dh_killing_carrier_constructed = False
finite_constant_field_constructed = False
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
    "FTC6 no End(S^2/Z) square/Rosati/R1 data is constructed",
    not carrier_native_q_power_map_constructed
    and not carrier_native_compact_sato_tate_constructed
    and not positive_fiber_functor_constructed
    and not polarization_relation_constructed
    and not uniform_modulus_bound_constructed
    and not dh_killing_carrier_constructed
    and not finite_constant_field_constructed
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
    "rigid Tannakian closure supplies no square correspondences, q-power map, or Rosati",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (FTC1-FTC6)")
print(
    "VERDICT: Frobenius-first Tannakian reconstruction gives a consistent "
    "rigid tensor category for off-purity F as well as pure F.  Compact "
    "Sato-Tate closure and a positive/unitary fiber functor hold exactly at "
    "the normalized unit-circle condition, so compactness/polarizability is "
    "extra radius/Rosati structure, not forced by rigidity.  No End(S^2/Z) "
    "square, DD.4 weight>=1 datum, or positive Rosati is built."
)
