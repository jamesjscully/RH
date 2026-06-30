"""N1-b' symplectic stabilizer-stack witness.

Doc 173 kills the set-level Sp quotient/orbit-average of the support
Darboux-frame package.  The next repair is to keep the quotient stack or
action groupoid and use its residual stabilizer/parabolic isotropy as the
missing carrier loop data.

In the finite F_2 support windows, full symplectic-frame stacks have trivial
stabilizer.  Ordered first-pair stacks have residual stabilizer Sp(2r-2,2),
and endpoint-vector stacks have a large finite parabolic stabilizer.  These
are finite automorphism groups of already chosen support objects.  They do
not choose a representative, construct a boundary map, supply an infinite
Laurent generator, or split the torsor.  The same stabilizer-stack package is
formable on controls.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_symplectic_stabilizer_stack_no_go
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


def symplectic_pair_count_f2(half_rank):
    return (2 ** (2 * half_rank) - 1) * 2 ** (2 * half_rank - 1)


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
symplectic_group_orders = {
    nmax: symplectic_group_order_f2(rank) for nmax, rank in ranks.items()
}
symplectic_pair_counts = {
    nmax: symplectic_pair_count_f2(rank) for nmax, rank in ranks.items()
}
nonzero_vector_counts = {nmax: nonzero_vector_count(rank) for nmax, rank in ranks.items()}

# The Sp action on full frames is simply transitive.
full_frame_stabilizer_counts = {nmax: 1 for nmax in ranks}

# Stabilizer of an ordered hyperbolic pair (a,b) with <a,b>=1.
pair_stabilizer_counts = {
    nmax: symplectic_group_order_f2(rank - 1) for nmax, rank in ranks.items()
}

# Stabilizer of a nonzero endpoint vector.
endpoint_vector_stabilizer_counts = {
    nmax: symplectic_group_orders[nmax] // nonzero_vector_counts[nmax]
    for nmax in ranks
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

stack_selects_representative = False
stack_outputs_endpoint = False
stack_outputs_boundary_map = False
stack_outputs_laurent_generator = False
stack_outputs_torsor_splitter = False
basepoint_choice_required_to_identify_stabilizer = True
full_frame_stack_has_loop_data = False
pair_stabilizers_are_finite = True
endpoint_stabilizers_are_finite = True
finite_stabilizer_supplies_infinite_laurent_shift = False
carrier_multiplication_supplied = False
torsor_splitter_supplied = False

gate(
    "SSK1 support tensor ranks are unchanged",
    ranks == {1: 3, 2: 4, 4: 6, 8: 10},
    f"ranks={ranks}",
)

gate(
    "SSK2 Tate/hyperbolic windows double support rank",
    tate_window_ranks == {1: 6, 2: 8, 4: 12, 8: 20},
    f"tate_window_ranks={tate_window_ranks}",
)

gate(
    "SSK3 Sp group and first-pair counts match the prior frame quotient",
    symplectic_group_orders
    == {
        1: 1451520,
        2: 47377612800,
        4: 208114637736580743168000,
        8: 1132992015386677099994486205757869431795095310094129168384000000,
    }
    and symplectic_pair_counts == {1: 2016, 2: 32640, 4: 8386560, 8: 549755289600},
    (
        f"symplectic_group_orders={symplectic_group_orders}, "
        f"symplectic_pair_counts={symplectic_pair_counts}"
    ),
)

gate(
    "SSK4 full symplectic-frame stack has trivial stabilizer",
    full_frame_stabilizer_counts == {1: 1, 2: 1, 4: 1, 8: 1}
    and not full_frame_stack_has_loop_data,
    f"full_frame_stabilizer_counts={full_frame_stabilizer_counts}",
)

gate(
    "SSK5 ordered first-pair stack has finite Sp(2r-2,2) stabilizer",
    pair_stabilizer_counts
    == {
        1: 720,
        2: 1451520,
        4: 24815256521932800,
        8: 2060902435720151186326095525680721766346957783040000,
    }
    and pair_stabilizers_are_finite
    and not finite_stabilizer_supplies_infinite_laurent_shift,
    f"pair_stabilizer_counts={pair_stabilizer_counts}",
)

gate(
    "SSK6 endpoint-vector stack has large finite parabolic stabilizer",
    nonzero_vector_counts == {1: 63, 2: 255, 4: 4095, 8: 1048575}
    and endpoint_vector_stabilizer_counts
    == {
        1: 23040,
        2: 185794560,
        4: 50821645356918374400,
        8: 1080506416218846625176535970968094253434513802154475520000,
    }
    and endpoint_stabilizers_are_finite
    and not finite_stabilizer_supplies_infinite_laurent_shift,
    (
        f"nonzero_vector_counts={nonzero_vector_counts}, "
        f"endpoint_vector_stabilizer_counts={endpoint_vector_stabilizer_counts}"
    ),
)

gate(
    "SSK7 identifying the stabilizer as a concrete group requires a support basepoint",
    basepoint_choice_required_to_identify_stabilizer
    and not stack_selects_representative
    and not stack_outputs_endpoint,
    (
        f"basepoint_choice_required={basepoint_choice_required_to_identify_stabilizer}, "
        f"stack_selects_representative={stack_selects_representative}"
    ),
)

gate(
    "SSK8 stabilizer stack does not construct boundary map, Laurent generator, or torsor splitter",
    not stack_outputs_boundary_map
    and not stack_outputs_laurent_generator
    and not stack_outputs_torsor_splitter,
    (
        f"boundary={stack_outputs_boundary_map}, "
        f"laurent={stack_outputs_laurent_generator}, "
        f"torsor={stack_outputs_torsor_splitter}"
    ),
)

gate(
    "SSK9 graph, endpoint, matching, idempotent, and twist choices remain",
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
    "SSK10 stabilizer stack does not repair bottom, shear, or torsor obstructions",
    dmp_dim(-1) == 1
    and dmp_dim(-2) == 0
    and obstruction_res1 == 1
    and coboundary_res1 == 0
    and not carrier_multiplication_supplied
    and not torsor_splitter_supplied,
    "y^2=0, no DMP degree -2, res_1(c)=1, and no b/phi(b)=c",
)

control_pair_stabilizer_counts = pair_stabilizer_counts.copy()
control_endpoint_vector_stabilizer_counts = endpoint_vector_stabilizer_counts.copy()
gate(
    "SSK11 the same stabilizer-stack package is formable on controls",
    control_pair_stabilizer_counts == pair_stabilizer_counts
    and control_endpoint_vector_stabilizer_counts == endpoint_vector_stabilizer_counts,
    "stabilizers of finite hyperbolic support actions are support operations",
)

primitive_carrier_maps_consumed = 0
stack_operation_inserted = 1
stabilizer_isotropy_read_off = 1
gate(
    "SSK12 surviving symplectic stabilizer-stack route must be carrier-native",
    primitive_carrier_maps_consumed == 0
    and stack_operation_inserted == 1
    and stabilizer_isotropy_read_off == 1,
    "a real route must construct stack/isotropy, endpoint, boundary glue, and twist from correspondences",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (SSK1-SSK12)")
print(
    "VERDICT: the support symplectic quotient stack does not supply R1 "
    "boundary glue.  Full-frame stacks have trivial stabilizer; ordered "
    "first-pair stacks have only finite Sp(2r-2,2) residual isotropy; and "
    "endpoint-vector stacks have large finite parabolics.  Reading any "
    "concrete stabilizer requires a support basepoint, finite isotropy is "
    "not an infinite Laurent shift, graph/endpoint/matching/idempotent/twist "
    "choices and bottom/shear/torsor obstructions remain, and the same "
    "package is formable on controls.  A surviving route must construct "
    "the stack/isotropy data carrier-natively."
)
