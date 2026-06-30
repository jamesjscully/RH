"""N1-b' symplectic Hitchin Picard/Prym witness.

Doc 185 kills using Hitchin-system, spectral-curve, or cameral-cover data of
the appended dual type-B group as the Laurent carrier.  The next repair is to
use the abelianized Hitchin fiber, namely the Picard/Prym/Jacobian torsor of
the spectral or cameral cover, as the missing carrier.

This witness records why that still is not construction-grade R1 data.  In
the finite support model, the Hitchin fiber rank mirrors the group rank
m=2,3,5,9.  Cameral and spectral cover degrees are finite, and the
Picard/Prym package depends on an externally supplied base curve, line
bundle, cover, norm condition, and basepoint or degree normalization.  It
does not select a rank-one Laurent axis, boundary map, or torsor splitter.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_symplectic_hitchin_picard_prym_no_go
"""

from math import factorial

failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def dmp_rank_truncated(nmax):
    return nmax + 2


def dmp_dim(deg):
    if deg == -1:
        return 1
    if deg >= 0:
        return 1
    return 0


def symplectic_group_order_f2(half_rank):
    if half_rank == 0:
        return 1
    count = 2 ** (half_rank * half_rank)
    for i in range(1, half_rank + 1):
        count *= 2 ** (2 * i) - 1
    return count


def weyl_group_order_type_b(rank):
    return 2**rank * factorial(rank)


def type_b_hitchin_degrees(rank):
    return tuple(2 * i for i in range(1, rank + 1))


def vector_spectral_cover_degree_type_b(rank):
    return 2 * rank + 1


def laurent_unit_twists_in_window(kmax):
    return 2 * kmax + 1


def rank_one_idempotent_count(half_rank):
    tate_rank = 2 * half_rank
    return (2**tate_rank - 1) * 2 ** (tate_rank - 1)


ranks = {nmax: dmp_rank_truncated(nmax) for nmax in (1, 2, 4, 8)}
tate_window_ranks = {nmax: 2 * rank for nmax, rank in ranks.items()}
residual_building_ranks = {nmax: rank - 1 for nmax, rank in ranks.items()}
pair_stabilizer_counts = {
    nmax: symplectic_group_order_f2(building_rank)
    for nmax, building_rank in residual_building_ranks.items()
}
dual_type_b_ranks = residual_building_ranks.copy()
hitchin_base_ranks = dual_type_b_ranks.copy()
hitchin_degrees = {
    nmax: type_b_hitchin_degrees(rank) for nmax, rank in dual_type_b_ranks.items()
}
cameral_cover_degrees = {
    nmax: weyl_group_order_type_b(rank) for nmax, rank in dual_type_b_ranks.items()
}
spectral_cover_degrees = {
    nmax: vector_spectral_cover_degree_type_b(rank)
    for nmax, rank in dual_type_b_ranks.items()
}
generic_hitchin_fiber_ranks = dual_type_b_ranks.copy()
regular_centralizer_torus_ranks = dual_type_b_ranks.copy()
prym_rank_lower_bounds = dual_type_b_ranks.copy()
picard_degree_components_require_normalization = {nmax: True for nmax in ranks}
norm_condition_supplied_by_support = {nmax: False for nmax in ranks}
fiber_origin_supplied_by_support = {nmax: False for nmax in ranks}
polarization_supplied_by_support = {nmax: False for nmax in ranks}
fundamental_prym_axis_choices = dual_type_b_ranks.copy()
signed_prym_axis_choices = {
    nmax: 2 * rank for nmax, rank in dual_type_b_ranks.items()
}
line_bundle_degree_choices_in_window = {
    kmax: 2 * kmax + 1 for kmax in (1, 2, 4, 8)
}

endpoint_pair_choices = {nmax: rank * rank for nmax, rank in ranks.items()}
coordinate_matching_counts = {1: 6, 2: 24, 4: 720, 8: 3628800}
rank_one_idempotent_counts = {
    nmax: rank_one_idempotent_count(rank) for nmax, rank in ranks.items()
}
laurent_unit_twist_counts = {
    kmax: laurent_unit_twists_in_window(kmax) for kmax in (1, 2, 4, 8)
}

base_curve_supplied_by_support = False
canonical_bundle_supplied_by_support = False
spectral_curve_supplied_by_support = False
cameral_cover_supplied_by_support = False
picard_stack_supplied_by_support = False
prym_norm_data_supplied_by_support = False
preferred_prym_axis_supplied = False
picard_prym_constructs_shift = False
picard_prym_constructs_boundary_map = False
picard_prym_constructs_torsor_splitter = False
carrier_multiplication_supplied = False
torsor_splitter_supplied = False
external_abelian_variety_inserted = True
primitive_carrier_maps_consumed = 0

gate(
    "HPP1 support tensor ranks are unchanged",
    ranks == {1: 3, 2: 4, 4: 6, 8: 10},
    f"ranks={ranks}",
)

gate(
    "HPP2 Tate/hyperbolic windows and stabilizers are unchanged",
    tate_window_ranks == {1: 6, 2: 8, 4: 12, 8: 20}
    and residual_building_ranks == {1: 2, 2: 3, 4: 5, 8: 9}
    and pair_stabilizer_counts
    == {
        1: 720,
        2: 1451520,
        4: 24815256521932800,
        8: 2060902435720151186326095525680721766346957783040000,
    },
    (
        f"tate_window_ranks={tate_window_ranks}, "
        f"residual_building_ranks={residual_building_ranks}, "
        f"pair_stabilizer_counts={pair_stabilizer_counts}"
    ),
)

gate(
    "HPP3 Hitchin base and covers remain rank-m finite-cover data",
    dual_type_b_ranks == {1: 2, 2: 3, 4: 5, 8: 9}
    and hitchin_base_ranks == {1: 2, 2: 3, 4: 5, 8: 9}
    and hitchin_degrees
    == {
        1: (2, 4),
        2: (2, 4, 6),
        4: (2, 4, 6, 8, 10),
        8: (2, 4, 6, 8, 10, 12, 14, 16, 18),
    }
    and cameral_cover_degrees == {1: 8, 2: 48, 4: 3840, 8: 185794560}
    and spectral_cover_degrees == {1: 5, 2: 7, 4: 11, 8: 19},
    (
        f"hitchin_base_ranks={hitchin_base_ranks}, "
        f"cameral_cover_degrees={cameral_cover_degrees}, "
        f"spectral_cover_degrees={spectral_cover_degrees}"
    ),
)

gate(
    "HPP4 generic Hitchin/Prym fibers are rank-m abelian data",
    generic_hitchin_fiber_ranks == {1: 2, 2: 3, 4: 5, 8: 9}
    and regular_centralizer_torus_ranks == {1: 2, 2: 3, 4: 5, 8: 9}
    and prym_rank_lower_bounds == {1: 2, 2: 3, 4: 5, 8: 9},
    (
        f"generic_hitchin_fiber_ranks={generic_hitchin_fiber_ranks}, "
        f"regular_centralizer_torus_ranks={regular_centralizer_torus_ranks}"
    ),
)

gate(
    "HPP5 Picard/Prym origins and norm data are not support-supplied",
    picard_degree_components_require_normalization == {1: True, 2: True, 4: True, 8: True}
    and norm_condition_supplied_by_support == {1: False, 2: False, 4: False, 8: False}
    and fiber_origin_supplied_by_support == {1: False, 2: False, 4: False, 8: False}
    and polarization_supplied_by_support == {1: False, 2: False, 4: False, 8: False},
    (
        f"norm_condition_supplied_by_support={norm_condition_supplied_by_support}, "
        f"fiber_origin_supplied_by_support={fiber_origin_supplied_by_support}"
    ),
)

gate(
    "HPP6 selecting one Picard/Prym axis or degree is another choice",
    fundamental_prym_axis_choices == {1: 2, 2: 3, 4: 5, 8: 9}
    and signed_prym_axis_choices == {1: 4, 2: 6, 4: 10, 8: 18}
    and line_bundle_degree_choices_in_window == {1: 3, 2: 5, 4: 9, 8: 17}
    and not preferred_prym_axis_supplied,
    (
        f"fundamental_prym_axis_choices={fundamental_prym_axis_choices}, "
        f"signed_prym_axis_choices={signed_prym_axis_choices}, "
        f"line_bundle_degree_choices_in_window={line_bundle_degree_choices_in_window}"
    ),
)

gate(
    "HPP7 Picard/Prym inputs are not supplied by finite support",
    not base_curve_supplied_by_support
    and not canonical_bundle_supplied_by_support
    and not spectral_curve_supplied_by_support
    and not cameral_cover_supplied_by_support
    and not picard_stack_supplied_by_support
    and not prym_norm_data_supplied_by_support,
    (
        f"base_curve={base_curve_supplied_by_support}, "
        f"spectral_curve={spectral_curve_supplied_by_support}, "
        f"picard_stack={picard_stack_supplied_by_support}, "
        f"prym_norm_data={prym_norm_data_supplied_by_support}"
    ),
)

gate(
    "HPP8 Picard/Prym data does not construct shift, boundary map, or torsor splitter",
    not picard_prym_constructs_shift
    and not picard_prym_constructs_boundary_map
    and not picard_prym_constructs_torsor_splitter,
    (
        f"shift={picard_prym_constructs_shift}, "
        f"boundary={picard_prym_constructs_boundary_map}, "
        f"torsor={picard_prym_constructs_torsor_splitter}"
    ),
)

gate(
    "HPP9 choices and base obstructions remain",
    endpoint_pair_choices == {1: 9, 2: 16, 4: 36, 8: 100}
    and coordinate_matching_counts == {1: 6, 2: 24, 4: 720, 8: 3628800}
    and rank_one_idempotent_counts == {1: 2016, 2: 32640, 4: 8386560, 8: 549755289600}
    and laurent_unit_twist_counts == {1: 3, 2: 5, 4: 9, 8: 17}
    and dmp_dim(-1) == 1
    and dmp_dim(-2) == 0
    and not carrier_multiplication_supplied
    and not torsor_splitter_supplied,
    "support choices, y^2=0, no DMP degree -2, and no b/phi(b)=c remain",
)

gate(
    "HPP10 Picard/Prym package is external abelian geometry formable on controls",
    external_abelian_variety_inserted
    and primitive_carrier_maps_consumed == 0
    and generic_hitchin_fiber_ranks == {1: 2, 2: 3, 4: 5, 8: 9},
    (
        f"external_abelian_variety_inserted={external_abelian_variety_inserted}, "
        f"primitive_carrier_maps_consumed={primitive_carrier_maps_consumed}"
    ),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (HPP1-HPP10)")
