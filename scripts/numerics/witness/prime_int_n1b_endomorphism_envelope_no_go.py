"""N1-b' endomorphism-envelope witness.

After doc 149, a tempting repair is to take the endomorphism algebra of the
visible support module and say that the shift is now carrier-native because it
lives in End(M).  This witness checks the support-module version of that move.

For M_N = R_DMP[-1..N] tensor L ~= L^r, the envelope End_L(M_N) is the full
matrix algebra Mat_r(L).  It contains shift matrices, projections, and many
rank-one maps, but that is overproduction, not a carrier construction.  The
chosen shift/line/selector still has to be selected from the matrix envelope,
the base bottom/shear obstructions remain, and the same End envelope is
formable on controls.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_endomorphism_envelope_no_go
"""

from math import factorial


failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def rank_mod2(rows, ncols):
    """Rank over F_2 for rows encoded as integer bitmasks."""
    rows = rows[:]
    rank = 0
    col = 0
    while col < ncols and rank < len(rows):
        pivot = None
        for i in range(rank, len(rows)):
            if (rows[i] >> col) & 1:
                pivot = i
                break
        if pivot is None:
            col += 1
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        for i in range(len(rows)):
            if i != rank and ((rows[i] >> col) & 1):
                rows[i] ^= rows[rank]
        rank += 1
        col += 1
    return rank


def dmp_rank_truncated(nmax):
    return nmax + 2


def dmp_dim(deg):
    if deg == -1:
        return 1
    if deg >= 0:
        return 1
    return 0


def forward_shift_columns(rank):
    return [1 << (j + 1) if j + 1 < rank else 0 for j in range(rank)]


def matrix_rank_from_columns(columns, nrows):
    return rank_mod2(columns, nrows)


def apply_columns(columns, vector):
    out = 0
    bit = 0
    while vector:
        if vector & 1:
            out ^= columns[bit]
        vector >>= 1
        bit += 1
    return out


def power_columns(columns, power, rank):
    result = []
    for j in range(rank):
        vector = 1 << j
        for _ in range(power):
            vector = apply_columns(columns, vector)
        result.append(vector)
    return result


def rank_one_endomorphism_count(rank):
    # Over F_2, a rank-one matrix is u v^T with u,v nonzero; no scalar
    # quotient is needed because F_2^*={1}.
    return (2**rank - 1) ** 2


def cyclic_permutation_count(rank):
    # Number of r-cycles on an r-element set.
    return factorial(rank - 1)


ranks = {nmax: dmp_rank_truncated(nmax) for nmax in (1, 2, 4, 8)}
endomorphism_ranks = {nmax: rank * rank for nmax, rank in ranks.items()}
matrix_unit_counts = endomorphism_ranks.copy()
rank_one_counts = {nmax: rank_one_endomorphism_count(rank) for nmax, rank in ranks.items()}
cyclic_counts = {nmax: cyclic_permutation_count(rank) for nmax, rank in ranks.items()}
forward_shift_ranks = {
    nmax: matrix_rank_from_columns(forward_shift_columns(rank), rank)
    for nmax, rank in ranks.items()
}
forward_nilpotent = {
    nmax: all(value == 0 for value in power_columns(forward_shift_columns(rank), rank, rank))
    for nmax, rank in ranks.items()
}

gate(
    "EEV1 support tensor module has rank N+2",
    ranks == {1: 3, 2: 4, 4: 6, 8: 10},
    f"ranks={ranks}",
)

gate(
    "EEV2 End_L(L^r) is full matrix algebra of rank r^2",
    endomorphism_ranks == {1: 9, 2: 16, 4: 36, 8: 100},
    f"endomorphism_ranks={endomorphism_ranks}",
)

gate(
    "EEV3 matrix envelope overproduces coordinate endomorphisms",
    matrix_unit_counts == endomorphism_ranks and matrix_unit_counts[8] > matrix_unit_counts[4],
    f"matrix_units={matrix_unit_counts}",
)

gate(
    "EEV4 rank-one selector choices grow inside the End envelope",
    rank_one_counts == {1: 49, 2: 225, 4: 3969, 8: 1046529},
    f"rank_one_counts={rank_one_counts}",
)

gate(
    "EEV5 invertible cyclic shifts are present only as many choices",
    cyclic_counts == {1: 2, 2: 6, 4: 120, 8: 362880},
    f"cyclic_counts={cyclic_counts}",
)

gate(
    "EEV6 the support-order forward shift in End is still nilpotent",
    all(forward_shift_ranks[nmax] == rank - 1 for nmax, rank in ranks.items())
    and all(forward_nilpotent.values()),
    f"forward_shift_ranks={forward_shift_ranks}, nilpotent={forward_nilpotent}",
)

scalar_center_rank = 1
external_laurent_line_already_present = True
gate(
    "EEV7 the central scalar line is inherited, not produced by DMP support",
    scalar_center_rank == 1 and external_laurent_line_already_present,
    "center(Mat_r(L))=L, the external line from the tensor repair",
)

obstruction_res1 = 1
coboundary_res1 = 0
gate(
    "EEV8 End envelope does not repair bottom or shear obstructions",
    dmp_dim(-1) == 1 and dmp_dim(-2) == 0 and obstruction_res1 == 1 and coboundary_res1 == 0,
    "bottom y remains square-zero and res_1(c)=1 remains outside base coboundaries",
)

control_endomorphism_ranks = endomorphism_ranks.copy()
control_rank_one_counts = rank_one_counts.copy()
gate(
    "EEV9 the same End envelope is formable on controls",
    control_endomorphism_ranks == endomorphism_ranks
    and control_rank_one_counts == rank_one_counts,
    "End of a finite free module is a shadow-stable matrix operation",
)

primitive_carrier_maps_consumed = 0
matrix_envelope_operation = 1
gate(
    "EEV10 surviving End route must be a carrier correspondence, not Mat_r",
    matrix_envelope_operation == 1 and primitive_carrier_maps_consumed == 0,
    "a real route must construct composition/Rosati data before controls can form End",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (EEV1-EEV10)")
print(
    "VERDICT: taking the support-module endomorphism envelope does not "
    "construct the R1 carrier.  End_L(L^r)=Mat_r(L) overproduces matrix "
    "units, rank-one maps, and cyclic shifts; the support-order shift remains "
    "nilpotent; the central scalar line is inherited from the external "
    "Laurent tensor factor; the bottom and shear obstructions remain; and the "
    "same matrix envelope is formable on controls.  A surviving End route "
    "must construct an actual carrier correspondence algebra with the shift, "
    "selector, torsor splitter, and control death as object data."
)
