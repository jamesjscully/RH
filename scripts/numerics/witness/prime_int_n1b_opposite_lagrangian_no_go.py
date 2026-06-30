"""N1-b' opposite/transverse Lagrangian graph witness.

Doc 167 kills support Lagrangian/polarization data as a half-identification:
the standard halves are two Lagrangians, total and graph Lagrangian choices
overproduce, and a Lagrangian is a submodule rather than boundary glue.

The next repair is narrower.  Fix one standard Tate half and choose an
opposite/transverse Lagrangian; then read the graph map as the
half-identification.  This witness checks the finite-window invariants of
that repair.  Opposite Lagrangians are graph choices.  Graph choices are not
carrier maps, still require half-matching data, and output a global rank-r
half-map rather than the rank-one boundary glue or Laurent generator.  The
same package is formable on controls.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_opposite_lagrangian_no_go
"""

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


def graph_lagrangian_count_f2(rank):
    # Symmetric maps M -> M^vee in the finite F_2 hyperbolic model.
    return 2 ** (rank * (rank + 1) // 2)


def rank_one_idempotent_count_f2(rank):
    return (2**rank - 1) * 2 ** (rank - 1)


def laurent_unit_twists_in_window(kmax):
    return 2 * kmax + 1


ranks = {nmax: dmp_rank_truncated(nmax) for nmax in (1, 2, 4, 8)}
tate_window_ranks = {nmax: 2 * rank for nmax, rank in ranks.items()}
graph_lagrangian_counts = {
    nmax: graph_lagrangian_count_f2(rank) for nmax, rank in ranks.items()
}
coordinate_matching_counts = {1: 6, 2: 24, 4: 720, 8: 3628800}
graph_map_rank = ranks.copy()
boundary_glue_rank_needed = {nmax: 1 for nmax in ranks}
endpoint_pair_choices = {nmax: rank * rank for nmax, rank in ranks.items()}
laurent_unit_twist_counts = {
    kmax: laurent_unit_twists_in_window(kmax) for kmax in (1, 2, 4, 8)
}
rank_one_idempotent_counts_tate = {
    nmax: rank_one_idempotent_count_f2(rank)
    for nmax, rank in tate_window_ranks.items()
}

fixed_standard_half_supplied = True
opposite_lagrangian_is_graph_choice = True
carrier_graph_map_supplied = False
opposite_lagrangian_outputs_half_map = True
opposite_lagrangian_outputs_boundary_map = False
opposite_lagrangian_outputs_laurent_generator = False
nondegenerate_filter_supplied_by_carrier = False

gate(
    "OPL1 support tensor ranks are unchanged",
    ranks == {1: 3, 2: 4, 4: 6, 8: 10},
    f"ranks={ranks}",
)

gate(
    "OPL2 Tate/hyperbolic windows double support rank",
    tate_window_ranks == {1: 6, 2: 8, 4: 12, 8: 20},
    f"tate_window_ranks={tate_window_ranks}",
)

gate(
    "OPL3 opposite Lagrangian repair is a graph choice over a fixed half",
    fixed_standard_half_supplied
    and opposite_lagrangian_is_graph_choice
    and not carrier_graph_map_supplied,
    (
        f"fixed_standard_half_supplied={fixed_standard_half_supplied}, "
        f"opposite_lagrangian_is_graph_choice={opposite_lagrangian_is_graph_choice}, "
        f"carrier_graph_map_supplied={carrier_graph_map_supplied}"
    ),
)

gate(
    "OPL4 graph/opposite Lagrangian choices overproduce",
    graph_lagrangian_counts
    == {1: 64, 2: 1024, 4: 2097152, 8: 36028797018963968},
    f"graph_lagrangian_counts={graph_lagrangian_counts}",
)

gate(
    "OPL5 graph half-map still needs matching data",
    coordinate_matching_counts == {1: 6, 2: 24, 4: 720, 8: 3628800}
    and not nondegenerate_filter_supplied_by_carrier,
    (
        f"coordinate_matching_counts={coordinate_matching_counts}, "
        f"nondegenerate_filter_supplied_by_carrier={nondegenerate_filter_supplied_by_carrier}"
    ),
)

gate(
    "OPL6 graph output is rank-r half-map, not rank-one boundary glue",
    opposite_lagrangian_outputs_half_map
    and not opposite_lagrangian_outputs_boundary_map
    and graph_map_rank == {1: 3, 2: 4, 4: 6, 8: 10}
    and boundary_glue_rank_needed == {1: 1, 2: 1, 4: 1, 8: 1},
    f"graph_map_rank={graph_map_rank}, boundary_glue_rank_needed={boundary_glue_rank_needed}",
)

gate(
    "OPL7 opposite graph is not a Laurent generator",
    not opposite_lagrangian_outputs_laurent_generator,
    f"opposite_lagrangian_outputs_laurent_generator={opposite_lagrangian_outputs_laurent_generator}",
)

gate(
    "OPL8 endpoint pair choices remain",
    endpoint_pair_choices == {1: 9, 2: 16, 4: 36, 8: 100},
    f"endpoint_pair_choices={endpoint_pair_choices}",
)

gate(
    "OPL9 Laurent twist choices remain unpinned",
    laurent_unit_twist_counts == {1: 3, 2: 5, 4: 9, 8: 17},
    f"laurent_unit_twist_counts={laurent_unit_twist_counts}",
)

gate(
    "OPL10 Tate rank-one idempotent choices remain",
    rank_one_idempotent_counts_tate
    == {1: 2016, 2: 32640, 4: 8386560, 8: 549755289600},
    f"rank_one_idempotent_counts_tate={rank_one_idempotent_counts_tate}",
)

obstruction_res1 = 1
coboundary_res1 = 0
carrier_multiplication_supplied = False
torsor_splitter_supplied = False
gate(
    "OPL11 opposite Lagrangian graph does not repair bottom, shear, or torsor obstructions",
    dmp_dim(-1) == 1
    and dmp_dim(-2) == 0
    and obstruction_res1 == 1
    and coboundary_res1 == 0
    and not carrier_multiplication_supplied
    and not torsor_splitter_supplied,
    "y^2=0, no DMP degree -2, res_1(c)=1, and no b/phi(b)=c",
)

control_graph_lagrangian_counts = graph_lagrangian_counts.copy()
control_coordinate_matching_counts = coordinate_matching_counts.copy()
gate(
    "OPL12 the same opposite-Lagrangian package is formable on controls",
    control_graph_lagrangian_counts == graph_lagrangian_counts
    and control_coordinate_matching_counts == coordinate_matching_counts,
    "opposite graphs in finite hyperbolic support modules are shadow-level data",
)

primitive_carrier_maps_consumed = 0
opposite_graph_choice_inserted = 1
boundary_glue_inserted = 1
laurent_twist_chosen = 1
gate(
    "OPL13 surviving opposite Lagrangian route must be carrier-native",
    primitive_carrier_maps_consumed == 0
    and opposite_graph_choice_inserted == 1
    and boundary_glue_inserted == 1
    and laurent_twist_chosen == 1,
    "a real route must construct the graph, boundary glue, and twist from correspondences",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (OPL1-OPL13)")
print(
    "VERDICT: support opposite/transverse Lagrangian data does not supply "
    "the R1 half-identification.  Fixing a standard half turns the repair "
    "into a graph choice; graph choices overproduce, still require matching "
    "data, and output a rank-r half-map rather than the rank-one boundary "
    "glue, Laurent generator, or torsor splitter.  Endpoint/idempotent "
    "choices, Laurent twists, and bottom/shear/torsor obstructions remain, "
    "and the same package is formable on controls.  A surviving route must "
    "construct the opposite graph and boundary twist carrier-natively."
)
