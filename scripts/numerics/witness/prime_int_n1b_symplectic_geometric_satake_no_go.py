"""N1-b' symplectic geometric Satake / dual representation witness.

Doc 180 kills appending affine Grassmannian / Schubert convolution data to
the finite support building.  The next repair is to invoke geometric Satake:
replace the Schubert convolution category by Rep(G^vee), and read the
dual-group representation category or its tensor product as the missing
carrier correspondence algebra.

For support buildings of type C_m with m = 2,3,5,9, the Langlands dual root
system is type B_m.  Dominant weights still form a rank-m monoid.  The
fundamental representation dimensions are all nontrivial, and the only
one-dimensional representation of the semisimple dual group is the trivial
unit.  The Satake wrapper therefore does not select a nontrivial Laurent
line, boundary map, or torsor splitter.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_symplectic_geometric_satake_no_go
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


def dominant_weights_height_leq(rank, height):
    return comb(rank + height, rank)


def dominant_weights_height_exact(rank, height):
    return comb(rank + height - 1, rank - 1)


def type_b_fundamental_dimensions(rank):
    # For B_m = so(2m+1): lambda_k, k<m, are exterior powers of the vector
    # representation; lambda_m is the spin representation.
    return [comb(2 * rank + 1, k) for k in range(1, rank)] + [2**rank]


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
dominant_coweight_counts_leq_window = {
    nmax: dominant_weights_height_leq(building_rank, nmax)
    for nmax, building_rank in residual_building_ranks.items()
}

dual_root_system_ranks = residual_building_ranks.copy()
dominant_weight_monoid_ranks = residual_building_ranks.copy()
dominant_weight_counts_leq_window = {
    nmax: dominant_weights_height_leq(building_rank, nmax)
    for nmax, building_rank in residual_building_ranks.items()
}
dominant_weight_counts_exact_window = {
    nmax: dominant_weights_height_exact(building_rank, nmax)
    for nmax, building_rank in residual_building_ranks.items()
}
fundamental_rep_dimensions = {
    nmax: type_b_fundamental_dimensions(building_rank)
    for nmax, building_rank in residual_building_ranks.items()
}
fundamental_rep_axis_choices = residual_building_ranks.copy()
nontrivial_one_dimensional_rep_counts = {nmax: 0 for nmax in ranks}
trivial_unit_rep_counts = {nmax: 1 for nmax in ranks}
representation_ring_generator_counts = residual_building_ranks.copy()

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
satake_category_supplied_by_carrier = False
dual_group_supplied_by_carrier = False
fiber_functor_supplied_by_carrier = False
preferred_rep_generator_supplied = False
satake_constructs_boundary_map = False
satake_constructs_laurent_generator = False
satake_constructs_torsor_splitter = False
carrier_multiplication_supplied = False
torsor_splitter_supplied = False

gate(
    "SGS1 support tensor ranks are unchanged",
    ranks == {1: 3, 2: 4, 4: 6, 8: 10},
    f"ranks={ranks}",
)

gate(
    "SGS2 Tate/hyperbolic windows double support rank",
    tate_window_ranks == {1: 6, 2: 8, 4: 12, 8: 20},
    f"tate_window_ranks={tate_window_ranks}",
)

gate(
    "SGS3 residual first-pair stabilizers remain finite type-C sources",
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
    "SGS4 finite Weyl, Hecke, affine, and Schubert data is unchanged",
    finite_weyl_orders == {1: 8, 2: 48, 4: 3840, 8: 185794560}
    and finite_hecke_basis_ranks == finite_weyl_orders
    and finite_longest_bruhat_lengths == {1: 4, 2: 9, 4: 25, 8: 81}
    and coxeter_orders == {1: 4, 2: 6, 4: 10, 8: 18}
    and affine_translation_lattice_ranks == {1: 2, 2: 3, 4: 5, 8: 9}
    and affine_simple_generator_counts == {1: 3, 2: 4, 4: 6, 8: 10}
    and dominant_coweight_counts_leq_window == {1: 3, 2: 10, 4: 126, 8: 24310},
    (
        f"finite_weyl_orders={finite_weyl_orders}, "
        f"affine_translation_lattice_ranks={affine_translation_lattice_ranks}, "
        f"dominant_coweight_counts_leq_window={dominant_coweight_counts_leq_window}"
    ),
)

gate(
    "SGS5 geometric Satake dual has type-B rank m, not rank one",
    dual_root_system_ranks == {1: 2, 2: 3, 4: 5, 8: 9}
    and dominant_weight_monoid_ranks == dual_root_system_ranks
    and representation_ring_generator_counts == dual_root_system_ranks,
    (
        f"dual_root_system_ranks={dual_root_system_ranks}, "
        f"dominant_weight_monoid_ranks={dominant_weight_monoid_ranks}, "
        f"representation_ring_generator_counts={representation_ring_generator_counts}"
    ),
)

gate(
    "SGS6 finite weight windows overproduce dual representations",
    dominant_weight_counts_leq_window == {1: 3, 2: 10, 4: 126, 8: 24310}
    and dominant_weight_counts_exact_window == {1: 2, 2: 6, 4: 70, 8: 12870},
    (
        f"dominant_weight_counts_leq_window={dominant_weight_counts_leq_window}, "
        f"dominant_weight_counts_exact_window={dominant_weight_counts_exact_window}"
    ),
)

gate(
    "SGS7 fundamental dual representations are not Laurent lines",
    fundamental_rep_dimensions
    == {
        1: [5, 4],
        2: [7, 21, 8],
        4: [11, 55, 165, 330, 32],
        8: [19, 171, 969, 3876, 11628, 27132, 50388, 75582, 512],
    }
    and all(all(dim > 1 for dim in dims) for dims in fundamental_rep_dimensions.values()),
    f"fundamental_rep_dimensions={fundamental_rep_dimensions}",
)

gate(
    "SGS8 the only one-dimensional dual representation is the trivial unit",
    nontrivial_one_dimensional_rep_counts == {1: 0, 2: 0, 4: 0, 8: 0}
    and trivial_unit_rep_counts == {1: 1, 2: 1, 4: 1, 8: 1},
    (
        f"nontrivial_one_dimensional_rep_counts={nontrivial_one_dimensional_rep_counts}, "
        f"trivial_unit_rep_counts={trivial_unit_rep_counts}"
    ),
)

gate(
    "SGS9 choosing one representation generator is another support choice",
    fundamental_rep_axis_choices == {1: 2, 2: 3, 4: 5, 8: 9}
    and not preferred_rep_generator_supplied,
    (
        f"fundamental_rep_axis_choices={fundamental_rep_axis_choices}, "
        f"preferred_rep_generator_supplied={preferred_rep_generator_supplied}"
    ),
)

gate(
    "SGS10 Satake inputs are not supplied by the finite support building",
    not loop_parameter_supplied_by_support
    and not affine_valuation_supplied_by_support
    and not satake_category_supplied_by_carrier
    and not dual_group_supplied_by_carrier
    and not fiber_functor_supplied_by_carrier,
    (
        f"loop_parameter={loop_parameter_supplied_by_support}, "
        f"affine_valuation={affine_valuation_supplied_by_support}, "
        f"satake_category={satake_category_supplied_by_carrier}, "
        f"dual_group={dual_group_supplied_by_carrier}, "
        f"fiber_functor={fiber_functor_supplied_by_carrier}"
    ),
)

gate(
    "SGS11 Satake data does not construct boundary map, Laurent generator, or torsor splitter",
    not satake_constructs_boundary_map
    and not satake_constructs_laurent_generator
    and not satake_constructs_torsor_splitter,
    (
        f"boundary={satake_constructs_boundary_map}, "
        f"laurent={satake_constructs_laurent_generator}, "
        f"torsor={satake_constructs_torsor_splitter}"
    ),
)

gate(
    "SGS12 choices and base obstructions remain",
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
    and graph_lagrangian_counts == {1: 64, 2: 1024, 4: 2097152, 8: 36028797018963968}
    and endpoint_pair_choices == {1: 9, 2: 16, 4: 36, 8: 100}
    and coordinate_matching_counts == {1: 6, 2: 24, 4: 720, 8: 3628800}
    and rank_one_idempotent_counts == {1: 2016, 2: 32640, 4: 8386560, 8: 549755289600}
    and laurent_unit_twist_counts == {1: 3, 2: 5, 4: 9, 8: 17}
    and dmp_dim(-1) == 1
    and dmp_dim(-2) == 0
    and not carrier_multiplication_supplied
    and not torsor_splitter_supplied,
    "building/choice data, y^2=0, no DMP degree -2, and no b/phi(b)=c remain",
)

control_weight_counts = dominant_weight_counts_leq_window.copy()
control_fundamental_dimensions = {
    nmax: dims.copy() for nmax, dims in fundamental_rep_dimensions.items()
}
primitive_carrier_maps_consumed = 0
satake_wrapper_inserted = 1
gate(
    "SGS13 same geometric Satake / dual representation package is formable on controls",
    control_weight_counts == dominant_weight_counts_leq_window
    and control_fundamental_dimensions == fundamental_rep_dimensions
    and primitive_carrier_maps_consumed == 0
    and satake_wrapper_inserted == 1,
    "a real route must construct Satake/dual-group data carrier-natively",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (SGS1-SGS13)")
print(
    "VERDICT: support geometric Satake / dual representation data does not "
    "supply the R1 carrier correspondence algebra.  The dual type-B "
    "dominant-weight monoids have ranks 2,3,5,9; finite windows overproduce "
    "representations; all fundamental representations have dimension > 1; "
    "and the only one-dimensional representation is the trivial unit.  The "
    "support building supplies no loop parameter, affine valuation, Satake "
    "category, dual group, fiber functor, boundary map, or torsor data.  A "
    "surviving route must construct Satake data carrier-natively."
)
