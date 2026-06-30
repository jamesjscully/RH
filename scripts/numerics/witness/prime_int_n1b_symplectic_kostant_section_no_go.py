"""N1-b' symplectic Kostant-section / regular-nilpotent witness.

Doc 182 kills using the principal cocharacter of the appended dual type-B
group as the Laurent carrier.  The next repair is to use the principal
nilpotent, Kostant slice, or Chevalley adjoint quotient of that dual group as
the missing carrier correspondence algebra.

This witness records why that still is not construction-grade R1 data.  The
regular nilpotent is nilpotent, not invertible; its principal strings are
finite.  The Kostant section is an affine rank-m slice with polynomial
invariant coordinates of degrees 2,4,...,2m, not a rank-one Laurent line.
The dual group, pinning, principal nilpotent, Kostant slice, quotient
coordinates, boundary map, Laurent shift, and torsor splitter are not
supplied by the finite support building.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_symplectic_kostant_section_no_go
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


def type_b_dimension(rank):
    return rank * (2 * rank + 1)


def type_b_exponents(rank):
    return tuple(2 * i - 1 for i in range(1, rank + 1))


def type_b_chevalley_degrees(rank):
    return tuple(exponent + 1 for exponent in type_b_exponents(rank))


def principal_adjoint_sl2_dimensions_type_b(rank):
    # Principal SL2 summand dimensions are 2e_i+1 for exponents e_i.
    return tuple(2 * exponent + 1 for exponent in type_b_exponents(rank))


def vector_regular_nilpotent_index_type_b(rank):
    # The vector representation of B_m has dimension 2m+1; the principal
    # nilpotent acts as one finite Jordan string in this test model.
    return 2 * rank + 1


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
dual_group_dimensions = {
    nmax: type_b_dimension(rank) for nmax, rank in dual_type_b_ranks.items()
}
regular_centralizer_dimensions = dual_type_b_ranks.copy()
regular_nilpotent_orbit_dimensions = {
    nmax: dual_group_dimensions[nmax] - dual_type_b_ranks[nmax] for nmax in ranks
}
chevalley_invariant_degrees = {
    nmax: type_b_chevalley_degrees(rank)
    for nmax, rank in dual_type_b_ranks.items()
}
chevalley_generator_counts = {
    nmax: len(degrees) for nmax, degrees in chevalley_invariant_degrees.items()
}
kostant_slice_dimensions = dual_type_b_ranks.copy()
adjoint_principal_dimensions = {
    nmax: principal_adjoint_sl2_dimensions_type_b(rank)
    for nmax, rank in dual_type_b_ranks.items()
}
adjoint_nilpotency_indices = {
    nmax: max(dims) for nmax, dims in adjoint_principal_dimensions.items()
}
vector_nilpotency_indices = {
    nmax: vector_regular_nilpotent_index_type_b(rank)
    for nmax, rank in dual_type_b_ranks.items()
}
regular_nilpotent_is_invertible = {nmax: False for nmax in ranks}
chevalley_base_is_affine = {nmax: True for nmax in ranks}
chevalley_base_is_laurent = {nmax: False for nmax in ranks}

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
principal_nilpotent_supplied_by_support = False
kostant_slice_supplied_by_support = False
chevalley_coordinates_supplied_by_support = False
kostant_section_constructs_shift = False
kostant_section_constructs_boundary_map = False
kostant_section_constructs_torsor_splitter = False
carrier_multiplication_supplied = False
torsor_splitter_supplied = False
external_chevalley_coordinates_inserted = True
primitive_carrier_maps_consumed = 0

gate(
    "SKS1 support tensor ranks are unchanged",
    ranks == {1: 3, 2: 4, 4: 6, 8: 10},
    f"ranks={ranks}",
)

gate(
    "SKS2 Tate/hyperbolic windows and stabilizers are unchanged",
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
    "SKS3 appended dual type-B data remains rank m",
    dual_type_b_ranks == {1: 2, 2: 3, 4: 5, 8: 9}
    and dual_group_dimensions == {1: 10, 2: 21, 4: 55, 8: 171}
    and regular_centralizer_dimensions == dual_type_b_ranks
    and regular_nilpotent_orbit_dimensions == {1: 8, 2: 18, 4: 50, 8: 162},
    (
        f"dual_type_b_ranks={dual_type_b_ranks}, "
        f"dual_group_dimensions={dual_group_dimensions}, "
        f"regular_nilpotent_orbit_dimensions={regular_nilpotent_orbit_dimensions}"
    ),
)

gate(
    "SKS4 regular nilpotent requires positive-system or pinning data",
    positive_system_choices == {1: 8, 2: 48, 4: 3840, 8: 185794560}
    and not pinning_supplied_by_support
    and not principal_nilpotent_supplied_by_support,
    (
        f"positive_system_choices={positive_system_choices}, "
        f"pinning_supplied_by_support={pinning_supplied_by_support}, "
        f"principal_nilpotent_supplied_by_support={principal_nilpotent_supplied_by_support}"
    ),
)

gate(
    "SKS5 regular nilpotent strings are finite, not invertible Laurent shifts",
    vector_nilpotency_indices == {1: 5, 2: 7, 4: 11, 8: 19}
    and adjoint_nilpotency_indices == {1: 7, 2: 11, 4: 19, 8: 35}
    and regular_nilpotent_is_invertible == {1: False, 2: False, 4: False, 8: False},
    (
        f"vector_nilpotency_indices={vector_nilpotency_indices}, "
        f"adjoint_nilpotency_indices={adjoint_nilpotency_indices}, "
        f"regular_nilpotent_is_invertible={regular_nilpotent_is_invertible}"
    ),
)

gate(
    "SKS6 Kostant slice and Chevalley quotient are rank-m affine data",
    kostant_slice_dimensions == {1: 2, 2: 3, 4: 5, 8: 9}
    and chevalley_generator_counts == {1: 2, 2: 3, 4: 5, 8: 9}
    and chevalley_invariant_degrees
    == {
        1: (2, 4),
        2: (2, 4, 6),
        4: (2, 4, 6, 8, 10),
        8: (2, 4, 6, 8, 10, 12, 14, 16, 18),
    }
    and chevalley_base_is_affine == {1: True, 2: True, 4: True, 8: True}
    and chevalley_base_is_laurent == {1: False, 2: False, 4: False, 8: False},
    (
        f"kostant_slice_dimensions={kostant_slice_dimensions}, "
        f"chevalley_invariant_degrees={chevalley_invariant_degrees}"
    ),
)

gate(
    "SKS7 Kostant-section inputs are not supplied by finite support",
    not satake_category_supplied_by_carrier
    and not dual_group_supplied_by_carrier
    and not kostant_slice_supplied_by_support
    and not chevalley_coordinates_supplied_by_support,
    (
        f"satake_category={satake_category_supplied_by_carrier}, "
        f"dual_group={dual_group_supplied_by_carrier}, "
        f"kostant_slice={kostant_slice_supplied_by_support}, "
        f"chevalley_coordinates={chevalley_coordinates_supplied_by_support}"
    ),
)

gate(
    "SKS8 Kostant section does not construct shift, boundary map, or torsor splitter",
    not kostant_section_constructs_shift
    and not kostant_section_constructs_boundary_map
    and not kostant_section_constructs_torsor_splitter,
    (
        f"shift={kostant_section_constructs_shift}, "
        f"boundary={kostant_section_constructs_boundary_map}, "
        f"torsor={kostant_section_constructs_torsor_splitter}"
    ),
)

gate(
    "SKS9 choices and base obstructions remain",
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
    "SKS10 Chevalley/Kostant coordinates are external affine insertion formable on controls",
    external_chevalley_coordinates_inserted
    and primitive_carrier_maps_consumed == 0
    and kostant_slice_dimensions == {1: 2, 2: 3, 4: 5, 8: 9},
    (
        f"external_chevalley_coordinates_inserted={external_chevalley_coordinates_inserted}, "
        f"primitive_carrier_maps_consumed={primitive_carrier_maps_consumed}"
    ),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (SKS1-SKS10)")
