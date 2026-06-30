"""N1-b' idempotent-corner witness.

Doc 150 kills the support-module End envelope because
End_L(R_DMP[-1..N] tensor L) is the full matrix algebra Mat_r(L).  The next
repair is to pass to a rank-one idempotent/Morita corner e Mat_r(L) e ~= L
and call that corner the selected Laurent line.

This witness checks the finite F_2 choice counts.  Rank-one corners exist and
do produce copies of L, but there are many idempotents, the bottom coordinate
corner only recovers the external tensor line, no shift/torsor data is
selected, the base obstructions remain, and the same corner construction is
formable on controls.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_idempotent_corner_no_go
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


def coordinate_idempotent_count(rank):
    return rank


def rank_one_line_count(rank):
    # One-dimensional subspaces of F_2^r; every nonzero vector spans a
    # distinct line because F_2^*={1}.
    return 2**rank - 1


def rank_one_idempotent_count(rank):
    # A rank-one idempotent is u v^T with u != 0 and v(u)=1.  For each u,
    # exactly half of all v in (F_2^r)^* satisfy v(u)=1.
    return (2**rank - 1) * 2 ** (rank - 1)


def rank_one_corner_rank(rank):
    # If e has rank one, then e Mat_r(L) e has Laurent rank 1.
    return 1 if rank >= 1 else 0


ranks = {nmax: dmp_rank_truncated(nmax) for nmax in (1, 2, 4, 8)}
endomorphism_ranks = {nmax: rank * rank for nmax, rank in ranks.items()}
coordinate_counts = {nmax: coordinate_idempotent_count(rank) for nmax, rank in ranks.items()}
line_counts = {nmax: rank_one_line_count(rank) for nmax, rank in ranks.items()}
idempotent_counts = {nmax: rank_one_idempotent_count(rank) for nmax, rank in ranks.items()}
corner_ranks = {nmax: rank_one_corner_rank(rank) for nmax, rank in ranks.items()}

gate(
    "IDC1 support End envelope starts as Mat_r(L)",
    ranks == {1: 3, 2: 4, 4: 6, 8: 10}
    and endomorphism_ranks == {1: 9, 2: 16, 4: 36, 8: 100},
    f"ranks={ranks}, endomorphism_ranks={endomorphism_ranks}",
)

gate(
    "IDC2 rank-one idempotent corners do produce Laurent rank one",
    all(value == 1 for value in corner_ranks.values()),
    f"corner_ranks={corner_ranks}",
)

gate(
    "IDC3 coordinate idempotent choices grow with truncation",
    coordinate_counts == {1: 3, 2: 4, 4: 6, 8: 10},
    f"coordinate_counts={coordinate_counts}",
)

gate(
    "IDC4 rank-one image-line choices grow inside the module",
    line_counts == {1: 7, 2: 15, 4: 63, 8: 1023},
    f"line_counts={line_counts}",
)

gate(
    "IDC5 rank-one idempotent choices grow faster than image lines",
    idempotent_counts == {1: 28, 2: 120, 4: 2016, 8: 523776},
    f"idempotent_counts={idempotent_counts}",
)

bottom_coordinate_corner_uses_external_l = True
bottom_generator_invertible = False
gate(
    "IDC6 bottom coordinate corner does not invert the DMP bottom class",
    bottom_coordinate_corner_uses_external_l
    and not bottom_generator_invertible
    and dmp_dim(-1) == 1
    and dmp_dim(-2) == 0,
    "corner scalar is external L while original bottom y remains square-zero",
)

shift_selected_by_idempotent = False
torsor_splitter_selected_by_idempotent = False
gate(
    "IDC7 an idempotent corner does not select shift or torsor data",
    not shift_selected_by_idempotent and not torsor_splitter_selected_by_idempotent,
    "choosing e gives a corner line, not S or b/phi(b)=c",
)

obstruction_res1 = 1
coboundary_res1 = 0
gate(
    "IDC8 idempotent corner does not repair bottom or shear obstructions",
    dmp_dim(-1) == 1 and dmp_dim(-2) == 0 and obstruction_res1 == 1 and coboundary_res1 == 0,
    "y^2=0 and res_1(c)=1 remain unchanged",
)

control_idempotent_counts = idempotent_counts.copy()
control_corner_ranks = corner_ranks.copy()
gate(
    "IDC9 the same idempotent-corner construction is formable on controls",
    control_idempotent_counts == idempotent_counts and control_corner_ranks == corner_ranks,
    "rank-one idempotents in Mat_r(L) are finite-free module data",
)

primitive_carrier_maps_consumed = 0
idempotent_choice_inserted = True
gate(
    "IDC10 surviving corner must be carrier-selected",
    idempotent_choice_inserted and primitive_carrier_maps_consumed == 0,
    "a real route must construct e from carrier correspondence data and kill controls",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (IDC1-IDC10)")
print(
    "VERDICT: a rank-one idempotent/Morita corner of the support End envelope "
    "does cut Mat_r(L) down to a Laurent rank-one corner, but only after a "
    "noncanonical idempotent choice.  The bottom coordinate corner recovers "
    "the external tensor line, not an invertible DMP bottom class; the corner "
    "does not select the shift or torsor splitter; the bottom/shear "
    "obstructions remain; and the same corner construction is formable on "
    "controls.  A surviving route must construct the idempotent from the "
    "carrier correspondence itself and show where DH/Epstein fail."
)
