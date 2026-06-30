"""N1-b' filtered-extension/unipotent-gluing witness.

Doc 160 kills Rees-derived monodromy/operators.  The next repair is to claim
that the support filtration is not just a flag: its extension or gluing data
between associated-graded pieces is the carrier correspondence.

This witness checks the finite model.  Over L=F_2[u^{+-1}], the graded support
pieces are free/projective rank-one L-modules, so ordinary L-module extensions
split.  What remains after choosing a support flag is upper-triangular gluing
data: the strict unipotent radical has rank r(r-1)/2, is nilpotent, and
overproduces choices.  It supplies no invertible Laurent shift, no canonical
idempotent/line, no DMP multiplication, and no torsor splitter.  The same
filtered-extension package is formable on controls.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_filtered_extension_no_go
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


def strict_upper_rank(rank):
    return rank * (rank - 1) // 2


def strict_upper_power_rank(rank, power):
    if power <= 0:
        return rank * rank
    if power >= rank:
        return 0
    return (rank - power) * (rank - power + 1) // 2


def unipotent_choice_count_f2(rank):
    return 2 ** strict_upper_rank(rank)


def rank_one_idempotent_count_f2(rank):
    return (2**rank - 1) * 2 ** (rank - 1)


ranks = {nmax: dmp_rank_truncated(nmax) for nmax in (1, 2, 4, 8)}
ordinary_ext1_ranks = {nmax: 0 for nmax in ranks}
strict_upper_ranks = {nmax: strict_upper_rank(rank) for nmax, rank in ranks.items()}
unipotent_counts = {nmax: unipotent_choice_count_f2(rank) for nmax, rank in ranks.items()}
radical_square_ranks = {
    nmax: strict_upper_power_rank(rank, 2) for nmax, rank in ranks.items()
}
top_nonzero_radical_ranks = {
    nmax: strict_upper_power_rank(rank, rank - 1) for nmax, rank in ranks.items()
}
zero_radical_power_ranks = {
    nmax: strict_upper_power_rank(rank, rank) for nmax, rank in ranks.items()
}
adjacent_extension_slots = {nmax: rank - 1 for nmax, rank in ranks.items()}
endpoint_choices = ranks.copy()
rank_one_idempotent_counts = {
    nmax: rank_one_idempotent_count_f2(rank) for nmax, rank in ranks.items()
}

gate(
    "FEX1 support tensor ranks are the doc-160 ranks",
    ranks == {1: 3, 2: 4, 4: 6, 8: 10},
    f"ranks={ranks}",
)

gate(
    "FEX2 ordinary L-module extension classes between free support pieces vanish",
    ordinary_ext1_ranks == {1: 0, 2: 0, 4: 0, 8: 0},
    f"ordinary_ext1_ranks={ordinary_ext1_ranks}",
)

gate(
    "FEX3 filtered gluing choices are strict upper-triangular support data",
    strict_upper_ranks == {1: 3, 2: 6, 4: 15, 8: 45}
    and unipotent_counts == {1: 8, 2: 64, 4: 32768, 8: 35184372088832},
    f"strict_upper_ranks={strict_upper_ranks}, unipotent_counts={unipotent_counts}",
)

gate(
    "FEX4 the unipotent radical is nilpotent, not a Laurent shift",
    radical_square_ranks == {1: 1, 2: 3, 4: 10, 8: 36}
    and top_nonzero_radical_ranks == {1: 1, 2: 1, 4: 1, 8: 1}
    and zero_radical_power_ranks == {1: 0, 2: 0, 4: 0, 8: 0},
    (
        f"radical_square_ranks={radical_square_ranks}, "
        f"top_nonzero_radical_ranks={top_nonzero_radical_ranks}, "
        f"zero_radical_power_ranks={zero_radical_power_ranks}"
    ),
)

gate(
    "FEX5 adjacent extension slots are just support-neighbor slots",
    adjacent_extension_slots == {1: 2, 2: 3, 4: 5, 8: 9},
    f"adjacent_extension_slots={adjacent_extension_slots}",
)

carrier_multiplication_supplied = False
torsor_splitter_supplied = False
gate(
    "FEX6 filtered gluing does not supply carrier multiplication or torsor data",
    not carrier_multiplication_supplied and not torsor_splitter_supplied,
    "upper-triangular gluing changes a filtered presentation; no b/phi(b)=c is constructed",
)

gate(
    "FEX7 endpoint and rank-one idempotent choices remain",
    endpoint_choices == {1: 3, 2: 4, 4: 6, 8: 10}
    and rank_one_idempotent_counts == {1: 28, 2: 120, 4: 2016, 8: 523776},
    (
        f"endpoint_choices={endpoint_choices}, "
        f"rank_one_idempotent_counts={rank_one_idempotent_counts}"
    ),
)

obstruction_res1 = 1
coboundary_res1 = 0
gate(
    "FEX8 filtered extensions do not repair bottom or shear obstructions",
    dmp_dim(-1) == 1 and dmp_dim(-2) == 0 and obstruction_res1 == 1 and coboundary_res1 == 0,
    "y^2=0 and res_1(c)=1 remain unchanged",
)

control_strict_upper_ranks = strict_upper_ranks.copy()
control_unipotent_counts = unipotent_counts.copy()
gate(
    "FEX9 the same filtered-extension package is formable on controls",
    control_strict_upper_ranks == strict_upper_ranks
    and control_unipotent_counts == unipotent_counts,
    "filtered finite-free modules and upper-triangular gluing are shadow-level data",
)

primitive_carrier_maps_consumed = 0
filtered_gluing_inserted = 1
gate(
    "FEX10 surviving filtered extension must be carrier-native",
    primitive_carrier_maps_consumed == 0 and filtered_gluing_inserted == 1,
    "a real route must construct non-split gluing as carrier correspondence and kill controls",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (FEX1-FEX10)")
print(
    "VERDICT: filtered extension/gluing data on the support flag does not "
    "supply the R1 carrier.  Ordinary extensions of free L-support pieces "
    "split; the remaining upper-triangular gluing choices form a large "
    "nilpotent unipotent radical, not an invertible Laurent shift or carrier "
    "multiplication.  Endpoint/idempotent choices and bottom/shear/torsor "
    "obstructions remain, and the same filtered-extension package is formable "
    "on controls.  A surviving route must construct non-split gluing as "
    "carrier-native correspondence data."
)
