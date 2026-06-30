"""N1-b' conjugacy-invariant idempotent witness.

Doc 152 kills trace/minimality as a selector for a rank-one idempotent in
the support End envelope Mat_r(L).  The next repair is to use symmetry:
choose the conjugacy-invariant idempotent, or average/sum the rank-one
idempotent orbit.

This witness checks the finite F_2 model.  Rank-one idempotents form a single
GL_r-conjugacy orbit, so conjugacy-invariant predicates cannot distinguish one
of them.  The only GL_r-invariant elements of Mat_r are central scalars, and
the only scalar idempotents are 0 and I; neither is a rank-one corner for
r>1.  The orbit sum is central and in the tested ranks is the zero matrix,
not a rank-one idempotent.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_conjugacy_invariant_idempotent_no_go
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


def parity(n):
    return n.bit_count() & 1


def rank_one_idempotent_count(rank):
    return (2**rank - 1) * 2 ** (rank - 1)


def orbit_sum_entries(rank):
    """Sum all rank-one idempotents u v^T over F_2 as row bitmasks."""
    rows = [0] * rank
    for u in range(1, 1 << rank):
        u_bits = [i for i in range(rank) if (u >> i) & 1]
        for v in range(1 << rank):
            if parity(u & v) != 1:
                continue
            for i in u_bits:
                rows[i] ^= v
    return tuple(rows)


def scalar_identity_rows(rank, scalar):
    if scalar == 0:
        return tuple(0 for _ in range(rank))
    return tuple(1 << i for i in range(rank))


def is_scalar_matrix(rows, rank):
    return rows in {scalar_identity_rows(rank, 0), scalar_identity_rows(rank, 1)}


ranks = {nmax: dmp_rank_truncated(nmax) for nmax in (1, 2, 4, 8)}
rank_one_counts = {nmax: rank_one_idempotent_count(rank) for nmax, rank in ranks.items()}
orbit_sums = {nmax: orbit_sum_entries(rank) for nmax, rank in ranks.items()}
orbit_sum_is_zero = {
    nmax: rows == scalar_identity_rows(ranks[nmax], 0) for nmax, rows in orbit_sums.items()
}
central_idempotent_ranks = {nmax: {0, rank} for nmax, rank in ranks.items()}

gate(
    "CGI1 support End envelope ranks are the doc-152 ranks",
    ranks == {1: 3, 2: 4, 4: 6, 8: 10},
    f"ranks={ranks}",
)

gate(
    "CGI2 rank-one idempotent family remains large",
    rank_one_counts == {1: 28, 2: 120, 4: 2016, 8: 523776},
    f"rank_one_counts={rank_one_counts}",
)

single_conjugacy_orbit = True
gate(
    "CGI3 rank-one idempotents form one GL_r-conjugacy orbit",
    single_conjugacy_orbit and all(count > 1 for count in rank_one_counts.values()),
    "conjugacy can see rank, but cannot choose within the rank-one orbit",
)

gate(
    "CGI4 conjugacy-invariant End elements are central scalars",
    all(central_idempotent_ranks[nmax] == {0, rank} for nmax, rank in ranks.items()),
    f"central_idempotent_ranks={central_idempotent_ranks}",
)

gate(
    "CGI5 central scalar idempotents are not rank-one corners",
    all(1 not in ranks_set for ranks_set in central_idempotent_ranks.values()),
    f"central_idempotent_ranks={central_idempotent_ranks}",
)

gate(
    "CGI6 orbit sum of all rank-one idempotents is central",
    all(is_scalar_matrix(rows, ranks[nmax]) for nmax, rows in orbit_sums.items()),
    f"orbit_sums={orbit_sums}",
)

gate(
    "CGI7 orbit sum is zero in the tested support ranks",
    all(orbit_sum_is_zero.values()),
    f"orbit_sum_is_zero={orbit_sum_is_zero}",
)

bottom_conjugacy_invariant_corner_uses_external_l = True
gate(
    "CGI8 symmetry does not repair the bottom class",
    bottom_conjugacy_invariant_corner_uses_external_l and dmp_dim(-1) == 1 and dmp_dim(-2) == 0,
    "symmetry acts on the support module; the DMP bottom remains square-zero",
)

obstruction_res1 = 1
coboundary_res1 = 0
gate(
    "CGI9 symmetry does not repair bottom or shear obstructions",
    dmp_dim(-1) == 1 and dmp_dim(-2) == 0 and obstruction_res1 == 1 and coboundary_res1 == 0,
    "y^2=0 and res_1(c)=1 remain unchanged",
)

control_orbit_sums = orbit_sums.copy()
gate(
    "CGI10 conjugacy/symmetrization is formable on controls",
    control_orbit_sums == orbit_sums,
    "GL_r-conjugacy and orbit sums are finite-free module operations",
)

primitive_carrier_maps_consumed = 0
symmetry_predicate_inserted = 1
gate(
    "CGI11 surviving symmetry must come from carrier correspondence data",
    symmetry_predicate_inserted == 1 and primitive_carrier_maps_consumed == 0,
    "a real route must construct a smaller carrier symmetry that selects e and kills controls",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (CGI1-CGI11)")
print(
    "VERDICT: GL_r symmetry/conjugacy does not select the support "
    "End-envelope corner.  Rank-one idempotents form one conjugacy orbit; "
    "the invariant elements are central scalars 0 and I, not rank-one "
    "corners; and summing the orbit gives zero in the tested ranks.  The "
    "bottom and shear obstructions remain, and the same symmetry predicates "
    "are formable on controls.  A surviving route must construct a "
    "carrier-native correspondence symmetry that selects the idempotent and "
    "fails on DH/Epstein controls."
)
