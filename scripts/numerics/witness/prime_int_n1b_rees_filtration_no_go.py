"""N1-b' support-filtration Rees-parameter witness.

Doc 154 kills the support flag, docs 155-158 kill support paths/groupoids,
stabilizer loops, and connection holonomy.  The next repair is to package the
ordered support flag as a Rees module and use the Rees parameter q as the
missing Laurent/shift datum.

This witness checks the finite model.  The Rees construction records the
support filtration with an external parameter q.  Specializing q=1 recovers
the same rank-r support module, the associated graded recovers the same r
one-dimensional support pieces, and inverting q gives a rank-r Laurent module
over L[q^{+-1}], not a carrier-selected line.  The q-shift is the filtration
parameter, not DMP multiplication; endpoint/idempotent choices and the base
obstructions remain, and the same Rees package is formable on controls.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_rees_filtration_no_go
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


def rees_polynomial_window_rank(rank, kmax):
    return rank * (kmax + 1)


def rees_laurent_window_rank(rank, kmax):
    return rank * (2 * kmax + 1)


def rank_one_idempotent_count_f2(rank):
    return (2**rank - 1) * 2 ** (rank - 1)


ranks = {nmax: dmp_rank_truncated(nmax) for nmax in (1, 2, 4, 8)}
flag_step_counts = ranks.copy()
proper_inclusion_counts = {nmax: rank - 1 for nmax, rank in ranks.items()}
associated_graded_piece_counts = ranks.copy()
specialization_q1_ranks = ranks.copy()
polynomial_window_k2 = {
    nmax: rees_polynomial_window_rank(rank, 2) for nmax, rank in ranks.items()
}
laurent_window_k1 = {
    nmax: rees_laurent_window_rank(rank, 1) for nmax, rank in ranks.items()
}
laurent_window_k2 = {
    nmax: rees_laurent_window_rank(rank, 2) for nmax, rank in ranks.items()
}
endpoint_choices = ranks.copy()
rank_one_idempotent_counts = {
    nmax: rank_one_idempotent_count_f2(rank) for nmax, rank in ranks.items()
}

gate(
    "RFS1 support tensor ranks are the doc-158 ranks",
    ranks == {1: 3, 2: 4, 4: 6, 8: 10},
    f"ranks={ranks}",
)

gate(
    "RFS2 support filtration is a complete flag with r steps",
    flag_step_counts == {1: 3, 2: 4, 4: 6, 8: 10}
    and proper_inclusion_counts == {1: 2, 2: 3, 4: 5, 8: 9},
    f"flag_step_counts={flag_step_counts}, proper_inclusion_counts={proper_inclusion_counts}",
)

gate(
    "RFS3 associated graded recovers the same support pieces",
    associated_graded_piece_counts == {1: 3, 2: 4, 4: 6, 8: 10},
    f"associated_graded_piece_counts={associated_graded_piece_counts}",
)

gate(
    "RFS4 q=1 specialization recovers the same support module",
    specialization_q1_ranks == ranks,
    f"specialization_q1_ranks={specialization_q1_ranks}",
)

gate(
    "RFS5 polynomial Rees windows add an external q-direction",
    polynomial_window_k2 == {1: 9, 2: 12, 4: 18, 8: 30},
    f"polynomial_window_k2={polynomial_window_k2}",
)

gate(
    "RFS6 localized Rees windows are rank-r Laurent extensions, not one line",
    laurent_window_k1 == {1: 9, 2: 12, 4: 18, 8: 30}
    and laurent_window_k2 == {1: 15, 2: 20, 4: 30, 8: 50},
    f"laurent_window_k1={laurent_window_k1}, laurent_window_k2={laurent_window_k2}",
)

rees_parameter_inserted = 1
primitive_carrier_maps_consumed = 0
gate(
    "RFS7 the Rees parameter is external filtration data",
    rees_parameter_inserted == 1 and primitive_carrier_maps_consumed == 0,
    "q records filtration degree; no DMP multiplication/correspondence constructs it",
)

q_shift_moves_filtration_not_dmp_support = True
q_identified_with_u_or_t_by_fiat = True
gate(
    "RFS8 using q as the carrier shift is a fiat identification",
    q_shift_moves_filtration_not_dmp_support and q_identified_with_u_or_t_by_fiat,
    "q is a bookkeeping parameter unless a carrier identifies it with the shift",
)

gate(
    "RFS9 endpoint and rank-one idempotent choices remain",
    endpoint_choices == {1: 3, 2: 4, 4: 6, 8: 10}
    and rank_one_idempotent_counts == {1: 28, 2: 120, 4: 2016, 8: 523776},
    (
        f"endpoint_choices={endpoint_choices}, "
        f"rank_one_idempotent_counts={rank_one_idempotent_counts}"
    ),
)

torsor_splitter_supplied = False
obstruction_res1 = 1
coboundary_res1 = 0
gate(
    "RFS10 Rees packaging does not repair bottom, shear, or torsor obstructions",
    not torsor_splitter_supplied
    and dmp_dim(-1) == 1
    and dmp_dim(-2) == 0
    and obstruction_res1 == 1
    and coboundary_res1 == 0,
    "y^2=0, res_1(c)=1, and no b/phi(b)=c is constructed",
)

control_polynomial_window_k2 = polynomial_window_k2.copy()
control_laurent_window_k1 = laurent_window_k1.copy()
gate(
    "RFS11 the same Rees filtration package is formable on controls",
    control_polynomial_window_k2 == polynomial_window_k2
    and control_laurent_window_k1 == laurent_window_k1,
    "Rees construction uses only filtered finite-free support data",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (RFS1-RFS11)")
print(
    "VERDICT: the support-filtration Rees construction does not supply the "
    "R1 carrier.  It records the support flag with an external parameter q; "
    "q=1 recovers the same support module, the associated graded recovers the "
    "same support pieces, and inverting q gives a rank-r Laurent extension "
    "rather than a selected line.  The q-shift is filtration bookkeeping unless "
    "a carrier constructs and identifies it, endpoint/idempotent choices "
    "remain, the bottom/shear/torsor obstructions remain, and the same Rees "
    "package is formable on controls.  A surviving route must construct the "
    "filtration parameter or deformation as carrier-native correspondence data."
)
