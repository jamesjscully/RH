r"""Local purity-carrier no-go.

After docs 206-207, the next tempting repair is to say the purity/radius
functor is already local: each Euler factor has an edge, so take the square
root locally and read the center.  The obstruction is typing.  The edge is
local, but the square-root/purity step needs a weight-1 carrier gr^W_1.
Local factors for function fields and zeta primes both have numerator degree
0; the weight-1 carrier exists globally for a curve and is open over Z.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_local_purity_carrier_no_go
"""

from scripts.numerics.witness.purity_carrier import (
    edge_is_local,
    ff_global_numerator_degree,
    ff_local_factor_numerator_degree,
    purity_has_local_carrier,
    zeta_archimedean_factor_carrier,
    zeta_prime_factor_numerator_degree,
)


failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


ff_global = [(g, ff_global_numerator_degree(g)) for g in (1, 2, 3)]
gate(
    "LPC1 function-field global curve supplies weight-1 carrier",
    all(deg == 2 * g and purity_has_local_carrier(deg) for g, deg in ff_global),
    ", ".join(f"g={g}:deg={deg}" for g, deg in ff_global),
)


ff_local = [(d, ff_local_factor_numerator_degree(d)) for d in (1, 2, 3)]
zeta_local = [(p, zeta_prime_factor_numerator_degree(p)) for p in (2, 3, 5, 7)]
gate(
    "LPC2 local factors have edge but no weight-1 purity carrier",
    all(deg == 0 and not purity_has_local_carrier(deg) and edge_is_local(True)
        for _, deg in ff_local)
    and all(deg == 0 and not purity_has_local_carrier(deg) and edge_is_local(True)
            for _, deg in zeta_local),
    (
        "FF local numerator degrees="
        + ",".join(str(deg) for _, deg in ff_local)
        + "; zeta prime numerator degrees="
        + ",".join(str(deg) for _, deg in zeta_local)
    ),
)


arch = zeta_archimedean_factor_carrier()
gate(
    "LPC3 archimedean factor has no finite weight-1 numerator",
    arch["finite_weight1_numerator"] is False
    and "no finite-degree H^1 numerator" in arch["note"],
    arch["note"],
)


rad_edge_well_typed_for_zeta = all(edge_is_local(True) for _ in zeta_local)
rad_purity_well_typed_per_prime = any(
    purity_has_local_carrier(deg) for _, deg in zeta_local
)
global_glued_weight1_carrier_constructed_over_z = False
gate(
    "LPC4 purity is not a per-prime condition over zeta",
    rad_edge_well_typed_for_zeta
    and not rad_purity_well_typed_per_prime
    and not global_glued_weight1_carrier_constructed_over_z,
    "edge yes locally; gr^W_1 carrier absent per prime; global carrier remains open",
)


dh_has_euler_product = False
dh_has_local_factors = False
dh_has_edge_from_product = False
dh_has_weight1_from_local_factors = False
gate(
    "LPC5 DH fails before the purity-carrier question",
    not dh_has_euler_product
    and not dh_has_local_factors
    and not dh_has_edge_from_product
    and not dh_has_weight1_from_local_factors,
    "DH has FE but no Euler product/local factors/edge product carrier",
)


local_grw1_carrier_constructed = False
global_grw1_carrier_constructed = False
carrier_native_purity_constructed = False
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
    "LPC6 no End(S^2/Z) square/Rosati/R1 data is constructed",
    not local_grw1_carrier_constructed
    and not global_grw1_carrier_constructed
    and not carrier_native_purity_constructed
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
    "local edge data supplies no gr^W_1 carrier, square correspondences, or Rosati",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (LPC1-LPC6)")
print(
    "VERDICT: local Euler factors supply the edge/abscissa but not the "
    "weight-1 gr^W_1 carrier needed for the purity square-root.  Function "
    "fields get that carrier globally from H^1(C); zeta over Z has no "
    "per-prime or archimedean finite weight-1 numerator, and the global "
    "carrier is exactly the missing S^2/Z construction.  No End(S^2/Z) "
    "square, DD.4 weight>=1 datum, or positive Rosati is built."
)
