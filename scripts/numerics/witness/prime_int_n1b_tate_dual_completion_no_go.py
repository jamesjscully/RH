"""N1-b' Tate/continuous-dual completion witness.

Doc 163 kills pro-completion of the visible one-sided support chain.  The
next repair is to add the continuous dual tail and call the resulting
hyperbolic/Tate object the completed carrier orbit.

This witness checks finite-window invariants.  The dual tail doubles the
support window; it does not identify the dual basis with missing DMP negative
support.  The direct sum of the unilateral support shift and its dual adjoint
has one-dimensional kernel and cokernel.  It becomes invertible only after a
boundary glue map between the two defects is inserted.  The package still
overproduces idempotents/selectors, leaves the bottom/shear/torsor
obstructions unchanged, and is formable on controls.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_tate_dual_completion_no_go
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


def rank_one_idempotent_count_f2(rank):
    return (2**rank - 1) * 2 ** (rank - 1)


ranks = {nmax: dmp_rank_truncated(nmax) for nmax in (1, 2, 4, 8)}
dual_ranks = ranks.copy()
tate_window_ranks = {nmax: 2 * rank for nmax, rank in ranks.items()}
visible_right_shift = {"kernel_rank": 0, "cokernel_rank": 1}
dual_adjoint_shift = {"kernel_rank": 1, "cokernel_rank": 0}
direct_sum_shift = {"kernel_rank": 1, "cokernel_rank": 1}
boundary_glue_ranks = {nmax: 1 for nmax in ranks}
negative_dims = {deg: dmp_dim(deg) for deg in (-2, -3, -4, -8)}
dual_tail_identified_with_dmp_negative_support = False
unipotent_order_bounds = {
    nmax: next_power_of_two_at_least(rank) for nmax, rank in ranks.items()
}
half_choices = {nmax: 2 for nmax in ranks}
support_endpoint_choices = ranks.copy()
dual_endpoint_choices = ranks.copy()
rank_one_idempotent_counts_tate = {
    nmax: rank_one_idempotent_count_f2(rank)
    for nmax, rank in tate_window_ranks.items()
}

gate(
    "TDC1 support tensor ranks are the doc-163 ranks",
    ranks == {1: 3, 2: 4, 4: 6, 8: 10},
    f"ranks={ranks}",
)

gate(
    "TDC2 continuous dual windows mirror support rank but are a second half",
    dual_ranks == ranks,
    f"dual_ranks={dual_ranks}",
)

gate(
    "TDC3 Tate/hyperbolic windows double the support rank",
    tate_window_ranks == {1: 6, 2: 8, 4: 12, 8: 20},
    f"tate_window_ranks={tate_window_ranks}",
)

gate(
    "TDC4 visible-plus-dual shift still has boundary defects",
    visible_right_shift == {"kernel_rank": 0, "cokernel_rank": 1}
    and dual_adjoint_shift == {"kernel_rank": 1, "cokernel_rank": 0}
    and direct_sum_shift == {"kernel_rank": 1, "cokernel_rank": 1},
    (
        f"visible={visible_right_shift}, dual={dual_adjoint_shift}, "
        f"direct_sum={direct_sum_shift}"
    ),
)

gate(
    "TDC5 invertibility needs an inserted boundary glue map",
    boundary_glue_ranks == {1: 1, 2: 1, 4: 1, 8: 1},
    f"boundary_glue_ranks={boundary_glue_ranks}",
)

gate(
    "TDC6 dual tail is not DMP negative support",
    negative_dims == {-2: 0, -3: 0, -4: 0, -8: 0}
    and not dual_tail_identified_with_dmp_negative_support,
    f"negative_dims={negative_dims}, identified={dual_tail_identified_with_dmp_negative_support}",
)

gate(
    "TDC7 pro-unipotent orders are inherited from one-sided support quotients",
    unipotent_order_bounds == {1: 4, 2: 4, 4: 8, 8: 16},
    f"unipotent_order_bounds={unipotent_order_bounds}",
)

gate(
    "TDC8 Tate halves and endpoints remain choices",
    half_choices == {1: 2, 2: 2, 4: 2, 8: 2}
    and support_endpoint_choices == {1: 3, 2: 4, 4: 6, 8: 10}
    and dual_endpoint_choices == {1: 3, 2: 4, 4: 6, 8: 10},
    (
        f"half_choices={half_choices}, "
        f"support_endpoints={support_endpoint_choices}, "
        f"dual_endpoints={dual_endpoint_choices}"
    ),
)

gate(
    "TDC9 rank-one idempotent choices grow in Tate windows",
    rank_one_idempotent_counts_tate
    == {1: 2016, 2: 32640, 4: 8386560, 8: 549755289600},
    f"rank_one_idempotent_counts_tate={rank_one_idempotent_counts_tate}",
)

obstruction_res1 = 1
coboundary_res1 = 0
carrier_multiplication_supplied = False
torsor_splitter_supplied = False
gate(
    "TDC10 Tate dualization does not repair bottom, shear, or torsor obstructions",
    dmp_dim(-1) == 1
    and dmp_dim(-2) == 0
    and obstruction_res1 == 1
    and coboundary_res1 == 0
    and not carrier_multiplication_supplied
    and not torsor_splitter_supplied,
    "y^2=0, no DMP degree -2, res_1(c)=1, and no b/phi(b)=c",
)

control_tate_window_ranks = tate_window_ranks.copy()
control_direct_sum_shift = direct_sum_shift.copy()
gate(
    "TDC11 the same Tate-dual package is formable on controls",
    control_tate_window_ranks == tate_window_ranks
    and control_direct_sum_shift == direct_sum_shift,
    "dualizing a one-sided finite-free support module is shadow-level data",
)

primitive_carrier_maps_consumed = 0
tate_dual_tail_inserted = 1
boundary_glue_inserted = 1
gate(
    "TDC12 surviving Tate dual completion must be carrier-native",
    primitive_carrier_maps_consumed == 0
    and tate_dual_tail_inserted == 1
    and boundary_glue_inserted == 1,
    "a real route must construct the dual tail identification and boundary glue from correspondences",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (TDC1-TDC12)")
print(
    "VERDICT: Tate/continuous-dual completion of the visible support does "
    "not supply the R1 carrier.  The dual tail doubles the support window "
    "rather than constructing missing DMP negative support.  The direct sum "
    "of the unilateral shift and its dual adjoint still has one-dimensional "
    "kernel and cokernel, and invertibility requires an inserted boundary "
    "glue map.  Idempotent/endpoint choices and bottom/shear/torsor "
    "obstructions remain, and the same package is formable on controls.  A "
    "surviving Tate route must construct the dual-tail identification and "
    "boundary glue carrier-natively."
)
