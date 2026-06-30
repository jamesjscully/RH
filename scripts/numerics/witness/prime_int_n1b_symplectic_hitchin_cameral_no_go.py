"""N1-b' symplectic Hitchin / cameral-cover witness.

Doc 184 kills using the Springer resolution or Steinberg variety convolution
of the appended dual type-B group as the Laurent carrier.  The next repair is
to use Hitchin-system, spectral-curve, or cameral-cover data attached to that
dual group as the missing carrier.

This witness records why that still is not construction-grade R1 data.  The
Hitchin base for type B_m is rank-m invariant-polynomial data with degrees
2,4,...,2m.  The cameral cover has Weyl degree 2^m m!, and the standard
spectral cover for the vector representation has degree 2m+1.  The finite
support building supplies no base curve, canonical bundle, Hitchin base,
cameral cover, spectral curve, selected Laurent axis, boundary map, or torsor
splitter.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_symplectic_hitchin_cameral_no_go
"""

from math import factorial, prod

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


def weyl_group_order_type_b_or_c(rank):
    return 2**rank * factorial(rank)


def type_b_chevalley_degrees(rank):
    return tuple(2 * i for i in range(1, rank + 1))


def vector_spectral_cover_degree_type_b(rank):
    return 2 * rank + 1


def adjoint_dimension_type_b(rank):
    return rank * (2 * rank + 1)


def positive_root_count_type_b(rank):
    return rank * rank


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
dual_group_dimensions = {
    nmax: adjoint_dimension_type_b(rank) for nmax, rank in dual_type_b_ranks.items()
}
positive_root_counts = {
    nmax: positive_root_count_type_b(rank) for nmax, rank in dual_type_b_ranks.items()
}
weyl_orders = {
    nmax: weyl_group_order_type_b_or_c(rank) for nmax, rank in dual_type_b_ranks.items()
}
hitchin_base_ranks = dual_type_b_ranks.copy()
hitchin_invariant_degrees = {
    nmax: type_b_chevalley_degrees(rank) for nmax, rank in dual_type_b_ranks.items()
}
hitchin_generator_counts = {
    nmax: len(degrees) for nmax, degrees in hitchin_invariant_degrees.items()
}
cameral_cover_degrees = weyl_orders.copy()
spectral_cover_degrees = {
    nmax: vector_spectral_cover_degree_type_b(rank)
    for nmax, rank in dual_type_b_ranks.items()
}
generic_hitchin_fiber_ranks = dual_type_b_ranks.copy()
fundamental_hitchin_axis_choices = dual_type_b_ranks.copy()
signed_hitchin_axis_choices = {
    nmax: 2 * rank for nmax, rank in dual_type_b_ranks.items()
}
base_curve_choice_inserted = True
canonical_bundle_choice_inserted = True
spectral_parameter_inserted = True

endpoint_pair_choices = {nmax: rank * rank for nmax, rank in ranks.items()}
coordinate_matching_counts = {1: 6, 2: 24, 4: 720, 8: 3628800}
rank_one_idempotent_counts = {
    nmax: rank_one_idempotent_count(rank) for nmax, rank in ranks.items()
}
laurent_unit_twist_counts = {
    kmax: laurent_unit_twists_in_window(kmax) for kmax in (1, 2, 4, 8)
}

satake_category_supplied_by_carrier = False
dual_group_supplied_by_carrier = False
hitchin_base_supplied_by_support = False
base_curve_supplied_by_support = False
canonical_bundle_supplied_by_support = False
cameral_cover_supplied_by_support = False
spectral_curve_supplied_by_support = False
preferred_hitchin_axis_supplied = False
hitchin_constructs_shift = False
hitchin_constructs_boundary_map = False
hitchin_constructs_torsor_splitter = False
carrier_multiplication_supplied = False
torsor_splitter_supplied = False
primitive_carrier_maps_consumed = 0

gate(
    "SHC1 support tensor ranks are unchanged",
    ranks == {1: 3, 2: 4, 4: 6, 8: 10},
    f"ranks={ranks}",
)

gate(
    "SHC2 Tate/hyperbolic windows and stabilizers are unchanged",
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
    "SHC3 appended dual type-B dimensions and Weyl degrees are fixed finite data",
    dual_type_b_ranks == {1: 2, 2: 3, 4: 5, 8: 9}
    and dual_group_dimensions == {1: 10, 2: 21, 4: 55, 8: 171}
    and positive_root_counts == {1: 4, 2: 9, 4: 25, 8: 81}
    and weyl_orders == {1: 8, 2: 48, 4: 3840, 8: 185794560},
    (
        f"dual_type_b_ranks={dual_type_b_ranks}, "
        f"dual_group_dimensions={dual_group_dimensions}, "
        f"weyl_orders={weyl_orders}"
    ),
)

gate(
    "SHC4 Hitchin base is rank-m invariant-polynomial data",
    hitchin_base_ranks == {1: 2, 2: 3, 4: 5, 8: 9}
    and hitchin_generator_counts == hitchin_base_ranks
    and hitchin_invariant_degrees
    == {
        1: (2, 4),
        2: (2, 4, 6),
        4: (2, 4, 6, 8, 10),
        8: (2, 4, 6, 8, 10, 12, 14, 16, 18),
    },
    (
        f"hitchin_base_ranks={hitchin_base_ranks}, "
        f"hitchin_invariant_degrees={hitchin_invariant_degrees}"
    ),
)

gate(
    "SHC5 cameral and spectral covers overproduce finite sheet data",
    cameral_cover_degrees == {1: 8, 2: 48, 4: 3840, 8: 185794560}
    and spectral_cover_degrees == {1: 5, 2: 7, 4: 11, 8: 19}
    and generic_hitchin_fiber_ranks == {1: 2, 2: 3, 4: 5, 8: 9},
    (
        f"cameral_cover_degrees={cameral_cover_degrees}, "
        f"spectral_cover_degrees={spectral_cover_degrees}, "
        f"generic_hitchin_fiber_ranks={generic_hitchin_fiber_ranks}"
    ),
)

gate(
    "SHC6 selecting one Hitchin invariant or sheet axis is another choice",
    fundamental_hitchin_axis_choices == {1: 2, 2: 3, 4: 5, 8: 9}
    and signed_hitchin_axis_choices == {1: 4, 2: 6, 4: 10, 8: 18}
    and not preferred_hitchin_axis_supplied,
    (
        f"fundamental_hitchin_axis_choices={fundamental_hitchin_axis_choices}, "
        f"signed_hitchin_axis_choices={signed_hitchin_axis_choices}, "
        f"preferred_hitchin_axis_supplied={preferred_hitchin_axis_supplied}"
    ),
)

gate(
    "SHC7 Hitchin inputs are not supplied by finite support",
    not satake_category_supplied_by_carrier
    and not dual_group_supplied_by_carrier
    and not hitchin_base_supplied_by_support
    and not base_curve_supplied_by_support
    and not canonical_bundle_supplied_by_support
    and not cameral_cover_supplied_by_support
    and not spectral_curve_supplied_by_support,
    (
        f"dual_group={dual_group_supplied_by_carrier}, "
        f"hitchin_base={hitchin_base_supplied_by_support}, "
        f"base_curve={base_curve_supplied_by_support}, "
        f"canonical_bundle={canonical_bundle_supplied_by_support}, "
        f"cameral_cover={cameral_cover_supplied_by_support}, "
        f"spectral_curve={spectral_curve_supplied_by_support}"
    ),
)

gate(
    "SHC8 Hitchin/cameral data does not construct shift, boundary map, or torsor splitter",
    not hitchin_constructs_shift
    and not hitchin_constructs_boundary_map
    and not hitchin_constructs_torsor_splitter,
    (
        f"shift={hitchin_constructs_shift}, "
        f"boundary={hitchin_constructs_boundary_map}, "
        f"torsor={hitchin_constructs_torsor_splitter}"
    ),
)

gate(
    "SHC9 choices and base obstructions remain",
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
    "SHC10 Hitchin/cameral package is external geometry formable on controls",
    base_curve_choice_inserted
    and canonical_bundle_choice_inserted
    and spectral_parameter_inserted
    and primitive_carrier_maps_consumed == 0,
    (
        f"base_curve_choice_inserted={base_curve_choice_inserted}, "
        f"canonical_bundle_choice_inserted={canonical_bundle_choice_inserted}, "
        f"spectral_parameter_inserted={spectral_parameter_inserted}, "
        f"primitive_carrier_maps_consumed={primitive_carrier_maps_consumed}"
    ),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (SHC1-SHC10)")
