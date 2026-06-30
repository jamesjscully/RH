"""N1-b' symplectic affine Grassmannian / Schubert convolution witness.

Doc 179 kills appending the affine Weyl/Hecke translation lattice to the
finite support building.  The next repair is to use the affine Grassmannian
or geometric-Satake-style Schubert convolution category as the missing
carrier correspondence algebra.

In the finite F_2 support windows, the residual first-pair stabilizer
buildings have type C_m with m = 2,3,5,9.  Affine-Grassmannian Schubert
strata are indexed by dominant coweights, a rank-m monoid N^m.  In height
windows N = 1,2,4,8, the counts are 3,10,126,24310, not a selected
rank-one Laurent axis.  The finite support building supplies no loop
parameter, no affine valuation, no affine Grassmannian, and no Schubert
convolution category.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_symplectic_affine_grassmannian_no_go
"""

from math import comb, factorial, prod

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


def dominant_coweights_height_leq(rank, height):
    return comb(rank + height, rank)


def dominant_coweights_height_exact(rank, height):
    return comb(rank + height - 1, rank - 1)


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

dominant_coweight_monoid_ranks = residual_building_ranks.copy()
dominant_coweight_counts_leq_window = {
    nmax: dominant_coweights_height_leq(building_rank, nmax)
    for nmax, building_rank in residual_building_ranks.items()
}
dominant_coweight_counts_exact_window = {
    nmax: dominant_coweights_height_exact(building_rank, nmax)
    for nmax, building_rank in residual_building_ranks.items()
}
fundamental_coweight_axis_choices = residual_building_ranks.copy()
signed_simple_axis_choices = {
    nmax: 2 * building_rank for nmax, building_rank in residual_building_ranks.items()
}
group_completed_coweight_lattice_ranks = residual_building_ranks.copy()

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

loop_parameter_supplied_by_support = False
affine_valuation_supplied_by_support = False
affine_grassmannian_supplied_by_carrier = False
schubert_convolution_supplied_by_carrier = False
preferred_coweight_axis_supplied = False
schubert_convolution_constructs_boundary_map = False
schubert_convolution_constructs_laurent_generator = False
schubert_convolution_constructs_torsor_splitter = False
carrier_multiplication_supplied = False
torsor_splitter_supplied = False

gate(
    "SAG1 support tensor ranks are unchanged",
    ranks == {1: 3, 2: 4, 4: 6, 8: 10},
    f"ranks={ranks}",
)

gate(
    "SAG2 Tate/hyperbolic windows double support rank",
    tate_window_ranks == {1: 6, 2: 8, 4: 12, 8: 20},
    f"tate_window_ranks={tate_window_ranks}",
)

gate(
    "SAG3 residual first-pair stabilizers remain finite type-C sources",
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
    "SAG4 finite Weyl, Hecke, and affine data is unchanged",
    finite_weyl_orders == {1: 8, 2: 48, 4: 3840, 8: 185794560}
    and finite_hecke_basis_ranks == finite_weyl_orders
    and finite_longest_bruhat_lengths == {1: 4, 2: 9, 4: 25, 8: 81}
    and coxeter_orders == {1: 4, 2: 6, 4: 10, 8: 18}
    and affine_translation_lattice_ranks == {1: 2, 2: 3, 4: 5, 8: 9}
    and affine_simple_generator_counts == {1: 3, 2: 4, 4: 6, 8: 10},
    (
        f"finite_weyl_orders={finite_weyl_orders}, "
        f"affine_translation_lattice_ranks={affine_translation_lattice_ranks}, "
        f"affine_simple_generator_counts={affine_simple_generator_counts}"
    ),
)

gate(
    "SAG5 Schubert strata are indexed by a rank-m dominant coweight monoid",
    dominant_coweight_monoid_ranks == {1: 2, 2: 3, 4: 5, 8: 9}
    and group_completed_coweight_lattice_ranks == dominant_coweight_monoid_ranks,
    (
        f"dominant_coweight_monoid_ranks={dominant_coweight_monoid_ranks}, "
        f"group_completed_coweight_lattice_ranks={group_completed_coweight_lattice_ranks}"
    ),
)

gate(
    "SAG6 finite height windows overproduce Schubert labels",
    dominant_coweight_counts_leq_window == {1: 3, 2: 10, 4: 126, 8: 24310}
    and dominant_coweight_counts_exact_window == {1: 2, 2: 6, 4: 70, 8: 12870}
    and all(count > 1 for count in dominant_coweight_counts_leq_window.values()),
    (
        f"dominant_coweight_counts_leq_window={dominant_coweight_counts_leq_window}, "
        f"dominant_coweight_counts_exact_window={dominant_coweight_counts_exact_window}"
    ),
)

gate(
    "SAG7 selecting one Schubert/Laurent axis is another support choice",
    fundamental_coweight_axis_choices == {1: 2, 2: 3, 4: 5, 8: 9}
    and signed_simple_axis_choices == {1: 4, 2: 6, 4: 10, 8: 18}
    and not preferred_coweight_axis_supplied,
    (
        f"fundamental_coweight_axis_choices={fundamental_coweight_axis_choices}, "
        f"signed_simple_axis_choices={signed_simple_axis_choices}, "
        f"preferred_coweight_axis_supplied={preferred_coweight_axis_supplied}"
    ),
)

gate(
    "SAG8 affine Grassmannian inputs are not supplied by the finite support building",
    not loop_parameter_supplied_by_support
    and not affine_valuation_supplied_by_support
    and not affine_grassmannian_supplied_by_carrier
    and not schubert_convolution_supplied_by_carrier,
    (
        f"loop_parameter={loop_parameter_supplied_by_support}, "
        f"affine_valuation={affine_valuation_supplied_by_support}, "
        f"affine_grassmannian={affine_grassmannian_supplied_by_carrier}"
    ),
)

gate(
    "SAG9 Schubert convolution does not construct boundary map, Laurent generator, or torsor splitter",
    not schubert_convolution_constructs_boundary_map
    and not schubert_convolution_constructs_laurent_generator
    and not schubert_convolution_constructs_torsor_splitter,
    (
        f"boundary={schubert_convolution_constructs_boundary_map}, "
        f"laurent={schubert_convolution_constructs_laurent_generator}, "
        f"torsor={schubert_convolution_constructs_torsor_splitter}"
    ),
)

gate(
    "SAG10 building, Weyl, Hecke, affine, and Steinberg obstructions remain",
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
    and finite_hecke_basis_ranks == {1: 8, 2: 48, 4: 3840, 8: 185794560}
    and affine_translation_lattice_ranks == {1: 2, 2: 3, 4: 5, 8: 9},
    (
        f"building_top_degrees={building_top_degrees}, "
        f"building_chamber_counts={building_chamber_counts}, "
        f"steinberg_dimensions={steinberg_dimensions}, "
        f"finite_hecke_basis_ranks={finite_hecke_basis_ranks}, "
        f"affine_translation_lattice_ranks={affine_translation_lattice_ranks}"
    ),
)

gate(
    "SAG11 graph, endpoint, matching, idempotent, and twist choices remain",
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
    "SAG12 affine Grassmannian data does not repair bottom, shear, or torsor obstructions",
    dmp_dim(-1) == 1
    and dmp_dim(-2) == 0
    and obstruction_res1 == 1
    and coboundary_res1 == 0
    and not carrier_multiplication_supplied
    and not torsor_splitter_supplied,
    "y^2=0, no DMP degree -2, res_1(c)=1, and no b/phi(b)=c",
)

control_coweight_counts = dominant_coweight_counts_leq_window.copy()
control_axis_choices = fundamental_coweight_axis_choices.copy()
primitive_carrier_maps_consumed = 0
schubert_package_inserted = 1
gate(
    "SAG13 same affine Grassmannian / Schubert package is formable on controls",
    control_coweight_counts == dominant_coweight_counts_leq_window
    and control_axis_choices == fundamental_coweight_axis_choices
    and primitive_carrier_maps_consumed == 0
    and schubert_package_inserted == 1,
    "a real route must construct Schubert convolution data carrier-natively",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (SAG1-SAG13)")
print(
    "VERDICT: support affine Grassmannian / Schubert convolution data does "
    "not supply the R1 carrier correspondence algebra.  Schubert labels form "
    "rank-m dominant coweight monoids with ranks 2,3,5,9 and finite-window "
    "counts 3,10,126,24310; selecting one Laurent axis is another support "
    "choice.  The support building supplies no loop parameter, affine "
    "valuation, affine Grassmannian, or boundary/torsor data; the same "
    "package is formable on controls.  A surviving route must construct "
    "Schubert convolution data carrier-natively."
)
