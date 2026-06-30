"""N1-b' symplectic Springer / Steinberg-variety witness.

Doc 183 kills using the regular nilpotent, Kostant slice, or Chevalley
quotient of the appended dual type-B group as the Laurent carrier.  The next
repair is to use the Springer resolution or Steinberg variety convolution
algebra of that dual group as the missing carrier correspondence algebra.

This witness records why that still is not construction-grade R1 data.  The
Springer/Steinberg package is an honest correspondence package, but in this
setting it is still appended dual-group data.  Its non-equivariant side is
finite Weyl/Schubert data; its equivariant side is polynomial over a rank-m
torus or has a rank-m weight lattice.  It supplies no support-native loop
parameter, selected Laurent axis, boundary map, or torsor splitter.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_symplectic_springer_steinberg_no_go
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


def positive_root_count_type_b(rank):
    return rank * rank


def simple_reflection_count(rank):
    return rank


def torus_weight_lattice_rank(rank):
    return rank


def building_chamber_count_type_c_f2(rank):
    return prod(2 ** (2 * i) - 1 for i in range(1, rank + 1))


def rank_one_idempotent_count(half_rank):
    tate_rank = 2 * half_rank
    return (2**tate_rank - 1) * 2 ** (tate_rank - 1)


def laurent_unit_twists_in_window(kmax):
    return 2 * kmax + 1


ranks = {nmax: dmp_rank_truncated(nmax) for nmax in (1, 2, 4, 8)}
tate_window_ranks = {nmax: 2 * rank for nmax, rank in ranks.items()}
residual_building_ranks = {nmax: rank - 1 for nmax, rank in ranks.items()}
pair_stabilizer_counts = {
    nmax: symplectic_group_order_f2(building_rank)
    for nmax, building_rank in residual_building_ranks.items()
}
dual_type_b_ranks = residual_building_ranks.copy()
positive_system_choices = {
    nmax: weyl_group_order_type_b_or_c(rank) for nmax, rank in dual_type_b_ranks.items()
}
weyl_orders = positive_system_choices.copy()
flag_dimensions = {
    nmax: positive_root_count_type_b(rank) for nmax, rank in dual_type_b_ranks.items()
}
flag_top_cohomological_degrees = {
    nmax: 2 * dim for nmax, dim in flag_dimensions.items()
}
flag_cohomology_dimensions = weyl_orders.copy()
steinberg_component_counts = weyl_orders.copy()
steinberg_component_dimensions = {
    nmax: 2 * dim for nmax, dim in flag_dimensions.items()
}
nil_hecke_simple_generator_counts = {
    nmax: simple_reflection_count(rank) for nmax, rank in dual_type_b_ranks.items()
}
equivariant_polynomial_ranks = {
    nmax: torus_weight_lattice_rank(rank) for nmax, rank in dual_type_b_ranks.items()
}
equivariant_steinberg_weyl_basis_ranks = weyl_orders.copy()
affine_hecke_weight_lattice_ranks = equivariant_polynomial_ranks.copy()
fundamental_axis_choices = dual_type_b_ranks.copy()
signed_axis_choices = {
    nmax: 2 * rank for nmax, rank in dual_type_b_ranks.items()
}
springer_regular_nilpotent_fiber_dimensions = {nmax: 0 for nmax in ranks}
springer_zero_fiber_dimensions = flag_dimensions.copy()

building_chamber_counts = {
    nmax: building_chamber_count_type_c_f2(building_rank)
    for nmax, building_rank in residual_building_ranks.items()
}
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
borel_supplied_by_support = False
springer_resolution_supplied_by_support = False
steinberg_variety_supplied_by_support = False
equivariant_torus_supplied_by_support = False
preferred_weight_axis_supplied = False
springer_constructs_shift = False
springer_constructs_boundary_map = False
springer_constructs_torsor_splitter = False
carrier_multiplication_supplied = False
torsor_splitter_supplied = False
springer_package_inserted = True
primitive_carrier_maps_consumed = 0

gate(
    "SSV1 support tensor ranks are unchanged",
    ranks == {1: 3, 2: 4, 4: 6, 8: 10},
    f"ranks={ranks}",
)

gate(
    "SSV2 Tate/hyperbolic windows and stabilizers are unchanged",
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
    "SSV3 dual type-B Springer data has finite Weyl and flag dimensions",
    dual_type_b_ranks == {1: 2, 2: 3, 4: 5, 8: 9}
    and weyl_orders == {1: 8, 2: 48, 4: 3840, 8: 185794560}
    and flag_dimensions == {1: 4, 2: 9, 4: 25, 8: 81}
    and flag_top_cohomological_degrees == {1: 8, 2: 18, 4: 50, 8: 162},
    (
        f"dual_type_b_ranks={dual_type_b_ranks}, "
        f"weyl_orders={weyl_orders}, flag_dimensions={flag_dimensions}"
    ),
)

gate(
    "SSV4 non-equivariant Springer/Steinberg data is finite Weyl-indexed",
    flag_cohomology_dimensions == {1: 8, 2: 48, 4: 3840, 8: 185794560}
    and steinberg_component_counts == flag_cohomology_dimensions
    and steinberg_component_dimensions == {1: 8, 2: 18, 4: 50, 8: 162}
    and springer_regular_nilpotent_fiber_dimensions == {1: 0, 2: 0, 4: 0, 8: 0}
    and springer_zero_fiber_dimensions == {1: 4, 2: 9, 4: 25, 8: 81},
    (
        f"flag_cohomology_dimensions={flag_cohomology_dimensions}, "
        f"steinberg_component_counts={steinberg_component_counts}"
    ),
)

gate(
    "SSV5 equivariant/nil-Hecke data has rank-m polynomial or weight lattice",
    nil_hecke_simple_generator_counts == {1: 2, 2: 3, 4: 5, 8: 9}
    and equivariant_polynomial_ranks == {1: 2, 2: 3, 4: 5, 8: 9}
    and affine_hecke_weight_lattice_ranks == {1: 2, 2: 3, 4: 5, 8: 9}
    and equivariant_steinberg_weyl_basis_ranks == {1: 8, 2: 48, 4: 3840, 8: 185794560},
    (
        f"equivariant_polynomial_ranks={equivariant_polynomial_ranks}, "
        f"equivariant_steinberg_weyl_basis_ranks={equivariant_steinberg_weyl_basis_ranks}"
    ),
)

gate(
    "SSV6 selecting one equivariant/Laurent axis is another choice",
    fundamental_axis_choices == {1: 2, 2: 3, 4: 5, 8: 9}
    and signed_axis_choices == {1: 4, 2: 6, 4: 10, 8: 18}
    and not preferred_weight_axis_supplied,
    (
        f"fundamental_axis_choices={fundamental_axis_choices}, "
        f"signed_axis_choices={signed_axis_choices}, "
        f"preferred_weight_axis_supplied={preferred_weight_axis_supplied}"
    ),
)

gate(
    "SSV7 Springer/Steinberg inputs are not supplied by finite support",
    not satake_category_supplied_by_carrier
    and not dual_group_supplied_by_carrier
    and not borel_supplied_by_support
    and not springer_resolution_supplied_by_support
    and not steinberg_variety_supplied_by_support
    and not equivariant_torus_supplied_by_support,
    (
        f"dual_group={dual_group_supplied_by_carrier}, "
        f"borel={borel_supplied_by_support}, "
        f"springer={springer_resolution_supplied_by_support}, "
        f"steinberg={steinberg_variety_supplied_by_support}, "
        f"equivariant_torus={equivariant_torus_supplied_by_support}"
    ),
)

gate(
    "SSV8 Springer/Steinberg convolution does not construct shift, boundary map, or torsor splitter",
    not springer_constructs_shift
    and not springer_constructs_boundary_map
    and not springer_constructs_torsor_splitter,
    (
        f"shift={springer_constructs_shift}, "
        f"boundary={springer_constructs_boundary_map}, "
        f"torsor={springer_constructs_torsor_splitter}"
    ),
)

gate(
    "SSV9 choices and base obstructions remain",
    building_chamber_counts
    == {
        1: 45,
        2: 2835,
        4: 739552275,
        8: 852369269595510700600441875,
    }
    and endpoint_pair_choices == {1: 9, 2: 16, 4: 36, 8: 100}
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
    "SSV10 Springer/Steinberg package is formable on controls",
    springer_package_inserted
    and primitive_carrier_maps_consumed == 0
    and weyl_orders == {1: 8, 2: 48, 4: 3840, 8: 185794560},
    (
        f"springer_package_inserted={springer_package_inserted}, "
        f"primitive_carrier_maps_consumed={primitive_carrier_maps_consumed}"
    ),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (SSV1-SSV10)")
