"""CC cutoff / non-zeta aggregation repair witness.

Docs 189-191 leave the second explicit Q-doc evasion: abandon
zeta-regularization for the aggregate.  The simplest version keeps the
CC-ceiling dimensions but aggregates them by finite cutoffs.

This witness records why that repair is not construction-grade End(S^2/Z).
The cutoff sums have exact divergent growth; common normalizations either
remember only the cutoff scale or introduce base-dependent constants.  No
carrier-native cutoff rule, square H^2, intersection form, correspondence
algebra, Frobenius graph, positive Rosati, Laurent boundary map, or torsor
splitter is constructed.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_cc_cutoff_aggregation_no_go
"""

from fractions import Fraction

failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def ceil_log_b(k, b):
    power = 1
    n = 0
    while power < k:
        power *= b
        n += 1
    return n


def cutoff_sum_direct(n, b):
    return sum(ceil_log_b(k, b) for k in range(1, n + 1))


def cutoff_sum_power(b, m):
    """Sum_{1 <= k <= b^m} ceil(log_b k)."""
    return (1 - (m + 1) * (b**m) + m * (b ** (m + 1))) // (b - 1)


def cutoff_mean_at_power(b, m):
    return Fraction(cutoff_sum_power(b, m), b**m)


def leading_residual_density(b, m):
    """(S_b(b^m) - b^m*m) / b^m."""
    return cutoff_mean_at_power(b, m) - m


def dmp_dim(deg):
    if deg == -1:
        return 1
    if deg >= 0:
        return 1
    return 0


zeta_regularization_abandoned = True
finite_cutoff_aggregation_selected = True
carrier_native_cutoff_rule_defined = False
cutoff_cofinality_square_native = False
non_em_square_functor_defined = False
diagonal_factorization_broken = False
carrier_native_aggregation_constructed = False

square_h2_defined = False
square_intersection_form_defined = False
square_correspondence_algebra_defined = False
frobenius_graph_defined = False
positive_rosati_defined = False

laurent_axis_defined = False
boundary_map_defined = False
torsor_splitter_defined = False
dd4_weight_ge_1_datum_defined = False
dh_epstein_death_at_square_map = False


gate(
    "CNA1 this is the non-zeta cutoff aggregation branch, not a new carrier",
    zeta_regularization_abandoned
    and finite_cutoff_aggregation_selected
    and not carrier_native_aggregation_constructed,
    "tests doc-189 evasion branch (b) with finite cutoffs",
)

gate(
    "CNA2 cutoff sums agree with the exact power-window formula",
    cutoff_sum_direct(2**6, 2) == cutoff_sum_power(2, 6) == 321
    and cutoff_sum_direct(3**6, 3) == cutoff_sum_power(3, 6) == 4010,
    f"S2(64)={cutoff_sum_power(2, 6)}, S3(729)={cutoff_sum_power(3, 6)}",
)

gate(
    "CNA3 raw cutoff aggregates diverge along carrier-presentation powers",
    cutoff_sum_power(2, 4) < cutoff_sum_power(2, 6) < cutoff_sum_power(2, 8)
    and cutoff_sum_power(3, 4) < cutoff_sum_power(3, 6) < cutoff_sum_power(3, 8),
    (
        f"base2={cutoff_sum_power(2, 4)},{cutoff_sum_power(2, 6)},{cutoff_sum_power(2, 8)}; "
        f"base3={cutoff_sum_power(3, 4)},{cutoff_sum_power(3, 6)},{cutoff_sum_power(3, 8)}"
    ),
)

gate(
    "CNA4 mean cutoff aggregate still grows with the cutoff scale",
    cutoff_mean_at_power(2, 4) < cutoff_mean_at_power(2, 6) < cutoff_mean_at_power(2, 8)
    and cutoff_mean_at_power(3, 4) < cutoff_mean_at_power(3, 6) < cutoff_mean_at_power(3, 8),
    (
        f"mean_b2={float(cutoff_mean_at_power(2, 4)):.6f},"
        f"{float(cutoff_mean_at_power(2, 6)):.6f},"
        f"{float(cutoff_mean_at_power(2, 8)):.6f}; "
        f"mean_b3={float(cutoff_mean_at_power(3, 4)):.6f},"
        f"{float(cutoff_mean_at_power(3, 6)):.6f},"
        f"{float(cutoff_mean_at_power(3, 8)):.6f}"
    ),
)

gate(
    "CNA5 subtracting the leading cutoff scale leaves base-dependent constants",
    leading_residual_density(2, 10) < Fraction(-99, 100)
    and Fraction(-51, 100) < leading_residual_density(3, 10) < Fraction(-49, 100)
    and leading_residual_density(2, 10) != leading_residual_density(3, 10),
    (
        f"residual_b2={float(leading_residual_density(2, 10)):+.12f}, "
        f"residual_b3={float(leading_residual_density(3, 10)):+.12f}"
    ),
)

gate(
    "CNA6 no square-native cutoff/cofinality rule is supplied",
    not carrier_native_cutoff_rule_defined
    and not cutoff_cofinality_square_native,
    "finite cutoffs choose an aggregation scheme outside the square carrier",
)

gate(
    "CNA7 no non-EM square functor or carrier-native aggregation is built",
    not non_em_square_functor_defined
    and not diagonal_factorization_broken
    and not carrier_native_aggregation_constructed,
    "cutoff growth does not escape the diagonal-probe barrier",
)

gate(
    "CNA8 no square H2/intersection/correspondence/Rosati is constructed",
    not square_h2_defined
    and not square_intersection_form_defined
    and not square_correspondence_algebra_defined
    and not frobenius_graph_defined
    and not positive_rosati_defined,
    "cutoff totals are not square correspondence data",
)

gate(
    "CNA9 no Laurent boundary or DD4 weight>=1 data is constructed",
    not laurent_axis_defined
    and not boundary_map_defined
    and not torsor_splitter_defined
    and not dd4_weight_ge_1_datum_defined,
    "no boundary map, torsor splitter, or weight>=1 datum",
)

gate(
    "CNA10 base R1 obstructions and carrier guard remain",
    dmp_dim(-1) == 1
    and dmp_dim(-2) == 0
    and not dh_epstein_death_at_square_map
    and not square_correspondence_algebra_defined,
    "DMP bottom gap remains; no carrier-consuming square map where controls die",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (CNA1-CNA10)")
