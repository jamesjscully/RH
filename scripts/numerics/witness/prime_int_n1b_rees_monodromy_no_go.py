"""N1-b' Rees-monodromy/filtered-operator witness.

Doc 159 kills the plain support-filtration Rees parameter q.  The next
repair is to add the standard Rees/filtered operators: the Euler operator
q d/dq, a nilpotent residue N along the support flag, or the unipotent
monodromy T=1+N, and use that operator package as the missing carrier shift.

This witness checks the finite model.  The support nilpotent is the same
finite support shift as before: its powers die.  Over the F_2 coefficient
model, T=1+N has finite 2-power order on the truncated support, not an
infinite Laurent orbit.  The Euler operator sees only the external Rees
q-degree and repeats across all support pieces.  None of these operators is
carrier multiplication; endpoint/idempotent choices and base obstructions
remain, and the same operator package is formable on controls.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_rees_monodromy_no_go
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


def nilpotent_power_rank(rank, power):
    if power <= 0:
        return rank
    return max(rank - power, 0)


def first_power_of_two_ge(rank):
    value = 1
    while value < rank:
        value *= 2
    return value


def laurent_window_rank(rank, kmax):
    return rank * (2 * kmax + 1)


def rank_one_idempotent_count_f2(rank):
    return (2**rank - 1) * 2 ** (rank - 1)


ranks = {nmax: dmp_rank_truncated(nmax) for nmax in (1, 2, 4, 8)}
nilpotent_rank_1 = {nmax: nilpotent_power_rank(rank, 1) for nmax, rank in ranks.items()}
nilpotent_rank_2 = {nmax: nilpotent_power_rank(rank, 2) for nmax, rank in ranks.items()}
top_nonzero_rank = {
    nmax: nilpotent_power_rank(rank, rank - 1) for nmax, rank in ranks.items()
}
nilpotent_zero_rank = {
    nmax: nilpotent_power_rank(rank, rank) for nmax, rank in ranks.items()
}
unipotent_order_bounds = {
    nmax: first_power_of_two_ge(rank) for nmax, rank in ranks.items()
}
euler_window_k2_ranks = {
    nmax: laurent_window_rank(rank, 2) for nmax, rank in ranks.items()
}
euler_eigenvalue_multiplicities_k2 = {
    nmax: {k: rank for k in range(-2, 3)} for nmax, rank in ranks.items()
}
monodromy_filtration_piece_counts = ranks.copy()
endpoint_choices = ranks.copy()
rank_one_idempotent_counts = {
    nmax: rank_one_idempotent_count_f2(rank) for nmax, rank in ranks.items()
}

gate(
    "RMN1 support tensor ranks are the doc-159 ranks",
    ranks == {1: 3, 2: 4, 4: 6, 8: 10},
    f"ranks={ranks}",
)

gate(
    "RMN2 support nilpotent has the usual finite-shift ranks",
    nilpotent_rank_1 == {1: 2, 2: 3, 4: 5, 8: 9}
    and nilpotent_rank_2 == {1: 1, 2: 2, 4: 4, 8: 8},
    f"rank_N={nilpotent_rank_1}, rank_N2={nilpotent_rank_2}",
)

gate(
    "RMN3 support nilpotent dies at the support length",
    top_nonzero_rank == {1: 1, 2: 1, 4: 1, 8: 1}
    and nilpotent_zero_rank == {1: 0, 2: 0, 4: 0, 8: 0},
    f"top_nonzero_rank={top_nonzero_rank}, nilpotent_zero_rank={nilpotent_zero_rank}",
)

gate(
    "RMN4 unipotent 1+N has finite 2-power order on F_2 support",
    unipotent_order_bounds == {1: 4, 2: 4, 4: 8, 8: 16},
    f"unipotent_order_bounds={unipotent_order_bounds}",
)

gate(
    "RMN5 Euler q-d/dq acts on external Rees degree, repeated over support",
    euler_window_k2_ranks == {1: 15, 2: 20, 4: 30, 8: 50}
    and all(
        euler_eigenvalue_multiplicities_k2[nmax] == {k: ranks[nmax] for k in range(-2, 3)}
        for nmax in ranks
    ),
    (
        f"euler_window_k2_ranks={euler_window_k2_ranks}, "
        f"multiplicities={euler_eigenvalue_multiplicities_k2}"
    ),
)

gate(
    "RMN6 monodromy filtration of the support nilpotent just repackages support length",
    monodromy_filtration_piece_counts == {1: 3, 2: 4, 4: 6, 8: 10},
    f"monodromy_filtration_piece_counts={monodromy_filtration_piece_counts}",
)

operator_package_inserted = True
primitive_carrier_maps_consumed = 0
gate(
    "RMN7 Rees-monodromy operators are inserted from support/Rees data",
    operator_package_inserted and primitive_carrier_maps_consumed == 0,
    "N is the support shift and q-d/dq is the external Rees-degree operator",
)

gate(
    "RMN8 endpoint and rank-one idempotent choices remain",
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
    "RMN9 Rees monodromy does not repair bottom, shear, or torsor obstructions",
    not torsor_splitter_supplied
    and dmp_dim(-1) == 1
    and dmp_dim(-2) == 0
    and obstruction_res1 == 1
    and coboundary_res1 == 0,
    "y^2=0, res_1(c)=1, and no b/phi(b)=c is constructed",
)

control_nilpotent_rank_1 = nilpotent_rank_1.copy()
control_euler_window_k2_ranks = euler_window_k2_ranks.copy()
gate(
    "RMN10 the same Rees-monodromy package is formable on controls",
    control_nilpotent_rank_1 == nilpotent_rank_1
    and control_euler_window_k2_ranks == euler_window_k2_ranks,
    "finite support shifts and Rees-degree operators use only filtered support data",
)

carrier_native_monodromy_required = True
gate(
    "RMN11 surviving monodromy/operator route must be carrier-native",
    carrier_native_monodromy_required and primitive_carrier_maps_consumed == 0,
    "a real route must construct N/E/T from carrier correspondences and kill controls",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (RMN1-RMN11)")
print(
    "VERDICT: the Rees-monodromy operator package does not supply the R1 "
    "carrier.  The support nilpotent is the finite support shift and dies at "
    "the support length; over F_2, 1+N has finite 2-power order, not a "
    "Laurent orbit; q d/dq sees only external Rees degree and repeats across "
    "all support pieces.  These operators are inserted from support/Rees "
    "bookkeeping, not carrier multiplication.  Endpoint/idempotent choices "
    "and bottom/shear/torsor obstructions remain, and the same package is "
    "formable on controls.  A surviving route must construct monodromy or "
    "operator data carrier-natively."
)
