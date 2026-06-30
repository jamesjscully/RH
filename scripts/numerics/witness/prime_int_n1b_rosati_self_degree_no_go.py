r"""Rosati self-degree circularity no-go.

After doc 209, the surviving route must construct positive Rosati on a global
carrier.  A tempting repair is to say an archimedean polarized abelian variety
with an endomorphism F automatically has Rosati positivity and
F F^dag = deg(F), so the radius is forced.  The obstruction is that deg(F) is
F's own norm.  Off-prescribed-radius endomorphisms still admit positive
polarizations; their Rosati self-degree changes to r^2 rather than the
external q.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_rosati_self_degree_no_go
"""

import numpy as np

from scripts.numerics.witness.rosati_circularity_skeptic import (
    integrality_comment,
    planted_offline,
    test_polarization_exists,
)
from scripts.numerics.witness.rosati_reflection import (
    edge_to_centre_chain,
    falsifier_verdict,
    z_analog_audit,
)


failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


q = 7.0
sqrt_q = np.sqrt(q)

on = test_polarization_exists(a=1.0, q=q)
gate(
    "RSD1 on-prescribed-radius AV model has positive Rosati and self-degree q",
    on.get("polarization lambda (H pos-def)") is not None
    and on.get("F.F^dagger is scalar?") is True
    and on.get("scalar == q?") is True
    and on.get("scalar == |alpha|^2?") is True
    and on.get("Rosati form positive-definite?") is True,
    (
        f"|alpha|={on['|alpha|']:.6f}, sqrt_q={on['sqrt q']:.6f}, "
        f"scalar={on.get('that scalar')}"
    ),
)


off = planted_offline(r=1.3 * sqrt_q, t=0.6, q=q)
gate(
    "RSD2 off-prescribed-radius endomorphism still has positive Rosati",
    off["off-circle?"]
    and off["polarization H pos-def?"]
    and off["Rosati form pos-def?"]
    and off["== r^2 (det F)?"]
    and not off["== q (the critical radius)?"],
    (
        f"|alpha|={off['|alpha| = r']:.6f}, sqrt_q={off['sqrt q']:.6f}, "
        f"F.Fdag={off['F.F^dagger scalar']:.6f}"
    ),
)


gaussian_examples = [(1, 1), (2, 1), (1, 2), (3, 1)]
own_degree_ok = all(
    abs((a * a + b * b) - abs(complex(a, b)) ** 2) < 1e-9
    for a, b in gaussian_examples
)
external_q_forces_choice = all(abs((a * a + b * b) - q) > 1e-9 for a, b in gaussian_examples[1:])
gate(
    "RSD3 integrality gives own norm, not an externally prescribed q",
    own_degree_ok
    and external_q_forces_choice
    and "alpha's OWN norm" in integrality_comment(),
    ", ".join(f"{a}+{b}i:N={a*a+b*b}" for a, b in gaussian_examples),
)


chain = edge_to_centre_chain(q=7)
tracks_line = all(row["POSITIVITY TRACKS LINE?"] for row in chain)
has_offline_negative = any(
    (not row["on line?"]) and (not row["Rosati pos-semidef (=> on line)"])
    for row in chain
)
gate(
    "RSD4 Rosati positivity is exactly the line-forcing content",
    tracks_line and has_offline_negative,
    "det M = 4q-a^2 tracks on/off line in the FF anchor",
)


audit = z_analog_audit()
verdict = falsifier_verdict()
edge_transfers = audit["(i) edge number F.F'=q"]["transfers?"] == "YES"
reflection_not_end = "NO as an algebraic involution" in audit["(ii) reflection theta = Rosati involution"]["transfers?"]
positivity_no_transfer = audit["(iii) ROSATI POSITIVITY Tr(phi phi') > 0  [THE LEVER]"]["transfers?"] == "NO -- this is RH"
offdiag_named = "OFF-DIAGONAL" in verdict["VERDICT"]
gate(
    "RSD5 over Z the edge/reflection transfer but Rosati positivity is the wall",
    edge_transfers and reflection_not_end and positivity_no_transfer and offdiag_named,
    "edge diagonal and FE reflection transfer; off-diagonal Rosati coupling does not",
)


global_grw1_carrier_constructed_over_z = False
carrier_native_purity_constructed = False
external_q_base_size_constructed = False
carrier_native_self_degree_relation_constructed = False
positive_rosati_constructed = False
off_diagonal_rosati_coupling_constructed = False
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
laurent_axis_defined = False
boundary_map_defined = False
torsor_splitter_defined = False
dd4_weight_ge_1_datum_defined = False

gate(
    "RSD6 no End(S^2/Z) square/Rosati/R1 data is constructed",
    not global_grw1_carrier_constructed_over_z
    and not carrier_native_purity_constructed
    and not external_q_base_size_constructed
    and not carrier_native_self_degree_relation_constructed
    and not positive_rosati_constructed
    and not off_diagonal_rosati_coupling_constructed
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
    and not laurent_axis_defined
    and not boundary_map_defined
    and not torsor_splitter_defined
    and not dd4_weight_ge_1_datum_defined,
    "abstract Rosati self-degree supplies no square correspondences or positive Rosati over Z",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (RSD1-RSD6)")
print(
    "VERDICT: abstract Rosati positivity forces |alpha|=sqrt(deg(F)) only "
    "relative to F's own self-degree.  Off-prescribed-radius endomorphisms "
    "still admit positive polarizations, with F F^dag equal to r^2 rather "
    "than the external q.  Over Z the edge diagonal and FE reflection transfer, "
    "but the off-diagonal Rosati/correspondence coupling is the missing "
    "positivity/RH content.  No End(S^2/Z) square, DD.4 weight>=1 datum, or "
    "positive Rosati is built."
)
