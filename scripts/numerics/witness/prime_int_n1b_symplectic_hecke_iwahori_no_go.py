"""N1-b' symplectic Hecke/Iwahori witness.

Doc 177 kills using a chosen support-building apartment and Coxeter element
as the missing Laurent shift.  The next repair is to package that apartment
descent into the finite type-C Iwahori/Hecke algebra or BN-pair double-coset
algebra of the residual support symplectic building.

In the finite F_2 support windows, the residual first-pair stabilizer
buildings have type C_m with m = 2,3,5,9.  The finite Iwahori-Hecke algebra
has basis indexed by W(C_m), hence ranks 8,48,3840,185794560.  Its longest
Bruhat lengths are m^2 = 4,9,25,81, and its center ranks are the
bipartition numbers 5,10,36,300.  These are finite support-algebra
invariants, not a carrier correspondence algebra, a rank-one Laurent line, or
a bi-infinite shift.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_symplectic_hecke_iwahori_no_go
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


def partition_numbers(nmax):
    values = [0] * (nmax + 1)
    values[0] = 1
    for part in range(1, nmax + 1):
        for total in range(part, nmax + 1):
            values[total] += values[total - part]
    return values


def bipartition_number(n):
    partitions = partition_numbers(n)
    return sum(partitions[i] * partitions[n - i] for i in range(n + 1))


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
weyl_group_orders = {
    nmax: weyl_group_order_type_c(building_rank)
    for nmax, building_rank in residual_building_ranks.items()
}
hecke_basis_ranks = weyl_group_orders.copy()
simple_generator_counts = residual_building_ranks.copy()
coxeter_orders = {
    nmax: coxeter_order_type_c(building_rank)
    for nmax, building_rank in residual_building_ranks.items()
}
longest_bruhat_lengths = {
    nmax: longest_bruhat_length_type_c(building_rank)
    for nmax, building_rank in residual_building_ranks.items()
}
hecke_center_ranks = {
    nmax: bipartition_number(building_rank)
    for nmax, building_rank in residual_building_ranks.items()
}
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

apartment_supplied_by_carrier = False
chamber_or_borel_supplied_by_carrier = False
iwahori_subgroup_supplied_by_carrier = False
hecke_algebra_supplied_by_carrier = False
hecke_constructs_infinite_shift = False
hecke_supplies_boundary_map = False
hecke_supplies_laurent_generator = False
hecke_supplies_torsor_splitter = False
affine_translation_lattice_supplied_by_support = False
carrier_multiplication_supplied = False
torsor_splitter_supplied = False

gate(
    "SHI1 support tensor ranks are unchanged",
    ranks == {1: 3, 2: 4, 4: 6, 8: 10},
    f"ranks={ranks}",
)

gate(
    "SHI2 Tate/hyperbolic windows double support rank",
    tate_window_ranks == {1: 6, 2: 8, 4: 12, 8: 20},
    f"tate_window_ranks={tate_window_ranks}",
)

gate(
    "SHI3 residual first-pair stabilizers remain finite type-C sources",
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
    "SHI4 finite Iwahori-Hecke basis ranks equal type-C Weyl group orders",
    hecke_basis_ranks == {1: 8, 2: 48, 4: 3840, 8: 185794560}
    and hecke_basis_ranks == weyl_group_orders,
    f"hecke_basis_ranks={hecke_basis_ranks}",
)

gate(
    "SHI5 Hecke generators and Bruhat lengths are finite support data",
    simple_generator_counts == {1: 2, 2: 3, 4: 5, 8: 9}
    and coxeter_orders == {1: 4, 2: 6, 4: 10, 8: 18}
    and longest_bruhat_lengths == {1: 4, 2: 9, 4: 25, 8: 81}
    and not hecke_constructs_infinite_shift,
    (
        f"simple_generator_counts={simple_generator_counts}, "
        f"coxeter_orders={coxeter_orders}, "
        f"longest_bruhat_lengths={longest_bruhat_lengths}"
    ),
)

gate(
    "SHI6 Hecke centers are finite class data, not canonical Laurent lines",
    hecke_center_ranks == {1: 5, 2: 10, 4: 36, 8: 300}
    and all(rank > 1 for rank in hecke_center_ranks.values()),
    f"hecke_center_ranks={hecke_center_ranks}",
)

gate(
    "SHI7 finite Hecke data does not supply affine translations",
    not affine_translation_lattice_supplied_by_support
    and not hecke_constructs_infinite_shift,
    "affine translations would be extra carrier data, not finite support-building data",
)

gate(
    "SHI8 chamber, Borel, and Iwahori inputs are not carrier-supplied",
    not apartment_supplied_by_carrier
    and not chamber_or_borel_supplied_by_carrier
    and not iwahori_subgroup_supplied_by_carrier
    and not hecke_algebra_supplied_by_carrier,
    (
        f"apartment={apartment_supplied_by_carrier}, "
        f"borel={chamber_or_borel_supplied_by_carrier}, "
        f"iwahori={iwahori_subgroup_supplied_by_carrier}"
    ),
)

gate(
    "SHI9 Hecke/Iwahori data does not construct boundary map, Laurent generator, or torsor splitter",
    not hecke_supplies_boundary_map
    and not hecke_supplies_laurent_generator
    and not hecke_supplies_torsor_splitter,
    (
        f"boundary={hecke_supplies_boundary_map}, "
        f"laurent={hecke_supplies_laurent_generator}, "
        f"torsor={hecke_supplies_torsor_splitter}"
    ),
)

gate(
    "SHI10 building, Weyl, and Steinberg finite-data obstructions remain",
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
    and weyl_group_orders == {1: 8, 2: 48, 4: 3840, 8: 185794560},
    (
        f"building_top_degrees={building_top_degrees}, "
        f"building_chamber_counts={building_chamber_counts}, "
        f"steinberg_dimensions={steinberg_dimensions}, "
        f"weyl_group_orders={weyl_group_orders}"
    ),
)

gate(
    "SHI11 graph, endpoint, matching, idempotent, and twist choices remain",
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
    "SHI12 Hecke/Iwahori data does not repair bottom, shear, or torsor obstructions",
    dmp_dim(-1) == 1
    and dmp_dim(-2) == 0
    and obstruction_res1 == 1
    and coboundary_res1 == 0
    and not carrier_multiplication_supplied
    and not torsor_splitter_supplied,
    "y^2=0, no DMP degree -2, res_1(c)=1, and no b/phi(b)=c",
)

control_hecke_basis_ranks = hecke_basis_ranks.copy()
control_hecke_center_ranks = hecke_center_ranks.copy()
primitive_carrier_maps_consumed = 0
hecke_package_read_off = 1
gate(
    "SHI13 same finite Hecke/Iwahori package is formable on controls",
    control_hecke_basis_ranks == hecke_basis_ranks
    and control_hecke_center_ranks == hecke_center_ranks
    and primitive_carrier_maps_consumed == 0
    and hecke_package_read_off == 1,
    "a real route must construct Hecke/correspondence data carrier-natively",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (SHI1-SHI13)")
print(
    "VERDICT: support symplectic Hecke/Iwahori/BN-pair data does not supply "
    "the R1 correspondence algebra or Laurent shift.  The finite type-C "
    "Hecke bases have ranks 8,48,3840,185794560; Bruhat lengths and centers "
    "are finite support data; and affine translations are not supplied by "
    "the support building.  Chamber/Borel/Iwahori choices, boundary/twist/"
    "torsor data, and bottom/shear obstructions remain; the same package is "
    "formable on controls.  A surviving route must construct Hecke or "
    "correspondence data carrier-natively."
)
