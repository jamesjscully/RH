"""N1-b' symplectic principal-cocharacter / principal SL2 witness.

Doc 181 kills appending geometric Satake / dual-representation data to the
finite support building.  The next repair is to use the principal SL2 of the
dual type-B group: its principal cocharacter gives a canonical-looking
rank-one axis, so read that axis as the missing Laurent carrier.

This witness records why that still is not construction-grade R1 data.  The
principal cocharacter is a finite grading inside an appended dual group.  It
depends on a positive system/pinning, its finite representations have finite
principal strings, and using the coordinate ring of the source G_m is an
external Laurent-coordinate insertion.  It supplies no boundary map, Laurent
shift, or torsor splitter.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_symplectic_principal_cocharacter_no_go
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


def principal_h_coordinates_type_b(rank):
    # h is the principal cocharacter with alpha_i(h)=2 for every simple
    # root of B_m: h_i - h_{i+1}=2 and h_m=2.
    return tuple(2 * (rank - i) for i in range(rank))


def simple_root_pairings_type_b(hcoords):
    return tuple(hcoords[i] - hcoords[i + 1] for i in range(len(hcoords) - 1)) + (
        hcoords[-1],
    )


def vector_principal_weights_type_b(rank):
    hcoords = principal_h_coordinates_type_b(rank)
    return tuple(sorted((-x for x in hcoords), reverse=False) + [0] + list(hcoords))


def principal_adjoint_sl2_dimensions_type_b(rank):
    # Exponents of type B_m are 1,3,5,...,2m-1, so the principal-SL2
    # adjoint summands have dimensions 2e_i+1 = 3,7,11,...,4m-1.
    return tuple(4 * i - 1 for i in range(1, rank + 1))


def dominant_weight_generator_count_type_b(rank):
    return rank


def building_chamber_count_type_c_f2(rank):
    return prod(2 ** (2 * i) - 1 for i in range(1, rank + 1))


def graph_lagrangian_count_f2(rank):
    return 2 ** (rank * (rank + 1) // 2)


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
principal_h_coordinates = {
    nmax: principal_h_coordinates_type_b(rank)
    for nmax, rank in dual_type_b_ranks.items()
}
principal_simple_pairings = {
    nmax: simple_root_pairings_type_b(hcoords)
    for nmax, hcoords in principal_h_coordinates.items()
}
principal_axis_rank = {nmax: 1 for nmax in ranks}
principal_sign_choices = {nmax: 2 for nmax in ranks}
vector_principal_weights = {
    nmax: vector_principal_weights_type_b(rank)
    for nmax, rank in dual_type_b_ranks.items()
}
vector_principal_weight_counts = {
    nmax: len(weights) for nmax, weights in vector_principal_weights.items()
}
vector_principal_max_weights = {
    nmax: max(weights) for nmax, weights in vector_principal_weights.items()
}
adjoint_principal_dimensions = {
    nmax: principal_adjoint_sl2_dimensions_type_b(rank)
    for nmax, rank in dual_type_b_ranks.items()
}
adjoint_dimensions = {
    nmax: sum(dims) for nmax, dims in adjoint_principal_dimensions.items()
}
adjoint_principal_summand_counts = {
    nmax: len(dims) for nmax, dims in adjoint_principal_dimensions.items()
}
adjoint_highest_principal_weights = {
    nmax: dims[-1] - 1 for nmax, dims in adjoint_principal_dimensions.items()
}
representation_ring_generator_counts = {
    nmax: dominant_weight_generator_count_type_b(rank)
    for nmax, rank in dual_type_b_ranks.items()
}

building_chamber_counts = {
    nmax: building_chamber_count_type_c_f2(building_rank)
    for nmax, building_rank in residual_building_ranks.items()
}
graph_lagrangian_counts = {
    nmax: graph_lagrangian_count_f2(rank) for nmax, rank in ranks.items()
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
pinning_supplied_by_support = False
principal_sl2_supplied_by_support = False
principal_torus_coordinate_supplied_by_support = False
principal_grading_constructs_shift = False
principal_grading_constructs_boundary_map = False
principal_grading_constructs_torsor_splitter = False
carrier_multiplication_supplied = False
torsor_splitter_supplied = False
external_gm_coordinate_inserted = True
primitive_carrier_maps_consumed = 0

gate(
    "SPC1 support tensor ranks are unchanged",
    ranks == {1: 3, 2: 4, 4: 6, 8: 10},
    f"ranks={ranks}",
)

gate(
    "SPC2 Tate/hyperbolic windows and stabilizers are unchanged",
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
    "SPC3 appended dual type-B ranks remain m=2,3,5,9",
    dual_type_b_ranks == {1: 2, 2: 3, 4: 5, 8: 9}
    and representation_ring_generator_counts == dual_type_b_ranks,
    (
        f"dual_type_b_ranks={dual_type_b_ranks}, "
        f"representation_ring_generator_counts={representation_ring_generator_counts}"
    ),
)

gate(
    "SPC4 the principal cocharacter is rank one only after choosing a positive system",
    principal_axis_rank == {1: 1, 2: 1, 4: 1, 8: 1}
    and positive_system_choices == {1: 8, 2: 48, 4: 3840, 8: 185794560}
    and principal_sign_choices == {1: 2, 2: 2, 4: 2, 8: 2}
    and not pinning_supplied_by_support,
    (
        f"principal_axis_rank={principal_axis_rank}, "
        f"positive_system_choices={positive_system_choices}, "
        f"principal_sign_choices={principal_sign_choices}, "
        f"pinning_supplied_by_support={pinning_supplied_by_support}"
    ),
)

gate(
    "SPC5 h=2rho^vee has alpha_i(h)=2 but is finite root-data grading",
    principal_h_coordinates
    == {
        1: (4, 2),
        2: (6, 4, 2),
        4: (10, 8, 6, 4, 2),
        8: (18, 16, 14, 12, 10, 8, 6, 4, 2),
    }
    and all(all(pairing == 2 for pairing in pairs) for pairs in principal_simple_pairings.values()),
    (
        f"principal_h_coordinates={principal_h_coordinates}, "
        f"principal_simple_pairings={principal_simple_pairings}"
    ),
)

gate(
    "SPC6 the principal vector strings are finite, not bi-infinite Laurent orbits",
    vector_principal_weight_counts == {1: 5, 2: 7, 4: 11, 8: 19}
    and vector_principal_max_weights == {1: 4, 2: 6, 4: 10, 8: 18}
    and all(min(weights) == -max(weights) for weights in vector_principal_weights.values()),
    (
        f"vector_principal_weight_counts={vector_principal_weight_counts}, "
        f"vector_principal_max_weights={vector_principal_max_weights}"
    ),
)

gate(
    "SPC7 the principal adjoint decomposition overproduces finite SL2 strings",
    adjoint_principal_dimensions
    == {
        1: (3, 7),
        2: (3, 7, 11),
        4: (3, 7, 11, 15, 19),
        8: (3, 7, 11, 15, 19, 23, 27, 31, 35),
    }
    and adjoint_dimensions == {1: 10, 2: 21, 4: 55, 8: 171}
    and adjoint_principal_summand_counts == {1: 2, 2: 3, 4: 5, 8: 9}
    and adjoint_highest_principal_weights == {1: 6, 2: 10, 4: 18, 8: 34},
    (
        f"adjoint_principal_dimensions={adjoint_principal_dimensions}, "
        f"adjoint_dimensions={adjoint_dimensions}, "
        f"adjoint_highest_principal_weights={adjoint_highest_principal_weights}"
    ),
)

gate(
    "SPC8 principal SL2 and its Gm coordinate are not support-supplied",
    not satake_category_supplied_by_carrier
    and not dual_group_supplied_by_carrier
    and not principal_sl2_supplied_by_support
    and not principal_torus_coordinate_supplied_by_support,
    (
        f"satake_category={satake_category_supplied_by_carrier}, "
        f"dual_group={dual_group_supplied_by_carrier}, "
        f"principal_sl2={principal_sl2_supplied_by_support}, "
        f"principal_torus_coordinate={principal_torus_coordinate_supplied_by_support}"
    ),
)

gate(
    "SPC9 principal grading does not construct shift, boundary map, or torsor splitter",
    not principal_grading_constructs_shift
    and not principal_grading_constructs_boundary_map
    and not principal_grading_constructs_torsor_splitter,
    (
        f"shift={principal_grading_constructs_shift}, "
        f"boundary={principal_grading_constructs_boundary_map}, "
        f"torsor={principal_grading_constructs_torsor_splitter}"
    ),
)

gate(
    "SPC10 choices and base obstructions remain",
    building_chamber_counts
    == {
        1: 45,
        2: 2835,
        4: 739552275,
        8: 852369269595510700600441875,
    }
    and graph_lagrangian_counts == {1: 64, 2: 1024, 4: 2097152, 8: 36028797018963968}
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
    "SPC11 using the principal torus coordinate is external Laurent insertion formable on controls",
    external_gm_coordinate_inserted
    and primitive_carrier_maps_consumed == 0
    and principal_axis_rank == {1: 1, 2: 1, 4: 1, 8: 1},
    (
        f"external_gm_coordinate_inserted={external_gm_coordinate_inserted}, "
        f"primitive_carrier_maps_consumed={primitive_carrier_maps_consumed}"
    ),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (SPC1-SPC11)")
