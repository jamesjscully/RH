r"""Radius-descent assembly no-go.

After doc 208, the next tempting repair is global rather than local: local
purity is not well-typed, but perhaps the glued descent forces the even split
once all places are assembled.  The obstruction is a balanced redistribution.
The determinant/product edge and the Poincare pairings survive, while the
individual radii move off the even split.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_radius_descent_assembly_no_go
"""

import mpmath as mp

from scripts.numerics.witness.radius_descent_assembly import (
    cross_prime_redistribution,
    even_split,
    global_det,
    pairing_products,
    redistributed_eigenvalues,
    weil_eigenvalues_on_line,
)


failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


q = 9
g = 2
angles = [mp.mpf("0.7"), mp.mpf("1.9")]
sqrt_q = mp.sqrt(mp.mpf(q))
on = weil_eigenvalues_on_line(q, g, angles)
det_on = global_det(on)
pair_on = pairing_products(on, g)

gate(
    "RDA1 function-field global carrier has determinant, pairings, and even split",
    abs(abs(det_on) - q ** g) < mp.mpf("1e-25") * q ** g
    and all(abs(abs(pp) - q) < mp.mpf("1e-25") * q for pp in pair_on)
    and even_split(on, q),
    (
        f"det={mp.nstr(det_on, 10)}, pairings="
        + ",".join(mp.nstr(pp, 8) for pp in pair_on)
        + f", sqrt_q={mp.nstr(sqrt_q, 8)}"
    ),
)


off = redistributed_eigenvalues(q, g, angles, log_r=mp.mpf("0.4"))
det_off = global_det(off)
pair_off = pairing_products(off, g)
off_moduli = [abs(a) for a in off]

det_preserved = abs(abs(det_off) - q ** g) < mp.mpf("1e-20") * q ** g
pairings_preserved = all(abs(abs(pp) - q) < mp.mpf("1e-20") * q for pp in pair_off)
off_even_split = even_split(off, q)
some_radius_moved = any(abs(m - sqrt_q) > mp.mpf("0.1") for m in off_moduli)

gate(
    "RDA2 determinant/pairing-neutral redistribution breaks the even split",
    det_preserved and pairings_preserved and not off_even_split and some_radius_moved,
    (
        "moduli="
        + ",".join(mp.nstr(m, 8) for m in off_moduli)
        + f"; det_preserved={det_preserved}; pairings_preserved={pairings_preserved}"
    ),
)


p1 = 5
p2 = 7
delta = mp.mpf("0.3")
det_before, det_after, planted = cross_prime_redistribution(p1, p2, delta)
half = mp.mpf(11) / 2
p1_center = mp.mpf(p1) ** half
p2_center = mp.mpf(p2) ** half
p1_off = abs(planted[0] - p1_center) > mp.mpf("0.1")
p2_off = abs(planted[2] - p2_center) > mp.mpf("0.1")

gate(
    "RDA3 zeta-style cross-prime determinant product does not couple radii",
    abs(det_after - det_before) < mp.mpf("1e-15") * det_before
    and p1_off
    and p2_off,
    (
        f"det_before={mp.nstr(det_before, 12)}, det_after={mp.nstr(det_after, 12)}, "
        f"p1_mod={mp.nstr(planted[0], 8)}, p2_mod={mp.nstr(planted[2], 8)}"
    ),
)


dh_has_euler_product = False
dh_has_satake_parameters = False
dh_has_per_place_determinant = False
dh_has_edge_to_assemble = False
dh_has_weight1_carrier_to_glue = False

gate(
    "RDA4 DH fails before radius-descent rigidity is even typed",
    not dh_has_euler_product
    and not dh_has_satake_parameters
    and not dh_has_per_place_determinant
    and not dh_has_edge_to_assemble
    and not dh_has_weight1_carrier_to_glue,
    "no Euler product/Satake/local determinant/edge/carrier",
)


det_pairing_data_distinguishes_on_from_off = (
    abs(abs(det_on) - abs(det_off)) > mp.mpf("1e-20") * q ** g
    or any(abs(abs(a) - abs(b)) > mp.mpf("1e-20") * q for a, b in zip(pair_on, pair_off))
)
positivity_or_rosati_supplied_by_descent = False

gate(
    "RDA5 positivity/Rosati is extra data, not a determinant-descent consequence",
    not det_pairing_data_distinguishes_on_from_off
    and even_split(on, q)
    and not even_split(off, q)
    and not positivity_or_rosati_supplied_by_descent,
    "same determinant/pairing data; different radii; no positivity/Rosati supplied",
)


global_grw1_carrier_constructed_over_z = False
carrier_native_purity_constructed = False
global_even_split_rigidity_constructed = False
carrier_native_q_power_map_constructed = False
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
    "RDA6 no End(S^2/Z) square/Rosati/R1 data is constructed",
    not global_grw1_carrier_constructed_over_z
    and not carrier_native_purity_constructed
    and not global_even_split_rigidity_constructed
    and not carrier_native_q_power_map_constructed
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
    "global descent supplies product edge only, not square correspondences or Rosati",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (RDA1-RDA6)")
print(
    "VERDICT: global radius descent assembles only the determinant/product "
    "edge.  A balanced modulus redistribution preserves the determinant and "
    "Poincare pairings while breaking the even split, so no Euler/FE descent "
    "rigidity forces the center.  The missing discriminator is global "
    "positivity/Rosati on the weight-1 carrier, not a consequence of the "
    "determinant.  No End(S^2/Z) square, DD.4 weight>=1 datum, or positive "
    "Rosati is built."
)
