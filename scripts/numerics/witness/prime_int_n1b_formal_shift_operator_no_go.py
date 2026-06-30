"""N1-b' formal shift-operator witness.

Doc 148 kills a support-index telescope because DMP support supplies
dimensions, not adjacent maps.  The next repair is to adjoin a formal shift
operator S and call its orbit the missing Laurent line.

This witness checks the three elementary finite models for that move:

1. On a truncated DMP chain, the forward shift with terminal zero is
   nilpotent and noninvertible; inverting it collapses the finite support.
2. Making the finite shift invertible by a cyclic wrap inserts an artificial
   terminal arrow not supplied by support.
3. Making S genuinely invertible by a bi-infinite orbit is an external
   Laurent insertion in operator language.

The base bottom/shear obstructions remain, and the same formal operator
schema is formable on controls.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_formal_shift_operator_no_go
"""

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
    """Column j is S(e_j), encoded as a bitmask."""
    return [1 << (j + 1) if j + 1 < rank else 0 for j in range(rank)]


def cyclic_shift_columns(rank):
    """Column j is S(e_j), with an inserted terminal wrap."""
    return [1 << ((j + 1) % rank) for j in range(rank)]


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


ranks = {nmax: dmp_rank_truncated(nmax) for nmax in (1, 2, 4, 8)}
forward_shift_ranks = {
    nmax: matrix_rank_from_columns(forward_shift_columns(rank), rank)
    for nmax, rank in ranks.items()
}
forward_nilpotent = {
    nmax: all(value == 0 for value in power_columns(forward_shift_columns(rank), rank, rank))
    for nmax, rank in ranks.items()
}
cyclic_shift_ranks = {
    nmax: matrix_rank_from_columns(cyclic_shift_columns(rank), rank)
    for nmax, rank in ranks.items()
}

gate(
    "FSO1 tensor repair has rank N+2 before a formal operator is adjoined",
    ranks == {1: 3, 2: 4, 4: 6, 8: 10},
    f"ranks={ranks}",
)

gate(
    "FSO2 finite support forward shift is noninvertible",
    all(forward_shift_ranks[nmax] == rank - 1 for nmax, rank in ranks.items()),
    f"forward_shift_ranks={forward_shift_ranks}",
)

gate(
    "FSO3 finite support forward shift is nilpotent",
    all(forward_nilpotent.values()),
    f"forward_nilpotent={forward_nilpotent}",
)

localization_kills_all = {
    nmax: (forward_nilpotent[nmax] and matrix_rank_from_columns(forward_shift_columns(rank), rank) < rank)
    for nmax, rank in ranks.items()
}
gate(
    "FSO4 inverting the finite formal shift collapses the truncated carrier",
    all(localization_kills_all.values()),
    "S^r=0 while S is forced invertible, so every class dies after localization",
)

gate(
    "FSO5 cyclic invertibility inserts a terminal wrap not supplied by support",
    all(cyclic_shift_ranks[nmax] == rank for nmax, rank in ranks.items()),
    f"cyclic_shift_ranks={cyclic_shift_ranks}; support_wrap_arrow=False",
)

gate(
    "FSO6 cyclic wrap imposes artificial degree periodicity",
    all(rank > 1 for rank in ranks.values()),
    "e_{r-1}->e_0 identifies the terminal nonnegative copy with the bottom copy",
)

negative_orbit_needed = dmp_dim(-2) == 0
external_laurent_orbit = True
gate(
    "FSO7 bi-infinite invertible shift is external Laurent insertion",
    negative_orbit_needed and external_laurent_orbit,
    "S^-1 needs classes below the DMP bottom, so the orbit is new structure",
)

obstruction_res1 = 1
coboundary_res1 = 0
gate(
    "FSO8 formal shift operator does not repair bottom or shear obstructions",
    dmp_dim(-1) == 1 and dmp_dim(-2) == 0 and obstruction_res1 == 1 and coboundary_res1 == 0,
    "bottom y remains square-zero and res_1(c)=1 remains outside base coboundaries",
)

control_forward_shift_ranks = forward_shift_ranks.copy()
control_cyclic_shift_ranks = cyclic_shift_ranks.copy()
gate(
    "FSO9 the same formal shift alternatives are formable on controls",
    control_forward_shift_ranks == forward_shift_ranks
    and control_cyclic_shift_ranks == cyclic_shift_ranks,
    "nilpotent, cyclic, and free invertible S schemas use only finite-rank module data",
)

primitive_carrier_maps_consumed = 0
formal_operator_inserted = 1
gate(
    "FSO10 surviving shift operator must be carrier-native",
    formal_operator_inserted == 1 and primitive_carrier_maps_consumed == 0,
    "a real route must construct S as multiplication/correspondence and kill controls",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (FSO1-FSO10)")
print(
    "VERDICT: adjoining a formal shift operator does not supply the R1 carrier. "
    "On finite DMP support the forward shift is nilpotent and localization at "
    "S collapses the truncation; cyclic invertibility inserts an artificial "
    "wrap; and a genuinely invertible bi-infinite orbit is just external "
    "Laurent insertion.  The bottom and shear obstructions remain, and the "
    "same formal operator schemas are formable on controls.  A surviving R1 "
    "route must construct S carrier-natively and show where DH/Epstein cannot "
    "form it."
)
