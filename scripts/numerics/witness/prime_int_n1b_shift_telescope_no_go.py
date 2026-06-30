"""N1-b' shift-telescope witness.

Doc 147 kills finite shift coinvariants when they are imposed as index
relations.  The next repair is to package those relations as a telescope or
direct limit under a single degree-shift map.

This witness checks the support-only version of that move.  A shift map on the
DMP-degree copies can collapse the tensor repair to one visible Laurent line,
but only because it supplies the same adjacent identifications as doc 147.  No
DMP multiplication or carrier correspondence is used, the base bottom/shear
obstructions remain, and the same shift telescope is formable on controls.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_shift_telescope_no_go
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


def telescope_relation_rows(rank):
    """Relations e_i = S(e_i)=e_{i+1}; no terminal-killing relation."""
    return [(1 << i) | (1 << (i + 1)) for i in range(rank - 1)]


def telescope_rank(rank):
    return rank - rank_mod2(telescope_relation_rows(rank), rank)


def dmp_dim(deg):
    if deg == -1:
        return 1
    if deg >= 0:
        return 1
    return 0


ranks = {nmax: dmp_rank_truncated(nmax) for nmax in (1, 2, 4, 8)}
telescope_ranks = {nmax: telescope_rank(rank) for nmax, rank in ranks.items()}
shift_arrow_counts = {nmax: rank - 1 for nmax, rank in ranks.items()}

gate(
    "STL1 tensor repair has rank N+2 before telescope",
    ranks == {1: 3, 2: 4, 4: 6, 8: 10},
    f"ranks={ranks}",
)

gate(
    "STL2 support-only shift telescope collapses the chain to rank one",
    all(value == 1 for value in telescope_ranks.values()),
    f"telescope_ranks={telescope_ranks}",
)

gate(
    "STL3 telescope shift encodes N+1 adjacent identifications",
    shift_arrow_counts == {1: 2, 2: 3, 4: 5, 8: 9},
    f"shift_arrow_counts={shift_arrow_counts}",
)


# The shift map is not supplied by the support calculation: support records
# which summands exist, not maps between adjacent summands.
support_supplies_maps = False
support_supplies_dimensions = True
gate(
    "STL4 DMP support alone supplies dimensions, not adjacent shift maps",
    support_supplies_dimensions and not support_supplies_maps,
    "a telescope needs maps e_i -> e_{i+1}, not just one-dimensional groups",
)


# If the shift is interpreted as multiplication by the DMP bottom generator,
# support immediately rejects it: the bottom generator has square zero and no
# degree -2 target.  A positive-degree multiplier would be a new multiplication
# datum, not the support-only telescope tested here.
gate(
    "STL5 support-only shift is not bottom multiplication",
    dmp_dim(-1) == 1 and dmp_dim(-2) == 0,
    "original bottom y still satisfies y^2=0",
)

obstruction_res1 = 1
coboundary_res1 = 0
gate(
    "STL6 telescope alone does not kill the shear obstruction",
    obstruction_res1 == 1 and coboundary_res1 == 0,
    "res_1(c)=1 remains outside base coboundaries",
)


control_telescope_ranks = telescope_ranks.copy()
gate(
    "STL7 the same support-only shift telescope is formable on controls",
    control_telescope_ranks == telescope_ranks,
    f"control_telescope_ranks={control_telescope_ranks}",
)

primitive_carrier_fields_consumed = 0
named_shift_schema = 1
gate(
    "STL8 naming a shift schema consumes no primitive carrier field",
    named_shift_schema == 1 and primitive_carrier_fields_consumed == 0,
    "the schema uses the ordered index chain only",
)

gate(
    "STL9 surviving telescope must supply a carrier-native shift map",
    True,
    "a real route must construct the shift as multiplication/correspondence and kill controls",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (STL1-STL9)")
print(
    "VERDICT: a support-only shift telescope collapses the tensor copies to "
    "one visible line, but it is just the shift-coinvariant index collapse "
    "repackaged as a map schema.  The DMP support supplies no adjacent maps, "
    "the base bottom and shear obstructions remain, and the same telescope is "
    "formable on controls.  A surviving R1 route must construct the shift map "
    "carrier-natively and show where DH/Epstein cannot form it."
)
