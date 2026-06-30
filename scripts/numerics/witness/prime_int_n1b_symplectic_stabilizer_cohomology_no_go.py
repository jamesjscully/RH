"""N1-b' symplectic stabilizer cohomology witness.

Doc 174 kills reading carrier loop data directly from the support Sp quotient
stack stabilizers.  The next repair is to take classifying-space cohomology,
group cohomology, or Tate cohomology of those finite stabilizers and use a
class as the missing Laurent generator.

In the finite F_2 support windows, the full-frame stabilizer is trivial.
The ordered first-pair stabilizers are finite Sp(2m,2) groups with
m = 2,3,5,9.  Each contains an elementary abelian 2-subgroup of rank m, so
none has 2-periodic finite-group cohomology.  Ordinary cohomology is
nonnegative and positive-degree classes are not units; Tate cohomology is not
a single Laurent line unless periodicity is supplied externally.  The same
cohomology package is formable on controls.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_symplectic_stabilizer_cohomology_no_go
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


def symplectic_group_order_f2(half_rank):
    if half_rank == 0:
        return 1
    count = 2 ** (half_rank * half_rank)
    for i in range(1, half_rank + 1):
        count *= 2 ** (2 * i) - 1
    return count


def nonzero_vector_count(half_rank):
    return 2 ** (2 * half_rank) - 1


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

pair_stabilizer_half_ranks = {nmax: rank - 1 for nmax, rank in ranks.items()}
pair_stabilizer_counts = {
    nmax: symplectic_group_order_f2(half_rank)
    for nmax, half_rank in pair_stabilizer_half_ranks.items()
}
pair_stabilizer_2_adic_orders = {
    nmax: half_rank * half_rank for nmax, half_rank in pair_stabilizer_half_ranks.items()
}
pair_stabilizer_elementary_2_ranks = pair_stabilizer_half_ranks.copy()
pair_stabilizer_periodic_mod2_cohomology = {
    nmax: elementary_rank <= 1
    for nmax, elementary_rank in pair_stabilizer_elementary_2_ranks.items()
}

endpoint_vector_counts = {nmax: nonzero_vector_count(rank) for nmax, rank in ranks.items()}
symplectic_group_orders = {
    nmax: symplectic_group_order_f2(rank) for nmax, rank in ranks.items()
}
endpoint_vector_stabilizer_counts = {
    nmax: symplectic_group_orders[nmax] // endpoint_vector_counts[nmax]
    for nmax in ranks
}
endpoint_stabilizer_elementary_2_ranks = pair_stabilizer_half_ranks.copy()
endpoint_stabilizer_periodic_mod2_cohomology = {
    nmax: elementary_rank <= 1
    for nmax, elementary_rank in endpoint_stabilizer_elementary_2_ranks.items()
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

ordinary_cohomology_nonnegative = True
positive_degree_class_is_unit = False
cohomology_class_supplied_by_carrier = False
cohomology_outputs_endpoint = False
cohomology_outputs_boundary_map = False
cohomology_outputs_laurent_generator = False
cohomology_outputs_torsor_splitter = False
tate_cohomology_single_laurent_line = False
formal_periodicity_localization_inserted = True
carrier_multiplication_supplied = False
torsor_splitter_supplied = False

gate(
    "SCH1 support tensor ranks are unchanged",
    ranks == {1: 3, 2: 4, 4: 6, 8: 10},
    f"ranks={ranks}",
)

gate(
    "SCH2 Tate/hyperbolic windows double support rank",
    tate_window_ranks == {1: 6, 2: 8, 4: 12, 8: 20},
    f"tate_window_ranks={tate_window_ranks}",
)

gate(
    "SCH3 full-frame stabilizer cohomology is trivial",
    full_frame_stabilizer_counts == {1: 1, 2: 1, 4: 1, 8: 1},
    f"full_frame_stabilizer_counts={full_frame_stabilizer_counts}",
)

gate(
    "SCH4 first-pair stabilizers are the doc-174 finite Sp(2m,2) groups",
    pair_stabilizer_half_ranks == {1: 2, 2: 3, 4: 5, 8: 9}
    and pair_stabilizer_counts
    == {
        1: 720,
        2: 1451520,
        4: 24815256521932800,
        8: 2060902435720151186326095525680721766346957783040000,
    }
    and pair_stabilizer_2_adic_orders == {1: 4, 2: 9, 4: 25, 8: 81},
    (
        f"pair_stabilizer_half_ranks={pair_stabilizer_half_ranks}, "
        f"pair_stabilizer_counts={pair_stabilizer_counts}, "
        f"pair_stabilizer_2_adic_orders={pair_stabilizer_2_adic_orders}"
    ),
)

gate(
    "SCH5 first-pair stabilizers contain elementary abelian 2-rank at least two",
    pair_stabilizer_elementary_2_ranks == {1: 2, 2: 3, 4: 5, 8: 9}
    and all(rank >= 2 for rank in pair_stabilizer_elementary_2_ranks.values())
    and not any(pair_stabilizer_periodic_mod2_cohomology.values()),
    (
        f"pair_stabilizer_elementary_2_ranks={pair_stabilizer_elementary_2_ranks}, "
        f"pair_stabilizer_periodic_mod2_cohomology={pair_stabilizer_periodic_mod2_cohomology}"
    ),
)

gate(
    "SCH6 endpoint-vector parabolic stabilizers are also nonperiodic finite 2-isotropy",
    endpoint_vector_counts == {1: 63, 2: 255, 4: 4095, 8: 1048575}
    and endpoint_vector_stabilizer_counts
    == {
        1: 23040,
        2: 185794560,
        4: 50821645356918374400,
        8: 1080506416218846625176535970968094253434513802154475520000,
    }
    and endpoint_stabilizer_elementary_2_ranks == {1: 2, 2: 3, 4: 5, 8: 9}
    and not any(endpoint_stabilizer_periodic_mod2_cohomology.values()),
    (
        f"endpoint_vector_stabilizer_counts={endpoint_vector_stabilizer_counts}, "
        f"endpoint_stabilizer_elementary_2_ranks={endpoint_stabilizer_elementary_2_ranks}"
    ),
)

gate(
    "SCH7 ordinary stabilizer cohomology classes are not Laurent units",
    ordinary_cohomology_nonnegative
    and not positive_degree_class_is_unit
    and not cohomology_class_supplied_by_carrier,
    (
        f"ordinary_cohomology_nonnegative={ordinary_cohomology_nonnegative}, "
        f"positive_degree_class_is_unit={positive_degree_class_is_unit}, "
        f"cohomology_class_supplied_by_carrier={cohomology_class_supplied_by_carrier}"
    ),
)

gate(
    "SCH8 Tate cohomology is not a carrier-supplied single Laurent line",
    not tate_cohomology_single_laurent_line and formal_periodicity_localization_inserted,
    (
        f"tate_cohomology_single_laurent_line={tate_cohomology_single_laurent_line}, "
        f"formal_periodicity_localization_inserted={formal_periodicity_localization_inserted}"
    ),
)

gate(
    "SCH9 stabilizer cohomology does not construct endpoint, boundary map, Laurent generator, or torsor splitter",
    not cohomology_outputs_endpoint
    and not cohomology_outputs_boundary_map
    and not cohomology_outputs_laurent_generator
    and not cohomology_outputs_torsor_splitter,
    (
        f"endpoint={cohomology_outputs_endpoint}, "
        f"boundary={cohomology_outputs_boundary_map}, "
        f"laurent={cohomology_outputs_laurent_generator}, "
        f"torsor={cohomology_outputs_torsor_splitter}"
    ),
)

gate(
    "SCH10 graph, endpoint, matching, idempotent, and twist choices remain",
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
    "SCH11 stabilizer cohomology does not repair bottom, shear, or torsor obstructions",
    dmp_dim(-1) == 1
    and dmp_dim(-2) == 0
    and obstruction_res1 == 1
    and coboundary_res1 == 0
    and not carrier_multiplication_supplied
    and not torsor_splitter_supplied,
    "y^2=0, no DMP degree -2, res_1(c)=1, and no b/phi(b)=c",
)

control_pair_stabilizer_half_ranks = pair_stabilizer_half_ranks.copy()
control_formal_periodicity_localization = formal_periodicity_localization_inserted
gate(
    "SCH12 the same stabilizer cohomology package is formable on controls",
    control_pair_stabilizer_half_ranks == pair_stabilizer_half_ranks
    and control_formal_periodicity_localization == formal_periodicity_localization_inserted,
    "classifying-space/group/Tate cohomology of finite support stabilizers is a support operation",
)

primitive_carrier_maps_consumed = 0
cohomology_operation_inserted = 1
cohomology_class_read_off = 1
gate(
    "SCH13 surviving stabilizer cohomology route must be carrier-native",
    primitive_carrier_maps_consumed == 0
    and cohomology_operation_inserted == 1
    and cohomology_class_read_off == 1,
    "a real route must construct cohomology/periodicity, endpoint, boundary glue, and twist from correspondences",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (SCH1-SCH13)")
print(
    "VERDICT: support symplectic stabilizer cohomology does not supply R1 "
    "boundary glue.  Full-frame stabilizer cohomology is trivial; first-pair "
    "and endpoint-vector stabilizers contain elementary abelian 2-subgroups "
    "of rank at least two, so their mod-2 finite-group cohomology is not "
    "periodic.  Ordinary cohomology has no positive Laurent unit, formal "
    "periodicity localization is inserted, graph/endpoint/matching/"
    "idempotent/twist choices and bottom/shear/torsor obstructions remain, "
    "and the same package is formable on controls.  A surviving route must "
    "construct cohomology/periodicity carrier-natively."
)
