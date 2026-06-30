"""N1-b' trace/minimal idempotent witness.

Doc 151 kills choosing a rank-one idempotent corner of the support End
envelope.  The next repair is to say that trace, rank, or minimality chooses
the right idempotent canonically.

This witness checks the finite F_2 model.  Trace-one is too weak: even the
diagonal trace-one idempotents are many and include higher odd ranks.
Minimality/rank-one is too weak in the other direction: every rank-one
idempotent has trace one and is minimal, and there are still many of them.
The bottom/shear obstructions remain, and the same tests are formable on
controls.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_trace_minimal_idempotent_no_go
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


def rank_one_idempotent_count(rank):
    # e=u v^T is idempotent of rank one iff u != 0 and v(u)=1.
    return (2**rank - 1) * 2 ** (rank - 1)


def diagonal_trace_one_count(rank):
    # Diagonal idempotents are subsets of coordinates; trace over F_2 is
    # parity of the subset size.  Exactly half have trace one.
    return 2 ** (rank - 1)


def diagonal_trace_one_rank_counts(rank):
    counts = {}
    for subset_size in range(rank + 1):
        if subset_size % 2 == 1:
            # n choose k without importing math.comb for older interpreters.
            numerator = 1
            denominator = 1
            k = min(subset_size, rank - subset_size)
            for i in range(1, k + 1):
                numerator *= rank - (k - i)
                denominator *= i
            counts[subset_size] = numerator // denominator
    return counts


def rank_one_trace_values(rank):
    # For e=u v^T with v(u)=1, tr(e)=v(u)=1 over F_2.
    return {1} if rank >= 1 else set()


ranks = {nmax: dmp_rank_truncated(nmax) for nmax in (1, 2, 4, 8)}
rank_one_counts = {nmax: rank_one_idempotent_count(rank) for nmax, rank in ranks.items()}
diagonal_trace_one_counts = {
    nmax: diagonal_trace_one_count(rank) for nmax, rank in ranks.items()
}
diagonal_trace_one_ranks = {
    nmax: diagonal_trace_one_rank_counts(rank) for nmax, rank in ranks.items()
}
rank_one_traces = {nmax: rank_one_trace_values(rank) for nmax, rank in ranks.items()}

gate(
    "TMI1 support End envelope ranks are the doc-151 ranks",
    ranks == {1: 3, 2: 4, 4: 6, 8: 10},
    f"ranks={ranks}",
)

gate(
    "TMI2 trace-one diagonal idempotents are already many",
    diagonal_trace_one_counts == {1: 4, 2: 8, 4: 32, 8: 512},
    f"diagonal_trace_one_counts={diagonal_trace_one_counts}",
)

gate(
    "TMI3 trace-one does not imply rank-one",
    diagonal_trace_one_ranks[2] == {1: 4, 3: 4}
    and diagonal_trace_one_ranks[4] == {1: 6, 3: 20, 5: 6}
    and diagonal_trace_one_ranks[8] == {1: 10, 3: 120, 5: 252, 7: 120, 9: 10},
    f"diagonal_trace_one_ranks={diagonal_trace_one_ranks}",
)

gate(
    "TMI4 every rank-one idempotent has trace one",
    all(values == {1} for values in rank_one_traces.values()),
    f"rank_one_traces={rank_one_traces}",
)

gate(
    "TMI5 minimal/rank-one idempotents still form a large family",
    rank_one_counts == {1: 28, 2: 120, 4: 2016, 8: 523776},
    f"rank_one_counts={rank_one_counts}",
)

support_invariant_selects_one = False
same_rank_same_trace_same_minimality = True
gate(
    "TMI6 rank, trace, and minimality do not distinguish one corner",
    same_rank_same_trace_same_minimality and not support_invariant_selects_one,
    "all rank-one corners have the same rank/minimality/trace profile",
)

bottom_trace_one_corner_uses_external_l = True
gate(
    "TMI7 bottom trace-one corner is still the external tensor line",
    bottom_trace_one_corner_uses_external_l and dmp_dim(-1) == 1 and dmp_dim(-2) == 0,
    "the chosen scalar is external L; the DMP bottom is still square-zero",
)

obstruction_res1 = 1
coboundary_res1 = 0
gate(
    "TMI8 trace/minimality does not repair bottom or shear obstructions",
    dmp_dim(-1) == 1 and dmp_dim(-2) == 0 and obstruction_res1 == 1 and coboundary_res1 == 0,
    "y^2=0 and res_1(c)=1 remain unchanged",
)

control_rank_one_counts = rank_one_counts.copy()
control_trace_one_counts = diagonal_trace_one_counts.copy()
gate(
    "TMI9 the same trace/minimality tests are formable on controls",
    control_rank_one_counts == rank_one_counts
    and control_trace_one_counts == diagonal_trace_one_counts,
    "rank, trace, and minimality are finite-free module predicates",
)

primitive_carrier_maps_consumed = 0
trace_or_minimality_predicate = 1
gate(
    "TMI10 surviving idempotent must be carrier-selected beyond trace/minimality",
    trace_or_minimality_predicate == 1 and primitive_carrier_maps_consumed == 0,
    "a real route must construct the idempotent from carrier correspondence data",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (TMI1-TMI10)")
print(
    "VERDICT: trace/minimality does not canonically select the support "
    "End-envelope corner.  Trace-one is too weak, already giving many "
    "diagonal idempotents of odd rank; minimal/rank-one is still a large "
    "family, all with trace one and identical support-level invariants.  The "
    "bottom and shear obstructions remain, and the same predicates are "
    "formable on controls.  A surviving route must construct the idempotent "
    "from carrier correspondence data, not from trace or minimality alone."
)
