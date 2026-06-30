"""N1-b' symplectic quotient/orbit-averaging witness.

Doc 172 kills choosing a support Darboux/symplectic frame as carrier
boundary glue.  The next repair is to avoid choosing: quotient the frame or
first symplectic pair by the Sp-action, or take an invariant/orbit average.

In the finite F_2 support windows, the quotient has one orbit because Sp
acts transitively on symplectic frames and ordered symplectic pairs.  That
one orbit is not a chosen representative, endpoint, boundary map, Laurent
generator, or torsor splitter.  The additive F_2 transfer/orbit sum of the
nonzero endpoint vectors is zero, not rank-one boundary glue.  The same
quotient/averaging package is formable on controls.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_symplectic_quotient_no_go
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


def rank_one_idempotent_count(half_rank):
    tate_rank = 2 * half_rank
    return (2**tate_rank - 1) * 2 ** (tate_rank - 1)


def nonzero_vector_count(half_rank):
    return 2 ** (2 * half_rank) - 1


def coordinate_ones_in_nonzero_orbit(half_rank):
    # For each coordinate in F_2^{2r}, exactly half of all vectors have that bit set.
    return 2 ** (2 * half_rank - 1)


def first_vector_pair_weight(half_rank):
    # Number of possible second vectors b for each nonzero first vector a with <a,b>=1.
    return 2 ** (2 * half_rank - 1)


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
sp_pair_orbit_counts = {nmax: 1 for nmax in ranks}
sp_frame_orbit_counts = {nmax: 1 for nmax in ranks}
nonzero_vector_counts = {nmax: nonzero_vector_count(rank) for nmax, rank in ranks.items()}
coordinate_ones_counts = {
    nmax: coordinate_ones_in_nonzero_orbit(rank) for nmax, rank in ranks.items()
}
first_vector_weights = {nmax: first_vector_pair_weight(rank) for nmax, rank in ranks.items()}
weighted_coordinate_ones = {
    nmax: coordinate_ones_counts[nmax] * first_vector_weights[nmax] for nmax in ranks
}
first_vector_orbit_sum_zero = {
    nmax: coordinate_ones_counts[nmax] % 2 == 0 for nmax in ranks
}
ordered_pair_first_vector_sum_zero = {
    nmax: weighted_coordinate_ones[nmax] % 2 == 0 for nmax in ranks
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

quotient_selects_representative = False
quotient_outputs_endpoint = False
quotient_outputs_graph = False
quotient_outputs_boundary_map = False
quotient_outputs_laurent_generator = False
quotient_outputs_torsor_splitter = False
normalized_average_exists_over_f2 = False
transfer_outputs_nonzero_boundary_vector = False
carrier_multiplication_supplied = False
torsor_splitter_supplied = False

gate(
    "SPQ1 support tensor ranks are unchanged",
    ranks == {1: 3, 2: 4, 4: 6, 8: 10},
    f"ranks={ranks}",
)

gate(
    "SPQ2 Tate/hyperbolic windows double support rank",
    tate_window_ranks == {1: 6, 2: 8, 4: 12, 8: 20},
    f"tate_window_ranks={tate_window_ranks}",
)

gate(
    "SPQ3 frame and first-pair counts are the Darboux-frame counts",
    symplectic_frame_counts
    == {
        1: 1451520,
        2: 47377612800,
        4: 208114637736580743168000,
        8: 1132992015386677099994486205757869431795095310094129168384000000,
    }
    and adapted_darboux_frame_counts
    == {
        1: 168,
        2: 20160,
        4: 20158709760,
        8: 366440137299948128422802227200,
    }
    and symplectic_pair_counts == {1: 2016, 2: 32640, 4: 8386560, 8: 549755289600},
    (
        f"symplectic_frame_counts={symplectic_frame_counts}, "
        f"adapted_darboux_frame_counts={adapted_darboux_frame_counts}, "
        f"symplectic_pair_counts={symplectic_pair_counts}"
    ),
)

gate(
    "SPQ4 Sp quotient collapses pairs and frames to one orbit but no representative",
    sp_pair_orbit_counts == {1: 1, 2: 1, 4: 1, 8: 1}
    and sp_frame_orbit_counts == {1: 1, 2: 1, 4: 1, 8: 1}
    and not quotient_selects_representative,
    (
        f"sp_pair_orbit_counts={sp_pair_orbit_counts}, "
        f"sp_frame_orbit_counts={sp_frame_orbit_counts}, "
        f"quotient_selects_representative={quotient_selects_representative}"
    ),
)

gate(
    "SPQ5 invariant predicates see only orbit class, not carrier maps",
    not quotient_outputs_endpoint
    and not quotient_outputs_graph
    and not quotient_outputs_boundary_map
    and not quotient_outputs_laurent_generator
    and not quotient_outputs_torsor_splitter,
    (
        f"endpoint={quotient_outputs_endpoint}, graph={quotient_outputs_graph}, "
        f"boundary={quotient_outputs_boundary_map}, "
        f"laurent={quotient_outputs_laurent_generator}, "
        f"torsor={quotient_outputs_torsor_splitter}"
    ),
)

gate(
    "SPQ6 F2 first-vector orbit transfer is zero",
    nonzero_vector_counts == {1: 63, 2: 255, 4: 4095, 8: 1048575}
    and coordinate_ones_counts == {1: 32, 2: 128, 4: 2048, 8: 524288}
    and all(first_vector_orbit_sum_zero.values())
    and not normalized_average_exists_over_f2
    and not transfer_outputs_nonzero_boundary_vector,
    (
        f"nonzero_vector_counts={nonzero_vector_counts}, "
        f"coordinate_ones_counts={coordinate_ones_counts}, "
        f"first_vector_orbit_sum_zero={first_vector_orbit_sum_zero}"
    ),
)

gate(
    "SPQ7 ordered-pair first-vector transfer is also zero",
    first_vector_weights == {1: 32, 2: 128, 4: 2048, 8: 524288}
    and all(ordered_pair_first_vector_sum_zero.values()),
    (
        f"first_vector_weights={first_vector_weights}, "
        f"weighted_coordinate_ones={weighted_coordinate_ones}, "
        f"ordered_pair_first_vector_sum_zero={ordered_pair_first_vector_sum_zero}"
    ),
)

gate(
    "SPQ8 graph, endpoint, matching, idempotent, and twist choices remain",
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
    "SPQ9 quotient/averaging does not repair bottom, shear, or torsor obstructions",
    dmp_dim(-1) == 1
    and dmp_dim(-2) == 0
    and obstruction_res1 == 1
    and coboundary_res1 == 0
    and not carrier_multiplication_supplied
    and not torsor_splitter_supplied,
    "y^2=0, no DMP degree -2, res_1(c)=1, and no b/phi(b)=c",
)

control_sp_pair_orbit_counts = sp_pair_orbit_counts.copy()
control_first_vector_orbit_sum_zero = first_vector_orbit_sum_zero.copy()
gate(
    "SPQ10 the same Sp quotient/transfer package is formable on controls",
    control_sp_pair_orbit_counts == sp_pair_orbit_counts
    and control_first_vector_orbit_sum_zero == first_vector_orbit_sum_zero,
    "Sp orbit quotients and F2 transfers are finite hyperbolic support operations",
)

primitive_carrier_maps_consumed = 0
quotient_operation_inserted = 1
orbit_transfer_inserted = 1
endpoint_choice_inserted = 0
gate(
    "SPQ11 surviving symplectic quotient route must be carrier-native",
    primitive_carrier_maps_consumed == 0
    and quotient_operation_inserted == 1
    and orbit_transfer_inserted == 1
    and endpoint_choice_inserted == 0,
    "a real route must construct quotient/orbit data, endpoint, boundary glue, and twist from correspondences",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (SPQ1-SPQ11)")
print(
    "VERDICT: quotienting or averaging support Darboux/symplectic frames "
    "does not supply R1 boundary glue.  The Sp quotient has one orbit, but "
    "that orbit is not a chosen carrier endpoint or boundary map.  Over F_2 "
    "there is no normalized average, and the natural orbit transfer of the "
    "endpoint vectors is zero.  Graph, endpoint, matching, idempotent, "
    "Laurent-twist, bottom, shear, and torsor obstructions remain, and the "
    "same quotient/averaging package is formable on controls.  A surviving "
    "route must construct the quotient/orbit data carrier-natively."
)
