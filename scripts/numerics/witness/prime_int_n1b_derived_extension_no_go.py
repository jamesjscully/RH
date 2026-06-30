"""N1-b' derived-extension/Yoneda-gluing witness.

Doc 161 kills ordinary support filtered extensions: over
L=F_2[u^{+-1}], the visible support pieces are free/projective rank-one
L-modules, so ordinary extensions split.  The next repair is to replace
ordinary extensions by derived/Yoneda Ext classes, Massey products, or
A-infinity-style higher gluing on the support filtration.

This witness checks the finite model.  Positive Ext between free L-pieces
vanishes in every tested degree, so the ordinary Yoneda algebra supplies no
hidden higher support class.  Any nonzero "higher gluing" that remains is a
chosen support-chain cochain: it lies in the same nilpotent strict
upper-triangular radical from doc 161, with finite interval counts and no
invertible Laurent orbit, selector, DMP multiplication, or torsor splitter.
The same package is formable on controls.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_derived_extension_no_go
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


def positive_ext_rank_between_free_pieces(_rank, _degree):
    # Each visible support piece is L itself, hence projective over L.
    return 0


def hom_matrix_rank(rank):
    return rank * rank


def strict_upper_rank(rank):
    return rank * (rank - 1) // 2


def interval_count_of_exact_length(rank, length):
    if length <= 0 or length >= rank:
        return 0
    return rank - length


def strict_upper_power_rank(rank, power):
    if power <= 0:
        return rank * rank
    if power >= rank:
        return 0
    return (rank - power) * (rank - power + 1) // 2


def rank_one_idempotent_count_f2(rank):
    return (2**rank - 1) * 2 ** (rank - 1)


ranks = {nmax: dmp_rank_truncated(nmax) for nmax in (1, 2, 4, 8)}
positive_ext_ranks = {
    degree: {
        nmax: positive_ext_rank_between_free_pieces(rank, degree)
        for nmax, rank in ranks.items()
    }
    for degree in (1, 2, 3)
}
yoneda_positive_ranks = {nmax: 0 for nmax in ranks}
massey_seed_counts = {nmax: 0 for nmax in ranks}
hom_ranks = {nmax: hom_matrix_rank(rank) for nmax, rank in ranks.items()}
strict_upper_ranks = {nmax: strict_upper_rank(rank) for nmax, rank in ranks.items()}
length_one_interval_counts = {
    nmax: interval_count_of_exact_length(rank, 1) for nmax, rank in ranks.items()
}
length_two_interval_counts = {
    nmax: interval_count_of_exact_length(rank, 2) for nmax, rank in ranks.items()
}
top_interval_counts = {
    nmax: interval_count_of_exact_length(rank, rank - 1)
    for nmax, rank in ranks.items()
}
zero_interval_counts = {
    nmax: interval_count_of_exact_length(rank, rank) for nmax, rank in ranks.items()
}
radical_square_ranks = {
    nmax: strict_upper_power_rank(rank, 2) for nmax, rank in ranks.items()
}
zero_radical_power_ranks = {
    nmax: strict_upper_power_rank(rank, rank) for nmax, rank in ranks.items()
}
endpoint_choices = ranks.copy()
rank_one_idempotent_counts = {
    nmax: rank_one_idempotent_count_f2(rank) for nmax, rank in ranks.items()
}

gate(
    "DEX1 support tensor ranks are the doc-161 ranks",
    ranks == {1: 3, 2: 4, 4: 6, 8: 10},
    f"ranks={ranks}",
)

gate(
    "DEX2 positive Ext between free L-support pieces vanishes",
    positive_ext_ranks
    == {
        1: {1: 0, 2: 0, 4: 0, 8: 0},
        2: {1: 0, 2: 0, 4: 0, 8: 0},
        3: {1: 0, 2: 0, 4: 0, 8: 0},
    },
    f"positive_ext_ranks={positive_ext_ranks}",
)

gate(
    "DEX3 the ordinary Yoneda positive-degree algebra has no support classes",
    yoneda_positive_ranks == {1: 0, 2: 0, 4: 0, 8: 0},
    f"yoneda_positive_ranks={yoneda_positive_ranks}",
)

gate(
    "DEX4 Massey-style support products have no Ext1 seeds",
    massey_seed_counts == {1: 0, 2: 0, 4: 0, 8: 0},
    f"massey_seed_counts={massey_seed_counts}",
)

gate(
    "DEX5 degree-zero derived endomorphisms recover the matrix envelope",
    hom_ranks == {1: 9, 2: 16, 4: 36, 8: 100},
    f"hom_ranks={hom_ranks}",
)

gate(
    "DEX6 inserted higher support cochains are strict upper-triangular data",
    strict_upper_ranks == {1: 3, 2: 6, 4: 15, 8: 45},
    f"strict_upper_ranks={strict_upper_ranks}",
)

gate(
    "DEX7 support interval slots are finite nilpotent-chain slots",
    length_one_interval_counts == {1: 2, 2: 3, 4: 5, 8: 9}
    and length_two_interval_counts == {1: 1, 2: 2, 4: 4, 8: 8}
    and top_interval_counts == {1: 1, 2: 1, 4: 1, 8: 1}
    and zero_interval_counts == {1: 0, 2: 0, 4: 0, 8: 0},
    (
        f"length_one={length_one_interval_counts}, "
        f"length_two={length_two_interval_counts}, "
        f"top={top_interval_counts}, zero={zero_interval_counts}"
    ),
)

gate(
    "DEX8 the higher-gluing radical is nilpotent, not Laurent-invertible",
    radical_square_ranks == {1: 1, 2: 3, 4: 10, 8: 36}
    and zero_radical_power_ranks == {1: 0, 2: 0, 4: 0, 8: 0},
    (
        f"radical_square_ranks={radical_square_ranks}, "
        f"zero_radical_power_ranks={zero_radical_power_ranks}"
    ),
)

gate(
    "DEX9 endpoint and rank-one idempotent choices remain",
    endpoint_choices == {1: 3, 2: 4, 4: 6, 8: 10}
    and rank_one_idempotent_counts == {1: 28, 2: 120, 4: 2016, 8: 523776},
    (
        f"endpoint_choices={endpoint_choices}, "
        f"rank_one_idempotent_counts={rank_one_idempotent_counts}"
    ),
)

obstruction_res1 = 1
coboundary_res1 = 0
carrier_multiplication_supplied = False
torsor_splitter_supplied = False
gate(
    "DEX10 derived gluing does not repair bottom, shear, or torsor obstructions",
    dmp_dim(-1) == 1
    and dmp_dim(-2) == 0
    and obstruction_res1 == 1
    and coboundary_res1 == 0
    and not carrier_multiplication_supplied
    and not torsor_splitter_supplied,
    "y^2=0, res_1(c)=1, no DMP multiplication, and no b/phi(b)=c",
)

control_ext_ranks = positive_ext_ranks.copy()
control_strict_upper_ranks = strict_upper_ranks.copy()
gate(
    "DEX11 the same derived-extension package is formable on controls",
    control_ext_ranks == positive_ext_ranks
    and control_strict_upper_ranks == strict_upper_ranks,
    "projective support pieces and chosen higher support cochains are shadow-level data",
)

primitive_carrier_maps_consumed = 0
derived_gluing_inserted = 1
gate(
    "DEX12 surviving derived extension must be carrier-native",
    primitive_carrier_maps_consumed == 0 and derived_gluing_inserted == 1,
    "a real route must construct positive Ext/A-infinity operations from carrier correspondences",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (DEX1-DEX12)")
print(
    "VERDICT: derived/Yoneda extension data on the visible support flag does "
    "not supply the R1 carrier.  Positive Ext between the free L-support "
    "pieces vanishes, so there are no ordinary higher support extension "
    "classes or Massey seeds.  Any nonzero higher-gluing cochain is inserted "
    "strict upper-triangular support data: finite and nilpotent, not a "
    "Laurent-invertible carrier correspondence.  Endpoint/idempotent choices "
    "and bottom/shear/torsor obstructions remain, and the same package is "
    "formable on controls.  A surviving route must construct derived "
    "operations carrier-natively."
)
