r"""Single-Frobenius count/radius recoupling no-go.

After doc 205, the next repair is to ask for one archimedean Frobenius-like
operator F_inf that does both jobs finite-field Frobenius does:

    count  = trace/Lefschetz data
    radius = eigenvalue modulus/purity data

The obstruction is that the finite-field coupling is not trace alone.  The
count scale supplies |det F|=q^g, while radius/purity is the stronger
polarization relation F F^dag=q Id.  At infinity there is no q-power ring
endomorphism that is both fixed-point/counting map and scaling map; graded
repairs split count into a unitary factor and radius into a free scalar.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_single_frobenius_recoupling_no_go
"""

import math

from scripts.numerics.witness.recouple_count_radius import (
    attempt_A_count_determines_radius,
    attempt_B_qpower_ring_endomorphism,
    attempt_C_graded_repair,
    count_data,
    dh_vacuous,
    frobenius_config,
    radius_data,
)


failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


g = 2
q = 7
sqrt_q = math.sqrt(q)
pure = frobenius_config(g, q)
off = frobenius_config(g, q, off_pair=(sqrt_q * 1.6, 0))

pure_count = count_data(pure, q)
off_count = count_data(off, q)
pure_radius = radius_data(pure, q)
off_radius = radius_data(off, q)

gate(
    "SFR1 finite-field anchor separates count scale from radius",
    abs(pure_count["|det F|"] - q ** g) < 1e-6
    and abs(off_count["|det F|"] - q ** g) < 1e-6
    and pure_radius["max dev |.|-sqrt(q)"] < 1e-6
    and off_radius["max dev |.|-sqrt(q)"] > 0.1,
    (
        f"pure det={pure_count['|det F|']}, off det={off_count['|det F|']}, "
        f"pure dev={pure_radius['max dev |.|-sqrt(q)']}, "
        f"off dev={off_radius['max dev |.|-sqrt(q)']}"
    ),
)


attempt_a = attempt_A_count_determines_radius(off, q)
gate(
    "SFR2 determinant/count scale gives geometric mean, not uniform modulus",
    attempt_a["det F = q^g (count-scale)?"]
    and attempt_a["equals sqrt(q)?"]
    and not attempt_a["BUT individual |alpha_i| all = sqrt(q)?"],
    (
        f"geom_mean={attempt_a['geometric-mean modulus (det)^{1/2g}']}, "
        f"uniform={attempt_a['BUT individual |alpha_i| all = sqrt(q)?']}"
    ),
)


attempt_b = attempt_B_qpower_ring_endomorphism()
gate(
    "SFR3 no archimedean q-power ring endomorphism fuses count and scale",
    attempt_b["ALL archimedean field-automorphism moduli = 1?"]
    and not attempt_b["the SCALING (modulus character) is a field endomorphism?"]
    and attempt_b["continuous field endos of R"] == ["identity"]
    and attempt_b["continuous field endos of C"] == ["identity", "conjugation"],
    "field automorphisms are isometries; modulus scaling is not a field endomorphism",
)


attempt_c = attempt_C_graded_repair(g, q, off=True)
true_moduli = attempt_c["F_inf = m * U, eig moduli with m=sqrt(q)"]
wrong_moduli = attempt_c["F_inf eig moduli with WRONG m"]
gate(
    "SFR4 graded/tensor repair separates count from radius",
    all(abs(m - 1.0) < 1e-6 for m in attempt_c["U unitary (count/phase carrier), |eig U|"])
    and attempt_c["is the count Tr(U^n) changed by m?"] is False
    and attempt_c["=> m (the RADIUS) is determined by the count?"] is False
    and max(abs(a - b) for a, b in zip(true_moduli, wrong_moduli)) > 1.0,
    (
        f"true_moduli={true_moduli}, wrong_moduli={wrong_moduli}, "
        "Tr(U^n) is m-independent"
    ),
)


dh_text = dh_vacuous()
gate(
    "SFR5 DH-vacuity: no Euler product means no Frobenius count-source",
    "no Euler product" in dh_text
    and "no Frobenius" in dh_text
    and "no operator F" in dh_text,
    dh_text,
)


carrier_native_q_power_map_constructed = False
single_frobenius_count_radius_operator_constructed = False
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
    "SFR6 no End(S^2/Z) square/Rosati/R1 data is constructed",
    not carrier_native_q_power_map_constructed
    and not single_frobenius_count_radius_operator_constructed
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
    "single-operator recoupling supplies no q-power map, polarization, square, or Rosati",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (SFR1-SFR6)")
print(
    "VERDICT: a single archimedean Frobenius-style operator does not recouple "
    "count and radius.  The count fixes determinant/geometric mean, not "
    "uniform modulus; archimedean field automorphisms are isometries rather "
    "than q-power maps; and graded repairs split count from the scalar radius. "
    "Forcing F F^dag=q Id is exactly the missing polarization/Rosati input. "
    "No End(S^2/Z) square, DD.4 weight>=1 datum, or positive Rosati is built."
)
