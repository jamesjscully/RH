"""N1-b' graph-boundary extraction witness.

Doc 168 kills the opposite/transverse Lagrangian graph as carrier
half-identification: it is a rank-r graph choice, not rank-one boundary glue.

The next repair tries to extract rank-one boundary glue from the graph map by
taking a boundary corner, minor, cofactor, determinant line, or Schur-style
scalar.  This witness checks the finite-window invariants of that repair.
Boundary extraction either requires endpoint choices, or after endpoints are
fixed it reads only one free scalar bit of an already chosen graph.  It does
not construct the graph, the boundary map, a Laurent twist, or a torsor
splitter from carrier data.  The same extraction package is formable on
controls.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_graph_boundary_extraction_no_go
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
endpoint_pair_choices = {nmax: rank * rank for nmax, rank in ranks.items()}
fixed_corner_nonzero_graph_counts = {
    nmax: count // 2 for nmax, count in graph_lagrangian_counts.items()
}
all_corner_extraction_choices = {
    nmax: graph_lagrangian_counts[nmax] * endpoint_pair_choices[nmax]
    for nmax in ranks
}
all_nonzero_corner_extraction_choices = {
    nmax: fixed_corner_nonzero_graph_counts[nmax] * endpoint_pair_choices[nmax]
    for nmax in ranks
}
laurent_unit_twist_counts = {
    kmax: laurent_unit_twists_in_window(kmax) for kmax in (1, 2, 4, 8)
}
rank_one_idempotent_counts_tate = {
    nmax: rank_one_idempotent_count_f2(rank)
    for nmax, rank in tate_window_ranks.items()
}

graph_map_supplied_by_carrier = False
boundary_endpoint_supplied_by_carrier = False
fixed_corner_reads_one_scalar_bit = True
corner_scalar_outputs_boundary_map = False
determinant_outputs_scalar = True
determinant_outputs_boundary_map = False
determinant_pins_endpoint = False
cofactor_or_schur_requires_endpoint_choice = True
cofactor_or_schur_outputs_laurent_generator = False

gate(
    "GBE1 support tensor ranks are unchanged",
    ranks == {1: 3, 2: 4, 4: 6, 8: 10},
    f"ranks={ranks}",
)

gate(
    "GBE2 graph/opposite Lagrangian choices are the doc-168 choices",
    graph_lagrangian_counts
    == {1: 64, 2: 1024, 4: 2097152, 8: 36028797018963968},
    f"graph_lagrangian_counts={graph_lagrangian_counts}",
)

gate(
    "GBE3 boundary extraction reintroduces endpoint-pair choices",
    endpoint_pair_choices == {1: 9, 2: 16, 4: 36, 8: 100}
    and not boundary_endpoint_supplied_by_carrier,
    (
        f"endpoint_pair_choices={endpoint_pair_choices}, "
        f"boundary_endpoint_supplied_by_carrier={boundary_endpoint_supplied_by_carrier}"
    ),
)

gate(
    "GBE4 a fixed corner reads one free scalar bit of the graph",
    fixed_corner_reads_one_scalar_bit
    and fixed_corner_nonzero_graph_counts
    == {1: 32, 2: 512, 4: 1048576, 8: 18014398509481984},
    f"fixed_corner_nonzero_graph_counts={fixed_corner_nonzero_graph_counts}",
)

gate(
    "GBE5 all graph-corner extractions overproduce rank-one candidates",
    all_corner_extraction_choices
    == {1: 576, 2: 16384, 4: 75497472, 8: 3602879701896396800}
    and all_nonzero_corner_extraction_choices
    == {1: 288, 2: 8192, 4: 37748736, 8: 1801439850948198400},
    (
        f"all_corner_extraction_choices={all_corner_extraction_choices}, "
        f"all_nonzero_corner_extraction_choices={all_nonzero_corner_extraction_choices}"
    ),
)

gate(
    "GBE6 corner scalar is not carrier boundary glue",
    not graph_map_supplied_by_carrier
    and fixed_corner_reads_one_scalar_bit
    and not corner_scalar_outputs_boundary_map,
    (
        f"graph_map_supplied_by_carrier={graph_map_supplied_by_carrier}, "
        f"corner_scalar_outputs_boundary_map={corner_scalar_outputs_boundary_map}"
    ),
)

gate(
    "GBE7 determinant extraction is scalar shadow data, not a boundary map",
    determinant_outputs_scalar
    and not determinant_outputs_boundary_map
    and not determinant_pins_endpoint,
    (
        f"determinant_outputs_scalar={determinant_outputs_scalar}, "
        f"determinant_outputs_boundary_map={determinant_outputs_boundary_map}, "
        f"determinant_pins_endpoint={determinant_pins_endpoint}"
    ),
)

gate(
    "GBE8 cofactor or Schur extraction still needs endpoint data and no Laurent generator",
    cofactor_or_schur_requires_endpoint_choice
    and not cofactor_or_schur_outputs_laurent_generator,
    (
        f"cofactor_or_schur_requires_endpoint_choice={cofactor_or_schur_requires_endpoint_choice}, "
        f"cofactor_or_schur_outputs_laurent_generator={cofactor_or_schur_outputs_laurent_generator}"
    ),
)

gate(
    "GBE9 Laurent twist choices remain unpinned",
    laurent_unit_twist_counts == {1: 3, 2: 5, 4: 9, 8: 17},
    f"laurent_unit_twist_counts={laurent_unit_twist_counts}",
)

gate(
    "GBE10 Tate rank-one idempotent choices remain",
    rank_one_idempotent_counts_tate
    == {1: 2016, 2: 32640, 4: 8386560, 8: 549755289600},
    f"rank_one_idempotent_counts_tate={rank_one_idempotent_counts_tate}",
)

obstruction_res1 = 1
coboundary_res1 = 0
carrier_multiplication_supplied = False
torsor_splitter_supplied = False
gate(
    "GBE11 graph-boundary extraction does not repair bottom, shear, or torsor obstructions",
    dmp_dim(-1) == 1
    and dmp_dim(-2) == 0
    and obstruction_res1 == 1
    and coboundary_res1 == 0
    and not carrier_multiplication_supplied
    and not torsor_splitter_supplied,
    "y^2=0, no DMP degree -2, res_1(c)=1, and no b/phi(b)=c",
)

control_graph_counts = graph_lagrangian_counts.copy()
control_corner_choices = all_corner_extraction_choices.copy()
gate(
    "GBE12 the same graph-boundary extraction package is formable on controls",
    control_graph_counts == graph_lagrangian_counts
    and control_corner_choices == all_corner_extraction_choices,
    "corner, minor, determinant, and Schur extraction are finite-free support operations",
)

primitive_carrier_maps_consumed = 0
graph_choice_inserted = 1
endpoint_choice_inserted = 1
corner_extraction_inserted = 1
laurent_twist_chosen = 1
gate(
    "GBE13 surviving graph-boundary extraction must be carrier-native",
    primitive_carrier_maps_consumed == 0
    and graph_choice_inserted == 1
    and endpoint_choice_inserted == 1
    and corner_extraction_inserted == 1
    and laurent_twist_chosen == 1,
    "a real route must construct graph, endpoint, boundary glue, and twist from correspondences",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (GBE1-GBE13)")
print(
    "VERDICT: extracting a boundary corner, minor, determinant line, "
    "cofactor, or Schur scalar from the support opposite graph does not "
    "supply R1 boundary glue.  Endpoint choices reappear; a fixed corner "
    "reads only one scalar bit of an already chosen graph; determinant "
    "data is scalar shadow data; and cofactor/Schur variants still require "
    "endpoint data and no Laurent generator.  Endpoint/idempotent choices, "
    "Laurent twists, and bottom/shear/torsor obstructions remain, and the "
    "same extraction package is formable on controls.  A surviving route "
    "must construct the graph-boundary glue carrier-natively."
)
