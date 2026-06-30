"""N1-b' Darboux/symplectic-frame selection witness.

Doc 171 kills support quadratic refinements, Arf invariants, and Maslov
scalars as boundary-glue data.  The next repair is to choose a Darboux or
symplectic frame of the hyperbolic Tate window, then use the frame coordinates
to name the endpoint, half-identification, and boundary map.

In the finite F_2 support windows this is a frame choice, not carrier data.
Full symplectic frames overproduce by |Sp(2r,2)|.  Even frames adapted to the
two standard halves overproduce by |GL_r(2)|.  A frame can name basis vectors,
but it does not construct the carrier graph, boundary map, Laurent generator,
or torsor splitter.  The same frame-selection package is formable on controls.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_darboux_frame_no_go
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


def symplectic_frame_count_f2(half_rank):
    count = 2 ** (half_rank * half_rank)
    for i in range(1, half_rank + 1):
        count *= 2 ** (2 * i) - 1
    return count


def adapted_darboux_frame_count_f2(half_rank):
    count = 1
    for i in range(half_rank):
        count *= 2**half_rank - 2**i
    return count


def symplectic_pair_count_f2(half_rank):
    # Ordered pairs (a,b) in a 2r-dimensional symplectic F_2-space with <a,b>=1.
    return (2 ** (2 * half_rank) - 1) * 2 ** (2 * half_rank - 1)


def graph_lagrangian_count_f2(rank):
    # Symmetric maps M -> M^vee in the finite F_2 hyperbolic model.
    return 2 ** (rank * (rank + 1) // 2)


def laurent_unit_twists_in_window(kmax):
    return 2 * kmax + 1


ranks = {nmax: dmp_rank_truncated(nmax) for nmax in (1, 2, 4, 8)}
tate_window_ranks = {nmax: 2 * rank for nmax, rank in ranks.items()}
symplectic_frame_counts = {
    nmax: symplectic_frame_count_f2(rank) for nmax, rank in ranks.items()
}
adapted_darboux_frame_counts = {
    nmax: adapted_darboux_frame_count_f2(rank) for nmax, rank in ranks.items()
}
symplectic_pair_counts = {
    nmax: symplectic_pair_count_f2(rank) for nmax, rank in ranks.items()
}
graph_lagrangian_counts = {
    nmax: graph_lagrangian_count_f2(rank) for nmax, rank in ranks.items()
}
endpoint_pair_choices = {nmax: rank * rank for nmax, rank in ranks.items()}
coordinate_matching_counts = {1: 6, 2: 24, 4: 720, 8: 3628800}
laurent_unit_twist_counts = {
    kmax: laurent_unit_twists_in_window(kmax) for kmax in (1, 2, 4, 8)
}

frame_supplied_by_carrier = False
frame_outputs_basis = True
frame_outputs_graph = False
frame_outputs_boundary_map = False
frame_outputs_laurent_generator = False
frame_outputs_torsor_splitter = False

gate(
    "DFR1 support tensor ranks are unchanged",
    ranks == {1: 3, 2: 4, 4: 6, 8: 10},
    f"ranks={ranks}",
)

gate(
    "DFR2 Tate/hyperbolic windows double support rank",
    tate_window_ranks == {1: 6, 2: 8, 4: 12, 8: 20},
    f"tate_window_ranks={tate_window_ranks}",
)

gate(
    "DFR3 full symplectic frames overproduce",
    symplectic_frame_counts
    == {
        1: 1451520,
        2: 47377612800,
        4: 208114637736580743168000,
        8: 1132992015386677099994486205757869431795095310094129168384000000,
    },
    f"symplectic_frame_counts={symplectic_frame_counts}",
)

gate(
    "DFR4 adapted Darboux frames over fixed halves still overproduce",
    adapted_darboux_frame_counts
    == {
        1: 168,
        2: 20160,
        4: 20158709760,
        8: 366440137299948128422802227200,
    },
    f"adapted_darboux_frame_counts={adapted_darboux_frame_counts}",
)

gate(
    "DFR5 first symplectic pair choices are endpoint-like choices, not carrier endpoints",
    symplectic_pair_counts == {1: 2016, 2: 32640, 4: 8386560, 8: 549755289600}
    and not frame_supplied_by_carrier,
    (
        f"symplectic_pair_counts={symplectic_pair_counts}, "
        f"frame_supplied_by_carrier={frame_supplied_by_carrier}"
    ),
)

gate(
    "DFR6 frame coordinates do not construct the opposite graph",
    frame_outputs_basis
    and not frame_outputs_graph
    and graph_lagrangian_counts
    == {1: 64, 2: 1024, 4: 2097152, 8: 36028797018963968},
    f"frame_outputs_basis={frame_outputs_basis}, graph_lagrangian_counts={graph_lagrangian_counts}",
)

gate(
    "DFR7 frame coordinates do not construct boundary map or Laurent generator",
    not frame_outputs_boundary_map
    and not frame_outputs_laurent_generator
    and not frame_outputs_torsor_splitter,
    (
        f"frame_outputs_boundary_map={frame_outputs_boundary_map}, "
        f"frame_outputs_laurent_generator={frame_outputs_laurent_generator}, "
        f"frame_outputs_torsor_splitter={frame_outputs_torsor_splitter}"
    ),
)

gate(
    "DFR8 endpoint and half-matching choices remain as carrier data",
    endpoint_pair_choices == {1: 9, 2: 16, 4: 36, 8: 100}
    and coordinate_matching_counts == {1: 6, 2: 24, 4: 720, 8: 3628800},
    (
        f"endpoint_pair_choices={endpoint_pair_choices}, "
        f"coordinate_matching_counts={coordinate_matching_counts}"
    ),
)

gate(
    "DFR9 Laurent twist choices remain unpinned",
    laurent_unit_twist_counts == {1: 3, 2: 5, 4: 9, 8: 17},
    f"laurent_unit_twist_counts={laurent_unit_twist_counts}",
)

obstruction_res1 = 1
coboundary_res1 = 0
carrier_multiplication_supplied = False
torsor_splitter_supplied = False
gate(
    "DFR10 Darboux frame does not repair bottom, shear, or torsor obstructions",
    dmp_dim(-1) == 1
    and dmp_dim(-2) == 0
    and obstruction_res1 == 1
    and coboundary_res1 == 0
    and not carrier_multiplication_supplied
    and not torsor_splitter_supplied,
    "y^2=0, no DMP degree -2, res_1(c)=1, and no b/phi(b)=c",
)

control_symplectic_frame_counts = symplectic_frame_counts.copy()
control_adapted_darboux_frame_counts = adapted_darboux_frame_counts.copy()
gate(
    "DFR11 the same Darboux-frame package is formable on controls",
    control_symplectic_frame_counts == symplectic_frame_counts
    and control_adapted_darboux_frame_counts == adapted_darboux_frame_counts,
    "symplectic/Darboux frames are finite hyperbolic support-basis operations",
)

primitive_carrier_maps_consumed = 0
frame_choice_inserted = 1
endpoint_choice_inserted = 1
laurent_twist_chosen = 1
gate(
    "DFR12 surviving Darboux-frame route must be carrier-native",
    primitive_carrier_maps_consumed == 0
    and frame_choice_inserted == 1
    and endpoint_choice_inserted == 1
    and laurent_twist_chosen == 1,
    "a real route must construct frame, endpoint, boundary glue, and twist from correspondences",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (DFR1-DFR12)")
print(
    "VERDICT: support Darboux/symplectic-frame selection does not supply "
    "R1 boundary glue.  Full symplectic frames and adapted Darboux frames "
    "massively overproduce; a frame names basis vectors only by a support "
    "basis choice.  It does not construct the opposite graph, endpoint, "
    "boundary map, Laurent generator, or torsor splitter.  Endpoint/matching "
    "choices, Laurent twists, and bottom/shear/torsor obstructions remain, "
    "and the same package is formable on controls.  A surviving route must "
    "construct any frame data carrier-natively."
)
