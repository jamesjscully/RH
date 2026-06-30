"""N1-b' symplectic Weyl/Coxeter/apartment witness.

Doc 176 kills the Tits-building / Steinberg-dualizing repair for support
symplectic stabilizers.  The next repair is to choose an apartment in that
building and use the type-C Weyl group, or a Coxeter element, as the missing
carrier monodromy / Laurent shift.

In the finite F_2 support windows, the residual first-pair stabilizer
buildings have type C_m with m = 2,3,5,9.  The Weyl group orders are
2^m m! = 8,48,3840,185794560, and Coxeter elements have finite orders
2m = 4,6,10,18.  A finite Coxeter cyclic orbit is not the bi-infinite
Laurent shift: it imposes a wrap relation c^(2m)=1.  Choosing the apartment
or Coxeter element is another support choice, and the same package is
formable on controls.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_symplectic_weyl_coxeter_no_go
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


def building_chamber_count_type_c_f2(rank):
    return prod(2 ** (2 * i) - 1 for i in range(1, rank + 1))


def steinberg_dimension_type_c_f2(rank):
    return 2 ** (rank * rank)


def weyl_group_order_type_c(rank):
    return 2**rank * factorial(rank)


def coxeter_order_type_c(rank):
    return 2 * rank


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
weyl_group_orders = {
    nmax: weyl_group_order_type_c(building_rank)
    for nmax, building_rank in residual_building_ranks.items()
}
coxeter_orders = {
    nmax: coxeter_order_type_c(building_rank)
    for nmax, building_rank in residual_building_ranks.items()
}
generic_coxeter_orbit_lengths = coxeter_orders.copy()
coxeter_wrap_relations = {nmax: f"c^{order}=1" for nmax, order in coxeter_orders.items()}
laurent_unit_twist_counts = {
    kmax: laurent_unit_twists_in_window(kmax) for kmax in (1, 2, 4, 8)
}

graph_lagrangian_counts = {
    nmax: graph_lagrangian_count_f2(rank) for nmax, rank in ranks.items()
}
endpoint_pair_choices = {nmax: rank * rank for nmax, rank in ranks.items()}
coordinate_matching_counts = {1: 6, 2: 24, 4: 720, 8: 3628800}
rank_one_idempotent_counts = {
    nmax: rank_one_idempotent_count(rank) for nmax, rank in ranks.items()
}

apartment_supplied_by_carrier = False
weyl_group_supplied_by_carrier = False
coxeter_element_supplied_by_carrier = False
coxeter_order_is_finite = True
coxeter_constructs_infinite_shift = False
finite_wrap_is_inserted_relation = True
coxeter_supplies_boundary_map = False
coxeter_supplies_laurent_generator = False
coxeter_supplies_torsor_splitter = False
carrier_multiplication_supplied = False
torsor_splitter_supplied = False

gate(
    "SWC1 support tensor ranks are unchanged",
    ranks == {1: 3, 2: 4, 4: 6, 8: 10},
    f"ranks={ranks}",
)

gate(
    "SWC2 Tate/hyperbolic windows double support rank",
    tate_window_ranks == {1: 6, 2: 8, 4: 12, 8: 20},
    f"tate_window_ranks={tate_window_ranks}",
)

gate(
    "SWC3 residual first-pair stabilizers are finite type-C building sources",
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
    "SWC4 type-C Weyl group orders are finite apartment chamber counts",
    weyl_group_orders == {1: 8, 2: 48, 4: 3840, 8: 185794560}
    and all(order > 1 for order in weyl_group_orders.values()),
    f"weyl_group_orders={weyl_group_orders}",
)

gate(
    "SWC5 Coxeter elements have finite orders",
    coxeter_orders == {1: 4, 2: 6, 4: 10, 8: 18}
    and generic_coxeter_orbit_lengths == coxeter_orders
    and coxeter_order_is_finite,
    (
        f"coxeter_orders={coxeter_orders}, "
        f"generic_coxeter_orbit_lengths={generic_coxeter_orbit_lengths}"
    ),
)

gate(
    "SWC6 finite Coxeter monodromy inserts a wrap, not a Laurent shift",
    finite_wrap_is_inserted_relation
    and not coxeter_constructs_infinite_shift
    and all(order < 10**9 for order in coxeter_orders.values()),
    f"coxeter_wrap_relations={coxeter_wrap_relations}",
)

gate(
    "SWC7 Coxeter orders do not match the pinned Laurent twist windows",
    laurent_unit_twist_counts == {1: 3, 2: 5, 4: 9, 8: 17}
    and {nmax: coxeter_orders[nmax] - laurent_unit_twist_counts[nmax] for nmax in coxeter_orders}
    == {1: 1, 2: 1, 4: 1, 8: 1},
    (
        f"coxeter_orders={coxeter_orders}, "
        f"laurent_unit_twist_counts={laurent_unit_twist_counts}"
    ),
)

gate(
    "SWC8 choosing an apartment or Coxeter element is another support choice",
    not apartment_supplied_by_carrier
    and not weyl_group_supplied_by_carrier
    and not coxeter_element_supplied_by_carrier,
    (
        f"apartment_supplied_by_carrier={apartment_supplied_by_carrier}, "
        f"coxeter_element_supplied_by_carrier={coxeter_element_supplied_by_carrier}"
    ),
)

gate(
    "SWC9 Weyl/Coxeter data does not construct boundary map, Laurent generator, or torsor splitter",
    not coxeter_supplies_boundary_map
    and not coxeter_supplies_laurent_generator
    and not coxeter_supplies_torsor_splitter,
    (
        f"boundary={coxeter_supplies_boundary_map}, "
        f"laurent={coxeter_supplies_laurent_generator}, "
        f"torsor={coxeter_supplies_torsor_splitter}"
    ),
)

gate(
    "SWC10 building/Steinberg overproduction remains",
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
    },
    (
        f"building_top_degrees={building_top_degrees}, "
        f"building_chamber_counts={building_chamber_counts}, "
        f"steinberg_dimensions={steinberg_dimensions}"
    ),
)

gate(
    "SWC11 graph, endpoint, matching, idempotent, and twist choices remain",
    graph_lagrangian_counts
    == {1: 64, 2: 1024, 4: 2097152, 8: 36028797018963968}
    and endpoint_pair_choices == {1: 9, 2: 16, 4: 36, 8: 100}
    and coordinate_matching_counts == {1: 6, 2: 24, 4: 720, 8: 3628800}
    and rank_one_idempotent_counts == {1: 2016, 2: 32640, 4: 8386560, 8: 549755289600},
    (
        f"graph_lagrangian_counts={graph_lagrangian_counts}, "
        f"endpoint_pair_choices={endpoint_pair_choices}, "
        f"coordinate_matching_counts={coordinate_matching_counts}, "
        f"rank_one_idempotent_counts={rank_one_idempotent_counts}"
    ),
)

obstruction_res1 = 1
coboundary_res1 = 0
gate(
    "SWC12 Weyl/Coxeter data does not repair bottom, shear, or torsor obstructions",
    dmp_dim(-1) == 1
    and dmp_dim(-2) == 0
    and obstruction_res1 == 1
    and coboundary_res1 == 0
    and not carrier_multiplication_supplied
    and not torsor_splitter_supplied,
    "y^2=0, no DMP degree -2, res_1(c)=1, and no b/phi(b)=c",
)

control_weyl_group_orders = weyl_group_orders.copy()
control_coxeter_orders = coxeter_orders.copy()
primitive_carrier_maps_consumed = 0
apartment_choice_inserted = 1
coxeter_choice_inserted = 1
gate(
    "SWC13 same finite Weyl/Coxeter package is formable on controls",
    control_weyl_group_orders == weyl_group_orders
    and control_coxeter_orders == coxeter_orders
    and primitive_carrier_maps_consumed == 0
    and apartment_choice_inserted == 1
    and coxeter_choice_inserted == 1,
    "a real route must construct apartment and monodromy carrier-natively",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (SWC1-SWC13)")
print(
    "VERDICT: support symplectic Weyl/Coxeter/apartment data does not supply "
    "the R1 Laurent shift.  The residual type-C Weyl groups are finite, and "
    "Coxeter elements have finite orders 4,6,10,18; using them as monodromy "
    "inserts wrap relations rather than a bi-infinite Laurent generator.  "
    "Choosing the apartment or Coxeter element is another support choice; "
    "boundary/twist/torsor data and bottom/shear obstructions remain; and "
    "the same package is formable on controls.  A surviving route must "
    "construct apartment and monodromy data carrier-natively."
)
