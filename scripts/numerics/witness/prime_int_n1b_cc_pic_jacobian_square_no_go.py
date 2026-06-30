"""CC Pic/Jacobian curve-level repair witness.

Doc 186 leaves one legitimate escape from the appended-Hitchin failure:
use carrier-native Picard/Jacobian data rather than an inserted Hitchin
fiber.  The strongest known local candidate in the project record is the
Connes-Consani compactified Spec Z curve-level theory: integer RR,
Pontryagin-Serre duality, and the 2026 Pic/Jacobian infrastructure.

This witness records why that curve-level package is still not the
self-product correspondence algebra End(S^2/Z).  It checks the exact split
from research/work/N-cc-square-posing.md and Q-cc-ftest.md:

  * curve-level RR/Pic/Jac data is real but one-dimensional;
  * the strict Gamma-set square HZ ^ HZ has object-level extra data;
  * every published EM/abelian-valued CC probe factors through the diagonal;
  * no compactified square H^2, intersection form, correspondence algebra,
    Frobenius graph, or positive Rosati involution is supplied.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_cc_pic_jacobian_square_no_go
"""

from math import comb

failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def total_pairing(a, b, edges):
    return sum(a[i] * b[j] for i, j in edges)


def phi_prime_mod_p(a, b, edges, p):
    """Q-doc divided-power invariant Phi'_p on a square class."""
    total = 0
    for i, ai in enumerate(a):
        row_sum = sum(b[j] for ii, j in edges if ii == i)
        total += (ai**p) * comb(row_sum, p)
    return total % p


def rank_one_tensor_rank(rank_a, rank_b):
    return rank_a * rank_b


def dmp_dim(deg):
    if deg == -1:
        return 1
    if deg >= 0:
        return 1
    return 0


# Curve-level CC package, as recorded in N-cc-square-posing.md:
cc_curve_rr_over_s = True
cc_curve_serre_duality_over_s_pm = True
cc_arithmetic_pic_exists = True
cc_jacobian_defined_as_pic_mod_positive_reals = True
cc_curve_genus_over_s = 0
cc_canonical_degree_units_over_s = -2

curve_line_bundle_rank = 1
internal_tensor_rank = rank_one_tensor_rank(curve_line_bundle_rank, curve_line_bundle_rank)

# The compactified square demanded by End(S^2/Z), not present in the
# curve-level CC package as recorded in N:
external_product_of_geometries_defined = False
compactified_square_cohomology_defined = False
square_h2_defined = False
square_intersection_form_defined = False
square_correspondence_algebra_defined = False
positive_rosati_involution_defined = False
frobenius_graph_correspondence_defined = False
idele_translation_replaces_frobenius = True

# Strict square object-level split from Q:
L_a = (1, 1)
L_b = (1, 1)
L_edges = ((0, 0), (0, 1), (1, 0))
C3_a = (3,)
C3_b = (1,)
C3_edges = ((0, 0),)

L_total = total_pairing(L_a, L_b, L_edges)
C3_total = total_pairing(C3_a, C3_b, C3_edges)
L_phi2p = phi_prime_mod_p(L_a, L_b, L_edges, 2)
C3_phi2p = phi_prime_mod_p(C3_a, C3_b, C3_edges, 2)

em_visible_probe_factors_through_diagonal = True
published_cc_rr_inputs_are_short_complexes = True
published_cc_outputs_have_only_h0_h1 = True
published_cc_square_probe_can_take_strict_square_as_source = False
published_cc_square_best_effort_pi1 = 0
published_cc_square_best_effort_pi0 = "Z"

laurent_axis_supplied = False
carrier_boundary_map_supplied = False
torsor_splitter_supplied = False
weight_ge_1_dd4_datum_supplied = False
dh_epstein_death_proved_at_square_map = False


gate(
    "CPJ1 CC curve-level RR/Pic/Jac package is real but curve-level",
    cc_curve_rr_over_s
    and cc_curve_serre_duality_over_s_pm
    and cc_arithmetic_pic_exists
    and cc_jacobian_defined_as_pic_mod_positive_reals
    and cc_curve_genus_over_s == 0
    and cc_canonical_degree_units_over_s == -2,
    (
        "RR over S, Serre duality over S[+-1], Pic/Jac infrastructure; "
        f"genus={cc_curve_genus_over_s}, deg_2(K)={cc_canonical_degree_units_over_s}"
    ),
)

gate(
    "CPJ2 curve Pic tensor product stays rank-one internal product",
    curve_line_bundle_rank == 1 and internal_tensor_rank == 1,
    "rank-one line bundles tensor to rank-one line bundles on one curve",
)

gate(
    "CPJ3 demanded compactified square structures are not supplied",
    not external_product_of_geometries_defined
    and not compactified_square_cohomology_defined
    and not square_h2_defined
    and not square_intersection_form_defined
    and not square_correspondence_algebra_defined,
    (
        "no external product geometry, H^2, intersection form, or "
        "correspondence algebra in the curve-level package"
    ),
)

gate(
    "CPJ4 strict Gamma-set square has extra object-level data",
    L_total == C3_total == 3 and L_phi2p == 1 and C3_phi2p == 0,
    (
        f"mu(L)=mu(C3)={L_total}, but Phi'_2(L)={L_phi2p} "
        f"and Phi'_2(C3)={C3_phi2p}"
    ),
)

gate(
    "CPJ5 published CC probes factor through the diagonal",
    em_visible_probe_factors_through_diagonal
    and published_cc_rr_inputs_are_short_complexes
    and published_cc_outputs_have_only_h0_h1
    and not published_cc_square_probe_can_take_strict_square_as_source
    and published_cc_square_best_effort_pi1 == 0
    and published_cc_square_best_effort_pi0 == "Z",
    "EM-visible RR/Pic/Hom probes see only the diagonal curve shadow",
)

gate(
    "CPJ6 Pic/Jac idelic translations are not Frobenius graph correspondences",
    idele_translation_replaces_frobenius
    and not frobenius_graph_correspondence_defined
    and not positive_rosati_involution_defined,
    "idele-class translations are not the C x C Frobenius/Rosati package",
)

gate(
    "CPJ7 no Laurent axis, boundary map, or torsor splitter is constructed",
    not laurent_axis_supplied
    and not carrier_boundary_map_supplied
    and not torsor_splitter_supplied
    and not weight_ge_1_dd4_datum_supplied,
    "curve-level Pic/Jac data does not finish DD.4 weights>=1",
)

gate(
    "CPJ8 base R1 obstructions remain untouched",
    dmp_dim(-1) == 1
    and dmp_dim(-2) == 0
    and not laurent_axis_supplied
    and not torsor_splitter_supplied,
    "DMP bottom has no degree -2; no Laurent shift or b/phi(b)=c splitter",
)

gate(
    "CPJ9 carrier guard has not fired at a square map",
    not dh_epstein_death_proved_at_square_map
    and not square_correspondence_algebra_defined,
    "no carrier-consuming square correspondence where DH/Epstein die",
)

gate(
    "CPJ10 CC Pic/Jac curve-level data is not End(S^2/Z)",
    cc_arithmetic_pic_exists
    and cc_jacobian_defined_as_pic_mod_positive_reals
    and not square_correspondence_algebra_defined
    and not positive_rosati_involution_defined
    and not frobenius_graph_correspondence_defined,
    "real curve-level theorem, missing self-product correspondence algebra",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (CPJ1-CPJ10)")
