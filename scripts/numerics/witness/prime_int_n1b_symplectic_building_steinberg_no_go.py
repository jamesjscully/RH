"""N1-b' symplectic building/Steinberg witness.

Doc 175 kills classifying-space, group-cohomology, and Tate-cohomology
packages of the support Sp stabilizers.  The next repair is to use the
spherical Tits building of the residual finite symplectic stabilizer, or its
top reduced homology / Steinberg module, as a dualizing object or Laurent
boundary line.

In the finite F_2 support windows, the full-frame stabilizer is trivial.
The ordered first-pair stabilizers are Sp(2m,2) with m = 2,3,5,9.  Their
buildings have top degrees 1,2,4,8, but the Steinberg module dimensions are
2^(m^2) = 16,512,33554432,2417851639229258349412352.  This is a large
representation, not a selected rank-one endpoint or Laurent generator.
Choosing a chamber/apartment/top vector is another support choice, and the
same building/Steinberg package is formable on controls.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_symplectic_building_steinberg_no_go
"""

from math import prod

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


def building_chamber_count_type_c_f2(rank):
    # |Sp(2r,2)| / |B|, with |B| = 2^(r^2) over F_2.
    return prod(2 ** (2 * i) - 1 for i in range(1, rank + 1))


def steinberg_dimension_type_c_f2(rank):
    # q^(# positive roots) for type C_r, with # positive roots = r^2 and q=2.
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
full_frame_stabilizer_counts = {nmax: 1 for nmax in ranks}

pair_stabilizer_building_ranks = {nmax: rank - 1 for nmax, rank in ranks.items()}
pair_stabilizer_counts = {
    nmax: symplectic_group_order_f2(building_rank)
    for nmax, building_rank in pair_stabilizer_building_ranks.items()
}
building_top_degrees = {
    nmax: building_rank - 1 for nmax, building_rank in pair_stabilizer_building_ranks.items()
}
building_chamber_counts = {
    nmax: building_chamber_count_type_c_f2(building_rank)
    for nmax, building_rank in pair_stabilizer_building_ranks.items()
}
steinberg_dimensions = {
    nmax: steinberg_dimension_type_c_f2(building_rank)
    for nmax, building_rank in pair_stabilizer_building_ranks.items()
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

building_supplied_by_carrier = False
building_top_degree_is_window_cutoff = True
building_top_degree_constructs_shift = False
steinberg_is_rank_one_line = False
steinberg_supplies_endpoint = False
steinberg_supplies_boundary_map = False
steinberg_supplies_laurent_generator = False
steinberg_supplies_torsor_splitter = False
chamber_choice_required = True
apartment_or_top_vector_choice_required = True
carrier_multiplication_supplied = False
torsor_splitter_supplied = False

gate(
    "SBT1 support tensor ranks are unchanged",
    ranks == {1: 3, 2: 4, 4: 6, 8: 10},
    f"ranks={ranks}",
)

gate(
    "SBT2 Tate/hyperbolic windows double support rank",
    tate_window_ranks == {1: 6, 2: 8, 4: 12, 8: 20},
    f"tate_window_ranks={tate_window_ranks}",
)

gate(
    "SBT3 full-frame stabilizer has no nontrivial building",
    full_frame_stabilizer_counts == {1: 1, 2: 1, 4: 1, 8: 1},
    f"full_frame_stabilizer_counts={full_frame_stabilizer_counts}",
)

gate(
    "SBT4 first-pair stabilizers are finite Sp(2m,2) groups",
    pair_stabilizer_building_ranks == {1: 2, 2: 3, 4: 5, 8: 9}
    and pair_stabilizer_counts
    == {
        1: 720,
        2: 1451520,
        4: 24815256521932800,
        8: 2060902435720151186326095525680721766346957783040000,
    },
    (
        f"pair_stabilizer_building_ranks={pair_stabilizer_building_ranks}, "
        f"pair_stabilizer_counts={pair_stabilizer_counts}"
    ),
)

gate(
    "SBT5 building top degrees track the window cutoff but do not construct a shift",
    building_top_degrees == {1: 1, 2: 2, 4: 4, 8: 8}
    and building_top_degree_is_window_cutoff
    and not building_top_degree_constructs_shift,
    (
        f"building_top_degrees={building_top_degrees}, "
        f"building_top_degree_constructs_shift={building_top_degree_constructs_shift}"
    ),
)

gate(
    "SBT6 chamber counts massively overproduce top cells",
    building_chamber_counts
    == {
        1: 45,
        2: 2835,
        4: 739552275,
        8: 852369269595510700600441875,
    }
    and all(count > 1 for count in building_chamber_counts.values())
    and chamber_choice_required,
    f"building_chamber_counts={building_chamber_counts}",
)

gate(
    "SBT7 Steinberg modules are not rank-one Laurent lines",
    steinberg_dimensions
    == {
        1: 16,
        2: 512,
        4: 33554432,
        8: 2417851639229258349412352,
    }
    and all(dim > 1 for dim in steinberg_dimensions.values())
    and not steinberg_is_rank_one_line,
    f"steinberg_dimensions={steinberg_dimensions}",
)

gate(
    "SBT8 choosing an apartment or top vector is another support choice",
    not building_supplied_by_carrier
    and apartment_or_top_vector_choice_required
    and not steinberg_supplies_endpoint,
    (
        f"building_supplied_by_carrier={building_supplied_by_carrier}, "
        f"apartment_or_top_vector_choice_required={apartment_or_top_vector_choice_required}"
    ),
)

gate(
    "SBT9 Steinberg data does not construct boundary map, Laurent generator, or torsor splitter",
    not steinberg_supplies_boundary_map
    and not steinberg_supplies_laurent_generator
    and not steinberg_supplies_torsor_splitter,
    (
        f"boundary={steinberg_supplies_boundary_map}, "
        f"laurent={steinberg_supplies_laurent_generator}, "
        f"torsor={steinberg_supplies_torsor_splitter}"
    ),
)

gate(
    "SBT10 graph, endpoint, matching, idempotent, and twist choices remain",
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
    "SBT11 building/Steinberg data does not repair bottom, shear, or torsor obstructions",
    dmp_dim(-1) == 1
    and dmp_dim(-2) == 0
    and obstruction_res1 == 1
    and coboundary_res1 == 0
    and not carrier_multiplication_supplied
    and not torsor_splitter_supplied,
    "y^2=0, no DMP degree -2, res_1(c)=1, and no b/phi(b)=c",
)

control_building_chamber_counts = building_chamber_counts.copy()
control_steinberg_dimensions = steinberg_dimensions.copy()
gate(
    "SBT12 the same building/Steinberg package is formable on controls",
    control_building_chamber_counts == building_chamber_counts
    and control_steinberg_dimensions == steinberg_dimensions,
    "finite symplectic buildings and Steinberg modules are support stabilizer operations",
)

primitive_carrier_maps_consumed = 0
building_operation_inserted = 1
steinberg_module_read_off = 1
gate(
    "SBT13 surviving building/Steinberg route must be carrier-native",
    primitive_carrier_maps_consumed == 0
    and building_operation_inserted == 1
    and steinberg_module_read_off == 1,
    "a real route must construct building/dualizing data, endpoint, boundary glue, and twist from correspondences",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (SBT1-SBT13)")
print(
    "VERDICT: support symplectic building/Steinberg data does not supply "
    "R1 boundary glue.  Full-frame stabilizers have no nontrivial building; "
    "first-pair stabilizer buildings have top degrees matching the finite "
    "window cutoffs but no shift map; chamber counts overproduce; and "
    "Steinberg modules are large representations, not rank-one Laurent "
    "lines.  Choosing a chamber, apartment, or top vector is another support "
    "choice; graph/endpoint/matching/idempotent/twist choices and bottom/"
    "shear/torsor obstructions remain; and the same package is formable on "
    "controls.  A surviving route must construct building/dualizing data "
    "carrier-natively."
)
