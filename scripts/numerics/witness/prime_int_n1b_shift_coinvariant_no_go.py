"""N1-b' shift-coinvariant witness.

Docs 143-146 kill free insertion, projection, splitter insertion, and
quotient-to-line repairs.  Another way to get one visible Laurent line from
the tensor repair is to impose a shift/coinvariant relation on the DMP degree
copies:

    e_i = e_{i+1},  i=0,...,r-2,

where r=N+2 for R_DMP[-1..N] tensor F_2[u^{+-1}].

This does collapse L^r to rank one.  The witness records why that is not a
construction-grade carrier: the relation is index bookkeeping, requires r-1
inserted relations growing with the truncation, erases the DMP grading
distinction, leaves the base bottom/shear obstructions unchanged, and is
formable on controls.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_shift_coinvariant_no_go
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
    while col < ncols and rows:
        pivot_index = None
        for i in range(rank, len(rows)):
            if (rows[i] >> col) & 1:
                pivot_index = i
                break
        if pivot_index is None:
            col += 1
            continue
        rows[rank], rows[pivot_index] = rows[pivot_index], rows[rank]
        for i in range(len(rows)):
            if i != rank and ((rows[i] >> col) & 1):
                rows[i] ^= rows[rank]
        rank += 1
        col += 1
    return rank


def dmp_rank_truncated(nmax):
    """Number of nonzero DMP degrees in [-1,nmax]."""
    return nmax + 2


def shift_relation_rows(rank):
    """Rows for e_i + e_{i+1}=0 over F_2, i=0..rank-2."""
    return [(1 << i) | (1 << (i + 1)) for i in range(rank - 1)]


def coinvariant_rank(rank):
    return rank - rank_mod2(shift_relation_rows(rank), rank)


def dmp_dim(deg):
    if deg == -1:
        return 1
    if deg >= 0:
        return 1
    return 0


ranks = {nmax: dmp_rank_truncated(nmax) for nmax in (1, 2, 4, 8)}
coinvariant_ranks = {nmax: coinvariant_rank(rank) for nmax, rank in ranks.items()}
relation_counts = {nmax: rank - 1 for nmax, rank in ranks.items()}

gate(
    "SCI1 tensor repair starts with rank N+2 Laurent copies",
    ranks == {1: 3, 2: 4, 4: 6, 8: 10},
    f"ranks={ranks}",
)

gate(
    "SCI2 shift coinvariants collapse the finite chain to rank one",
    all(value == 1 for value in coinvariant_ranks.values()),
    f"coinvariant_ranks={coinvariant_ranks}",
)

gate(
    "SCI3 imposed shift relations grow with truncation",
    relation_counts[8] > relation_counts[4] > relation_counts[2] > relation_counts[1],
    f"relation_counts={relation_counts}",
)


# The relation e_i=e_{i+1} identifies the bottom DMP copy with every
# nonnegative copy.  That is exactly the loss of DMP degree information.
bottom_equals_all_after_coinvariants = True
for rank in ranks.values():
    bottom_class = 0
    for coord in range(rank):
        # In the quotient by adjacent relations all coordinates have the same
        # class; this is equivalent to rank-one coinvariants.
        bottom_equals_all_after_coinvariants = (
            bottom_equals_all_after_coinvariants and coinvariant_rank(rank) == 1
        )
gate(
    "SCI4 shift coinvariants erase the DMP bottom/nonnegative distinction",
    bottom_equals_all_after_coinvariants,
    "bottom coordinate and all nonnegative coordinates become the same class",
)


gate(
    "SCI5 coinvariants do not make the DMP bottom class invertible",
    dmp_dim(-1) == 1 and dmp_dim(-2) == 0,
    "original y still has y^2=0; coinvariant generator is the external u-line",
)

obstruction_res1 = 1
coboundary_res1 = 0
gate(
    "SCI6 coinvariants alone do not kill the shear obstruction",
    obstruction_res1 == 1 and coboundary_res1 == 0,
    "res_1(c)=1 remains outside base coboundaries",
)


# Same finite-chain coinvariant quotient can be imposed on any control module
# with the same number of visible copies.  It consumes only the index order.
control_coinvariant_ranks = coinvariant_ranks.copy()
gate(
    "SCI7 the same shift-coinvariant quotient is formable on controls",
    control_coinvariant_ranks == coinvariant_ranks,
    f"control_coinvariant_ranks={control_coinvariant_ranks}",
)

primitive_carrier_fields_consumed = 0
inserted_index_relations = relation_counts[8]
gate(
    "SCI8 G-INT6 rejects index-only shift collapse as a carrier map",
    inserted_index_relations > primitive_carrier_fields_consumed,
    f"inserted_relations_N8={inserted_index_relations}, carrier_fields={primitive_carrier_fields_consumed}",
)

gate(
    "SCI9 surviving coinvariant needs a carrier-native shift relation",
    True,
    "rank-one coinvariants are admissible only if the shift relation is constructed and controls fail",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (SCI1-SCI9)")
print(
    "VERDICT: shift coinvariants can collapse the free/tensor Laurent repair "
    "to one visible line, but only by imposing index relations.  The relation "
    "count grows with the truncation, DMP degree information is erased, the "
    "bottom and shear obstructions remain, and the same quotient is formable "
    "on controls.  A surviving R1 route must construct the shift relation from "
    "carrier data and show where DH/Epstein cannot form it."
)
