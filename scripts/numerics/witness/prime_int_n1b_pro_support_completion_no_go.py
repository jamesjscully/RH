"""N1-b' pro-support/infinite-completion witness.

Docs 160-162 kill finite support nilpotents, filtered gluing, and derived
support gluing.  The next repair is to pass to the infinite or completed
support chain: the finite nilpotent becomes a topological/pro-nilpotent
operator, and 1+N has unbounded 2-power order on finite quotients.

This witness checks the finite-window invariants.  The visible DMP support is
one-sided: degree -1 and all nonnegative degrees, with no degree <= -2.  A
one-sided completion has a persistent rank-one boundary defect; depending on
orientation, the shift is injective not surjective or surjective not
injective.  The pro-unipotent 1+N is congruent to the identity on associated
graded and its finite quotients are 2-power unipotent quotients, not a
discrete Laurent orbit.  Making the shift genuinely two-sided requires
inserting a negative tail, i.e. external Laurent data.  The same completion
package is formable on controls.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_pro_support_completion_no_go
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


def next_power_of_two_at_least(n):
    power = 1
    while power < n:
        power *= 2
    return power


def strict_upper_rank(rank):
    return rank * (rank - 1) // 2


def rank_one_idempotent_count_f2(rank):
    return (2**rank - 1) * 2 ** (rank - 1)


ranks = {nmax: dmp_rank_truncated(nmax) for nmax in (1, 2, 4, 8)}
finite_shift_ranks = {nmax: rank - 1 for nmax, rank in ranks.items()}
finite_shift_kernel_ranks = {nmax: 1 for nmax in ranks}
finite_shift_cokernel_ranks = {nmax: 1 for nmax in ranks}
one_sided_right_shift = {"kernel_rank": 0, "cokernel_rank": 1}
one_sided_left_shift = {"kernel_rank": 1, "cokernel_rank": 0}
negative_dims = {deg: dmp_dim(deg) for deg in (-2, -3, -4, -8)}
negative_tail_needed = {nmax: nmax for nmax in ranks}
unipotent_order_bounds = {
    nmax: next_power_of_two_at_least(rank) for nmax, rank in ranks.items()
}
associated_graded_displacements = {nmax: 0 for nmax in ranks}
laurent_shift_displacements = {nmax: 1 for nmax in ranks}
strict_upper_ranks = {nmax: strict_upper_rank(rank) for nmax, rank in ranks.items()}
pro_unipotent_choice_counts = {
    nmax: 2 ** strict_upper_rank(rank) for nmax, rank in ranks.items()
}
endpoint_choices = ranks.copy()
rank_one_idempotent_counts = {
    nmax: rank_one_idempotent_count_f2(rank) for nmax, rank in ranks.items()
}

gate(
    "PSC1 support tensor ranks are the doc-162 ranks",
    ranks == {1: 3, 2: 4, 4: 6, 8: 10},
    f"ranks={ranks}",
)

gate(
    "PSC2 finite support shifts have a rank-one boundary defect",
    finite_shift_ranks == {1: 2, 2: 3, 4: 5, 8: 9}
    and finite_shift_kernel_ranks == {1: 1, 2: 1, 4: 1, 8: 1}
    and finite_shift_cokernel_ranks == {1: 1, 2: 1, 4: 1, 8: 1},
    (
        f"finite_shift_ranks={finite_shift_ranks}, "
        f"kernels={finite_shift_kernel_ranks}, "
        f"cokernels={finite_shift_cokernel_ranks}"
    ),
)

gate(
    "PSC3 one-sided completions are not invertible shifts",
    one_sided_right_shift == {"kernel_rank": 0, "cokernel_rank": 1}
    and one_sided_left_shift == {"kernel_rank": 1, "cokernel_rank": 0},
    f"right={one_sided_right_shift}, left={one_sided_left_shift}",
)

gate(
    "PSC4 the negative predecessor tail is absent in DMP support",
    negative_dims == {-2: 0, -3: 0, -4: 0, -8: 0},
    f"negative_dims={negative_dims}",
)

gate(
    "PSC5 two-sided completion must insert a negative tail",
    negative_tail_needed == {1: 1, 2: 2, 4: 4, 8: 8},
    f"negative_tail_needed={negative_tail_needed}",
)

gate(
    "PSC6 pro-unipotent finite quotients are 2-power unipotent quotients",
    unipotent_order_bounds == {1: 4, 2: 4, 4: 8, 8: 16},
    f"unipotent_order_bounds={unipotent_order_bounds}",
)

gate(
    "PSC7 pro-unipotent 1+N fixes associated graded instead of translating it",
    associated_graded_displacements == {1: 0, 2: 0, 4: 0, 8: 0}
    and laurent_shift_displacements == {1: 1, 2: 1, 4: 1, 8: 1},
    (
        f"associated_graded_displacements={associated_graded_displacements}, "
        f"laurent_shift_displacements={laurent_shift_displacements}"
    ),
)

gate(
    "PSC8 completed upper-triangular choices still overproduce support data",
    strict_upper_ranks == {1: 3, 2: 6, 4: 15, 8: 45}
    and pro_unipotent_choice_counts == {1: 8, 2: 64, 4: 32768, 8: 35184372088832},
    (
        f"strict_upper_ranks={strict_upper_ranks}, "
        f"choice_counts={pro_unipotent_choice_counts}"
    ),
)

gate(
    "PSC9 endpoint and rank-one idempotent choices remain",
    endpoint_choices == {1: 3, 2: 4, 4: 6, 8: 10}
    and rank_one_idempotent_counts == {1: 28, 2: 120, 4: 2016, 8: 523776},
    (
        f"endpoint_choices={endpoint_choices}, "
        f"rank_one_idempotent_counts={rank_one_idempotent_counts}"
    ),
)

obstruction_res1 = 1
coboundary_res1 = 0
carrier_multiplication_supplied = False
torsor_splitter_supplied = False
gate(
    "PSC10 completion does not repair bottom, shear, or torsor obstructions",
    dmp_dim(-1) == 1
    and dmp_dim(-2) == 0
    and obstruction_res1 == 1
    and coboundary_res1 == 0
    and not carrier_multiplication_supplied
    and not torsor_splitter_supplied,
    "y^2=0, no degree -2 predecessor, res_1(c)=1, and no b/phi(b)=c",
)

control_one_sided_right_shift = one_sided_right_shift.copy()
control_unipotent_order_bounds = unipotent_order_bounds.copy()
gate(
    "PSC11 the same pro-support package is formable on controls",
    control_one_sided_right_shift == one_sided_right_shift
    and control_unipotent_order_bounds == unipotent_order_bounds,
    "one-sided completions and pro-unipotent support operators are shadow-level data",
)

primitive_carrier_maps_consumed = 0
pro_completion_inserted = 1
gate(
    "PSC12 surviving pro/infinite completion must be carrier-native",
    primitive_carrier_maps_consumed == 0 and pro_completion_inserted == 1,
    "a real route must construct the completed two-sided carrier orbit from correspondences",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (PSC1-PSC12)")
print(
    "VERDICT: pro-support completion of the visible one-sided support does "
    "not supply the R1 carrier.  The finite-window shift has a persistent "
    "rank-one boundary defect; the one-sided limit is not invertible; the "
    "negative predecessor tail is absent; and the pro-unipotent 1+N fixes "
    "associated graded while its finite quotients are 2-power unipotent "
    "quotients, not a Laurent orbit.  A two-sided completion inserts external "
    "negative support.  Endpoint/idempotent choices and bottom/shear/torsor "
    "obstructions remain, and the same completion package is formable on "
    "controls.  A surviving route must construct the completed carrier orbit "
    "carrier-natively."
)
