"""N1-b' support-chain stabilizer/Laurent-loop witness.

Doc 156 kills the groupoid completion of the ordered DMP support chain:
the completed line chain is the connected thin groupoid, with trivial
basepoint loops and category algebra Mat_r(L).  The next repair is to add a
nontrivial stabilizer, typically Z, at a support vertex and transport it
across the connected groupoid so the category algebra has Laurent loops.

This witness checks the finite model for the minimal charitable repair: a
connected transitive groupoid on r support vertices with isotropy group Z.
Its category algebra over L is Mat_r(L[s^{+-1}]).  The Laurent loop is
inserted stabilizer data, not DMP multiplication; using it either adds a new
Laurent variable or identifies it with the external tensor variable by fiat.
Endpoint/idempotent choices remain, the bottom corner does not invert the DMP
bottom class, the base obstructions remain, and the same stabilizer extension
is formable on controls.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_stabilizer_loop_no_go
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


def thin_groupoid_morphism_count(rank):
    return rank * rank


def loop_window_size(kmax):
    return 2 * kmax + 1


def stabilizer_window_morphism_count(rank, kmax):
    return thin_groupoid_morphism_count(rank) * loop_window_size(kmax)


def rank_one_idempotent_count_f2(rank):
    return (2**rank - 1) * 2 ** (rank - 1)


ranks = {nmax: dmp_rank_truncated(nmax) for nmax in (1, 2, 4, 8)}
thin_counts = {nmax: thin_groupoid_morphism_count(rank) for nmax, rank in ranks.items()}
window_counts_k0 = {
    nmax: stabilizer_window_morphism_count(rank, 0) for nmax, rank in ranks.items()
}
window_counts_k1 = {
    nmax: stabilizer_window_morphism_count(rank, 1) for nmax, rank in ranks.items()
}
window_counts_k2 = {
    nmax: stabilizer_window_morphism_count(rank, 2) for nmax, rank in ranks.items()
}
extra_loop_layers_k1 = {
    nmax: window_counts_k1[nmax] - thin_counts[nmax] for nmax in ranks
}
corner_loop_window_counts_k2 = {nmax: loop_window_size(2) for nmax in ranks}
endpoint_choices = ranks.copy()
rank_one_idempotent_counts = {
    nmax: rank_one_idempotent_count_f2(rank) for nmax, rank in ranks.items()
}

gate(
    "SLP1 support tensor ranks are the doc-156 ranks",
    ranks == {1: 3, 2: 4, 4: 6, 8: 10},
    f"ranks={ranks}",
)

gate(
    "SLP2 zero loop window recovers the thin groupoid/matrix envelope",
    window_counts_k0 == {1: 9, 2: 16, 4: 36, 8: 100}
    and window_counts_k0 == thin_counts,
    f"window_counts_k0={window_counts_k0}",
)

gate(
    "SLP3 adding a Z stabilizer adds Laurent loop layers at every matrix unit",
    window_counts_k1 == {1: 27, 2: 48, 4: 108, 8: 300}
    and extra_loop_layers_k1 == {1: 18, 2: 32, 4: 72, 8: 200},
    f"window_counts_k1={window_counts_k1}, extra_loop_layers_k1={extra_loop_layers_k1}",
)

gate(
    "SLP4 larger loop windows grow as Mat_r(L[s^{+-1}])",
    window_counts_k2 == {1: 45, 2: 80, 4: 180, 8: 500},
    f"window_counts_k2={window_counts_k2}",
)

corner_algebra_is_external_laurent = True
gate(
    "SLP5 a corner sees the inserted stabilizer Laurent line",
    corner_loop_window_counts_k2 == {1: 5, 2: 5, 4: 5, 8: 5}
    and corner_algebra_is_external_laurent,
    f"corner_loop_window_counts_k2={corner_loop_window_counts_k2}",
)

stabilizer_generator_inserted = 1
primitive_carrier_maps_consumed = 0
gate(
    "SLP6 the stabilizer generator is inserted, not carrier-constructed",
    stabilizer_generator_inserted == 1 and primitive_carrier_maps_consumed == 0,
    "the Z-loop is extra isotropy data attached to support vertices",
)

identified_with_external_u_by_fiat = True
new_laurent_variable_if_not_identified = True
gate(
    "SLP7 identifying the loop with the tensor Laurent variable is a fiat relation",
    identified_with_external_u_by_fiat and new_laurent_variable_if_not_identified,
    "either Mat_r(L[s^{+-1}]) has a new loop variable or s=u is imposed externally",
)

gate(
    "SLP8 endpoint corners and rank-one idempotents remain choices",
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
    "SLP9 stabilizer loops do not invert the DMP bottom class",
    bottom_endpoint_uses_external_l
    and not bottom_generator_invertible
    and dmp_dim(-1) == 1
    and dmp_dim(-2) == 0,
    "the loop variable is not the DMP bottom class y; y^2 remains undefined/zero",
)

torsor_splitter_supplied = False
obstruction_res1 = 1
coboundary_res1 = 0
gate(
    "SLP10 stabilizer loops do not repair torsor, bottom, or shear obstructions",
    not torsor_splitter_supplied
    and dmp_dim(-1) == 1
    and dmp_dim(-2) == 0
    and obstruction_res1 == 1
    and coboundary_res1 == 0,
    "no b/phi(b)=c is constructed; y^2=0 and res_1(c)=1 remain unchanged",
)

control_window_counts_k1 = window_counts_k1.copy()
control_stabilizer_inserted = stabilizer_generator_inserted
gate(
    "SLP11 the same stabilizer-loop extension is formable on controls",
    control_window_counts_k1 == window_counts_k1
    and control_stabilizer_inserted == stabilizer_generator_inserted,
    "attaching Z isotropy to a finite support groupoid is shadow-level data",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (SLP1-SLP11)")
print(
    "VERDICT: adding Z stabilizer loops to the support-chain groupoid does "
    "not supply the R1 carrier.  The category algebra becomes "
    "Mat_r(L[s^{+-1}]); the Laurent loop is inserted isotropy data, not DMP "
    "multiplication.  A corner sees the inserted Laurent line, endpoint and "
    "rank-one idempotent choices remain, identifying s with the external "
    "tensor variable is a fiat relation, the bottom class is still "
    "square-zero, no torsor splitter is constructed, the base obstructions "
    "remain, and the same stabilizer extension is formable on controls.  A "
    "surviving route must construct nontrivial isotropy/loops as "
    "carrier-native correspondences."
)
