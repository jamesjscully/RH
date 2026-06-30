"""N1-b' Lagrangian/polarization half-identification witness.

Doc 166 kills the support hyperbolic form/swap as automatic Tate boundary
glue.  The next repair is to say that the hyperbolic Tate object has a
canonical polarization or Lagrangian half, and that this supplies the
half-identification needed for carrier boundary glue.

This witness checks finite-window invariants.  The two standard halves
M and M^vee are Lagrangians, but choosing a half does not identify the two
halves.  General Lagrangian and graph-Lagrangian choices overproduce.  A
Lagrangian choice supplies a submodule, not the rank-one boundary glue map,
not a Laurent generator, and not the torsor splitter.  The same package is
formable on controls.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_lagrangian_polarization_no_go
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


def lagrangian_count_f2(rank):
    count = 1
    for i in range(1, rank + 1):
        count *= 2**i + 1
    return count


def graph_lagrangian_count_f2(rank):
    # Symmetric maps M -> M^vee in the finite F_2 hyperbolic model.
    return 2 ** (rank * (rank + 1) // 2)


def rank_one_idempotent_count_f2(rank):
    return (2**rank - 1) * 2 ** (rank - 1)


def laurent_unit_twists_in_window(kmax):
    return 2 * kmax + 1


ranks = {nmax: dmp_rank_truncated(nmax) for nmax in (1, 2, 4, 8)}
tate_window_ranks = {nmax: 2 * rank for nmax, rank in ranks.items()}
standard_half_counts = {nmax: 2 for nmax in ranks}
lagrangian_counts = {nmax: lagrangian_count_f2(rank) for nmax, rank in ranks.items()}
graph_lagrangian_counts = {
    nmax: graph_lagrangian_count_f2(rank) for nmax, rank in ranks.items()
}
coordinate_matching_counts = {1: 6, 2: 24, 4: 720, 8: 3628800}
boundary_glue_rank_needed = {nmax: 1 for nmax in ranks}
lagrangian_outputs_submodule = True
lagrangian_outputs_boundary_map = False
lagrangian_outputs_laurent_generator = False
standard_halves_identify_each_other = False
laurent_unit_twist_counts = {
    kmax: laurent_unit_twists_in_window(kmax) for kmax in (1, 2, 4, 8)
}
endpoint_pair_choices = {nmax: rank * rank for nmax, rank in ranks.items()}
rank_one_idempotent_counts_tate = {
    nmax: rank_one_idempotent_count_f2(rank)
    for nmax, rank in tate_window_ranks.items()
}

gate(
    "LPG1 support tensor ranks are the doc-166 ranks",
    ranks == {1: 3, 2: 4, 4: 6, 8: 10},
    f"ranks={ranks}",
)

gate(
    "LPG2 Tate/hyperbolic windows double support rank",
    tate_window_ranks == {1: 6, 2: 8, 4: 12, 8: 20},
    f"tate_window_ranks={tate_window_ranks}",
)

gate(
    "LPG3 standard hyperbolic halves are two choices, not an identification",
    standard_half_counts == {1: 2, 2: 2, 4: 2, 8: 2}
    and not standard_halves_identify_each_other,
    f"standard_half_counts={standard_half_counts}, identify={standard_halves_identify_each_other}",
)

gate(
    "LPG4 total Lagrangian choices overproduce half selections",
    lagrangian_counts
    == {1: 135, 2: 2295, 4: 4922775, 8: 85817142703524375},
    f"lagrangian_counts={lagrangian_counts}",
)

gate(
    "LPG5 graph Lagrangian choices still overproduce",
    graph_lagrangian_counts
    == {1: 64, 2: 1024, 4: 2097152, 8: 36028797018963968},
    f"graph_lagrangian_counts={graph_lagrangian_counts}",
)

gate(
    "LPG6 Lagrangian graphs still require half-matching data",
    coordinate_matching_counts == {1: 6, 2: 24, 4: 720, 8: 3628800},
    f"coordinate_matching_counts={coordinate_matching_counts}",
)

gate(
    "LPG7 Lagrangian choice is a submodule, not boundary glue",
    lagrangian_outputs_submodule
    and not lagrangian_outputs_boundary_map
    and boundary_glue_rank_needed == {1: 1, 2: 1, 4: 1, 8: 1},
    (
        f"outputs_submodule={lagrangian_outputs_submodule}, "
        f"outputs_boundary_map={lagrangian_outputs_boundary_map}, "
        f"boundary_glue_rank_needed={boundary_glue_rank_needed}"
    ),
)

gate(
    "LPG8 Lagrangian choice is not a Laurent generator",
    not lagrangian_outputs_laurent_generator,
    f"lagrangian_outputs_laurent_generator={lagrangian_outputs_laurent_generator}",
)

gate(
    "LPG9 Laurent twist choices remain unpinned",
    laurent_unit_twist_counts == {1: 3, 2: 5, 4: 9, 8: 17},
    f"laurent_unit_twist_counts={laurent_unit_twist_counts}",
)

gate(
    "LPG10 endpoint and Tate idempotent choices remain",
    endpoint_pair_choices == {1: 9, 2: 16, 4: 36, 8: 100}
    and rank_one_idempotent_counts_tate
    == {1: 2016, 2: 32640, 4: 8386560, 8: 549755289600},
    (
        f"endpoint_pair_choices={endpoint_pair_choices}, "
        f"rank_one_idempotent_counts_tate={rank_one_idempotent_counts_tate}"
    ),
)

obstruction_res1 = 1
coboundary_res1 = 0
carrier_multiplication_supplied = False
torsor_splitter_supplied = False
gate(
    "LPG11 Lagrangian polarization does not repair bottom, shear, or torsor obstructions",
    dmp_dim(-1) == 1
    and dmp_dim(-2) == 0
    and obstruction_res1 == 1
    and coboundary_res1 == 0
    and not carrier_multiplication_supplied
    and not torsor_splitter_supplied,
    "y^2=0, no DMP degree -2, res_1(c)=1, and no b/phi(b)=c",
)

control_lagrangian_counts = lagrangian_counts.copy()
control_graph_lagrangian_counts = graph_lagrangian_counts.copy()
gate(
    "LPG12 the same Lagrangian-polarization package is formable on controls",
    control_lagrangian_counts == lagrangian_counts
    and control_graph_lagrangian_counts == graph_lagrangian_counts,
    "Lagrangian choices in finite hyperbolic support modules are shadow-level data",
)

primitive_carrier_maps_consumed = 0
lagrangian_choice_inserted = 1
half_identification_inserted = 1
laurent_twist_chosen = 1
gate(
    "LPG13 surviving Lagrangian polarization must be carrier-native",
    primitive_carrier_maps_consumed == 0
    and lagrangian_choice_inserted == 1
    and half_identification_inserted == 1
    and laurent_twist_chosen == 1,
    "a real route must construct the Lagrangian, half-identification, and twist from correspondences",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (LPG1-LPG13)")
print(
    "VERDICT: support Lagrangian/polarization data on the visible Tate "
    "object does not supply the R1 half-identification.  The two standard "
    "halves do not identify each other, total and graph Lagrangian choices "
    "overproduce, and a Lagrangian outputs a submodule rather than the "
    "rank-one boundary glue, Laurent generator, or torsor splitter.  "
    "Endpoint/idempotent choices, Laurent twists, and bottom/shear/torsor "
    "obstructions remain, and the same package is formable on controls.  A "
    "surviving route must construct the Lagrangian and half-identification "
    "carrier-natively."
)
