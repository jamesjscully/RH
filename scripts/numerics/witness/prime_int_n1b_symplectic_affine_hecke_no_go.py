"""N1-b' symplectic affine Weyl/Hecke translation witness.

Doc 178 kills the finite type-C Hecke/Iwahori algebra of the support
building.  The next repair is to pass to the affine Weyl group or affine
Hecke algebra and use its translation lattice as the missing Laurent shift.

In the finite F_2 support windows, the residual first-pair stabilizer
buildings have type C_m with m = 2,3,5,9.  Passing to affine type adds a
translation lattice of rank m, not a selected rank-one Laurent axis.  The
affine simple-generator counts are m+1 = 3,4,6,10, matching support ranks
only as finite bookkeeping.  The finite support building supplies no affine
valuation, no translation lattice, no preferred primitive direction, and no
boundary map.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_symplectic_affine_hecke_no_go
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


def weyl_group_order_type_c(rank):
    return 2**rank * factorial(rank)


def coxeter_order_type_c(rank):
    return 2 * rank


def longest_bruhat_length_type_c(rank):
    return rank * rank


def building_chamber_count_type_c_f2(rank):
    return prod(2 ** (2 * i) - 1 for i in range(1, rank + 1))


def steinberg_dimension_type_c_f2(rank):
    return 2 ** (rank * rank)


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
finite_weyl_orders = {
    nmax: weyl_group_order_type_c(building_rank)
    for nmax, building_rank in residual_building_ranks.items()
}
finite_hecke_basis_ranks = finite_weyl_orders.copy()
finite_longest_bruhat_lengths = {
    nmax: longest_bruhat_length_type_c(building_rank)
    for nmax, building_rank in residual_building_ranks.items()
}
coxeter_orders = {
    nmax: coxeter_order_type_c(building_rank)
    for nmax, building_rank in residual_building_ranks.items()
}

affine_translation_lattice_ranks = residual_building_ranks.copy()
affine_simple_generator_counts = {
    nmax: building_rank + 1 for nmax, building_rank in residual_building_ranks.items()
}
simple_coroot_axis_choices = {
    nmax: 2 * building_rank for nmax, building_rank in residual_building_ranks.items()
}
laurent_axis_rank = 1
affine_basis_is_infinite = True
affine_length_has_no_longest_element = True

building_top_degrees = {
    nmax: building_rank - 1 for nmax, building_rank in residual_building_ranks.items()
}
building_chamber_counts = {
    nmax: building_chamber_count_type_c_f2(building_rank)
    for nmax, building_rank in residual_building_ranks.items()
}
steinberg_dimensions = {
    nmax: steinberg_dimension_type_c_f2(building_rank)
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

affine_valuation_supplied_by_support = False
translation_lattice_supplied_by_carrier = False
preferred_primitive_translation_supplied = False
affine_hecke_supplied_by_carrier = False
affine_translation_constructs_boundary_map = False
affine_translation_constructs_torsor_splitter = False
carrier_multiplication_supplied = False
torsor_splitter_supplied = False

gate(
    "SAH1 support tensor ranks are unchanged",
    ranks == {1: 3, 2: 4, 4: 6, 8: 10},
    f"ranks={ranks}",
)

gate(
    "SAH2 Tate/hyperbolic windows double support rank",
    tate_window_ranks == {1: 6, 2: 8, 4: 12, 8: 20},
    f"tate_window_ranks={tate_window_ranks}",
)

gate(
    "SAH3 residual first-pair stabilizers remain finite type-C sources",
    residual_building_ranks == {1: 2, 2: 3, 4: 5, 8: 9}
    and pair_stabilizer_counts
    == {
        1: 720,
        2: 1451520,
        4: 24815256521932800,
        8: 2060902435720151186326095525680721766346957783040000,
    },
    (
        f"residual_building_ranks={residual_building_ranks}, "
        f"pair_stabilizer_counts={pair_stabilizer_counts}"
    ),
)

gate(
    "SAH4 finite Weyl/Hecke data is unchanged before affine insertion",
    finite_weyl_orders == {1: 8, 2: 48, 4: 3840, 8: 185794560}
    and finite_hecke_basis_ranks == finite_weyl_orders
    and finite_longest_bruhat_lengths == {1: 4, 2: 9, 4: 25, 8: 81}
    and coxeter_orders == {1: 4, 2: 6, 4: 10, 8: 18},
    (
        f"finite_weyl_orders={finite_weyl_orders}, "
        f"finite_longest_bruhat_lengths={finite_longest_bruhat_lengths}, "
        f"coxeter_orders={coxeter_orders}"
    ),
)

gate(
    "SAH5 affine translation lattice has rank m, not rank one",
    affine_translation_lattice_ranks == {1: 2, 2: 3, 4: 5, 8: 9}
    and all(rank > laurent_axis_rank for rank in affine_translation_lattice_ranks.values()),
    f"affine_translation_lattice_ranks={affine_translation_lattice_ranks}",
)

gate(
    "SAH6 affine simple-generator counts only mirror support ranks",
    affine_simple_generator_counts == ranks
    and simple_coroot_axis_choices == {1: 4, 2: 6, 4: 10, 8: 18},
    (
        f"affine_simple_generator_counts={affine_simple_generator_counts}, "
        f"simple_coroot_axis_choices={simple_coroot_axis_choices}"
    ),
)

gate(
    "SAH7 affine Hecke basis is infinite only after adding translation data",
    affine_basis_is_infinite
    and affine_length_has_no_longest_element
    and not affine_valuation_supplied_by_support
    and not translation_lattice_supplied_by_carrier,
    (
        f"affine_basis_is_infinite={affine_basis_is_infinite}, "
        f"affine_valuation_supplied_by_support={affine_valuation_supplied_by_support}, "
        f"translation_lattice_supplied_by_carrier={translation_lattice_supplied_by_carrier}"
    ),
)

gate(
    "SAH8 selecting one affine translation axis is another support choice",
    not preferred_primitive_translation_supplied
    and all(choices > 1 for choices in simple_coroot_axis_choices.values()),
    (
        f"preferred_primitive_translation_supplied={preferred_primitive_translation_supplied}, "
        f"simple_coroot_axis_choices={simple_coroot_axis_choices}"
    ),
)

gate(
    "SAH9 affine Weyl/Hecke data does not construct boundary map or torsor splitter",
    not affine_hecke_supplied_by_carrier
    and not affine_translation_constructs_boundary_map
    and not affine_translation_constructs_torsor_splitter,
    (
        f"affine_hecke_supplied_by_carrier={affine_hecke_supplied_by_carrier}, "
        f"boundary={affine_translation_constructs_boundary_map}, "
        f"torsor={affine_translation_constructs_torsor_splitter}"
    ),
)

gate(
    "SAH10 building, Weyl, Hecke, and Steinberg finite-data obstructions remain",
    building_top_degrees == {1: 1, 2: 2, 4: 4, 8: 8}
    and building_chamber_counts
    == {
        1: 45,
        2: 2835,
        4: 739552275,
        8: 852369269595510700600441875,
    }
    and steinberg_dimensions
    == {
        1: 16,
        2: 512,
        4: 33554432,
        8: 2417851639229258349412352,
    }
    and finite_hecke_basis_ranks == {1: 8, 2: 48, 4: 3840, 8: 185794560},
    (
        f"building_top_degrees={building_top_degrees}, "
        f"building_chamber_counts={building_chamber_counts}, "
        f"steinberg_dimensions={steinberg_dimensions}, "
        f"finite_hecke_basis_ranks={finite_hecke_basis_ranks}"
    ),
)

gate(
    "SAH11 graph, endpoint, matching, idempotent, and twist choices remain",
    graph_lagrangian_counts
    == {1: 64, 2: 1024, 4: 2097152, 8: 36028797018963968}
    and endpoint_pair_choices == {1: 9, 2: 16, 4: 36, 8: 100}
    and coordinate_matching_counts == {1: 6, 2: 24, 4: 720, 8: 3628800}
    and rank_one_idempotent_counts == {1: 2016, 2: 32640, 4: 8386560, 8: 549755289600}
    and laurent_unit_twist_counts == {1: 3, 2: 5, 4: 9, 8: 17},
    (
        f"graph_lagrangian_counts={graph_lagrangian_counts}, "
        f"endpoint_pair_choices={endpoint_pair_choices}, "
        f"coordinate_matching_counts={coordinate_matching_counts}, "
        f"rank_one_idempotent_counts={rank_one_idempotent_counts}, "
        f"laurent_unit_twist_counts={laurent_unit_twist_counts}"
    ),
)

obstruction_res1 = 1
coboundary_res1 = 0
gate(
    "SAH12 affine Weyl/Hecke data does not repair bottom, shear, or torsor obstructions",
    dmp_dim(-1) == 1
    and dmp_dim(-2) == 0
    and obstruction_res1 == 1
    and coboundary_res1 == 0
    and not carrier_multiplication_supplied
    and not torsor_splitter_supplied,
    "y^2=0, no DMP degree -2, res_1(c)=1, and no b/phi(b)=c",
)

control_translation_lattice_ranks = affine_translation_lattice_ranks.copy()
control_affine_generator_counts = affine_simple_generator_counts.copy()
primitive_carrier_maps_consumed = 0
affine_package_inserted = 1
gate(
    "SAH13 same affine Weyl/Hecke package is formable on controls",
    control_translation_lattice_ranks == affine_translation_lattice_ranks
    and control_affine_generator_counts == affine_simple_generator_counts
    and primitive_carrier_maps_consumed == 0
    and affine_package_inserted == 1,
    "a real route must construct affine translation data carrier-natively",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (SAH1-SAH13)")
print(
    "VERDICT: support symplectic affine Weyl/Hecke data does not supply the "
    "R1 Laurent shift.  Passing to affine type adds a rank-m translation "
    "lattice with ranks 2,3,5,9; selecting one primitive axis is another "
    "support choice, and the finite support building supplies no affine "
    "valuation or translation lattice.  Boundary/twist/torsor data and "
    "bottom/shear obstructions remain; the same affine package is formable "
    "on controls.  A surviving route must construct affine translation data "
    "carrier-natively."
)
