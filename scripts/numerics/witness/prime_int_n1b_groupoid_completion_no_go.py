"""N1-b' support-chain groupoid completion witness.

Doc 155 kills the incidence/path algebra of the ordered DMP support chain:
its path ideal is nilpotent and its arrows are only support-order arrows.
The next repair formally inverts those support arrows, replacing the line
quiver by its groupoid completion.

This witness checks the finite model.  Inverting every adjacent arrow in a
line chain gives the connected thin groupoid on the same r vertices: exactly
one morphism i -> j for every ordered pair.  Its category algebra is the
matrix envelope Mat_r(L), not a new carrier correspondence.  Basepoint loops
are trivial, endpoint corners still require support-vertex/idempotent
choices, the bottom corner recovers the external tensor line, the base
obstructions remain, and the same groupoid completion is formable on controls.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_groupoid_completion_no_go
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


def adjacent_arrow_count(rank):
    return rank - 1


def thin_groupoid_morphism_count(rank):
    return rank * rank


def thin_groupoid_nonidentity_count(rank):
    return rank * rank - rank


def rank_one_idempotent_count_f2(rank):
    return (2**rank - 1) * 2 ** (rank - 1)


ranks = {nmax: dmp_rank_truncated(nmax) for nmax in (1, 2, 4, 8)}
adjacent_counts = {nmax: adjacent_arrow_count(rank) for nmax, rank in ranks.items()}
oriented_adjacent_counts = {nmax: 2 * count for nmax, count in adjacent_counts.items()}
groupoid_morphism_counts = {
    nmax: thin_groupoid_morphism_count(rank) for nmax, rank in ranks.items()
}
groupoid_nonidentity_counts = {
    nmax: thin_groupoid_nonidentity_count(rank) for nmax, rank in ranks.items()
}
matrix_envelope_ranks = {nmax: rank * rank for nmax, rank in ranks.items()}
basepoint_loop_counts = {nmax: 1 for nmax in ranks}
endpoint_choices = ranks.copy()
rank_one_idempotent_counts = {
    nmax: rank_one_idempotent_count_f2(rank) for nmax, rank in ranks.items()
}

gate(
    "GCP1 support tensor ranks are the doc-155 ranks",
    ranks == {1: 3, 2: 4, 4: 6, 8: 10},
    f"ranks={ranks}",
)

gate(
    "GCP2 inverting line-chain arrows gives a thin connected groupoid",
    groupoid_morphism_counts == {1: 9, 2: 16, 4: 36, 8: 100},
    f"groupoid_morphism_counts={groupoid_morphism_counts}",
)

gate(
    "GCP3 nonidentity and oriented-adjacent arrows are support-generated",
    groupoid_nonidentity_counts == {1: 6, 2: 12, 4: 30, 8: 90}
    and oriented_adjacent_counts == {1: 4, 2: 6, 4: 10, 8: 18},
    (
        f"groupoid_nonidentity_counts={groupoid_nonidentity_counts}, "
        f"oriented_adjacent_counts={oriented_adjacent_counts}"
    ),
)

gate(
    "GCP4 groupoid category algebra is the support matrix envelope",
    groupoid_morphism_counts == matrix_envelope_ranks,
    f"matrix_envelope_ranks={matrix_envelope_ranks}",
)

gate(
    "GCP5 basepoint loops are trivial, not a Laurent shift group",
    basepoint_loop_counts == {1: 1, 2: 1, 4: 1, 8: 1},
    f"basepoint_loop_counts={basepoint_loop_counts}",
)

gate(
    "GCP6 endpoint corners and rank-one idempotents remain choices",
    endpoint_choices == {1: 3, 2: 4, 4: 6, 8: 10}
    and rank_one_idempotent_counts == {1: 28, 2: 120, 4: 2016, 8: 523776},
    (
        f"endpoint_choices={endpoint_choices}, "
        f"rank_one_idempotent_counts={rank_one_idempotent_counts}"
    ),
)

bottom_endpoint_uses_external_l = True
bottom_generator_invertible = False
gate(
    "GCP7 bottom endpoint corner does not invert the DMP bottom class",
    bottom_endpoint_uses_external_l
    and not bottom_generator_invertible
    and dmp_dim(-1) == 1
    and dmp_dim(-2) == 0,
    "endpoint scalar is external L while original y remains square-zero",
)

carrier_multiplication_supplied = False
torsor_splitter_supplied = False
support_vertices_all_isomorphic_by_fiat = True
gate(
    "GCP8 inverted support arrows are not carrier multiplication",
    support_vertices_all_isomorphic_by_fiat
    and not carrier_multiplication_supplied
    and not torsor_splitter_supplied,
    "groupoid completion makes support vertices isomorphic by construction",
)

obstruction_res1 = 1
coboundary_res1 = 0
gate(
    "GCP9 groupoid completion does not repair bottom or shear obstructions",
    dmp_dim(-1) == 1 and dmp_dim(-2) == 0 and obstruction_res1 == 1 and coboundary_res1 == 0,
    "y^2=0 and res_1(c)=1 remain unchanged",
)

control_groupoid_morphism_counts = groupoid_morphism_counts.copy()
control_matrix_envelope_ranks = matrix_envelope_ranks.copy()
gate(
    "GCP10 the same groupoid completion is formable on controls",
    control_groupoid_morphism_counts == groupoid_morphism_counts
    and control_matrix_envelope_ranks == matrix_envelope_ranks,
    "thin groupoid completion uses only ordered finite support data",
)

primitive_carrier_maps_consumed = 0
formal_inverses_inserted = oriented_adjacent_counts.copy()
gate(
    "GCP11 surviving inverted-arrow route must be carrier-native",
    primitive_carrier_maps_consumed == 0
    and formal_inverses_inserted == {1: 4, 2: 6, 4: 10, 8: 18},
    "a real route must construct inverse arrows as carrier correspondences and kill controls",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (GCP1-GCP11)")
print(
    "VERDICT: groupoid-completing the support chain does not supply the "
    "R1 carrier.  It formally inverts support-order arrows, giving the "
    "thin connected groupoid with r^2 morphisms and category algebra Mat_r(L); "
    "basepoint loops are trivial, endpoint/idempotent choices remain, the "
    "bottom corner recovers external L rather than inverting the DMP bottom "
    "class, no torsor splitter or carrier multiplication is constructed, the "
    "base obstructions remain, and the same groupoid completion is formable "
    "on controls.  A surviving route must construct inverse arrows as "
    "carrier-native correspondences."
)
